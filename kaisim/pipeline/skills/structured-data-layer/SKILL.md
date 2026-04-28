---
name: calibrated-layer
description: Build a calibrated, year-frozen demographic snapshot for a WB constituency in the same shape as data/calibrated_2019/. Use when the user asks to calibrate AC N to year Y, add a new AC to the calibrated layer, or scaffold a new calibration year (e.g. calibrated_2024).
---

# Calibrated layer — structured data pattern

Reference implementation: [`data/calibrated_2019/`](../../data/calibrated_2019/) (AC 95 Bangaon Uttar). This skill codifies that pattern so it can be replicated for any (AC, target_year) pair.

## When to use

Trigger this skill when the task is to produce structured calibrated input for the simulator — i.e. a frozen-at-target-year demographic snapshot of a constituency, designed to feed the population sampler and narrative engine. Do **not** trigger for ad-hoc data lookups or for the rolling 294-AC `data/constituencies.csv` (that is a separate, current-state asset).

This skill stays strictly upstream of simulation code — see `memory/division_of_labor.md`. It produces data files only.

## What the layer is

A calibrated layer is a directory `data/calibrated_<YEAR>/` containing four classes of artifact:

1. **Per-AC MD profile** (`NNN_<slug>_<year>.md`) — canonical source of truth. The MD is the human + machine readable artifact; CSVs derive from it.
2. **Companion CSVs** (`csv/NNN_*.csv`) — one long-format marginals CSV + one wide-format CSV per joint table + one calibration-target CSV. **Always derived from the MD by script — never hand-edited.**
3. **Methodology document** (`methodology_<year>.md`) — projection assumptions, source list, validation gates, repro commands. One per year, shared across all ACs in that year.
4. **Raw inputs** (`raw/`) — canonical scraper outputs, source PDFs. Do not edit.

## The freeze rule (most important constraint)

The MD is **frozen at target-year-state-of-knowledge**. It must not reference anything that happened after `<year>`. The downstream simulator uses post-`<year>` events as out-of-sample validation gates; pre-baking them into the data leaks future information.

For `calibrated_2019/`, the explicit forbidden-keyword list is:
`2020, 2021, 2022, 2023, 2024, 2025, 2026, CAA rules, SIR, Thakurbari, RG Kar, SSC scam, Lakshmir Bhandar, Cyclone Amphan, COVID-19, coronavirus`

For other target years, derive an equivalent list (years strictly greater than `<year>` plus event names that crystallized after `<year>`). Validation gate 5 enforces this via grep.

## Tier taxonomy (A–E)

Every data cell carries a confidence tier. Same as the main dataset:

- **A** — direct AC/block-level hard data (ECI, Census tables for the exact unit)
- **B** — state govt or central MIS dashboard, sub-AC granularity, aggregated to AC
- **C** — academic study or CSDS regional subsample
- **D** — journalistic estimate
- **E** — modeled imputation (projection, residual, equal-weight assumption)

Tier-A cells must always cite a primary source. Tier-D/E cells must cite the modelling rule that produced them. Validation gate 1 does **not** accept a cell with no source.

## Per-AC MD — required section skeleton

Use this skeleton (extracted from `095_bangaon_uttar_2019.md`). The section letter+number IDs are load-bearing — the parser in `scripts/derive_calibrated_<year>_csvs.py` keys off them.

```markdown
# AC NNN — <Name> (<Reservation>) — Calibrated <YEAR> Population Snapshot

> **Frozen at end-<YEAR>.** [freeze-rule preamble — see methodology §1]
> Companion artifacts: methodology_<year>.md · csv/
> All tables use the standardized 4-column format: Category | % | Tier | Source.

## A. Identity (as of <YEAR>)
   [AC number, name, reservation, district, sub-division, LS constituency,
    LS segments, AC composition, geographic note, sub-units]

## B. <YEAR> population & electorate
   [base-year population, projected population, sex ratio, electorate,
    M/F/TG split, polling stations]

## C. Marginal distributions (one section per axis, 4-col table each)
   C.1  Religion
   C.2  Caste / community
   C.3  Age cohort
   C.4  Gender
   C.5  Mother tongue
   C.6  Education level
   C.7  Workforce status
   C.8  Occupation
   C.9  Class of worker
   C.10 Economic / poverty
   C.11 GP / Municipality location
   C.12 Household composition
   C.13 Marital status
   C.14 Asset / media access      [does NOT sum to 100 — independent ownership]
   C.15 Household amenities       [does NOT sum to 100 — independent ownership]
   C.16 Migration / birthplace

   Each marginal table:
   | Category | % | Tier | Source / Note |
   Each table ends with a self-check **Sum** row (100.00) except C.14, C.15.

## D. Joint conditional distributions
   D.1  Religion × Mother tongue
   D.2  Religion × Caste (Hindu-internal sub-structure)
   D.3  Religion × Migration / birthplace
   D.4  Religion × Asset / media (TV, smartphone, banking)
   D.5  Caste × Education
   D.6  Age × Gender × Education
   D.7  Marital status × Age × Gender
   D.8  Occupation × Asset / media
   D.9  Education × Workforce participation
   D.10 Asset / media × Bilingualism
   D.11 GP × Religion
   D.12 GP × Caste
   D.13 GP × Asset / media
   D.14 GP × Amenities
   D.15 Vote × Religion (target-year LS, regional anchor)
   D.16 Vote × Caste (target-year LS)
   D.17 Vote × Gender (target-year LS)
   D.18 Vote × Welfare-scheme exposure (target-year)

## E. <YEAR> baseline vote (calibration target)
   ### Whole <LS> (PC NN) — <YEAR> result (tier A, ECI)
   ### AC NNN segment estimate (tier D unless Form-20 obtained → tier A)

## F. Pre-<YEAR> vote history (anchors, NOT calibration targets)
   ### AC NNN specifically (Assembly Elections)
   ### <LS> Lok Sabha historical

## G. Sources & tier flags
   ### Primary sources (tier A — direct hard data)
   ### Secondary sources (tier B/C)
   ### Tertiary / journalistic (tier D)
   ### Tier-D/E reliance flags (what to distrust)
   ### v0 known gaps (cross-reference methodology §7)
```

