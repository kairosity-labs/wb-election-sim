"""Joint — a conditional probability / rate table linking parent axes to a child.

A Joint encodes one of these semantics:

    conditional             P(child | parents) — child is a partition.
                            Rows must sum to ~100 over child categories.

    flag_rate_conditional   P(child_flag = True | parents) — for one or more
                            child flags. Rates are independent.

    two_indicator_rates     Two Bernoulli rates per parent value (used by
                            workforce: Main_worker + Unemployed_seeking).

    vote_conditional        P(party | parent) for the vote field. Consumed by
                            VoteBlender, not by the DAG sampling step.

Optional bucket maps (`caste_bucket_map`, `education_bucket_map`):
    Some joints use coarser-grained labels than the underlying axis. The
    bucket map declares "this joint's bucket X covers leaf categories [...]"
    so the sampler can route a leaf value to the right joint bucket.

To add a new joint to a simulation:
    1. Append a JSON entry to joints.json with:
        - parents: list of axis names (must already exist in axes.json)
        - child: target axis name (or "vote_<field>" for vote joints)
        - semantics: one of the four above
        - table: nested dict (parent values → child rates/categories → pct)
    2. If joint labels differ from axis category codes, add a bucket_map.
    3. Reference the joint by name from your sampling_spec.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Joint:
    name: str
    parents: list[str]
    child: str
    semantics: str
    table: dict[str, Any]

    # semantics-specific extras
    flags: list[str] | None = None
    indicators: list[str] | None = None
    parties: list[str] | None = None
    child_categories: list[str] | None = None
    child_other_expansion_axis: str | None = None
    child_other_expansion_categories: list[str] | None = None
    caste_bucket_map: dict[str, list[str]] | None = None
    education_bucket_map: dict[str, str] | None = None

    # metadata
    tier: str | None = None
    source_csv: str | None = None
    use: str | None = None                          # e.g., "verifier_only"
    notes: str | None = None

    @classmethod
    def from_json(cls, d: dict) -> "Joint":
        return cls(
            name=d["name"],
            parents=d["parents"],
            child=d["child"],
            semantics=d["semantics"],
            table=d["table"],
            flags=d.get("flags"),
            indicators=d.get("indicators"),
            parties=d.get("parties"),
            child_categories=d.get("child_categories"),
            child_other_expansion_axis=d.get("child_other_expansion_axis"),
            child_other_expansion_categories=d.get("child_other_expansion_categories"),
            caste_bucket_map=d.get("caste_bucket_map"),
            education_bucket_map=d.get("education_bucket_map"),
            tier=d.get("tier"),
            source_csv=d.get("source_csv"),
            use=d.get("use"),
            notes=d.get("notes"),
        )

    def is_for_sampling(self) -> bool:
        """Joints marked use=verifier_only are ignored by the sampler."""
        return self.use != "verifier_only"

    def is_for_verifying(self) -> bool:
        """Joints marked use=sampling_only are ignored by the verifier."""
        return self.use != "sampling_only"


@dataclass
class AggregateTarget:
    """A scalar target the verifier checks against the population aggregate.

    The most common case is the per-party vote share (e.g., BJP=48.0). Each
    bucket may sum over multiple field values (`Left_INC_combined` =
    INC + LF), declared as `vote_values`.
    """
    name: str
    field: str                                      # persona field to aggregate
    buckets: list[dict[str, Any]]                   # [{name, target_pct, vote_values}, ...]
    tier: str | None = None
    source_csv: str | None = None

    @classmethod
    def from_json(cls, d: dict) -> "AggregateTarget":
        return cls(
            name=d["name"],
            field=d["field"],
            buckets=d["buckets"],
            tier=d.get("tier"),
            source_csv=d.get("source_csv"),
        )
