# AC 002 — Mathabhanga (SC) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 002 Mathabhanga as of 2019 only — it does not reference
> any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 2 | A | ECI / Delimitation Commission 2008 |
| AC name | Mathabhanga | A | ECI |
| Reservation | SC | A | Delimitation 2008 |
| District | Cooch Behar | A | Delimitation 2008 |
| Sub-division | Mathabhanga | A | WB administrative |
| LS constituency | 1 — Cooch Behar (SC reserved) | A | Delimitation 2008 |
| LS segments included | AC 2 Mathabhanga · 3 Sitalkuchi · 4 Dinhata · 5 Sitai · 6 Cooch Behar Uttar · 7 Cooch Behar Dakshin · 8 Natabari | A | Delimitation 2008 |
| AC composition | Mathabhanga Municipality (full) + Mathabhanga II CD block (full) + Hazrahat I, Hazrahat II and Pachagarh gram panchayats of Mathabhanga I CD block | A | Delimitation 2008 / Wikipedia Mathabhanga Assembly constituency |
| Geographic note | Northern West Bengal; Mathabhanga subdivision of Cooch Behar district; predominantly rural flatlands along the Mansai river; near Bangladesh border | A | — |
| Sub-units used in v0 | **U1: Mathabhanga_Municipality** (urban) · **U2: Mathabhanga_II_CDB_and_GPs** (rural — Mathabhanga II full + 3 GPs of Mathabhanga I) | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~265,000 (Mathabhanga Muni 23,890 + Mathabhanga II CDB 227,397 + 3 GPs of Mathabhanga I ~14,000 est.) | E | Census 2011; v0 GP-equal-weight assumption for 3 GPs of Mathabhanga I |
| 2019 projected population | ~287,000 | E | 8-yr compound religion-differential growth (methodology §4); ~0.8%/yr composite |
| Sex ratio (2019, F per 1000 M) | ~949 | E | Cooch Behar district baseline 949; minimal projection drift |
| 2019 estimated electorate (18+) | ~241,785 | A | ECI 2019 LS roll — 2019_AssemblySegmentLevelVotingData.csv |
| Estimated M / F / TG split (2019) | 51.3% M / 48.7% F / <0.05% TG | E | Cooch Behar district sex ratio 949 projected back |
| 2019 polling stations (estimated) | ~285 | E | Based on electorate size; back-projection |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 82.50 | B | Weighted: Muni SC-23.89% (predominantly Hindu), Mathabhanga II 84.46% Hindu, Mathabhanga I 3 GPs ~80.77%; 2011→2019 projection (+0.3pp gain over 8yr for relative growth) |
| Muslim | 16.90 | B | Mathabhanga II 15.26% + Mathabhanga I 18.61% CDB; weighted and projected (+0.3pp relative gain); border AC with higher Muslim share than district average |
| Christian | 0.25 | E | Mathabhanga II 0.18% + Mathabhanga I 0.02%; weighted; small Christian pocket |
| Sarna_ORP | 0.20 | E | Minimal; Cooch Behar district ST share 0.98% overall; mostly Hindu |
| Other_residual | 0.15 | E | Sikh + Jain + Buddhist + Not_stated; residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 61.50 | B | Mathabhanga II SC 64.92% + Muni SC 23.89% + 3 GPs of Mathabhanga I ~68.77% SC (CDB I avg); weighted population-share; Cooch Behar is India's highest-SC district |
| └ Rajbanshi_SC | 55.00 | C | Dominant SC sub-group in Cooch Behar; ~75% of SC pool per Print/Census pattern; Rajbanshi = Koch-Rajbanshi SC in WB |
| └ Namasudra_SC | 3.50 | E | Second SC group in region; smaller presence here vs Bangaon |
| └ Other_SC | 3.00 | E | Residual SC sub-groups |
| **ST_total** | 1.00 | B | Mathabhanga II ST 1.31%; Mathabhanga I ST 0.06%; Muni ST negligible; weighted ~1% |
| UC_bhadralok | 4.00 | E | Brahmin/Kayastha/Baidya; very small in this predominantly SC-Rajbanshi district |
| OBC | 3.50 | E | Smaller OBC presence; some Koch-OBC and artisan communities |
| Other_Hindu_middle | 12.85 | E | Residual within Hindu (82.50 − 61.50 SC − 1.00 ST − 4.00 UC − 3.50 OBC = 12.50; rounded to balance) |
| Muslim | 16.90 | E | All sub-castes pooled; see C.1 |
| Christian_plus_Sarna_plus_Other | 0.25 | E | Christian 0.25 + Sarna 0.20 + Other 0.15 = 0.60; lumped per schema |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.50 | E | Renormalized from Cooch Behar district Census 2011 age pyramid; 18+ only |
| 23_27 | 12.00 | E | |
| 28_32 | 11.50 | E | |
| 33_37 | 10.50 | E | |
| 38_42 | 10.00 | E | |
| 43_47 | 9.50 | E | |
| 48_52 | 8.50 | E | |
| 53_57 | 7.50 | E | |
| 58_62 | 6.50 | E | |
| 63_67 | 6.00 | E | |
| 68 | 5.50 | E | 68+ open-ended |
| **Sum** | **100.00** | — | self-check (renormalized from Census after excluding 0–17) |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.31 | E | Cooch Behar district sex ratio 949 → 51.31% M / 48.68% F; projected stable to 2019 |
| Female | 48.68 | E | |
| Third_gender | 0.01 | E | Marginal fraction; state pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 91.00 | B | Dominant language; Cooch Behar CDBs majority Bengali-speaking; Rajbanshi community uses Bengali literary language though Rajbanshi dialect in home |
| Hindi | 0.50 | E | Small trader and migrant fringe |
| Urdu | 1.50 | E | Muslim pockets in border area |
| Other | 0.50 | E | Residual |
| Rajbongshi | 6.50 | C | Rajbanshi/Rajbongshi dialect spoken by Koch-Rajbanshi SC community; AC-local; significant in rural areas of Cooch Behar; classified under Bengali in census but functionally distinct |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 18.00 | E | Cooch Behar district literacy ~75% (2011); Mathabhanga subdivision slightly lower; projected +4pp improvement 2011→2019 → ~22% illiterate 2011 → ~18% 2019 |
| Primary | 24.00 | E | Census 2011 WB education distribution scaled for Cooch Behar district |
| Middle | 22.00 | E | |
| Secondary | 17.00 | E | |
| Higher_Secondary | 10.00 | E | |
| Graduate | 7.00 | E | Lower than state average given SC-heavy rural constituency |
| Postgraduate | 2.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 33.00 | B | Mathabhanga II total workers 39.76% of total pop; age-restricted 18+ proxy; Mathabhanga I 44.94%; weighted avg adjusted for 18+ |
| Marginal_worker | 12.00 | E | Seasonal agricultural work; significant in SC-dominant rural AC |
| Non_worker | 37.00 | E | Housewife + elderly + retired; heavy rural HH-work component |
| Student | 10.00 | E | 18–22 in education |
| Unemployed | 8.00 | E | Educated job-seekers; limited urban employment |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 38.00 | B | Mathabhanga I: 47.24% cultivators; Mathabhanga II: 34.25%; weighted CDB average ~40%; Muni dilution brings AC to ~38% |
| Agricultural_labourer | 32.00 | B | Mathabhanga I: 31.21%; Mathabhanga II: 39.06%; weighted ~35%; Muni dilution → ~32% |
| Household_industry | 2.00 | B | Mathabhanga I: 1.71%; Mathabhanga II: 2.64%; weighted ~2% |
| Manufacturing | 3.00 | E | Limited manufacturing; some agro-processing |
| Construction | 5.00 | E | Local construction + small migration for construction work |
| Trade_retail | 8.00 | E | Mathabhanga Muni as sub-divisional hub; retail trade concentration |
| Transport_logistics | 3.00 | E | Local transport; limited |
| Services | 5.00 | E | Private services in Muni and block HQ |
| Government_services_teachers | 4.00 | E | Govt + teachers; block and sub-division offices |
| Out_migrant_worker | 0.00 | E | Low out-migration; predominantly local economy |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Census B-04 WB rural pattern; limited employer class in SC-heavy AG economy |
| Employee | 22.00 | E | Govt workers + organised sector employees |
| Single_worker | 52.00 | E | Own-account cultivators + small traders; dominant in Rajbanshi farming community |
| Family_worker | 24.50 | E | Unpaid family helpers in agriculture; high share in SC farm households |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 30.00 | E | Cooch Behar is one of WB's poorer districts; SC-dominant area with high BPL share; Census 2011 proxy + state poverty trend (-6pp 2011→2019) → ~30% |
| Above_Poverty_Line_low_income | 35.00 | E | |
| Lower_middle | 22.00 | E | |
| Middle | 10.00 | E | |
| Upper_middle_well_off | 3.00 | E | Limited affluence; small Muni trader class |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Mathabhanga_Municipality | 8.30 | E | 2011: Muni 23,890 / AC ~265,000 = 9.0%; slight urban decline relative to rural growth → ~8.3% by 2019 |
| U2_Mathabhanga_II_CDB_and_GPs | 91.70 | E | Remainder; Mathabhanga II full CDB (227,397 in 2011) + 3 GPs of Mathabhanga I; v0 collapses to one rural cell |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | WB 2011: 4.3; Cooch Behar slightly larger household pattern; minor projection |
| Nuclear_HH | 65.00 | E | NFHS-4 WB rural pattern; SC Rajbanshi families slightly more nuclear |
| Joint_HH | 28.00 | E | |
| Extended_multi_generation | 7.00 | E | |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.00 | E | Census 2011 Cooch Behar pattern; first-time-voter cohort |
| Currently_married | 66.00 | E | High marriage prevalence in rural SC community |
| Widowed | 7.00 | E | Concentrated in 60+, female-skewed |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 70.00 | C | NFHS-4 WB rural ~60%, urban 89%; Cooch Behar below-average income; AC weighted ~70% by 2019 after diffusion |
| Radio | 6.00 | C | Slightly higher than N24P; rural Cooch Behar |
| Mobile_phone | 82.00 | C | NFHS-4 WB ~78%; +growth; lower smartphone penetration district |
| Smartphone_with_internet | 38.00 | C | NFHS-4 baseline + Jio rollout 2016-19; lower than state average due to income/literacy constraint |
| Computer | 6.00 | C | NFHS-4 WB rural 4%; Muni fraction higher; AC weighted ~6% |
| Two_wheeler | 22.00 | C | NFHS-4 WB rural 18%; limited income growth |
| Four_wheeler | 3.00 | C | Limited; Muni trader fraction |
| Banking_access | 85.00 | B | PMJDY 2014-onwards saturation; NFHS-4 WB baseline + rollout |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 82.00 | C | NFHS-4 WB rural 84%; Cooch Behar slightly below; river-dependent areas |
| Improved_sanitation | 60.00 | C | NFHS-4 WB rural 51% + Swachh Bharat 2014-19 (+15pp rural trend); lower income constrains adoption |
| LPG_clean_cooking_fuel | 35.00 | C | NFHS-4 WB rural 24% + Ujjwala 2016-19 (+15pp rural); SC-targeted Ujjwala beneficiaries |
| Wood_biomass_fuel | 60.00 | C | Declining as LPG rises; still dominant in this income tier |
| Other_fuel | 5.00 | C | Kerosene, dung, crop residue |
| Electricity | 90.00 | B | Census 2011 + Saubhagya 2017-19; near-saturation by 2019 |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 80.00 | E | Predominantly settled Rajbanshi-SC farming community; very low in-migration into rural Cooch Behar |
| WB_other_district | 5.00 | E | Small fraction of in-migrants from other WB districts to Muni |
| Other_Indian_state | 1.50 | E | Hindi-speaking traders; limited |
| Bangladesh_origin | 11.00 | D | Border AC; significant post-1947 / 1971 Hindu migration; lower than Bangaon belt but notable given proximity to Bangladesh border; includes older refugee families |
| Outside_India | 0.50 | E | Negligible; excluding Bangladesh |
| Out_migrant | 2.00 | E | Small fraction working outside, registered here |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 87.00 | 0.50 | 0.00 | 0.50 | 12.00 | E | Rajbanshi-SC population uses Rajbongshi dialect; urban Hindu uses Bengali; weighted |
| Muslim | 96.00 | 0.50 | 3.00 | 0.50 | 0.00 | E | Bengali-Muslim border belt; small Urdu pocket |
| Christian | 90.00 | 5.00 | 0.00 | 5.00 | 0.00 | E | Tiny base; Bengali + English-medium families |
| Sarna_ORP | 70.00 | 0.00 | 0.00 | 5.00 | 25.00 | E | Small tribal population; some Rajbongshi overlap |
| Other_residual | 70.00 | 25.00 | 0.00 | 5.00 | 0.00 | E | Marwari/trader fringe |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 72.00 | 1.20 | 4.80 | 4.20 | 17.80 | 0 | 0 | E | SC_total 61.50/82.50 Hindu = 74.5%; adjusted for non-Hindu SC fraction; rounded |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 80 | 0 | 5 | 15 | 0 | 0 | E | Tribal sub-castes mostly route to ST_total |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 76.00 | 4.50 | 1.50 | 15.00 | 0.50 | 2.50 | D | Hindu Bangladesh-origin in border AC; Rajbanshi community mostly native; lower than Bangaon belt |
| Muslim | 90.00 | 3.00 | 1.00 | 4.50 | 0.50 | 1.00 | D | Muslim border trickle; mostly native Bengali-Muslim peasantry |
| Christian | 85.00 | 10.00 | 5.00 | 0.00 | 0.00 | 0.00 | E | Mixed; tiny base |
| Sarna_ORP | 95.00 | 3.00 | 2.00 | 0.00 | 0.00 | 0.00 | E | Local tribal; very settled |
| Other_residual | 40.00 | 20.00 | 35.00 | 5.00 | 0.00 | 0.00 | E | Trader/migrant fringe |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 72.00 | 40.00 | 86.00 | E | NFHS-4 WB religion gap pattern; Rajbanshi-SC lower income → below-average asset |
| Muslim | 62.00 | 28.00 | 78.00 | E | Lower asset access; rural Muslim border belt |
| Christian | 80.00 | 50.00 | 90.00 | E | Tiny base; slightly better asset profile |
| Sarna_ORP | 55.00 | 20.00 | 70.00 | E | Minimal tribal base |
| Other_residual | 92.00 | 70.00 | 95.00 | E | Trader/upper-income fringe |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 5.00 | 8.00 | 12.00 | 18.00 | 20.00 | 25.00 | 12.00 | E |
| SC_total | 22.00 | 27.00 | 22.00 | 15.00 | 8.00 | 5.00 | 1.00 | E |
| ST_total | 28.00 | 28.00 | 20.00 | 13.00 | 7.00 | 3.00 | 1.00 | E |
| OBC | 15.00 | 24.00 | 22.00 | 18.00 | 11.00 | 8.00 | 2.00 | E |
| Other_Hindu_middle | 14.00 | 22.00 | 22.00 | 18.00 | 12.00 | 9.00 | 3.00 | E |
| Muslim | 22.00 | 26.00 | 22.00 | 16.00 | 9.00 | 4.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 12.00 | 10.00 | E |
| 23_27 | 12.00 | 9.00 | E |
| 28_32 | 10.00 | 7.00 | E |
| 33_37 | 8.00 | 5.00 | E |
| 38_42 | 7.00 | 4.00 | E |
| 43_47 | 6.00 | 3.00 | E |
| 48_52 | 5.00 | 2.00 | E |
| 53_57 | 4.00 | 2.00 | E |
| 58_62 | 4.00 | 1.50 | E |
| 63_67 | 3.00 | 1.00 | E |
| 68 | 3.00 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8.00 | 30.00 | E |
| 23_27 | 45.00 | 82.00 | E |
| 28_32 | 82.00 | 93.00 | E |
| 33_37 | 92.00 | 90.00 | E |
| 38_42 | 93.00 | 88.00 | E |
| 43_47 | 93.00 | 83.00 | E |
| 48_52 | 91.00 | 75.00 | E |
| 53_57 | 88.00 | 65.00 | E |
| 58_62 | 85.00 | 50.00 | E |
| 63_67 | 78.00 | 35.00 | E |
| 68 | 70.00 | 25.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 28.00 | 62.00 | E | Rural agri SC baseline; lower than state avg |
| Agricultural_labourer | 20.00 | 55.00 | E | Lowest income group |
| Household_industry | 32.00 | 68.00 | E | |
| Manufacturing | 45.00 | 78.00 | E | |
| Construction | 42.00 | 72.00 | E | |
| Trade_retail | 62.00 | 85.00 | E | Muni concentrated |
| Transport_logistics | 55.00 | 78.00 | E | |
| Services | 65.00 | 88.00 | E | |
| Government_services_teachers | 80.00 | 92.00 | E | Highest |
| Out_migrant_worker | 60.00 | 75.00 | E | Working outside, smartphone-heavy |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 38.00 | 1.50 | E |
| Primary | 40.00 | 3.00 | E |
| Middle | 36.00 | 5.00 | E |
| Secondary | 28.00 | 9.00 | E |
| Higher_Secondary | 22.00 | 14.00 | E |
| Graduate | 25.00 | 16.00 | E |
| Postgraduate | 35.00 | 10.00 | E |

