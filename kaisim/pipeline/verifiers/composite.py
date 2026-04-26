"""Composite verifier — runs all three passes and produces one GapReport.

The composite score is **Pearson chi-square** (sum of z²) tier-weighted:

    score = sum_axis    (tier_weight[axis.tier]    * axis.chisq_sum)
          + sum_joint   (tier_weight[joint.tier]   * joint.chisq_sum)
          + sum_aggrgt  (tier_weight[agg.tier]     * agg.chisq_sum)

where each cell contributes z² = ((observed_pct - target_pct) / SE_pp)² and
SE_pp is the binomial standard error at the cell's effective n. This is the
principled successor to summing raw pp-gaps: small-n cells (large SE → small
z) automatically contribute less, so sampling noise on rare buckets no longer
dominates the score.

A population is `within_tolerance` iff:
    - every cell |z| ≤ cell_z_max         (cell-level statistical sig)
    - composite_score ≤ composite_chisq_max (whole-population test)

cell_z_max default = 2.5 (≈ 99% two-sided CI; conservative).
composite_chisq_max default = 1500.0 — calibrated so a well-fit n=1000
population (most cells |z|<2.5, a handful of plugin-driven biases) passes,
but a population with many systematically-shifted cells fails.

Raw pp gaps remain visible in every cell dict for human readability and as
a back-compat path; only the score formula and tolerance check use z.
"""
from __future__ import annotations

from ..core.config import SimulationContext
from ..core.persona import Persona
from .base import GapReport
from .marginal import verify_axis
from .joint import verify_joint
from .aggregate import verify_aggregate


DEFAULT_TIER_WEIGHTS = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.5, "E": 1.0, None: 1.0}
DEFAULT_TOLERANCE = {
    # Per-cell statistical-significance threshold. |z|=2.5 ≈ 99% two-sided CI.
    "cell_z_max": 2.5,
    # Whole-population test. Pure-noise expectation is roughly N_cells *
    # avg_tier_weight (≈ 486 in the WB sim with 324 cells and weights
    # avg ≈ 1.5). 800 leaves ~64% headroom for natural variation; populations
    # with multiple systematically-shifted cells will exceed it.
    "composite_chisq_max": 800.0,
    # Legacy pp tolerances kept for reporting only; not used in the score.
    "tier_A_axis_pp": 2.0,
    "tier_BC_axis_pp": 3.0,
    "tier_DE_axis_pp": 4.0,
    "joint_cell_pp": 5.0,
    "aggregate_vote_pp": 2.0,
}


def _tier_weight(tier: str | None, weights: dict[str, float]) -> float:
    return weights.get(tier or "E", weights.get(None, 1.0))


def verify_population(
    ctx: SimulationContext,
    personas: list[Persona],
    tolerance: dict[str, float] | None = None,
    tier_weights: dict[str, float] | None = None,
) -> GapReport:
    tol = {**DEFAULT_TOLERANCE, **(tolerance or {})}
    tw = {**DEFAULT_TIER_WEIGHTS, **(tier_weights or {})}

    axis_gaps = [
        verify_axis(a, personas, tol)
        for a in ctx.axes
        if a.is_sampleable() and a.kind != "scalar"
    ]
    joint_gaps = [verify_joint(j, personas, tol) for j in ctx.joints if j.is_for_verifying()]
    agg_gaps = [verify_aggregate(t, personas, tol) for t in ctx.aggregate_targets]

    score = 0.0
    for a in axis_gaps:
        score += _tier_weight(a.tier, tw) * a.chisq_sum
    for j in joint_gaps:
        if j.skipped_reason is None:
            score += _tier_weight(j.tier, tw) * j.chisq_sum
    for ag in agg_gaps:
        score += _tier_weight(ag.tier, tw) * ag.chisq_sum

    z_max = float(tol["cell_z_max"])
    within = (
        all(a.max_abs_z <= z_max for a in axis_gaps)
        and all(j.skipped_reason is not None or j.max_abs_z <= z_max for j in joint_gaps)
        and all(ag.max_abs_z <= z_max for ag in agg_gaps)
        and score <= tol["composite_chisq_max"]
    )

    return GapReport(
        n=len(personas),
        axis_gaps=axis_gaps,
        joint_gaps=joint_gaps,
        aggregate_gaps=agg_gaps,
        composite_score=round(score, 2),
        within_tolerance=within,
        tolerance_used=tol,
        tier_weights_used=tw,
    )


