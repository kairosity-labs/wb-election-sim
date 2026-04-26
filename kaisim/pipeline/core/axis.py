"""Axis — a single demographic dimension along which personas are described.

An Axis is one of:
    partition   — a single value drawn from a fixed category list
                  (e.g., religion ∈ {Hindu, Muslim, Christian, ...})
    flag        — a vector of independent Bernoulli flags
                  (e.g., asset_media = {TV: True, Smartphone: False, ...})
    scalar      — a constant (e.g., household_size_avg = 4.4); not sampled
    derived     — computed from prior fields by a plugin function
                  (e.g., welfare_exposure derived from occupation+gender+age)

Axes are declared in `simulations/<sim>/structures/axes.json`. The framework
loads them via `Axis.from_json` and treats them uniformly.

To add a new axis to a simulation:
    1. Append a JSON entry to axes.json with the right `kind`.
    2. If `partition`: provide `categories` + `marginal` (must sum to ~100).
    3. If `flag`: provide `flags` + `rates` (each in [0, 100]).
    4. If `derived`: provide `parents`, `module`, `function`.
    5. Reference the axis in your `sampling_spec` (see persona_config.yaml).
    6. Add any joints that condition the new axis on others.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Axis:
    name: str
    kind: str                                       # partition | flag | scalar | derived

    # partition
    categories: list[str] | None = None             # leaf category codes
    marginal: dict[str, float] | None = None        # category -> pct (sums ~100)
    subgroup_rollups: dict[str, list[str]] | None = None
    """Optional verifier-only roll-ups (e.g., SC_total = Namasudra+Bagdi+...)."""

    # flag
    flags: list[str] | None = None
    rates: dict[str, float] | None = None           # flag -> pct (each independent)

    # scalar
    value: Any = None

    # derived
    parents: list[str] | None = None                # axis names this depends on
    module: str | None = None                       # dotted path to plugin module
    function: str | None = None                     # function name in plugin module

    # metadata
    tier: str | None = None                         # A | B | C | D | E
    source_csv: str | None = None
    display_names: dict[str, str] | None = None     # code -> human label
    notes: str | None = None

    # verifier control: only verify personas where condition matches.
    # E.g., occupation only verified among workers:
    #     "verify_condition": {"field": "workforce_status",
    #                          "values": ["Main_worker", "Marginal_worker"]}
    verify_condition: dict | None = None

    @classmethod
    def from_json(cls, d: dict) -> "Axis":
        return cls(
            name=d["name"],
            kind=d["kind"],
            categories=d.get("categories"),
            marginal=d.get("marginal"),
            subgroup_rollups=d.get("subgroup_rollups"),
            flags=d.get("flags"),
            rates=d.get("rates"),
            value=d.get("value"),
            parents=d.get("parents"),
            module=d.get("module"),
            function=d.get("function"),
            tier=d.get("tier"),
            source_csv=d.get("source_csv"),
            display_names=d.get("display_names"),
            notes=d.get("notes"),
            verify_condition=d.get("verify_condition"),
        )

    def is_sampleable(self) -> bool:
        """Whether the framework will sample a value for this axis per persona.

        Scalar axes are descriptive metadata, not per-persona fields.
        """
        return self.kind in {"partition", "flag", "derived"}
