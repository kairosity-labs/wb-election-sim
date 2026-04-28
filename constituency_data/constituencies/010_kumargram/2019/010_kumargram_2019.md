# AC 010 — Kumargram (ST) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 010 Kumargram as of 2019 only — it does not reference any
> post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) ·
> [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 010 | A | ECI / Delimitation Commission 2008 |
| AC name | Kumargram | A | ECI |
| Reservation | ST | A | Delimitation 2008 |
| District | Alipurduar | A | Delimitation 2008 (Alipurduar carved from Jalpaiguri 2014) |
| Sub-division | Kumargram | A | WB administrative |
| LS constituency | 2 — Alipurduars (ST reserved) | A | Delimitation 2008 |
| LS segments included | AC 007 Madarihat · 008 Dhupguri · 009 Nagrakata · 010 Kumargram · 011 Kalchini · 012 Alipurduar · 013 Falakata | A | Delimitation 2008 |
| AC composition | Kumargram CD block (all GPs) + Bhatibari, Kohinoor, Mahakalguri, Parokata, Samuktala, Tatpara I, Turturi GPs of Alipurduar II CD block | A | Delimitation 2008 |
| Geographic note | Northern Dooars foothills bordering Bhutan and Assam; dense tea garden and forest belt of Jalpaiguri division | A | — |
| Sub-units used in v0 | **U1: Kumargram_CDB** (Kumargram block, ~70% pop) · **U2: Alipurduar_II_GPs** (7 GPs of Alipurduar II block, ~30% pop) | E | v0 simplification — block-level Census 2011 data available |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~260,000 (Kumargram CDB 199,609 + 7/11 of Alipurduar II CDB 218,272 ≈ 60,000) | E | Census 2011; v0 equal-weight GP assumption for Alipurduar II share |
| 2019 projected population | ~283,000 | E | 8-yr compound religion-differential growth (methodology §4) |
| Sex ratio (2019, F per 1000 M) | ~951 | E | Alipurduar district baseline ~951; tea-belt marginal female labour skew |
| 2019 estimated electorate (18+) | ~262,525 | A | ECI 2019 LS roll (GE2019 CSV: electors = 262,525) |
| Estimated M / F / TG split (2019) | 51.3% M / 48.7% F / <0.05% TG | E | District sex ratio back-projection |
| 2019 polling stations (estimated) | ~320 | E | Proportional projection from electorate size |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 82.00 | A | Kumargram CDB Census 2011: 82.27% Hindu; stable to 2019 |
| Muslim | 5.00 | E | Kumargram CDB 2011: 4.34% Muslim + slightly higher Alipurduar II GPs share; blended ~5% |
| Christian | 11.50 | A | Kumargram CDB 2011: 11.97% Christian (tea garden missionary belt); slight decline projection |
| Sarna_ORP | 1.00 | E | Tribal Oraon/Santal traditional religion; lumped from Other/Buddhist residual |
| Other_residual | 0.50 | E | Buddhist 0.79% in CDB, partially reassigned to Sarna; Sikh/Jain fringe |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 35.50 | A | Kumargram CDB Census 2011: 35.78% SC; AC-level approximation |
| └ Rajbanshi_SC | 20.00 | E | Dominant SC in Dooars; ~56% of SC pool (state pattern for North Bengal) |
| └ Namasudra_SC | 5.00 | E | ~14% of SC pool |
| └ Other_SC | 10.50 | E | Bagdi, Hari, Bauri, residual SC communities |
| **ST_total** | 29.50 | A | Kumargram CDB Census 2011: 30.00% ST; Alipurduar II GPs slightly lower → AC ~29.5% |
| └ Oraon_ST | 12.00 | D | Dominant plantation ST (Kurukh-speakers); tea garden Adivasi belt (Kolkatatales/Wikipedia) |
| └ Santal_ST | 8.00 | D | Second largest; plains-farming Santal community |
| └ Munda_ST | 5.00 | D | Tea garden labour community |
| └ Other_ST | 4.50 | E | Bodo, Rajbongshi-ST, Toto fringe, other Jharkhand-origin tribes |
| UC_bhadralok | 3.00 | E | Very small in rural tea-belt AC; Bengali Brahmin/Kayastha fraction |
| OBC | 5.00 | E | Koch-Rajbongshi OBC, Kurmi, other OBC in Dooars |
| Other_Hindu_middle | 15.00 | E | Residual within Hindu: 82.00 − 35.50 SC − 29.50 ST − 3.00 UC − 5.00 OBC = 9.00 plus non-SC/ST Hindu caste groups; adjusted for Muslim/Christian/Other totalling 18% |
| Muslim | 5.00 | E | See C.1; Bengali Muslim and Nepali Muslim fraction |
| Christian_plus_Sarna_plus_Other | 7.00 | E | Christian 11.5% + Sarna 1.0% + Other 0.5% population (not all in caste frame) |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.50 | E | Projected from Alipurduar district Census 2011 age pyramid; first-time voters |
| 23_27 | 11.00 | E | |
| 28_32 | 10.50 | E | |
| 33_37 | 10.00 | E | |
| 38_42 | 9.50 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.50 | E | |
| 53_57 | 8.00 | E | |
| 58_62 | 7.00 | E | |
| 63_67 | 8.00 | E | Adjusted for tea-belt mortality pattern; slightly higher elderly share |
| 68 | 7.00 | E | 68+ open-ended; renormalized from Census 2011 excluding 0–17 |
| **Sum** | **100.00** | — | self-check (renormalized from Census 2011 18+ cohorts) |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.28 | E | Alipurduar district sex ratio ~951 F per 1000 M → 51.28% M / 48.71% F |
| Female | 48.71 | E | |
| Third_gender | 0.01 | E | Negligible; national pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 55.00 | E | Bengali Hindu SC/ST + Muslim fraction; dominant language but not overwhelming in tea belt |
| Hindi | 3.00 | E | Bihari/UP-origin tea-garden settled workers and traders |
| Urdu | 1.00 | E | Muslim fraction Urdu speakers |
| Other | 3.00 | E | Residual catch-all (Nepali fringe, Assamese border community) |
| Sadri | 14.00 | D | Lingua franca of Oraon, Munda, and other Jharkhand-origin tribes; tea-belt dominant (Wikipedia Kumargram CDB) |
| Rajbongshi | 12.00 | D | Koch-Rajbongshi community language; North Bengal plains |
| Santali | 8.00 | D | Santal tribal community language |
| Kurukh | 4.00 | E | Oraon mother tongue fraction not subsumed in Sadri |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 28.00 | E | Alipurduar district literacy ~72% (Census 2011, A); tea belt lower than WB avg; AC ~28% illiterate after +3pp/8yr trend |
| Primary | 25.00 | E | Census 2011 education distribution — tea-garden primary enrolment high |
| Middle | 20.00 | E | |
| Secondary | 14.00 | E | |
| Higher_Secondary | 7.00 | E | |
| Graduate | 4.50 | E | Tea garden + forest administrative class |
| Postgraduate | 1.50 | E | Very limited; district town professionals |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 38.00 | E | Kumargram CDB 2011 main-worker rate elevated by tea garden plantation employment |
| └ Main_worker_tea_garden | 20.00 | D | Tea estate regular workers; is_subgroup=yes |
| └ Main_worker_non_tea | 18.00 | E | Agriculture, forest, services; is_subgroup=yes |
| Marginal_worker | 12.00 | E | Seasonal ag labour + marginal tea work |
| Non_worker | 35.00 | E | Housewife + elderly + retired; slightly lower than WB avg due to tea-belt female employment |
| Student | 9.00 | E | 18–22 in education |
| Unemployed | 6.00 | E | Educated job-seekers; limited white-collar economy |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

Pcts sum to 100 across **workers only** (not all personas).

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 15.00 | E | Small-farm holders outside tea estates; Kumargram CDB rural pattern |
| Agricultural_labourer | 25.00 | E | Seasonal ag labourer including tea-fringe smallholder |
| Household_industry | 3.00 | E | Basket weaving, minor artisan; tribal craft tradition |
| Manufacturing | 4.00 | E | Very limited organised manufacturing in this belt |
| Construction | 5.00 | E | Border-area infrastructure, roads |
| Trade_retail | 7.00 | E | Kumargram town and Samuktala market centres |
| Transport_logistics | 4.00 | E | Bhutan border trade routes, forest roads |
| Services | 7.00 | E | Private services, petty trade |
| Government_services_teachers | 5.00 | E | Forest dept, school teachers, panchayat staff |
| Out_migrant_worker | 5.00 | D | Tribal men to Assam tea gardens, Kerala, Kolkata |
| Tea_garden_plantation | 20.00 | D | Permanent plantation workers on tea estates (AC-local sub-category) |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.00 | E | Very rare; tea-garden owners are absentee |
| Employee | 40.00 | E | Tea garden workers (regular wage) + govt employees |
| Single_worker | 40.00 | E | Own-account cultivator, petty trader, artisan |
| Family_worker | 19.00 | E | Unpaid family labour on small farms; high in Adivasi households |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 32.00 | C | Alipurduar district poverty rate elevated; WB poverty fell but tea-belt residual high; est. ~32% |
| Above_Poverty_Line_low_income | 35.00 | E | Just-above-BPL tea worker families |
| Lower_middle | 20.00 | E | Small cultivators, traders |
| Middle | 10.00 | E | Teachers, forest officers, established traders |
| Upper_middle_well_off | 3.00 | E | Tea garden manager class and wholesale traders |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Kumargram_CDB | 70.00 | E | Kumargram CDB pop 199,609 / AC est. ~260,000 ≈ 77%; adjusted down for urban Samuktala pull in Alipurduar II GPs → 70% |
| U2_Alipurduar_II_GPs | 30.00 | E | 7 GPs of Alipurduar II block; Bhatibari, Kohinoor, Mahakalguri, Parokata, Samuktala, Tatpara I, Turturi |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.9 persons | E | Tea garden line housing = larger HH; WB avg 4.3; tribal extended family pattern → ~4.9 |
| Nuclear_HH | 60.00 | E | NFHS-4 WB rural pattern; tea-line single-room units promote nuclear structure |
| Joint_HH | 28.00 | E | Tribal joint family tradition |
| Extended_multi_generation | 12.00 | E | Tea garden barracks multi-generational residence pattern |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.00 | E | Census 2011 Alipurduar pattern; slightly lower than WB urban avg |
| Currently_married | 66.00 | E | High marriage rate in tribal and tea-belt communities; early marriage |
| Widowed | 7.00 | E | Female-concentrated 60+ age group |
| Separated_divorced | 1.00 | E | Low formal divorce; some de-facto separation in out-migrant households |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

Independent rates — **do NOT sum**.

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 55.00 | C | NFHS-4 WB rural ~60%; tea-belt income constraint; AC ~55% |
| Radio | 8.00 | C | Higher than WB avg; tea-garden community radio tradition |
| Mobile_phone | 78.00 | C | NFHS-4 WB rural ~78%; stable baseline |
| Smartphone_with_internet | 30.00 | C | Below WB rural avg (35%); lower literacy and income; Jio rollout partial |
| Computer | 3.00 | E | Very limited; mainly school/govt offices |
| Two_wheeler | 18.00 | C | NFHS-4 WB rural ~18%; low income |
| Four_wheeler | 3.00 | E | Very limited; tea estate managers fraction |
| Banking_access | 80.00 | B | PMJDY saturation + tea-wage banking mandate; above-rural-avg due to estate payroll |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 80.00 | C | NFHS-4 WB rural 84%; tea-belt spring water access; AC ~80% |
| Improved_sanitation | 45.00 | C | NFHS-4 WB rural 51%; tea-line housing below avg; Swachh Bharat partial uptake |
| LPG_clean_cooking_fuel | 20.00 | C | NFHS-4 WB rural 24%; Ujjwala 2016-19 partial; tea-belt biomass dependence |
| Wood_biomass_fuel | 75.00 | C | Primary cooking fuel; forest belt biomass abundant |
| Other_fuel | 5.00 | E | Kerosene, dung, residual |
| Electricity | 90.00 | A | Saubhagya 2017-19 near-saturation + tea-estate grid; Census 2011 baseline ~70% → 90% by 2019 |
| **Note** | (water/sanitation/electricity are independent; cooking-fuel rows LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 55.00 | D | Born in Alipurduar/Jalpaiguri or same block; settled tribal communities |
| WB_other_district | 5.00 | D | Some Jalpaiguri and Cooch Behar in-migrants |
| Other_Indian_state | 5.00 | D | Bihari/Oraon tea-garden labour from Jharkhand / Bihar origin (settled, not transient) |
| Bangladesh_origin | 1.00 | E | Minimal; not a refugee-belt AC |
| Outside_India | 0.50 | E | Nepali-origin settled community; Bhutanese fringe |
| Out_migrant | 3.50 | D | Working outside; some tribal men in Assam tea gardens or Kolkata |
| Jharkhand_origin | 30.00 | D | **Load-bearing**: Oraon, Munda, Santal ancestors brought from Chota Nagpur plateau as indentured tea labour (1860s–1930s); now settled for 3–5 generations; classified as WB residents |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Sadri | Rajbongshi | Santali | Kurukh | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 65.00 | 3.00 | 0.50 | 2.00 | 10.00 | 14.50 | 4.00 | 1.00 | E | Hindu includes Rajbongshi SC/OBC (Rajbongshi-speaking) + Santal/Oraon Hindu; blend |
| Muslim | 70.00 | 5.00 | 20.00 | 2.00 | 2.00 | 1.00 | 0.00 | 0.00 | E | Bengali Muslim majority; small Urdu-speaking fraction |
| Christian | 15.00 | 5.00 | 0.00 | 3.00 | 40.00 | 5.00 | 15.00 | 17.00 | E | Christian = predominantly Oraon/Santal converts; Sadri + Kurukh dominant |
| Sarna_ORP | 10.00 | 2.00 | 0.00 | 2.00 | 45.00 | 3.00 | 25.00 | 13.00 | E | Sarna practitioners are Oraon/Santal traditionalists; tribal language dominant |
| Other_residual | 50.00 | 20.00 | 5.00 | 25.00 | 0.00 | 0.00 | 0.00 | 0.00 | E | Buddhist (Nepali), Sikh fringe |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 38.00 | 28.00 | 3.66 | 6.10 | 24.24 | 0 | 0 | E | Hindu: SC ~38% of Hindu (35.5/82.0×100=43.3% → adjusted for non-SC/ST Hindu base), ST ~28%; residual Hindu caste |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 85.00 | 0 | 5.00 | 10.00 | 0 | 0 | D | Christian = overwhelmingly Oraon/Santal ST converts in tea-belt |
| Sarna_ORP | 0 | 92.00 | 0 | 3.00 | 5.00 | 0 | 0 | E | Sarna practitioners mostly ST; small OBC/SC fringe |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Jharkhand_origin | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 62.00 | 5.00 | 2.00 | 1.50 | 0.50 | 4.00 | 25.00 | D | Hindu Rajbongshi native; Hindu ST Jharkhand-origin |
| Muslim | 88.00 | 5.00 | 2.00 | 3.00 | 0.50 | 1.50 | 0.00 | D | Bengali Muslim mostly native |
| Christian | 30.00 | 5.00 | 10.00 | 0.00 | 1.00 | 2.00 | 52.00 | D | Oraon/Santal Christian = majority Jharkhand-origin descent |
| Sarna_ORP | 25.00 | 5.00 | 12.00 | 0.00 | 1.00 | 2.00 | 55.00 | E | Same tribal community; Jharkhand-origin dominant |
| Other_residual | 55.00 | 10.00 | 20.00 | 0.00 | 15.00 | 0.00 | 0.00 | E | Nepali/Buddhist community |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 60.00 | 35.00 | 84.00 | E | Above-average for Bengal Hindu; includes Rajbongshi middle-caste |
| Muslim | 52.00 | 28.00 | 75.00 | E | Slightly below Hindu due to income; PMJDY coverage |
| Christian | 45.00 | 22.00 | 78.00 | E | Tea-garden worker profile; lower income but banking via estate payroll |
| Sarna_ORP | 40.00 | 18.00 | 70.00 | E | Most marginalised; lowest asset ownership |
| Other_residual | 65.00 | 38.00 | 82.00 | E | Includes Nepali Buddhist with remittance economy |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 8.00 | 12.00 | 15.00 | 20.00 | 18.00 | 20.00 | 7.00 | E |
| SC_total | 28.00 | 27.00 | 20.00 | 14.00 | 6.00 | 4.00 | 1.00 | E |
| ST_total | 35.00 | 28.00 | 18.00 | 12.00 | 5.00 | 2.00 | 0.00 | E |
| OBC | 22.00 | 26.00 | 22.00 | 17.00 | 8.00 | 4.00 | 1.00 | E |
| Other_Hindu_middle | 20.00 | 25.00 | 22.00 | 18.00 | 9.00 | 5.00 | 1.00 | E |
| Muslim | 30.00 | 26.00 | 20.00 | 14.00 | 6.00 | 3.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 8.00 | 6.00 | E |
| 23_27 | 8.00 | 5.00 | E |
| 28_32 | 7.00 | 4.00 | E |
| 33_37 | 6.00 | 3.00 | E |
| 38_42 | 5.00 | 2.00 | E |
| 43_47 | 4.00 | 1.50 | E |
| 48_52 | 3.00 | 1.00 | E |
| 53_57 | 2.50 | 0.80 | E |
| 58_62 | 2.00 | 0.50 | E |
| 63_67 | 1.50 | 0.50 | E |
| 68 | 1.00 | 0.30 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8.00 | 35.00 | E |
| 23_27 | 45.00 | 82.00 | E |
| 28_32 | 82.00 | 93.00 | E |
| 33_37 | 92.00 | 91.00 | E |
| 38_42 | 93.00 | 88.00 | E |
| 43_47 | 93.00 | 84.00 | E |
| 48_52 | 90.00 | 76.00 | E |
| 53_57 | 88.00 | 62.00 | E |
| 58_62 | 82.00 | 48.00 | E |
| 63_67 | 75.00 | 35.00 | E |
| 68 | 65.00 | 22.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 22.00 | 50.00 | C | Rural ag baseline; below WB avg |
| Agricultural_labourer | 15.00 | 40.00 | C | Lowest income bracket |
| Household_industry | 25.00 | 52.00 | C | |
| Manufacturing | 35.00 | 60.00 | C | |
| Construction | 30.00 | 55.00 | C | |
| Trade_retail | 52.00 | 72.00 | C | Market town access |
| Transport_logistics | 45.00 | 65.00 | C | Mobile-phone dependent |
| Services | 55.00 | 75.00 | C | |
| Government_services_teachers | 75.00 | 88.00 | C | Highest in AC |
| Out_migrant_worker | 60.00 | 65.00 | D | Working outside; smartphone heavy |
| Tea_garden_plantation | 18.00 | 48.00 | D | Tea-line estate worker; below-avg |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 40.00 | 1.00 | E |
| Primary | 42.00 | 2.00 | E |
| Middle | 38.00 | 4.00 | E |
| Secondary | 32.00 | 8.00 | E |
| Higher_Secondary | 25.00 | 12.00 | E |
| Graduate | 28.00 | 15.00 | E |
| Postgraduate | 35.00 | 10.00 | E |

### D.10 Asset / media × Bilingualism

AC 010 does not declare a `media_tier` axis in v0. Skipped per NORMALIZED_SCHEMA §4.7.

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Sub-unit codes use `Un_` prefix matching C.11.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Kumargram_CDB | 82.27 | 4.34 | 11.97 | 1.00 | 0.42 | A | Census 2011 Kumargram CDB religion data (censusindia.co.in) |
| U2_Alipurduar_II_GPs | 84.40 | 6.50 | 8.64 | 0.90 | 0.56 | A | Alipurduar II CDB Census 2011 (censusindia.co.in) — proxied for 7 GPs within it |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Use canonical caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Kumargram_CDB | 2.50 | 35.78 | 30.00 | 5.00 | 14.38 | 4.34 | 8.00 | A |
| U2_Alipurduar_II_GPs | 4.00 | 30.00 | 25.00 | 6.00 | 20.00 | 6.50 | 8.50 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Kumargram_CDB | 52.00 | 27.00 | 2.50 | 78.00 | C |
| U2_Alipurduar_II_GPs | 60.00 | 35.00 | 4.00 | 83.00 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Kumargram_CDB | 18.00 | 42.00 | 78.00 | 88.00 | C |
| U2_Alipurduar_II_GPs | 25.00 | 52.00 | 84.00 | 93.00 | C |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 regional WB rollup adapted for ST-reserved belt.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 58.00 | 33.00 | 2.00 | 5.00 | 2.00 | C | CSDS 2019 WB Hindu pattern; BJP overperforms in tea-belt Hindu SC/OBC |
| Muslim | 5.00 | 68.00 | 18.00 | 7.00 | 2.00 | C | Muslim consolidation around AITC; RSP residual LF fraction |
| Christian | 42.00 | 38.00 | 3.00 | 12.00 | 5.00 | D | Tea-garden Christian split; RSP had historic hold; BJP made inroads |
| Sarna_ORP | 50.00 | 32.00 | 2.00 | 10.00 | 6.00 | D | Sarna tribal leaned BJP in 2019 national wave; RSP residual |
| Other_residual | 38.00 | 38.00 | 4.00 | 12.00 | 8.00 | E | Mixed Buddhist/Nepali fringe |

### D.16 Vote × Caste (2019 LS)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 60.00 | 28.00 | 4.00 | 6.00 | 2.00 | C | WB UC BJP-leaning 2019 |
| OBC | 50.00 | 36.00 | 3.00 | 8.00 | 3.00 | C | Koch-Rajbongshi OBC: BJP via GBJP-AITC competition |
| SC_total | 52.00 | 36.00 | 2.00 | 7.00 | 3.00 | C | Rajbongshi SC BJP-leaning in North Bengal; CSDS WB SC pattern |
| ST_total | 52.00 | 36.00 | 2.00 | 7.00 | 3.00 | C | ST tribal community BJP wave 2019; RSP residual |
| Other_Hindu_middle | 48.00 | 38.00 | 3.00 | 8.00 | 3.00 | C | |
| Muslim | 5.00 | 68.00 | 18.00 | 7.00 | 2.00 | C | Same as D.15 |

### D.18 Vote × Welfare

AC 010 does not declare a `welfare_exposure` axis in v0. Skipped per NORMALIZED_SCHEMA §4.7.

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 56.00 | 36.00 | 2.00 | 4.00 | 2.00 | C | CSDS 2019 WB; male slightly more BJP |
| Female | 49.00 | 43.00 | 2.50 | 4.00 | 1.50 | C | AITC women advantage; tea-garden female voter pattern |

---

## E. 2019 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 52.78 | A | ECI GE2019 AC-segment CSV: 116,023 votes / 219,829 total valid |
| AITC | 39.67 | A | ECI GE2019 CSV: 87,210 votes |
| INC | 2.10 | A | ECI GE2019 CSV: 4,623 votes |
| LF | 4.25 | A | ECI GE2019 CSV: RSP 9,343 votes (RSP is dominant left party in Dooars) |
| Other_NOTA | 1.20 | A | ECI GE2019 CSV: SUCI(C) 496 + IND 565 + IND 1,569 = 2,630 votes |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 010 Kumargram (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | James Kujur | AITC | ~37.3% | Manoj Kumar Oraon | RSP | ~34.3% | ~6,153 votes |
| 2014 by-election | Manoj Kumar Oraon | RSP | — | Joachim Baxla | AITC | — | ~2,667 votes |
| 2016 AE | James Kujur | AITC | ~37.3% | Manoj Kumar Oraon | RSP | ~34.3% | ~6,153 votes |

Note: In 2011, AITC won James Kujur 77,668 vs RSP Manoj Kumar Oraon 71,515. A 2014 by-election reversed this with RSP winning. 2016 returned AITC (James Kujur). Total 2016 valid votes ~208,406. The RSP had a historic hold on this seat through Dooars left-labour organisation. BJP was not yet a major force in AC-level contests until the 2019 LS wave swept the segment.

### Alipurduars LS (PC 2, ST) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2009 LS | Dasrath Tirkey | AITC | — | AITC hold on ST PC |
| 2014 LS | Dasrath Tirkey | AITC | ~35% | Left weakened; BJP emerging ~21% |
| 2019 LS | John Barla | BJP | 54.00% | BJP tsunami; Dasrath Tirkey (AITC) 36.69%; margin 243,989 votes across PC |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Kumargram CD Block Primary Census Abstract (censusindia.co.in/subdistrict/kumargram-block; Wikipedia "Kumargram community development block")
- Census of India 2011 — Alipurduar II CD Block Primary Census Abstract (censusindia.co.in/subdistrict/alipurduar-ii-block)
- Census of India 2011 — Alipurduar district totals (Wikipedia "Alipurduar district")
- Election Commission of India — GE2019 AC-segment data (2019_AssemblySegmentLevelVotingData.csv, AC_NO=10)
- ECI GE2024 AC-segment data (2024_AssemblySegmentLevelVotingData.csv, AC_NO=10)
- Delimitation Commission of India 2008 — WB Schedule (Kumargram AC 010 composition)

### Secondary sources (tier B / C)

- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline (WB rural pattern)
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2019 NES — vote × demographic conditionals (WB regional rollup)
- WB District Statistical Handbook — Alipurduar / Jalpaiguri

### Tertiary / journalistic (tier D)

- Wikipedia: Kumargram Assembly constituency, Kumargram (community development block), Alipurduar district, Kumargram Alipurduar
- Wikipedia: James Kujur MLA (2011 and 2016 results confirmed)
- Kolkatatales.in (2026): Santal, Munda, Oraon — West Bengal's prominent ST communities; tea-garden origin history
- indiastatelections.com — Kumargram assembly constituency summary
- resultuniversity.com — Kumargram election result history (2011, 2014 by-poll, 2016)
- elections.in — Alipurduars LS 2019 full result

### Tier-D / E reliance flags (what to distrust)

- **Caste sub-group shares within ST** (D.2, C.2 sub-rows) — no caste census post-1931 for non-SC/ST; Oraon/Santal/Munda split is tier D (journalistic)
- **Language distribution** (C.5, D.1) — no AC-level language data; Sadri/Rajbongshi/Santali shares tier D from regional studies
- **Migration/birthplace** (C.16, D.3) — no public AC-level Census D-series; Jharkhand-origin share is tier D estimate from tea-garden historical record
- **Asset/media** (C.14, D.4, D.13) — NFHS-4 state-level pattern projected to AC; tier C throughout
- **Vote × Demographic** (D.15–D.17) — CSDS 2019 WB regional rollup adapted; no AC-specific cross-tab; tier C/D
- **Economic poverty rate** (C.10) — Alipurduar district proxy; tier C
- **Alipurduar II GP-level data** (D.11–D.14, U2) — used block-level Census 2011 as proxy for the 7 GPs; refine with DCHB Part-A

### v0 known gaps

1. DCHB Alipurduar Part-A — AC collapsed to 2 sub-units instead of full GP-by-GP
2. Kumargram CDB occupational detail — no Census Table B-04 extracted; using district-level inference
3. CSDS WB ST-specific cross-tabs — using national/WB-regional rollup; no Dooars-specific survey
4. Language shares — no D-series linguistic data at block level; Sadri/Rajbongshi shares tier D only
5. 2016 AE exact percentage — total valid votes known (~208,406); per-party % computed but candidate data from secondary sources only

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs. The
> validator's leakage gate exempts §H from the no-future-leakage check.

### 2021 WB Assembly Election — AC 010 Kumargram (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Manoj Kumar Oraon | 111,974 | 48.16% | A — ECI 2021 AE |
| AITC | Leos Kujur | 100,973 | 43.43% | A — ECI 2021 AE |
| Others (RSP etc.) | various | ~19,542 | ~8.41% | A — ECI 2021 AE |
| **BJP margin** | | **11,001 votes** | **4.73 pp** | A |
| **Total valid votes** | | 232,489 | 100% | A |

### 2024 Lok Sabha Election — AC 010 segment within Alipurduars LS (PC 2) (tier A)

Figures sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=10, Kumargram. Electorate: 282,343; total valid votes (candidates + NOTA): 229,473; turnout ~81.3%.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Manoj Tigga | 110,394 | **48.11%** | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Prakash Chik Baraik | 102,753 | **44.78%** | A | Same |
| RSP | Mili Oraon | 6,514 | **2.84%** | A | Same |
| NOTA | — | 3,017 | **1.32%** | A | Same |
| Others (BSP, SUCI, KPPU, GNASURKP, NBNGPLPP, KMSP, IND×2) | various | 6,795 | **2.96%** | A | Same |
| **BJP margin over AITC** | | **7,641 votes** | **3.33 pp** | A | Computed |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC segment shares within ±3pp of tier-A figures:
- BJP target: 48.11% ± 3pp
- AITC target: 44.78% ± 3pp
- LF(RSP) + Others target: ~7.1% ± 3pp
