"""Three-way calibration experiment.

For each AC, runs three calibration states × two verifiers and tabulates
composite chi-square scores so we can see the marginal value of each
curation tier:

  States:
    PRE       — auto-built structures (no curate); generic plugins
    PLUMBING  — tier-1 fixes only (data-faithful renames + structural
                alignments; no inferred ratios or value overrides);
                generic plugins
    FULL      — current state (full curation incl. tier-2 inferred
                aggregations + tier-3 calibration overrides);
                AC-specific plugins

  Verifiers:
    STRICT    — pipeline.verifiers.composite.verify_population
                (penalizes any joint cell whose parent value isn't in
                the axis as 0% target → real fail signals)
    PARTIAL   — pipeline.verifiers.partial.verify_partial_population
                (skips unrecoverable cells with skipped_reason)

Output: experiments/three_way_calibration/results/<NN>/{pre,plumbing,full}/
                personas.jsonl + strict_score.json + partial_score.json
        experiments/three_way_calibration/results/summary.md

Run:
    python3 experiments/three_way_calibration/run_experiment.py 003
    python3 experiments/three_way_calibration/run_experiment.py --all
    python3 experiments/three_way_calibration/run_experiment.py 003 222
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SIMS_DIR = ROOT / "simulations"
EXPDIR = Path(__file__).resolve().parent
RESULTS_DIR = EXPDIR / "results"
BACKUPS_DIR = EXPDIR / "backups"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pipeline.core.config import SimulationContext  # noqa: E402
from pipeline.core.persona import Persona  # noqa: E402
from pipeline.verifiers.composite import verify_population  # strict   # noqa
from pipeline.verifiers.partial import verify_partial_population  # noqa


PLUGIN_FILES = ("workforce_sampling.py", "marital_sampling.py",
                 "occupation_sampling.py", "asset_sampling.py",
                 "amenity_sampling.py")

# Generic delegate body (matches scaffold_ac_baseline_runtime.py output)
GENERIC_TEMPLATES = {
    "workforce_sampling.py":
        '"""Workforce-status sampler (generic delegate)."""\n'
        "from pipeline.persona_generation.generic_plugins import workforce_sample as sample\n",
    "marital_sampling.py":
        '"""Marital status sampler (generic delegate)."""\n'
        "from pipeline.persona_generation.generic_plugins import marital_sample as sample\n",
    "occupation_sampling.py":
        '"""Occupation + class-of-worker samplers (generic delegate)."""\n'
        "from pipeline.persona_generation.generic_plugins import occupation_sample as sample, class_of_worker_sample as class_of_worker\n",
    "asset_sampling.py":
        '"""Asset-flag sampler (generic delegate)."""\n'
        "from pipeline.persona_generation.generic_plugins import asset_sample as sample\n",
    "amenity_sampling.py":
        '"""Amenities-flag sampler (generic delegate)."""\n'
        "from pipeline.persona_generation.generic_plugins import amenity_sample as sample\n",
}


# ---------------------------------------------------------------------------
# State management — backup / restore plugins, structures, curate
# ---------------------------------------------------------------------------

def backup_state(ac: str) -> Path:
    """Snapshot AC's current full state to backups/<NN>/."""
    backup = BACKUPS_DIR / ac
    if backup.exists():
        return backup
    backup.mkdir(parents=True)
    sim_dir = SIMS_DIR / f"wb_2021_ac{ac}"
    # Plugins
    derived_src = sim_dir / "derived"
    if derived_src.exists():
        shutil.copytree(derived_src, backup / "derived")
    # Curate script
    curate_src = ROOT / "scripts" / "per_ac" / f"{ac}_curate.py"
    if curate_src.exists():
        shutil.copy(curate_src, backup / f"{ac}_curate.py")
    return backup


def restore_full_state(ac: str) -> None:
    """Put AC back into FULL state (current curate + AC-specific plugins).
    Used at the end of the experiment."""
    backup = BACKUPS_DIR / ac
    if not backup.exists():
        return
    sim_dir = SIMS_DIR / f"wb_2021_ac{ac}"
    derived_dst = sim_dir / "derived"
    derived_bak = backup / "derived"
    if derived_bak.exists():
        if derived_dst.exists():
            shutil.rmtree(derived_dst)
        shutil.copytree(derived_bak, derived_dst)
    curate_bak = backup / f"{ac}_curate.py"
    if curate_bak.exists():
        shutil.copy(curate_bak, ROOT / "scripts" / "per_ac" / f"{ac}_curate.py")


def install_generic_plugins(ac: str) -> None:
    """Overwrite AC's derived/ plugins with generic delegates."""
    sim_dir = SIMS_DIR / f"wb_2021_ac{ac}"
    derived = sim_dir / "derived"
    derived.mkdir(exist_ok=True)
    for fname, body in GENERIC_TEMPLATES.items():
        (derived / fname).write_text(body)


