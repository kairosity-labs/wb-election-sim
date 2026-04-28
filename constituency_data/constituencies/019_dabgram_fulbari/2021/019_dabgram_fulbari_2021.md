# AC 019 — Dabgram-Fulbari (GEN) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 019 Dabgram-Fulbari as of end-2021 — after the May 2021 WB
> Assembly Election results were known. It does not reference any post-2021
> events. Use 2024 LS as out-of-sample validation gate for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../../NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 019 | A | ECI / Delimitation Commission 2008 |
| AC name | Dabgram-Fulbari | A | ECI |
| Reservation | GEN (unreserved) | A | Delimitation 2008 |
| District | Jalpaiguri | A | Delimitation 2008 |
| Sub-division | Jalpaiguri Sadar (Siliguri sub-division for SMC wards) | A | WB administrative |
| LS constituency | 03 — Jalpaiguri (SC reserved) | A | Delimitation 2008 |
| LS segments included with AC 019 | AC 19 Dabgram-Fulbari · 20 Maynaguri · 21 Jalpaiguri · 22 Rajganj · 23 Dhupguri · 24 Mal · plus partial Mekliganj from Cooch Behar | A | Delimitation 2008 |
| AC composition | Ward Nos. 31–44 of Siliguri Municipal Corporation (SMC, Jalpaiguri portion) + Dabgram-I GP · Dabgram-II GP · Fulbari-I GP · Fulbari-II GP of Rajganj CD Block | A | Delimitation 2008; Wikipedia |
| Geographic note | Peri-urban fringe of Siliguri city; SMC wards are urban; GPs are transitional semi-rural on the Teesta / Jaldhaka plains | A | — |
| Sub-units used in v0 | **U1: SMC_wards_31_44** (urban, 14 wards) · **U2: Rajganj_GP_rural** (4 GPs of Rajganj block) | E | v0 simplification — see methodology §3 |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~230,000 (SMC wards 31–44 ≈ ~157,000 + 4 GPs of Rajganj block ≈ ~73,000) | E | Census 2011; SMC ward data + Rajganj CD block GP-equal-weight estimate |
| 2021 projected population | ~263,000 | E | 10-yr compound growth ~1.3%/yr from 2011 base (urban area + peri-urban GP growth); Census 2011 extrapolation |
| Sex ratio (2021, F per 1000 M) | ~1,000 | E | NFHS-5 Jalpaiguri district sex ratio 1,038 (tier A); higher than 2011 (953); AC blended estimate ~1,000 accounting for urban male in-migration |
| 2021 estimated electorate (18+) | ~310,354 | A | ECI 2021 AE roll: 310,354 (AC 019, tier A — from detailed_results.csv) |
| Estimated M / F / TG split (2021) | 50.9% M / 49.1% F / <0.05% TG | E | NFHS-5 Jalpaiguri sex ratio 1,038 adjusted for urban male in-migration; ~50.9/49.1 |
| 2021 polling stations (estimated) | ~320 | E | Projected from 2019 estimate ~290; electorate growth ~9%; ~320 |
| 2021 AE turnout | 83.44% | A | ECI 2021 AE: 258,969 valid votes / 310,354 electors; tier A |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 88.00 | E | Siliguri city 91.98% Hindu (Census 2011 A); Rajganj block 79.17% Hindu (A); AC weighted blend ~88.5% in 2019; slight Muslim differential growth +0.5pp over 2yr → ~88.0% by 2021 |
| Muslim | 8.10 | E | 2019 estimate 7.8%; +0.3pp Muslim differential growth 2019-2021; AC blended ~8.1% |
| Christian | 1.40 | E | Stable from 2019; Siliguri 0.94% + Rajganj block 1.06%; tea-belt Christian fringe |
| Sarna_ORP | 1.50 | E | Stable; ST tribal population in Rajganj GP pocket |
| Other_residual | 1.00 | E | Buddhist (Siliguri urban), Sikh, Jain, Nepali fringe; minor uptick from Nepali community growth |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 32.35 | A | Census 2011 Dabgram-Fulbari: 32.35% SC (constituency factbook, tier A); unchanged — no post-2011 census |
| └ Rajbanshi_SC | 27.00 | C | Dominant SC in Jalpaiguri; ~75% of WB SC in North Bengal; forms bulk of SC pool here |
| └ Other_SC | 5.35 | E | Residual SC sub-groups (Bagdi, Namasudra fringe, etc.) |
| **ST_total** | 1.16 | A | Census 2011 Dabgram-Fulbari: 1.16% ST (constituency factbook, tier A) |
| └ Oraon_Munda_other | 1.16 | E | Small tribal pool; mostly in Rajganj GP portion; tea-plantation adjacent |
| UC_bhadralok | 8.00 | E | Brahmin/Kayastha/Baidya; Siliguri urban professional class; higher in SMC wards |
| OBC | 10.00 | E | Kumhar, Teli, Sutradhar in Siliguri trade; ~10% estimate; WB OBC list includes some North Bengal groups |
| Other_Hindu_middle | 36.29 | E | Residual within Hindu (88.0 − 32.35 SC − 1.16 ST − 8 UC − 10 OBC = 36.49 Hindu middle; adjusted for slight Muslim growth) |
| Muslim | 8.10 | E | See C.1 |
| Christian_plus_Sarna_plus_Other | 4.10 | E | Christian 1.4% + Sarna_ORP 1.5% + Other_residual 1.0% + small fringe → ~4.10% |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2021, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.50 | E | Jalpaiguri district age pyramid 2011 + 10yr projection; first-time-voter cohort (2019 2yr older → shifted down); urban growth |
| 23_27 | 13.00 | E | Young adult urban in-migration; 2019 18–22 cohort aged into this bracket |
| 28_32 | 12.50 | E | |
| 33_37 | 11.50 | E | |
| 38_42 | 10.50 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.00 | E | |
| 63_67 | 5.50 | E | |
| 68 | 5.50 | E | 68+ open-ended |
| **Sum** | **100.00** | — | self-check (renormalized from Census 2011 adult cohorts + 10yr shift) |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.94 | E | NFHS-5 Jalpaiguri sex ratio 1,038 → 49.06% F; urban male in-migration moderates to ~50.94/49.05 blended; slight improvement from 2019 51.28/48.72 |
| Female | 49.05 | E | |
| Third_gender | 0.01 | E | Negligible; ~0.01% standard WB estimate |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 62.00 | E | SMC 2011: 60.88% Bengali (A); Rajganj block 81.43% Bengali (A); AC blended weighted estimate; stable from 2019 |
| Hindi | 18.00 | E | SMC 2011: 25.24% Hindi (A); Rajganj 5.09%; blended ~18%; stable given continued North Indian in-migration |
| Urdu | 1.00 | E | Small Muslim Urdu-speaker pocket in Siliguri urban; slight uptick with Muslim growth |
| Other | 3.00 | E | Sadri 1.70% in Rajganj (A); other residual |
| Rajbongshi | 12.00 | E | Rajganj block 2.98% Rajbongshi (A); higher in GP portion; AC-local Rajbanshi SC community; stable |
| Nepali | 3.00 | E | SMC Siliguri 4.66% Nepali (A); diluted in AC portion; stable |
| Bhojpuri | 1.00 | E | SMC fringe; North India in-migrant labour; stable |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 13.00 | E | NFHS-5 Jalpaiguri women literacy 73.6% (A); 2011 literacy 73.25%; improvement to ~87% literate by 2021 → ~13% illiterate |
| Primary | 19.00 | E | Census 2011 Jalpaiguri district education distribution scaled; some shift to higher levels |
| Middle | 20.00 | E | |
| Secondary | 18.00 | E | Stable; mass education system |
| Higher_Secondary | 14.00 | E | Urban Siliguri wards boost HS share; +1pp from 2019 |
| Graduate | 11.00 | E | Professional class in SMC wards; +1pp from 2019 |
| Postgraduate | 5.00 | E | Urban university / college graduates; +1pp from 2019 |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 33.00 | E | Rajganj block main-worker share ~37.6% (Census 2011, A); urban SMC dilution; COVID-19 disruption in 2020-21 → slight dip from 2019 34%; some return to normalcy by end-2021 |
| Marginal_worker | 8.00 | E | Rajganj block marginal share (A); COVID-19 may have added marginal workers; stable estimate |
| Non_worker | 36.00 | E | Housewife + elderly + retired; COVID-19 lockdown pushed some workers to non-worker status temporarily |
| Student | 13.00 | E | Urban 18–22 in education; Siliguri college town fringe; COVID-19 disrupted schooling but enrolment broadly maintained |
| Unemployed | 10.00 | E | Educated unemployment elevated post-COVID; job-aspirant pool enlarged by COVID job losses; +1pp from 2019 |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 8.00 | E | Rajganj block cultivator 10.56% (A); urban wards dilute; stable from 2019 |
| Agricultural_labourer | 10.00 | E | Rajganj block 15.08% (A); urban dilution; stable |
| Household_industry | 4.00 | E | Rajganj block 3.31% (A); COVID-19 disrupted home industry temporarily |
| Manufacturing | 5.00 | E | COVID-19 hit manufacturing; slight dip from 2019 6% |
| Construction | 8.00 | E | Urban construction boom in Siliguri; return migration of labourers after COVID lockdowns |
| Trade_retail | 22.00 | E | Siliguri is major trading hub for North-East India; recovered by end-2021 |
| Transport_logistics | 10.00 | E | Siliguri gateway city; trucking, logistics; recovered after COVID lockdowns |
| Services | 18.00 | E | Urban private services; Siliguri service economy; stable |
| Government_services_teachers | 9.00 | E | Administrative town; government sector + teachers; +1pp from 2019 (some government jobs added) |
| Out_migrant_worker | 6.00 | D | COVID-19 reverse migration 2020; some returned by 2021; estimate stable |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 3.00 | E | Siliguri trade hub has larger employer class than rural WB; stable |
| Employee | 38.00 | E | Govt + organised retail + service employees; urban skew |
| Single_worker | 42.00 | E | Own-account traders, cultivators, transport operators |
| Family_worker | 17.00 | E | Unpaid family labour; higher in GP rural portion |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 21.00 | C | WB state BPL ~23% (2011); urban peri-urban has lower BPL; Rajganj block offsets; COVID-19 may have temporarily increased poverty; ~21% by end-2021 after welfare support (PM-GKAY, etc.) |
| Above_Poverty_Line_low_income | 35.00 | E | |
| Lower_middle | 26.00 | E | Siliguri trade / service class; slight shift up from COVID economic disruption easing |
| Middle | 13.00 | E | Urban middle class in SMC wards |
| Upper_middle_well_off | 5.00 | E | Siliguri affluent trader / professional class |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_SMC_wards_31_44 | 62.00 | E | 14 SMC wards; SMC Jalpaiguri portion ~157k / total AC ~263k; urban dominant share; stable from 2019 |
| U2_Rajganj_GP_rural | 38.00 | E | 4 GPs (Dabgram-I, Dabgram-II, Fulbari-I, Fulbari-II) of Rajganj CD block; rural/semi-rural |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.1 persons | E | Jalpaiguri district 4.3 (2011); urban Siliguri slightly lower; NFHS-5 trend toward smaller HH; ~4.1 by 2021 |
| Nuclear_HH | 73.00 | E | NFHS-5 WB urban pattern; urban AC has higher nuclear share; +1pp from 2019 |
| Joint_HH | 21.00 | E | |
| Extended_multi_generation | 6.00 | E | |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 27.00 | E | Census 2011 Jalpaiguri pattern; large young urban cohort; NFHS-5 age at marriage improving |
| Currently_married | 64.50 | E | Stable from 2019 |
| Widowed | 7.00 | E | Concentrated in 60+, female-skewed; stable |
| Separated_divorced | 1.50 | E | Slightly higher in urban area vs rural WB |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 87.00 | C | NFHS-4 WB urban 89%, rural 60%; saturation approaching; AC blended ~87% by 2021 (+2pp from 2019 85%) |
| Radio | 3.00 | C | Continuing decline; -1pp from 2019 |
| Mobile_phone | 93.00 | C | Near saturation in peri-urban Siliguri; +3pp from 2019 90%; post-COVID lockdown drove adoption |
| Smartphone_with_internet | 80.00 | C | Post-COVID surge + Jio continued penetration; NFHS-5 WB women internet use 48% urban / 14% rural; AC blended +22pp from 2019 58% → ~80% by end-2021 (major shift) |
| Computer | 16.00 | C | NFHS-4 WB urban 27%; AC blended ~16%; +1pp from 2019 |
| Two_wheeler | 42.00 | C | Higher in urban Siliguri; +2pp from 2019 |
| Four_wheeler | 10.00 | C | Stable; Siliguri trader / logistics class |
| Banking_access | 95.00 | B | PMJDY saturation + urban banking infrastructure; NFHS-5 WB women with bank account 76.5% (urban higher); +5pp from 2019 90%; near-saturation in Siliguri urban |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 95.00 | A | NFHS-5 Jalpaiguri district 95.2% (tier A); +3pp from 2019 estimate |
| Improved_sanitation | 73.00 | A | NFHS-5 Jalpaiguri district 73.2% (tier A); +8pp from 2019 80% estimate (reflects Swachh Bharat completion); NOTE: district figure lower than AC estimate; use district A-tier |
| LPG_clean_cooking_fuel | 43.00 | A | NFHS-5 Jalpaiguri clean fuel 42.7% (tier A); below 2019 AC estimate due to district including more rural; SMC wards higher ~70%, GP rural ~22%; district average 43% |
| Wood_biomass_fuel | 53.00 | C | Inverse of LPG; higher in GP rural; estimated from NFHS-5 clean fuel gap |
| Other_fuel | 4.00 | C | Kerosene / dung cake fringe; stable |
| Electricity | 97.00 | A | NFHS-5 Jalpaiguri 97.4% (tier A); Saubhagya saturation |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 54.00 | D | Siliguri is major in-migration destination; native share lower than rural WB; COVID-19 reverse migration (2020) brought some back, partially offset by urban in-migration post-lockdown |
| WB_other_district | 15.00 | D | In-migration from Darjeeling, Cooch Behar, Murshidabad etc. for trade/services; stable |
| Other_Indian_state | 17.00 | D | Bihar / UP / Jharkhand / Rajasthan in-migration; COVID reverse migration reduced this pool temporarily; -1pp from 2019 |
| Bangladesh_origin | 4.00 | D | Smaller than South Bengal border ACs; some Hindu refugee / economic migrant pool; stable |
| Outside_India | 0.50 | E | Nepal-origin (Nepali-speaking ~3%); Bhutan fringe; small |
| Out_migrant | 5.00 | E | COVID-19 reverse migration (2020); some Rajbanshi youth and North Indian labourers returned to home towns, registered here; +2pp from 2019 3% |
| Nepal_Bhutan_origin | 4.50 | D | Siliguri gateway city; Nepali community; stable |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Nepali | Bhojpuri | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 63.00 | 19.50 | 0.00 | 2.50 | 13.00 | 1.50 | 0.50 | E | SMC 2011 Bengali 60.88% / Hindi 25.24% weighted; Rajbanshi SC in Hindu; Nepali fringe; stable from 2019 |
| Muslim | 55.00 | 10.00 | 20.00 | 3.00 | 10.00 | 1.00 | 1.00 | E | Bengali-Muslim majority in Rajganj; Urdu-speaker in Siliguri urban Muslim; stable |
| Christian | 50.00 | 5.00 | 0.00 | 5.00 | 15.00 | 25.00 | 0.00 | E | Mixed: Nepali Christian (Siliguri), Rajbanshi Christian (GP), Bengali |
| Sarna_ORP | 20.00 | 5.00 | 0.00 | 45.00 | 20.00 | 5.00 | 5.00 | E | Tribal: Sadri / Oraon / Munda languages; Rajbongshi adjacent |
| Other_residual | 25.00 | 35.00 | 5.00 | 10.00 | 5.00 | 15.00 | 5.00 | E | Buddhist Nepali + Sikh + Jain in Siliguri; multilingual fringe |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. One row per religion.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 34.50 | 1.10 | 9.00 | 11.00 | 44.40 | 0 | 0 | E | 88.0% Hindu: SC 32.35%÷88.0%×100=36.8% of Hindu; blended with OBC/other-middle estimate; stable from 2019 |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 90 | 0 | 5 | 5 | 0 | 0 | E | Tribal: overwhelmingly ST; small OBC/Hindu fringe |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 52.00 | 15.00 | 19.50 | 5.00 | 5.00 | 3.50 | E | Hindu includes Nepali-origin (Outside_India), Hindi-belt in-migrants; COVID reverse migration partially absorbed |
| Muslim | 72.00 | 12.00 | 8.00 | 6.00 | 0.50 | 1.50 | E | Rajganj block Muslims largely native Bengali-Muslim; smaller in-migration |
| Christian | 55.00 | 15.00 | 5.00 | 2.00 | 20.00 | 3.00 | E | Nepali Christian (Outside_India), some WB-other-district |
| Sarna_ORP | 65.00 | 20.00 | 10.00 | 0.00 | 2.00 | 3.00 | E | Tribal: tea-belt displaced; some from Jharkhand (Other_Indian_state) |
| Other_residual | 30.00 | 10.00 | 35.00 | 0.00 | 20.00 | 5.00 | E | Marwari/Sikh/Jain mostly Other_Indian_state or Outside_India |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion. 2021 updated for smartphone surge.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 89.00 | 83.00 | 97.00 | C | NFHS-5 religion gap pattern; Hindu urban class higher; smartphone +23pp from 2019 |
| Muslim | 78.00 | 65.00 | 87.00 | C | Below-average across assets; Rajganj rural Muslim lower; smartphone +17pp |
| Christian | 84.00 | 72.00 | 92.00 | C | Mixed urban-rural; Nepali Christian urban-leaning; smartphone +17pp |
| Sarna_ORP | 63.00 | 45.00 | 72.00 | E | Tribal: lowest asset ownership; GP rural; smartphone +15pp from 2019 |
| Other_residual | 96.00 | 90.00 | 99.00 | E | Marwari/Jain trader class: highest asset ownership in Siliguri; near-saturation smartphone |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 3.00 | 7.00 | 11.00 | 18.00 | 20.00 | 27.00 | 14.00 | E |
| SC_total | 14.00 | 21.00 | 22.00 | 18.00 | 13.00 | 9.00 | 3.00 | E |
| ST_total | 22.00 | 27.00 | 22.00 | 14.00 | 9.00 | 4.00 | 2.00 | E |
| OBC | 11.00 | 19.00 | 21.00 | 20.00 | 14.00 | 11.00 | 4.00 | E |
| Other_Hindu_middle | 10.00 | 18.00 | 21.00 | 20.00 | 15.00 | 12.00 | 4.00 | E |
| Muslim | 18.00 | 23.00 | 22.00 | 17.00 | 11.00 | 7.00 | 2.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 21.00 | 19.00 | E |
| 23_27 | 23.00 | 18.00 | E |
| 28_32 | 19.00 | 14.00 | E |
| 33_37 | 16.00 | 10.00 | E |
| 38_42 | 14.00 | 8.00 | E |
| 43_47 | 12.00 | 6.00 | E |
| 48_52 | 9.00 | 4.00 | E |
| 53_57 | 7.00 | 3.00 | E |
| 58_62 | 6.00 | 2.00 | E |
| 63_67 | 5.00 | 2.00 | E |
| 68 | 4.00 | 1.50 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 6.00 | 25.00 | E |
| 23_27 | 40.00 | 78.00 | E |
| 28_32 | 79.00 | 91.00 | E |
| 33_37 | 91.00 | 89.00 | E |
| 38_42 | 92.00 | 87.00 | E |
| 43_47 | 91.00 | 83.00 | E |
| 48_52 | 89.00 | 76.00 | E |
| 53_57 | 87.00 | 65.00 | E |
| 58_62 | 84.00 | 52.00 | E |
| 63_67 | 78.00 | 38.00 | E |
| 68 | 68.00 | 28.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — 2021 updated for post-COVID surge.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 50.00 | 76.00 | C | Rural ag baseline; GP pockets; +15pp smartphone from 2019 |
| Agricultural_labourer | 38.00 | 64.00 | C | Lowest income; GP rural; +13pp smartphone |
| Household_industry | 55.00 | 82.00 | C | +15pp smartphone |
| Manufacturing | 67.00 | 88.00 | C | |
| Construction | 62.00 | 82.00 | C | In-migrant labour; smartphone-heavy by 2021 |
| Trade_retail | 90.00 | 95.00 | C | Siliguri trade hub; near-saturation smartphone by 2021 |
| Transport_logistics | 85.00 | 92.00 | C | Logistics / trucking; smartphone for route navigation; +13pp |
| Services | 92.00 | 96.00 | C | Urban private services; near saturation |
| Government_services_teachers | 96.00 | 98.00 | C | Near saturation |
| Out_migrant_worker | 82.00 | 86.00 | D | Remittance earners; smartphone-heavy; +12pp |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 30.00 | 2.00 | E |
| Primary | 35.00 | 4.00 | E |
| Middle | 32.00 | 8.00 | E |
| Secondary | 27.00 | 14.00 | E |
| Higher_Secondary | 23.00 | 18.00 | E |
| Graduate | 29.00 | 20.00 | E |
| Postgraduate | 39.00 | 13.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 019. See NORMALIZED_SCHEMA.md §4.7.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_SMC_wards_31_44 | 91.20 | 5.70 | 0.94 | 0.50 | 1.66 | A | Siliguri city Census 2011 religion (A); minor Muslim growth adjustment; SMC wards approximate city average |
| U2_Rajganj_GP_rural | 78.50 | 19.90 | 1.06 | 0.42 | 0.12 | A | Rajganj CD block Census 2011 religion (A); minor Muslim growth adjustment |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit).

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_SMC_wards_31_44 | 10.00 | 26.00 | 0.70 | 12.00 | 43.60 | 5.70 | 2.00 | E |
| U2_Rajganj_GP_rural | 4.00 | 49.56 | 4.12 | 5.00 | 17.40 | 19.90 | 0.02 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_SMC_wards_31_44 | 94.00 | 90.00 | 23.00 | 98.00 | C |
| U2_Rajganj_GP_rural | 75.00 | 58.00 | 7.00 | 88.00 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_SMC_wards_31_44 | 65.00 | 88.00 | 98.00 | 99.00 | C |
| U2_Rajganj_GP_rural | 22.00 | 52.00 | 90.00 | 96.00 | C |

