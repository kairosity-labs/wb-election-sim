# AC 004 — Cooch Behar Dakshin (GEN) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 004 Cooch Behar Dakshin as of 2019 only — it does not reference
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
| AC number | 004 | A | ECI / Delimitation Commission 2008 |
| AC name | Cooch Behar Dakshin | A | ECI |
| Reservation | GEN | A | Delimitation 2008 |
| District | Cooch Behar (Koch Bihar) | A | Delimitation 2008 |
| Sub-division | Sadar | A | WB administrative |
| LS constituency | 1 — Cooch Behar (SC reserved) | A | Delimitation 2008 |
| LS segments included | AC 1 Mekhliganj · 2 Mathabhanga · 3 Cooch Behar Uttar · 4 Cooch Behar Dakshin · 5 Sitai · 6 Sitalkuchi · 7 Tufanganj | A | Delimitation 2008 |
| AC composition | Cooch Behar Municipality (full) + Chandamari, Chilkirhat, Falimari, Ghughumari, Haribhanga, Moyamari, Patchhara, Putimari Fuleswari and Suktabari GPs of Cooch Behar I CDB | A | Delimitation 2008 |
| Geographic note | Southern part of Cooch Behar town and surrounding rural belt of Cooch Behar I block; Rasikbeel wetland to south-east | A | — |
| Sub-units used in v0 | **U1: Cooch_Behar_Municipality** (urban) · **U2: CDB_Cooch_Behar_I_rural** (9 GPs of CDB Cooch Behar I) | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~287,879 (Muni 77,935 + 9/17 GPs of CDB CB-I ~209,944) | E | Census 2011; Coochbehar Municipality website; Census 2011 CB-I CDB aggregate |
| 2019 projected population | ~312,000 | E | 8-yr compound religion-differential growth (methodology §4); ~0.96%/yr net growth |
| Sex ratio (2019, F per 1000 M) | ~958 | E | Cooch Behar district 2011 sex ratio 942; CB-I block 942; Muni urban higher ~972; AC weighted ~958 |
| 2019 estimated electorate (18+) | ~223,411 | A | ECI 2019 LS roll (from 2019_AssemblySegmentLevelVotingData.csv) |
| Estimated M / F / TG split (2019) | 51.0% M / 48.9% F / <0.05% TG | E | District sex ratio projected to 2019 |
| 2019 polling stations (estimated) | ~255 | E | Back-projection from 2019 electorate at ~875 electors/booth |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 66.50 | E | CB-I CDB 2011: 66.00% Hindu (Census via censusindia.co.in); Muni slightly higher ~70%; AC weighted ~66.5%; +0.5pp Hindu over 8yr relative to Muslim |
| Muslim | 33.10 | E | CB-I CDB 2011: 33.71% Muslim; Muni urban lower ~29%; AC weighted ~33.1%; -0.5pp vs 2011 |
| Christian | 0.20 | E | CB-I CDB 2011: 0.17% Christian; rounded up for 2019 |
| Sarna_ORP | 0.10 | E | Marginal tribal pocket; CB-I block ST 0.4% of which fraction Sarna |
| Other_residual | 0.10 | E | Sikh + Jain + Buddhist + Not_stated residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 39.80 | B | CB-I block Census 2011: SC 39.8% (censusindia.co.in); Cooch Behar district SC majority 50.17% reflects all blocks; AC CB-Dakshin coverage of CB-I block portion |
| └ Rajbanshi_SC | 36.50 | C | Rajbanshi ~75.2% of district SC pool (The Print 2021 citing 2011 data); majority SC sub-caste in CB-I |
| └ Other_SC | 3.30 | E | Residual SC (Kaibarta, Bagdi, Hari etc.) |
| **ST_total** | 0.40 | B | CB-I block Census 2011: ST 0.4% |
| **UC_bhadralok** | 5.00 | E | Brahmin/Kayastha/Baidya; limited in Cooch Behar; concentrated in municipality |
| **OBC** | 4.00 | E | OBC non-SC non-ST Hindu; smaller population in this AC |
| **Other_Hindu_middle** | 17.30 | E | Residual within Hindu (66.50 − 39.80 SC − 0.40 ST − 5.00 UC − 4.00 OBC = 17.30; Goala/Sutradhar/Tanti/unclassified Hindu) |
| **Muslim** | 33.10 | E | All sub-castes pooled; see C.1 |
| └ Muslim_Sheikh | 25.00 | D | Sheikh dominant in Cooch Behar Muslim community (Bengali Muslim peasantry) |
| └ Muslim_OBC | 5.50 | D | OBC Muslims (Jolaha, Nai, etc.) |
| └ Muslim_other | 2.60 | D | Pathan, Sayyid, Nasya-Sheikh residual |
| **Christian_plus_Sarna_plus_Other** | 0.40 | E | See C.1 Christian + Sarna_ORP + Other_residual |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.50 | E | Cooch Behar district age pyramid Census 2011; renormalized to 18+ only |
| 23_27 | 11.00 | E | |
| 28_32 | 10.50 | E | |
| 33_37 | 9.50 | E | |
| 38_42 | 9.00 | E | |
| 43_47 | 8.50 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 7.00 | E | |
| 63_67 | 9.50 | E | |
| 68 | 8.50 | E | 68+ open-ended; district pattern including elderly rural concentration |
| **Sum** | **100.00** | — | self-check (renormalized from Census age pyramid excluding 0–17) |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.05 | E | Cooch Behar district sex ratio 942 F/1000 M → 51.5% M; CB-I block 942; Muni 972; AC weighted ~958 → ~51.05% M |
| Female | 48.94 | E | |
| Third_gender | 0.01 | E | Estimated ~0.01% per WB average |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 56.50 | E | Bengali-speaking Hindu and Muslim population; Cooch Behar municipality Bengali dominant |
| Hindi | 1.00 | E | Trader community in Muni; Bihar migrant workers |
| Urdu | 1.50 | E | Muslim population some Urdu-medium; primarily Bengali-speaking however |
| Other | 2.00 | E | Residual — Santhali, Bodo fringe |
| Rajbongshi | 39.00 | E | AC-local: Rajbanshi community primary language; dominant in rural CDB-I GPs; ~75% of SC speaks Rajbongshi; adjusting for Muslim Bengali-speakers; est. ~39% of AC |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 24.50 | E | CB-I block literacy 76.56% (2011, Census); district 74.78%; Muni higher; AC weighted ~75.5% literate → ~24.5% illiterate; small improvement 2011-19 |
| Primary | 22.00 | E | Census 2011 education distribution Cooch Behar district scaled to AC |
| Middle | 19.00 | E | |
| Secondary | 15.00 | E | |
| Higher_Secondary | 10.00 | E | |
| Graduate | 7.00 | E | |
| Postgraduate | 2.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 32.00 | E | CB-I block Census 2011 main-worker share ~41% of total pop; adult-only renormalization ~32% |
| Marginal_worker | 10.00 | E | Seasonal agricultural workers; crop cycle |
| Non_worker | 38.00 | E | Housewife + elderly + retired; heavy in rural areas |
| Student | 12.00 | E | 18–22 in education; aligned with age cohort |
| Unemployed | 8.00 | E | Educated job-seekers; district level unemployment pattern |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

