# AC 016 — Maynaguri (SC) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 016 Maynaguri as of 2019 only — it does not reference any
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
| AC number | 016 | A | ECI / Delimitation Commission 2008 |
| AC name | Maynaguri | A | ECI |
| Reservation | SC | A | Delimitation 2008 |
| District | Jalpaiguri | A | Delimitation 2008 |
| Sub-division | Maynaguri | A | WB administrative |
| LS constituency | 3 — Jalpaiguri (SC reserved) | A | Delimitation 2008 |
| LS segments included with AC 016 | AC 13 Mekliganj · 14 Dhupguri · 15 Phalakata · 16 Maynaguri · 17 Mal · 18 Nagrakata · 19 Jalpaiguri | A | Delimitation 2008 |
| AC composition | Mainaguri census town + Maynaguri community development block (rural GPs) | A | Delimitation 2008 |
| Geographic note | Northern Jalpaiguri district, terai-foothills transition zone; borders Dhupguri block to west and Rajganj block to east | A | — |
| Sub-units used in v0 | **U1: Mainaguri_town** (census town / proto-urban) · **U2: Maynaguri_CDB_rural** (rural GPs of CDB Maynaguri) | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~329,032 (Maynaguri CDB total; includes ~30,490 in Mainaguri census town) | A | Census 2011 Maynaguri Block PCA |
| 2019 projected population | ~356,000 | E | 8-yr compound growth ~1.1%/yr (Jalpaiguri district baseline) |
| Sex ratio (2019, F per 1000 M) | ~940 | E | Maynaguri Block 2011: 935; slight improvement trend to 2019 |
| 2019 estimated electorate (18+) | ~251,373 | A | ECI 2019 LS roll — AC 016 total electors |
| Estimated M / F / TG split (2019) | 51.6% M / 48.4% F / <0.05% TG | E | Block sex ratio projection; TG from WB SIR pattern |
| 2019 polling stations (estimated) | ~285 | E | Back-derived from electorate size; Jalpaiguri district pattern |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 90.20 | A | Maynaguri CDB 2011: 90.02% Hindu; minimal drift 2011→2019 (+0.2pp projection) |
| Muslim | 9.55 | A | Maynaguri CDB 2011: 9.79% Muslim; slight relative decline as Hindu growth slightly faster |
| Christian | 0.05 | E | Maynaguri CDB 2011: 0.03%; small upward trend |
| Sarna_ORP | 0.10 | E | Tribal religion; ST population 1.3% with fraction Sarna |
| Other_residual | 0.10 | E | Sikh + Jain + Buddhist + Not_stated, lumped; 2011 Others 0.16% |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 71.20 | A | Maynaguri Block Census 2011: SC = 71.2% — overwhelmingly SC-dominant block |
| └ Rajbanshi_SC | 65.00 | C | Rajbanshi is the dominant SC in northern Jalpaiguri; ~91% of SC pool (journalistic + district pattern) |
| └ Other_SC | 6.20 | E | Residual SC sub-castes (Namasudra, Bagdi, etc.) |
| **ST_total** | 1.30 | A | Maynaguri Block Census 2011: ST = 1.3% |
| └ Other_ST | 1.30 | E | Small adivasi pockets; Boro/Rabha community traces |
| UC_bhadralok | 3.00 | E | Low bhadralok presence; SC-dominant AC; Brahmin/Kayastha/Baidya minimal |
| OBC | 4.00 | E | OBC Hindus including Kurmi, Mahishya fringe; Jalpaiguri district pattern |
| Other_Hindu_middle | 10.70 | E | Residual within Hindu (90.20 − 71.20 SC − 1.30 ST − 3.0 UC − 4.0 OBC − small rounding adj) |
| Muslim | 9.55 | E | See C.1; predominantly Bengali-speaking peasantry |
| Christian_plus_Sarna_plus_Other | 0.25 | E | Sarna_ORP + Christian + Other_residual combined |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.50 | E | Jalpaiguri district 2011 age pyramid; first-time voter cohort renormalised to 18+ adults |
| 23_27 | 11.80 | E | |
| 28_32 | 11.60 | E | |
| 33_37 | 10.80 | E | |
| 38_42 | 10.20 | E | |
| 43_47 | 9.50 | E | |
| 48_52 | 8.80 | E | |
| 53_57 | 7.50 | E | |
| 58_62 | 6.50 | E | |
| 63_67 | 5.30 | E | |
| 68 | 6.50 | E | 68+ open-ended; elderly cohort |
| **Sum** | **100.00** | — | self-check (renormalised from Census 2011 age pyramid excluding 0–17) |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.58 | E | Maynaguri Block 2011 sex ratio 935 → ~51.6% M; rounded |
| Female | 48.41 | E | Complement |
| Third_gender | 0.01 | E | WB SIR pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 84.26 | A | Maynaguri Block 2011: 84.26% Bengali first language (Census language data) |
| Hindi | 0.80 | E | Small trader/migrant Hindi-speaking minority; district pattern |
| Urdu | 0.50 | E | Muslim population Bengali-dominant; small Urdu fringe |
| Other | 2.14 | E | Residual catch-all (Nepali, Sadri, etc.) |
| Rajbongshi | 5.08 | A | Maynaguri Block 2011: 5.08% Rajbongshi first language (Census language data) |
| Sadri | 1.02 | A | Maynaguri Block 2011: 1.02% Sadri (tea garden worker language) |
| Nepali | 6.20 | E | Significant Nepali-speaking population in Jalpaiguri district terai zone |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 23.50 | E | Maynaguri Block 2011 literacy 75.63%; 2019 ~+2pp trend → ~22.5% illiterate; rounded |
| Primary | 26.00 | E | Jalpaiguri district education distribution scaled to block literacy level |
| Middle | 21.00 | E | |
| Secondary | 15.00 | E | |
| Higher_Secondary | 8.00 | E | |
| Graduate | 5.00 | E | Lower than state average; SC-dominant, rural AC |
| Postgraduate | 1.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 36.00 | E | Maynaguri CDB rural-dominant; Census 2011 main worker ~35%; slight +1pp trend |
| Marginal_worker | 13.00 | E | Seasonal agricultural marginal workers; typical for agrarian SC belt |
| Non_worker | 37.00 | E | Housewives + elderly + retired; heavy in rural households |
| Student | 8.00 | E | 18–22 in education; lower than urban areas |
| Unemployed | 6.00 | E | Educated job-seekers; depressed rural economy |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 28.00 | E | Maynaguri CDB rural belt; dominant agricultural cultivators |
| Agricultural_labourer | 32.00 | E | High SC labourer share; Rajbanshi community pattern |
| Household_industry | 5.00 | E | Bidi-rolling, weaving, cottage industry |
| Manufacturing | 3.00 | E | Limited organised manufacturing in block |
| Construction | 6.00 | E | Includes seasonal migrant construction workers |
| Trade_retail | 10.00 | E | Mainaguri town retail hub for block |
| Transport_logistics | 4.00 | E | NH-27 (Siliguri–Assam corridor) passes through area |
| Services | 7.00 | E | Private services; hospitality |
| Government_services_teachers | 3.00 | E | SC-reserved quota positions; teachers, panchayat staff |
| Out_migrant_worker | 2.00 | D | Relatively low out-migration compared to South Bengal; some to Siliguri/Kolkata |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Census B-04 WB rural pattern; low employer share |
| Employee | 22.00 | E | Govt employees + organised sector; moderate |
| Single_worker | 48.00 | E | Own-account cultivators + petty traders |
| Family_worker | 28.50 | E | High unpaid family worker share in agricultural households |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 28.00 | D | Jalpaiguri rural BPL ~35% in 2012; WB poverty fell ~7pp 2011–19 → ~28%; SC-dominated AC skews higher than state |
| Above_Poverty_Line_low_income | 37.00 | E | Just above BPL; near-poor agrarian households |
| Lower_middle | 22.00 | E | |
| Middle | 11.00 | E | Mainaguri town / government employee households |
| Upper_middle_well_off | 2.00 | E | Very limited affluent class in SC-dominated rural AC |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Mainaguri_town | 9.27 | A | Mainaguri census town pop 30,490 / CDB total 329,032 = 9.27%; held stable 2011→2019 |
| U2_Maynaguri_CDB_rural | 90.73 | A | Remainder: rural GPs of Maynaguri CDB; dominant share |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.6 persons | E | WB 2011: 4.3 state average; Jalpaiguri rural slightly higher; projected stable |
| Nuclear_HH | 65.00 | E | NFHS-4 WB rural pattern; lower than urban areas |
| Joint_HH | 28.00 | E | Higher joint HH share in SC agricultural communities |
| Extended_multi_generation | 7.00 | E | |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.00 | E | Census 2011 Jalpaiguri district pattern; first-time-voter cohort lower in rural areas |
| Currently_married | 66.00 | E | High marriage rate in rural SC communities; younger marriage age |
| Widowed | 7.50 | E | Female-skewed; concentrated in 60+ cohort |
| Separated_divorced | 1.50 | E | Rural WB pattern |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 68.00 | C | NFHS-4 WB rural 60%; +Jalpaiguri slightly higher district; +trend to 2019 ~68% |
| Radio | 8.00 | C | Higher than South Bengal; North Bengal AM radio traditionally stronger |
| Mobile_phone | 82.00 | C | NFHS-4 WB rural ~74%; Jio rollout 2016–19 growth → ~82% |
| Smartphone_with_internet | 38.00 | C | NFHS-4 baseline + Jio 4G rural rollout; lower than South Bengal metro-adjacent ACs |
| Computer | 4.00 | C | Very low; rural SC-dominant AC |
| Two_wheeler | 22.00 | C | NFHS-4 WB rural 18%; modest growth to 2019 |
| Four_wheeler | 3.00 | E | Minimal in this income bracket |
| Banking_access | 85.00 | B | PMJDY saturation 2016–19; Jan Dhan accounts; slight lag vs South Bengal |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 89.00 | C | NFHS-4 WB rural 84%; Jalpaiguri river-fed groundwater access slightly higher |
| Improved_sanitation | 55.00 | C | NFHS-4 WB rural 51%; +Swachh Bharat 2014–19 rural gains (~+4pp) |
| LPG_clean_cooking_fuel | 35.00 | C | NFHS-4 WB rural 24%; +Ujjwala 2016–19 rural push (~+11pp); lower uptake in remote blocks |
| Wood_biomass_fuel | 60.00 | C | Dominant fuel in forested/semi-forested terai zone; declining as LPG rises |
| Other_fuel | 5.00 | E | Kerosene + dung + other; residual |
| Electricity | 90.00 | E | Census 2011 Maynaguri CDB; +Saubhagya 2017–19 gains; estimated ~90% by 2019 |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 82.00 | E | Predominantly native Rajbanshi SC community; low outmigration from North Bengal |
| WB_other_district | 5.00 | E | Some in-migrants from Cooch Behar, Darjeeling; Jalpaiguri district pattern |
| Other_Indian_state | 2.50 | E | Hindi/Bihari trader fringe in Mainaguri town; Nepali-origin settled families |
| Bangladesh_origin | 4.00 | D | Smaller refugee fraction than South Bengal; some Namasudra/SC inflow from partition |
| Outside_India | 0.50 | E | Negligible; some Nepal-origin registered households |
| Out_migrant | 3.00 | E | Seasonal/permanent out-migrants to Siliguri and Kolkata; registered here |
| Nepal_Bhutan_origin | 3.00 | E | AC-local: significant Nepali-speaking settled community in terai zone |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Sadri | Nepali | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 81.00 | 0.80 | 0.10 | 1.10 | 5.50 | 1.10 | 10.40 | E | Rajbanshi SC = Rajbongshi-speaking; Nepali within Hindu; district language pattern |
| Muslim | 97.00 | 0.50 | 1.50 | 0.50 | 0.50 | 0.00 | 0.00 | E | Maynaguri Muslims are Bengali-dominant peasantry; tiny Urdu fringe |
| Christian | 70.00 | 5.00 | 0.00 | 10.00 | 5.00 | 5.00 | 5.00 | E | Small base; mixed language |
| Sarna_ORP | 30.00 | 0.00 | 0.00 | 20.00 | 20.00 | 30.00 | 0.00 | E | Tribal; Sadri + Rajbongshi dominant among ORP |
| Other_residual | 60.00 | 10.00 | 0.00 | 10.00 | 5.00 | 5.00 | 10.00 | E | Mixed residual |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. 2D canonical layout.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 78.94 | 1.44 | 3.33 | 4.43 | 11.86 | 0.00 | 0.00 | E | SC_total 71.2% / 90.2% Hindu; ST 1.3% / 90.2%; UC, OBC, Other scaled to Hindu total |
| Muslim | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 100.00 | 0.00 | A | self-evident |
| Christian | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 100.00 | A | self-evident |
| Sarna_ORP | 10.00 | 80.00 | 0.00 | 5.00 | 5.00 | 0.00 | 0.00 | E | Tribal religion routes mostly to ST; small SC fraction |
| Other_residual | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 100.00 | E | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 82.00 | 4.50 | 2.50 | 4.50 | 0.50 | 2.50 | E | Rajbanshi SC native-dominant; some Bangladesh partition inflow |
| Muslim | 88.00 | 5.00 | 1.00 | 3.00 | 0.50 | 2.50 | E | Mostly native Bengali Muslim peasantry |
| Christian | 75.00 | 10.00 | 5.00 | 5.00 | 0.00 | 5.00 | E | Mixed base |
| Sarna_ORP | 90.00 | 5.00 | 2.00 | 0.00 | 0.00 | 3.00 | E | Tribal; predominantly native |
| Other_residual | 40.00 | 15.00 | 35.00 | 3.00 | 2.00 | 5.00 | E | Nepali/Hindi trade/service migrants |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 69.00 | 39.00 | 86.00 | C | Dominant group; near AC average |
| Muslim | 60.00 | 30.00 | 78.00 | C | Slightly below Hindu; NFHS-4 WB religion gap |
| Christian | 75.00 | 45.00 | 90.00 | E | Small base; slightly higher asset access |
| Sarna_ORP | 45.00 | 20.00 | 70.00 | E | Tribal fringe; lower asset access |
| Other_residual | 80.00 | 50.00 | 92.00 | E | Mostly better-off Nepali/Hindi migrants |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 8.00 | 15.00 | 15.00 | 20.00 | 18.00 | 18.00 | 6.00 | E |
| SC_total | 25.00 | 28.00 | 22.00 | 14.00 | 7.00 | 3.00 | 1.00 | E |
| ST_total | 30.00 | 28.00 | 20.00 | 13.00 | 6.00 | 2.50 | 0.50 | E |
| OBC | 18.00 | 25.00 | 22.00 | 18.00 | 10.00 | 5.50 | 1.50 | E |
| Other_Hindu_middle | 18.00 | 25.00 | 22.00 | 18.00 | 10.00 | 5.50 | 1.50 | E |
| Muslim | 22.00 | 27.00 | 23.00 | 16.00 | 8.00 | 3.50 | 0.50 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share within age-gender cell.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 10.00 | 8.00 | E |
| 23_27 | 9.00 | 7.00 | E |
| 28_32 | 8.00 | 5.00 | E |
| 33_37 | 7.00 | 4.00 | E |
| 38_42 | 6.00 | 3.00 | E |
| 43_47 | 5.50 | 2.50 | E |
| 48_52 | 5.00 | 2.00 | E |
| 53_57 | 4.50 | 1.50 | E |
| 58_62 | 4.00 | 1.00 | E |
| 63_67 | 3.50 | 1.00 | E |
| 68 | 3.00 | 0.50 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 6.00 | 30.00 | E |
| 23_27 | 42.00 | 82.00 | E |
| 28_32 | 82.00 | 93.00 | E |
| 33_37 | 92.00 | 91.00 | E |
| 38_42 | 93.00 | 89.00 | E |
| 43_47 | 92.00 | 85.00 | E |
| 48_52 | 91.00 | 78.00 | E |
| 53_57 | 90.00 | 68.00 | E |
| 58_62 | 88.00 | 55.00 | E |
| 63_67 | 82.00 | 38.00 | E |
| 68 | 72.00 | 22.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 28.00 | 60.00 | C | Rural cultivator baseline; Jalpaiguri district |
| Agricultural_labourer | 20.00 | 50.00 | C | Lowest income; lowest smartphone access |
| Household_industry | 35.00 | 65.00 | C | Slightly higher; cottage industry exposure |
| Manufacturing | 48.00 | 78.00 | C | |
| Construction | 42.00 | 68.00 | C | |
| Trade_retail | 65.00 | 85.00 | C | Mainaguri town concentration |
| Transport_logistics | 60.00 | 80.00 | C | NH-27 corridor workers |
| Services | 70.00 | 88.00 | C | Private services |
| Government_services_teachers | 85.00 | 95.00 | C | Highest access |
| Out_migrant_worker | 65.00 | 72.00 | D | Working outside; smartphone-dependent for remittances |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 38.00 | 1.50 | E |
| Primary | 40.00 | 3.00 | E |
| Middle | 37.00 | 5.00 | E |
| Secondary | 30.00 | 8.00 | E |
| Higher_Secondary | 22.00 | 12.00 | E |
| Graduate | 25.00 | 14.00 | E |
| Postgraduate | 35.00 | 10.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 016. See NORMALIZED_SCHEMA.md §4.7.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Mainaguri_town | 87.00 | 11.00 | 0.50 | 0.20 | 1.30 | E | Town slightly higher Muslim presence than rural; trade community |
| U2_Maynaguri_CDB_rural | 90.40 | 9.38 | 0.04 | 0.08 | 0.10 | E | Rural CDB approximates block-level Census 2011 data |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit).

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Mainaguri_town | 6.00 | 60.00 | 1.00 | 6.00 | 15.00 | 11.00 | 1.00 | E |
| U2_Maynaguri_CDB_rural | 2.50 | 72.50 | 1.35 | 3.75 | 10.90 | 8.75 | 0.25 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Mainaguri_town | 82.00 | 55.00 | 10.00 | 92.00 | C |
| U2_Maynaguri_CDB_rural | 66.00 | 35.00 | 3.00 | 83.00 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Mainaguri_town | 65.00 | 75.00 | 95.00 | 98.00 | C |
| U2_Maynaguri_CDB_rural | 30.00 | 51.00 | 88.00 | 89.00 | C |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 WB regional rollup calibrated to AC 016 result.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 54.00 | 38.00 | 0.70 | 3.00 | 4.30 | C | CSDS 2019 WB regional; BJP Hindu consolidation; Rajbanshi SC BJP swing |
| Muslim | 5.00 | 80.00 | 5.00 | 6.00 | 4.00 | C | Muslim AITC bloc; standard WB Muslim vote pattern |
| Christian | 20.00 | 60.00 | 5.00 | 8.00 | 7.00 | E | Small base; approximation |
| Sarna_ORP | 40.00 | 45.00 | 2.00 | 8.00 | 5.00 | E | Tribal; mixed; BJP appeal to tribal communities |
| Other_residual | 45.00 | 35.00 | 5.00 | 5.00 | 10.00 | E | Nepali/Hindi fringe; BJP-leaning |

