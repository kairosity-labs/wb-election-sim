"""Aggregate verifier — bucket sums vs scalar targets.

Used for the AC-95 calibration target: the per-party vote share over the
whole population should match the published 2019 LS Bangaon segment estimate
(BJP=48, AITC=44, Left+INC=6, Other/NOTA=2) within tolerance.

Each bucket may sum over multiple field values (e.g., Left+INC = INC + LF).
"""
from __future__ import annotations

from ..core.joint import AggregateTarget
from ..core.persona import Persona
from .base import AggregateGap, standard_error_pp, z_from_gap


def verify_aggregate(target: AggregateTarget, personas: list[Persona],
                     tolerance: dict[str, float]) -> AggregateGap:
    gap = AggregateGap(name=target.name, field=target.field, tier=target.tier)
    n = len(personas)
    if n == 0:
        return gap
    z_max = float(tolerance.get("cell_z_max", 2.5))

    for bucket in target.buckets:
        vote_values = set(bucket["vote_values"])
        obs_count = sum(1 for p in personas if p.get(target.field) in vote_values)
        obs = obs_count / n * 100
        tgt = float(bucket["target_pct"])
        g = obs - tgt
        se = standard_error_pp(tgt, n)
        z = z_from_gap(obs, tgt, n)
        in_tol = abs(z) <= z_max
        gap.buckets.append({
            "name": bucket["name"],
            "vote_values": bucket["vote_values"],
            "target_pct": round(tgt, 2),
            "observed_pct": round(obs, 2),
            "gap_pp": round(g, 2),
            "se_pp": round(se, 3),
            "z": round(z, 2),
            "in_tol": in_tol,
        })
        gap.max_abs_gap_pp = max(gap.max_abs_gap_pp, abs(g))
        gap.max_abs_z = max(gap.max_abs_z, abs(z))
        gap.chisq_sum += z * z
        if not in_tol:
            gap.n_out_of_tol += 1
    return gap
