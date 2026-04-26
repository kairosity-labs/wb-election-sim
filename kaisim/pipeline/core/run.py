"""SimulationRun — the artifact produced by the (Phase-2) simulation pipeline.

A Run cites a PersonaSet by name and adds:
    - run_config snapshot
    - per-persona simulation results (e.g., predicted vote, narrative deltas)
    - aggregate metrics

Phase 1 only defines the dataclass + I/O so Phase-2 work can plug in without
touching the framework core.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


@dataclass
class SimulationRun:
    name: str
    persona_set_name: str
    persona_set_meta_hash: str
    results: list[dict] = field(default_factory=list)        # per-persona outputs
    aggregates: dict[str, Any] = field(default_factory=dict) # whole-population metrics
    run_config_snapshot: dict = field(default_factory=dict)
    meta: dict = field(default_factory=dict)

    def save(self, root: Path) -> None:
        root = Path(root)
        root.mkdir(parents=True, exist_ok=True)
        self.meta.setdefault(
            "created_at", datetime.now(timezone.utc).isoformat(timespec="seconds")
        )
        self.meta["name"] = self.name
        self.meta["persona_set"] = self.persona_set_name
        self.meta["persona_set_meta_hash"] = self.persona_set_meta_hash

        (root / "meta.json").write_text(json.dumps(self.meta, indent=2))
        if self.run_config_snapshot:
            (root / "run_config.snapshot.yaml").write_text(
                yaml.safe_dump(self.run_config_snapshot, sort_keys=False)
            )
        if self.results:
            (root / "results.jsonl").write_text(
                "\n".join(json.dumps(r) for r in self.results) + "\n"
            )
        if self.aggregates:
            (root / "aggregates.json").write_text(json.dumps(self.aggregates, indent=2))
        (root / "reports").mkdir(exist_ok=True)
