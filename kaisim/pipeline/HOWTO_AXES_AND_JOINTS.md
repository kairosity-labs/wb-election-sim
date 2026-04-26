# HOWTO — Designing axes and joints

The single most important schema decision in a Kaisim simulation is what
counts as an axis and what counts as a joint. Getting this right makes the
sampler, verifier, and prompts all simpler. Getting it wrong means
compensating with plugin glue everywhere.

---

## What is an axis?

An axis is **one demographic dimension a persona has a value on**. Each
persona's `fields[axis_name]` holds a value typed by the axis's `kind`:

| kind        | Persona field shape          | Example                               |
|-------------|------------------------------|---------------------------------------|
| `partition` | a single string (category)   | `religion = "Hindu"`                  |
| `flag`      | dict of bool flags           | `asset_media = {"TV": true, ...}`     |
| `scalar`    | not per-persona; metadata only | `household_size_avg = 4.4`          |
| `derived`   | output of a plugin function  | `welfare_exposure = {"Krishak..." }`  |

### Choosing partition vs flag

A **partition** is appropriate when categories are mutually exclusive and
collectively exhaustive — pick one. Religion, gender, education-level,
occupation, household-type. Marginal pcts must sum to ~100.

A **flag** is appropriate when each item is an independent yes/no — own/don't
own. Asset ownership, scheme enrollment, amenity access. Each flag has its
own Bernoulli rate; they don't sum to anything in particular.

If you're unsure: ask "could a persona have two of these at once?" If yes →
flag. If no → partition.

### Subgroup roll-ups

If your data has hierarchical categories (e.g., "SC total" containing
{Namasudra, Bagdi, ...}), declare:

```json
{ "name": "caste",
  "kind": "partition",
  "categories": ["Namasudra_Matua", "Bagdi", "Poundra", "Other_SC", ...],
  "marginal": {...},
  "subgroup_rollups": {
    "SC_total": ["Namasudra_Matua", "Bagdi", "Poundra", "Other_SC"]
  }
}
```

The verifier will report both the leaf-level shares AND the rolled-up
"SC_total" line. Sampling stays at the leaf level.

### Derived axes

If a value can be computed from prior fields, it's derived. Don't generate
welfare_exposure independently of occupation / age / gender — make it a
plugin that takes those as inputs.

```json
{ "name": "welfare_exposure",
  "kind": "derived",
  "parents": ["occupation", "gender", "age_cohort", "economic_status"],
  "module": "derived.welfare_exposure",
  "function": "derive",
  "flags": ["Krishak_Bandhu", "Kanyashree", "..."]
}
```

The framework calls `derived.welfare_exposure.derive(rng, ctx, axis, persona)`
once parents are sampled.

---

## What is a joint?

A joint is **a conditional probability table** linking parents to a child:
P(child | parents). Joints have one of four `semantics`:

| semantics                 | Table shape                                  | Use for                                             |
|---------------------------|----------------------------------------------|-----------------------------------------------------|
| `conditional`             | `{parent_value: {child_cat: pct}}`, rows sum to 100 | Categorical child given categorical parents         |
| `flag_rate_conditional`   | `{parent_value: {flag: rate}}`, independent | Per-flag Bernoulli rate given parent                |
| `two_indicator_rates`     | `{parent_value: {indicator: rate}}`         | Two named Bernoulli rates per parent (e.g., workforce) |
| `vote_conditional`        | `{parent_value: {party: pct}}`, rows sum to 100 | P(vote | parent) — consumed by VoteBlender, not DAG |

### Choosing parents

A joint declares which axes feed its child. Parent axes must already be in
`axes.json`. The framework topologically sorts the DAG so parents are
sampled before children.