### D.15 Vote × Religion (2021 AE, regional anchor)

P(party ‖ religion) — anchored on 2021 AE AC 019 result (BJP 49.85%, AITC 39.19%, LF 7.16%, Other_NOTA 3.80%, INC 0%).

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 57.00 | 33.00 | 1.00 | 6.00 | 3.00 | C | Anchored on 2021 AE result; BJP consolidated in Hindu but AITC recovered vs 2019 LS (-6pp BJP shift); Rajbanshi SC BJP loyalty remained high; Siliguri urban BJP reduced |
| Muslim | 4.00 | 74.00 | 10.00 | 9.00 | 3.00 | C | AITC gained Muslim vote back in 2021; LF held residual support; INC nominal |
| Christian | 25.00 | 52.00 | 5.00 | 13.00 | 5.00 | E | Mixed; AITC gained from BJP in 2021 WB |
| Sarna_ORP | 38.00 | 38.00 | 3.00 | 16.00 | 5.00 | E | Tribal: split; BJP still ahead but AITC gained in 2021 |
| Other_residual | 55.00 | 28.00 | 4.00 | 6.00 | 7.00 | E | Marwari/Jain/Sikh urban: BJP-leaning nationally but some AITC switch in 2021 |

### D.16 Vote × Caste (2021 AE)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 57.00 | 31.00 | 4.00 | 5.00 | 3.00 | C | CSDS 2021 WB UC BJP-leaning; some AITC recovery; anchored on 2021 AE AC 019 result |
| OBC | 48.00 | 35.00 | 3.00 | 10.00 | 4.00 | C | Mixed; OBC BJP mobilization partly held |
| SC_total | 60.00 | 32.00 | 1.00 | 5.00 | 2.00 | C | Rajbanshi SC: strong BJP; reduced slightly from 2019 LS (70%); AITC welfare appeal |
| ST_total | 42.00 | 35.00 | 3.00 | 15.00 | 5.00 | C | Tribal: BJP still ahead; AITC recovery; LF has historical tribal support |
| Other_Hindu_middle | 55.00 | 33.00 | 2.00 | 7.00 | 3.00 | E | North Bengal Hindu middle: BJP still dominant but AITC improved |
| Muslim | 4.00 | 74.00 | 10.00 | 9.00 | 3.00 | C | Same as D.15 Muslim |