Pcts sum to 100 across workers only (not all personas).

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 22.00 | E | CB-I block 2011: 30,381 cultivators / 134,573 main workers = 22.6%; AC weighted ~22% |
| Agricultural_labourer | 25.00 | E | CB-I block 2011: 28,496 ag-labourers / 134,573 = 21.2%; plus marginal workers inflate share; ~25% |
| Household_industry | 5.00 | E | CB-I block pattern; weaving/handicraft small fraction |
| Manufacturing | 4.00 | E | Limited in CB district |
| Construction | 7.00 | E | Town expansion + migrant construction workers |
| Trade_retail | 12.00 | E | Cooch Behar Muni hub; market economy |
| Transport_logistics | 5.00 | E | Road-based; no major port/rail node |
| Services | 11.00 | E | Private services in Muni |
| Government_services_teachers | 6.00 | E | District headquarter town; govt employment higher than average |
| Out_migrant_worker | 3.00 | D | Limited out-migration; North Bengal retains workers |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.00 | E | Census B-04 WB rural pattern |
| Employee | 30.00 | E | Govt + organised + retail employees; district HQ inflates |
| Single_worker | 48.00 | E | Own-account cultivator + artisan + small trader |
| Family_worker | 20.00 | E | Unpaid agri-household labour |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 26.00 | C | Cooch Behar district BPL ~30% (2011 pattern); WB poverty reduction trend -4pp by 2019 → ~26% |
| Above_Poverty_Line_low_income | 36.00 | E | |
| Lower_middle | 24.00 | E | |
| Middle | 11.00 | E | |
| Upper_middle_well_off | 3.00 | E | Cooch Behar Muni professional/trader fringe |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Cooch_Behar_Municipality | 27.07 | B | Cooch Behar Muni population 77,935 / AC total 287,879 = 27.07% (Census 2011; indiastatpublications) |
| U2_CDB_Cooch_Behar_I_rural | 72.93 | B | Remainder — 9 GPs of CDB Cooch Behar I; v0 collapses 9 GPs into one rural cell |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | WB 2011: 4.3; Cooch Behar rural slightly larger; projection 4.5 |
| Nuclear_HH | 68.00 | E | NFHS-4 WB rural pattern |
| Joint_HH | 26.00 | E | |
| Extended_multi_generation | 6.00 | E | |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 27.00 | E | Census 2011 Cooch Behar district pattern; first-time-voter cohort |
| Currently_married | 64.00 | E | |
| Widowed | 8.00 | E | Concentrated in 60+, female-skewed; rural elderly concentration |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

