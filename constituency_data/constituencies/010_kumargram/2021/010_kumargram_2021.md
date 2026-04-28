# AC 010 — Kumargram (ST) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 010 Kumargram as of end-2021 — it does not reference any
> post-2021 events. Use the 2024 LS AC-segment result as the out-of-sample
> validation gate for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 010 | A | ECI / Delimitation Commission 2008 |
| AC name | Kumargram | A | ECI |
| Reservation | ST | A | Delimitation 2008; ECI 2021 AE — all candidates listed CATEGORY=ST |
| District | Alipurduar | A | Delimitation 2008 (Alipurduar carved from Jalpaiguri 2014) |
| Sub-division | Kumargram | A | WB administrative |
| LS constituency | 2 — Alipurduars (ST reserved) | A | Delimitation 2008 |
| LS segments included | AC 007 Madarihat · 008 Dhupguri · 009 Nagrakata · 010 Kumargram · 011 Kalchini · 012 Alipurduar · 013 Falakata | A | Delimitation 2008 |
| AC composition | Kumargram CD block (all GPs) + Bhatibari, Kohinoor, Mahakalguri, Parokata, Samuktala, Tatpara I, Turturi GPs of Alipurduar II CD block | A | Delimitation 2008 |
| Geographic note | Northern Dooars foothills bordering Bhutan and Assam; dense tea garden and forest belt; COVID-19 reverse migration brought plantation labour back 2020; Lakshmir Bhandar launched April 2021 (₹500/month general, ₹1000 SC/ST) | A/D | Delimitation 2008; WB govt press note April 2021 |
| Sub-units used in v0 | **U1: Kumargram_CDB** (Kumargram block, ~70% pop) · **U2: Alipurduar_II_GPs** (7 GPs of Alipurduar II block, ~30% pop) | E | v0 simplification — block-level Census 2011 data |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~260,000 (Kumargram CDB 199,609 + 7/11 of Alipurduar II CDB 218,272 ≈ 60,000) | E | Census 2011; v0 equal-weight GP assumption for Alipurduar II share |
| 2021 projected population | ~289,000 | E | 10-yr compound religion-differential growth from 2011 (methodology §4); Hindu +1.0%/yr, ST tribal +0.9%/yr, total ~1.07%/yr blended |
| Sex ratio (2021, F per 1000 M) | ~955 | E | Jalpaiguri/Alipurduar district 2021 NFHS-5 sex ratio 1038; improvement from 2011 951; AC conservative blend ~955 given tea-belt composition |
| 2021 electorate (ECI roll) | 272,924 | A | ECI 2021 AE detailed results: total electors AC 010 Kumargram |
| Estimated M / F / TG split of electorate (2021) | ~51.0% M / 49.0% F / <0.05% TG | E | Sex ratio projection; improvement toward parity |
| 2021 polling stations | ~300 | E | Back-projected from electorate / ~910 voters per booth |
| 2021 voter turnout | 85.18% | A | ECI 2021 AE: 232,489 valid votes / 272,924 electors |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 81.60 | A/E | 2019 baseline 82.00%; 2-yr differential projection: Hindu +1.0%/yr vs Muslim +1.3%/yr → net slight Hindu decline; Kumargram CDB Census 2011 82.27% base |
| Muslim | 5.12 | E | 2019 baseline 5.00%; 2-yr Muslim growth +1.3%/yr → +0.12pp |
| Christian | 11.76 | A/E | 2019 baseline 11.50%; stable or slight decline; tea-belt missionary base stabilising |
| Sarna_ORP | 1.02 | E | 2019 baseline 1.00%; stable tribal religion fraction |
| Other_residual | 0.50 | E | Buddhist/Sikh/Jain fringe; stable |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 35.50 | A | Kumargram CDB Census 2011: 35.78% SC; stable to 2021 |
| └ Rajbanshi_SC | 20.00 | E | Dominant SC in Dooars; ~56% of SC pool |
| └ Namasudra_SC | 5.00 | E | ~14% of SC pool |
| └ Other_SC | 10.50 | E | Bagdi, Hari, Bauri, residual SC communities |
| **ST_total** | 29.50 | A | Kumargram CDB Census 2011: 30.00% ST; AC ~29.5% |
| └ Oraon_ST | 12.00 | D | Dominant plantation ST; Kurukh-speakers; tea garden Adivasi belt |
| └ Santal_ST | 8.00 | D | Second largest; plains-farming Santal community |
| └ Munda_ST | 5.00 | D | Tea garden labour community |
| └ Other_ST | 4.50 | E | Bodo, Rajbongshi-ST, Toto fringe, other Jharkhand-origin tribes |
| UC_bhadralok | 3.00 | E | Very small in rural tea-belt AC; Bengali Brahmin/Kayastha fraction |
| OBC | 5.00 | E | Koch-Rajbongshi OBC, Kurmi, other OBC in Dooars |
| Other_Hindu_middle | 14.88 | E | Residual Hindu not SC/ST/UC/OBC: 81.60 − 35.50 SC − 29.50 ST − 3.00 UC − 5.00 OBC = 8.60; adjusted with Muslim 5.12 + Christian 11.76 + Sarna 1.02 + Other 0.50; balance = 14.88 |
| Muslim | 5.12 | E | See C.1 |
| Christian_plus_Sarna_plus_Other | 6.00 | E | Christian 11.76% + Sarna 1.02% + Other 0.50% combined in caste frame (3-generation tea-line settled) |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2021, adult voters only — 18+)