If a child has multiple sources (e.g., asset.TV depends on gp + religion +
occupation), declare *one joint per parent path* and write a custom plugin
that blends them. Don't try to encode all of them as a single `parents:
[gp, religion, occupation]` joint unless you actually have a 3-way cross-tab.

### Bucket maps — when joint labels are coarser than axis leaves

Real-world data often gives you joints over coarse buckets like
"Bagdi/other SC" while your axis distinguishes leaves like Bagdi, Poundra,
Other_SC. Declare a bucket map:

```json
{ "name": "education_given_caste",
  "parents": ["caste"],
  "child":   "education",
  "table": {
    "Bagdi_other_SC": { "Illiterate": 22, "Primary": 28, ... },
    ...
  },
  "caste_bucket_map": {
    "Bagdi_other_SC":   ["Bagdi", "Poundra", "Other_SC"],
    "Namasudra_Matua":  ["Namasudra_Matua"],
    ...
  }
}
```

Both sampler and verifier honor `caste_bucket_map` for parent lookups. For
joints where the *child* is also coarsened (e.g., `caste_given_gp` whose
child is the same coarse caste), the verifier's child-bucket logic kicks in
automatically when `joint.child == "caste"`.

### `use:` directives — when to skip a joint

Some joints are useful for sampling but not directly verifiable, or vice
versa. Mark them with the `use` field:

  - `"use": "sampling_only"` — sampler uses, verifier skips. E.g., joints
    with compound age buckets ("33–47") that don't 1:1 map to your axis
    leaves.
  - `"use": "verifier_only"` — sampler skips, verifier uses. E.g., a
    cross-check joint like `caste_given_gp` when the DAG samples caste via
    `caste_given_religion` instead.
  - omitted (default) — both pipelines use the joint.

### Aggregate targets

For scalar checks like "BJP vote share in this AC = 48%", use
`aggregate_targets`:

```json
{ "name": "vote_aggregate_2019_LS",
  "field": "vote_2019_LS",
  "buckets": [
    { "name": "BJP",               "target_pct": 48.0, "vote_values": ["BJP"] },
    { "name": "Left_INC_combined", "target_pct": 6.0,  "vote_values": ["INC", "LF"] }
  ],
  "tier": "D"
}
```

Each bucket may sum over multiple values of the persona field. The verifier
compares observed pct (count where field ∈ vote_values, divided by n)
against `target_pct`.

---

## Tier guidance

Every axis and joint gets a tier A–E describing source strength. The
verifier's tolerance and tier-weighted scoring depend on this — be honest:

  - **A** — direct measured / hard data (Census, ECI Form 20)
  - **B** — state MIS dashboard, sub-AC granularity, weighted to AC
  - **C** — academic study or CSDS regional subsample
  - **D** — journalistic estimate (single source)
  - **E** — modeled imputation / inference

If multiple rows of a marginal have different tiers, take the max.

---

## Naming conventions

Codes used as keys in axes.json categories, joint table keys, and persona
fields should be:

  - **snake_case** ASCII identifiers
  - **canonical** — the same conceptual entity has the same code everywhere
    (don't have "TV" in one joint and "Television" in another for the same
    axis)
  - **stable** — once written, don't rename mid-flight; old persona sets
    will diff against changed codes

If your CSVs use inconsistent labels, normalize them in `build_structures.py`
via a `CANONICAL_CODES` dict (see the WB build script for an example).

Display labels (human-readable strings with spaces and parens) live in the
`display_names` field of each axis — used by prompts and reports, not by
the framework's lookups.

---

## Anti-patterns

  - **One joint per parent value**. Don't write 8 separate joints for "P(X |
    religion=Hindu)", "P(X | religion=Muslim)", etc. Write one joint with
    `parents: ["religion"]` and 8 rows in `table`.
  - **Vote tables in the demographic DAG**. Vote tables have `semantics:
    "vote_conditional"` and are skipped by the DAG; they're consumed by the
    VoteBlender post-walk. Don't declare them as `conditional`.
  - **Hard-coded category lists in plugins**. The plugin should read
    `axis.flags` / `axis.categories` from the Axis dataclass, never hard-
    code the list. That way reordering or renaming categories doesn't break
    the plugin.
  - **Mixing voter-population with whole-population marginals**. If your
    election uses voter-aged data but the age axis is the full population
    pyramid, every conditional axis on age will mismatch. Filter to voters
    in `build_structures.py` and renormalize.
