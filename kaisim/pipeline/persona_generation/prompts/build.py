"""Prompt builder — compose system + per-batch user prompts for the LLM sampler.

System prompt (cacheable, ~constant per run):
    1. Region-specific narrative anchors      (simulations/<sim>/prompts/system_anchors.md)
    2. Persona coherence rules                 (simulations/<sim>/prompts/persona_rules.md)
    3. Pre-period opinion context              (simulations/<sim>/news/<news_context_file>)
    4. Demographic axes (canonical codes + marginals)
    5. Joint targets summary
    6. Vote prior tables + aggregate calibration target
    7. Output schema spec (JSON shape + narrative format)
    8. Generation rules (no narrative leakage past the period, etc.)

User prompt (dynamic per batch):
    1. Current population status (n / target / composite chi-sq)
    2. Top axis gaps (signed, with z scores)
    3. Top joint cell gaps
    4. Aggregate vote gaps
    5. Explicit "produce N personas as JSON, biased to fill these gaps" instruction
       Drawn from simulations/<sim>/prompts/batch_guidance.md
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from ...core.axis import Axis
from ...core.config import PersonaConfig, SimulationContext
from ...core.joint import Joint
from ...core.persona import Persona
from ...verifiers.base import GapReport


# ---------------------------------------------------------------------------
# System prompt — assembled once per run, reused across batches
# ---------------------------------------------------------------------------

def _read_sim_text(sim_dir: Path, rel: str) -> str:
    p = sim_dir / rel
    return p.read_text() if p.exists() else ""


def _axes_block(ctx: SimulationContext) -> str:
    out = ["## Demographic axes (use these CANONICAL CODES exactly)\n"]
    for a in ctx.axes:
        if not a.is_sampleable() or a.kind == "scalar":
            continue
        if a.kind == "partition" or (a.kind == "derived" and a.categories):
            cats = a.categories or list((a.marginal or {}).keys())
            mar = a.marginal or {}
            tier = a.tier or "?"
            out.append(f"### {a.name}  (tier {tier}, partition)")
            for c in cats:
                pct = mar.get(c)
                if pct is not None:
                    out.append(f"  - `{c}`  →  {pct:.2f}% target")
                else:
                    out.append(f"  - `{c}`")
            if a.subgroup_rollups:
                for parent, leaves in a.subgroup_rollups.items():
                    out.append(f"  > rollup `{parent}` = sum of {leaves}")
            out.append("")
        elif a.kind == "flag" or (a.kind == "derived" and a.flags):
            flags = a.flags or list((a.rates or {}).keys())
            rates = a.rates or {}
            tier = a.tier or "?"
            out.append(f"### {a.name}  (tier {tier}, independent Bernoulli flags)")
            for f in flags:
                pct = rates.get(f)
                if pct is not None:
                    out.append(f"  - `{f}`  →  {pct:.2f}% target")
                else:
                    out.append(f"  - `{f}`  (derived; no marginal target)")
            out.append("")
    return "\n".join(out)


def _joints_block(ctx: SimulationContext) -> str:
    out = ["## Conditional relationships to honor\n",
           "When picking a persona's fields, respect these conditional distributions.",
           "Tables below are P(child | parent) in percent; rows for each parent value sum to 100"
           " (for `conditional`) or are independent rates (for `flag_rate_conditional`).\n"]
    for j in ctx.joints:
        if j.semantics == "vote_conditional":
            continue  # surfaced separately below
        if j.use == "sampling_only":
            continue  # sampler-only joints (compound buckets) — confusing for LLM
        out.append(f"### {j.name}  ({' + '.join(j.parents)} → {j.child}, {j.semantics}, tier {j.tier})")
        for parent_value, row in j.table.items():
            if not isinstance(row, dict):
                continue
            kvs = ", ".join(f"{k}={v:.0f}" for k, v in row.items())
            out.append(f"  - {parent_value!r}: {{{kvs}}}")
        if j.caste_bucket_map:
            out.append(f"  > caste bucket map: {j.caste_bucket_map}")
        if j.notes:
            out.append(f"  > {j.notes}")
        out.append("")
    return "\n".join(out)


def _vote_tables_block(ctx: SimulationContext) -> str:
    out = ["## Vote prior tables — P(party | parent), informational\n",
           "These are the conditional vote distributions from CSDS-style data;"
           " your assigned `vote_2019_LS` for each persona should be plausible"
           " given their religion, caste, gender, and welfare exposure.\n"]
    for j in ctx.joints:
        if j.semantics != "vote_conditional":
            continue
        out.append(f"### {j.name}  ({j.parents[0]} → vote_2019_LS, tier {j.tier})")
        for parent_value, row in j.table.items():
            kvs = ", ".join(f"{k}={v:.0f}" for k, v in row.items())
            out.append(f"  - {parent_value!r}: {{{kvs}}}")
        out.append("")
    return "\n".join(out)


def _aggregate_target_block(ctx: SimulationContext) -> str:
    if not ctx.aggregate_targets:
        return ""
    out = ["## Aggregate calibration target\n",
           "The whole population's vote share must approximately match:\n"]
    for t in ctx.aggregate_targets:
        out.append(f"### {t.name}  (tier {t.tier})")
        for b in t.buckets:
            vv = "/".join(b["vote_values"])
            out.append(f"  - `{b['name']}` ({vv}): **{b['target_pct']:.1f}%**")
        out.append("")
    return "\n".join(out)


def _persona_schema_block(ctx: SimulationContext, vote_field: str) -> str:
    """Describe the JSON output shape with a worked example using canonical codes."""
    example_fields: dict[str, Any] = {}
    for a in ctx.axes:
        if not a.is_sampleable() or a.kind == "scalar":
            continue
        if a.kind == "partition" or (a.kind == "derived" and a.categories):
            cats = a.categories or []
            example_fields[a.name] = cats[0] if cats else None
        elif a.kind == "flag" or (a.kind == "derived" and a.flags):
            example_fields[a.name] = {f: False for f in (a.flags or [])}
    example_fields[vote_field] = "AITC"

    example = {
        "personas": [{
            "fields": example_fields,
            "narrative": {
                "self_prompt": (
                    "You are <Name>, a <age> year old <religion> <caste> "
                    "<gender> living in <gp_location>. Your psychology... "
                    "Your political affiliation... When asked about voting "
                    "in the 2019 Lok Sabha you would say..."
                )
            }
        }]
    }

    return (
        "## Output schema (return ONLY valid JSON matching this shape, no preamble or markdown fences)\n\n"
        "```json\n"
        + json.dumps(example, indent=2)
        + "\n```\n\n"
        "### Field rules\n"
        "- Every field in `fields` must use the EXACT canonical codes listed in the axes section above.\n"
        "- Boolean flag axes (`asset_media`, `amenities`, `welfare_exposure`) must include all their flags as keys.\n"
        "- If `workforce_status` is not in {`Main_worker`, `Marginal_worker`}, set `occupation` and `class_of_worker` to `None` (string).\n"
        "- `welfare_dominant` should be the single most-salient scheme this persona qualifies for, OR `None`.\n"
        f"- `{vote_field}` must be one of the parties listed in the vote tables above.\n"
        "- `narrative.self_prompt` is **a single string** addressed to the persona in the second person.\n"
        "  It will be used downstream as a system prompt for that persona in a simulation.\n"
        "  Style: vivid, specific, ~200–350 words, written like an actor's character brief.\n"
        "  Cover: name, family/refugee history if relevant, daily life, household relationships,\n"
        "  what news/issues animate them, what local figures they admire or distrust, what daily\n"
        "  pressures and welfare touch-points shape their politics. Use details from the\n"
        "  pre-period context.\n"
        "  **DO NOT** explain or rationalize their 2019 LS vote choice in the narrative — that\n"
        "  vote is recorded separately in the `fields` dict. The narrative should describe the\n"
        "  identity and pressures that PRODUCE political views, not lock in a frozen\n"
        "  rationalization of the 2019 outcome. (When the persona later answers a 2021/2024 vote\n"
        "  query, the answer should emerge from these biographical pressures + what they've\n"
        "  lived through since 2019, not from a frozen self-justification.)\n"
        "  DO NOT reference any event after the pre-period cutoff specified in the context.\n"
    )


def build_persona_json_schema(
    ctx: SimulationContext, vote_field: str, batch_size: int | None = None
) -> dict:
    """Build a strict JSON schema for the LLM's `response_format`.

    sglang/vLLM/OpenAI all support `response_format = {"type":"json_schema",
    "json_schema":{"name":..., "schema":..., "strict":True}}`. Constrained
    decoding (xgrammar-backed in sglang) GUARANTEES the model emits valid
    JSON with the exact shape we want — every category becomes an enum, all
    required fields are present, no preamble. Schema-violation drops at the
    validator should fall to ~0 with this in place.

    Each `fields.<axis>` is typed:
      partition / derived-with-categories  → string with `enum`
      flag / derived-with-flags            → object with all flags as
                                             required boolean properties
    """
    fields_props: dict[str, Any] = {}
    fields_required: list[str] = []
    for a in ctx.axes:
        if not a.is_sampleable() or a.kind == "scalar":
            continue
        if a.kind == "partition" or (a.kind == "derived" and a.categories):
            cats = list(a.categories or [])
            # Match validate_persona's special-cases.
            if a.name in {"occupation", "class_of_worker", "welfare_dominant"}:
                if "None" not in cats:
                    cats = cats + ["None"]
            fields_props[a.name] = {"type": "string", "enum": cats}
            fields_required.append(a.name)
        elif a.kind == "flag" or (a.kind == "derived" and a.flags):
            flags = list(a.flags or [])
            fields_props[a.name] = {
                "type": "object",
                "properties": {f: {"type": "boolean"} for f in flags},
                "required": flags,
                "additionalProperties": False,
            }
            fields_required.append(a.name)

    # Vote field: enum over parties seen in any vote_conditional joint.
    parties: list[str] = []
    for j in ctx.joints:
        if j.semantics == "vote_conditional" and j.parties:
            for p in j.parties:
                if p not in parties:
                    parties.append(p)
    if not parties:
        parties = ["BJP", "AITC", "INC", "LF", "Other"]
    fields_props[vote_field] = {"type": "string", "enum": parties}
    fields_required.append(vote_field)

    persona_schema = {
        "type": "object",
        "properties": {
            "fields": {
                "type": "object",
                "properties": fields_props,
                "required": fields_required,
                "additionalProperties": False,
            },
            "narrative": {
                "type": "object",
                "properties": {
                    "self_prompt": {"type": "string", "minLength": 200},
                },
                "required": ["self_prompt"],
                "additionalProperties": False,
            },
        },
        "required": ["fields", "narrative"],
        "additionalProperties": False,
    }

    array_constraint: dict[str, Any] = {
        "type": "array",
        "items": persona_schema,
    }
    if batch_size is not None:
        # Soft bound — encourages exactly batch_size items but doesn't
        # block decode at upper edge.
        array_constraint["minItems"] = max(1, batch_size - 2)
        array_constraint["maxItems"] = batch_size + 4

    return {
        "type": "object",
        "properties": {"personas": array_constraint},
        "required": ["personas"],
        "additionalProperties": False,
    }


def build_system_prompt(ctx: SimulationContext, persona_config: PersonaConfig) -> str:
    sim_dir = ctx.sim_dir
    prompts_cfg = persona_config.get("prompts", {}) or {}
    vote_field = persona_config.get("vote.field_name", "vote_2019_LS")

    anchors = _read_sim_text(sim_dir, prompts_cfg.get("anchors", "prompts/system_anchors.md"))
    news_path = prompts_cfg.get("news_context", "news/persona_context_pre2019.md")
    news = _read_sim_text(sim_dir, news_path)

    parts = []
    parts.append(f"# Persona generator — {ctx.sim_dir.name}\n")
    parts.append(
        "You generate synthetic voter personas for a calibrated simulation. "
        "Each persona is one row of demographics + a narrative paragraph. "
        "The full population must approximately match the target distributions "
        "given below. After each batch, you will receive a gap report describing "
        "which categories are over- or under-represented; bias the next batch "
        "to fill those gaps.\n"
    )

    if anchors:
        parts.append("# Region narrative anchors\n")
        parts.append(anchors.strip())
        parts.append("")

    if news:
        parts.append("# Pre-period opinion context (do NOT reference events after the cutoff)\n")
        parts.append(news.strip())
        parts.append("")

    parts.append(_axes_block(ctx))
    parts.append(_joints_block(ctx))
    parts.append(_vote_tables_block(ctx))
    parts.append(_aggregate_target_block(ctx))
    parts.append(_persona_schema_block(ctx, vote_field))

    return "\n".join(parts).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Per-batch user prompt — gap report + ask
# ---------------------------------------------------------------------------

def _gap_summary_lines(report: GapReport, k: int = 12) -> list[str]:
    """Compact text summary of the worst gaps the next batch should address."""
    if report.n == 0:
        return ["(no personas yet — generate from scratch using the targets above)"]
    out = []
    out.append(f"Population so far: n={report.n}.")
    out.append(f"Composite chi-sq: {report.composite_score:.1f} "
               f"(threshold {report.tolerance_used.get('composite_chisq_max', '?')}).")
    out.append("")
    # Axis gaps
    flat = []
    for a in report.axis_gaps:
        for r in a.rows:
            if r.get("is_rollup"):
                continue
            flat.append((a.axis, r["category"], r["target_pct"], r["observed_pct"], r["gap_pp"], r["z"]))
    flat.sort(key=lambda t: -abs(t[5]))
    if flat:
        out.append(f"### Top {k} category gaps (most → least urgent, signed):")
        out.append("```")
        out.append(f"{'axis':22s} {'category':36s} {'target':>7s} {'obs':>7s} {'gap_pp':>7s} {'z':>6s}")
        for axis, cat, tgt, obs, g, z in flat[:k]:
            sign = "→ need MORE" if g < 0 else "→ need FEWER"
            out.append(f"{axis:22s} {cat[:36]:36s} {tgt:7.1f} {obs:7.1f} {g:+7.1f} {z:+6.2f}  {sign}")
        out.append("```")
        out.append("")
    # Aggregate vote gaps
    for ag in report.aggregate_gaps:
        out.append(f"### Aggregate {ag.name} gaps:")
        out.append("```")
        out.append(f"{'bucket':24s} {'target':>7s} {'obs':>7s} {'gap_pp':>7s} {'z':>6s}")
        for b in ag.buckets:
            out.append(f"{b['name']:24s} {b['target_pct']:7.1f} {b['observed_pct']:7.1f} "
                       f"{b['gap_pp']:+7.1f} {b['z']:+6.2f}")
        out.append("```")
        out.append("")
    return out


def build_batch_user_prompt(
    *,
    report: GapReport,
    batch_size: int,
    target_n: int,
    n_so_far: int,
    batch_guidance: str = "",
    correction_phase: bool = False,
) -> str:
    parts = []
    parts.append(f"# Batch request ({n_so_far}/{target_n} personas generated so far)\n")
    if correction_phase:
        parts.append(
            "**Correction phase** — the population has reached the target size but is "
            "out of statistical tolerance. This batch should be small and surgically "
            "biased to fix the largest remaining gaps.\n"
        )
    parts.extend(_gap_summary_lines(report))

    parts.append("---\n")
    if batch_guidance.strip():
        parts.append(batch_guidance.strip())
        parts.append("")
    parts.append(
        f"Generate exactly **{batch_size}** new personas as a JSON object of the shape "
        "shown in the system prompt's Output schema section. Bias your picks to close "
        "the gaps above. Return ONLY the JSON — no prose, no markdown fences.\n\n"
        "**HARD REQUIREMENTS** (drop one and the persona is rejected):\n"
        "  1. Top-level shape: `{\"personas\": [ {...}, {...}, ... ]}`.\n"
        "  2. Each persona has BOTH `fields` AND `narrative.self_prompt`.\n"
        "  3. Every value in `fields` must be EXACTLY a canonical code from the\n"
        "     axes section of the system prompt. No new codes, no relabeling,\n"
        "     no plain-English variants. Examples of common errors to avoid:\n"
        "       `bagdi` → use `Bagdi`; `Main worker` → use `Main_worker`;\n"
        "       `25_27` is NOT an age cohort (use `23_27` or `28_32`);\n"
        "       `Employee` is a class_of_worker code, not occupation/workforce_status;\n"
        "       `Sheikh` is NOT a caste leaf (Muslim sub-castes pooled to `Muslim`).\n"
        "  4. `narrative.self_prompt` is a single 200-350 word English string."
    )
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Response parsing & validation
# ---------------------------------------------------------------------------

_JSON_FENCE = re.compile(r"```(?:json)?\s*(\{.*?\}|\[.*?\])\s*```", re.DOTALL)


def parse_persona_response(text: str) -> list[dict]:
    """Extract personas from the LLM response.

    Strategy: try strict JSON parse first; if that fails, fall back to
    iterative per-object recovery using `JSONDecoder.raw_decode`. This handles:
      - small structural errors (one extra `}`)
      - mid-array truncation
      - leading/trailing prose
      - code fences
    """
    # Pass 1: strict JSON, possibly inside a code fence.
    candidates: list[str] = []
    for m in _JSON_FENCE.finditer(text):
        candidates.append(m.group(1))
    candidates.append(text.strip())
    starts = [text.find(c) for c in "[{" if text.find(c) != -1]
    if starts:
        candidates.append(text[min(starts):])

    for blob in candidates:
        try:
            data = json.loads(blob)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and "personas" in data:
            return data["personas"]
        if isinstance(data, list):
            return data

    # Pass 2: iterative per-object recovery. Walk through the response,
    # finding each `{"fields":` opening and trying to decode one persona.
    return _extract_personas_iteratively(text)


def _extract_personas_iteratively(text: str) -> list[dict]:
    decoder = json.JSONDecoder()
    personas: list[dict] = []
    pos = 0
    while True:
        # Find next `{"fields":` (or `{ "fields"`) — the start of a persona.
        next_obj = text.find('"fields"', pos)
        if next_obj == -1:
            break
        # Walk back to the opening `{` of the persona dict.
        brace = text.rfind("{", pos, next_obj)
        if brace == -1:
            break
        try:
            obj, end = decoder.raw_decode(text, brace)
            if isinstance(obj, dict) and "fields" in obj:
                personas.append(obj)
            pos = end
        except json.JSONDecodeError:
            # Couldn't parse this persona; skip past its `{` and try the next.
            pos = brace + 1
    return personas


def _norm_code(s: str) -> str:
    """Normalize a category code for fuzzy lookup: lowercase, only alnum kept."""
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def _fuzzy_resolve(value: str, canonicals: set[str]) -> str | None:
    """Try to canonicalize a malformed category value.

    The 9B local LLM frequently produces casing/punctuation drift
    (e.g. `bagdi` vs `Bagdi`, `Main worker` vs `Main_worker`,
    `Higher Secondary (Class 11-12)` vs `Higher_Secondary`). Canonical-
    code normalization rescues those cases without loosening real schema
    violations like `Sheikh` for caste (which legitimately doesn't exist
    after our Muslim sub-caste pooling).
    """
    if value in canonicals:
        return value
    nv = _norm_code(value)
    if not nv:
        return None
    for c in canonicals:
        if _norm_code(c) == nv:
            return c
    return None


def validate_persona(d: dict, ctx: SimulationContext, vote_field: str) -> tuple[bool, str | None]:
    """Check (and lightly normalize) a parsed persona. Returns (ok, error_msg).

    Mutates `d['fields']` in place when fuzzy normalization recovers a value
    so downstream code (vote sampler, verifier) sees the canonical code.
    """
    if not isinstance(d, dict):
        return False, "persona is not a dict"
    fields = d.get("fields")
    if not isinstance(fields, dict):
        return False, "missing or non-dict 'fields'"
    for axis in ctx.axes:
        if not axis.is_sampleable() or axis.kind == "scalar":
            continue
        v = fields.get(axis.name)
        if v is None:
            return False, f"missing field {axis.name!r}"
        if axis.kind == "partition" or (axis.kind == "derived" and axis.categories):
            cats = set(axis.categories or [])
            if axis.name == "occupation" or axis.name == "class_of_worker":
                cats.add("None")
            if axis.name == "welfare_dominant":
                cats.add("None")
            if v not in cats:
                resolved = _fuzzy_resolve(str(v), cats)
                if resolved is None:
                    return False, f"field {axis.name!r} value {v!r} not in categories"
                fields[axis.name] = resolved
        elif axis.kind == "flag" or (axis.kind == "derived" and axis.flags):
            if not isinstance(v, dict):
                return False, f"field {axis.name!r} must be a dict of flags"
            # Allow case/punctuation drift in flag KEYS, e.g. `tv`/`Television`.
            flag_set = set(axis.flags or [])
            normalized: dict[str, bool] = {}
            for k, val in v.items():
                if k in flag_set:
                    normalized[k] = bool(val)
                    continue
                resolved = _fuzzy_resolve(str(k), flag_set)
                if resolved is not None:
                    normalized[resolved] = bool(val)
            for flag in flag_set:
                if flag not in normalized:
                    return False, f"field {axis.name!r} missing flag {flag!r}"
            fields[axis.name] = normalized
    if vote_field not in fields:
        return False, f"missing vote field {vote_field!r}"
    narrative = d.get("narrative", {})
    if not isinstance(narrative, dict) or not narrative.get("self_prompt"):
        return False, "missing narrative.self_prompt"
    return True, None
