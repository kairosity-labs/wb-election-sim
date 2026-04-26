---
name: run-simulation
description: Run a full Kaisim belief-evolution simulation — async LLM-driven agent dynamics over a period, producing per-agent memory streams + final vote queries + per-period reports. Use when the user wants to "run the simulation", "simulate the period", "do the LLM agent run", or "generate belief evolution".
---

# Kaisim — Run Simulation

You are launching the Phase-2 simulation pipeline: ~100 LLM agents living
through the news stream, updating beliefs each period, then casting a final
vote.

## Pre-flight check

  - **Persona set exists**: `kaisim/simulations/$SIM/personas/$PSET/personas.jsonl`
  - **Events YAML exists** and audited (every event has tags + valence + scope)
  - **`.env` populated** with LLM API keys at `kaisim/.env`
  - **Simulation config chosen**: `simulation_configs/<config>.yaml` references
    the right persona_set + events_file

## Run

```bash
SIM=<sim_name>
SCFG=rule_based      # or show_all, embedding, custom
python kaisim/simulations/$SIM/run_simulation.py $SCFG
```

For long runs, use background:

```bash
python kaisim/simulations/$SIM/run_simulation.py $SCFG > /tmp/sim.log 2>&1 &
```

## Live monitoring

Outputs flush incrementally to `runs/<timestamp>_<config>/agents/<id>/`:
  - `memory_stream.jsonl` (appends after each LLM call)
  - `feeds.jsonl` (appends after each event delivered)
  - `structured_history.jsonl` (appends after each structured delta)
  - `final_vote.json` (written when final vote query completes)

Watch any agent live:

```bash
tail -f kaisim/simulations/$SIM/runs/$RUN_DIR/agents/<persona_id>/memory_stream.jsonl
```

## Completion artifacts

```
runs/<timestamp>_<config>/
├── config.snapshot.yaml      ← reproducibility
├── summary.json              ← totals + ignore rate + final vote dist
├── vote_distribution.json    ← vs ground_truth from config
├── ignore_rate_by_demographic.json
├── plots/vote_distribution.png
└── agents/                   ← × N agents
    └── <persona_id>/
        ├── persona.json (snapshot)
        ├── memory_stream.jsonl
        ├── reflections (interleaved in memory_stream)
        ├── belief_narrative.md (regenerated at end)
        ├── structured_history.jsonl
        ├── feeds.jsonl
        ├── final_vote.json
        └── agent_meta.json
```

## Typical wall time + cost (n=100, ~50 ticks, Haiku 4.5 no thinking)

  - Wall: 12-18 min at concurrency 25-50
  - Cost: ~$15-25 (Haiku 4.5)
  - LLM calls: ~2,500-3,500 (depends on news density × persona-tag overlap)

## Killing + restarting

If you need to stop mid-run:

```bash
ps aux | grep run_simulation
kill <PID>
```

Per-agent artifacts up to that point are preserved (incremental flush). Re-running starts a fresh run dir; old run dir can be deleted or kept for diff.

## After the run

Always run analysis next:

```bash
python -c "
import sys; sys.path.insert(0, 'kaisim')
from pathlib import Path
from pipeline.simulation.belief_analysis import run
run(Path('kaisim/simulations/$SIM/runs/<run_dir>'))
"
```

Or use the `/analyze-run` skill.

## Switching strategies / models for ablation

Same persona set, different `simulation_configs/*.yaml`:

  - `show_all.yaml` — no targeting (every agent sees every event), sanity baseline
  - `rule_based.yaml` — broadcast + tag-overlap scoring (default)
  - Custom `embedding.yaml` (if implemented) — semantic similarity targeting

Compare runs with `/compare-runs`.

## Reference

  - Orchestrator: `kaisim/pipeline/simulation/orchestrator.py`
  - Updaters: `kaisim/pipeline/simulation/updaters/`
  - Targeting: `kaisim/pipeline/simulation/targeting/`
  - Methodology: `kaisim/pipeline/docs/METHODOLOGY.pdf`
