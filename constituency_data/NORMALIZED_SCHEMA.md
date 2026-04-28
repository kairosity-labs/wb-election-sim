# Normalized AC MD schema (v1)

Canonical identifier names + table layouts that **the auto-builder consumes
without needing per-AC plumbing fixes**.

The 9 ACs we hand-calibrated needed 50–470 lines of `<NN>_curate.py` patches
each — almost all of which rename identifiers (`TV → Television`,
`WB_other_dist → WB_other_district`), align prefixes (`U1_` on axis vs bare
on joint), expand compound age buckets (`33_47 → [33_37, 38_42, 43_47]`),
or aggregate sub-codes onto axis leaves. **If new ACs follow this schema
from the start, none of that plumbing is needed.**

This file is the source of truth. The companion fillable template
[`TEMPLATE_AC_NNN_2019.md`](TEMPLATE_AC_NNN_2019.md) is a worked-through MD
skeleton you can hand to a writer or an LLM to fill in for a new AC.

---

## 1. Section structure (mandatory)

Every AC MD must contain these sections in this order:

| Section | Purpose |
|---|---|
| `## A. Identity` | AC number, name, district, LS, sub-units used |
| `## B. 2019 population & electorate` | Headcount, M/F split, polling-station count |
| `## C. Marginal distributions (16 axes)` | C.1–C.16 (see §3) |
| `## D. Joint conditional distributions` | D.1–D.18 (see §4) |
| `## E. 2019 baseline vote (calibration target)` | AC-segment 2019 LS share — exactly the columns in §5 |
| `## F. Pre-2019 vote history` | Free-form anchors for belief evolution |
| `## G. Sources & tier flags` | Citation list, tier-D/E reliance flags |
| `## H. Post-2019 validation anchors` | OUT-OF-SAMPLE only — exempt from leakage gate |

**Section IDs are load-bearing.** The auto-builder parses on `### C.N`
and `### D.N` headings. Don't renumber, don't merge, don't split.

---

## 2. Identifier naming rules

### 2.1 Snake-case canonical names

Every category code in every table uses `Snake_Case_With_Capitalised_Words`,
no parenthetical qualifiers in the cell value (those go in the Source
column). The auto-builder snake-cases on parse, so:

| Source-row label (in table cell) | Canonical code generated |
|---|---|
| `Bengali` | `Bengali` ✅ |
| `Higher Secondary (Class 11–12)` | `Higher_Secondary` ✅ (parenthetical stripped) |
| `Currently married` | `Currently_married` ✅ |
| `Currently_married` | `Currently_married` ✅ |
| `Bengali / Hindi bilingual` | `Bengali_Hindi_bilingual` ✅ |

### 2.2 Tables must use canonical labels everywhere

The same concept must use the **identical text** in:

- C.x marginal table rows (first column)
- D.y joint table rows AND columns
- §E vote target rows
- Cross-references in source notes