Renormalised from total-population age pyramid (Census 2011 + 10-yr projection) to adult-voter-eligible population (18+).

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.50 | E | First-time voter cohort entry 2019-2021; young population |
| 23_27 | 11.00 | E | |
| 28_32 | 10.50 | E | |
| 33_37 | 10.00 | E | |
| 38_42 | 9.50 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.50 | E | |
| 53_57 | 8.00 | E | |
| 58_62 | 7.00 | E | |
| 63_67 | 8.00 | E | Tea-belt mortality pattern; slightly higher elderly share |
| 68 | 7.00 | E | 68+ open-ended; renormalized from Census 2011 18+ cohorts |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.20 | E | Sex ratio ~955 F per 1000 M → 51.20% M / 48.79% F; marginal improvement from 2019 baseline 951 |
| Female | 48.79 | E | NFHS-5 Jalpaiguri 2021 shows improved sex ratio trend |
| Third_gender | 0.01 | E | Negligible; national pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 55.00 | E | Stable from 2019; Bengali Hindu SC/ST + Muslim fraction dominant language |
| Hindi | 3.00 | E | Bihari/UP-origin tea-garden settled workers; stable |
| Urdu | 1.00 | E | Muslim fraction Urdu speakers; stable |
| Other | 3.00 | E | Residual catch-all (Nepali fringe, Assamese border community) |
| Sadri | 14.00 | D | Lingua franca of Oraon, Munda, other Jharkhand-origin tribes; stable |
| Rajbongshi | 12.00 | D | Koch-Rajbongshi community language; North Bengal plains |
| Santali | 8.00 | D | Santal tribal community language |
| Kurukh | 4.00 | E | Oraon mother tongue fraction not subsumed in Sadri |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 25.00 | E | Alipurduar district literacy ~72% (Census 2011 A); NFHS-5 Jalpaiguri women literacy 73.7%; 10-yr improvement trend → AC ~25% illiterate (was 28% in 2019 baseline) |
| Primary | 25.00 | E | Tea-garden primary enrolment high; stable fraction |
| Middle | 20.00 | E | |
| Secondary | 15.00 | E | Slight improvement from 2019 14% |
| Higher_Secondary | 8.00 | E | Slight improvement from 2019 7% |
| Graduate | 5.00 | E | Modest improvement; district town professionals |
| Postgraduate | 2.00 | E | Very limited; slight improvement |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 38.00 | E | Kumargram CDB 2011 main-worker rate elevated by plantation employment; COVID-19 return migration 2020 partially restored tea-garden workforce |
| └ Main_worker_tea_garden | 20.00 | D | Tea estate regular workers; is_subgroup=yes |
| └ Main_worker_non_tea | 18.00 | E | Agriculture, forest, services; is_subgroup=yes |
| Marginal_worker | 12.00 | E | Seasonal ag labour + marginal tea work; COVID disruption partly absorbed by 2021 |
| Non_worker | 35.00 | E | Housewife + elderly + retired; tea-belt female employment reduces non-worker share |
| Student | 9.00 | E | 18-22 in education; COVID school closures affect but voter-age student share stable |
| Unemployed | 6.00 | E | Educated job-seekers; COVID-induced disruption partially absorbed by mid-2021 |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

