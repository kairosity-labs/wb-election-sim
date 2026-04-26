"""SimulationContext + PersonaConfig — load + validate per-simulation config.

A simulation lives at `simulations/<sim_name>/` and exposes:
    structures/axes.json
    structures/joints.json
    derived/*.py
    persona_configs/<config_name>.yaml
    prompts/*.md
    news/*.md

`SimulationContext.load(sim_dir)` reads axes + joints once. Subsequent calls to
`PersonaConfig.load(sim_dir, config_name)` parse the YAML and resolve all paths
relative to the sim_dir so generation code never touches absolute paths.
"""
from __future__ import annotations

import importlib
import importlib.util
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .axis import Axis
from .joint import AggregateTarget, Joint


@dataclass
class SimulationContext:
    sim_dir: Path
    axes: list[Axis]
    joints: list[Joint]
    aggregate_targets: list[AggregateTarget]

    @classmethod
    def load(cls, sim_dir: str | Path) -> "SimulationContext":
        sim_dir = Path(sim_dir)
        axes_doc = json.loads((sim_dir / "structures" / "axes.json").read_text())
        joints_doc = json.loads((sim_dir / "structures" / "joints.json").read_text())
        return cls(
            sim_dir=sim_dir,
            axes=[Axis.from_json(a) for a in axes_doc["axes"]],
            joints=[Joint.from_json(j) for j in joints_doc["joints"]],
            aggregate_targets=[
                AggregateTarget.from_json(t) for t in joints_doc.get("aggregate_targets", [])
            ],
        )

    # ---- lookup helpers ----
    def axis(self, name: str) -> Axis:
        for a in self.axes:
            if a.name == name:
                return a
        raise KeyError(f"No axis named {name!r} in simulation {self.sim_dir.name}")

    def joint(self, name: str) -> Joint:
        for j in self.joints:
            if j.name == name:
                return j
        raise KeyError(f"No joint named {name!r} in simulation {self.sim_dir.name}")

    # ---- plugin loading ----
    def load_plugin(self, module: str, function: str):
        """Resolve a `module.function` reference declared in axes.json or
        sampling_spec, importing the simulation's local package if needed.
        """
        full_module = f"simulations.{self.sim_dir.name}.{module}"
        if full_module not in sys.modules:
            # Add the kaisim/ root to sys.path so `simulations.<sim>` imports.
            kaisim_root = self.sim_dir.parent.parent
            if str(kaisim_root) not in sys.path:
                sys.path.insert(0, str(kaisim_root))
            importlib.import_module(full_module)
        return getattr(sys.modules[full_module], function)


@dataclass
class PersonaConfig:
    """Parsed + path-resolved persona-generation config.

    See `simulations/wb_2021_ac095/persona_configs/baseline_rule.yaml` for
    a worked example with all fields.
    """
    raw: dict
    sim_dir: Path

    # convenience views
    set_name: str = ""
    sampler: str = "rule_based"
    target_n: int = 100
    batch_size: int = 20

    @classmethod
    def load(cls, sim_dir: str | Path, config_path: str | Path) -> "PersonaConfig":
        sim_dir = Path(sim_dir)
        config_path = Path(config_path)
        if not config_path.is_absolute():
            config_path = sim_dir / config_path
        raw = yaml.safe_load(config_path.read_text())
        ps = raw.get("persona_set", {})
        gen = raw.get("generation", {})
        return cls(
            raw=raw,
            sim_dir=sim_dir,
            set_name=ps.get("name", config_path.stem),
            sampler=gen.get("sampler", "rule_based"),
            target_n=gen.get("target_n", 100),
            batch_size=gen.get("batch_size", 20),
        )

    def get(self, key: str, default: Any = None) -> Any:
        """Dotted-key lookup into the raw config (e.g. "vote.blending.method")."""
        cur = self.raw
        for part in key.split("."):
            if not isinstance(cur, dict) or part not in cur:
                return default
            cur = cur[part]
        return cur
