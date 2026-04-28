"""Distributional analysis of why our 2021_targeted simulations missed.

Tests four hypotheses:

  H1  Anchoring to 2019: predicted 2021 vote ≈ persona's vote_2019_LS prior.
      → compute switch rate (agents whose 2021 vote != 2019 prior) per AC.
      → compute correlation between 2019 distribution and predicted 2021.

  H2  NOTA over-voting: simulator emits NOTA at unrealistic rates.
      → tally NOTA share per AC and compare to 2021 truth (~0.5-2%).

  H3  Agents don't change beliefs: memory_stream is too short / events too
      sparse / engagement rate too low to actually shift opinions.
      → distribution of memory counts per agent (engaged vs ignored events).

  H4  AITC under-predicted in BJP-winning ACs: structural bias in scoring.
      → compute predicted AITC pp gap by AC, group by truth-winner.

Output: a single markdown report `bias_analysis.md` + companion CSVs.
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from statistics import mean, median, stdev

import yaml

ROOT = Path(__file__).resolve().parents[2]               # kaisim/
SIMS_DIR = ROOT / "simulations"
GT_PATH = SIMS_DIR / "_phase2_2021/ground_truth_2021.yaml"
OUT_DIR = SIMS_DIR / "_phase2_2021/results"


def load_2019_prior_distribution(persona_set_dir: Path) -> Counter:
    """Tally vote_2019_LS values across the persona set."""
    c = Counter()
    with (persona_set_dir / "personas.jsonl").open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            p = json.loads(line)
            v = p.get("fields", {}).get("vote_2019_LS")
            if v:
                c[v] += 1
    return c


def per_ac_analysis(ac_dir_name: str, gt_for_ac: dict) -> dict:
    ac_num = ac_dir_name.split("_", 1)[0]
    ac_dir = SIMS_DIR / f"wb_2021_ac{ac_num}"
    persona_set = ac_dir / "personas/local_qwen_n100"
    run_dir = sorted([p for p in (ac_dir / "runs").iterdir()
                      if "2021_targeted" in p.name], reverse=True)[0]

    # Load every persona's 2019 prior keyed by id
    prior_by_id: dict[str, str] = {}
    with (persona_set / "personas.jsonl").open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            p = json.loads(line)
            prior_by_id[p["id"]] = p.get("fields", {}).get("vote_2019_LS", "ABSENT")

    prior_dist = Counter(prior_by_id.values())

    # Load every agent's 2021 final vote (only those with final_vote.json)
    pred_by_id: dict[str, str] = {}
    memcount_by_id: dict[str, int] = {}
    for ad in (run_dir / "agents").iterdir():
        if not ad.is_dir():
            continue
        fv = ad / "final_vote.json"
        mem = ad / "memory_stream.jsonl"
        if fv.exists():
            d = json.loads(fv.read_text())
            pred_by_id[ad.name] = d.get("vote", "ABSENT")
        memcount_by_id[ad.name] = sum(1 for _ in mem.open()) if mem.exists() else 0

    pred_dist = Counter(pred_by_id.values())
    n_pred = sum(pred_dist.values())

    # H1 switch analysis
    switches = []
    same_party = 0
    switched = 0
    for aid, pred in pred_by_id.items():
        prior = prior_by_id.get(aid)
        if prior is None:
            continue
        if prior == pred:
            same_party += 1
        else:
            switched += 1
            switches.append((prior, pred))
    switch_rate = switched / max(1, same_party + switched)
    switch_breakdown = Counter(switches)

    # H2 NOTA share predicted
    nota_share = 100 * pred_dist.get("NOTA", 0) / max(1, n_pred)

    # H3 memory engagement
    mem_counts = list(memcount_by_id.values())
    mem_summary = {
        "mean": round(mean(mem_counts), 2) if mem_counts else 0,
        "median": median(mem_counts) if mem_counts else 0,
        "max": max(mem_counts) if mem_counts else 0,
        "with_zero_memories_pct": round(100 * sum(1 for c in mem_counts if c == 0) / max(1, len(mem_counts)), 1),
    }

    # H4 AITC pp gap (truth - pred)
    truth = {
        party: float(info.get("pct", 0.0))
        for party, info in gt_for_ac["candidates"].items()
    }
    pred_pcts = {p: round(100 * pred_dist.get(p, 0) / max(1, n_pred), 1) for p in truth}
    pp_gap = {p: round(pred_pcts.get(p, 0) - truth.get(p, 0), 1) for p in truth}

    # Convert prior_dist to pcts as well so we can compare directly
    n_prior = sum(prior_dist.values())
    prior_pcts = {p: round(100 * prior_dist.get(p, 0) / max(1, n_prior), 1)
                  for p in {"BJP", "AITC", "INC", "LF", "Other", "NOTA"}}

    return {
        "ac": ac_dir_name,
        "true_winner": next((p for p, info in gt_for_ac["candidates"].items()
                             if info.get("won")), None),
        "n_personas_in_set": n_prior,
        "n_predicted": n_pred,
        "prior_2019_pcts": prior_pcts,
        "true_2021_pcts": {p: round(truth[p], 1) for p in truth},
        "predicted_2021_pcts": pred_pcts,
        "pp_gap_pred_minus_truth": pp_gap,
        "switch_rate_2019_to_2021": round(switch_rate, 3),
        "n_switched": switched,
        "n_same_party": same_party,
        "top_switch_flows": switch_breakdown.most_common(5),
        "nota_pct_predicted": round(nota_share, 2),
        "memory_engagement": mem_summary,
    }


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    gts = yaml.safe_load(GT_PATH.read_text())["constituencies"]
    rows = []
    for ac_dir_name, gt_for_ac in gts.items():
        try:
            row = per_ac_analysis(ac_dir_name, gt_for_ac)
        except Exception as e:
            print(f"  ! {ac_dir_name}: {e}")
            continue
        rows.append(row)

    # Headline aggregates
    mean_switch = mean(r["switch_rate_2019_to_2021"] for r in rows)
    mean_nota = mean(r["nota_pct_predicted"] for r in rows)
    mean_pred_aitc = mean(r["predicted_2021_pcts"].get("AITC", 0) for r in rows)
    mean_true_aitc = mean(r["true_2021_pcts"].get("AITC", 0) for r in rows)
    mean_pred_bjp = mean(r["predicted_2021_pcts"].get("BJP", 0) for r in rows)
    mean_true_bjp = mean(r["true_2021_pcts"].get("BJP", 0) for r in rows)

    bjp_winning = [r for r in rows if r["true_winner"] == "BJP"]
    aitc_winning = [r for r in rows if r["true_winner"] == "AITC"]

    summary = {
        "n_acs": len(rows),
        "headline": {
            "mean_switch_rate_2019_to_2021": round(mean_switch, 3),
            "mean_nota_pct_predicted": round(mean_nota, 2),
            "mean_AITC_pred": round(mean_pred_aitc, 1),
            "mean_AITC_true": round(mean_true_aitc, 1),
            "mean_AITC_pp_gap": round(mean_pred_aitc - mean_true_aitc, 1),
            "mean_BJP_pred": round(mean_pred_bjp, 1),
            "mean_BJP_true": round(mean_true_bjp, 1),
            "mean_BJP_pp_gap": round(mean_pred_bjp - mean_true_bjp, 1),
        },
        "split_by_winner": {
            "bjp_winning_acs": {
                "n": len(bjp_winning),
                "mean_AITC_pp_gap": round(mean(r["pp_gap_pred_minus_truth"].get("AITC", 0)
                                               for r in bjp_winning), 1) if bjp_winning else None,
                "mean_BJP_pp_gap":  round(mean(r["pp_gap_pred_minus_truth"].get("BJP", 0)
                                               for r in bjp_winning), 1) if bjp_winning else None,
            },
            "aitc_winning_acs": {
                "n": len(aitc_winning),
                "mean_AITC_pp_gap": round(mean(r["pp_gap_pred_minus_truth"].get("AITC", 0)
                                               for r in aitc_winning), 1) if aitc_winning else None,
                "mean_BJP_pp_gap":  round(mean(r["pp_gap_pred_minus_truth"].get("BJP", 0)
                                               for r in aitc_winning), 1) if aitc_winning else None,
            },
        },
        "per_ac": rows,
    }

    out_path = OUT_DIR / "bias_analysis.json"
    out_path.write_text(json.dumps(summary, indent=2))

    # Markdown table
    md = ["# Distributional bias analysis — 2021_targeted variant\n",
          f"**N ACs analyzed**: {len(rows)}\n",
          "## Headline numbers\n",
          f"- Mean switch rate (2019 prior → 2021 final): **{mean_switch:.1%}**",
          f"- Mean NOTA% predicted: **{mean_nota:.2f}%**  (truth typically <2%)",
          f"- Mean BJP%: predicted {mean_pred_bjp:.1f}, true {mean_true_bjp:.1f} → "
            f"**{mean_pred_bjp - mean_true_bjp:+.1f} pp**",
          f"- Mean AITC%: predicted {mean_pred_aitc:.1f}, true {mean_true_aitc:.1f} → "
            f"**{mean_pred_aitc - mean_true_aitc:+.1f} pp**",
          "",
          "## Per-AC table\n",
          "| AC | True winner | 2019 prior (BJP/AITC/Other) | True 2021 (BJP/AITC/Other) | "
              "Pred 2021 (BJP/AITC/Other) | Switch% | NOTA% pred | Mean memories/agent |",
          "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        prior = r["prior_2019_pcts"]
        true = r["true_2021_pcts"]
        pred = r["predicted_2021_pcts"]
        md.append(
            f"| {r['ac']} | {r['true_winner']} | "
            f"{prior.get('BJP',0)}/{prior.get('AITC',0)}/{100-(prior.get('BJP',0)+prior.get('AITC',0)):.1f} | "
            f"{true.get('BJP',0)}/{true.get('AITC',0)}/{100-(true.get('BJP',0)+true.get('AITC',0)):.1f} | "
            f"{pred.get('BJP',0)}/{pred.get('AITC',0)}/{100-(pred.get('BJP',0)+pred.get('AITC',0)):.1f} | "
            f"{r['switch_rate_2019_to_2021']:.1%} | "
            f"{r['nota_pct_predicted']:.1f}% | "
            f"{r['memory_engagement']['mean']} (zero-mem agents: {r['memory_engagement']['with_zero_memories_pct']}%) |"
        )

    md.append("\n## Hypothesis verdicts\n")
    md.append(f"- **H1 anchoring to 2019**: switch rate averages {mean_switch:.1%}. "
              f"{'STRONG anchoring' if mean_switch < 0.15 else 'MILD anchoring' if mean_switch < 0.35 else 'agents do change'} ")
    md.append(f"- **H2 NOTA over-voting**: predicted NOTA averages {mean_nota:.2f}% — "
              f"{'NOT distorting (close to real ~1%)' if mean_nota < 3 else 'OVER-VOTED (real ~1%)'}")
    md.append(f"- **H3 belief change inertia**: see per-AC `mean memories/agent`")
    md.append(f"- **H4 AITC asymmetric under-prediction**: in BJP-winning ACs, mean AITC gap = "
              f"{summary['split_by_winner']['bjp_winning_acs']['mean_AITC_pp_gap']:+.1f} pp; "
              f"in AITC-winning ACs, mean AITC gap = "
              f"{summary['split_by_winner']['aitc_winning_acs']['mean_AITC_pp_gap']:+.1f} pp")

    (OUT_DIR / "bias_analysis.md").write_text("\n".join(md))
    print(f"Wrote: {OUT_DIR}/bias_analysis.md")
    print(f"Wrote: {OUT_DIR}/bias_analysis.json")
    print()
    print("\n".join(md))


if __name__ == "__main__":
    main()
