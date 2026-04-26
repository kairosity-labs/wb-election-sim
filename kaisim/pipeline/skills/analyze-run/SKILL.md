---
name: analyze-run
description: Generate the full belief-evolution analysis from a completed Kaisim simulation run — vote redistribution timeline, switches per month, per-event impact, switcher matrix, demographic trajectories, trust evolution, and a Markdown report with sample switcher narratives. Use when the user wants to "analyze the run", "generate plots", "produce a report on the simulation", or "see how voters evolved".
---

# Kaisim — Analyze Simulation Run

Generate the full per-run analysis pack.

## Run

```bash
SIM=<sim_name>
RUN_DIR=runs/<timestamp>_<config>     # e.g. runs/20260425_230641_rule_based

python -c "
import sys; sys.path.insert(0, 'kaisim')
from pathlib import Path
from pipeline.simulation.belief_analysis import run
run(Path('kaisim/simulations/$SIM/$RUN_DIR'))
"
```

## Outputs (in `<run_dir>/analysis/`)

| File | Purpose |
|---|---|
| `vote_redistribution.png` | Stacked area: % of agents leaning each party per month |
| `switches_over_time.png` | Bar: # agents who flipped lean per month |
| `party_momentum.png` | Cumulative explicit `more_X` shifts (sparse signal) |
| `trust_evolution.png` | Avg signed trust score per political actor over time |
| `event_impact.png` | Top 18 events by agent-shift count |
| `switcher_matrix.png` | 2019 prior → 2024 vote heatmap |
| `demographic_trajectories.png` | Vote-share over time split by demographic |
| `report.md` | Full narrative report with sample switcher narratives |

## What to look for

  - **Stable trajectories with election-year crystallization** is the
    realistic pattern. If the redistribution chart is FLAT throughout,
    the structured deltas are too coarse. Trust evolution is the cleaner
    sentiment signal.
  - **Total switches** should be 15-30% of n for a 4-year period.
    If <5%, anchor strength is too high or events too sparse.
    If >50%, agents are flipping noisily — tighten the prompt's
    "most news doesn't move you" framing.
  - **Final vote vs ground truth**: compare `vote_distribution.json`'s
    `pcts` vs `ground_truth_pcts`. Gap of <5pp per major party is good
    for n=100; <2pp would require n=1000+.
  - **Sample switcher narratives** (in report.md): these should sound
    like specific human reasoning grounded in events, not generic
    talking points. Quotes referencing specific dates / scheme names /
    leader names = LLM is doing its job.

## Common analysis follow-ups

  - **Per-demographic deep dive**: re-run `belief_analysis.run()` after
    splitting agents by tag — see `pipeline/simulation/belief_analysis.py`
    for the `_trajectory(filter_fn)` helper.
  - **Per-event qualitative** narrative: pull all monologues triggered by
    a specific event (`grep -h 'triggering_event_slug.*caa_rules'
    runs/*/agents/*/structured_history.jsonl`).
  - **Compare to baseline**: use `/compare-runs` against a `show_all`
    baseline to measure what targeting changed.

## Reference

  - Analysis script: `kaisim/pipeline/simulation/belief_analysis.py`
  - Plot rendering: matplotlib (PDF/PNG via `Agg` backend)
