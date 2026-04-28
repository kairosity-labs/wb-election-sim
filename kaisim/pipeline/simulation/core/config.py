"""SimulationConfig — load + parse a sim YAML from simulations/<sim>/simulation_configs/.

Schema (see simulation_configs/rule_based.yaml for a worked example):
    simulation: name, description
    input:      persona_set, events_file
    clock:      start_date, end_date, tick_unit, tick_size, reflection_every_n_ticks
    targeting:  strategy, config (free-form, strategy-specific)
    update:     style, prompt_template
    reflection: enabled, trigger, every_n_ticks, compression_target_tokens
    llm:        provider, model, reasoning, temperature, max_tokens, cache_system_prompt
    execution:  async, max_concurrent_personas
    output:     runs_dir, save_raw_responses, save_feeds_audit
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

import yaml


@dataclass
class SimulationConfig:
    raw: dict
    sim_dir: Path
    name: str = ""

    @classmethod
    def load(cls, sim_dir: str | Path, config_path: str | Path) -> "SimulationConfig":
        sim_dir = Path(sim_dir)
        config_path = Path(config_path)
        if not config_path.is_absolute():
            config_path = sim_dir / config_path
        raw = yaml.safe_load(config_path.read_text())
        return cls(
            raw=raw,
            sim_dir=sim_dir,
            name=raw.get("simulation", {}).get("name", config_path.stem),
        )

    def get(self, dotted: str, default: Any = None) -> Any:
        cur: Any = self.raw
        for part in dotted.split("."):
            if not isinstance(cur, dict) or part not in cur:
                return default
            cur = cur[part]
        return cur

    # convenience
    @property
    def persona_set_name(self) -> str:
        return self.get("input.persona_set", "")

    def _repo_root(self) -> Path:
        """Walk up from sim_dir to repo root (parent of `kaisim`)."""
        d = self.sim_dir
        while d.name and d.name != "kaisim":
            d = d.parent
        return d.parent if d.name else self.sim_dir

    @property
    def events_file(self) -> Path:
        """Resolve the per-AC events YAML path.

        Resolution order:
          1. `input.events_file` (relative to sim_dir if not absolute) — legacy
             path-based config, e.g. "news/events_2019_2024.yaml".
          2. `ac_id` → `constituency_data/constituencies/<ac_id>/events.yaml`
             (or first match of "<ac_id>_*" if ac_id is just a 3-digit number).
             This is the canonical post-migration location.
          3. Fallback: `sim_dir / news/events.yaml`.
        """
        ev = self.get("input.events_file")
        if ev:
            p = Path(ev)
            return p if p.is_absolute() else (self.sim_dir / p)

        ac_id = self.get("ac_id")
        if ac_id:
            consts = self._repo_root() / "constituency_data" / "constituencies"
            direct = consts / str(ac_id) / "events.yaml"
            if direct.exists():
                return direct
            for cand in sorted(consts.glob(f"{ac_id}_*")):
                ev_yaml = cand / "events.yaml"
                if ev_yaml.exists():
                    return ev_yaml
            raise FileNotFoundError(
                f"ac_id={ac_id!r}: no events.yaml under {consts}")

        return self.sim_dir / "news/events.yaml"

    @property
    def state_events_file(self) -> Path | None:
        """Resolve the state/national-scope events YAML.

        Defaults to `constituency_data/state_events_2019_2026.yaml`. Override
        via `input.state_events_file` (absolute or relative to sim_dir). Set
        to `false` / `null` in YAML to disable.
        """
        explicit = self.get("input.state_events_file", "__unset__")
        if explicit is False or explicit is None:
            return None
        if explicit != "__unset__":
            p = Path(explicit)
            return p if p.is_absolute() else (self.sim_dir / p)
        # Default: convention-resolved file under constituency_data/
        cand = self._repo_root() / "constituency_data" / "state_events_2019_2026.yaml"
        return cand if cand.exists() else None

    @property
    def events_files(self) -> list[Path]:
        """The full set of event YAMLs the orchestrator should union into the
        NewsPool. Order matters: AC-local file goes FIRST so its slugs win
        on collisions with state-level events."""
        out: list[Path] = []
        try:
            ac_yaml = self.events_file
            if ac_yaml.exists():
                out.append(ac_yaml)
        except FileNotFoundError:
            pass
        state_yaml = self.state_events_file
        if state_yaml and state_yaml.exists():
            out.append(state_yaml)
        return out

    @property
    def start_date(self) -> date:
        return date.fromisoformat(self.get("clock.start_date"))

    @property
    def end_date(self) -> date:
        return date.fromisoformat(self.get("clock.end_date"))

    @property
    def tick_unit(self) -> str:
        return self.get("clock.tick_unit", "month")

    @property
    def tick_size(self) -> int:
        return int(self.get("clock.tick_size", 1))

    @property
    def reflection_every_n_ticks(self) -> int:
        return int(self.get("clock.reflection_every_n_ticks",
                            self.get("reflection.every_n_ticks", 12)))
