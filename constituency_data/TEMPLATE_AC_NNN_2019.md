# AC <NNN> — <Constituency Name> — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC <NNN> <Constituency Name> as of 2019 only — it does not reference
> any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | <NNN> | A | ECI / Delimitation Commission 2008 |
| AC name | <Constituency Name> | A | ECI |
| Reservation | <SC / ST / GEN> | A | Delimitation 2008 |
| District | <District Name> | A | Delimitation 2008 |
| Sub-division | <Sub-division Name> | A | WB administrative |
| LS constituency | <LS PC number — name> | A | Delimitation 2008 |
| LS segments included | <list of AC numbers in same LS> | A | Delimitation 2008 |
| AC composition | <Municipalities + GPs / wards / blocks> | A | Delimitation 2008 |
| Geographic note | <one-line geography> | A | — |
| Sub-units used in v0 | **U1: <name>** · **U2: <name>** · ... | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | <est> | E | Census 2011 |
| 2019 projected population | <est> | E | 8-yr compound projection |
| Sex ratio (2019, F per 1000 M) | <est> | E | District baseline |
| 2019 estimated electorate (18+) | <est> | D | Back-derived from 2021 SIR |
| Estimated M / F / TG split | <% M / % F / 0.0X% TG> | E | 2021 SIR back-projection |
| 2019 polling stations (estimated) | ~<N> | E | 2021 SIR back-projection |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | <pct> | <tier> | <source> |
| Muslim | <pct> | <tier> | <source> |
| Christian | <pct> | <tier> | <source> |
| Sarna_ORP | <pct> | <tier> | Tribal religion (set 0 if not applicable) |
| Other_residual | <pct> | <tier> | Sikh + Jain + Buddhist + Not_stated, lumped |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | <pct> | <tier> | Parent rollup |
| └ <local_sc_subcode_1> | <pct> | <tier> | Sub-row (is_subgroup=yes) |
| └ <local_sc_subcode_2> | <pct> | <tier> | Sub-row |
| **ST_total** | <pct> | <tier> | Parent rollup |
| └ <local_st_subcode> | <pct> | <tier> | Sub-row (set parent=0 if no ST) |
| UC_bhadralok | <pct> | <tier> | <source> |
| OBC | <pct> | <tier> | <source> |
| Other_Hindu_middle | <pct> | <tier> | Residual within Hindu |
| Muslim | <pct> | <tier> | All sub-castes pooled (or split into Sheikh/Ansari/Syed/OBC-Muslim if disaggregating — see schema §3 C.2) |
| Christian_plus_Sarna_plus_Other | <pct> | <tier> | <source> |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | <pct> | <tier> | <source> |
| 23_27 | <pct> | <tier> | <source> |
| 28_32 | <pct> | <tier> | <source> |
| 33_37 | <pct> | <tier> | <source> |
| 38_42 | <pct> | <tier> | <source> |
| 43_47 | <pct> | <tier> | <source> |
| 48_52 | <pct> | <tier> | <source> |
| 53_57 | <pct> | <tier> | <source> |
| 58_62 | <pct> | <tier> | <source> |
| 63_67 | <pct> | <tier> | <source> |
| 68 | <pct> | <tier> | 68+ open-ended |
| **Sum** | **100.00** | — | self-check (renormalize from Census after excluding 0–17) |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | <pct> | <tier> | District sex ratio |
| Female | <pct> | <tier> | <source> |
| Third_gender | <pct> | <tier> | 2021 SIR |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

Required rows first, then AC-local additions:

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | <pct> | <tier> | <source> |
| Hindi | <pct> | <tier> | <source> |
| Urdu | <pct> | <tier> | <source> |
| Other | <pct> | <tier> | Residual catch-all |
| <local_lang_1> *(optional, e.g. Santali, Rajbongshi)* | <pct> | <tier> | AC-local |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | <pct> | <tier> | <source> |
| Primary | <pct> | <tier> | Class 1–5 |
| Middle | <pct> | <tier> | Class 6–8 |
| Secondary | <pct> | <tier> | Class 9–10 |
| Higher_Secondary | <pct> | <tier> | Class 11–12 |
| Graduate | <pct> | <tier> | <source> |
| Postgraduate | <pct> | <tier> | <source> |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | <pct> | <tier> | <source> |
| Marginal_worker | <pct> | <tier> | <source> |
| Non_worker | <pct> | <tier> | Housewife + elderly + retired |
| Student | <pct> | <tier> | 18–22 in education |
| Unemployed | <pct> | <tier> | Educated job-seekers |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