### D.16 Vote × Caste (2019 LS)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 62.00 | 28.00 | 3.00 | 5.00 | 2.00 | C | Bhadralok BJP-leaning by 2019; CSDS WB pattern |
| OBC | 45.00 | 38.00 | 3.00 | 8.00 | 6.00 | C | Mixed; CSDS WB pattern |
| SC_total | 53.00 | 38.00 | 0.50 | 3.50 | 5.00 | C | Rajbanshi SC BJP swing 2019; key to BJP win; CSDS WB + AC result calibrated |
| ST_total | 40.00 | 42.00 | 2.00 | 10.00 | 6.00 | C | Tribal; mixed; slight AITC lead |
| Other_Hindu_middle | 48.00 | 40.00 | 2.00 | 5.00 | 5.00 | E | Residual Hindu middle; BJP-leaning |
| Muslim | 5.00 | 80.00 | 5.00 | 6.00 | 4.00 | C | Same as D.15 Muslim row |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 52.00 | 39.00 | 0.80 | 3.50 | 4.70 | C | CSDS 2019 WB; male BJP-leaning relative to female |
| Female | 47.00 | 47.00 | 0.70 | 2.20 | 3.10 | C | Women more AITC-leaning; pre-LB baseline |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for AC 016. See NORMALIZED_SCHEMA.md §4.7.)