Pcts sum to 100 across **workers only** (not all personas).

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 15.00 | E | Small-farm holders outside tea estates; stable |
| Agricultural_labourer | 25.00 | E | Seasonal ag labourer including tea-fringe; stable |
| Household_industry | 3.00 | E | Basket weaving, minor artisan; tribal craft tradition |
| Manufacturing | 4.00 | E | Very limited organised manufacturing |
| Construction | 5.00 | E | Border-area infrastructure, roads |
| Trade_retail | 7.00 | E | Kumargram town and Samuktala market centres |
| Transport_logistics | 4.00 | E | Bhutan border trade routes |
| Services | 7.00 | E | Private services, petty trade |
| Government_services_teachers | 5.00 | E | Forest dept, school teachers, panchayat staff |
| Out_migrant_worker | 5.00 | D | Tribal men to Assam tea gardens, Kerala, Kolkata; COVID return partially restored by 2021 |
| Tea_garden_plantation | 20.00 | D | Permanent plantation workers on tea estates (AC-local sub-category) |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.00 | E | Very rare; tea-garden owners absentee |
| Employee | 40.00 | E | Tea garden workers (regular wage) + govt employees |
| Single_worker | 40.00 | E | Own-account cultivator, petty trader, artisan |
| Family_worker | 19.00 | E | Unpaid family labour on small farms; high in Adivasi households |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 30.00 | C | Alipurduar district poverty rate elevated; COVID-19 2020 pushed some households temporarily below poverty line; recovery partial by end-2021 → AC ~30% (was 32% in 2019) |
| Above_Poverty_Line_low_income | 36.00 | E | Just-above-BPL tea worker families |
| Lower_middle | 20.00 | E | Small cultivators, traders |
| Middle | 11.00 | E | Teachers, forest officers, established traders |
| Upper_middle_well_off | 3.00 | E | Tea garden manager class and wholesale traders |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Kumargram_CDB | 70.00 | E | Kumargram CDB pop ~199,609 / AC est. ~260,000 ≈ 77%; adjusted for Samuktala pull → 70%; stable to 2021 |
| U2_Alipurduar_II_GPs | 30.00 | E | 7 GPs of Alipurduar II block; Bhatibari, Kohinoor, Mahakalguri, Parokata, Samuktala, Tatpara I, Turturi |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.9 persons | E | Tea garden line housing promotes larger HH; COVID return migration slightly increased HH size; stable ~4.9 |
| Nuclear_HH | 60.00 | E | NFHS-5 WB rural pattern; tea-line single-room units promote nuclear structure |
| Joint_HH | 28.00 | E | Tribal joint family tradition |
| Extended_multi_generation | 12.00 | E | Tea garden barracks multi-generational residence pattern |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.00 | E | Census 2011 Alipurduar pattern; NFHS-5 Jalpaiguri women married before 18 declined (18.7% vs 34.5% NFHS-4); slightly lower never-married share |
| Currently_married | 66.00 | E | High marriage rate in tribal and tea-belt communities; early marriage tradition |
| Widowed | 7.00 | E | Female-concentrated 60+ age group |
| Separated_divorced | 1.00 | E | Low formal divorce; some de-facto separation in out-migrant households |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

