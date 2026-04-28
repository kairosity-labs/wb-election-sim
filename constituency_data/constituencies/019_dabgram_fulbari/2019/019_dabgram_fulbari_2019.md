# AC 019 — Dabgram-Fulbari (GEN) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 019 Dabgram-Fulbari as of 2019 only — it does not reference
> any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../../NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 019 | A | ECI / Delimitation Commission 2008 |
| AC name | Dabgram-Fulbari | A | ECI |
| Reservation | GEN (unreserved) | A | Delimitation 2008 |
| District | Jalpaiguri | A | Delimitation 2008 |
| Sub-division | Jalpaiguri Sadar (Siliguri sub-division for SMC wards) | A | WB administrative |
| LS constituency | 03 — Jalpaiguri (SC reserved) | A | Delimitation 2008 |
| LS segments included with AC 019 | AC 14 Mekliganj · 15 Mathabhanga · 16 Sitai · 17 Sitalkuchi · 18 Tufanganj · 19 Dabgram-Fulbari · 20 Dhupguri · (partial Cooch Behar) — or Jalpaiguri LS: AC 19 Dabgram-Fulbari · 20 Maynaguri · 21 Jalpaiguri · 22 Rajganj · 23 Dhupguri · 24 Mal · plus Mekliganj from Cooch Behar | A | Delimitation 2008 |
| AC composition | Ward Nos. 31–44 of Siliguri Municipal Corporation (SMC, Jalpaiguri portion) + Dabgram-I GP · Dabgram-II GP · Fulbari-I GP · Fulbari-II GP of Rajganj CD Block | A | Delimitation 2008; Wikipedia |
| Geographic note | Peri-urban fringe of Siliguri city; SMC wards are urban; GPs are transitional semi-rural on the Teesta / Jaldhaka plains | A | — |
| Sub-units used in v0 | **U1: SMC_wards_31_44** (urban, 14 wards) · **U2: Rajganj_GP_rural** (4 GPs of Rajganj block) | E | v0 simplification — see methodology §3 |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~230,000 (SMC wards 31–44 ≈ ~157,000 + 4 GPs of Rajganj block ≈ ~73,000) | E | Census 2011; SMC ward data + Rajganj CD block GP-equal-weight estimate |
| 2019 projected population | ~252,000 | E | 8-yr compound growth ~1.3%/yr (urban area + peri-urban GP growth) |
| Sex ratio (2019, F per 1000 M) | ~950 | E | Jalpaiguri district 953 (Census 2011, A); SMC ~938; blended estimate |
| 2019 estimated electorate (18+) | ~284,000 | A | ECI 2019 LS roll: 283,995 (AC 019 segment, tier A) |
| Estimated M / F / TG split (2019) | 51.3% M / 48.7% F / <0.05% TG | E | District sex ratio back-projection |
| 2019 polling stations (estimated) | ~290 | E | Back-projection from electorate size; Rajganj block density |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 88.50 | E | Siliguri city 91.98% Hindu (Census 2011 A); Rajganj block 79.17% Hindu (A); AC weighted blend ~88.5%; Hindu growth +0.8%/yr 2011-19 |
| Muslim | 7.80 | E | Siliguri 5.37% + Rajganj block 19.35%; AC blended ~7.8%; Muslim growth +1.1%/yr |
| Christian | 1.40 | E | Siliguri 0.94% + Rajganj block 1.06%; AC ~1.4% incl. tea-belt Christian fringe |
| Sarna_ORP | 1.50 | E | ST tribal population in Rajganj GP pocket; tea-plantation proximate |
| Other_residual | 0.80 | E | Buddhist (Siliguri urban), Sikh, Jain, Nepali fringe; Siliguri 0.65% Buddhist + others |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 32.35 | A | Census 2011 Dabgram-Fulbari estimate — 32.35% SC (constituency factbook, tier A) |
| └ Rajbanshi_SC | 27.00 | C | Dominant SC in Jalpaiguri; Rajbanshi ~75% of WB SC in North Bengal; forms bulk of SC pool here |
| └ Other_SC | 5.35 | E | Residual SC sub-groups (Bagdi, Namasudra fringe, etc.) |
| **ST_total** | 1.16 | A | Census 2011 Dabgram-Fulbari: 1.16% ST (constituency factbook, tier A) |
| └ Oraon_Munda_other | 1.16 | E | Small tribal pool; mostly in Rajganj GP portion; tea-plantation adjacent |
| UC_bhadralok | 8.00 | E | Brahmin/Kayastha/Baidya; Siliguri urban professional class; higher in SMC wards |
| OBC | 10.00 | E | Rajbanshi OBC classification in some states — but WB classifies Rajbanshi as SC; other OBCs (Kumhar, Teli, Sutradhar) present in Siliguri trade; ~10% estimate |
| Other_Hindu_middle | 36.49 | E | Residual within Hindu (88.5 − 32.35 SC − 1.16 ST − 8 UC − 10 OBC = 37% Hindu middle; minus ~0.5 non-Hindu portion) |
| Muslim | 7.80 | E | See C.1 |
| Christian_plus_Sarna_plus_Other | 4.20 | E | Christian 1.4% + Sarna_ORP 1.5% + Other_residual 0.8% + small fringe = 3.7% → ~4.20% rounded to align |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.00 | E | Jalpaiguri district age pyramid 2011 + projection; large first-time-voter cohort (urban growth) |
| 23_27 | 13.00 | E | Young adult urban in-migration |
| 28_32 | 12.50 | E | |
| 33_37 | 11.50 | E | |
| 38_42 | 10.00 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.00 | E | |
| 63_67 | 5.50 | E | |
| 68 | 5.50 | E | 68+ open-ended |
| **Sum** | **100.00** | — | self-check (renormalized from Census 2011 adult cohorts) |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.28 | E | Jalpaiguri district sex ratio 953 F/1000 M → 51.28% M / 48.72% F; projected stable to 2019 |
| Female | 48.71 | E | |
| Third_gender | 0.01 | E | Negligible; ~0.01% standard WB estimate |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 62.00 | E | SMC 2011: 60.88% Bengali (A); Rajganj block 81.43% Bengali (A); AC blended weighted estimate |
| Hindi | 18.00 | E | SMC 2011: 25.24% Hindi (A); Rajganj 5.09%; blended ~18% |
| Urdu | 1.00 | E | Small Muslim Urdu-speaker pocket in Siliguri urban |
| Other | 3.00 | E | Sadri 1.70% in Rajganj (A); other residual |
| Rajbongshi | 12.00 | E | Rajganj block 2.98% Rajbongshi (A); higher in GP portion; AC-local Rajbanshi SC community |
| Nepali | 3.00 | E | SMC Siliguri 4.66% Nepali (A); diluted in AC portion |
| Bhojpuri | 1.00 | E | SMC fringe; North India in-migrant labour |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 15.00 | E | Jalpaiguri literacy 73.25% (2011, A); urban Siliguri higher; AC peri-urban estimate ~15% illiterate by 2019 |
| Primary | 20.00 | E | Census 2011 Jalpaiguri district education distribution scaled |
| Middle | 20.00 | E | |
| Secondary | 18.00 | E | |
| Higher_Secondary | 13.00 | E | Urban Siliguri wards boost HS share |
| Graduate | 10.00 | E | Professional class in SMC wards |
| Postgraduate | 4.00 | E | Urban university / college graduates |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 34.00 | E | Rajganj block main-worker share ~37.6% (Census 2011, A); urban SMC dilution of ag workers; AC ~34% |
| Marginal_worker | 8.00 | E | Rajganj block 20.2% marginal share within workers (A); scaled to AC with urban offset |
| Non_worker | 36.00 | E | Housewife + elderly + retired; high in urban HH |
| Student | 13.00 | E | Urban 18–22 in education; Siliguri college town fringe |
| Unemployed | 9.00 | E | Educated unemployment salience in urban peri-urban; job-aspirant pool |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 8.00 | E | Rajganj block cultivator 10.56% (A); urban wards dilute → AC ~8% |
| Agricultural_labourer | 10.00 | E | Rajganj block 15.08% (A); urban dilution |
| Household_industry | 4.00 | E | Rajganj block 3.31% (A); some urban small enterprise |
| Manufacturing | 6.00 | E | Small manufacturing in Siliguri fringe |
| Construction | 8.00 | E | Urban construction boom in Siliguri; in-migrant labour |
| Trade_retail | 22.00 | E | Siliguri is major trading hub for North-East India; high trade/retail share |
| Transport_logistics | 10.00 | E | Siliguri is gateway city; trucking, logistics, freight; elevated transport share |
| Services | 18.00 | E | Urban private services; Siliguri service economy |
| Government_services_teachers | 8.00 | E | Administrative town; government sector significant |
| Out_migrant_worker | 6.00 | D | Some Rajbanshi men to Assam/Bhutan tea estates or other states |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 3.00 | E | Siliguri trade hub has larger employer class than rural WB |
| Employee | 38.00 | E | Govt + organised retail + service employees; urban skew |
| Single_worker | 42.00 | E | Own-account traders, cultivators, transport operators |
| Family_worker | 17.00 | E | Unpaid family labour; higher in GP rural portion |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 22.00 | C | WB state BPL ~23% (2011); urban peri-urban has lower BPL than deep rural; Rajganj block offsets; ~22% estimate |
| Above_Poverty_Line_low_income | 35.00 | E | |
| Lower_middle | 25.00 | E | Siliguri trade / service class |
| Middle | 13.00 | E | Urban middle class in SMC wards |
| Upper_middle_well_off | 5.00 | E | Siliguri affluent trader / professional class; higher than typical WB AC |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_SMC_wards_31_44 | 62.00 | E | 14 SMC wards; SMC Jalpaiguri portion ~157k / total AC ~253k; urban dominant share |
| U2_Rajganj_GP_rural | 38.00 | E | 4 GPs (Dabgram-I, Dabgram-II, Fulbari-I, Fulbari-II) of Rajganj CD block; rural/semi-rural |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.2 persons | E | Jalpaiguri district 4.3 (2011); urban Siliguri slightly lower; ~4.2 |
| Nuclear_HH | 72.00 | E | NFHS-4 WB urban pattern; urban AC has higher nuclear share |
| Joint_HH | 22.00 | E | |
| Extended_multi_generation | 6.00 | E | |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 27.00 | E | Census 2011 Jalpaiguri pattern; large young urban cohort |
| Currently_married | 64.50 | E | |
| Widowed | 7.00 | E | Concentrated in 60+, female-skewed |
| Separated_divorced | 1.50 | E | Slightly higher in urban area vs rural WB |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 85.00 | C | NFHS-4 WB urban 89%, rural 60%; AC blended peri-urban ~85%; +projection to 2019 |
| Radio | 4.00 | C | Declining nationally; urban lower |
| Mobile_phone | 90.00 | C | High urban penetration; Siliguri telecom hub; ~90% by 2019 |
| Smartphone_with_internet | 58.00 | C | NFHS-4 baseline + Jio rollout 2016-19; urban Siliguri higher than rural WB |
| Computer | 15.00 | C | NFHS-4 WB urban 27%; AC blended ~15% |
| Two_wheeler | 40.00 | C | Higher in urban Siliguri; transport / trade economy |
| Four_wheeler | 10.00 | C | Siliguri trader / logistics class; above-average four-wheeler |
| Banking_access | 90.00 | B | PMJDY saturation + urban banking infrastructure; high in Siliguri |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 92.00 | C | NFHS-4 WB urban 93%; Rajganj GP lower; AC ~92% |
| Improved_sanitation | 80.00 | C | NFHS-4 WB urban 84%; Rajganj rural lower 51%; blended ~80% |
| LPG_clean_cooking_fuel | 60.00 | C | NFHS-4 WB urban 81%; GP rural 24%; blended ~60%; Ujjwala 2016-19 boost |
| Wood_biomass_fuel | 36.00 | C | Declining as LPG rises; higher in GP rural portion |
| Other_fuel | 4.00 | C | Kerosene / dung cake fringe |
| Electricity | 98.00 | A | Census 2011 + Saubhagya 2017-19 saturation; SMC wards near 100% |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 55.00 | D | Siliguri is major in-migration destination; native share lower than rural WB |
| WB_other_district | 15.00 | D | In-migration from Darjeeling, Cooch Behar, Murshidabad etc. for trade/services |
| Other_Indian_state | 18.00 | D | Significant Bihar / UP / Jharkhand / Rajasthan in-migration; Siliguri Hindi-speaker 25% |
| Bangladesh_origin | 4.00 | D | Smaller than South Bengal border ACs; some Hindu refugee / economic migrant pool |
| Outside_India | 0.50 | E | Nepal-origin (Nepali-speaking 3%); Bhutan fringe; small |
| Out_migrant | 3.00 | E | Some Rajbanshi youth to Assam tea belt / other states; registered here |
| Nepal_Bhutan_origin | 4.50 | D | Siliguri is gateway city; Nepali community 3% SMC mother tongue; includes Bhutan-origin residents |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Nepali | Bhojpuri | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 63.00 | 19.50 | 0.00 | 2.50 | 13.00 | 1.50 | 0.50 | E | SMC 2011 Bengali 60.88% / Hindi 25.24% weighted; Rajbanshi SC in Hindu; Nepali fringe |
| Muslim | 55.00 | 10.00 | 20.00 | 3.00 | 10.00 | 1.00 | 1.00 | E | Bengali-Muslim majority in Rajganj; Urdu-speaker in Siliguri urban Muslim |
| Christian | 50.00 | 5.00 | 0.00 | 5.00 | 15.00 | 25.00 | 0.00 | E | Mixed: Nepali Christian (Siliguri), Rajbanshi Christian (GP), Bengali |
| Sarna_ORP | 20.00 | 5.00 | 0.00 | 45.00 | 20.00 | 5.00 | 5.00 | E | Tribal: Sadri / Oraon / Munda languages; Rajbongshi adjacent |
| Other_residual | 25.00 | 35.00 | 5.00 | 10.00 | 5.00 | 15.00 | 5.00 | E | Buddhist Nepali + Sikh + Jain in Siliguri; multilingual fringe |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. One row per religion.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 34.50 | 1.10 | 9.00 | 11.00 | 44.40 | 0 | 0 | E | 88.5% Hindu: SC 32.35%÷88.5%×100=36.6% of Hindu; blended with OBC/other-middle estimate |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 90 | 0 | 5 | 5 | 0 | 0 | E | Tribal: overwhelmingly ST; small OBC/Hindu fringe |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 52.00 | 15.00 | 19.50 | 5.00 | 5.00 | 3.50 | E | Hindu includes Nepali-origin (Outside_India), Hindi-belt in-migrants |
| Muslim | 72.00 | 12.00 | 8.00 | 6.00 | 0.50 | 1.50 | E | Rajganj block Muslims largely native Bengali-Muslim; smaller in-migration |
| Christian | 55.00 | 15.00 | 5.00 | 2.00 | 20.00 | 3.00 | E | Nepali Christian (Outside_India), some WB-other-district |
| Sarna_ORP | 65.00 | 20.00 | 10.00 | 0.00 | 2.00 | 3.00 | E | Tribal: tea-belt displaced; some from Jharkhand (Other_Indian_state) |
| Other_residual | 30.00 | 10.00 | 35.00 | 0.00 | 20.00 | 5.00 | E | Marwari/Sikh/Jain mostly Other_Indian_state or Outside_India |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 87.00 | 60.00 | 92.00 | C | NFHS-4 WB religion-gap pattern; Hindu urban class higher |
| Muslim | 76.00 | 48.00 | 80.00 | C | Below-average across assets; Rajganj rural Muslim lower |
| Christian | 82.00 | 55.00 | 88.00 | C | Mixed urban-rural; Nepali Christian urban-leaning |
| Sarna_ORP | 60.00 | 30.00 | 65.00 | E | Tribal: lowest asset ownership; GP rural |
| Other_residual | 95.00 | 78.00 | 97.00 | E | Marwari/Jain trader class: highest asset ownership in Siliguri |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4.00 | 8.00 | 12.00 | 18.00 | 20.00 | 26.00 | 12.00 | E |
| SC_total | 16.00 | 22.00 | 22.00 | 18.00 | 12.00 | 8.00 | 2.00 | E |
| ST_total | 24.00 | 28.00 | 22.00 | 14.00 | 8.00 | 3.00 | 1.00 | E |
| OBC | 13.00 | 20.00 | 22.00 | 20.00 | 13.00 | 10.00 | 2.00 | E |
| Other_Hindu_middle | 12.00 | 19.00 | 21.00 | 20.00 | 14.00 | 11.00 | 3.00 | E |
| Muslim | 20.00 | 24.00 | 22.00 | 17.00 | 10.00 | 6.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 20.00 | 18.00 | E |
| 23_27 | 22.00 | 17.00 | E |
| 28_32 | 18.00 | 13.00 | E |
| 33_37 | 15.00 | 9.00 | E |
| 38_42 | 13.00 | 7.00 | E |
| 43_47 | 11.00 | 5.00 | E |
| 48_52 | 9.00 | 4.00 | E |
| 53_57 | 7.00 | 3.00 | E |
| 58_62 | 6.00 | 2.00 | E |
| 63_67 | 5.00 | 2.00 | E |
| 68 | 4.00 | 1.50 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 6.00 | 28.00 | E |
| 23_27 | 40.00 | 80.00 | E |
| 28_32 | 78.00 | 91.00 | E |
| 33_37 | 91.00 | 89.00 | E |
| 38_42 | 92.00 | 87.00 | E |
| 43_47 | 91.00 | 83.00 | E |
| 48_52 | 89.00 | 76.00 | E |
| 53_57 | 87.00 | 65.00 | E |
| 58_62 | 84.00 | 52.00 | E |
| 63_67 | 78.00 | 38.00 | E |
| 68 | 68.00 | 28.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 35.00 | 72.00 | C | Rural ag baseline; GP pockets |
| Agricultural_labourer | 25.00 | 60.00 | C | Lowest income; GP rural |
| Household_industry | 40.00 | 78.00 | C | |
| Manufacturing | 52.00 | 85.00 | C | |
| Construction | 48.00 | 78.00 | C | In-migrant labour: lower smartphone |
| Trade_retail | 78.00 | 92.00 | C | Siliguri trade hub; high smartphone access |
| Transport_logistics | 72.00 | 88.00 | C | Logistics / trucking; smartphone for route navigation |
| Services | 80.00 | 93.00 | C | Urban private services |
| Government_services_teachers | 88.00 | 96.00 | C | Highest |
| Out_migrant_worker | 70.00 | 82.00 | D | Remittance earners; smartphone-heavy |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 30.00 | 2.00 | E |
| Primary | 36.00 | 4.00 | E |
| Middle | 33.00 | 7.00 | E |
| Secondary | 28.00 | 12.00 | E |
| Higher_Secondary | 24.00 | 16.00 | E |
| Graduate | 30.00 | 18.00 | E |
| Postgraduate | 40.00 | 12.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 019. See NORMALIZED_SCHEMA.md §4.7.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_SMC_wards_31_44 | 91.98 | 5.37 | 0.94 | 0.50 | 1.21 | A | Siliguri city Census 2011 religion (A); SMC wards approximate city average |
| U2_Rajganj_GP_rural | 79.17 | 19.35 | 1.06 | 0.42 | 0.00 | A | Rajganj CD block Census 2011 religion (A) |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit).

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_SMC_wards_31_44 | 10.00 | 26.00 | 0.70 | 12.00 | 43.93 | 5.37 | 2.00 | E |
| U2_Rajganj_GP_rural | 4.00 | 45.00 | 2.00 | 7.00 | 24.35 | 19.35 | -1.70 | E |

