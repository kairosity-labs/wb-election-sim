# AC 009 — Tufanganj (GEN) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 009 Tufanganj as of 2019 only — it does not reference any
> post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../../NORMALIZED_SCHEMA.md)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 009 | A | ECI / Delimitation Commission 2008 |
| AC name | Tufanganj | A | ECI |
| Reservation | GEN (General) | A | Delimitation 2008 |
| District | Cooch Behar | A | Delimitation 2008 |
| Sub-division | Tufanganj | A | WB administrative |
| LS constituency | 02 — Cooch Behar (SC reserved) | A | Delimitation 2008 |
| LS segments included | AC 005 Mekhliganj · 006 Mathabhanga · 007 Cooch Behar Uttar · 008 Cooch Behar Dakshin · 009 Tufanganj · 010 Sitalkuchi · 011 Sitai | A | Delimitation 2008 |
| AC composition | Tufanganj Municipality (full) + Tufanganj II CD Block (full) + 4 GPs of Tufanganj I CD Block: Andaran Fulbari I, Balabhut, Dhalpal I, Nakkatigachh | A | Delimitation 2008 |
| Geographic note | North Bengal plains, Tufanganj subdivision; borders Assam; Torsa and Kaljani river basin | A | — |
| Sub-units used in v0 | **U1: Tufanganj_Municipality** (urban) · **U2: Tufanganj_II_CDB_and_rural** (Tufanganj II full + 4 GPs from Tufanganj I) | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~210,000 (Tufanganj Muni 20,998 + Tufanganj II CDB 186,726 + ~4/72 rural share of Tufanganj I ≈ ~13,800) | E | Census 2011; v0 GP-share approximation |
| 2019 projected population | ~228,000 | E | 8-yr compound religion-differential growth (methodology §4) |
| Sex ratio (2019, F per 1000 M) | ~952 | E | Cooch Behar district 952 (Census 2011 baseline); minimal projection drift |
| 2019 estimated electorate (18+) | ~225,957 | A | ECI 2019 LS roll (data/2019_AssemblySegmentLevelVotingData.csv) |
| Estimated M / F / TG split (2019) | 51.2% M / 48.7% F / <0.1% TG | E | Cooch Behar district sex ratio back-projected |
| 2019 polling stations (estimated) | ~250 | E | Back-projection from AC-level electorate |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 84.50 | E | Tufanganj II CDB 2011: 85.60% Hindu (A); Tufanganj I GPs (4 of 72): ~70% Hindu; Muni ~82% Hindu; AC pop-weighted ~84.5% |
| Muslim | 15.00 | E | Tufanganj II 2011: 14.15% Muslim; Tufanganj I GP rural pocket ~28%; Muni ~17%; AC weighted ~15% |
| Christian | 0.30 | E | Cooch Behar district baseline; small urban pocket |
| Sarna_ORP | 0.10 | E | Marginal tribal religion population |
| Other_residual | 0.10 | E | Sikh + Jain + Buddhist + Not_stated lumped |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 47.00 | A | Pop-weighted from Tufanganj II CDB (53.8%) + Muni (23.03%) + 4 GPs Tufanganj I (~46%) |
| └ Rajbanshi_SC | 43.00 | C | ~91.5% of SC pool; dominant community in Cooch Behar |
| └ Other_SC | 4.00 | E | Namasudra, Bagdi, Chamar residual |
| **ST_total** | 1.50 | A | Tufanganj II 2.1% + Muni 0.41% weighted |
| UC_bhadralok | 5.00 | E | Brahmin/Kayastha concentrated in Muni |
| OBC | 4.00 | E | Koch (non-SC), Teli, Sutradhar etc. |
| Other_Hindu_middle | 27.00 | E | Residual Hindu (84.5 − 47 − 1.5 − 5 − 4) = 27 |
| Muslim | 15.00 | E | All sub-castes pooled |
| Christian_plus_Sarna_plus_Other | 0.50 | E | C.1 residual combined |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.50 | E | Renormalized from Cooch Behar district Census 2011 age pyramid (18+ only) |
| 23_27 | 12.00 | E | |
| 28_32 | 11.50 | E | |
| 33_37 | 10.50 | E | |
| 38_42 | 9.50 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.00 | E | |
| 63_67 | 8.00 | E | |
| 68 | 7.00 | E | 68+ open-ended; Cooch Behar older cohort slightly larger |
| **Sum** | **100.00** | — | self-check (renormalized from Census 2011 after excluding 0–17) |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.23 | E | Cooch Behar district 2011 sex ratio 952 F per 1000 M → 51.23% M |
| Female | 48.76 | E | |
| Third_gender | 0.01 | E | Marginal; WB 2021 SIR pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 79.00 | E | District dominant; but Rajbongshi language significant |
| Hindi | 0.50 | E | Muni trader + migrant fringe |
| Urdu | 0.50 | E | Muslim urban pocket |
| Other | 0.50 | E | Residual catch-all (Assamese, Nepali minor) |
| Rajbongshi | 19.50 | C | Rajbongshi (a Bengali dialect / distinct language) spoken by Rajbanshi SC; significant in Tufanganj; Census 2011 Cooch Behar pattern |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 22.00 | E | Tufanganj II CDB literacy 75.75% (2011, A); literacy ~79% by 2019 (+3pp trend) → ~21% illiterate; Muni higher; AC weighted ~22% |
| Primary | 22.00 | E | Census 2011 education distribution, Cooch Behar pattern |
| Middle | 20.00 | E | |
| Secondary | 17.00 | E | |
| Higher_Secondary | 10.00 | E | |
| Graduate | 7.00 | E | |
| Postgraduate | 2.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 32.00 | E | Cooch Behar district Census 2011 main-worker share ~32%; stable trend |
| Marginal_worker | 13.00 | E | Agricultural seasonal work dominant |
| Non_worker | 38.00 | E | Housewife + elderly + retired; high female non-worker share in rural |
| Student | 9.00 | E | 18–22 cohort in education |
| Unemployed | 8.00 | E | Educated job-seekers; limited formal sector |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 22.00 | E | Tufanganj II CDB: high agricultural share; Cooch Behar plains rice/jute cultivation |
| Agricultural_labourer | 35.00 | E | Largest worker category; SC-heavy agricultural labour |
| Household_industry | 5.00 | E | Weaving, handloom minor |
| Manufacturing | 3.00 | E | Very limited organised sector |
| Construction | 6.00 | E | Includes out-migrant returnees |
| Trade_retail | 10.00 | E | Tufanganj Muni hub |
| Transport_logistics | 5.00 | E | Road transport; Cooch Behar-Assam corridor |
| Services | 7.00 | E | Private services |
| Government_services_teachers | 4.00 | E | Government and educational services |
| Out_migrant_worker | 3.00 | D | Limited compared to South Bengal; some migration to tea gardens and Assam |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Census B-04 WB rural pattern; very low in agrarian AC |
| Employee | 22.00 | E | Govt + organised sector + retail |
| Single_worker | 52.00 | E | Own-account cultivator + artisan + small trader dominant |
| Family_worker | 24.50 | E | Unpaid family farm help |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 28.00 | C | Cooch Behar district BPL ~32% (2011); WB poverty fell ~5pp 2011-19 → ~28%; high SC share drives higher BPL |
| Above_Poverty_Line_low_income | 35.00 | E | |
| Lower_middle | 22.00 | E | |
| Middle | 12.00 | E | |
| Upper_middle_well_off | 3.00 | E | Muni small affluent fringe |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Tufanganj_Municipality | 9.20 | E | 2011: Muni 20,998 / AC ~228,000 projected = ~9.2%; urban anchor |
| U2_Tufanganj_II_CDB_and_rural | 90.80 | E | Tufanganj II CDB (186,726) + 4 GPs of Tufanganj I (~13,800) = ~200,500 / AC ~228,000 |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | WB 2011: 4.3 persons; North Bengal slightly higher; minor projection |
| Nuclear_HH | 66.00 | E | NFHS-4 WB rural pattern; North Bengal slight joint-family retention |
| Joint_HH | 27.00 | E | |
| Extended_multi_generation | 7.00 | E | |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.00 | E | Census 2011 Cooch Behar pattern; first-time-voter cohort |
| Currently_married | 65.00 | E | Rural-dominant AC; high marriage rate |
| Widowed | 8.00 | E | Concentrated in 60+; female-skewed |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 68.00 | C | NFHS-4 WB rural ~60%, urban ~89%; North Bengal rural slightly lower than state; AC ~68% |
| Radio | 6.00 | C | Declining nationally; slightly higher in rural North Bengal |
| Mobile_phone | 82.00 | C | NFHS-4 WB rural ~70%, +growth → ~82% by 2019 |
| Smartphone_with_internet | 38.00 | C | NFHS-4 baseline + Jio rollout 2016-19; rural North Bengal lag vs South Bengal |
| Computer | 5.00 | C | NFHS-4 WB rural ~4%; Muni slightly higher; AC weighted ~5% |
| Two_wheeler | 22.00 | C | NFHS-4 WB rural ~18%; growth to ~22% |
| Four_wheeler | 4.00 | C | Limited rural penetration |
| Banking_access | 85.00 | B | PMJDY 2014+ saturation; Cooch Behar high PMJDY enrollment |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 88.00 | C | NFHS-4 WB rural 84%; North Bengal river-plain area with tubewell access; AC ~88% |
| Improved_sanitation | 55.00 | C | NFHS-4 WB rural ~51%; Swachh Bharat rollout 2014-19 (+10pp rural) → ~55% |
| LPG_clean_cooking_fuel | 28.00 | C | NFHS-4 WB rural ~24%; Ujjwala 2016-19 rollout (+8pp rural) → ~28% |
| Wood_biomass_fuel | 67.00 | C | Dominant fuel in rural North Bengal |
| Other_fuel | 5.00 | C | Kerosene, dung, etc. |
| Electricity | 92.00 | A | Census 2011 Cooch Behar + Saubhagya 2017-19 saturation; North Bengal electrification |
| **Note** | (water/sanitation/electricity independent; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 78.00 | D | Rajbanshi community historically settled; Cooch Behar princely state integrated 1949; high native share |
| WB_other_district | 8.00 | D | Some in-migration from Jalpaiguri, North Dinajpur |
| Other_Indian_state | 3.00 | D | Assamese, Bihari, migrant workers |
| Bangladesh_origin | 8.00 | D | Hindu refugee population (post-1947 + 1971); lower than South Bengal but present; some Rajbanshi from East Pakistan origin |
| Outside_India | 0.50 | E | Negligible; minor Nepal/Bhutan-origin in border fringe |
| Out_migrant | 2.50 | E | Limited; some working in Assam tea gardens or metro cities |
| Nepal_Bhutan_origin | 0.00 | E | Border area; set 0 — negligible for AC level |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 73.00 | 0.50 | 0.00 | 0.50 | 26.00 | E | Rajbongshi speakers are predominantly Hindu Rajbanshi-SC; Cooch Behar Census 2011 pattern |
| Muslim | 92.00 | 1.00 | 4.50 | 2.50 | 0.00 | E | Bengali-Muslim (Koch Bihar pattern); small Urdu-speaking pocket in Muni |
| Christian | 90.00 | 5.00 | 0.00 | 5.00 | 0.00 | E | Tiny base; Bengali + mission-school families |
| Sarna_ORP | 60.00 | 10.00 | 0.00 | 30.00 | 0.00 | E | Tribal languages; approximated |
| Other_residual | 70.00 | 20.00 | 0.00 | 10.00 | 0.00 | E | Marwari/other trader pop |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 53.85 | 1.78 | 5.92 | 4.73 | 31.95 | 0 | 1.78 | E | 47% SC / 84.5% Hindu = 55.6% of Hindu → minor adj for mixed; total Hindu = 84.5%; SC 47/84.5=55.6; Muni lower SC dilutes; AC blend ~53.85% |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 90 | 0 | 5 | 5 | 0 | 0 | E | Tribal sub-castes route to ST_total |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 75.00 | 8.00 | 3.00 | 11.50 | 0.50 | 2.00 | D | Rajbanshi Hindu largely native; Bangladesh-origin subset from pre-1971 trickle |
| Muslim | 90.00 | 5.00 | 2.00 | 2.00 | 0.50 | 0.50 | D | Koch Bihar Muslims are mostly native Bengali-peasantry; small Bangladesh trickle |
| Christian | 80.00 | 12.00 | 5.00 | 3.00 | 0.00 | 0.00 | E | Mixed; mission community |
| Sarna_ORP | 85.00 | 10.00 | 5.00 | 0.00 | 0.00 | 0.00 | E | Tribal population locally rooted |
| Other_residual | 40.00 | 15.00 | 40.00 | 5.00 | 0.00 | 0.00 | E | Marwari/trader community mostly other-state |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 69.00 | 39.00 | 86.00 | C | NFHS-4 WB religion gap; Rajbanshi-SC slightly below district mean |
| Muslim | 60.00 | 30.00 | 76.00 | C | NFHS-4 WB Muslim HH lower asset baseline |
| Christian | 80.00 | 50.00 | 92.00 | E | Small base; educated |
| Sarna_ORP | 55.00 | 22.00 | 70.00 | E | Marginal tribal population |
| Other_residual | 90.00 | 70.00 | 95.00 | E | Trader/upper-income residual |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 8.00 | 12.00 | 15.00 | 20.00 | 18.00 | 20.00 | 7.00 | E |
| SC_total | 24.00 | 24.00 | 21.00 | 16.00 | 9.00 | 5.00 | 1.00 | E |
| ST_total | 28.00 | 26.00 | 20.00 | 14.00 | 7.00 | 4.00 | 1.00 | E |
| OBC | 18.00 | 22.00 | 20.00 | 18.00 | 12.00 | 8.00 | 2.00 | E |
| Other_Hindu_middle | 18.00 | 23.00 | 21.00 | 18.00 | 11.00 | 7.00 | 2.00 | E |
| Muslim | 22.00 | 25.00 | 21.00 | 17.00 | 9.00 | 5.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 12.00 | 10.00 | E |
| 23_27 | 13.00 | 9.00 | E |
| 28_32 | 11.00 | 7.00 | E |
| 33_37 | 9.00 | 5.00 | E |
| 38_42 | 8.00 | 4.00 | E |
| 43_47 | 7.00 | 3.00 | E |
| 48_52 | 6.00 | 2.50 | E |
| 53_57 | 5.00 | 2.00 | E |
| 58_62 | 4.00 | 1.50 | E |
| 63_67 | 3.50 | 1.00 | E |
| 68 | 3.00 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 6.00 | 28.00 | E |
| 23_27 | 40.00 | 80.00 | E |
| 28_32 | 78.00 | 92.00 | E |
| 33_37 | 88.00 | 90.00 | E |
| 38_42 | 90.00 | 88.00 | E |
| 43_47 | 90.00 | 84.00 | E |
| 48_52 | 88.00 | 78.00 | E |
| 53_57 | 86.00 | 68.00 | E |
| 58_62 | 82.00 | 55.00 | E |
| 63_67 | 76.00 | 40.00 | E |
| 68 | 68.00 | 28.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 28.00 | 60.00 | C | Rural agricultural baseline; North Bengal lag |
| Agricultural_labourer | 20.00 | 50.00 | C | Lowest income segment |
| Household_industry | 32.00 | 65.00 | C | |
| Manufacturing | 45.00 | 75.00 | C | |
| Construction | 38.00 | 65.00 | C | |
| Trade_retail | 62.00 | 85.00 | C | Muni concentrated |
| Transport_logistics | 55.00 | 78.00 | C | Road transport workers |
| Services | 65.00 | 85.00 | C | |
| Government_services_teachers | 82.00 | 92.00 | C | Highest access |
| Out_migrant_worker | 65.00 | 72.00 | D | Working outside; smartphone-heavy for remittance |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 30.00 | 2.00 | E |
| Primary | 35.00 | 3.00 | E |
| Middle | 33.00 | 5.00 | E |
| Secondary | 28.00 | 8.00 | E |
| Higher_Secondary | 22.00 | 14.00 | E |
| Graduate | 25.00 | 18.00 | E |
| Postgraduate | 35.00 | 12.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 009. AC 009 does not segment the simulation by media tier. See NORMALIZED_SCHEMA.md §4.7.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Tufanganj_Municipality | 82.00 | 16.50 | 1.00 | 0.10 | 0.40 | E | Muni 2011 pattern; urban Muslim higher than Tufanganj II rural |
| U2_Tufanganj_II_CDB_and_rural | 84.80 | 14.90 | 0.20 | 0.10 | 0.00 | A | Tufanganj II CDB 2011: 85.60% Hindu, 14.15% Muslim (A); 4 GP rural share weighted in |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit).

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Tufanganj_Municipality | 12.00 | 23.00 | 0.50 | 6.00 | 40.50 | 16.50 | 1.50 | E |
| U2_Tufanganj_II_CDB_and_rural | 4.00 | 50.50 | 1.60 | 3.70 | 24.70 | 14.90 | 0.60 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Tufanganj_Municipality | 85.00 | 55.00 | 12.00 | 94.00 | C |
| U2_Tufanganj_II_CDB_and_rural | 65.00 | 35.00 | 3.00 | 83.00 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Tufanganj_Municipality | 65.00 | 82.00 | 95.00 | 98.00 | C |
| U2_Tufanganj_II_CDB_and_rural | 24.00 | 50.00 | 87.00 | 91.00 | C |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 regional WB adjusted for Cooch Behar Rajbanshi-BJP pattern.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 57.00 | 35.50 | 1.00 | 5.00 | 1.50 | C | Rajbanshi-SC BJP swing 2019 Cooch Behar; CSDS WB Hindu baseline adjusted for North Bengal |
| Muslim | 5.00 | 68.00 | 22.00 | 4.00 | 1.00 | C | CSDS-Lokniti 2019 WB Muslim vote; AITC dominant |
| Christian | 30.00 | 50.00 | 10.00 | 8.00 | 2.00 | E | Approximation |
| Sarna_ORP | 40.00 | 40.00 | 5.00 | 12.00 | 3.00 | E | Tribal pattern North Bengal |
| Other_residual | 50.00 | 30.00 | 10.00 | 5.00 | 5.00 | E | |

