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
        return self.sim_dir / self.get("input.events_file", "news/events.yaml")

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
