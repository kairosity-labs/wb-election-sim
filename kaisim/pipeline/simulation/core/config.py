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

    @property
    def events_file(self) -> Path:
        """Resolve the events YAML path.

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
            # Walk up from sim_dir to find the repo root (parent of `kaisim`).
            kaisim_dir = self.sim_dir
            while kaisim_dir.name and kaisim_dir.name != "kaisim":
                kaisim_dir = kaisim_dir.parent
            repo_root = kaisim_dir.parent if kaisim_dir.name else self.sim_dir
            consts = repo_root / "constituency_data" / "constituencies"
            # Exact match first.
            direct = consts / str(ac_id) / "events.yaml"
            if direct.exists():
                return direct
            # Glob match: "<ac_id>_*" (handles ac_id="095" → "095_bangaon_uttar")
            for cand in sorted(consts.glob(f"{ac_id}_*")):
                ev_yaml = cand / "events.yaml"
                if ev_yaml.exists():
                    return ev_yaml
            raise FileNotFoundError(
                f"ac_id={ac_id!r}: no events.yaml under {consts}")

        return self.sim_dir / "news/events.yaml"

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