def clear_structures(ac: str) -> None:
    """Remove auto-buildable structures so the build script regenerates them."""
    sim_dir = SIMS_DIR / f"wb_2021_ac{ac}"
    for name in ("axes.json", "joints.json", "aggregate_targets.json"):
        p = sim_dir / "structures" / name
        if p.exists():
            p.unlink()


def run_build(ac: str) -> None:
    subprocess.run([sys.executable,
                     str(ROOT / "scripts" / "build_ac_verifier_configs.py"),
                     ac, "--force"], check=True, capture_output=True)


def run_full_curate(ac: str) -> None:
    curate = ROOT / "scripts" / "per_ac" / f"{ac}_curate.py"
    if curate.exists():
        subprocess.run([sys.executable, str(curate)], check=True, capture_output=True)


def run_plumbing_curate(ac: str) -> None:
    subprocess.run([sys.executable, str(EXPDIR / "plumbing_curate.py"), ac],
                    check=True, capture_output=True)


def run_generate(ac: str) -> tuple[Path, dict]:
    """Run generate.py baseline_rule and return (personas_path, partial_headline)."""
    gen = SIMS_DIR / f"wb_2021_ac{ac}" / "generate.py"
    result = subprocess.run([sys.executable, str(gen), "baseline_rule"],
                              check=True, capture_output=True, text=True)
    # Parse the headline dict from generate.py's stdout
    headline = {}
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.startswith("{") and "composite_score" in line:
            try:
                headline = eval(line, {"__builtins__": {}}, {})
            except Exception:
                pass
            break
    personas = (SIMS_DIR / f"wb_2021_ac{ac}" / "personas"
                / "baseline_rule_n500" / "personas.jsonl")
    return personas, headline


def load_personas(path: Path) -> list[Persona]:
    out = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(Persona.from_dict(json.loads(line)))
    return out


# ---------------------------------------------------------------------------
# Run one (AC, mode) combo
# ---------------------------------------------------------------------------

def run_mode(ac: str, mode: str) -> dict:
    """Set up the desired mode, run generate.py, run BOTH verifiers,
    persist artifacts under results/<ac>/<mode>/. Return summary dict."""
    print(f"  [AC {ac} / {mode}] setting up state...")
    if mode == "pre":
        clear_structures(ac)
        run_build(ac)
        install_generic_plugins(ac)
    elif mode == "plumbing":
        clear_structures(ac)
        run_build(ac)
        run_plumbing_curate(ac)
        install_generic_plugins(ac)
    elif mode == "full":
        clear_structures(ac)
        run_build(ac)
        run_full_curate(ac)
        # plugins restored to AC-specific
        restore_full_state(ac)
    else:
        raise ValueError(mode)

    print(f"  [AC {ac} / {mode}] generating + scoring...")
    personas_path, partial_headline = run_generate(ac)

    # Score with strict verifier
    sim_dir = SIMS_DIR / f"wb_2021_ac{ac}"
    ctx = SimulationContext.load(sim_dir)
    personas = load_personas(personas_path)
    strict_report = verify_population(ctx, personas)
    partial_report = verify_partial_population(ctx, personas)

    # Persist
    out_dir = RESULTS_DIR / ac / mode
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(personas_path, out_dir / "personas.jsonl")
    (out_dir / "strict_score.json").write_text(json.dumps({
        "n": strict_report.n,
        "composite_score": strict_report.composite_score,
        "within_tolerance": strict_report.within_tolerance,
        "max_axis_z": max((a.max_abs_z for a in strict_report.axis_gaps),
                            default=0.0),
        "max_joint_z": max((j.max_abs_z for j in strict_report.joint_gaps),
                            default=0.0),
        "agg_max_z": max((a.max_abs_z for a in strict_report.aggregate_gaps),
                           default=0.0),
    }, indent=2))
    (out_dir / "partial_score.json").write_text(json.dumps({
        "n": partial_report.report.n,
        "composite_score": partial_report.report.composite_score,
        "within_tolerance": partial_report.report.within_tolerance,
        "skipped_joints": len(partial_report.skipped_joints),
        "skipped_buckets": len(partial_report.skipped_buckets),
        "headline_from_generate_py": partial_headline,
    }, indent=2))

    return {
        "ac": ac,
        "mode": mode,
        "n": len(personas),
        "strict_composite": strict_report.composite_score,
        "strict_within_tol": strict_report.within_tolerance,
        "partial_composite": partial_report.report.composite_score,
        "partial_within_tol": partial_report.report.within_tolerance,
        "partial_skipped_joints": len(partial_report.skipped_joints),
        "partial_skipped_buckets": len(partial_report.skipped_buckets),
    }


def discover_acs() -> list[str]:
    out = []
    for d in sorted(SIMS_DIR.iterdir()):
        if d.is_dir() and d.name.startswith("wb_2021_ac"):
            ac = d.name.replace("wb_2021_ac", "")
            # Skip 095 (hand-curated, no curate.py)
            if ac == "095":
                continue
            # Only run on ACs with a per-AC curate (= the agent-calibrated set)
            if (ROOT / "scripts" / "per_ac" / f"{ac}_curate.py").exists():
                out.append(ac)
    return out