### D.17 Vote × Gender (2021 AE)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 54.00 | 34.00 | 2.00 | 7.00 | 3.00 | C | 2021 WB male vote; BJP still ahead; AITC recovered vs 2019 LS |
| Female | 46.00 | 44.00 | 1.00 | 7.00 | 2.00 | C | AITC Lakshmir Bhandar (Apr 2021) boosted women vote; gender gap toward AITC wider in 2021 |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for AC 019. See NORMALIZED_SCHEMA.md §4.7.)

---

## E. 2021 baseline vote (calibration target)

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 49.85 | A | ECI 2021 AE: Sikha Chatterjee 129,088 votes / 258,969 total valid = 49.85% |
| AITC | 39.19 | A | Goutam Deb 101,495 votes / 258,969 = 39.19% |
| INC | 0.00 | A | INC did not contest AC 019 in 2021 AE |
| LF | 7.16 | A | CPI(M) 17,998 + SUCI 547 = 18,545 / 258,969 = 7.16% |
| Other_NOTA | 3.80 | A | NOTA 3,379 + BSP 1,395 + IND 1,391 + IND 1,093 + IND 1,052 + RPI(A) 881 + AMB 650 = 9,841 / 258,969 = 3.80%; sum check: 49.85+39.19+0.00+7.16+3.80=100.00 |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 019 Dabgram-Fulbari (Assembly Elections prior to 2021)

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin |
|---|---|---|---|---|---|---|---|---|---|
| 2011 AE | Goutam Deb | AITC | ~105,000 | ~50% | Dilip Singh | CPI(M) | ~80,000 | ~38% | ~25,000 |
| 2016 AE | Goutam Deb | AITC | 105,769 | 47.49% | Dilip Singh | CPI(M) | 81,958 | 36.80% | 23,811 |