## Methodology document — required section skeleton

One file per `<year>`, located at `data/calibrated_<year>/methodology_<year>.md`. Skeleton:

```markdown
# Methodology — <YEAR>-Calibrated <constituency or "all WB ACs">

## 1. Reading the calibrated file
   [Freeze rule statement; explicit list of post-<YEAR> events the file must
    not reference; statement that downstream uses these as validation gates.]

## 2. Confidence tiers
   [A–E recap; same taxonomy as main dataset.]

## 3. Composition of AC (Delimitation 2008)
   [Component CDBs/GPs/Muni; sub-unit decomposition for spatial heterogeneity;
    base-year population per sub-unit.]

## 4. Projection from Census 2011 → <YEAR>
   [Table of assumptions: religion-differential growth, migration, voter cohort
    additions, asset/media diffusion, literacy. Each row cites a source.]

## 5. Calibration target
   [The election result the synthetic population must reproduce; tier of that
    target; pre-target anchors as historical context.]

## 6. Source list
   [Numbered table: # | Source | Used for | Status (✓ have / ✗ deferred).]

## 7. v0 known gaps (to be closed in v1)
   [Numbered list: each gap = (what's missing, current proxy, refinement path).]

## 8. Validation gates
   [The 5 gates run by validate_calibrated_<year>.py — see below.]

## 9. Reproducing v0
   [Exact commands to regenerate CSVs and run gates.]
```

## CSV layer — what derives from what

Generated by `scripts/derive_calibrated_<year>_csvs.py`. Always re-derive after MD edits:

| CSV | Format | Source section | Schema |
|---|---|---|---|
| `NNN_marginals.csv` | long | C.1–C.16 stacked | `axis, category, pct, tier, source, is_subgroup` |
| `NNN_joint_<id>.csv` | wide | one D.* table | header preserved as parsed |
| `NNN_calibration_target_<year>.csv` | wide | E aggregate | `party, ac<NNN>_segment_pct_estimate, tier, note` |

**Naming for joint CSVs:** keep the existing slug map in `derive_calibrated_<year>_csvs.py` (`095_joint_religion_caste.csv`, etc.). When adding a new AC, the slugs are the same — only the `095_` prefix changes.

## The 5 validation gates

Run via `python3 scripts/validate_calibrated_<year>.py NNN`. Implementation lives in `scripts/validate_calibrated_2019.py` — copy/parameterize for new years.

| # | Gate | Pass criterion |
|---|---|---|
| 1 | Marginal sum | Each axis (excluding C.14 asset_media + C.15 amenities) sums to 100 ± 0.5 |
| 2 | Joint marginal recovery | Population-weighted recovery of dependent axis from each joint matches the marginal within ±1.0pp |
| 3 | Population calibration | Projected adult pop × eligibility ≈ ECI <year> roll within ±2% (skip if roll not fetched) |
| 4 | Vote calibration | Σ(P(party\|religion) × P(religion)) recovers AC segment within ±2pp on each major party |
| 5 | No-future-leakage | grep over MD + CSVs for the forbidden post-`<year>` keyword list returns zero hits |

Exit codes: 0 = all enforced pass · 1 = hard failure · 2 = only soft warnings.

## Source registry — use scrapers before manual search

Empirical audit of the first 30 calibrated 2019 ACs found that ~85% of every Tier-A/B/C cell traces to one of seven canonical sources. **Before doing any web search**, check the source registry at [`scripts/scrapers/SOURCE_REGISTRY.md`](../../../scripts/scrapers/SOURCE_REGISTRY.md) and run the scraper if it exists. This collapses the per-AC token budget from ~80k input tokens (search + read) to ~12k (CSV reads).

