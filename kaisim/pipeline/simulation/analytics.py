"""Aggregate analytics for a completed simulation run.

Reads the run directory's per-agent artifacts and produces:
  - vote_flow_by_period.csv     vote-intent timeseries via reflection extraction
  - vote_distribution.json      final-vote distribution
  - ignore_rate_by_demographic.csv  who tends to dismiss news
  - plots/vote_evolution.png    visual final-vote vs ground-truth
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def vote_distribution(run_root: Path, ground_truth: dict[str, float] | None = None) -> dict:
    run_root = Path(run_root)
    votes = Counter()
    n = 0
    for agent_dir in (run_root / "agents").iterdir():
        if not agent_dir.is_dir():
            continue
        fv = agent_dir / "final_vote.json"
        if fv.exists():
            d = json.loads(fv.read_text())
            votes[d.get("vote", "ABSENT")] += 1
            n += 1
    pct = {k: round(100 * v / max(n, 1), 1) for k, v in votes.items()}
    out = {"n": n, "counts": dict(votes), "pcts": pct}
    if ground_truth:
        out["ground_truth_pcts"] = ground_truth
        out["abs_gap_pp"] = {
            k: round(abs(pct.get(k, 0) - ground_truth.get(k, 0)), 1)
            for k in set(pct) | set(ground_truth)
        }
    (run_root / "vote_distribution.json").write_text(json.dumps(out, indent=2))
    return out


def ignore_rate_by_demographic(run_root: Path) -> dict:
    """For each demographic axis, compute average ignore-rate per category."""
    run_root = Path(run_root)
    by_field: dict[str, dict[str, list[float]]] = {}
    for agent_dir in (run_root / "agents").iterdir():
        if not agent_dir.is_dir():
            continue
        persona = json.loads((agent_dir / "persona.json").read_text())
        fields = persona.get("fields", {})
        feeds_path = agent_dir / "feeds.jsonl"
        if not feeds_path.exists():
            continue
        feeds = [json.loads(line) for line in feeds_path.read_text().splitlines() if line.strip()]
        if not feeds:
            continue
        ignore_rate = sum(1 for f in feeds if not f["accepted"]) / len(feeds)
        for field_name in ("religion", "caste", "gender", "age_cohort", "gp_location",
                            "education", "workforce_status", "economic_status"):
            v = fields.get(field_name)
            if v is None or isinstance(v, dict):
                continue
            by_field.setdefault(field_name, {}).setdefault(str(v), []).append(ignore_rate)

    out = {}
    for fname, by_cat in by_field.items():
        out[fname] = {cat: round(sum(rates) / len(rates), 3) for cat, rates in by_cat.items()}
    (run_root / "ignore_rate_by_demographic.json").write_text(json.dumps(out, indent=2))
    return out


def plot_vote_distribution(run_root: Path, ground_truth: dict[str, float] | None = None) -> Path:
    run_root = Path(run_root)
    out_path = run_root / "plots" / "vote_distribution.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    dist = vote_distribution(run_root, ground_truth=ground_truth)
    pcts = dist["pcts"]

    parties = ["BJP", "AITC", "INC", "LF", "Other", "NOTA"]
    obs = [pcts.get(p, 0) for p in parties]

    fig, ax = plt.subplots(figsize=(8, 5))
    x = list(range(len(parties)))
    width = 0.4

    if ground_truth:
        gt = [ground_truth.get(p, 0) for p in parties]
        ax.bar([i - width / 2 for i in x], gt, width=width, label="ground truth (2024 LS)",
               color="#4C72B0", edgecolor="white")
        ax.bar([i + width / 2 for i in x], obs, width=width, label="simulated",
               color="#DD8452", edgecolor="white")
    else:
        ax.bar(x, obs, width=width * 1.5, label="simulated",
               color="#DD8452", edgecolor="white")

    for i, v in enumerate(obs):
        ax.text(i + (width / 2 if ground_truth else 0), v + 0.5, f"{v:.1f}",
                ha="center", fontsize=9)
    if ground_truth:
        for i, v in enumerate(gt):
            ax.text(i - width / 2, v + 0.5, f"{v:.1f}", ha="center", fontsize=9)

    ax.set_xticks(x)
    ax.set_xticklabels(parties)
    ax.set_ylabel("% of personas")
    ax.set_title(f"Final 2024 LS vote distribution (n={dist['n']})", fontweight="bold")
    ax.legend()
    ax.grid(axis="y", linestyle=":", alpha=0.5)
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    return out_path


def run_all(run_root: Path, ground_truth: dict[str, float] | None = None) -> dict:
    run_root = Path(run_root)
    summary = {
        "vote_distribution": vote_distribution(run_root, ground_truth=ground_truth),
        "ignore_rate_by_demographic": ignore_rate_by_demographic(run_root),
        "plots": [str(plot_vote_distribution(run_root, ground_truth=ground_truth))],
    }
    return summary