**Common slips that break the auto-builder** (don't do these):

| Wrong | Right |
|---|---|
| `TV` (D.4 column) but `Television` (C.14 row) | Pick one and use everywhere — schema says `Television` |
| `LPG` (D.14 column) but `LPG / clean cooking fuel` (C.15 row) | `LPG_clean_cooking_fuel` everywhere |
| `Sec` / `HS` / `Grad` / `PG` (D.5 columns) but `Secondary` / `Higher Secondary` / `Graduate` / `Postgraduate` (C.6 rows) | Full names everywhere |
| `Ag_labourer` (D.8 row) but `Agricultural labourer` (C.8 row) | `Agricultural_labourer` everywhere |
| `WB_other_dist` (D.3 column) but `WB other district (in-migrant)` (C.16 row) | `WB_other_district` everywhere |
| `33_47_compound` (D.7 row) but `33_37`, `38_42`, `43_47` (C.3 rows) | Use 5-year cohorts in joints — see §4.4 |

If in doubt, **copy from AC 095 (`095_bangaon_uttar_2019.md`)** — it's the
gold-standard reference.

---

## 3. Marginal axes (C.1–C.16) canonical category sets

Each marginal section MUST include these category rows (exact spelling).
Add AC-local rows ONLY in §3.x extensions below. Pcts must sum to 100.0
± 0.1 across non-`is_subgroup` rows.

### C.1 Religion

| Required category |
|---|
| Hindu |
| Muslim |
| Christian |
| Sarna_ORP *(zero or non-zero; just include the row)* |
| Other_residual *(Sikh + Jain + Buddhist + Not_stated, lumped)* |

### C.2 Caste

| Required category | Subgroup-rollup parent? |
|---|---|
| SC_total | yes (rollup parent) |
| └ <local SC sub-codes> | sub-rows; `is_subgroup=yes` in CSV |
| ST_total | yes |
| └ <local ST sub-codes> | sub-rows |
| UC_bhadralok | leaf |
| OBC | leaf |
| Other_Hindu_middle | leaf |
| Muslim *(or Muslim_Sheikh, Muslim_Ansari_Jolaha if disaggregating)* | leaf |
| Christian_plus_Sarna_plus_Other | leaf |

**Sub-castes are sub-rows** prefixed with `└` in the MD table and marked
`is_subgroup=yes` after derive. They don't sum into the marginal — only
the parent (`SC_total`) does. The auto-builder's subgroup_rollups detector
picks them up.

If your AC has rich Muslim sub-caste structure (Murshidabad-style),
disaggregate Muslim into `Muslim_Sheikh` / `Muslim_Ansari_Jolaha` /
`Muslim_Syed_Pathan_Mughal` / `Muslim_other` instead of a single Muslim
row. Document the split rule in C.2.note.

### C.3 Age cohort

**Adults only** — Phase-2 simulates voters 18+. Do NOT include 0–17
cohorts in the marginal pcts (the auto-builder no longer needs to drop
them post-hoc).

| Required category |
|---|
| 18_22 · 23_27 · 28_32 · 33_37 · 38_42 · 43_47 · 48_52 · 53_57 · 58_62 · 63_67 · 68 |

Pcts sum to 100.0 across these 11 cohorts (renormalize from Census
including children → exclude children → renormalize).

### C.4 Gender

| Required category |
|---|
| Male · Female · Third_gender |

### C.5 Mother tongue

Required:

| Required category |
|---|
| Bengali · Hindi · Urdu · Other |

Add AC-local language rows (`Rajbongshi`, `Santali`, `Mundari`, `Sadri`,
`Marwari_Gujarati`, `Bhojpuri`, etc.) AS ADDITIONAL ROWS, not as
replacements. Keep `Other` as the residual catch-all.

### C.6 Education

| Required category |
|---|
| Illiterate · Primary · Middle · Secondary · Higher_Secondary · Graduate · Postgraduate |

### C.7 Workforce status

| Required category |
|---|
| Main_worker · Marginal_worker · Non_worker · Student · Unemployed |

If you need AC-local sub-categories (tea-belt: `Main_worker_tea_garden`,
`Main_worker_non_tea`), add as **sub-rows under Main_worker** (`└` prefix,
`is_subgroup=yes`). The aggregate `Main_worker` row is what enters joints.

### C.8 Occupation

| Required category |
|---|
| Cultivator · Agricultural_labourer · Household_industry · Manufacturing · Construction · Trade_retail · Transport_logistics · Services · Government_services_teachers · Out_migrant_worker |

Pcts sum to 100 across **workers only** (not all personas — the verifier
respects this via `verify_condition`).

### C.9 Class of worker

| Required category |
|---|
| Employer · Employee · Single_worker · Family_worker |

Pcts sum to 100 across workers only.

### C.10 Economic status

| Required category |
|---|
| BPL_household · Above_Poverty_Line_low_income · Lower_middle · Middle · Upper_middle_well_off |

### C.11 GP / Sub-unit location

**Always use a `Un_` prefix on every sub-unit code:**

| Pattern |
|---|
| `U1_<descriptive_snake>`, `U2_<descriptive_snake>`, ... |

Examples:
- `U1_Bangaon_Municipality` / `U2_CDB_Bangaon_rural_share`
- `U1_Cooch_Behar_Muni` / `U2_Cooch_Behar_CDB_rural`
- `U1_North_ward_cluster` / `U2_South_ward_cluster` *(KMC ward-style)*
- `U1_Nandigram_I` / `U2_Nandigram_II` *(CDB block-style)*

The prefix is REQUIRED (not optional) because we standardize on it.
Joint tables in D.11–D.14 use the same `U1_` prefix.

### C.12 Household composition

| Required category |
|---|
| Avg_HH_size *(scalar; not in marginal sum)* · Nuclear_HH · Joint_HH · Extended_multi_generation |

Pcts sum to 100 across the 3 partition rows (Avg_HH_size is metadata).

### C.13 Marital status

| Required category |
|---|
| Never_married · Currently_married · Widowed · Separated_divorced |

### C.14 Asset / media (FLAGS — independent rates, do NOT sum)

| Required flag |
|---|
| Television · Radio · Mobile_phone · Smartphone_with_internet · Computer · Two_wheeler · Four_wheeler · Banking_access |

### C.15 Amenities (FLAGS)

| Required flag |
|---|
| Improved_drinking_water_source · Improved_sanitation · LPG_clean_cooking_fuel · Wood_biomass_fuel · Other_fuel · Electricity |

(Cooking-fuel rows DO sum to 100 across `LPG_clean_cooking_fuel + Wood_biomass_fuel + Other_fuel` — note this in source.)

### C.16 Migration / birthplace

| Required category |
|---|
| Native · WB_other_district · Other_Indian_state · Bangladesh_origin · Outside_India · Out_migrant |

Add AC-local migration rows (`Nepal_Bhutan_origin`, `Jharkhand_origin`,
`Cyclone_Aila_displaced_2009`) AS ADDITIONAL ROWS without removing the 6
required ones (set them to 0% if not applicable).

---

## 4. Joint tables (D.1–D.18) canonical layouts

Every joint table has a fixed parent column + child columns. Use these
exact column headers.

### 4.1 Required parent / child columns

| Joint | Parent col | Child cols (in this order) |
|---|---|---|
| D.1 Religion × MotherTongue | `Religion` | C.5 categories (Bengali, Hindi, Urdu, Other, plus AC-local) + `Tier`, `Source` |
| D.2 Religion × Caste *(Hindu sub-structure)* | `Religion` | C.2 categories (SC_total, ST_total, UC_bhadralok, ...) — **see §4.6 for the wrap rule** |
| D.3 Religion × Migration | `Religion` | C.16 categories + `Tier`, `Source` |
| D.4 Religion × Asset (flags) | `Religion` | C.14 flags + `Tier`, `Source` |
| D.5 Caste × Education | `Caste` | C.6 categories + `Tier` |
| D.6 Age × Gender × Education | `Age_cohort` *(see §4.4)* | `Male_grad_plus`, `Female_grad_plus` + `Tier` |
| D.7 Marital × Age × Gender | `Age_cohort` *(see §4.4)* | `Male`, `Female` + `Tier` |
| D.8 Occupation × Asset (flags) | `Occupation` | C.14 flags + `Tier`, `Source` |
| D.9 Education × Workforce | `Education` | `Main_worker_rate`, `Unemployed_seeking` + `Tier` |
| D.10 Asset × Bilingualism | (skip if no `media_tier` axis) | — |
| D.11 GP × Religion | `Sub_unit` | C.1 categories + `Tier`, `Source` |
| D.12 GP × Caste | `Sub_unit` | C.2 categories *(parent leaves only — no sub-codes)* |
| D.13 GP × Asset (flags) | `Sub_unit` | C.14 flags + `Tier` |
| D.14 GP × Amenities (flags) | `Sub_unit` | C.15 flags + `Tier` |
| D.15 Vote × Religion | `Religion` | `BJP, AITC, INC, LF, Other_NOTA` + `Tier`, `Source` |
| D.16 Vote × Caste | `Caste` | same as D.15 |
| D.17 Vote × Gender | `Gender` | same as D.15 |
| D.18 Vote × Welfare *(skip if no welfare_exposure axis)* | — | — |

### 4.2 Parent values must be canonical axis category codes

`D.1 Religion` row keys are exactly `Hindu`, `Muslim`, `Christian`,
`Sarna_ORP`, `Other_residual` — same as C.1. **Do not** invent
sub-religion parents like `Hindu_non_Sarna` or `Hindu_Bengali`.

If your AC genuinely splits Hindu into Bengali/Non-Bengali sub-rows in
the underlying data, **collapse to one row in D.x** using a population-
share-weighted blend, and document the blend in `Source`. This is the
"Bengali / Non-Bengali Hindu collapse" pattern from AC 159.

### 4.3 Vote-target party set (LOCKED)

All vote joints (D.15–D.17) and §E use exactly these 5 party columns:

```
BJP | AITC | INC | LF | Other_NOTA
```

- `LF` = lump CPI(M) + CPI + RSP + AIFB + SUCI(C) + other_left
- `INC` stays separate
- `Other_NOTA` = NOTA + IND + every regional party (JKP, JKP(N), AKBJHP,
  BSP, BMUP, etc.)

**Local political-narrative detail** (e.g., "JKP got 0.96% in Jhargram")
goes in §F or §H narrative, not in D.15–D.17 columns. This is the
single biggest source of "skipped buckets" in the verifier.

### 4.4 Age-cohort joint keys

Joints D.6 and D.7 must key on **5-year cohorts**, identical to C.3:

```
| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | ... | ... | E |
| 23_27 | ... | ... | E |
...
| 68 | ... | ... | E |
```

**Do not use compound buckets** like `33_47_compound` or `48_62_compound`.
The previous-MD style (095) used compounds and required post-hoc
expansion in curate.py. Eliminate by writing 5-year rows directly —
copy values from the compound bucket if no finer data is available
(ack tier E).

### 4.5 GP / sub-unit joint keys (D.11–D.14)

Use the `Un_` prefix — same codes as C.11. So D.11 Religion-by-GP looks like:

```
| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier |
|---|---|---|---|---|---|---|
| U1_Bangaon_Municipality | 92 | 7 | 0.5 | 0 | 0.5 | E |
| U2_CDB_Bangaon_rural_share | 78.2 | 20.8 | 0.5 | 0 | 0.5 | A |
```

### 4.6 D.2 Religion × Caste — the canonical 2D layout

D.2 was the worst source of pain. Old MDs wrote it as a 1D "Hindu
sub-caste % of Hindu" table; the auto-builder had to wrap it. **Write
D.2 as a 2D table with one row per religion**, columns = caste leaves:

```
| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu  | 46.2 | 4.2 | 11.7 | 2.3 | 31.5 | 0 | 4.0 | C | ... |
| Muslim |    0 |   0 |    0 |   0 |    0 | 100 | 0 | A | ... |
| Sarna_ORP | 0 | 92 | 0 | 5 | 3 | 0 | 0 | E | ... |
| Christian | 0 |   0 |    0 |   0 |    0 |  0 | 100 | A | ... |
| Other_residual | 0 | 0 |  0 |   0 |    0 |  0 | 100 | E | ... |
```

Each Hindu sub-caste mass aggregates onto a parent leaf (Rajbanshi_SC,
Bagdi_SC, Namasudra_SC → SC_total). Document the aggregation in `Source`.
Each Hindu row sums to 100. Each non-Hindu row sums to 100 (mostly
diagonal with 100 in one bucket).

If you genuinely want to expose Muslim sub-castes (Sheikh / Ansari /
Syed / OBC-Muslim) as separate caste-axis leaves (Murshidabad-style),
declare them in C.2 AND in this D.2 Muslim row:

```
| Muslim | 0 | 0 | 0 | 0 | 0 | 48 (Sheikh) + 30 (Ansari) + 8 (Syed) + 14 (OBC-Muslim) | 0 | A | ... |
```

…where the right column has multiple sub-castes summing to 100.

### 4.7 Joints with no parent axis (D.10, D.18)

If your AC doesn't declare `media_tier` or `welfare_exposure` axes
(default for non-095 ACs), **omit D.10 and D.18 from the MD entirely.**
Don't write tables that the auto-builder will need to drop.

---

## 5. §E calibration target — locked schema

**Exactly 4 columns, one row per party (no Total / Electors / Turnout /
Margin meta rows mixed in):**

```
| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 48.0 | A | ECI 2024 GE2019 Form-20 (or D if proportional) |
| AITC | 44.0 | A | ... |
| INC | 1.5 | A | ... |
| LF | 4.5 | A | ... |
| Other_NOTA | 2.0 | A | ... |
```

Sum across the 5 parties must be 100.0 ± 0.5.

If you want to surface ECI Form-20 detail (per-candidate breakdown,
totals, electors, turnout, margin, regional parties), put it in §H as
a separate table — don't pollute §E.

---

## 6. Extension protocol (how to add AC-local detail without breaking compatibility)

The schema above is **conservative on purpose** — it enforces a common
shape so the auto-builder needs zero alignment patches. AC-local detail
that doesn't fit the canonical shape goes in three places:

### 6.1 Sub-row extensions in C-sections (allowed)

Use `└` prefix to add sub-categories under a canonical parent. The
auto-builder marks them `is_subgroup=yes` and they auto-roll-up:

```
| **SC_total** | 38.5 | A | Census 2011 block aggregate |
| └ Rajbanshi_SC | 36.0 | C | Dominant SC in Cooch Behar |
| └ Namasudra_SC |  3.0 | E | Smaller pool |
| └ Other_SC     |  ... | E | Residual |
```

These extra rows DON'T enter the marginal sum (only the parent does).

### 6.2 Additional rows in language / migration (allowed)

Append AC-local categories at the end of C.5 / C.16 keeping the required
ones present (set 0% if not applicable):

```
| Bengali | 81.5 | A | ... |
| Hindi | 0.3 | E | ... |
| Urdu | 0.0 | E | ... |
| Other | 0.5 | E | ... |
| **Santali** | 16.0 | A | AC-local (Jhargram tribal) |
| **Mundari** | 1.5 | A | AC-local |
| **Kurmali** | 0.5 | E | AC-local |
```

Joints (D.1, D.3) can include these extra columns; the auto-builder
preserves them. Just keep the required Bengali/Hindi/Urdu/Other present.

### 6.3 Narrative-only AC-local detail (use §F / §H)

Anything that doesn't fit the canonical schema — regional party name,
specific scheme exposure, displacement cohort, candidate-effect anchor —
goes in §F (pre-2019 history narrative) or §H (post-2019 anchors).
Downstream LLM persona narratives can read these; the auto-builder
ignores §F + §H.

---

## 7. Pre-flight compliance checklist

Before declaring an AC's MD ready for `derive_calibrated_2019_csvs.py`,
run through this list:

- [ ] All 16 C-sections present, in order, with required category rows
- [ ] All 18 D-section IDs present (D.10 / D.18 may be empty stub if
      no parent axis — see §4.7)
- [ ] §C.3 age cohorts cover only 18+ adults (no 0_4 / 5_9 / 10_14 / 15_17)
- [ ] §C.3 marginal sums to 100.0 ± 0.1
- [ ] §C.x marginals all sum to 100.0 ± 0.1 (excluding flag axes
      C.14, C.15, sub-rows)
- [ ] Every category code in §C uses canonical names (cross-check §3
      tables in this doc)
- [ ] Every D-table parent column uses the same identifier as the C-axis
- [ ] D.6 / D.7 use 5-year age-cohort rows (not compound buckets)
- [ ] D.11–D.14 use `Un_` prefix on Sub_unit column matching C.11
- [ ] D.15 / D.16 / D.17 have exactly 5 party columns: BJP, AITC, INC,
      LF, Other_NOTA
- [ ] D.2 written as 2D religion × caste table (not 1D Hindu-only)
- [ ] §E has exactly 4 columns + 5 party rows + sum to 100.0 ± 0.5
- [ ] Every D-table cell value is a numeric % (not a range, not a
      hyphen, not "see note")
- [ ] §H is present (post-2019 anchors) — content can be sparse but
      section header must exist for the validator's §H exemption to fire

Run `python3 kaisim/scripts/validate_md_schema.py <NN>` to auto-check.

---

## 8. Reference: AC 095 = the gold-standard worked example

For any ambiguity, look at `095_bangaon_uttar_2019.md` and its derived
artifacts in `simulations/wb_2021_ac095/`. Its production population
scores composite ≈ 359 with no curation patches — that's the target.

Older MDs (003, 011, 064, 123, 143, 159, 198, 210, 222) were written
before this schema was formalized; they need the per-AC `<NN>_curate.py`
patches to bridge to the canonical shape. **New ACs should follow this
schema directly to skip the curate step entirely.**

---

## 9. Versioning

This is **schema v1**. Future revisions go in `NORMALIZED_SCHEMA_v2.md`
etc., with the auto-builder reading a `schema_version: 1` field from
each AC MD's frontmatter. Any breaking change to canonical names will
bump the major version.
