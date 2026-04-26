# `simulations/` — concrete election simulations

Each subdirectory is one (region, election) instance built on the
[`pipeline/`](../pipeline/) framework. The framework is region-agnostic;
all the (region, election)-specific details live here.

To add a new simulation, follow
[`pipeline/HOWTO_NEW_SIMULATION.md`](../pipeline/HOWTO_NEW_SIMULATION.md).

---

## Per-simulation layout

```
simulations/<sim_name>/
├── README.md                       what this simulation is + status
├── STRUCTURE.md                    overlap resolutions + design choices
├── build_structures.py             one-off: CSV → structures/{axes,joints}.json
│
├── structures/                     framework-consumable JSON (built by above)
│   ├── axes.json                   16+ demographic dimensions
│   └── joints.json                 conditional tables + aggregate vote target
│
├── derived/                        region-specific Python plugins
│   ├── __init__.py
│   ├── welfare_exposure.py
│   ├── workforce_sampling.py
│   ├── ...
│
├── prompts/                        Phase 1.2: LLM prompt slots
│   ├── system_anchors.md           narrative facts
│   ├── persona_rules.md            coherence rules
│   └── batch_guidance.md           gap-fill template
│
├── news/                           opinion / event context
│   ├── persona_context_pre<year>.md   for persona generation narratives
│   └── timeline_<from>_<to>.jsonl     Phase 2: drip-fed headlines
│
├── persona_configs/                YAML configs for persona generation
│   ├── baseline_rule.yaml          rule-based reference (no LLM)
│   ├── default.yaml                LLM-generated (Phase 1.2)
│   └── ...                         additional configs (alt blender, weights)
│
├── personas/                       generated, named, reusable audiences
│   ├── baseline_rule_n1000/
│   │   ├── personas.jsonl
│   │   ├── meta.json               provenance (sampler, model, config_hash)
│   │   ├── persona_config.snapshot.yaml
│   │   ├── batches/                LLM raw responses (rule-based: empty)
│   │   └── reports/
│   │       └── FINAL.md            verifier report
│   └── default_n100_v1/
│       └── ...
│
├── experiments/                    Phase 2 run configs
│   ├── vote_2021_baseline.yaml     direct ask, no news
│   └── vote_2021_with_news.yaml    drip-fed news timeline
│
├── runs/                           Phase 2 simulation outputs
│   └── <run_name>/
│       ├── meta.json               cites a persona set by name + hash
│       ├── results.jsonl
│       └── reports/
│
├── generate.py                     CLI wrapper: persona-generation entry point
└── run.py                          CLI wrapper: Phase 2 simulation entry point
```

---

## Naming conventions

  - `<sim_name>` — `<region>_<year>_<scope>` (e.g., `wb_2021_ac095`,
    `up_2027_state`).
  - persona set names — `<config_stem>_n<n>[_v<v>]` (e.g.,
    `baseline_rule_n1000`, `default_n100_v2`). Include version when iterating
    on the same config.
  - experiment names — `<query_or_method>_<config_stem>` (e.g.,
    `vote_2021_baseline`, `vote_with_news_no_caa`).
  - run output names — `<date>_<experiment>_<set>` (e.g.,
    `2026-04-25_vote2021_baseline_default_v1`).

---

## Current simulations

  - [`wb_2021_ac095/`](wb_2021_ac095/) — Bangaon Uttar AC, calibrating to 2019
    LS Bangaon segment. Pilot of the framework. See
    [STRUCTURE.md](wb_2021_ac095/STRUCTURE.md) for design notes.