def render_md(report: GapReport, *, top_k_gaps: int = 8) -> str:
    """Human-readable per-batch report."""
    lines = []
    h = report.headline()
    lines.append(f"# Verifier report (n={h['n']})")
    lines.append("")
    lines.append(f"- composite chi-square: **{h['composite_score']}** "
                 f"(max allowed: {report.tolerance_used['composite_chisq_max']})")
    lines.append(f"- within tolerance: **{h['within_tolerance']}**")
    lines.append(f"- max axis |z|: {h['max_axis_z']}  · max joint cell |z|: {h['max_joint_z']}  "
                 f"· aggregate vote max |z|: {h['aggregate_vote_max_z']}")
    lines.append(f"- max axis gap: {h['max_axis_gap_pp']} pp  · max joint cell gap: "
                 f"{h['max_joint_cell_gap_pp']} pp  · aggregate max gap: "
                 f"{h['aggregate_vote_max_gap_pp']} pp")
    lines.append(f"- cell tolerance: |z| ≤ {report.tolerance_used['cell_z_max']}")
    lines.append("")

    lines.append("## Axes (sorted by max |z|)")
    lines.append("| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |")
    lines.append("|---|---|---|---|---|---|")
    for a in sorted(report.axis_gaps, key=lambda x: -x.max_abs_z):
        lines.append(f"| {a.axis} | {a.tier} | {a.max_abs_z:.2f} | {a.max_abs_gap_pp:.2f} "
                     f"| {a.chisq_sum:.1f} | {a.n_out_of_tol} |")
    lines.append("")

    flat = []
    for a in report.axis_gaps:
        for r in a.rows:
            flat.append((a.axis, r["category"], r["target_pct"],
                         r["observed_pct"], r["gap_pp"], r["z"]))
    flat.sort(key=lambda t: -abs(t[5]))
    lines.append(f"## Top {top_k_gaps} category gaps (by |z|)")
    lines.append("| axis | category | target | observed | gap_pp | z |")
    lines.append("|---|---|---|---|---|---|")
    for axis, cat, tgt, obs, g, z in flat[:top_k_gaps]:
        lines.append(f"| {axis} | {cat} | {tgt} | {obs} | {g:+.2f} | {z:+.2f} |")
    lines.append("")

    lines.append("## Joints (sorted by max cell |z|)")
    lines.append("| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |")
    lines.append("|---|---|---|---|---|---|---|")
    for j in sorted(report.joint_gaps, key=lambda x: -x.max_abs_z):
        sk = j.skipped_reason or ""
        lines.append(f"| {j.joint} | {j.tier} | {j.max_abs_z:.2f} | {j.max_abs_cell_gap_pp:.2f} "
                     f"| {j.chisq_sum:.1f} | {j.n_out_of_tol} | {sk} |")
    lines.append("")

    if report.aggregate_gaps:
        lines.append("## Aggregate vote share")
        for ag in report.aggregate_gaps:
            lines.append(f"### {ag.name} (tier {ag.tier})  max |z| = {ag.max_abs_z:.2f}")
            lines.append("| bucket | target | observed | gap_pp | z | in_tol |")
            lines.append("|---|---|---|---|---|---|")
            for b in ag.buckets:
                lines.append(f"| {b['name']} | {b['target_pct']} | {b['observed_pct']} "
                             f"| {b['gap_pp']:+.2f} | {b['z']:+.2f} | {b['in_tol']} |")
            lines.append("")

    return "\n".join(lines)