> Note: U2 sub-unit row is modeled. SC_total = 49.56% (Rajganj block, A) adjusted for GP subset; Muslim 19.35%.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_SMC_wards_31_44 | 10.00 | 26.00 | 0.70 | 12.00 | 43.93 | 5.37 | 2.00 | E |
| U2_Rajganj_GP_rural | 4.00 | 49.56 | 4.12 | 5.00 | 17.97 | 19.35 | 0.00 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_SMC_wards_31_44 | 92.00 | 70.00 | 22.00 | 95.00 | C |
| U2_Rajganj_GP_rural | 72.00 | 38.00 | 6.00 | 80.00 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_SMC_wards_31_44 | 78.00 | 92.00 | 96.00 | 99.00 | C |
| U2_Rajganj_GP_rural | 28.00 | 58.00 | 84.00 | 95.00 | C |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 WB rollup adjusted for North Bengal BJP dominance.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 72.00 | 18.00 | 2.00 | 5.00 | 3.00 | C | CSDS 2019 WB Hindu BJP 57% (state); North Bengal BJP boost: +15pp adjustment for Rajbanshi / Siliguri urban BJP surge; AC overall 63% BJP |
| Muslim | 5.00 | 68.00 | 16.00 | 9.00 | 2.00 | C | CSDS 2019 WB Muslim; LF slightly higher in North Bengal Muslim belt |
| Christian | 30.00 | 45.00 | 8.00 | 12.00 | 5.00 | E | Mixed; some BJP (NE identity); some AITC |
| Sarna_ORP | 45.00 | 30.00 | 5.00 | 15.00 | 5.00 | E | Tribal: BJP-leaning in North Bengal context; LF has historical tribal support |
| Other_residual | 60.00 | 20.00 | 5.00 | 5.00 | 10.00 | E | Marwari/Jain/Sikh urban class: BJP-leaning nationally |

