"""Persona — a single simulated agent with demographic fields + optional narrative.

Persona is schema-driven: `fields` is a dict keyed by axis name. The framework
makes no assumptions about which axes exist — that's defined per-simulation in
axes.json. Values are typed by the axis kind:

    partition axis  →  fields[axis] = "<category_code>"           (str)
    flag axis       →  fields[axis] = {"<flag>": True, ...}       (dict[str, bool])
    derived axis    →  fields[axis] depends on the plugin's return type
    vote field      →  fields["vote_2019_LS"] = "<party_code>"    (str)

`narrative` is optional and populated by LLM samplers, not by rule-based ones.
The expected shape is documented in the simulation's persona_rules.md but the
framework treats it as an opaque dict.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Persona:
    id: str
    fields: dict[str, Any] = field(default_factory=dict)
    narrative: dict[str, Any] | None = None

    # ---- dict-like access ----
    def __getitem__(self, k: str) -> Any:
        return self.fields[k]

    def get(self, k: str, default: Any = None) -> Any:
        return self.fields.get(k, default)

    def __contains__(self, k: str) -> bool:
        return k in self.fields

    # ---- I/O ----
    def to_dict(self) -> dict:
        d = {"id": self.id, "fields": self.fields}
        if self.narrative is not None:
            d["narrative"] = self.narrative
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "Persona":
        return cls(
            id=d["id"],
            fields=d.get("fields", {}),
            narrative=d.get("narrative"),
        )