| Source family | Coverage | Scraper | Output location |
|---|---|---|---|
| Census 2011 PCA / SC-ST / literacy | 30/30 | already mirrored | [`data/shrug/`](../../../data/shrug/), [`data/census_2011/`](../../../data/census_2011/) |
| Wikipedia AC + LS infoboxes | 30/30 | [`scrape_wikipedia_ac.py`](../../../scripts/scrapers/scrape_wikipedia_ac.py) | `data/wikipedia/<NNN>_<slug>.json` |
| TCPD LokDhaba (clean ECI mirror) | 30/30 | [`scrape_lokdhaba.py`](../../../scripts/scrapers/scrape_lokdhaba.py) | `data/lokdhaba/<type>_West_Bengal_<year>.csv` |
| ECI Form-20 (PS-level) | 16/30 | [`scrape_ceo_wb_form20.py`](../../../scripts/scrapers/scrape_ceo_wb_form20.py) | `data/ceo_wb_form20/<elec>_AC_<NNN>_psresults.csv` |
| NFHS-5 district fact sheets | 30/30 | [`scrape_nfhs_district.py`](../../../scripts/scrapers/scrape_nfhs_district.py) | `data/nfhs_5/district_indicators_long.csv` |
| ECI / Delimitation 2008 metadata | 30/30 | one-time, in [`data/master/`](../../../data/master/) | `wb_ac_master_v3.csv` |
| CSDS-Lokniti 2019 NES cross-tabs | 29/30 | manual (one-time) | `data/csds_lokniti_2019.csv` |

When adding a brand-new source family, follow the procedure in [`SOURCE_REGISTRY.md`](../../../scripts/scrapers/SOURCE_REGISTRY.md) §"Adding a new source family" and update the table above.

## Procedure — calibrating a new AC to an existing year

1. **Confirm the freeze year is settled.** If calibrating to a year that already has a `methodology_<year>.md`, reuse it; do not duplicate.
2. **Run the scrapers first** (idempotent; cached). For an unmirrored AC:
   ```bash
   python3 scripts/scrapers/scrape_wikipedia_ac.py --ac NNN --slug Foo_Bar
   python3 scripts/scrapers/scrape_ceo_wb_form20.py --election ge2019 --ac NNN
   # LokDhaba + NFHS-5 are state-wide one-time fetches — only re-run on schema change.
   ```
   Outputs land under `data/{wikipedia,ceo_wb_form20,lokdhaba,nfhs_5}/`. **Only after these have been consulted** should you fall back to web search for residual gaps. Apply the **scrape-first rule** (see `memory/feedback_scrape_first.md`): try sub-AC granularity before district rollup.
3. **Decompose the AC** into sub-units (Muni + GPs per Delimitation 2008). Get population per sub-unit at Census 2011.
4. **Project Census 2011 → `<year>`** using the methodology §4 assumption table. Document any AC-specific deviation.
5. **Draft the per-AC MD** following the section skeleton above. Every cell must have a tier and a source. Apply the freeze rule continuously — when in doubt, omit.
6. **Derive CSVs:** `python3 scripts/derive_calibrated_<year>_csvs.py`.
7. **Run gates:** `python3 scripts/validate_calibrated_<year>.py NNN`. Iterate on the MD until all 5 pass (or are explicitly deferred in §7 known gaps).
8. **Update methodology §6 source list** if any new source class was used. If a source had to be web-searched manually (i.e. no scraper exists), consider whether it should become a new scraper — see [`SOURCE_REGISTRY.md`](../../../scripts/scrapers/SOURCE_REGISTRY.md).

## Procedure — scaffolding a new calibration year

1. Create `data/calibrated_<year>/` with subdirs `csv/` and `raw/`.
2. Copy `methodology_2019.md` to `methodology_<year>.md` and rewrite §1 freeze list, §4 projection horizon, §5 calibration target, §8 forbidden-keyword list.
3. Duplicate `scripts/derive_calibrated_2019_csvs.py` and `scripts/validate_calibrated_2019.py` to `_<year>_` variants. Update the year-specific paths and forbidden-keyword list. The section parser logic is reusable as-is.
4. Pick a pilot AC (default Bangaon Uttar 095) and run the per-AC procedure above against the new year.
5. Only after the pilot passes all gates, scale to additional ACs.

## What this skill does not cover

- The 294-AC rolling `data/constituencies.csv` and its tier-coverage table — that is the current-state dataset, separate from the year-calibrated layer. See `data/methodology.md`.
- Simulation code: synthetic-population sampling, narrative injection, belief evolution. Strictly out of scope per division of labor.
- Choice of pilot AC — see `memory/pilot_seat.md` (Bangaon Uttar AC 95).