---

## E. 2019 baseline vote (calibration target)

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 49.58 | A | ECI GE2019 Form-20 AC-016 segment; Dr Jayanta Kumar Roy 110,819 votes / 223,510 total valid |
| AITC | 42.98 | A | Bijoy Chandra Barman 96,072 votes |
| INC | 0.76 | A | Mani Kumar Darnal 1,705 votes |
| LF | 2.85 | A | CPIM 5,916 + SUCI(C) 444 = 6,360 votes |
| Other_NOTA | 3.83 | A | BSP + AMB + SWJP + KPPU + IND × 3 + NOTA = 8,564 votes |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 016 (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Dinabandhu Roy (Palu) | RSP | ~48 | AITC candidate | AITC | ~36 | ~est. 15,000 |
| 2014 by-election | Ananta Deb Adhikari | AITC | — | Dinabandhu Roy (Palu) | RSP | — | ~31,790 |
| 2016 AE | Ananta Deb Adhikari | AITC | ~54 | Chhaya Dey (Roy) | RSP | ~35 | 34,907 |

Notes: Maynaguri was an RSP (Left Front) stronghold in 2011, reversing to AITC after the 2014 by-election when sitting RSP MLA Dinabandhu Roy reportedly switched party allegiances. AITC won comfortably in 2016. The 2019 LS result showed a sharp BJP surge (+49.6%) against AITC (+43%), mirroring the North Bengal BJP wave in the Jalpaiguri LS constituency.

### LS 3 Jalpaiguri — historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Bijoy Chandra Barman | AITC | ~39 | AITC won; CPI(M) second ~22%; BJP ~25% |
| 2019 LS | Dr Jayanta Kumar Roy | BJP | ~50 | BJP wave in North Bengal; AITC second ~44% |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Maynaguri CD Block Primary Census Abstract (via censusindia.co.in and Census 2011 block tables)
- Census of India 2011 — Maynaguri Block language data (Bengali 84.26%, Rajbongshi 5.08%, Sadri 1.02%)
- Census of India 2011 — Maynaguri Block: SC 71.2%, ST 1.3%; religion: Hindu 90.02%, Muslim 9.79%
- Census of India 2011 — Mainaguri census town population: 30,490
- Election Commission of India — 2019 LS GE results for AC 016 (data/2019_AssemblySegmentLevelVotingData.csv)
- Election Commission of India — 2016 AE result; 2014 by-election result for Maynaguri
- Delimitation Commission of India 2008 — WB Schedule (AC 016 Maynaguri SC reserved; part of PC 3 Jalpaiguri SC)

### Secondary sources (tier B / C)

- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline (urban/rural split)
- CSDS-Lokniti 2019 NES post-poll — vote × religion / caste / gender WB regional cross-tabs
- PMJDY enrollment data — banking access baseline
- Jalpaiguri District Census 2011: SC 37.7%, ST 18.9%, Hindu 82.41%, Muslim 13.25%

### Tertiary / journalistic (tier D)

- Resultuniversity.com / Oneindia — 2016 AE and 2014 by-election margin figures
- Jalpaiguri district BPL rate estimates (~35% rural 2012) via district statistical handbook pattern
- Jalpaiguri Lok Sabha 2014 result from election archives

### Tier-D / E reliance flags (what to distrust)

- **Caste sub-group shares within SC** (C.2 sub-rows) — Rajbanshi share estimated from district journalistic pattern; no post-1931 caste census; tier C/D
- **Migration / birthplace shares** (C.16, D.3) — no public AC-level Census D-series; tier E/D from district pattern
- **GP-level detail** (D.11–D.14) — collapsed to 2 sub-units; refine when DCHB Part-A accessible
- **Vote × Demographic** (D.15–D.17) — CSDS 2019 WB regional rollup calibrated to AC result; tier C
- **Pre-2019 AE results** (Section F) — Margin for 2011 AE estimated; 2014 by-election details from third-party aggregators; tier D
- **Nepali-origin population share** (C.16, C.5) — estimated from district language/migration pattern; tier E
- **Economic / poverty** (C.10) — AC-level BPL not directly available; Jalpaiguri district rural proxy used; tier D

### v0 known gaps

1. DCHB Jalpaiguri Part-A — sub-unit collapsed to 2 (town + CDB rural); GP-level decomposition deferred
2. ECI 2019 LS Form-20 already tier A from CSV; AC segment vote is direct (not proportional decomposition)
3. Census HH-13 block-level — using NFHS state-level proxy for asset/media
4. Census D-series — using qualitative/district-level anchor for migration
5. Full CSDS WB regional cross-tabs — using Swarajya/CSDS summary for D.15–D.17
6. 2011 AE detailed vote figures — margin estimate only; full candidate breakdown not retrieved

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2021 WB Assembly Election — AC 016 Maynaguri (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Koushik Roy | 115,306 | 48.84% | A — ECI 2021 AE |
| AITC | Manoj Roy | 103,395 | 43.79% | A — ECI 2021 AE |
| Others / LF | various | ~17,392 | ~7.37% | D — aggregated |
| **BJP margin** | | **11,911 votes** | ~5.05 pp | A |

Total valid votes: 236,093. BJP retained the seat won in the 2019 swing.

### 2024 Lok Sabha Election — AC 016 segment within Jalpaiguri LS (PC 3) (tier A, CSV)

> Figures below are **tier A** — sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=16, Maynaguri. Electors: 272,625; total valid votes: 232,631 + 2,224 NOTA = 232,631 candidates + NOTA.

| Party | Candidate (LS level) | Votes | AC-016 segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Dr Jayanta Kumar Roy | 112,763 | 48.47% | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Nirmal Chandra Roy | 108,018 | 46.43% | A | Same |
| CPI(M) | Debraj Barman | 5,988 | 2.57% | A | Same |
| NOTA | — | 2,224 | 0.96% | A | Same |
| Others (BSP, KPPU, SUCI, MPOI, IND) | various | 3,638 | 1.57% | A | Same |
| **BJP margin over AITC** | | **4,745 votes** | **2.04 pp** | A | Computed |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC-016 shares within ±3pp:
- BJP target: 48.5% ± 3pp
- AITC target: 46.4% ± 3pp
- LF + Others target: 5.1% ± 3pp

Note: The BJP margin narrowed sharply from 2019 (BJP +6.6pp) to 2024 (BJP +2.0pp), indicating AITC recovery in the interval.
