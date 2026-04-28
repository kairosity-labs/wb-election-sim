"""LLMBatchSampler — batched LLM persona generation with verifier feedback.

Loop:
    while len(population) < target_n:
        report = verify(population)                         # gap report
        user_prompt = build_user_prompt(report, batch_size) # tells LLM what gaps to fill
        response = provider.generate(system, user)          # cached system, dynamic user
        new = parse_and_validate(response, ctx)             # strict schema match
        population.extend(new)
        save_batch_artifact(...)

    while not within_tolerance(population) and corrections_run < max_corrections:
        # surgical small batches biased to the largest remaining z-score gaps

The static system prompt (axes + joints + vote tables + news context + schema)
is built once and reused across all batches with provider-side caching.

Each batch's raw response, gap report, and prompt go to disk under
`personas/<set_name>/batches/raw_NN.json` + `reports/batch_NN.{json,md}` so
runs are fully traceable.
"""
from __future__ import annotations

import json
import random
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from ...core.config import PersonaConfig, SimulationContext
from ...core.persona import Persona
from ...providers import make_provider
from ...verifiers import render_md, verify_population
from ..prompts import (
    build_batch_user_prompt,
    build_persona_json_schema,
    build_system_prompt,
    parse_persona_response,
    validate_persona,
)
from ..subset_selection import greedy_subset_selection