Note: Goutam Deb was Mayor of Siliguri and a senior AITC leader. He won both 2011 and 2016 from this seat. In 2016, BJP polled only 26,195 (11.76%) — a distant third. CPI(M) remained the main opposition until the BJP surge in 2019 LS and 2021 AE. LF (CPI(M)+SUCI) in 2016: 82,975 votes = 37.25%.

### 2019 LS — AC 019 segment within Jalpaiguri LS (PC 03) (anchor, no longer calibration target)

| Party | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|
| BJP | 150,566 | 63.42% | A | ECI 2019 LS Form-20 AC-segment data; 237,413 total valid |
| AITC | 64,449 | 27.15% | A | |
| CPI(M) | 13,408 | 5.65% | A | |
| INC | 4,300 | 1.81% | A | |
| Other_NOTA | 4,690 | 1.97% | A | BSP+AMB+SWJP+KPPU+SUCI+IND |
| **Electors** | 283,995 | — | A | ECI 2019 LS roll |

Context: The 2019 BJP wave in Jalpaiguri LS (BJP 63.4% at AC 019) reflects Rajbanshi SC mobilization, anti-AITC incumbency, and the North Bengal nationalist surge. AITC's recovery to 39.2% in 2021 AE (from 27.2% in 2019 LS) was driven by: Lakshmir Bhandar, Duare Sarkar welfare delivery, AITC's "Banglar Meye" Mamata Banerjee campaign, and COVID-19 welfare response.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Jalpaiguri district religion, SC/ST data (census2011.co.in)
- Census of India 2011 — Rajganj CD block: population, religion, workers, language (censusindia.co.in)
- Census of India 2011 — Siliguri Municipal Corporation: population, religion, mother tongue (census2011.co.in)
- Election Commission of India — `data/electoral_history/2021/detailed_results.csv`: AC 019 vote breakdown (tier A; 258,969 valid votes, 310,354 electors; BJP 49.85%, AITC 39.19%)
- Election Commission of India — `data/2019_AssemblySegmentLevelVotingData.csv`: AC 019 2019 LS segment (tier A; 237,413 valid votes, 283,995 electors; BJP 63.42%)
- NFHS-5 (2019-21) Jalpaiguri district — electricity 97.4%, drinking water 95.2%, sanitation 73.2%, clean fuel 42.7% (tier A)
- Delimitation Commission of India 2008 — WB Schedule: AC 019 = SMC wards 31–44 + 4 GPs of Rajganj block
- Wikipedia: Dabgram-Phulbari Assembly constituency — composition, reservation status, 2016 AE result