Pcts sum to 100 across **workers only** (not all personas).

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | <pct> | <tier> | <source> |
| Agricultural_labourer | <pct> | <tier> | <source> |
| Household_industry | <pct> | <tier> | <source> |
| Manufacturing | <pct> | <tier> | <source> |
| Construction | <pct> | <tier> | <source> |
| Trade_retail | <pct> | <tier> | <source> |
| Transport_logistics | <pct> | <tier> | <source> |
| Services | <pct> | <tier> | <source> |
| Government_services_teachers | <pct> | <tier> | <source> |
| Out_migrant_worker | <pct> | <tier> | <source> |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | <pct> | <tier> | <source> |
| Employee | <pct> | <tier> | <source> |
| Single_worker | <pct> | <tier> | Own-account |
| Family_worker | <pct> | <tier> | Unpaid |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | <pct> | <tier> | <source> |
| Above_Poverty_Line_low_income | <pct> | <tier> | <source> |
| Lower_middle | <pct> | <tier> | <source> |
| Middle | <pct> | <tier> | <source> |
| Upper_middle_well_off | <pct> | <tier> | <source> |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

Use the `Un_` prefix on every sub-unit code:

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_<name_snake> | <pct> | <tier> | <source> |
| U2_<name_snake> | <pct> | <tier> | <source> |
| <U3_..., U4_... as needed> | | | |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | <N persons> | <tier> | metadata, not in marginal sum |
| Nuclear_HH | <pct> | <tier> | <source> |
| Joint_HH | <pct> | <tier> | <source> |
| Extended_multi_generation | <pct> | <tier> | <source> |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | <pct> | <tier> | <source> |
| Currently_married | <pct> | <tier> | <source> |
| Widowed | <pct> | <tier> | <source> |
| Separated_divorced | <pct> | <tier> | <source> |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

