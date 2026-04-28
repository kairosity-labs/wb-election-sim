#!/usr/bin/env python3
"""
sample_baseline_for_ac.py
Generate a quick marginal-only baseline population for any AC and score it
with the partial verifier. No plugins required — derived axes are skipped.

For each persona this samples:
  - every partition axis: independent draw from axis.marginal
  - every flag axis:      independent Bernoulli per-flag from axis.rates
  - vote_2019_LS:         drawn from vote_given_religion joint (when present)
  - all derived axes:     SKIPPED (the partial verifier handles their absence)

This is the noisiest possible baseline that still respects each axis's
1-D marginal — useful for checking that a fresh AC's verifier configs +
partial verifier work end-to-end before any plugin-driven sampler is
authored. As you add joints / per-AC plugins, the composite chi-square
should fall.

Run:
    python3 scripts/sample_baseline_for_ac.py 003           # one AC, n=500
    python3 scripts/sample_baseline_for_ac.py 003 --n 1000
    python3 scripts/sample_baseline_for_ac.py --all         # every AC
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pipeline.core.axis import Axis  # noqa: E402
from pipeline.core.config import SimulationContext  # noqa: E402
from pipeline.core.persona import Persona  # noqa: E402
from pipeline.verifiers.partial import (verify_partial_population,
                                          render_partial_md)  # noqa: E402


def sample_marginal(rng: random.Random, axis: Axis) -> str | None:
    cats = axis.categories or []
    weights = [axis.marginal.get(c, 0.0) for c in cats] if axis.marginal else []
    total = sum(weights)
    if not cats or total <= 0:
        return None
    return rng.choices(cats, weights=weights, k=1)[0]


def sample_flag(rng: random.Random, axis: Axis) -> dict[str, bool]:
    out: dict[str, bool] = {}
    for flag in (axis.flags or []):
        rate = float((axis.rates or {}).get(flag, 0.0)) / 100.0
        out[flag] = rng.random() < rate
    return out


def sample_vote_from_religion(rng: random.Random, ctx: SimulationContext,
                                religion: str | None) -> str | None:
    """Look up vote_given_religion joint (if present) and sample a party."""
    try:
        j = ctx.joint("vote_given_religion")
    except KeyError:
        return None
    table = j.table or {}
    row = table.get(religion) if religion else None
    if not row:
        # Fall back to the most populous religion's row, then first row.
        if not table:
            return None
        row = next(iter(table.values()))
    parties = list(row.keys())
    weights = list(row.values())
    if not parties or sum(weights) <= 0:
        return None
    return rng.choices(parties, weights=weights, k=1)[0]


def _build_joint_index(ctx: SimulationContext) -> dict[str, list]:
    """Index conditional joints by child axis: child → [Joint, ...] sorted by
    least-uncertain (single-parent) first."""
    out: dict[str, list] = {}
    for j in ctx.joints:
        if j.semantics != "conditional":
            continue
        out.setdefault(j.child, []).append(j)
    # Prefer single-parent joints when multiple exist for the same child.
    for child in out:
        out[child].sort(key=lambda j: len(j.parents))
    return out


def _to_float(v) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def _sample_conditional(rng: random.Random, axis: Axis, fields: dict,
                          joints_for_child: list) -> str | None:
    """Try each available joint in turn — pick the first whose parents are
    fully populated AND whose row contains a non-empty distribution."""
    for j in joints_for_child:
        parent_vals = [fields.get(p) for p in j.parents]
        if any(v is None for v in parent_vals):
            continue
        key = parent_vals[0] if len(parent_vals) == 1 else tuple(parent_vals)
        row = j.table.get(key)
        if not row:
            continue
        legal = set(axis.categories or list(row.keys()))
        filtered = [(c, _to_float(w)) for c, w in row.items() if c in legal]
        filtered = [(c, w) for c, w in filtered if w > 0]
        if not filtered:
            continue
        cats, weights = zip(*filtered)
        return rng.choices(list(cats), weights=list(weights), k=1)[0]
    return None


def sample_one(idx: int, ctx: SimulationContext, rng: random.Random,
                set_name: str, mode: str = "marginal",
                joint_index: dict | None = None) -> Persona:
    fields: dict = {}
    for axis in ctx.axes:
        if axis.kind == "partition":
            v = None
            if mode == "conditional" and joint_index and axis.name in joint_index:
                v = _sample_conditional(rng, axis, fields, joint_index[axis.name])
            if v is None:
                v = sample_marginal(rng, axis)
            if v is not None:
                fields[axis.name] = v
        elif axis.kind == "flag":
            fields[axis.name] = sample_flag(rng, axis)
        elif axis.kind == "scalar":
            fields[axis.name] = axis.value
        # derived axes: skipped (no plugin available in baseline mode)

    # Vote field — try vote_given_religion if it exists.
    vote = sample_vote_from_religion(rng, ctx, fields.get("religion"))
    if vote is not None:
        fields["vote_2019_LS"] = vote

    return Persona(id=f"{set_name}_p{idx:04d}", fields=fields)


def baseline_for_ac(ac: str, n: int = 500, seed: int = 42,
                     write_personas: bool = False,
                     mode: str = "marginal") -> dict:
    sim_dir = ROOT / "simulations" / f"wb_2021_ac{ac}"
    if not (sim_dir / "structures" / "axes.json").exists():
        return {"ac": ac, "error": f"no structures/ for AC {ac}"}

    ctx = SimulationContext.load(sim_dir)
    rng = random.Random(seed)
    set_name = f"baseline_{mode}_n{n}"
    joint_index = _build_joint_index(ctx) if mode == "conditional" else None
    personas = [sample_one(i, ctx, rng, set_name, mode=mode,
                            joint_index=joint_index) for i in range(n)]

    report = verify_partial_population(ctx, personas)
    h = report.headline()

    out_summary = {
        "ac": ac,
        "n": n,
        "axes_loaded": len(ctx.axes),
        "joints_loaded": len(ctx.joints),
        "aggregate_targets": len(ctx.aggregate_targets),
        "composite_chisq": h["composite_score"],
        "max_axis_z": h["max_axis_z"],
        "max_joint_z": h["max_joint_z"],
        "aggregate_vote_max_z": h["aggregate_vote_max_z"],
        "skipped_joints": h["skipped_joints"],
        "skipped_buckets": h["skipped_buckets"],
        "within_tolerance": h["within_tolerance"],
        "composite_chisq_max": report.report.tolerance_used["composite_chisq_max"],
    }

    # Write per-AC artifacts under personas/baseline_marginal_n<N>/
    if write_personas:
        out_dir = sim_dir / "personas" / set_name
        out_dir.mkdir(parents=True, exist_ok=True)
        with (out_dir / "personas.jsonl").open("w") as f:
            for p in personas:
                f.write(json.dumps(p.to_dict(), ensure_ascii=False) + "\n")
        (out_dir / "reports").mkdir(exist_ok=True)
        (out_dir / "reports" / "FINAL.md").write_text(render_partial_md(report))
        out_summary["written_to"] = str(out_dir.relative_to(ROOT.parent))

    return out_summary


def discover_acs() -> list[str]:
    out = []
    for d in sorted((ROOT / "simulations").iterdir()):
        if d.is_dir() and d.name.startswith("wb_2021_ac"):
            out.append(d.name.replace("wb_2021_ac", ""))
    return out


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("ac", nargs="?", default=None,
                    help="3-digit AC number")
    p.add_argument("--all", action="store_true")
    p.add_argument("--n", type=int, default=500,
                    help="Population size (default 500)")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--mode", choices=("marginal", "conditional"),
                    default="marginal",
                    help="marginal: each axis sampled independently from its "
                         "marginal (noisy baseline). "
                         "conditional: use available joints when present "
                         "(respects P(child|parent) — closer to feasible).")
    p.add_argument("--write", action="store_true",
                    help="Persist personas.jsonl + report to "
                         "simulations/wb_2021_ac<NN>/personas/baseline_<mode>_n<N>/")
    args = p.parse_args()

    targets = (discover_acs() if args.all
               else [args.ac.zfill(3)] if args.ac else [])
    if not targets:
        p.error("provide AC number or --all")
        return 2

    print(f"Generating {args.mode}-mode baseline (n={args.n}, seed={args.seed})\n")
    print(f"  {'AC':>4}  {'n':>5}  {'axes':>5}  {'jts':>4}  "
          f"{'agg':>4}  {'comp_χ²':>9}  {'budget':>7}  "
          f"{'maxAxZ':>7}  {'maxJtZ':>7}  {'voteZ':>6}  "
          f"{'skJ':>4}  {'skB':>4}  ok?")
    print(f"  {'--':>4}  {'-':>5}  {'-':>5}  {'-':>4}  {'-':>4}  "
          f"{'-' * 9:>9}  {'-' * 7:>7}  {'-' * 7:>7}  {'-' * 7:>7}  "
          f"{'-' * 6:>6}  {'-' * 4:>4}  {'-' * 4:>4}  ----")
    rows = []
    for ac in targets:
        s = baseline_for_ac(ac, n=args.n, seed=args.seed, mode=args.mode,
                             write_personas=args.write)
        if "error" in s:
            print(f"  {ac:>4}  ✗ {s['error']}")
            continue
        rows.append(s)
        print(f"  {s['ac']:>4}  {s['n']:>5}  {s['axes_loaded']:>5}  "
              f"{s['joints_loaded']:>4}  {s['aggregate_targets']:>4}  "
              f"{s['composite_chisq']:>9.1f}  "
              f"{int(s['composite_chisq_max']):>7}  "
              f"{s['max_axis_z']:>7.2f}  {s['max_joint_z']:>7.2f}  "
              f"{s['aggregate_vote_max_z']:>6.2f}  "
              f"{s['skipped_joints']:>4}  {s['skipped_buckets']:>4}  "
              f"{'✓' if s['within_tolerance'] else '✗'}")

    if rows:
        passing = sum(1 for r in rows if r["within_tolerance"])
        print(f"\n  {passing}/{len(rows)} ACs pass the composite-chisq budget.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