Independent rates — do NOT sum.

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 72.00 | C | NFHS-4 WB rural 60%, urban 89%; CB district below-state average; AC weighted ~72% |
| Radio | 6.00 | C | Declining nationally; North Bengal slightly higher residual |
| Mobile_phone | 82.00 | C | NFHS-4 WB ~78%; +growth → ~82% by 2019 |
| Smartphone_with_internet | 40.00 | C | NFHS-4 baseline + Jio rollout 2016-19; rural North Bengal below WB avg |
| Computer | 7.00 | C | NFHS-4 WB rural 4%, urban 27%; AC weighted ~7% |
| Two_wheeler | 28.00 | C | NFHS-4 WB rural 18%, urban 41%; AC weighted ~28% |
| Four_wheeler | 5.00 | C | Limited; district HQ traders |
| Banking_access | 85.00 | B | PMJDY 2014- saturation; CB district pattern |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 80.00 | C | NFHS-4 WB rural 84%, urban 93%; CB district below-state; AC weighted ~80% |
| Improved_sanitation | 60.00 | C | NFHS-4 WB rural 51%, urban 84%; +Swachh Bharat 2014-19 (+12pp rural) → ~60% |
| LPG_clean_cooking_fuel | 40.00 | C | NFHS-4 WB rural 24%, urban 81%; +Ujjwala 2016-19 (+14pp rural) → AC ~40% |
| Wood_biomass_fuel | 55.00 | C | Dominant cooking fuel rural CB district |
| Other_fuel | 5.00 | C | Kerosene, dung, etc. residual |
| Electricity | 92.00 | B | Census 2011 + Saubhagya 2017-19 rollout; CB district below-average initially but Saubhagya nearly saturated |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 75.00 | D | Cooch Behar historically low out/in-migration; Rajbanshi and Bengali communities rooted; estimated ~75% native |
| WB_other_district | 8.00 | D | Some Kolkata service-class migrants in Muni; North Bengal internal migrants |
| Other_Indian_state | 3.00 | D | Bihari/UP trader fringe in Muni; construction workers |
| Bangladesh_origin | 12.00 | D | Cooch Behar is a border district; post-1947 and post-1971 Hindu Bengali refugee community; lower than Matua-belt ACs |
| Outside_India | 0.50 | E | Negligible; no significant non-Bangladesh foreign origin |
| Out_migrant | 1.50 | E | Small fraction registered here but working outside |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 42.00 | 1.00 | 0.00 | 1.50 | 55.50 | E | Rajbanshi SC dominant within Hindu (59.9% of Hindu is SC/OBC Rajbanshi-speaking); Muni Bengali Hindu fraction; weighted |
| Muslim | 92.00 | 0.50 | 4.50 | 1.50 | 1.50 | E | Bengali-Muslim peasantry dominant; small Urdu pocket; minimal Rajbongshi |
| Christian | 85.00 | 5.00 | 0.00 | 10.00 | 0.00 | E | Tiny base; Bengali + English-medium |
| Sarna_ORP | 30.00 | 0.00 | 0.00 | 40.00 | 30.00 | E | Tribal mix; Bodo/Rajbongshi fraction |
| Other_residual | 50.00 | 40.00 | 5.00 | 5.00 | 0.00 | E | Marwari/Bihari |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. 2D canonical table.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 59.85 | 0.60 | 7.52 | 6.02 | 26.01 | 0 | 0 | E | SC_total 39.8% / Hindu 66.5% = 59.85%; ST 0.40/66.5=0.60%; UC 5.0/66.5=7.52%; OBC 4.0/66.5=6.02%; residual 17.3/66.5=26.01% |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 92 | 0 | 5 | 3 | 0 | 0 | E | Tribal sub-castes mostly ST |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 70.00 | 8.00 | 3.50 | 17.00 | 0.50 | 1.00 | D | Hindu Rajbanshi community native; Hindu Bengali refugees from Bangladesh 1947/1971 in CB district |
| Muslim | 88.00 | 6.00 | 2.00 | 2.50 | 1.00 | 0.50 | D | Bengali-Muslim peasantry largely native; small Bangladesh-origin trickle |
| Christian | 80.00 | 10.00 | 5.00 | 5.00 | 0.00 | 0.00 | E | Mixed background |
| Sarna_ORP | 90.00 | 5.00 | 5.00 | 0.00 | 0.00 | 0.00 | E | Indigenous tribal, native |
| Other_residual | 30.00 | 15.00 | 50.00 | 5.00 | 0.00 | 0.00 | E | Marwari/Bihari mostly other-state |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 74.00 | 42.00 | 87.00 | E | NFHS-4 WB religion gap pattern; Hindu slightly higher asset access |
| Muslim | 67.00 | 34.00 | 80.00 | E | Muslim rural CB slightly lower than Hindu |
| Christian | 78.00 | 50.00 | 90.00 | E | Approximation |
| Sarna_ORP | 55.00 | 20.00 | 70.00 | E | Tribal lower asset access |
| Other_residual | 88.00 | 65.00 | 95.00 | E | Marwari trader fringe — high asset |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 8.00 | 12.00 | 15.00 | 20.00 | 18.00 | 19.00 | 8.00 | E |
| SC_total | 26.00 | 23.00 | 20.00 | 16.00 | 9.00 | 5.00 | 1.00 | E |
| ST_total | 30.00 | 25.00 | 20.00 | 14.00 | 7.00 | 3.00 | 1.00 | E |
| OBC | 20.00 | 22.00 | 20.00 | 18.00 | 11.00 | 7.00 | 2.00 | E |
| Other_Hindu_middle | 18.00 | 22.00 | 20.00 | 18.00 | 11.00 | 8.00 | 3.00 | E |
| Muslim | 30.00 | 25.00 | 21.00 | 14.00 | 6.00 | 3.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender). 5-year cohorts.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 14.00 | 12.00 | E |
| 23_27 | 13.00 | 10.00 | E |
| 28_32 | 12.00 | 8.00 | E |
| 33_37 | 10.00 | 6.00 | E |
| 38_42 | 9.00 | 5.00 | E |
| 43_47 | 8.00 | 4.00 | E |
| 48_52 | 7.00 | 3.00 | E |
| 53_57 | 6.00 | 2.00 | E |
| 58_62 | 5.00 | 2.00 | E |
| 63_67 | 4.00 | 1.50 | E |
| 68 | 3.00 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender). 5-year cohorts.

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8.00 | 30.00 | E |
| 23_27 | 42.00 | 80.00 | E |
| 28_32 | 82.00 | 92.00 | E |
| 33_37 | 92.00 | 90.00 | E |
| 38_42 | 93.00 | 88.00 | E |
| 43_47 | 92.00 | 85.00 | E |
| 48_52 | 91.00 | 78.00 | E |
| 53_57 | 90.00 | 68.00 | E |
| 58_62 | 88.00 | 55.00 | E |
| 63_67 | 80.00 | 40.00 | E |
| 68 | 72.00 | 28.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 30.00 | 65.00 | C | Rural agri baseline; below-state in CB |
| Agricultural_labourer | 22.00 | 55.00 | C | Lowest income bracket |
| Household_industry | 35.00 | 70.00 | C | |
| Manufacturing | 48.00 | 80.00 | C | |
| Construction | 42.00 | 72.00 | C | |
| Trade_retail | 62.00 | 85.00 | C | Muni concentrated |
| Transport_logistics | 55.00 | 78.00 | C | |
| Services | 68.00 | 88.00 | C | |
| Government_services_teachers | 82.00 | 92.00 | C | Highest; district HQ |
| Out_migrant_worker | 65.00 | 78.00 | D | Smartphone-heavy when outside |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 35.00 | 1.00 | E |
| Primary | 38.00 | 3.00 | E |
| Middle | 36.00 | 5.00 | E |
| Secondary | 30.00 | 8.00 | E |
| Higher_Secondary | 24.00 | 13.00 | E |
| Graduate | 26.00 | 16.00 | E |
| Postgraduate | 36.00 | 12.00 | E |

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Sub-unit codes use Un_ prefix matching C.11.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Cooch_Behar_Municipality | 70.00 | 28.00 | 0.80 | 0.10 | 1.10 | E | Cooch Behar Muni more Hindu-urban; lower Muslim fraction than rural CB-I block |
| U2_CDB_Cooch_Behar_I_rural | 64.50 | 35.10 | 0.10 | 0.10 | 0.20 | E | Rural CB-I block: 66% Hindu, 33.71% Muslim (Census 2011 adjusted slightly for 2019 trend) |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Parent caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Cooch_Behar_Municipality | 10.00 | 32.00 | 0.20 | 6.00 | 23.80 | 28.00 | 0.00 | E |
| U2_CDB_Cooch_Behar_I_rural | 3.00 | 43.00 | 0.50 | 3.50 | 14.00 | 35.10 | 0.90 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Cooch_Behar_Municipality | 88.00 | 58.00 | 18.00 | 92.00 | C |
| U2_CDB_Cooch_Behar_I_rural | 64.00 | 31.00 | 2.50 | 81.00 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Cooch_Behar_Municipality | 75.00 | 90.00 | 95.00 | 99.00 | C |
| U2_CDB_Cooch_Behar_I_rural | 25.00 | 47.00 | 72.00 | 88.00 | C |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 regional WB rollup adapted for Cooch Behar context.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 58.00 | 32.00 | 2.50 | 5.50 | 2.00 | C | CSDS 2019 WB Hindu vote pattern; North Bengal Hindu (incl. Rajbanshi) BJP-leaning in 2019 |
| Muslim | 5.00 | 68.00 | 14.00 | 10.00 | 3.00 | C | CSDS 2019 WB Muslim vote; Cooch Behar Muslim bloc AITC-heavy; INC residual stronger in CB than South WB |
| Christian | 25.00 | 55.00 | 10.00 | 7.00 | 3.00 | E | Approximation |
| Sarna_ORP | 40.00 | 40.00 | 5.00 | 12.00 | 3.00 | E | Tribal small base; split |
| Other_residual | 45.00 | 35.00 | 10.00 | 5.00 | 5.00 | E | Marwari/Bihari — BJP-leaning |

