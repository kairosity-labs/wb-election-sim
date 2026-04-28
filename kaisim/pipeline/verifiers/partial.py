"""Partial verifier — `verify_population` with graceful handling for the
data-coverage gaps that are normal when a per-AC config is built mechanically
from heterogeneous calibrated_2019 CSVs.

The standard verifier (`composite.verify_population`) assumes:
  - every joint table covers every parent value present in the population
  - every aggregate-target bucket maps to at least one populated field value

For per-AC configs synthesized from CSVs (where a Joint's parent might be
"caste" but the joint table only spans a subset of the AC's caste palette),
those assumptions don't hold. The standard verifier would flag parent values
absent from the joint as 0% target — turning every missing cell into a hard
fail.

This module wraps the same machinery but:
  - filters joint tables to only the parent values that appear BOTH in the
    AC's axis (legal sample space) AND the joint table (data we have)
  - rebuilds the joint with this filtered table before invoking verify_joint
  - filters aggregate-target buckets to only those whose `vote_values` are
    a subset of the field's known categories
  - never penalizes missing data; instead each filtered-out cell is reported
    as `partial_skip` in the GapReport.

Use this verifier when validating populations sampled against per-AC starter
configs. As an AC matures (extensions hand-written, joints fully audited),
you can graduate back to the standard `verify_population`.
"""
from __future__ import annotations

import copy
from dataclasses import dataclass
from pathlib import Path

from ..core.config import SimulationContext
from ..core.joint import AggregateTarget, Joint
from ..core.persona import Persona
from .base import GapReport, JointGap
from .composite import (DEFAULT_TIER_WEIGHTS, DEFAULT_TOLERANCE,
                          _tier_weight, verify_population)
from .joint import verify_joint
from .marginal import verify_axis
from .aggregate import verify_aggregate


@dataclass
class PartialReport:
    """Augments GapReport with coverage telemetry."""
    report: GapReport
    skipped_joints: list[dict]
    """[{joint_name, reason, parent_values_dropped}]"""
    skipped_buckets: list[dict]
    """[{aggregate_name, bucket, reason}]"""

    def headline(self) -> dict:
        h = self.report.headline()
        h["skipped_joints"] = len(self.skipped_joints)
        h["skipped_buckets"] = len(self.skipped_buckets)
        return h


# ---------------------------------------------------------------------------
# Filtering: trim joint tables / aggregate buckets to data we have
# ---------------------------------------------------------------------------

def _axis_value_space(ctx: SimulationContext) -> dict[str, set[str]]:
    """For each partition/derived axis, return the set of legal category codes."""
    out: dict[str, set[str]] = {}
    for a in ctx.axes:
        if a.kind in ("partition", "derived") and a.categories:
            out[a.name] = set(a.categories)
        elif a.kind == "flag" and a.flags:
            out[a.name] = set(a.flags)
    return out


def _filter_joint_to_axis(joint: Joint, axis_values: dict[str, set[str]]
                           ) -> tuple[Joint, list[str]]:
    """Return a new Joint whose `table` only contains parent-value tuples that
    are valid in the AC's axes. Drops parent values present in the joint's
    table but not in the corresponding axis's value space (i.e., joint
    references a category that this AC doesn't actually have).

    Returns (filtered_joint, dropped_parent_values).
    """
    if not joint.parents:
        return joint, []
    new_table: dict = {}
    dropped: list[str] = []
    for pv, cells in joint.table.items():
        if isinstance(pv, tuple):
            keep = all(p in axis_values.get(parent, set())
                       for p, parent in zip(pv, joint.parents))
        else:
            parent = joint.parents[0]
            keep = pv in axis_values.get(parent, set())
        if keep:
            new_table[pv] = cells
        else:
            dropped.append(str(pv))
    new_joint = copy.copy(joint)
    new_joint.table = new_table
    return new_joint, dropped


