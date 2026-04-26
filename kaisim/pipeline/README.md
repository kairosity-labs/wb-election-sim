# `pipeline/` — Kaisim framework

A **region- and election-agnostic** library for building synthetic-population
election simulations. The WB 2021 simulation under `simulations/wb_2021_ac095/`
is one consumer of this library — adding a new election means dropping a new
folder under `simulations/` with its own data + plugins + config; nothing in
`pipeline/` should need to change.

This README describes the framework's mental model. Two companion documents
walk you through actually using it:

  - [`HOWTO_NEW_SIMULATION.md`](HOWTO_NEW_SIMULATION.md) — start-to-finish recipe
    for building a new simulation from raw demographic data.
  - [`HOWTO_AXES_AND_JOINTS.md`](HOWTO_AXES_AND_JOINTS.md) — how to design the
    `axes.json` + `joints.json` schema that drives everything.

---

## The three pipelines

```
   ┌──────────────────────────┐    ┌─────────────────────────┐    ┌─────────────────────────┐
   │ Persona generation       │    │ Verifier                │    │ Simulation              │
   │ (Phase 1)                │ ─► │ (used by both)          │ ◄─ │ (Phase 2 — stub)        │
   │                          │    │                         │    │                         │
   │ in:  axes + joints       │    │ in:  PersonaSet         │    │ in:  PersonaSet ref     │
   │      sampling spec       │    │      target marginals   │    │      news timeline      │
   │      vote blending cfg   │    │      target joints      │    │      query / experiment │
   │      news context        │    │      tolerance          │    │                         │
   │                          │    │                         │    │                         │
   │ out: PersonaSet          │    │ out: GapReport          │    │ out: SimulationRun      │
   └──────────────────────────┘    └─────────────────────────┘    └─────────────────────────┘
```

Each pipeline is independent. Persona generation produces a *named, reusable
audience*. The verifier scores any PersonaSet against the simulation's target
distributions. Phase-2 simulations cite a PersonaSet by name and run
downstream experiments against it — many runs per persona set, many persona
sets per simulation.

---

## Module map

```
pipeline/
├── core/                          # generic primitives — no domain knowledge
│   ├── axis.py                    Axis dataclass: partition | flag | scalar | derived
│   ├── joint.py                   Joint dataclass + AggregateTarget dataclass
│   ├── dag.py                     Topological sort over axes from joint+derived parents
│   ├── persona.py                 Persona dataclass — fields driven by axes
│   ├── persona_set.py             PersonaSet I/O + meta.json provenance
│   ├── run.py                     SimulationRun dataclass (Phase 2)
│   └── config.py                  SimulationContext + PersonaConfig loaders
│
├── persona_generation/            # Pipeline 1
│   ├── samplers/
│   │   ├── base.py                Sampler protocol
│   │   └── rule_based.py          DAG-walk + plugin dispatch (no LLM)
│   │   └── llm_batch.py           (Phase 1.2) batched LLM with verifier feedback
│   └── blending/
│       ├── base.py                VoteBlender + WelfareOverlapReducer protocols
│       ├── log_odds_mean.py       weighted geometric mean of probabilities
│       ├── naive_bayes.py         conditional-independence product
│       └── welfare_overlap.py     precedence | mean | dominant reducers
│
├── verifiers/                     # Pipeline 3 (used by 1 and 2)
│   ├── base.py                    GapReport + per-pass *Gap dataclasses
│   ├── marginal.py                per-axis category/flag pct gaps
│   ├── joint.py                   per-cell conditional/flag-rate gaps
│   ├── aggregate.py               bucket sums vs scalar targets (e.g., vote share)
│   └── composite.py               tier-weighted score + tolerance check + Markdown report
│
├── providers/                     # (Phase 1.2) LLM provider abstraction
│   ├── base.py                    Provider interface
│   ├── anthropic_provider.py      Claude with prompt caching
│   └── openai_provider.py         OpenAI with cached_content
│
└── simulation/                    # (Phase 2) downstream simulation framework — stub
```