class LLMBatchSampler:
    def __init__(
        self,
        ctx: SimulationContext,
        persona_config: PersonaConfig,
        *,
        seed: int | None = None,
    ):
        self.ctx = ctx
        self.config = persona_config
        self.rng = random.Random(seed)

        # LLM config
        self.provider_name = persona_config.get("llm.provider", "anthropic")
        self.model = persona_config.get("llm.model")
        self.reasoning = persona_config.get("llm.reasoning", "medium")
        self.temperature = float(persona_config.get("llm.temperature", 0.7))
        self.max_tokens = int(persona_config.get("llm.max_tokens", 16000))
        self.cache_system = bool(persona_config.get("llm.cache_system_prompt", True))
        # OpenAI-compatible local backends (sglang/vLLM/ollama/llama.cpp/LM Studio):
        # set llm.base_url + llm.api_key in persona_config to redirect.
        self.base_url = persona_config.get("llm.base_url")
        self.api_key = persona_config.get("llm.api_key")
        provider_kwargs = {}
        if self.base_url:
            provider_kwargs["base_url"] = self.base_url
        if self.api_key:
            provider_kwargs["api_key"] = self.api_key
        self.provider = make_provider(self.provider_name, self.model,
                                       **provider_kwargs)

        # Generation config
        self.batch_size = int(persona_config.get("generation.batch_size", 20))
        self.max_correction_batches = int(persona_config.get("generation.max_correction_batches", 3))
        self.vote_field = persona_config.get("vote.field_name", "vote_2019_LS")
        # If True (default), correction phase OVER-generates and we then
        # trim to exactly target_n via greedy chi-sq selection. Yields a
        # better-fit population without exceeding target_n in the output.
        self.trim_to_target = bool(persona_config.get("generation.trim_to_target", True))

        # Verifier knobs (passed through to verify_population)
        self._tol = persona_config.get("verifier.tolerance")
        self._tw = persona_config.get("verifier.tier_weights")

        # Pre-build system prompt (cached at provider level on first call).
        self._system_prompt = build_system_prompt(ctx, persona_config)
        bg_rel = persona_config.get("prompts.batch_guidance", "prompts/batch_guidance.md")
        bg_path = ctx.sim_dir / bg_rel
        self._batch_guidance = bg_path.read_text() if bg_path.exists() else ""

        # Strict structured output (xgrammar via sglang's response_format).
        # Defaults ON for any non-Anthropic provider — eliminates schema drift
        # (wrong category codes, missing narrative, "Thinking Process:" preamble).
        # Override with `llm.use_json_schema: false` in persona_config to disable.
        default_schema = self.provider_name != "anthropic"
        self.use_json_schema = bool(
            persona_config.get("llm.use_json_schema", default_schema)
        )
        self._json_schema = (
            build_persona_json_schema(ctx, self.vote_field, batch_size=self.batch_size)
            if self.use_json_schema else None
        )

        # Per-AC parallelism — dispatch K calls per round so the sglang server
        # can engage continuous batching at >1 in-flight per replica. With 10
        # ACs running concurrently and parallel_calls=2 we hit ~20 in-flight
        # requests across 8 replicas (~2.5 per replica), nearly doubling
        # aggregate decode throughput vs serial-per-AC.
        # Trade-off: parallel batches in the same round share one (stale) gap
        # report — the verifier feedback is slightly less responsive. With
        # strict schema decoding the convergence is still tight.
        self.parallel_calls = max(1, int(
            persona_config.get("generation.parallel_calls", 1)
        ))

        # Artifact directory — populated by attach_artifact_dir().
        self._artifact_dir: Path | None = None
        self._batches_seen = 0
        self._batches_lock = threading.Lock()
        self.usage_total: dict[str, int] = {}
        self.usage_total_lock = threading.Lock()

    def attach_artifact_dir(self, root: Path) -> None:
        self._artifact_dir = Path(root)
        (self._artifact_dir / "batches").mkdir(parents=True, exist_ok=True)
        (self._artifact_dir / "reports").mkdir(parents=True, exist_ok=True)
        (self._artifact_dir / "system_prompt.md").write_text(self._system_prompt)

    # -----------------------------------------------------------------------

    def _round_call(self, *, report, wanted, n_so_far, target_n, correction_phase, K):
        """Dispatch K parallel batches in a thread pool. Returns the combined
        list of valid personas (across all K calls)."""
        if K == 1:
            return self._call_one_batch(
                report=report, batch_size=wanted, n_so_far=n_so_far,
                target_n=target_n, correction_phase=correction_phase,
            )
        out: list[Persona] = []
        with ThreadPoolExecutor(max_workers=K) as ex:
            futures = []
            for i in range(K):
                # Pre-allocate disjoint ID ranges so concurrent batches don't
                # collide on persona id naming. Each call gets `wanted` slots.
                futures.append(ex.submit(
                    self._call_one_batch,
                    report=report, batch_size=wanted,
                    n_so_far=n_so_far + i * wanted,
                    target_n=target_n, correction_phase=correction_phase,
                ))
            for fut in as_completed(futures):
                try:
                    personas = fut.result()
                except Exception as e:
                    print(f"    ! batch raised: {e}")
                    personas = []
                if personas:
                    out.extend(personas)
        return out

    def sample_many(self, n: int) -> list[Persona]:
        existing: list[Persona] = []
        # A locally-served model occasionally produces a fully-malformed
        # batch (wrong canonical codes, missing narrative, etc.) but recovers
        # on the next call. Bailing on the first zero-valid response under-
        # generates by 60-90%. Keep going up to N consecutive zeros before
        # giving up.
        max_zero_streak = int(
            self.config.get("generation.max_consecutive_zero_batches", 3)
        )
        # Initial generation phase
        zero_streak = 0
        while len(existing) < n:
            report = verify_population(self.ctx, existing, tolerance=self._tol,
                                       tier_weights=self._tw)
            self._save_report(report, prefix="batch")
            remaining = n - len(existing)
            # Limit K so total requested ≤ remaining + buffer (over-gen is fine
            # because trim_to_target greedily prunes back to n at the end).
            K = max(1, min(self.parallel_calls,
                           (remaining + self.batch_size - 1) // self.batch_size))
            wanted = self.batch_size if K > 1 else min(self.batch_size, remaining)
            new_personas = self._round_call(
                report=report, wanted=wanted, n_so_far=len(existing),
                target_n=n, correction_phase=False, K=K,
            )
            if not new_personas:
                zero_streak += 1
                if zero_streak >= max_zero_streak:
                    print(f"  ! {zero_streak} consecutive zero-valid rounds; stopping early")
                    break
                print(f"  ! zero-valid round (streak {zero_streak}/{max_zero_streak}); retrying")
                continue
            zero_streak = 0
            existing.extend(new_personas)

        # Correction phase
        zero_streak = 0
        for _ in range(self.max_correction_batches):
            report = verify_population(self.ctx, existing, tolerance=self._tol,
                                       tier_weights=self._tw)
            self._save_report(report, prefix="correction")
            if report.within_tolerance:
                break
            wanted = max(5, self.batch_size // 2)
            # Keep correction phase serial — narrower batches benefit from
            # tight verifier feedback between calls.
            new_personas = self._call_one_batch(
                report=report, batch_size=wanted, n_so_far=len(existing),
                target_n=n, correction_phase=True,
            )
            if not new_personas:
                zero_streak += 1
                if zero_streak >= max_zero_streak:
                    break
                continue
            zero_streak = 0
            existing.extend(new_personas)

        # Greedy trim to exactly target_n if we over-generated.
        if self.trim_to_target and len(existing) > n:
            print(f"\n  Trimming {len(existing)} → {n} via greedy chi-sq subset selection")
            kept, dropped = greedy_subset_selection(
                self.ctx, existing, n,
                tolerance=self._tol, tier_weights=self._tw, verbose=True,
            )
            existing = kept
            if self._artifact_dir:
                # Archive the dropped persona IDs for traceability.
                (self._artifact_dir / "dropped_in_trim.json").write_text(
                    json.dumps([{"id": p.id, "fields": p.fields,
                                 "narrative": p.narrative}
                                for p in dropped], indent=2)
                )

        # Final report
        final = verify_population(self.ctx, existing, tolerance=self._tol,
                                  tier_weights=self._tw)
        if self._artifact_dir:
            (self._artifact_dir / "reports" / "FINAL.md").write_text(render_md(final))
            (self._artifact_dir / "reports" / "FINAL.json").write_text(
                json.dumps(final.to_dict(), indent=2)
            )
            (self._artifact_dir / "usage_total.json").write_text(
                json.dumps({"provider": self.provider_name, "model": self.provider.model,
                            "reasoning": self.reasoning, "batches_run": self._batches_seen,
                            "usage_total": self.usage_total}, indent=2)
            )
        return existing

    def sample_one(self, idx: int) -> Persona:
        # Convenience for parity with RuleBasedSampler; not the intended path.
        ps = self.sample_many(1)
        if not ps:
            raise RuntimeError("LLM sampler returned no personas for sample_one")
        return ps[0]

    # -----------------------------------------------------------------------

    def _call_one_batch(self, *, report, batch_size, n_so_far, target_n, correction_phase):
        # Atomically reserve a unique batch index for artifact filenames + logs.
        # Without this, parallel calls would clobber each other's raw_NNN.json.
        with self._batches_lock:
            batch_idx = self._batches_seen
            self._batches_seen += 1

        user_prompt = build_batch_user_prompt(
            report=report, batch_size=batch_size, target_n=target_n,
            n_so_far=n_so_far, batch_guidance=self._batch_guidance,
            correction_phase=correction_phase,
        )
        kind = "correction" if correction_phase else "batch"
        print(f"  [{kind} {batch_idx}] requesting {batch_size} "
              f"({n_so_far}/{target_n} so far, composite={report.composite_score:.0f})")
        gen_kwargs = dict(
            system=self._system_prompt,
            user=user_prompt,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            reasoning=self.reasoning,
            cache_system=self.cache_system,
        )
        if self._json_schema is not None:
            gen_kwargs["json_schema"] = self._json_schema
        response = self.provider.generate(**gen_kwargs)
        self._save_raw(batch_idx, user_prompt, response, correction_phase)
        with self.usage_total_lock:
            for k, v in (response.usage or {}).items():
                self.usage_total[k] = self.usage_total.get(k, 0) + int(v or 0)

        try:
            parsed = parse_persona_response(response.text)
        except Exception as e:
            print(f"    [{kind} {batch_idx}] ! response parse failed: {e}")
            return []

        valid: list[Persona] = []
        dropped: list[str] = []
        for i, p_dict in enumerate(parsed):
            ok, err = validate_persona(p_dict, self.ctx, self.vote_field)
            if not ok:
                dropped.append(f"#{i}: {err}")
                continue
            persona = Persona(
                id=f"{self.config.set_name}_p{n_so_far + len(valid):04d}",
                fields=p_dict["fields"],
                narrative=p_dict.get("narrative"),
            )
            valid.append(persona)

        usage = response.usage or {}
        print(f"    [{kind} {batch_idx}] kept {len(valid)}/{len(parsed)} valid  "
              f"(input={usage.get('input_tokens', 0)} "
              f"cached={usage.get('cache_read_input_tokens', usage.get('cached_input_tokens', 0))} "
              f"output={usage.get('output_tokens', 0)} "
              f"reasoning={usage.get('reasoning_tokens', 0)})")
        if dropped:
            print(f"    [{kind} {batch_idx}] dropped {len(dropped)}:")
            for d in dropped[:5]:
                print(f"      {d}")
            if len(dropped) > 5:
                print(f"      ... and {len(dropped) - 5} more")
        return valid

    def _save_raw(self, idx: int, user_prompt: str, response, correction: bool) -> None:
        if not self._artifact_dir:
            return
        kind = "correction" if correction else "batch"
        raw = {
            "kind": kind,
            "provider": self.provider_name,
            "model": self.provider.model,
            "reasoning": self.reasoning,
            "user_prompt": user_prompt,
            "response_text": response.text,
            "thinking": response.thinking,
            "usage": response.usage,
        }
        (self._artifact_dir / "batches" / f"raw_{idx:03d}.json").write_text(
            json.dumps(raw, indent=2)
        )

    def _save_report(self, report, prefix: str) -> None:
        if not self._artifact_dir:
            return
        idx = self._batches_seen
        (self._artifact_dir / "reports" / f"{prefix}_{idx:03d}.json").write_text(
            json.dumps(report.to_dict(), indent=2)
        )
        (self._artifact_dir / "reports" / f"{prefix}_{idx:03d}.md").write_text(
            render_md(report)
        )