### Secondary sources (tier B / C)

- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership (urban/rural split); updated by NFHS-5 for 2021
- NFHS-5 (2019-21) West Bengal state — women internet use 48.1% urban, mobile phone 71.9% urban (tier C)
- CSDS-Lokniti 2021 WB post-poll cross-tabs (vote × religion / caste / gender; state-level WB rollup)
- WB District Statistical Handbook — Jalpaiguri
- Indiastatpublications.com — Dabgram-Fulbari Assembly Factbook (SC/ST %, electorate)
- PMJDY enrollment data — banking access baseline

### Tertiary / journalistic (tier D)

- Wikipedia: Rajganj (community development block) — language, workers, religion data
- The Print / NDTV: "Who won 2021 WB election" — TMC 213 seats, BJP 77 seats
- Bold News / Millennium Post: Goutam Deb political biography (Siliguri mayor, 2011/2016/2021 candidate)
- Lakshmir Bhandar scheme details — WB CDWDSW press releases, April 2021 launch; ₹500/month GEN, ₹1000/month SC/ST women household heads
- BSF 50km jurisdiction order — MHA October 2021 gazette notification

### Tier-D / E reliance flags (what to distrust)

- **Sub-unit population split** (C.11): SMC wards 31–44 vs Rajganj GP split is a rough estimate; ward-level Census data not disaggregated; tier E
- **Caste shares** (C.2, D.2, D.12): No post-1931 caste census; Rajbanshi SC dominant but sub-group shares are tier E
- **Migration/birthplace** (C.16, D.3): No AC-level Census D-series; tier D from city-level inference; COVID return migration is qualitative
- **Language splits** (C.5, D.1): SMC all-ward data used; ward 31–44 subset not separately available
- **Vote × demographic conditionals** (D.15–D.17): CSDS 2021 WB state rollup; adjusted for North Bengal BJP dominance and AITC 2021 recovery; tier C
- **Smartphone penetration** (C.14, D.4, D.8, D.13): Post-COVID surge is large (+22pp) and rapid; NFHS-5 (2019-21) provides district-level baseline but AC-level urban-rural split is modeled; tier C
- **Clean cooking fuel** (C.15): NFHS-5 Jalpaiguri 42.7% includes more rural areas than AC; AC estimate uses district figure as anchor