---

## Configuration as the API surface

The framework reads two files per simulation:

  - `structures/axes.json` — every demographic dimension you model
  - `structures/joints.json` — every conditional table + aggregate target

Per persona-generation run, you provide:

  - `persona_configs/<name>.yaml` — sampler choice, target n, sampling spec
    (which method per axis), vote blending config, verifier tolerance, LLM
    settings.

Everything else is data + plugins. The framework code itself contains zero
references to "Bengal", "Matua", "BJP", or any specific axis.

---

## DAG generation order

The framework infers a topological sort over axes from two sources:

  1. **Joint parents** — every joint with `semantics ∈ {conditional,
     flag_rate_conditional, two_indicator_rates}` declares `parents → child`,
     which becomes a sampling dependency.
  2. **Derived axis parents** — derived axes (e.g., `welfare_exposure`)
     declare their own parent list in `axes.json`.
  3. **Sampling-spec hints** — entries in the persona_config can add an
     `after: [parent1, parent2]` field to inject extra ordering edges
     (e.g., `occupation` after `workforce_status`).

A cycle raises an error at DAG construction time.

---

## Vote layer — separate from the demographic DAG

The vote field (`vote_2019_LS` for WB) is generated *after* the DAG walk
finishes. Each enabled vote table provides P(party | parent) for one parent
axis (religion, caste, gender, welfare_dominant). The configured **VoteBlender**
combines these into P(party | persona); the welfare table goes through the
configured **WelfareOverlapReducer** first. The result is a categorical sample
appended to the persona's `fields[vote_field_name]`.

This separation keeps the demographic graph independent of the vote machinery
and lets you swap blending methods or weights per persona-config without
touching the sampler.

---

## Verification & tolerance

The verifier scores a PersonaSet on three dimensions:

  - **Per-axis marginal**: target_pct vs observed_pct for every category /
    flag of every axis.
  - **Per-joint cell**: target vs observed for every (parent_value, child)
    cell in every joint marked `is_for_verifying()`.
  - **Aggregate**: vote-share buckets vs the calibration target (per-party
    pct), with bucket-level grouping (e.g., `Left_INC_combined = INC + LF`).

A composite score is the tier-weighted sum of max-abs gaps. A population is
"within tolerance" iff every individual check is within its threshold *and*
the composite is below `composite_score_max`.

Tier weights default to A:4.0 / B:3.0 / C:2.0 / D:1.5 / E:1.0; thresholds
default to ±2pp (A) / ±3pp (B,C) / ±4pp (D,E) on axes, ±5pp on joint cells,
±2pp on aggregate vote, composite < 30. Override per-config in the
`verifier:` block of `persona_configs/<name>.yaml`.

---

## Naming convention for persona sets

A PersonaSet is a *named*, *reusable* artifact. We recommend names that
encode the relevant dimensions of variation:

```
default_n100_v1                   # default config, 100 personas, version 1
naive_bayes_blend_n100            # alternate vote-blender method
high_welfare_weight_n1000         # welfare weight bumped to 2.0
baseline_rule_n1000               # rule-based reference (no LLM)
```

Each persona set's `meta.json` carries a `config_hash` for catch-the-dupe
checking. `experiments/` (cohabitating with `persona_configs/`) holds Phase 2
run configs that cite a persona set by name.

---

## What the framework does NOT do

  - Read CSVs directly. Translation from raw data to `axes.json` + `joints.json`
    is per-simulation glue (`simulations/<sim>/build_structures.py`).
  - Decide region-specific sampling rules. Custom logic (workforce/age rules,
    welfare derivation, asset-blending policy) lives in
    `simulations/<sim>/derived/` and is referenced by name from the
    `sampling_spec` block.
  - Assume any particular set of axes. The Persona dataclass is schema-driven;
    every field is keyed by an axis name from the simulation's `axes.json`.