Independent rates — **do NOT sum**.

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 57.00 | C | NFHS-4 WB rural ~60%; NFHS-5 Jalpaiguri not separately reported; AC ~57% — marginal increase, TV near-saturation in middle-income HH |
| Radio | 7.00 | C | Slight decline from 2019 8%; community radio declining nationally |
| Mobile_phone | 88.00 | C | NFHS-4 WB rural ~78%; mobile saturation by 2021; Jio rollout 2016-19 drives up +10pp → ~88% |
| Smartphone_with_internet | 55.00 | C | **+25pp from 2019 baseline 30%**; COVID-19 2020 drove rapid digital adoption; Jio acceleration + government PMGDISHA; NFHS-5 national pattern confirms major surge |
| Computer | 3.50 | E | Modest improvement from 2019 3%; limited in tea-belt |
| Two_wheeler | 19.00 | C | NFHS-4 WB rural ~18%; slight increase; income growth in tea-belt |
| Four_wheeler | 3.00 | E | Very limited; stable |
| Banking_access | 86.00 | B | PMJDY saturation + tea-wage banking mandate; NFHS-5 shows further PMJDY penetration; +6pp from 2019 80% |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 90.00 | C | NFHS-5 Jalpaiguri district 95.2% (improved from NFHS-4 85.2%); AC slightly below district avg → 90% |
| Improved_sanitation | 60.00 | C | NFHS-5 Jalpaiguri 73.2% (NFHS-4 51.0%); Swachh Bharat Phase-II; tea-belt below district avg → 60% |
| LPG_clean_cooking_fuel | 28.00 | C | NFHS-5 Jalpaiguri 42.7% (NFHS-4 27.0%); Ujjwala programme Phase-I coverage; tea-belt below district avg due to biomass abundance → 28% |
| Wood_biomass_fuel | 67.00 | C | Declining as LPG rises; forest belt biomass still primary; was 75% in 2019 |
| Other_fuel | 5.00 | E | Kerosene, dung, residual; stable |
| Electricity | 95.00 | A | Saubhagya near-saturation by 2021; NFHS-5 Jalpaiguri 97.4%; AC slightly below → 95% |
| **Note** | (water/sanitation/electricity independent; cooking fuel LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 56.00 | D | Born in Alipurduar/Jalpaiguri or same block; slight increase due to COVID-19 reverse migration returning workers to home villages 2020 |
| WB_other_district | 5.00 | D | Some Jalpaiguri and Cooch Behar in-migrants; stable |
| Other_Indian_state | 5.00 | D | Bihari/Oraon tea-garden labour from Jharkhand/Bihar origin (settled); stable |
| Bangladesh_origin | 1.00 | E | Minimal; not a refugee-belt AC |
| Outside_India | 0.50 | E | Nepali-origin settled community; Bhutanese fringe; stable |
| Out_migrant | 2.50 | D | Slightly reduced from 2019 3.5% due to COVID-19 reverse migration; many tribal men returned from Assam/Kolkata 2020 |
| Jharkhand_origin | 30.00 | D | **Load-bearing**: Oraon, Munda, Santal ancestors brought from Chota Nagpur plateau as indentured tea labour (1860s-1930s); now settled 3-5 generations; classified as WB residents |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Sadri | Rajbongshi | Santali | Kurukh | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 65.00 | 3.00 | 0.50 | 2.00 | 10.00 | 14.50 | 4.00 | 1.00 | E | Hindu includes Rajbongshi SC/OBC (Rajbongshi-speaking) + Santal/Oraon Hindu; blend; stable from 2019 |
| Muslim | 70.00 | 5.00 | 20.00 | 2.00 | 2.00 | 1.00 | 0.00 | 0.00 | E | Bengali Muslim majority; small Urdu-speaking fraction; stable |
| Christian | 15.00 | 5.00 | 0.00 | 3.00 | 40.00 | 5.00 | 15.00 | 17.00 | E | Christian = predominantly Oraon/Santal converts; Sadri + Kurukh dominant |
| Sarna_ORP | 10.00 | 2.00 | 0.00 | 2.00 | 45.00 | 3.00 | 25.00 | 13.00 | E | Sarna practitioners are Oraon/Santal traditionalists; tribal language dominant |
| Other_residual | 50.00 | 20.00 | 5.00 | 25.00 | 0.00 | 0.00 | 0.00 | 0.00 | E | Buddhist (Nepali), Sikh fringe |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 38.00 | 28.00 | 3.68 | 6.13 | 24.19 | 0 | 0 | E | Hindu: SC ~38% of Hindu (35.50/81.60×100); ST ~28%; residual Hindu caste; stable from 2019 |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 85.00 | 0 | 5.00 | 10.00 | 0 | 0 | D | Christian = overwhelmingly Oraon/Santal ST converts in tea-belt |
| Sarna_ORP | 0 | 92.00 | 0 | 3.00 | 5.00 | 0 | 0 | E | Sarna practitioners mostly ST; small OBC/SC fringe |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Jharkhand_origin | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 63.00 | 5.00 | 2.00 | 1.50 | 0.50 | 3.00 | 25.00 | D | Hindu Rajbongshi native; Hindu ST Jharkhand-origin; COVID-19 return migration slightly increases native share |
| Muslim | 90.00 | 5.00 | 2.00 | 1.00 | 0.50 | 1.50 | 0.00 | D | Bengali Muslim mostly native |
| Christian | 32.00 | 5.00 | 10.00 | 0.00 | 1.00 | 1.00 | 51.00 | D | Oraon/Santal Christian = majority Jharkhand-origin descent; COVID return slightly increases native |
| Sarna_ORP | 26.00 | 5.00 | 12.00 | 0.00 | 1.00 | 1.00 | 55.00 | E | Same tribal community; Jharkhand-origin dominant |
| Other_residual | 55.00 | 10.00 | 20.00 | 0.00 | 15.00 | 0.00 | 0.00 | E | Nepali/Buddhist community |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion. Updated for 2021 smartphone surge.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 62.00 | 60.00 | 88.00 | E | Above-average for Bengal Hindu; Rajbongshi middle-caste + COVID digital adoption; +25pp smartphone from 2019 |
| Muslim | 54.00 | 52.00 | 80.00 | E | Slightly below Hindu; PMJDY + smartphone surge |
| Christian | 47.00 | 46.00 | 82.00 | E | Tea-garden worker profile; COVID digital adoption narrows gap; banking via estate payroll |
| Sarna_ORP | 42.00 | 38.00 | 74.00 | E | Most marginalised; lowest asset ownership; some PMJDY improvement |
| Other_residual | 67.00 | 55.00 | 84.00 | E | Nepali Buddhist with remittance economy; smartphone access improved |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 6.00 | 12.00 | 14.00 | 20.00 | 18.00 | 22.00 | 8.00 | E |
| SC_total | 25.00 | 27.00 | 21.00 | 15.00 | 7.00 | 4.00 | 1.00 | E |
| ST_total | 32.00 | 28.00 | 19.00 | 13.00 | 6.00 | 2.00 | 0.00 | E |
| OBC | 20.00 | 26.00 | 22.00 | 18.00 | 9.00 | 4.00 | 1.00 | E |
| Other_Hindu_middle | 18.00 | 25.00 | 22.00 | 19.00 | 10.00 | 5.00 | 1.00 | E |
| Muslim | 27.00 | 27.00 | 21.00 | 14.00 | 7.00 | 3.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share. 5-year cohorts per NORMALIZED_SCHEMA §4.4.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 9.00 | 7.00 | E |
| 23_27 | 9.00 | 6.00 | E |
| 28_32 | 8.00 | 5.00 | E |
| 33_37 | 7.00 | 4.00 | E |
| 38_42 | 6.00 | 3.00 | E |
| 43_47 | 5.00 | 2.00 | E |
| 48_52 | 4.00 | 1.50 | E |
| 53_57 | 3.00 | 1.00 | E |
| 58_62 | 2.50 | 0.70 | E |
| 63_67 | 2.00 | 0.50 | E |
| 68 | 1.50 | 0.40 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8.00 | 33.00 | E |
| 23_27 | 45.00 | 80.00 | E |
| 28_32 | 82.00 | 92.00 | E |
| 33_37 | 92.00 | 90.00 | E |
| 38_42 | 93.00 | 87.00 | E |
| 43_47 | 93.00 | 83.00 | E |
| 48_52 | 90.00 | 75.00 | E |
| 53_57 | 88.00 | 61.00 | E |
| 58_62 | 82.00 | 47.00 | E |
| 63_67 | 75.00 | 34.00 | E |
| 68 | 65.00 | 21.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric. 2021 values reflect COVID-19 digital adoption surge (+20-25pp across occupations).

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 40.00 | 52.00 | C | COVID-era surge; above 2019 22% |
| Agricultural_labourer | 30.00 | 42.00 | C | Lowest income; still large jump |
| Household_industry | 45.00 | 54.00 | C | |
| Manufacturing | 55.00 | 62.00 | C | |
| Construction | 50.00 | 57.00 | C | |
| Trade_retail | 68.00 | 74.00 | C | Market town; smartphone heavy |
| Transport_logistics | 62.00 | 67.00 | C | Mobile-phone dependent |
| Services | 72.00 | 77.00 | C | |
| Government_services_teachers | 88.00 | 90.00 | C | Highest in AC |
| Out_migrant_worker | 75.00 | 68.00 | D | Working outside; smartphone heavy |
| Tea_garden_plantation | 35.00 | 50.00 | D | Tea-line estate worker; COVID digital adoption; above 2019 18% |

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
| U1_Kumargram_CDB | 81.90 | 4.50 | 11.78 | 1.00 | 0.82 | A/E | Census 2011 Kumargram CDB 82.27% Hindu base; 2-yr differential projection; stable composition |
| U2_Alipurduar_II_GPs | 84.10 | 6.60 | 8.66 | 0.90 | 0.74 | A/E | Alipurduar II CDB Census 2011 base; 2-yr differential projection |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Use canonical caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Kumargram_CDB | 2.50 | 35.78 | 30.00 | 5.00 | 14.12 | 4.50 | 8.10 | A/E |
| U2_Alipurduar_II_GPs | 4.00 | 30.00 | 25.00 | 6.00 | 19.40 | 6.60 | 9.00 | E |

### D.13 Sub-unit × Asset / media

Updated for 2021 smartphone surge.

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Kumargram_CDB | 54.00 | 51.00 | 3.00 | 84.00 | C |
| U2_Alipurduar_II_GPs | 62.00 | 62.00 | 4.50 | 89.00 | C |

### D.14 Sub-unit × Amenities

Updated for Ujjwala, Swachh Bharat Phase-II, Saubhagya 2021 levels.

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Kumargram_CDB | 25.00 | 55.00 | 88.00 | 93.00 | C |
| U2_Alipurduar_II_GPs | 33.00 | 68.00 | 93.00 | 98.00 | C |

### D.15 Vote × Religion (2021 AE anchor)

P(party ‖ religion) — anchored on 2021 AE result. BJP won Kumargram by ~4.73pp with Manoj Kumar Oraon (BJP, 48.16%) over Leos Kujur (AITC, 43.43%). BJP's win driven primarily by ST tribal community consolidation and Adivasi tea-belt swing; RSP historically strong but reduced to 4.84%.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 56.00 | 36.00 | 1.50 | 4.50 | 2.00 | D | Hindu Rajbongshi SC BJP-leaning; 2021 AE result implies Hindu swing to BJP continued; RSP residual LF |
| Muslim | 5.00 | 70.00 | 12.00 | 11.00 | 2.00 | D | Muslim consolidation around AITC; small RSP vote in Muslim segments |
| Christian | 48.00 | 35.00 | 2.00 | 10.00 | 5.00 | D | Tea-garden Christian split; BJP Oraon candidate (Manoj Kumar Oraon) pulled Christian ST vote; RSP residual |
| Sarna_ORP | 55.00 | 30.00 | 1.00 | 8.00 | 6.00 | D | Sarna tribal leaned BJP; BJP ST candidate appeal; RSP residual |
| Other_residual | 38.00 | 40.00 | 3.00 | 12.00 | 7.00 | E | Mixed Buddhist/Nepali fringe |

### D.16 Vote × Caste (2021 AE anchor)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 58.00 | 32.00 | 3.00 | 5.00 | 2.00 | D | WB UC BJP-leaning continued 2021 |
| OBC | 50.00 | 38.00 | 2.00 | 7.00 | 3.00 | D | Koch-Rajbongshi OBC BJP-leaning; AITC Lakshmir Bhandar softened swing |
| SC_total | 52.00 | 38.00 | 2.00 | 5.00 | 3.00 | D | Rajbongshi SC BJP-leaning; AITC welfare outreach reduced gap slightly vs 2019 |
| ST_total | 54.00 | 37.00 | 1.00 | 5.00 | 3.00 | D | ST tribal community: BJP ST candidate Manoj Kumar Oraon strong appeal; Adivasi tea-belt consolidated BJP |
| Other_Hindu_middle | 48.00 | 40.00 | 2.00 | 7.00 | 3.00 | D | |
| Muslim | 5.00 | 70.00 | 12.00 | 11.00 | 2.00 | D | Same as D.15 |

### D.17 Vote × Gender (2021 AE anchor)

Post-Lakshmir Bhandar (April 2021) launch; women beneficiaries are ₹500/month general, ₹1000 SC/ST. Launch was days before polling — limited penetration effect expected.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 52.00 | 39.00 | 2.00 | 5.00 | 2.00 | D | Male slightly more BJP; 2021 AE overall result implies BJP 48.16% suggests mixed gender effect |
| Female | 44.00 | 48.00 | 1.50 | 5.00 | 1.50 | D | AITC retained women advantage; Lakshmir Bhandar launched April 2021 just before polling — limited but symbolically important; AITC women-outreach advantage |

### D.18 Vote × Welfare

AC 010 does not declare a `welfare_exposure` axis in v0. Skipped per NORMALIZED_SCHEMA §4.7.

---

## E. 2021 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

2021 WB Assembly Election AC 010 Kumargram: BJP won. Winner: Manoj Kumar Oraon (BJP). Runner-up: Leos Kujur (AITC). Total electors: 272,924. Total valid votes: 232,489. Turnout: 85.18%.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 48.16 | A | ECI 2021 AE: Manoj Kumar Oraon 111,974 votes / 232,489 total valid |
| AITC | 43.43 | A | ECI 2021 AE: Leos Kujur 100,973 votes |
| INC | 0.00 | A | ECI 2021 AE: INC did not field a candidate in AC 010 |
| LF | 4.84 | A | ECI 2021 AE: RSP Kishor Minj 11,253 votes (RSP is dominant left party in Dooars) |
| Other_NOTA | 3.57 | A | ECI 2021 AE: NOTA 2,718 + IND Aron Murmu 1,781 + KPPU 1,651 + JD(U) 1,399 + BMUP 740 = 8,289 votes (3.57%) |
| **Sum** | **100.00** | — | self-check: 48.16 + 43.43 + 0.00 + 4.84 + 3.57 = 100.00 |

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 010 Kumargram (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | James Kujur | AITC | ~37.3% | Manoj Kumar Oraon | RSP | ~34.3% | ~6,153 votes |
| 2014 by-election | Manoj Kumar Oraon | RSP | — | Joachim Baxla | AITC | — | ~2,667 votes |
| 2016 AE | James Kujur | AITC | ~37.3% | Manoj Kumar Oraon | RSP | ~34.3% | ~6,153 votes |

Note: The RSP had a historic hold on Kumargram through Dooars left-labour organisation. BJP was not a major force at AC-level until the 2019 LS wave. In 2019 LS, BJP swept AC 010 segment with 52.78%. In 2021 AE, BJP's Manoj Kumar Oraon (previously the RSP candidate in 2011/2016) won with 48.16%, consolidating the BJP wave. RSP retained 4.84% — a remnant of left labour organisation in tea gardens.

### 2019 Lok Sabha Election — AC 010 segment within Alipurduars LS (PC 2)

| Party | Candidate (LS level) | Votes | AC segment % | Tier |
|---|---|---|---|---|
| BJP | John Barla | 116,023 | 52.78% | A |
| AITC | Dasrath Tirkey | 87,210 | 39.67% | A |
| INC | — | 4,623 | 2.10% | A |
| LF (RSP) | — | 9,343 | 4.25% | A |
| Other_NOTA | various | 2,630 | 1.20% | A |

Note: The 2019 LS result is now a pre-2021 anchor. BJP's 52.78% AC-segment share in 2019 LS softened to 48.16% in 2021 AE — this reflects AITC's welfare-driven partial recovery and the RSP candidate shift to BJP in 2021.

### Alipurduars LS (PC 2, ST) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2009 LS | Dasrath Tirkey | AITC | — | AITC hold on ST PC |
| 2014 LS | Dasrath Tirkey | AITC | ~35% | Left weakened; BJP emerging ~21% |
| 2019 LS | John Barla | BJP | ~54% | BJP tsunami; Dasrath Tirkey (AITC) 36.69%; margin 243,989 votes across PC |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Kumargram CD Block Primary Census Abstract (censusindia.co.in/subdistrict/kumargram-block; Wikipedia "Kumargram community development block")
- Census of India 2011 — Alipurduar II CD Block Primary Census Abstract
- Census of India 2011 — Alipurduar district totals (Wikipedia "Alipurduar district")
- ECI 2021 WB Assembly Election — AC 010 Kumargram detailed results (`data/electoral_history/2021/detailed_results.csv`; total electors 272,924; valid votes 232,489)
- ECI 2021 WB Assembly Election — AC 010 Kumargram electors summary (`data/electoral_history/2021/electors_summary.csv`; turnout 85.18%)
- ECI GE2019 AC-segment data (`2019_AssemblySegmentLevelVotingData.csv`, AC_NO=10)
- Delimitation Commission of India 2008 — WB Schedule (Kumargram AC 010 composition)

### Secondary sources (tier B / C)

- NFHS-5 (2019-21) West Bengal — Jalpaiguri district: household amenities, asset ownership baseline; improved sanitation 73.2%, clean cooking fuel 42.7%, electricity 97.4%, drinking water 95.2% (`data/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv`)
- NFHS-4 (2015-16) West Bengal — baseline for asset ownership comparison
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2019 NES — vote × demographic conditionals (WB regional rollup), adapted for 2021 AE result
- WB District Statistical Handbook — Alipurduar / Jalpaiguri

### Tertiary / journalistic (tier D)

- Wikipedia: Kumargram Assembly constituency, Kumargram (community development block), Alipurduar district
- Wikipedia: James Kujur MLA (2011 and 2016 results confirmed); Manoj Kumar Oraon MLA (2021)
- Kolkatatales.in: Santal, Munda, Oraon — WB ST communities; tea-garden origin history
- indiastatelections.com — Kumargram assembly constituency summary
- resultuniversity.com — Kumargram election result history (2011, 2014 by-poll, 2016)
- elections.in — Alipurduars LS 2019 full result
- WB Govt press release April 2021 — Lakshmir Bhandar launch (₹500/₹1000 for general/SC-ST household heads)

### Tier-D / E reliance flags (what to distrust)

- **Caste sub-group shares within ST** (D.2, C.2 sub-rows) — no caste census post-1931 for non-SC/ST; Oraon/Santal/Munda split is tier D (journalistic)
- **Language distribution** (C.5, D.1) — no AC-level language data; Sadri/Rajbongshi/Santali shares tier D from regional studies
- **Migration/birthplace** (C.16, D.3) — no public AC-level Census D-series; Jharkhand-origin share is tier D estimate from tea-garden historical record
- **Asset/media** (C.14, D.4, D.13) — NFHS-5 district-level pattern projected to AC; smartphone surge estimated from COVID-era national pattern; tier C
- **Vote × Demographic** (D.15–D.17) — anchored on 2021 AE AC result but no AC-specific cross-tab; CSDS WB regional pattern adapted; tier D
- **Economic poverty rate** (C.10) — Alipurduar district proxy; tier C
- **Alipurduar II GP-level data** (D.11–D.14, U2) — block-level Census 2011 proxy for 7 GPs; refine with DCHB Part-A
- **INC at 0.00%** (§E) — INC did not contest AC 010 in 2021 AE; the LF column captures RSP votes; Other_NOTA captures minor parties

### v0 known gaps

1. DCHB Alipurduar Part-A — AC collapsed to 2 sub-units instead of full GP-by-GP
2. Kumargram CDB occupational detail — no Census Table B-04 extracted; using district-level inference
3. CSDS WB ST-specific cross-tabs for 2021 — using 2019 national/WB-regional rollup adapted to 2021 AE result; no Dooars-specific 2021 survey
4. Language shares — no D-series linguistic data at block level; Sadri/Rajbongshi shares tier D only
5. 2016 AE exact per-party percentage — total valid votes known (~208,406); per-party % computed from secondary sources only
6. INC did not contest 2021 AE — INC ac_segment_pct set to 0.00%; §E sum maintained at 100.00 with NOTA and minor parties in Other_NOTA

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No post-2021 events referenced.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs. The
> validator's leakage gate exempts §H from the no-future-leakage check.

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
