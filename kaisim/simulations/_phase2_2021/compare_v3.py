"""Compare v3 sim runs to baseline + ground truth for AC 095 + AC 159.

Reads each AC's most-recent runs/<ts>_2021_targeted_v3 directory (and same for
baseline 2021_targeted), pulls vote_distribution.json, and prints:
  - per-AC vote shares: predicted vs ground truth, delta
  - winner_correct flag
  - NOTA% (key bias signal)
  - top-2 absolute pp gap

Outputs a single Markdown report to v3_logs/v3_comparison.md.

Usage:
    python kaisim/simulations/_phase2_2021/compare_v3.py
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]            # kaisim/
SIMS = ROOT / "simulations"
GT_2021 = ROOT / "simulations" / "_phase2_2021" / "ground_truth_2021.yaml"
GT_2024 = ROOT / "simulations" / "_phase2_2021" / "ground_truth_2024.yaml"
OUT = ROOT / "simulations" / "_phase2_2021" / "v3_logs" / "v3_comparison.md"

ACS = [("095", "095_bangaon_uttar"), ("159", "159_bhabanipur")]
PARTIES = ["BJP", "AITC", "INC", "LF", "Other", "NOTA"]


def latest_run(ac_dir: Path, suffix: str) -> Path | None:
    runs_dir = ac_dir / "runs"
    if not runs_dir.exists():
        return None
    candidates = sorted(p for p in runs_dir.iterdir()
                        if p.is_dir() and p.name.endswith(suffix))
    return candidates[-1] if candidates else None


def load_vote_dist(run_dir: Path) -> dict[str, float] | None:
    """Vote distribution as %, parties → pct (excluding nulls)."""
    summary = run_dir / "summary.json"
    if not summary.exists():
        return None
    s = json.loads(summary.read_text())
    vd = s.get("vote_distribution", {})
    return {k: float(v) for k, v in vd.items()}


def load_truth_2021(ac_full: str) -> dict[str, float]:
    doc = yaml.safe_load(GT_2021.read_text())
    cands = doc["constituencies"][ac_full]["candidates"]
    return {p: float(d.get("pct", 0.0)) for p, d in cands.items()}


def load_truth_2024(ac_full: str) -> dict[str, float] | None:
    if not GT_2024.exists():
        return None
    doc = yaml.safe_load(GT_2024.read_text())
    if ac_full not in doc.get("constituencies", {}):
        return None
    cands = doc["constituencies"][ac_full]["candidates"]
    return {p: float(d.get("pct", 0.0)) for p, d in cands.items()}


def compare_one(ac_short: str, ac_full: str, year: int, variant_suffix: str) -> dict[str, Any]:
    sim_dir = SIMS / f"wb_2021_ac{ac_short}"
    run = latest_run(sim_dir, variant_suffix)
    pred = load_vote_dist(run) if run else None
    truth = load_truth_2021(ac_full) if year == 2021 else load_truth_2024(ac_full)

    out = {
        "ac": ac_full,
        "year": year,
        "variant": variant_suffix,
        "run_dir": str(run.relative_to(SIMS)) if run else None,
        "pred": pred,
        "truth": truth,
    }
    if pred and truth:
        rows = []
        for p in PARTIES:
            t = truth.get(p, 0.0)
            r = pred.get(p, 0.0)
            rows.append({"party": p, "truth": t, "pred": r, "delta": r - t})
        out["rows"] = rows
        # winners (excluding NOTA)
        truth_winner = max((p for p in PARTIES if p != "NOTA"),
                           key=lambda p: truth.get(p, 0.0))
        pred_winner = max((p for p in PARTIES if p != "NOTA"),
                          key=lambda p: pred.get(p, 0.0))
        out["truth_winner"] = truth_winner
        out["pred_winner"] = pred_winner
        out["winner_correct"] = (pred_winner == truth_winner)
        # gaps
        out["winner_pp_gap"] = abs(pred.get(truth_winner, 0.0) - truth.get(truth_winner, 0.0))
        # top-2 gap = sum of |Δ| for top-2 ground-truth parties
        top2 = sorted(PARTIES, key=lambda p: -truth.get(p, 0.0))[:2]
        out["top2_pp_gap"] = sum(abs(pred.get(p, 0.0) - truth.get(p, 0.0)) for p in top2)
        out["nota_pred"] = pred.get("NOTA", 0.0)
        out["nota_truth"] = truth.get("NOTA", 0.0)
    return out


def fmt_row(r: dict) -> str:
    return f"| {r['party']:<7} | {r['truth']:>5.1f} | {r['pred']:>5.1f} | {r['delta']:>+5.1f} |"


def render(results: list[dict]) -> str:
    lines: list[str] = []
    lines.append("# v3 sim vs baseline + ground truth")
    lines.append("")
    for r in results:
        lines.append(f"## {r['ac']} — {r['year']} — variant `{r['variant']}`")
        lines.append("")
        if r["run_dir"] is None:
            lines.append(f"**No run found** for variant `{r['variant']}`.")
            lines.append("")
            continue
        lines.append(f"Run dir: `{r['run_dir']}`")
        if "rows" not in r:
            lines.append("No vote_distribution.json found.")
            lines.append("")
            continue
        lines.append("")
        lines.append(f"- Truth winner: **{r['truth_winner']}** | Pred winner: **{r['pred_winner']}** "
                     f"→ correct: {'✓' if r['winner_correct'] else '✗'}")
        lines.append(f"- Winner pp gap: **{r['winner_pp_gap']:.2f}**, top-2 gap: **{r['top2_pp_gap']:.2f}**")
        lines.append(f"- NOTA: pred {r['nota_pred']:.2f}% vs truth {r['nota_truth']:.2f}%")
        lines.append("")
        lines.append("| Party   | Truth |  Pred |  Δ pp |")
        lines.append("|---------|------:|------:|------:|")
        for row in r["rows"]:
            lines.append(fmt_row(row))
        lines.append("")
    return "\n".join(lines)


def main():
    results: list[dict] = []
    for ac_short, ac_full in ACS:
        # baseline 2021_targeted
        results.append(compare_one(ac_short, ac_full, 2021, "_2021_targeted"))
        # v3 2021_targeted
        results.append(compare_one(ac_short, ac_full, 2021, "_2021_targeted_v3"))
        # 2024 LS v3 (will be empty until we run it)
        results.append(compare_one(ac_short, ac_full, 2024, "_2024_ls_targeted_v3"))

    text = render(results)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text)
    print(text)
    print(f"\n[wrote {OUT}]")


if __name__ == "__main__":
    main()
