"""Marginal verifier — per-axis category/flag pct gaps + z-scores.

For each axis:
    partition  — count personas with each category, divide by n, compare to
                 axis.marginal[category]. Subgroup rollups also reported.
    flag       — for each flag, mean of personas[flag] vs axis.rates[flag].
    derived    — same as partition (if categories declared) or flag (if flags
                 declared). Targets with marginal=None / rates=None are
                 skipped (no comparison possible).
    scalar     — skipped (not per-persona).

Each row is annotated with both raw pp gap and a z-score = gap / SE where
SE is the binomial standard error at sample n. The cell-level tolerance is
|z| ≤ cell_z_max (default 2.5). The Pearson chi-square sum (Σz²) per axis
is what feeds the composite score.
"""
from __future__ import annotations

from ..core.axis import Axis
from ..core.persona import Persona
from .base import AxisGap, standard_error_pp, z_from_gap


def verify_axis(axis: Axis, personas: list[Persona], tolerance: dict[str, float]) -> AxisGap:
    gap = AxisGap(axis=axis.name, kind=axis.kind, tier=axis.tier)
    if axis.kind == "derived" and not axis.marginal and not axis.rates:
        return gap
    cond = getattr(axis, "verify_condition", None)
    if cond:
        cond_field = cond["field"]
        cond_values = set(cond["values"])
        personas = [p for p in personas if p.get(cond_field) in cond_values]
    n = len(personas)
    if n == 0:
        return gap
    z_max = float(tolerance.get("cell_z_max", 2.5))

    if axis.kind == "partition" or (axis.kind == "derived" and axis.categories is not None):
        target = axis.marginal or {c: 0.0 for c in (axis.categories or [])}
        cats = list(axis.categories or target.keys())
        for cat in cats:
            obs = sum(1 for p in personas if p.get(axis.name) == cat) / n * 100
            tgt = float(target.get(cat, 0.0))
            g = obs - tgt
            se = standard_error_pp(tgt, n)
            z = z_from_gap(obs, tgt, n)
            in_tol = abs(z) <= z_max
            gap.rows.append({
                "category": cat,
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
        if axis.subgroup_rollups:
            for parent_label, leaves in axis.subgroup_rollups.items():
                obs = sum(1 for p in personas if p.get(axis.name) in leaves) / n * 100
                tgt = sum(float(target.get(c, 0.0)) for c in leaves)
                g = obs - tgt
                se = standard_error_pp(tgt, n)
                z = z_from_gap(obs, tgt, n)
                in_tol = abs(z) <= z_max
                gap.rows.append({
                    "category": parent_label + " (rollup)",
                    "target_pct": round(tgt, 2),
                    "observed_pct": round(obs, 2),
                    "gap_pp": round(g, 2),
                    "se_pp": round(se, 3),
                    "z": round(z, 2),
                    "in_tol": in_tol,
                    "is_rollup": True,
                })
                gap.max_abs_gap_pp = max(gap.max_abs_gap_pp, abs(g))
                gap.max_abs_z = max(gap.max_abs_z, abs(z))
                # Don't double-count rollups in chi-square (already counted via leaves).
                if not in_tol:
                    gap.n_out_of_tol += 1

    elif axis.kind == "flag" or (axis.kind == "derived" and axis.flags is not None):
        rates = axis.rates or {f: 0.0 for f in (axis.flags or [])}
        for flag in (axis.flags or rates.keys()):
            obs_count = 0
            for p in personas:
                v = p.get(axis.name)
                if isinstance(v, dict) and v.get(flag):
                    obs_count += 1
            obs = obs_count / n * 100
            tgt = float(rates.get(flag, 0.0))
            g = obs - tgt
            se = standard_error_pp(tgt, n)
            z = z_from_gap(obs, tgt, n)
            in_tol = abs(z) <= z_max
            gap.rows.append({
                "category": flag,
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
