"""Distribution plots — observed (population) vs target (marginal) per axis.

Produces:
    plots/marginals_partitions.png     all partition axes in a grid
    plots/marginals_flags.png          all flag axes in a grid
    plots/aggregate_vote.png           per-party aggregate vs calibration target
    plots/gap_summary.png              ranked max-abs-gap-pp per axis (which to fix first)

Usage:
    from pipeline.verifiers.plots import save_all_plots
    save_all_plots(ctx, persona_set.personas, out_dir=root / "reports" / "plots")
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ..core.axis import Axis
from ..core.config import SimulationContext
from ..core.persona import Persona


def _filtered(personas: list[Persona], axis: Axis) -> list[Persona]:
    """Honor verify_condition (e.g., occupation only among workers)."""
    cond = getattr(axis, "verify_condition", None)
    if not cond:
        return personas
    field, accept = cond["field"], set(cond["values"])
    return [p for p in personas if p.get(field) in accept]


def _axis_target_observed(axis: Axis, personas: list[Persona]) -> tuple[list[str], list[float], list[float]]:
    pop = _filtered(personas, axis)
    n = len(pop) or 1
    if axis.kind == "partition" or (axis.kind == "derived" and axis.categories):
        if not axis.marginal:
            return [], [], []
        cats = axis.categories or list(axis.marginal.keys())
        targets = [float(axis.marginal.get(c, 0.0)) for c in cats]
        observed = [
            sum(1 for p in pop if p.get(axis.name) == c) / n * 100 for c in cats
        ]
        return cats, targets, observed
    if axis.kind == "flag" or (axis.kind == "derived" and axis.flags):
        if not axis.rates:
            return [], [], []
        flags = axis.flags or list(axis.rates.keys())
        targets = [float(axis.rates.get(f, 0.0)) for f in flags]
        observed = []
        for f in flags:
            cnt = 0
            for p in pop:
                v = p.get(axis.name)
                if isinstance(v, dict) and v.get(f):
                    cnt += 1
            observed.append(cnt / n * 100)
        return flags, targets, observed
    return [], [], []


def _plot_axis(ax, axis: Axis, personas: list[Persona]):
    cats, targets, observed = _axis_target_observed(axis, personas)
    if not cats:
        ax.set_visible(False)
        return 0.0
    x = list(range(len(cats)))
    width = 0.4
    ax.bar([i - width / 2 for i in x], targets, width=width, label="target",
           color="#4C72B0", edgecolor="white")
    ax.bar([i + width / 2 for i in x], observed, width=width, label="observed",
           color="#DD8452", edgecolor="white")
    ax.set_xticks(x)
    # Truncate long labels for readability.
    short = [c if len(c) <= 18 else c[:15] + "…" for c in cats]
    ax.set_xticklabels(short, rotation=45, ha="right", fontsize=7)
    ax.set_ylabel("%", fontsize=8)
    max_gap = max(abs(t - o) for t, o in zip(targets, observed)) if targets else 0
    title = f"{axis.name}  (tier {axis.tier})  max_gap={max_gap:.1f}pp"
    ax.set_title(title, fontsize=9, fontweight="bold")
    ax.legend(fontsize=7, loc="upper right")
    ax.grid(axis="y", linestyle=":", alpha=0.5)
    return max_gap


def plot_partitions(ctx: SimulationContext, personas: list[Persona], out_path: Path):
    axes = [a for a in ctx.axes if a.is_sampleable() and a.kind != "scalar"
            and (a.kind == "partition" or (a.kind == "derived" and a.categories))]
    n_axes = len(axes)
    cols = 4
    rows = math.ceil(n_axes / cols)
    fig, ax_grid = plt.subplots(rows, cols, figsize=(cols * 4.5, rows * 3.2))
    fig.suptitle("Partition axes — target (blue) vs observed (orange)", fontsize=13, fontweight="bold")
    flat_axes = ax_grid.flatten() if n_axes > 1 else [ax_grid]
    for ax_obj, axis in zip(flat_axes, axes):
        _plot_axis(ax_obj, axis, personas)
    for ax_obj in flat_axes[n_axes:]:
        ax_obj.set_visible(False)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=110)
    plt.close(fig)


def plot_flags(ctx: SimulationContext, personas: list[Persona], out_path: Path):
    axes = [a for a in ctx.axes if a.is_sampleable()
            and (a.kind == "flag" or (a.kind == "derived" and a.flags))]
    if not axes:
        return
    n_axes = len(axes)
    cols = 2
    rows = math.ceil(n_axes / cols)
    fig, ax_grid = plt.subplots(rows, cols, figsize=(cols * 6.5, rows * 3.5))
    fig.suptitle("Flag axes — per-flag Bernoulli rate", fontsize=13, fontweight="bold")
    flat_axes = ax_grid.flatten() if n_axes > 1 else [ax_grid]
    for ax_obj, axis in zip(flat_axes, axes):
        _plot_axis(ax_obj, axis, personas)
    for ax_obj in flat_axes[n_axes:]:
        ax_obj.set_visible(False)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=110)
    plt.close(fig)


def plot_aggregate_vote(ctx: SimulationContext, personas: list[Persona], out_path: Path):
    if not ctx.aggregate_targets:
        return
    n = len(personas) or 1
    fig, axes = plt.subplots(1, len(ctx.aggregate_targets),
                             figsize=(6.5 * len(ctx.aggregate_targets), 4.5),
                             squeeze=False)
    for col, target in enumerate(ctx.aggregate_targets):
        ax = axes[0][col]
        names = [b["name"] for b in target.buckets]
        targets = [float(b["target_pct"]) for b in target.buckets]
        observed = [
            sum(1 for p in personas if p.get(target.field) in set(b["vote_values"])) / n * 100
            for b in target.buckets
        ]
        x = list(range(len(names)))
        width = 0.4
        ax.bar([i - width / 2 for i in x], targets, width=width, label="target",
               color="#4C72B0", edgecolor="white")
        ax.bar([i + width / 2 for i in x], observed, width=width, label="observed",
               color="#DD8452", edgecolor="white")
        for i, (t, o) in enumerate(zip(targets, observed)):
            ax.text(i - width / 2, t + 0.5, f"{t:.1f}", ha="center", fontsize=8)
            ax.text(i + width / 2, o + 0.5, f"{o:.1f}", ha="center", fontsize=8)
        ax.set_xticks(x)
        ax.set_xticklabels(names, rotation=20, ha="right")
        ax.set_ylabel("% of personas", fontsize=10)
        ax.set_title(f"{target.name}  (tier {target.tier})", fontsize=11, fontweight="bold")
        ax.legend()
        ax.grid(axis="y", linestyle=":", alpha=0.5)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


def plot_gap_summary(ctx: SimulationContext, personas: list[Persona], out_path: Path):
    """Horizontal bar plot of max-abs-gap per axis, sorted desc — fix-priority view."""
    rows = []
    for a in ctx.axes:
        if not a.is_sampleable() or a.kind == "scalar":
            continue
        cats, targets, observed = _axis_target_observed(a, personas)
        if not cats:
            continue
        max_gap = max(abs(t - o) for t, o in zip(targets, observed))
        rows.append((a.name, a.tier or "?", max_gap))
    rows.sort(key=lambda r: -r[2])
    if not rows:
        return
    names = [r[0] for r in rows]
    gaps = [r[2] for r in rows]
    tiers = [r[1] for r in rows]
    fig, ax = plt.subplots(figsize=(9, max(3, len(rows) * 0.32)))
    bars = ax.barh(names[::-1], gaps[::-1], color="#DD8452", edgecolor="white")
    for bar, t in zip(bars, tiers[::-1]):
        w = bar.get_width()
        ax.text(w + 0.15, bar.get_y() + bar.get_height() / 2,
                f"{w:.1f}pp  · tier {t}", va="center", fontsize=8)
    ax.set_xlabel("Max abs gap (pp) per axis")
    ax.set_title("Per-axis worst-cell gap (sorted)", fontsize=11, fontweight="bold")
    ax.grid(axis="x", linestyle=":", alpha=0.5)
    ax.set_xlim(0, max(gaps) * 1.25 if gaps else 1)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


def save_all_plots(ctx: SimulationContext, personas: list[Persona], out_dir: Path):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    plot_partitions(ctx, personas, out_dir / "marginals_partitions.png")
    plot_flags(ctx, personas, out_dir / "marginals_flags.png")
    plot_aggregate_vote(ctx, personas, out_dir / "aggregate_vote.png")
    plot_gap_summary(ctx, personas, out_dir / "gap_summary.png")
    return [
        out_dir / "marginals_partitions.png",
        out_dir / "marginals_flags.png",
        out_dir / "aggregate_vote.png",
        out_dir / "gap_summary.png",
    ]