### D.16 Vote × Caste (2019 LS)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 62.00 | 25.00 | 5.00 | 6.00 | 2.00 | C | Bhadralok BJP-leaning 2019; CSDS WB |
| OBC | 45.00 | 38.00 | 5.00 | 10.00 | 2.00 | C | Mixed |
| SC_total | 57.00 | 36.50 | 1.00 | 4.50 | 1.00 | C | Rajbanshi SC strong BJP swing 2019 (The Print; Cooch Behar BJP win powered by Rajbanshi vote) |
| ST_total | 42.00 | 38.00 | 3.00 | 14.00 | 3.00 | C | Tribal North Bengal mixed pattern |
| Other_Hindu_middle | 52.00 | 38.00 | 2.00 | 6.00 | 2.00 | C | |
| Muslim | 5.00 | 68.00 | 22.00 | 4.00 | 1.00 | C | Same as D.15 |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 52.00 | 42.00 | 1.50 | 3.50 | 1.00 | C | CSDS 2019 WB gender pattern; male BJP-leaning |
| Female | 47.00 | 49.00 | 0.50 | 2.50 | 1.00 | C | Female AITC advantage smaller in Cooch Behar (Rajbanshi women also BJP-leaning) |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for AC 009. See NORMALIZED_SCHEMA.md §4.7.)

