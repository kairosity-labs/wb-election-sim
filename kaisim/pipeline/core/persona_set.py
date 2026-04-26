"""PersonaSet — a named, reusable corpus of personas + its provenance.

A PersonaSet is the unit that downstream simulations cite. It carries:
    - personas:           list of Persona objects
    - meta:               provenance (when/how/with-which-config it was made,
                          verifier composite score at end of generation)
    - config_snapshot:    frozen copy of the persona_config that produced it,
                          so an old set remains explainable years later

On disk:
    personas/<set_name>/
        personas.jsonl                  one Persona per line
        meta.json                       provenance + verifier headline
        persona_config.snapshot.yaml    frozen config
        batches/raw_NN.json             raw LLM batches (LLM samplers only)
        reports/gap_NN.{json,md}        per-batch verifier reports
        reports/FINAL.md                summary report

Two PersonaSets that came out of the same persona_config will have the same
`config_hash` in meta.json — useful for catching accidental duplicates.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from .persona import Persona


def hash_config(config: dict) -> str:
    """Stable SHA-256 of a config dict (sorted-keys serialization)."""
    blob = json.dumps(config, sort_keys=True, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(blob.encode()).hexdigest()[:16]


@dataclass
class PersonaSet:
    name: str
    personas: list[Persona] = field(default_factory=list)
    meta: dict = field(default_factory=dict)
    config_snapshot: dict = field(default_factory=dict)
    root: Path | None = None                        # on-disk location, if loaded

    # ---- size / iteration ----
    def __len__(self) -> int:
        return len(self.personas)

    def __iter__(self):
        return iter(self.personas)

    # ---- I/O ----
    @classmethod
    def load(cls, root: Path) -> "PersonaSet":
        root = Path(root)
        meta = json.loads((root / "meta.json").read_text())
        config_path = root / "persona_config.snapshot.yaml"
        config_snapshot = (
            yaml.safe_load(config_path.read_text()) if config_path.exists() else {}
        )
        personas = []
        with (root / "personas.jsonl").open() as f:
            for line in f:
                line = line.strip()
                if line:
                    personas.append(Persona.from_dict(json.loads(line)))
        return cls(
            name=meta["name"],
            personas=personas,
            meta=meta,
            config_snapshot=config_snapshot,
            root=root,
        )

    def save(self, root: Path) -> None:
        root = Path(root)
        root.mkdir(parents=True, exist_ok=True)
        (root / "personas.jsonl").write_text(
            "\n".join(json.dumps(p.to_dict()) for p in self.personas) + "\n"
        )
        (root / "meta.json").write_text(json.dumps(self.meta, indent=2))
        if self.config_snapshot:
            (root / "persona_config.snapshot.yaml").write_text(
                yaml.safe_dump(self.config_snapshot, sort_keys=False)
            )
        (root / "batches").mkdir(exist_ok=True)
        (root / "reports").mkdir(exist_ok=True)
        self.root = root

    # ---- meta builder ----
    def update_meta(self, *, sampler: str, verifier_summary: dict | None = None,
                    extra: dict | None = None) -> None:
        self.meta.update({
            "name": self.name,
            "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "n": len(self.personas),
            "sampler": sampler,
            "config_hash": hash_config(self.config_snapshot) if self.config_snapshot else None,
            "schema_version": "1.0",
        })
        if verifier_summary is not None:
            self.meta["verifier"] = verifier_summary
        if extra:
            self.meta.update(extra)
