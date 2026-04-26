"""Verifier — measure how well a population matches the target distributions.

Three verifier passes:
    marginal   — per-axis category-wise pct gap
    joint      — per-joint cell-wise pct gap
    aggregate  — per-bucket aggregate gap (e.g., vote share vs calibration)

Each cell is scored by a **z-score** (gap_pp / standard_error_pp) where SE is
the binomial standard error at the cell's effective n. The composite score is
**Pearson chi-square** — sum of (tier_weight × z²) across all cells. This
naturally discounts small-n cells (large SE → small z → small contribution)
and keeps the tolerance threshold scale-stable as n grows.

A cell is in tolerance when |z| ≤ `cell_z_max` (default 2.5, ≈99% CI). Raw pp
gaps and SEs are also reported for human readability.

Tier weights (default):
    A: 4.0    measured/hard data
    B: 3.0    state MIS / sub-AC granularity
    C: 2.0    academic / CSDS subsample
    D: 1.5    journalistic estimate
    E: 1.0    modeled imputation
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Statistical primitives
# ---------------------------------------------------------------------------

def standard_error_pp(target_pct: float, n: int) -> float:
    """Binomial standard error in percentage-points for proportion p̂ at sample n.
    Clamps target_pct to [0.1, 99.9] to avoid degenerate SE=0 when p∈{0,1}."""
    if n <= 0:
        return float("inf")
    p = max(1e-3, min(1 - 1e-3, target_pct / 100.0))
    return math.sqrt(p * (1 - p) / n) * 100.0


def z_from_gap(observed_pct: float, target_pct: float, n: int) -> float:
    """Signed z-score: (observed - target) / SE."""
    se = standard_error_pp(target_pct, n)
    if se == 0 or se == float("inf"):
        return 0.0
    return (observed_pct - target_pct) / se


@dataclass
class AxisGap:
    axis: str
    kind: str
    tier: str | None
    rows: list[dict] = field(default_factory=list)
    """Each row: {category, target_pct, observed_pct, gap_pp, se_pp, z, in_tol}."""
    max_abs_gap_pp: float = 0.0
    max_abs_z: float = 0.0
    chisq_sum: float = 0.0
    n_out_of_tol: int = 0


@dataclass
class JointGap:
    joint: str
    parents: list[str]
    child: str
    semantics: str
    tier: str | None
    cells: list[dict] = field(default_factory=list)
    """Each cell: {parent_values, child_label, target_pct, observed_pct, gap_pp, se_pp, z, in_tol, n_in_cell}."""
    max_abs_cell_gap_pp: float = 0.0
    max_abs_z: float = 0.0
    chisq_sum: float = 0.0
    n_out_of_tol: int = 0
    skipped_reason: str | None = None


@dataclass
class AggregateGap:
    name: str
    field: str
    tier: str | None
    buckets: list[dict] = field(default_factory=list)
    """Each bucket: {name, target_pct, observed_pct, gap_pp, se_pp, z, vote_values, in_tol}."""
    max_abs_gap_pp: float = 0.0
    max_abs_z: float = 0.0
    chisq_sum: float = 0.0
    n_out_of_tol: int = 0


@dataclass
class GapReport:
    n: int
    axis_gaps: list[AxisGap]
    joint_gaps: list[JointGap]
    aggregate_gaps: list[AggregateGap]
    composite_score: float
    within_tolerance: bool
    tolerance_used: dict[str, float]
    tier_weights_used: dict[str, float]

    def headline(self) -> dict:
        return {
            "n": self.n,
            "composite_score": round(self.composite_score, 2),
            "within_tolerance": self.within_tolerance,
            "max_axis_z": round(max((a.max_abs_z for a in self.axis_gaps), default=0.0), 2),
            "max_joint_z": round(max((j.max_abs_z for j in self.joint_gaps), default=0.0), 2),
            "aggregate_vote_max_z": round(max((a.max_abs_z for a in self.aggregate_gaps), default=0.0), 2),
            "max_axis_gap_pp": round(
                max((a.max_abs_gap_pp for a in self.axis_gaps), default=0.0), 2
            ),
            "max_joint_cell_gap_pp": round(
                max((j.max_abs_cell_gap_pp for j in self.joint_gaps), default=0.0), 2
            ),
            "aggregate_vote_max_gap_pp": round(
                max((a.max_abs_gap_pp for a in self.aggregate_gaps), default=0.0), 2
            ),
        }

    def to_dict(self) -> dict:
        return {
            "n": self.n,
            "composite_score": self.composite_score,
            "within_tolerance": self.within_tolerance,
            "tolerance_used": self.tolerance_used,
            "tier_weights_used": self.tier_weights_used,
            "axis_gaps": [
                {
                    "axis": a.axis, "kind": a.kind, "tier": a.tier,
                    "max_abs_gap_pp": a.max_abs_gap_pp, "max_abs_z": a.max_abs_z,
                    "chisq_sum": a.chisq_sum,
                    "n_out_of_tol": a.n_out_of_tol, "rows": a.rows,
                }
                for a in self.axis_gaps
            ],
            "joint_gaps": [
                {
                    "joint": j.joint, "parents": j.parents, "child": j.child,
                    "semantics": j.semantics, "tier": j.tier,
                    "max_abs_cell_gap_pp": j.max_abs_cell_gap_pp, "max_abs_z": j.max_abs_z,
                    "chisq_sum": j.chisq_sum,
                    "n_out_of_tol": j.n_out_of_tol,
                    "skipped_reason": j.skipped_reason,
                    "cells": j.cells,
                }
                for j in self.joint_gaps
            ],
            "aggregate_gaps": [
                {
                    "name": a.name, "field": a.field, "tier": a.tier,
                    "max_abs_gap_pp": a.max_abs_gap_pp, "max_abs_z": a.max_abs_z,
                    "chisq_sum": a.chisq_sum,
                    "n_out_of_tol": a.n_out_of_tol, "buckets": a.buckets,
                }
                for a in self.aggregate_gaps
            ],
        }