### D.16 Vote × Caste (2019 LS)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 65.00 | 22.00 | 5.00 | 5.00 | 3.00 | C | CSDS 2019 WB UC BJP-leaning; North Bengal adjustment |
| OBC | 55.00 | 28.00 | 5.00 | 9.00 | 3.00 | C | Mixed; OBC BJP mobilization in North Bengal |
| SC_total | 70.00 | 22.00 | 2.00 | 4.00 | 2.00 | C | Rajbanshi SC: strong BJP swing in North Bengal; BJP Rajbanshi mobilization strategy |
| ST_total | 48.00 | 28.00 | 4.00 | 16.00 | 4.00 | C | Tribal: split; LF has historical tribal support in North Bengal |
| Other_Hindu_middle | 65.00 | 24.00 | 3.00 | 5.00 | 3.00 | E | North Bengal Hindu middle: BJP-leaning in 2019 |
| Muslim | 5.00 | 68.00 | 16.00 | 9.00 | 2.00 | C | Same as D.15 Muslim |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 66.00 | 22.00 | 3.00 | 6.00 | 3.00 | C | CSDS 2019 WB male BJP higher; North Bengal adjustment |
| Female | 60.00 | 32.00 | 3.00 | 3.00 | 2.00 | C | AITC women advantage smaller in North Bengal than South |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for AC 019. See NORMALIZED_SCHEMA.md §4.7.)