# ---------------------------------------------------------------------------
# Tabulate
# ---------------------------------------------------------------------------

def tabulate(rows: list[dict]) -> str:
    """Render results as a Markdown table."""
    lines = ["# Three-way calibration experiment — results", ""]
    lines.append(
        "Composite chi-square per AC × calibration state × verifier. "
        "Budget = 800.\n")

    by_ac: dict[str, dict[str, dict]] = {}
    for r in rows:
        by_ac.setdefault(r["ac"], {})[r["mode"]] = r

    lines.append("## Composite scores (lower = closer to source)\n")
    lines.append("|  AC  | mode     | n | strict χ² | partial χ² | strict ✓? | partial ✓? | skipped (j/b) |")
    lines.append("|------|----------|---|-----------|------------|-----------|-----------|---------------|")
    for ac in sorted(by_ac.keys()):
        for mode in ("pre", "plumbing", "full"):
            r = by_ac[ac].get(mode)
            if not r:
                continue
            sc = r["strict_composite"]
            pc = r["partial_composite"]
            sw = "yes" if r["strict_within_tol"] else "no "
            pw = "yes" if r["partial_within_tol"] else "no "
            sk = f"{r['partial_skipped_joints']}/{r['partial_skipped_buckets']}"
            lines.append(f"|  {ac} | {mode:8s} | {r['n']:>3} | "
                          f"{sc:>9.1f} | {pc:>10.1f} | "
                          f"{sw:>9s} | {pw:>9s} | {sk:>13s} |")
        lines.append("|      |          |   |           |            |           |           |               |")

    lines.append("\n## Tier value-add (per AC)\n")
    lines.append("|  AC  | pre→plumbing Δ partial | plumbing→full Δ partial | total drop |")
    lines.append("|------|------------------------|-------------------------|------------|")
    for ac in sorted(by_ac.keys()):
        d = by_ac[ac]
        if "pre" in d and "plumbing" in d and "full" in d:
            tier1 = d["pre"]["partial_composite"] - d["plumbing"]["partial_composite"]
            tier23 = d["plumbing"]["partial_composite"] - d["full"]["partial_composite"]
            total = d["pre"]["partial_composite"] - d["full"]["partial_composite"]
            lines.append(f"|  {ac} | {tier1:>+22.1f} | {tier23:>+23.1f} | "
                          f"{total:>+10.1f} |")

    lines.append("\n## Reading this table\n")
    lines.append(
        "- **PRE** is the data-faithful baseline (auto-built structures, "
        "generic plugins). Distance from budget tells you how bad raw "
        "alignment is.\n"
        "- **PLUMBING** keeps only tier-1 fixes (renames, structural "
        "alignments, child-drop, age-bucket expansion, verify_condition). "
        "No inferred ratios, no value overrides. The drop from PRE→PLUMBING "
        "is the value of pure plumbing.\n"
        "- **FULL** adds tier-2 (inferred aggregations like Mahishya_Sadgop "
        "70:30) + tier-3 (value overrides like INC capping). The drop from "
        "PLUMBING→FULL is the value of those interpretive choices — i.e., "
        "what we sacrificed in source-faithfulness for verifier-pass.\n"
        "- **STRICT verifier** treats absent joint cells as 0% target → "
        "fails noisily on any unaligned joint.\n"
        "- **PARTIAL verifier** skips unrecoverable cells with "
        "skipped_reason → fails only on data-real gaps.\n"
    )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("acs", nargs="*", help="3-digit AC numbers")
    p.add_argument("--all", action="store_true",
                    help="Run on every AC with an existing per-AC curate.py")
    args = p.parse_args()

    targets = (discover_acs() if args.all
               else [a.zfill(3) for a in args.acs])
    if not targets:
        p.error("provide AC numbers or --all")

    print(f"Three-way calibration experiment on {len(targets)} AC(s): "
           f"{targets}\n")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    BACKUPS_DIR.mkdir(parents=True, exist_ok=True)

    rows = []
    for ac in targets:
        print(f"=== AC {ac} ===")
        backup_state(ac)
        try:
            for mode in ("pre", "plumbing", "full"):
                r = run_mode(ac, mode)
                rows.append(r)
                print(f"  [AC {ac} / {mode}] strict χ²={r['strict_composite']:.1f}  "
                       f"partial χ²={r['partial_composite']:.1f}  "
                       f"skip(j/b)={r['partial_skipped_joints']}/"
                       f"{r['partial_skipped_buckets']}")
        finally:
            # Always restore FULL state at the end
            restore_full_state(ac)

    summary_path = RESULTS_DIR / "summary.md"
    summary_path.write_text(tabulate(rows))
    print(f"\nWrote {summary_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