Independent rates — **do NOT sum**.

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | <pct> | <tier> | <source> |
| Radio | <pct> | <tier> | <source> |
| Mobile_phone | <pct> | <tier> | <source> |
| Smartphone_with_internet | <pct> | <tier> | <source> |
| Computer | <pct> | <tier> | <source> |
| Two_wheeler | <pct> | <tier> | <source> |
| Four_wheeler | <pct> | <tier> | <source> |
| Banking_access | <pct> | <tier> | <source> |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | <pct> | <tier> | <source> |
| Improved_sanitation | <pct> | <tier> | <source> |
| LPG_clean_cooking_fuel | <pct> | <tier> | <source> |
| Wood_biomass_fuel | <pct> | <tier> | <source> |
| Other_fuel | <pct> | <tier> | Kerosene, dung, etc. |
| Electricity | <pct> | <tier> | <source> |
| **Note** | (water + sanitation + electricity are independent; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | <pct> | <tier> | Born in district or village/town |
| WB_other_district | <pct> | <tier> | <source> |
| Other_Indian_state | <pct> | <tier> | <source> |
| Bangladesh_origin | <pct> | <tier> | Set 0 if not a border/refugee AC |
| Outside_India | <pct> | <tier> | Excl. Bangladesh |
| Out_migrant | <pct> | <tier> | Working outside, registered here |
| <local_migration_1> *(optional, e.g. Nepal_Bhutan_origin, Jharkhand_origin)* | <pct> | <tier> | AC-local |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | <local_langs as needed> | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | <pct> | <pct> | <pct> | <pct> | | <tier> | <source> |
| Muslim | <pct> | <pct> | <pct> | <pct> | | <tier> | <source> |
| Christian | <pct> | <pct> | <pct> | <pct> | | <tier> | <source> |
| Sarna_ORP | <pct> | <pct> | <pct> | <pct> | | <tier> | <source> |
| Other_residual | <pct> | <pct> | <pct> | <pct> | | <tier> | <source> |

### D.2 Religion × Caste (canonical 2D — see schema §4.6)

P(caste ‖ religion) — % within each religion's population. **One row per
religion-axis category.** Hindu sub-caste mass aggregates onto canonical
caste leaves (Rajbanshi_SC + Other_SC → SC_total; document blend in Source).

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | <pct> | <pct> | <pct> | <pct> | <pct> | 0 | 0 | <tier> | <source> |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | <pct> | <pct> | 0 | <pct> | <pct> | 0 | 0 | <tier> | Tribal sub-castes mostly route to ST_total |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| Muslim | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| Christian | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| Sarna_ORP | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| Other_residual | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | <pct> | <pct> | <pct> | <tier> | <source> |
| Muslim | <pct> | <pct> | <pct> | <tier> | <source> |
| Christian | <pct> | <pct> | <pct> | <tier> | <source> |
| Sarna_ORP | <pct> | <pct> | <pct> | <tier> | <source> |
| Other_residual | <pct> | <pct> | <pct> | <tier> | <source> |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> |
| SC_total | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> |
| ST_total | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> |
| OBC | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> |
| Other_Hindu_middle | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> |
| Muslim | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender). **5-year cohorts; no compound buckets.**

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | <pct> | <pct> | <tier> |
| 23_27 | <pct> | <pct> | <tier> |
| 28_32 | <pct> | <pct> | <tier> |
| 33_37 | <pct> | <pct> | <tier> |
| 38_42 | <pct> | <pct> | <tier> |
| 43_47 | <pct> | <pct> | <tier> |
| 48_52 | <pct> | <pct> | <tier> |
| 53_57 | <pct> | <pct> | <tier> |
| 58_62 | <pct> | <pct> | <tier> |
| 63_67 | <pct> | <pct> | <tier> |
| 68 | <pct> | <pct> | <tier> |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender). **5-year cohorts.**

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | <pct> | <pct> | <tier> |
| 23_27 | <pct> | <pct> | <tier> |
| 28_32 | <pct> | <pct> | <tier> |
| 33_37 | <pct> | <pct> | <tier> |
| 38_42 | <pct> | <pct> | <tier> |
| 43_47 | <pct> | <pct> | <tier> |
| 48_52 | <pct> | <pct> | <tier> |
| 53_57 | <pct> | <pct> | <tier> |
| 58_62 | <pct> | <pct> | <tier> |
| 63_67 | <pct> | <pct> | <tier> |
| 68 | <pct> | <pct> | <tier> |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | <pct> | <pct> | <tier> | <source> |
| Agricultural_labourer | <pct> | <pct> | <tier> | <source> |
| Household_industry | <pct> | <pct> | <tier> | <source> |
| Manufacturing | <pct> | <pct> | <tier> | <source> |
| Construction | <pct> | <pct> | <tier> | <source> |
| Trade_retail | <pct> | <pct> | <tier> | <source> |
| Transport_logistics | <pct> | <pct> | <tier> | <source> |
| Services | <pct> | <pct> | <tier> | <source> |
| Government_services_teachers | <pct> | <pct> | <tier> | <source> |
| Out_migrant_worker | <pct> | <pct> | <tier> | <source> |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | <pct> | <pct> | <tier> |
| Primary | <pct> | <pct> | <tier> |
| Middle | <pct> | <pct> | <tier> |
| Secondary | <pct> | <pct> | <tier> |
| Higher_Secondary | <pct> | <pct> | <tier> |
| Graduate | <pct> | <pct> | <tier> |
| Postgraduate | <pct> | <pct> | <tier> |

### D.10 Asset / media × Bilingualism