---

## E. 2019 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 49.50 | A | ECI GE2019 AC-segment data; 98,776 votes / 199,554 total valid |
| AITC | 45.75 | A | 91,290 votes / 199,554 total valid |
| INC | 1.00 | A | 1,999 votes / 199,554 total valid |
| LF | 2.70 | A | RSP 5,392 + SUCI(C) 437 = 5,829 votes / 199,554 (RSP dominant left; SUCI marginal) |
| Other_NOTA | 1.05 | A | IND 1,660 / 199,554 total valid |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 009 (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Arghya Roy Pradhan | AITC | ~52% | Dhananjoy Rava | CPI(M) | ~48% (est) | ~6,182 |
| 2016 AE | Fazal Karim Miah | AITC | ~54% | Shyamal Choudhury | INC | ~44% | ~15,270 |

Notes:
- 2011: Arghya Roy Pradhan (AITC) 73,721 votes, Dhananjoy Rava (CPI-M) 67,539 votes — AITC held against Left stronghold.
- 2016: Fazal Karim Miah (AITC) 85,052 votes, Shyamal Choudhury (INC) 69,782 votes — Left collapsed, Congress as runner-up unusual; indicative of RSP-INC vote transfer dynamics.
- Both elections AITC-held; BJP did not win or come close in either 2011 or 2016 AE.
- 2019 LS saw a dramatic BJP surge (49.5%) from near-zero AE performance, driven by Rajbanshi SC community swing to BJP on CAA/citizenship mobilisation and Nisith Pramanik's Cooch Behar organisational drive.

### LS Cooch Behar (PC 02) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Renuka Sinha | AITC | ~44% | Left second; BJP ~15%; Congress ~12% |
| 2019 LS | Nisith Pramanik | BJP | ~48% | First BJP win; AITC 44.4%; massive swing from Rajbanshi SC + anti-incumbency on border issues |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- Census of India 2011 — Tufanganj II CD Block primary census abstract (religion, SC/ST, literacy, worker categories)
- Census of India 2011 — Tufanganj Municipality demographics (SC 23.03%, ST 0.41%, pop 20,998)
- Census of India 2011 — Cooch Behar district demographics
- Election Commission of India — `data/2019_AssemblySegmentLevelVotingData.csv` AC 9: BJP 98,776 · AITC 91,290 · RSP 5,392 · INC 1,999 · SUCI 437 · IND 1,660; electorate 225,957; total valid 199,554
- Delimitation Commission of India 2008 — WB Schedule (AC 009 = Tufanganj Muni + Tufanganj II CDB + 4 GPs of Tufanganj I CDB)

### Secondary sources (tier B / C)
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2019 NES — vote × demographic conditionals (WB regional rollup)
- WB District Statistical Handbook — Cooch Behar

### Tertiary / journalistic (tier D)
- The Print (2021): "Who are Rajbanshis" — Rajbanshi ~75% of SC in Cooch Behar belt; BJP appeal
- Scroll.in (2016): BJP-Cooch Behar statehood demands; Rajbanshi mobilization history
- Wikipedia — Tufanganj Assembly constituency, Cooch Behar Lok Sabha constituency, 2011/2016/2019 election results
- Wikipedia — Tufanganj I, Tufanganj II CD Blocks (Census 2011 data)

### Tier-D / E reliance flags (what to distrust)
- **Caste sub-group shares within Hindu** (D.2, C.2) — no caste census post-1931 for non-SC/ST; Rajbanshi % within SC estimated from journalistic sources; tier C/E
- **Sub-unit population split** (C.11) — Muni + CDB-II full, but 4 GPs from Tufanganj-I estimated as ~4/72 equal-weight fraction; refine with DCHB Part-A
- **Migration/birthplace** (C.16, D.3) — no public AC-level Census D-series; tier D from district pattern
- **Asset/media** (C.14, D.4, D.13) — NFHS-4 state/district-level pattern projected to AC; tier C
- **Vote × Demographic** (D.15–D.17) — CSDS 2019 WB regional rollup adjusted for North Bengal Rajbanshi BJP swing; tier C
- **Mother tongue / Rajbongshi split** (C.5, D.1) — no AC-level language census; Rajbongshi share estimated from SC proportion; tier C/E
- **Age distribution** (C.3) — district-level age pyramid; no AC-specific data; tier E

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge.
No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs. The
> validator's leakage gate exempts §H from the no-future-leakage check.

### 2021 WB Assembly Election — AC 009 Tufanganj (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Malati Rava Roy | 114,503 | 54.70% | A — ECI 2021 AE |
| AITC | Pranab Kumar Dey | 83,305 | 39.80% | A — ECI 2021 AE |
| Others | various | ~11,570 | ~5.50% | A — ECI 2021 AE |
| **BJP margin** | | **31,198 votes** | **~14.9 pp** | A |

Total valid votes: ~209,378. BJP won decisively — significant swing gain from 2019 LS.

### 2024 Lok Sabha Election — AC 009 segment within Cooch Behar LS (PC 02) (tier A)

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Nisith Pramanik | 104,302 | **48.86%** | A | data/2024_AssemblySegmentLevelVotingData.csv |
| AITC | Jagadish Chandra Barma Basunia | 97,807 | **45.82%** | A | Same |
| RSP | (candidate) | 4,316 | **2.02%** | A | Same |
| Others + NOTA | various | 6,917 | **3.24%** | A | Same (NOTA 2,128 + other parties) |
| **Electorate** | | 245,696 | — | A | Same |
| **Total valid** | | 213,470 | — | A | Computed |

Note: AITC won the overall Cooch Behar LS seat in 2024 (Jagadish Chandra Barma Basunia, +39,250 votes at LS level), but at the AC 009 segment level BJP retained a narrow lead (48.86% vs 45.82%).

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC segment shares within ±3pp of tier-A figures:
- BJP target: 48.9% ± 3pp
- AITC target: 45.8% ± 3pp
- LF+Others combined target: ~5.3% ± 3pp