### v0 known gaps (cross-reference methodology §7)

1. **Sub-unit population data**: SMC wards 31–44 subset Census not separately published; v0 uses whole-SMC proxy
2. **NFHS-5 AC-level assets**: Only district-level NFHS-5 available; urban-rural blend within AC is tier E modeled
3. **2021 AE exit poll / voter survey**: No published CSDS AC-level cross-tab for Dabgram-Fulbari; D.15-D.17 use state-rollup adjusted for North Bengal
4. **Lakshmir Bhandar penetration**: No AC-level enrollment data for 2021; scheme was just launched (Apr 2021); D.17 female gender gap partially attributed to LB but is tier E
5. **Migration post-COVID**: COVID-19 reverse migration (2020) and re-migration (2021) estimates are tier D; no survey data

---

*v0 — generated 2026-04-28, frozen at 2021 state-of-knowledge. No post-2021 events referenced.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs. The
> validator's leakage gate exempts §H from the no-future-leakage check.

### 2024 Lok Sabha Election — AC 019 segment within Jalpaiguri LS (PC 03) (tier A, CSV)

Figures from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=19, Dabgram-Fulbari. Total valid votes: 256,373; electorate: 321,201; turnout ~79.8%.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Dr. Jayanta Kumar Roy | 156,023 | **60.86%** | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Nirmal Chandra Roy | 83,778 | **32.68%** | A | Same |
| CPI(M) | Debraj Barman | 11,486 | **4.48%** | A | Same |
| BSP | — | 1,104 | **0.43%** | A | Same |
| Others (IND, KPPU, MPOI, SUCI) | various | 3,982 | **1.55%** | A | Same |
| **BJP margin over AITC** | | **72,245 votes** | **28.18 pp** | A | Computed |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC segment shares within ±3pp of the tier-A figures, starting from the 2021 calibration:
- BJP target: 60.9% ± 3pp
- AITC target: 32.7% ± 3pp
- LF (CPI(M)) target: 4.5% ± 3pp

Note: The 2024 BJP recovery (+10.7pp from 2021 AE 49.85%) represents a significant shift. Key narrative shocks between 2021→2024 are out-of-sample inputs to the simulator, not baked into this file.