---

## E. 2019 baseline vote (calibration target)

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 63.42 | A | ECI 2019 LS Form-20 AC-segment data: 150,566 votes / 237,413 total valid = 63.42% |
| AITC | 27.15 | A | 64,449 votes / 237,413 |
| INC | 1.81 | A | 4,300 votes / 237,413 |
| LF | 5.65 | A | CPI(M) 13,408 votes / 237,413 (SUCI 439 + CPIM 13,408 = 13,847 = 5.83%; using CPIM 5.65% as LF proxy; SUCI classified Other_NOTA) |
| Other_NOTA | 1.97 | A | BSP 1,003 + AMB 341 + SWJP 254 + KPPU 261 + SUCI 439 + IND 2,392 = 4,690 / 237,413 = 1.97% |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 019 Dabgram-Fulbari (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Goutam Deb | AITC | ~50 | Dilip Singh | CPI(M) | ~38 | ~25,000 |
| 2016 AE | Goutam Deb | AITC | ~52 | (BJP / CPI(M) candidate) | BJP/CPI(M) | ~28 | ~28,000 |

Note: Goutam Deb was Mayor of Siliguri and a senior AITC leader. He won both 2011 and 2016 from this seat. The constituency is contiguous with Siliguri city and his personal vote was significant. By 2016 BJP had begun to grow in North Bengal but AITC held.

### LS — Jalpaiguri (PC 03) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Bijoy Chandra Barman | AITC | ~36 | AITC won Jalpaiguri narrowly; BJP rising |
| 2019 LS | Dr. Jayanta Kumar Roy | BJP | ~51 | BJP won by margin of ~184,000 votes; massive surge across Jalpaiguri LS |

Narrative context: The 2019 BJP sweep in Jalpaiguri LS (and AC 019's 63.4%) reflects the combined effect of Rajbanshi SC mobilization, anti-incumbency against AITC, and the broader North Bengal nationalist wave. Goutam Deb (sitting MLA) failed to protect AITC vote share even in his home constituency.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Jalpaiguri district religion, SC/ST data (census2011.co.in)
- Census of India 2011 — Rajganj CD block: population, religion, workers, language (censusindia.co.in)
- Census of India 2011 — Siliguri Municipal Corporation: population, religion, mother tongue (census2011.co.in)
- Election Commission of India — `2019_AssemblySegmentLevelVotingData.csv`: AC 019 vote breakdown (tier A; 237,413 valid votes, 283,995 electors)
- ECI — 2019 LS Jalpaiguri PC result (BJP 760,145 / 51%; AITC 576,141 / 38%)
- Delimitation Commission of India 2008 — WB Schedule: AC 019 = SMC wards 31–44 + 4 GPs of Rajganj block
- Wikipedia: Dabgram-Phulbari Assembly constituency — composition, reservation status

### Secondary sources (tier B / C)

- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership (urban/rural split)
- CSDS-Lokniti 2019 NES post-poll — vote × religion / caste / gender (state-level WB rollup)
- WB District Statistical Handbook — Jalpaiguri
- Indiastatpublications.com — Dabgram-Fulbari Assembly Factbook (SC/ST %, electorate)

### Tertiary / journalistic (tier D)

- Wikipedia: Rajganj (community development block) — language, workers, religion data
- The Print (2021): "Who are Rajbanshis" — Rajbanshi BJP mobilization in North Bengal
- Bold News / Millennium Post: Goutam Deb political biography (2011/2016 wins)
- india.com / elections.in: 2019 Jalpaiguri LS result summary

### Tier-D / E reliance flags (what to distrust)

- **Sub-unit population split** (C.11): SMC wards 31–44 vs Rajganj GP split is a rough estimate; ward-level Census data not disaggregated
- **Caste shares** (C.2, D.2, D.12): No post-1931 caste census; Rajbanshi SC dominant but sub-group shares are tier E
- **Migration/birthplace** (C.16, D.3): No AC-level Census D-series; tier D from city-level inference
- **Language splits** (C.5, D.1): SMC all-ward data used; ward 31–44 subset not separately available
- **Vote × demographic conditionals** (D.15–D.17): CSDS 2019 WB state rollup adjusted +15pp BJP for North Bengal context; adjustment is tier E
- **GP-level amenities / assets** (D.13–D.14): NFHS-4 urban/rural gradient proxy; sub-GP not available

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs. The
> validator's leakage gate exempts §H from the no-future-leakage check.

### 2021 WB Assembly Election — AC 019 Dabgram-Fulbari (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Sikha Chatterjee | 129,088 | 50.00 | A — ECI 2021 AE |
| AITC | Goutam Deb | ~100,700 | 39.00 | A — ECI 2021 AE |
| Others | various | ~28,000 | 11.00 | D — Wikipedia / ECI |
| **BJP margin** | | **~27,593 votes** | ~11 pp | A |

Note: Sikha Chatterjee (BJP) won despite Goutam Deb's incumbency advantage. BJP consolidated its 2019 LS gain at the AE level. AITC performed better in 2021 than 2019 LS at this seat (+12pp swing toward AITC from 27% to 39%), reflecting the statewide AITC 2021 recovery.

### 2024 Lok Sabha Election — AC 019 segment within Jalpaiguri LS (PC 03) (tier A, CSV)

Figures from `2024_AssemblySegmentLevelVotingData.csv`, AC_NO=19, Dabgram-Fulbari. Total valid votes: 256,373; electorate: 321,201; turnout ~79.8%.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Dr. Jayanta Kumar Roy | 156,023 | **60.86%** | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Nirmal Chandra Roy | 83,778 | **32.68%** | A | Same |
| CPI(M) | Debraj Barman | 11,486 | **4.48%** | A | Same |
| BSP | — | 1,104 | **0.43%** | A | Same |
| Others (IND, KPPU, MPOI, SUCI) | various | 3,982 | **1.55%** | A | Same |
| **BJP margin over AITC** | | **72,245 votes** | **28.18 pp** | A | Computed |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC segment shares within ±3pp of the tier-A figures:
- BJP target: 60.9% ± 3pp
- AITC target: 32.7% ± 3pp
- LF (CPI(M)) target: 4.5% ± 3pp