def _filter_aggregate_to_population(target: AggregateTarget,
                                     personas: list[Persona]
                                     ) -> tuple[AggregateTarget, list[dict]]:
    """Drop buckets whose `vote_values` don't appear in any persona's field.
    These are unrecoverable — the bucket's target party doesn't exist in
    this population's value space."""
    seen = set()
    for p in personas:
        v = p.get(target.field)
        if v is not None:
            seen.add(v)
    kept: list[dict] = []
    dropped: list[dict] = []
    for b in target.buckets:
        vote_values = set(b.get("vote_values", [b["name"]]))
        if vote_values & seen:
            kept.append(b)
        else:
            dropped.append({
                "aggregate_name": target.name,
                "bucket": b.get("name"),
                "reason": (f"vote_values={sorted(vote_values)} not present in "
                           f"sampled population (field={target.field})"),
            })
    new_target = copy.copy(target)
    new_target.buckets = kept
    return new_target, dropped


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def verify_partial_population(
    ctx: SimulationContext,
    personas: list[Persona],
    tolerance: dict[str, float] | None = None,
    tier_weights: dict[str, float] | None = None,
) -> PartialReport:
    """Like composite.verify_population but tolerant of partial joints +
    partial aggregate buckets. Skipped items are surfaced separately in
    the returned PartialReport rather than penalized."""
    tol = {**DEFAULT_TOLERANCE, **(tolerance or {})}
    tw = {**DEFAULT_TIER_WEIGHTS, **(tier_weights or {})}

    axis_values = _axis_value_space(ctx)

    # 1. Axes — unchanged.
    axis_gaps = [
        verify_axis(a, personas, tol)
        for a in ctx.axes
        if a.is_sampleable() and a.kind != "scalar"
    ]

    # 2. Joints — filter each to axis-legal parent values, then verify.
    joint_gaps: list[JointGap] = []
    skipped_joints: list[dict] = []
    for j in ctx.joints:
        if not j.is_for_verifying():
            continue
        filtered, dropped = _filter_joint_to_axis(j, axis_values)
        if not filtered.table:
            # Whole joint unrecoverable — skip with reason.
            gap = JointGap(joint=j.name, parents=j.parents, child=j.child,
                            semantics=j.semantics, tier=j.tier)
            gap.skipped_reason = (
                f"all parent values absent from axes "
                f"(dropped: {dropped[:5]}{'...' if len(dropped) > 5 else ''})"
            )
            joint_gaps.append(gap)
            skipped_joints.append({
                "joint_name": j.name, "reason": gap.skipped_reason,
                "parent_values_dropped": dropped,
            })
            continue
        if dropped:
            skipped_joints.append({
                "joint_name": j.name,
                "reason": f"{len(dropped)} parent value(s) dropped — "
                          "not in this AC's axis value-space",
                "parent_values_dropped": dropped,
            })
        gap = verify_joint(filtered, personas, tol)
        joint_gaps.append(gap)

    # 3. Aggregate targets — filter buckets to those present in population.
    agg_gaps = []
    skipped_buckets: list[dict] = []
    for t in ctx.aggregate_targets:
        filtered_t, dropped = _filter_aggregate_to_population(t, personas)
        skipped_buckets.extend(dropped)
        if filtered_t.buckets:
            agg_gaps.append(verify_aggregate(filtered_t, personas, tol))

    # Compose composite score and tolerance verdict.
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
        and all(j.skipped_reason is not None or j.max_abs_z <= z_max
                for j in joint_gaps)
        and all(ag.max_abs_z <= z_max for ag in agg_gaps)
        and score <= tol["composite_chisq_max"]
    )

    return PartialReport(
        report=GapReport(
            n=len(personas),
            axis_gaps=axis_gaps,
            joint_gaps=joint_gaps,
            aggregate_gaps=agg_gaps,
            composite_score=round(score, 2),
            within_tolerance=within,
            tolerance_used=tol,
            tier_weights_used=tw,
        ),
        skipped_joints=skipped_joints,
        skipped_buckets=skipped_buckets,
    )


# ---------------------------------------------------------------------------
# Convenience: load + verify in one step
# ---------------------------------------------------------------------------

def verify_ac_partial(
    sim_dir: str | Path,
    personas: list[Persona],
    tolerance: dict[str, float] | None = None,
    tier_weights: dict[str, float] | None = None,
) -> PartialReport:
    """Load `simulations/wb_2021_ac<NN>/` and run partial verification."""
    ctx = SimulationContext.load(sim_dir)
    return verify_partial_population(ctx, personas, tolerance, tier_weights)


def render_partial_md(report: PartialReport, *, top_k_gaps: int = 10) -> str:
    """Human-readable partial verification report."""
    from .composite import render_md  # reuse the standard renderer
    base = render_md(report.report, top_k_gaps=top_k_gaps)
    extra = ["", "## Partial-coverage telemetry", ""]
    if report.skipped_joints:
        extra.append("### Skipped / partial joints")
        extra.append("| joint | reason | n parent values dropped |")
        extra.append("|---|---|---|")
        for s in report.skipped_joints:
            n_dropped = len(s.get("parent_values_dropped", []))
            extra.append(f"| {s['joint_name']} | {s['reason']} | {n_dropped} |")
    else:
        extra.append("All joints fully covered.")
    extra.append("")
    if report.skipped_buckets:
        extra.append("### Skipped aggregate buckets")
        extra.append("| aggregate | bucket | reason |")
        extra.append("|---|---|---|")
        for s in report.skipped_buckets:
            extra.append(f"| {s['aggregate_name']} | {s['bucket']} | "
                          f"{s['reason']} |")
    else:
        extra.append("All aggregate buckets recoverable.")
    return base + "\n" + "\n".join(extra)
