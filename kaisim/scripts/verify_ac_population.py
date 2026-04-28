#!/usr/bin/env python3
"""
verify_ac_population.py
Verify a sampled population for any AC against its starter verifier configs.

Loads `simulations/wb_2021_ac<NN>/structures/{axes,joints,aggregate_targets}.json`
plus a `personas.jsonl` file, runs partial-coverage-aware verification (chi-
square per axis/joint/aggregate with binomial standard errors), and writes
a Markdown report.

The "partial" wrapper handles the cases that arise naturally when configs are
mechanically derived from heterogeneous calibrated_2019 CSVs:
  - joint table parent values absent from the AC's axis (dropped, not 0%)
  - aggregate-target buckets whose vote_values aren't in the population (skipped)
  - subgroup_rollups whose leaves aren't all present (filtered)

Use original CSVs OR JSON OR a mix — the CSVs are the source of truth, the
JSON files are the runtime contract for the verifier.

Run:
    python3 scripts/verify_ac_population.py 095 \\
        simulations/wb_2021_ac095/personas/default_n100_v1/personas.jsonl

    python3 scripts/verify_ac_population.py 095 \\
        simulations/wb_2021_ac095/personas/default_n100_v1/personas.jsonl \\
        --out /tmp/ac095_partial_report.md \\
        --tolerance cell_z_max=3.0
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pipeline.core.persona import Persona  # noqa: E402
from pipeline.verifiers.partial import (verify_ac_partial,
                                          render_partial_md)  # noqa: E402


def load_personas(path: Path) -> list[Persona]:
    out: list[Persona] = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(Persona.from_dict(json.loads(line)))
    return out


def _parse_kv(s: str) -> tuple[str, float]:
    if "=" not in s:
        raise argparse.ArgumentTypeError(f"expected key=value, got {s!r}")
    k, v = s.split("=", 1)
    return k.strip(), float(v)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("ac", help="3-digit AC number (e.g. 095)")
    p.add_argument("personas_jsonl",
                    help="Path to personas.jsonl produced by Phase-1 sampler")
    p.add_argument("--out", default=None,
                    help="Output Markdown path (default: stdout)")
    p.add_argument("--tolerance", action="append", default=[],
                    type=_parse_kv, metavar="key=value",
                    help="Override tolerance keys, e.g. --tolerance cell_z_max=3.0")
    p.add_argument("--json", action="store_true",
                    help="Also dump full GapReport JSON next to the MD report")
    args = p.parse_args()

    ac = args.ac.zfill(3)
    sim_dir = ROOT / "simulations" / f"wb_2021_ac{ac}"
    if not (sim_dir / "structures" / "axes.json").exists():
        print(f"✗ No structures/ for AC {ac}. Run "
              f"`scripts/build_ac_verifier_configs.py {ac}` first.")
        return 1

    personas_path = Path(args.personas_jsonl)
    if not personas_path.exists():
        print(f"✗ {personas_path} does not exist")
        return 1

    personas = load_personas(personas_path)
    print(f"Loaded {len(personas)} personas from {personas_path.name}")

    tolerance = dict(args.tolerance)
    report = verify_ac_partial(sim_dir, personas, tolerance=tolerance)
    h = report.headline()

    print(f"\nAC {ac} partial verification:")
    print(f"  composite chi-square: {h['composite_score']}  "
          f"(max allowed: {report.report.tolerance_used['composite_chisq_max']})")
    print(f"  within tolerance:     {h['within_tolerance']}")
    print(f"  max axis |z|:         {h['max_axis_z']}")
    print(f"  max joint cell |z|:   {h['max_joint_z']}")
    print(f"  aggregate vote |z|:   {h['aggregate_vote_max_z']}")
    print(f"  skipped joints:       {h['skipped_joints']}")
    print(f"  skipped buckets:      {h['skipped_buckets']}")

    md = render_partial_md(report)
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md)
        print(f"\nWrote MD report → {out_path}")
        if args.json:
            json_path = out_path.with_suffix(".json")
            json_path.write_text(json.dumps({
                "ac": ac,
                "n": h["n"],
                "headline": h,
                "report": report.report.to_dict(),
                "skipped_joints": report.skipped_joints,
                "skipped_buckets": report.skipped_buckets,
            }, indent=2, ensure_ascii=False))
            print(f"Wrote JSON report → {json_path}")
    else:
        print()
        print(md)

    return 0 if report.report.within_tolerance else 2


if __name__ == "__main__":
    sys.exit(main())