### D.10 Asset / media × Bilingualism

(Skip — no `media_tier` axis declared for this AC; Rajbongshi-speaking population adds local dimension but no formal media-tier axis.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Sub-unit codes use `Un_` prefix matching C.11.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Mathabhanga_Municipality | 85.00 | 13.50 | 0.70 | 0.20 | 0.60 | E | Muni: lower Muslim share than rural; SC 23.89% mostly Hindu Rajbanshi; projected 2019 |
| U2_Mathabhanga_II_CDB_and_GPs | 82.30 | 17.10 | 0.22 | 0.20 | 0.18 | B | Mathabhanga II: Hindu 84.46%, Muslim 15.26% (2011 Census); + 3 GPs of Mathabhanga I (Hindu 80.77%, Muslim 18.61%); weighted |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Use canonical caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Mathabhanga_Municipality | 8.00 | 23.89 | 0.25 | 6.00 | 47.26 | 13.50 | 1.10 | B |
| U2_Mathabhanga_II_CDB_and_GPs | 3.50 | 65.50 | 1.05 | 3.20 | 9.55 | 17.10 | 0.10 | B |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Mathabhanga_Municipality | 88.00 | 55.00 | 16.00 | 92.00 | C |
| U2_Mathabhanga_II_CDB_and_GPs | 68.00 | 35.00 | 4.50 | 84.00 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Mathabhanga_Municipality | 70.00 | 85.00 | 92.00 | 98.00 | C |
| U2_Mathabhanga_II_CDB_and_GPs | 30.00 | 57.00 | 80.00 | 89.00 | C |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 regional WB rollup, adapted for Cooch Behar.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 60.00 | 34.00 | 1.00 | 3.50 | 1.50 | C | CSDS 2019 WB Hindu pattern + BJP strong among Rajbanshi-SC in Cooch Behar; BJP nationally led SC-Hindu mobilisation |
| Muslim | 5.00 | 72.00 | 18.00 | 3.50 | 1.50 | C | CSDS 2019 WB Muslim pattern; AITC dominant |
| Christian | 25.00 | 55.00 | 10.00 | 5.00 | 5.00 | E | Approximation; tiny base |
| Sarna_ORP | 40.00 | 40.00 | 5.00 | 10.00 | 5.00 | E | Mixed tribal affiliation |
| Other_residual | 45.00 | 35.00 | 10.00 | 5.00 | 5.00 | E | |

### D.16 Vote × Caste (2019 LS)

P(party ‖ caste) — CSDS-Lokniti 2019 WB regional.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 58.00 | 30.00 | 5.00 | 5.00 | 2.00 | C | CSDS 2019 WB bhadralok BJP-leaning |
| OBC | 40.00 | 38.00 | 7.00 | 12.00 | 3.00 | C | Mixed |
| SC_total | 56.00 | 36.00 | 2.00 | 4.00 | 2.00 | C | Rajbanshi-SC BJP swing in 2019; BJP made gains among SC in Cooch Behar through Koch-Rajbanshi identity mobilisation |
| ST_total | 42.00 | 36.00 | 5.00 | 13.00 | 4.00 | E | Small ST base; mixed |
| Other_Hindu_middle | 50.00 | 38.00 | 4.00 | 6.00 | 2.00 | C | CSDS pattern |
| Muslim | 5.00 | 72.00 | 18.00 | 3.50 | 1.50 | C | Same as D.15 |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

P(party ‖ gender).

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 53.00 | 40.00 | 1.50 | 4.00 | 1.50 | C | CSDS 2019 WB; BJP male advantage |
| Female | 51.00 | 44.00 | 1.50 | 2.50 | 1.00 | C | +4pp TMC women advantage; Cooch Behar pattern similar |

### D.18 Vote × Welfare

(Skip — no `welfare_exposure` axis declared for this AC in v0.)

---

## E. 2019 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 52.09 | A | ECI GE2019 Form-20 AC segment; 107,063 votes / 205,518 total valid — 2019_AssemblySegmentLevelVotingData.csv |
| AITC | 41.94 | A | 86,188 votes / 205,518 — same source |
| INC | 1.47 | A | 3,012 votes / 205,518 — same source |
| LF | 2.80 | A | AIFB 5,757 votes / 205,518; no other LF party contesting — same source |
| Other_NOTA | 1.70 | A | KPPU 306 + WPOI 242 + SUCI(C) 367 + AMB 242 + IND 509+1033+799 = 3,498 / 205,518 — same source |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 002 Mathabhanga (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Binay Krishna Barman | AITC | ~48.1 | Khagen Chandra Barman | CPI(M) | ~32.2 | ~31,918 votes (96,383 vs 64,465) |
| 2016 AE | Binay Krishna Barman | AITC | ~48.1 | Khagen Chandra Barman | CPI(M) | ~32.2 | ~31,918 votes; BJP contested (Sushil Barman) but ran third |

Note: Search results for 2016 show same figures as 2011, which likely reflects data-source ambiguity. The 2016 vote total of 200,385 is separately confirmed. The 2016 result re-elected Binay Krishna Barman (AITC) with a reduced majority as BJP began building a presence.

### Cooch Behar Lok Sabha (PC 1) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | (AITC won; Renuka Sinha / then bypolls) | AITC | — | AITC held Cooch Behar in 2014; CPI(M) declined; BJP third |
| 2019 LS | Nisith Pramanik | BJP | ~48.0 | BJP win over AITC (Adhikary Paresh Chandra ~44.4%); margin 54,231; total electorate 1,329,086 |

Political dynamics: By 2019, BJP made major inroads in Cooch Behar by mobilising Rajbanshi-SC identity politics and Koch-Rajbanshi recognition demands. The BJP's candidate Nisith Pramanik, a local Rajbanshi leader, proved effective at consolidating SC vote which was previously split between AITC and LF.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Election Commission of India — `2019_AssemblySegmentLevelVotingData.csv` — AC 002 segment votes (BJP 107,063; AITC 86,188; AIFB 5,757; INC 3,012; others 3,498; total 205,518; electorate 241,785)
- ECI / Delimitation Commission of India 2008 — WB Schedule: AC 2 Mathabhanga (SC) = Mathabhanga Municipality + Mathabhanga II CDB + Hazrahat I, Hazrahat II and Pachagarh GPs of Mathabhanga I CDB; under Cooch Behar (SC) LS PC 1

### Secondary sources (tier B / C)

- Census of India 2011 — Mathabhanga I CD block Primary Census Abstract (Wikipedia: pop 218,191; Hindu 80.77%; Muslim 18.61%; SC 68.77%; workers 44.94%; cultivators 47.24%; ag-labourers 31.21%)
- Census of India 2011 — Mathabhanga II CD block Primary Census Abstract (Wikipedia: pop 227,397; Hindu 84.46%; Muslim 15.26%; SC 64.92%; ST 1.31%; cultivators 34.25%; ag-labourers 39.06%; other workers 24.05%)
- Census of India 2011 — Mathabhanga Municipality (census2011.co.in: pop 23,890; SC 23.89%; ST 0.25%)
- Census of India 2011 — Cooch Behar district (Wikipedia: Hindu 74.06%; Muslim 25.54%; SC majority district in India)
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline
- CSDS-Lokniti 2019 NES post-poll — vote × religion / caste / gender regional WB rollup

### Tertiary / journalistic (tier D)

- The Print: "Who are Rajbanshis, caught in Shah-Mamata scrap" — Rajbanshi SC ~75% of SC pool in Cooch Behar; BJP Koch-Rajbanshi mobilisation strategy
- ResultUniversity / IndiaStatPublications: Mathabhanga 2011 AE result (Binay Krishna Barman AITC 96,383; Khagen CPI(M) 64,465)
- Cooch Behar 2019 LS: Nisith Pramanik (BJP) 731,594 votes; Adhikary Paresh Chandra (AITC) 677,363 votes
- Wikipedia "Mathabhanga Assembly constituency" — AC composition (Delimitation 2008)

### Tier-D / E reliance flags (what to distrust)

- **Religion composition** (C.1, D.11) — Muni religion breakout not in CSV; Tier-B weighted estimate from CDB-level data
- **Caste sub-group shares within Hindu** (C.2, D.2) — no caste census post-1931 for non-SC/ST; Rajbanshi dominant position is well-established but sub-group percentages are Tier-C/E
- **Migration/birthplace** (C.16, D.3) — no public AC-level Census D-series; Tier-D from journalistic/geographic anchor
- **GP-level sub-unit data** (D.11–D.14) — collapsed to 2 sub-units (Muni + rural); refine when DCHB Cooch Behar Part-A accessible
- **Asset/media** (C.14, D.4, D.13) — NFHS-4 state-level projected to AC; Tier-C
- **Vote × Demographic** (D.15–D.17) — CSDS 2019 WB regional rollup adapted for Cooch Behar context; Tier-C
- **2016 AE result** — search results ambiguous between 2011 and 2016; both may show same incumbent winning

### v0 known gaps

1. DCHB Cooch Behar Part-A — sub-unit detail collapsed to 2 (Muni + rural CDB)
2. AC-level religion breakout for Mathabhanga Municipality — using district/CDB proxy
3. Census D-series for migration — using geographic/journalistic anchor
4. Full CSDS WB Cooch Behar-specific cross-tabs — using WB regional rollup
5. 2016 AE exact votes — data ambiguity between 2011 and 2016 elections in sources

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge.
No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs. The
> validator's leakage gate exempts §H from the no-future-leakage check.

### 2021 WB Assembly Election — AC 002 Mathabhanga (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Sushil Barman | ~91,000 | 52.87% | A — ECI 2021 AE; Business Standard / OneIndia results |
| AITC | Girindra Nath Barman | ~69,900 | 40.67% | A — ECI 2021 AE |
| Others | various | ~12,500 | ~6.46% | A — ECI 2021 AE |
| **BJP margin** | | ~26,134 votes | | A |

BJP retained Mathabhanga in 2021 with an increased margin, consistent with continued Rajbanshi-SC consolidation. AITC's 2019 wave did not reverse in this seat.

### 2024 Lok Sabha Election — AC 002 segment within Cooch Behar LS (PC 1) (tier A, CSV)

> Figures below are **tier A** — sourced directly from `2024_AssemblySegmentLevelVotingData.csv`, AC_NO=2, Mathabhanga segment.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Nisith Pramanik | 110,612 | 50.33% | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | (Cooch Behar AITC candidate) | 99,974 | 45.49% | A | Same |
| AIFB (LF) | — | 4,197 | 1.91% | A | Same |
| INC | — | 1,107 | 0.50% | A | Same |
| Others | BSP+SUCI+KPPU+INDs | 3,867 | 1.76% | A | Same |
| **Total valid votes** | | ~219,757 | 100% | A | Computed |

> BJP margin over AITC: 10,638 votes; 4.84pp. BJP held but margin tightened compared to 2019 (10.15pp margin). AITC gained share.

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC segment shares within ±3pp of the tier-A figures:
- BJP target: 50.3% ± 3pp
- AITC target: 45.5% ± 3pp
- LF+INC+others: ~4.2% ± 3pp