### D.16 Vote × Caste (2019 LS)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 58.00 | 28.00 | 6.00 | 6.00 | 2.00 | C | CSDS 2019 WB UC pattern |
| OBC | 40.00 | 38.00 | 8.00 | 11.00 | 3.00 | C | Mixed; North Bengal OBC less BJP-consolidated than South WB |
| SC_total | 58.00 | 32.00 | 3.00 | 5.00 | 2.00 | C | Rajbanshi SC swing to BJP 2019; Cooch Behar key BJP base; CSDS WB SC pattern |
| ST_total | 42.00 | 36.00 | 5.00 | 14.00 | 3.00 | C | ST small base; split |
| Other_Hindu_middle | 52.00 | 34.00 | 4.00 | 7.00 | 3.00 | C | |
| Muslim | 5.00 | 68.00 | 14.00 | 10.00 | 3.00 | C | Same as D.15 Muslim |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 50.00 | 40.00 | 3.00 | 5.00 | 2.00 | C | CSDS 2019 WB gender gap pattern; Cooch Behar male leaning BJP slightly more |
| Female | 45.00 | 48.00 | 2.00 | 4.00 | 1.00 | C | Women TMC advantage in 2019; pre-LB baseline |

---

## E. 2019 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 47.79 | A | ECI 2019 LS Form-20 AC-segment; 86431 votes / 180842 total = 47.79% |
| AITC | 44.46 | A | ECI 2019 LS Form-20 AC-segment; 80410 votes / 180842 = 44.46% |
| INC | 2.03 | A | ECI 2019 LS AC-segment; 3667 votes / 180842 = 2.03% |
| LF | 4.28 | A | AIFB 7197 + SUCI(C) 552 = 7749 votes / 180842 = 4.28%; AIFB dominant left party in Cooch Behar |
| Other_NOTA | 1.43 | A | KPPU + WPOI + AMB + 3 IND = 2585 / 180842 = 1.43% |
| **Sum** | **99.99** | — | self-check (rounding; within ±0.5) |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 004 (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Akshay Thakur | AIFB | ~49.5 | Abdul Jalil Ahmed | AITC | ~48.0 | 2,863 |
| 2016 AE | Mihir Goswami | AITC | ~46.2 | Debasis Banik | AIFB | ~36.1 | 18,195 |

Notes: 2011 was a rare AIFB win in an AITC wave year — unusual for Cooch Behar Dakshin. 2016 saw a big AITC swing nationally in WB and Goswami flipped the seat. 2019 LS saw BJP surge in the constituency (+~12pp over any AITC tally). BJP had been consolidating Rajbanshi SC vote since 2017. Total valid votes 2016 AE = 179,173.

### LS 1 — Cooch Behar Lok Sabha historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Renuka Sinha | AITC | ~42 | TMC won; CPI(M) competed; BJP nascent |
| 2019 LS | Nisith Pramanik | BJP | ~48 | BJP won 731,594 votes; AITC Paresh Chandra Adhikary 677,363; margin 54,231 votes (4.8pp at LS level) |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- Election Commission of India — 2019_AssemblySegmentLevelVotingData.csv (AC 4 vote tallies, electorate 223,411)
- Election Commission of India — 2016 AE, 2011 AE results for AC 004 Cooch Behar Dakshin
- ECI 2019 LS Cooch Behar PC result (Nisith Pramanik BJP win)
- Delimitation Commission of India 2008 — WB Schedule (AC 4 = Cooch Behar Muni + 9 GPs of CB-I CDB)
- Coochbehar Municipality official website — Muni population 77,935 (Census 2011)

### Secondary sources (tier B / C)
- Census of India 2011 — Cooch Behar I CDB (censusindia.co.in): population 326,558, Hindu 66%, Muslim 33.71%, SC 39.8%, ST 0.4%, literacy 76.56%, sex ratio 942
- Census of India 2011 — Cooch Behar district (census2011.co.in): district SC 50.17%, Hindu 74.06%, Muslim 25.54%, literacy 74.78%
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline
- CSDS-Lokniti 2019 NES post-poll — vote × religion/caste/gender cross-tabs (WB regional rollup)
- indiastatpublications.com — Coochbehar Dakshin Assembly demographic summary; constituency SC 36.19%, rural/urban 72.93/27.07%

### Tertiary / journalistic (tier D)
- The Print (2021) — "Who are Rajbanshis" — Rajbanshi ~75.2% of CB district SC pool; 91% workers in agriculture
- DNA India — 2019 LS Cooch Behar result detail
- mapsofindia.com — 2016 AE result breakdown Cooch Behar Dakshin
- Wikipedia — Cooch Behar Dakshin Assembly constituency; Cooch Behar Lok Sabha constituency; Mihir Goswami MLA

### Tier-D / E reliance flags (what to distrust)
- **Religion shares** (C.1): Muni religion data not available separately; CB-I block aggregate used with urban/rural adjustment → tier E
- **Caste sub-group shares** (C.2, D.2): No caste census post-1931 for non-SC/ST; Rajbanshi dominance from district-level journalistic sources → tier C/D
- **Mother tongue Rajbongshi share** (C.5): inferred from Rajbanshi SC fraction + demographic linguistic overlap; no AC-level mother tongue census data → tier E
- **Migration/birthplace shares** (C.16, D.3): no public AC-level Census D-series; estimated from district pattern → tier D
- **GP-level data** (D.11–D.14): collapsed to 2 sub-units (Muni + CDB-rural-share); refine when DCHB Part-A accessible for CB-I GPs
- **Asset/media** (C.14, D.4, D.13): NFHS-4 state-level pattern projected to AC → tier C
- **Vote × Demographic** (D.15–D.17): CSDS 2019 WB regional rollup → tier C

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge.
No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2021 WB Assembly Election — AC 004 Cooch Behar Dakshin (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Nikhil Ranjan Dey | 91,560 | 46.83% | A — ECI 2021 AE (oneindia.com) |
| AITC | Avijit De Bhowmik | 86,629 | 44.31% | A — ECI 2021 AE |
| Others | various | ~6,900 | ~3.53% | D — residual |
| **BJP margin** | | **4,931 votes** | **2.52 pp** | A |

BJP held seat in 2021 with reduced margin vs 2019 LS indicator; AITC recovered slightly.

### 2024 Lok Sabha Election — AC 004 segment within Cooch Behar LS (PC 1)

Per 2024_AssemblySegmentLevelVotingData.csv (to be populated in 2024 sprint).

### Calibration test

The simulator is considered validated on this seat if it reproduces 2021 AE AC segment shares within ±3pp of tier-A figures (BJP / AITC combined) and 2024 LS segment shares similarly.
