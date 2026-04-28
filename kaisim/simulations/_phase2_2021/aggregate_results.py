"""Aggregate Phase-2 simulation results across (AC × variant) and produce:

  - per-AC bar plots (true vs predicted vote distribution) for each variant
  - per-variant summary CSV
  - overall accuracy table:
        for each variant: how many of 10 ACs the simulator called the correct
        winner, plus mean absolute pp-gap on the leading-party vote share

Usage:
    python kaisim/simulations/_phase2_2021/aggregate_results.py [--out OUT_DIR]

Reads from:
    kaisim/simulations/wb_2021_ac<NN>/runs/<TS>_<variant>/vote_distribution.json
    kaisim/simulations/_phase2_2021/ground_truth_2021.yaml

Each AC × variant uses the LATEST run dir (newest timestamp) so re-running
the sweep just overwrites the numbers without you having to clean older runs.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import yaml

ROOT = Path(__file__).resolve().parents[2]            # kaisim/
SIMS_DIR = ROOT / "simulations"
GT_PATH = SIMS_DIR / "_phase2_2021/ground_truth_2021.yaml"
DEFAULT_OUT = SIMS_DIR / "_phase2_2021/results"

PARTIES = ["BJP", "AITC", "INC", "LF", "Other", "NOTA"]
VARIANTS = ["2021_targeted", "2021_show_all", "2021_blind_to_prior"]


def load_ground_truth() -> dict:
    return yaml.safe_load(GT_PATH.read_text())["constituencies"]


def latest_run(ac_dir: Path, variant: str) -> Path | None:
    """Newest run directory matching this variant for this AC."""
    runs_dir = ac_dir / "runs"
    if not runs_dir.exists():
        return None
    candidates = sorted(
        [p for p in runs_dir.iterdir() if p.is_dir() and variant in p.name],
        reverse=True,
    )
    return candidates[0] if candidates else None


def predicted_pcts(run_dir: Path) -> dict | None:
    vd = run_dir / "vote_distribution.json"
    if not vd.exists():
        return None
    return json.loads(vd.read_text())


def winning_party(gt: dict) -> str:
    """The party with `won: true` in ground truth, or max-pct if not flagged."""
    for party, info in gt["candidates"].items():
        if info.get("won"):
            return party
    return max(
        gt["candidates"].items(),
        key=lambda kv: kv[1].get("pct", 0),
    )[0]


def winning_party_predicted(pred: dict) -> str:
    pcts = pred.get("pcts", {})
    if not pcts:
        return "ABSENT"
    return max(pcts.items(), key=lambda kv: kv[1])[0]


def gt_pcts(gt_for_ac: dict) -> dict[str, float]:
    return {
        party: float(info.get("pct", 0.0))
        for party, info in gt_for_ac["candidates"].items()
    }


# ---------- per-(AC, variant) plot ------------------------------------

def plot_per_ac_variant(ac_dir_name: str, variant: str, gt: dict, pred: dict,
                        out_dir: Path) -> Path:
    truths = gt_pcts(gt)
    preds = pred.get("pcts", {})

    fig, ax = plt.subplots(figsize=(8, 4.5))
    x = list(range(len(PARTIES)))
    width = 0.4

    gt_vals = [truths.get(p, 0) for p in PARTIES]
    pr_vals = [preds.get(p, 0) for p in PARTIES]

    ax.bar([i - width / 2 for i in x], gt_vals, width=width,
           label="ground truth (2021 AE)", color="#4C72B0", edgecolor="white")
    ax.bar([i + width / 2 for i in x], pr_vals, width=width,
           label="simulated", color="#DD8452", edgecolor="white")

    for i, v in enumerate(gt_vals):
        ax.text(i - width / 2, v + 0.5, f"{v:.1f}", ha="center", fontsize=8)
    for i, v in enumerate(pr_vals):
        ax.text(i + width / 2, v + 0.5, f"{v:.1f}", ha="center", fontsize=8)

    ax.set_xticks(x)
    ax.set_xticklabels(PARTIES)
    ax.set_ylabel("% of personas")

    gt_winner = winning_party(gt)
    pr_winner = winning_party_predicted(pred)
    correct = gt_winner == pr_winner
    title = (f"AC {ac_dir_name} · {variant}\n"
             f"true winner = {gt_winner}, predicted = {pr_winner}  "
             f"{'✓' if correct else '✗'}  (n={pred.get('n', 0)})")
    ax.set_title(title, fontweight="bold", fontsize=10)
    ax.legend(loc="upper right", fontsize=8)
    ax.grid(axis="y", linestyle=":", alpha=0.5)
    fig.tight_layout()

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{ac_dir_name}__{variant}.png"
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    return out_path


# ---------- per-variant accuracy summary ------------------------------

def per_variant_summary(rows: list[dict]) -> dict:
    """Compute correct-winner count and mean pp-gap on top-2 parties per variant."""
    summary = {}
    for variant in VARIANTS:
        sub = [r for r in rows if r["variant"] == variant and r["pred_pcts"] is not None]
        n = len(sub)
        if not n:
            summary[variant] = {"n_acs": 0, "winners_correct": 0,
                                "mean_winner_pp_gap": None,
                                "mean_top2_pp_gap": None}
            continue
        correct = sum(1 for r in sub if r["winner_correct"])
        winner_gaps = [abs(r["truth"][r["true_winner"]] - r["pred_pcts"].get(r["true_winner"], 0))
                       for r in sub]
        # sum |truth - pred| over top-2 parties (by truth)
        top2_gaps = []
        for r in sub:
            top2 = sorted(r["truth"].items(), key=lambda kv: -kv[1])[:2]
            gap = sum(abs(p - r["pred_pcts"].get(party, 0)) for party, p in top2)
            top2_gaps.append(gap)
        summary[variant] = {
            "n_acs": n,
            "winners_correct": f"{correct}/{n}",
            "mean_winner_pp_gap": round(sum(winner_gaps) / n, 2),
            "mean_top2_pp_gap": round(sum(top2_gaps) / n, 2),
        }
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    gts = load_ground_truth()
    rows = []

    for ac_dir_name, gt_for_ac in gts.items():
        ac_num = ac_dir_name.split("_", 1)[0]
        ac_dir = SIMS_DIR / f"wb_2021_ac{ac_num}"
        truth = gt_pcts(gt_for_ac)
        true_winner = winning_party(gt_for_ac)

        for variant in VARIANTS:
            run_dir = latest_run(ac_dir, variant)
            pred = predicted_pcts(run_dir) if run_dir else None
            pred_pcts = pred.get("pcts", {}) if pred else None

            row = {
                "ac": ac_dir_name,
                "variant": variant,
                "true_winner": true_winner,
                "truth": truth,
                "pred_pcts": pred_pcts,
                "pred_winner": winning_party_predicted(pred) if pred else "ABSENT",
                "winner_correct": (winning_party_predicted(pred) == true_winner) if pred else False,
                "n_personas": pred.get("n", 0) if pred else 0,
            }
            rows.append(row)

            if pred:
                plot_per_ac_variant(ac_dir_name, variant, gt_for_ac, pred, args.out)

    # Per-variant CSV
    with (args.out / "per_ac_variant.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ac", "variant", "true_winner", "pred_winner", "winner_correct",
                    "n_personas",
                    *[f"truth_{p}" for p in PARTIES],
                    *[f"pred_{p}" for p in PARTIES]])
        for r in rows:
            w.writerow([
                r["ac"], r["variant"], r["true_winner"], r["pred_winner"],
                r["winner_correct"], r["n_personas"],
                *[r["truth"].get(p, "") for p in PARTIES],
                *[(r["pred_pcts"] or {}).get(p, "") for p in PARTIES],
            ])

    # Variant accuracy summary
    summary = per_variant_summary(rows)
    (args.out / "summary.json").write_text(json.dumps(summary, indent=2))

    # Print to stdout for terminal review
    print(f"Wrote: {args.out}/per_ac_variant.csv")
    print(f"Wrote: {args.out}/summary.json")
    print(f"Wrote: {args.out}/<ac>__<variant>.png  ({len(rows)} plots possible)")
    print()
    print("=== Variant accuracy summary ===")
    print(f"{'variant':<24}{'n':>4}  {'winners ✓':>11}  {'mean winner pp-gap':>20}  {'top-2 pp-gap':>14}")
    for v in VARIANTS:
        s = summary[v]
        print(f"{v:<24}{s['n_acs']:>4}  {str(s['winners_correct']):>11}  "
              f"{str(s['mean_winner_pp_gap']):>20}  {str(s['mean_top2_pp_gap']):>14}")


if __name__ == "__main__":
    main()