(Skip if no `media_tier` axis — most ACs.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Sub-unit codes use `Un_` prefix matching C.11.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_<name> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| U2_<name> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Use canonical caste leaves only (no sub-codes).

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_<name> | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> |
| U2_<name> | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_<name> | <pct> | <pct> | <pct> | <pct> | <tier> |
| U2_<name> | <pct> | <pct> | <pct> | <pct> | <tier> |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_<name> | <pct> | <pct> | <pct> | <pct> | <tier> |
| U2_<name> | <pct> | <pct> | <pct> | <pct> | <tier> |

### D.15 Vote × Religion (2019 LS)

**Locked party set: BJP, AITC, INC, LF, Other_NOTA.** Lump regional
parties + NOTA + IND into Other_NOTA. Document local detail in §F / §H.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| Muslim | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| Christian | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| Sarna_ORP | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| Other_residual | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |

### D.16 Vote × Caste (2019 LS)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| OBC | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| SC_total | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| ST_total | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| Other_Hindu_middle | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| Muslim | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |
| Female | <pct> | <pct> | <pct> | <pct> | <pct> | <tier> | <source> |

### D.18 Vote × Welfare

(Skip if no `welfare_exposure` axis — most ACs.)

---

## E. 2019 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.** Surface
ECI Form-20 detail (per-candidate breakdown, electors, turnout, margin,
regional parties) in §H, not here.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | <pct> | <tier> | <source — ECI Form-20 if A; whole-LS proportional if D> |
| AITC | <pct> | <tier> | <source> |
| INC | <pct> | <tier> | <source> |
| LF | <pct> | <tier> | CPI(M)+CPI+RSP+AIFB+SUCI+other_left lumped |
| Other_NOTA | <pct> | <tier> | NOTA + IND + regional parties lumped |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

Free-form. Document AC-level history: 2011 AE, 2014 LS, 2014 by-poll, 2016
AE, 2019 LS results. Note local political dynamics (defections, candidate
effects, regional parties). The simulator reads this as narrative anchor.

### AC <NNN> (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | <name> | <party> | <pct> | <name> | <party> | <pct> | <vote_margin> |
| 2016 AE | <name> | <party> | <pct> | <name> | <party> | <pct> | <vote_margin> |

### LS <PC> historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | <name> | <party> | <pct> | <notes> |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — <relevant tables>
- Election Commission of India — <2011 AE / 2014 LS / 2016 AE / 2019 LS results>
- Delimitation Commission of India 2008 — WB Schedule

### Secondary sources (tier B / C)

- NFHS-4 (2015-16) WB — household amenities, asset ownership baseline
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2019 NES — vote × demographic conditionals
- WB District Statistical Handbook — <district>

### Tertiary / journalistic (tier D)

- <relevant articles>

### Tier-D / E reliance flags (what to distrust)

- <list of axes / cells where data is heavily modeled or journalistically estimated>

---

*v0 — generated <YYYY-MM-DD>, frozen at 2019 state-of-knowledge.
No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs. The
> validator's leakage gate exempts §H from the no-future-leakage check.

### 2021 WB Assembly Election — AC <NNN> (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| <party> | <name> | <votes> | <pct> | A — ECI 2021 AE |

### 2024 Lok Sabha Election — AC <NNN> segment within <LS> (tier A)

Surface full ECI Form-20 detail here including:
- Per-candidate breakdown (any number of parties — no canonical limit applies in §H)
- Electors / turnout / margin
- Regional parties by name (JKP, AKBJHP, BSP, etc.)

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| <party> | <name> | <votes> | <pct> | A | <source> |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024
LS AC segment shares within ±3pp of the tier-A figures (BJP / AITC / INC
/ LF combined).

---

## Compliance checklist (run before deriving CSVs)

- [ ] All 16 C-sections present, in order, with required canonical category rows
- [ ] All D-section IDs present (D.10 / D.18 may be empty if axes don't exist)
- [ ] §C.3 covers only 18+ adults (no 0_4 / 5_9 / 10_14 / 15_17)
- [ ] All marginal sums = 100.0 ± 0.1 (excluding C.14 / C.15 flag axes + sub-rows)
- [ ] Every category code matches NORMALIZED_SCHEMA.md
- [ ] D.6 / D.7 use 5-year age cohorts (not compound buckets)
- [ ] D.11–D.14 use `Un_` prefix on Sub_unit column
- [ ] D.15 / D.16 / D.17 have exactly 5 columns: BJP, AITC, INC, LF, Other_NOTA
- [ ] D.2 written as 2D religion × caste table (not 1D Hindu-only)
- [ ] §E has exactly 4 columns + 5 party rows + sum = 100.0 ± 0.5
- [ ] §H present (post-2019 anchors); content can be sparse

Run `python3 kaisim/scripts/validate_md_schema.py <NNN>` to auto-check.
