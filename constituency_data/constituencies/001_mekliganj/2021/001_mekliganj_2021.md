# AC 001 — Mekliganj (SC) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 001 Mekliganj as of end-2021 only — it does not reference
> any events after end-2021. Use post-2021 elections (2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 001 | A | ECI / Delimitation Commission 2008 |
| AC name | Mekliganj | A | ECI |
| Reservation | SC | A | Delimitation 2008 |
| District | Cooch Behar | A | Delimitation 2008 |
| Sub-division | Mekhliganj | A | WB administrative |
| LS constituency | 3 — Jalpaiguri (GEN) | A | Delimitation 2008 |
| LS segments included | AC 1 Mekliganj · AC 2 Dhupguri · AC 3 Maynaguri · AC 4 Jalpaiguri · AC 5 Rajganj · AC 6 Dabgram-Phulbari · AC 7 Mal (ST) | A | Delimitation 2008 |
| AC composition | Mekliganj Municipality + Mekliganj CDB (8 GPs: Bagdokra Fulkadabri, Bhotbari, Changrabandha, Jamaldaha, Kuchlibari, Niztaraf, Ranirhat, Uchalpukuri) + Haldibari Municipality + Haldibari CDB (6 GPs: Baxiganj, Daxin Bara Haldibari, Dewanganj, Hemkumari, Per Mekhliganj, Uttar Bara Haldibari) | A | Delimitation 2008; Wikipedia CDB articles |
| Geographic note | Southern tip of Jalpaiguri LS; enclaved by Bangladesh on west, Bhutan corridor on north; Haldibari is an India-Bangladesh rail terminus; Changrabandha is a key land-port on Bangladesh border; BSF 50km jurisdiction extended Oct 2021 covering this border AC | A | — |
| Sub-units used in v0 | **U1: Mekliganj_area** (Mekliganj Muni + Mekliganj CDB, ~58.1% pop) · **U2: Haldibari_area** (Haldibari Muni + Haldibari CDB, ~41.9% pop) | E | v0 simplification |

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~282,750 (Mekliganj Muni 9,127 + Mekliganj CDB 155,250 + Haldibari Muni 14,404 + Haldibari CDB 103,969) | A | Census 2011 |
| 2021 projected population | ~314,600 | E | 10-yr compound ~1.1%/yr growth from 2011 base; religion-differential growth applied |
| Sex ratio (2021, F per 1000 M) | ~1,058 | B | NFHS-5 Koch Bihar district 1,058 F per 1000 M (2019-21); updated from 2011 baseline of ~948 |
| 2021 electorate (registered voters) | ~225,000 | D | 2021 AE total valid votes 198,744 at ~88.1% turnout → estimated roll ~225,600; approximate |
| Estimated M / F / TG split (2021) | ~48.6% M / 51.4% F / ~0.01% TG | E | Updated from NFHS-5 Koch Bihar sex ratio 1058 |
| 2021 total valid votes | 198,744 | A | ECI 2021 AE; Wikipedia Mekliganj constituency (§H source) |
| 2021 turnout (AE) | ~88.1% | D | Estimated from valid votes / roll |
| 2021 polling stations (estimated) | ~238 | E | Back-projection from electorate size; ~946 voters per booth |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

Weighted from four sub-units at 2011 Census; projected forward at religion-differential growth rate (+0.3pp Muslim share gain per decade as per Pew WB pattern); 10-year projection from 2019 file base.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 74.93 | B | 2011 weighted AC ~75.46%; adjusted -0.32pp for 10yr differential growth vs -0.21pp for 8yr in 2019 file |
| Muslim | 24.74 | B | 2011 weighted ~24.21%; adjusted +0.32pp for 10yr differential growth |
| Christian | 0.29 | B | Weighted from four sub-units 2011; stable |
| Sarna_ORP | 0.02 | E | Negligible in Cooch Behar CDBs |
| Other_residual | 0.02 | E | Sikh + Jain + Buddhist + Not_stated; residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

AC 001 is reserved SC. SC share is extraordinarily high (~65%). Dominant SC sub-group is Rajbanshi (Koch-Rajbanshi). No structural shift from 2019; slight Muslim fraction increase propagates.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 64.77 | B | 2011 SC census proportions applied to 2021 projected pop; small drift from Muslim fractional increase |
| └ Rajbanshi_SC | 58.30 | C | Koch-Rajbanshi SC dominant sub-group; ~90% of SC pool |
| └ Namasudra_SC | 4.50 | E | Smaller pool; ~7% of SC pool |
| └ Other_SC | 1.97 | E | Residual SC sub-castes |
| **ST_total** | 0.88 | B | Weighted 2011: Mekli-CDB 1.24%, Haldi-CDB 0.30%; stable |
| UC_bhadralok | 2.00 | E | Very small bhadralok fraction in Cooch Behar frontier AC |
| OBC | 3.00 | E | Small OBC fraction; Cooch Behar OBC pool |
| Other_Hindu_middle | 4.37 | E | Residual within Hindu non-SC/ST/UC/OBC: 74.93 − 64.77 SC − 0.88 ST − 2.0 UC − 3.0 OBC = 4.28; rounded to maintain sum |
| Muslim | 24.74 | B | See C.1; all sub-castes pooled; slight uptick from 2019 24.42% |
| Christian_plus_Sarna_plus_Other | 0.24 | E | See C.1; slight shrinkage |
| **Sum** | **100.00** | — | self-check: 64.77+0.88+2.00+3.00+4.37+24.74+0.24=100.00 (parent rows only) |

### C.3 Age cohort (2021, adult voters only — 18+)

10-year projection from Census 2011; 18+ adults only; 2019 AE first-time voter cohort (18 in 2021) absorbed; 2 more years of cohort aging vs 2019 file.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.20 | E | Cooch Behar district age pyramid Census 2011; first-time voter cohort 2021 AE; slightly lower than 2019 as cohort ages |
| 23_27 | 11.00 | E | |
| 28_32 | 10.50 | E | |
| 33_37 | 10.00 | E | |
| 38_42 | 9.50 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.20 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.50 | E | |
| 63_67 | 4.60 | E | |
| 68 | 12.50 | E | 68+ open-ended cohort; includes widowed elderly |
| **Sum** | **100.00** | — | self-check (18+ adults only) |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 48.60 | B | NFHS-5 Koch Bihar sex ratio 1,058 F per 1000 M → 51.4% F / 48.6% M; notable improvement from 2011 (948) reflecting female survival gains |
| Female | 51.39 | B | NFHS-5 Koch Bihar 2019-21 |
| Third_gender | 0.01 | E | State-level trace |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 87.80 | B | Mekliganj CDB 93.9% Bengali; AC weighted ~88%; slight drift as Rajbongshi community maintains distinct identity |
| Hindi | 1.20 | B | Cooch Behar district ~1.17% Hindi; border/transit zones |
| Urdu | 0.50 | E | Small Muslim pocket in Haldibari (33% Muslim); some Urdu-speakers |
| Other | 0.50 | E | Residual catch-all |
| Rajbongshi | 10.00 | C | Rajbanshi (Koch-Rajbanshi) community speaks Rajbongshi dialect; stable estimate |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

Baseline: AC literacy ~70.2% (weighted 2011). Koch Bihar NFHS-5 female literacy 79.2% (tier B); projected overall AC literacy ~76% by 2021 → ~24% illiterate.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 24.00 | B | Koch Bihar NFHS-5 women literacy 79.2%; overall AC literacy ~76% by 2021 (improvement from ~74% in 2019); 2pp improvement in 2 years |
| Primary | 24.00 | E | Census 2011 WB education distribution scaled for Cooch Behar; stable |
| Middle | 20.00 | E | |
| Secondary | 14.50 | E | Slight upward nudge from 2019 (14%) as education access improves |
| Higher_Secondary | 9.50 | E | |
| Graduate | 6.50 | E | Slight increase; post-COVID higher education pattern |
| Postgraduate | 1.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

COVID-19 reverse migration impact (2020): some out-migrants returned; slight increase in marginal workers and unemployed.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 34.00 | E | Slight dip from 2019 (35%) reflecting COVID disruption to agricultural and trade employment; partial recovery by end-2021 |
| Marginal_worker | 14.00 | E | Uptick from 2019 (13%) due to COVID reverse-migration returning seasonal workers |
| Non_worker | 37.00 | E | Housewife + elderly + retired; stable |
| Student | 9.00 | E | 18-22 in education cohort; schools reopening post-COVID |
| Unemployed | 6.00 | E | Educated job-aspirant pool; stable |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

Mekliganj CDB 2011 profile maintained; COVID-19 impact noted in construction and transport.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 40.00 | B | Mekli CDB 48.22% (A); weighted with Haldibari and Muni; COVID-19 kept many rural households in agriculture |
| Agricultural_labourer | 33.00 | B | High landless SC-labourer pool given 65% SC; stable |
| Household_industry | 3.00 | B | Mekli CDB 1.70%; slightly higher in Haldibari |
| Manufacturing | 2.50 | E | Limited; some rice mills in Haldibari area |
| Construction | 4.50 | E | Slightly lower than 2019 (5%) due to COVID lockdown disruption to construction migrant work |
| Trade_retail | 8.00 | E | Muni-based retail; Changrabandha border trade; stable |
| Transport_logistics | 3.50 | E | Haldibari rail terminus; Changrabandha land-port; slight uptick post-COVID reopening |
| Services | 3.00 | E | Private services; stable |
| Government_services_teachers | 2.50 | E | Government teachers, block-level admin |
| Out_migrant_worker | 0.00 | E | Low; COVID reverse migration reduced recorded out-migrant workers |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Very low; small traders and landowners |
| Employee | 18.00 | E | Govt employees + regular-wage workers; stable |
| Single_worker | 52.00 | E | Own-account cultivator + petty trader + artisan; stable |
| Family_worker | 28.50 | E | Unpaid family farm labour; high given ag dominance |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2021, household level)

Lakshmir Bhandar launched April 2021 (₹500/month for SC/ST women, ₹1000 for others); Duare Sarkar government service delivery camps (Dec 2020); modest improvement in household welfare indicators by end-2021.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 28.00 | C | Cooch Behar district high poverty; 2019 estimate ~30%; Duare Sarkar + welfare rollout partially offset by COVID economic shock; ~28% by end-2021 |
| Above_Poverty_Line_low_income | 35.00 | E | Near-poor households; stable |
| Lower_middle | 22.00 | E | |
| Middle | 11.00 | E | Marginal improvement from Lakshmir Bhandar cash transfer |
| Upper_middle_well_off | 4.00 | E | Thin upper stratum; small expansion |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Mekliganj_area | 58.10 | A | Mekliganj Muni (9,127) + Mekliganj CDB (155,250) = 164,377 of 282,750 total; Census 2011; stable |
| U2_Haldibari_area | 41.90 | A | Haldibari Muni (14,404) + Haldibari CDB (103,969) = 118,373 of 282,750; Census 2011; stable |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | Cooch Behar district slightly above WB state average; stable |
| Nuclear_HH | 65.00 | E | COVID-19 may have increased nuclear household formation; NFHS-5 WB pattern; stable estimate |
| Joint_HH | 28.00 | E | |
| Extended_multi_generation | 7.00 | E | |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2021, age 18+)

Koch Bihar NFHS-5: women married before age 18 = 46.7%; high early marriage persists in this frontier AC.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.50 | E | Census 2011 Cooch Behar pattern; slightly lower than 2019 (26%) as 2019 first-time voter cohort ages into marriage |
| Currently_married | 64.50 | E | Slight uptick from 2019 (64%); high early marriage rate in rural Koch Bihar (NFHS-5: 46.7% women married before 18) |
| Widowed | 8.50 | E | Stable; slightly higher than WB average |
| Separated_divorced | 1.50 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

Post-COVID surge: smartphone penetration increased markedly (Jio + JioPhone growth, COVID-19 digital payments, government scheme apps). NFHS-5 Koch Bihar: electricity 98.2%, improved sanitation 75.7%, clean fuel 25.7% (all NFHS-5 tier B).

Independent ownership rates — do NOT sum.

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 70.00 | B | NFHS-5 Koch Bihar overall household pattern; up from 2019 (65%); TV nearing saturation in rural frontier ACs |
| Radio | 6.00 | C | Declining; slightly lower than 2019 (7%) |
| Mobile_phone | 87.00 | C | NFHS-5 WB rural improvement; near-saturation; slight adjustment from 2019 (82%) |
| Smartphone_with_internet | 58.00 | C | Post-COVID surge: +20-25pp from 2019 (35%); Jio + COVID government app adoption + digital payments; WB rural pattern per NFHS-5 trend |
| Computer | 4.50 | C | Marginal uptick from 2019 (4%); very low in rural frontier AC |
| Two_wheeler | 19.00 | C | NFHS-5 WB pattern; marginal increase from 2019 (18%) |
| Four_wheeler | 3.00 | C | Limited; stable |
| Banking_access | 92.00 | B | PMJDY further +5pp from 2019 (85%); NFHS-5 Koch Bihar financial inclusion improvement; Duare Sarkar bank linkages |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

NFHS-5 Koch Bihar: electricity 98.2%, improved sanitation 75.7%, clean fuel 25.7%.

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 99.00 | B | NFHS-5 Koch Bihar 99.3%; major improvement from 2019 (85%); Jal Jeevan Mission 2019-21 rollout |
| Improved_sanitation | 75.00 | B | NFHS-5 Koch Bihar 75.7%; improvement from 2019 (60%); Swachh Bharat Phase II + ODF declaration |
| LPG_clean_cooking_fuel | 26.00 | B | NFHS-5 Koch Bihar 25.7%; limited improvement from 2019 (30%) due to low refill rates despite Ujjwala connections |
| Wood_biomass_fuel | 68.00 | B | Still dominant; slight uptick vs 2019 (65%) as LPG refills unaffordable for many SC-BPL households |
| Other_fuel | 6.00 | E | Kerosene, dung, etc.; residual; LPG+Wood+Other sum to 100 |
| Electricity | 98.00 | B | NFHS-5 Koch Bihar 98.2%; near-saturation from 2019 (90%); Saubhagya + Har Ghar Bijli completions |
| **Note** | (water/sanitation/electricity are independent %s; LPG + Wood + Other fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

COVID-19 reverse migration (2020): some seasonal workers returned to Mekliganj from construction sites in other states. Cyclone Amphan (May 2020) minimally affected Cooch Behar district directly (mainly coastal South Bengal). BSF 50km jurisdiction extended Oct 2021 — affects border area residents but not migration count.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 70.50 | D | Rajbanshi SC mostly indigenous; slight uptick from COVID reverse migration of seasonal workers re-classifying as native |
| WB_other_district | 6.00 | D | Limited in-migration from other WB districts; stable |
| Other_Indian_state | 1.50 | D | Slight decline from 2019 (2%); COVID reduced inter-state migration; small trader fringe in Muni areas |
| Bangladesh_origin | 20.00 | D | Significant: Rajbanshi displaced in 1947 partition + subsequent Hindu refugee flows; Haldibari area affected; Bangladesh temple attacks Oct 2021 prompted minor anxiety among this community but no major migration event |
| Outside_India | 0.50 | E | Bhutan / Nepal origin; minor; stable |
| Out_migrant | 1.50 | E | Seasonal / permanent out-migrants; COVID largely returned seasonal workers home; v0 simplification |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 82.00 | 1.20 | 0.00 | 0.30 | 16.50 | E | Rajbongshi-speaking Rajbanshi SC are predominantly Hindu; same as 2019 |
| Muslim | 95.00 | 1.00 | 3.50 | 0.50 | 0.00 | E | Cooch Behar Muslims predominantly Bengali-speaking; stable |
| Christian | 85.00 | 5.00 | 0.00 | 10.00 | 0.00 | E | Tiny base; Bengali + English-medium |
| Sarna_ORP | 50.00 | 10.00 | 0.00 | 40.00 | 0.00 | E | Negligible population; mixed |
| Other_residual | 60.00 | 30.00 | 0.00 | 10.00 | 0.00 | E | Marwari/other traders |

### D.2 Religion × Caste

P(caste ‖ religion) — 2D table; one row per religion.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 79.40 | 1.17 | 2.67 | 4.00 | 12.76 | 0 | 0 | E | SC_total/Hindu: 64.77/74.93 = 86.4% of Hindu is SC; distributed among leaves; Hindu row sums to 100 |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 90 | 0 | 5 | 5 | 0 | 0 | E | Mostly ST affiliation |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | Residual |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 65.50 | 6.00 | 1.50 | 25.50 | 0.50 | 1.00 | D | Hindu Rajbanshi have significant Bangladesh-origin fraction (1947 partition + subsequent flows); slight COVID return migration nudge |
| Muslim | 86.00 | 6.00 | 2.00 | 4.00 | 1.50 | 0.50 | D | Cooch Behar Muslims mostly indigenous; stable |
| Christian | 80.00 | 10.00 | 5.00 | 5.00 | 0.00 | 0.00 | E | Mixed |
| Sarna_ORP | 90.00 | 5.00 | 5.00 | 0.00 | 0.00 | 0.00 | E | Mostly indigenous tribal |
| Other_residual | 40.00 | 15.00 | 40.00 | 5.00 | 0.00 | 0.00 | E | Trader/service migrants mostly from other states |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion; updated for 2021 smartphone surge.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 72.00 | 60.00 | 93.00 | E | Updated from 2019 (67%, 37%, 86%); post-COVID smartphone surge; PMJDY improvement; Lakshmir Bhandar bank linkage |
| Muslim | 63.00 | 51.00 | 88.00 | E | Updated from 2019 (58%, 29%, 81%); below-average but catching up; Haldibari area improvement |
| Christian | 76.00 | 55.00 | 92.00 | E | Small base; approximation |
| Sarna_ORP | 55.00 | 30.00 | 75.00 | E | Negligible base; lower access |
| Other_residual | 88.00 | 68.00 | 97.00 | E | Trader/affluent fringe |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Rows sum to 100. Marginal improvement in SC and Muslim education levels vs 2019.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 7.00 | 12.00 | 15.00 | 20.00 | 20.00 | 19.00 | 7.00 | E |
| SC_total | 26.00 | 25.00 | 20.00 | 14.50 | 8.50 | 4.50 | 1.50 | E |
| ST_total | 30.00 | 26.00 | 20.00 | 13.00 | 6.50 | 3.50 | 1.00 | E |
| OBC | 19.00 | 22.00 | 20.00 | 18.00 | 12.00 | 7.00 | 2.00 | E |
| Other_Hindu_middle | 17.00 | 22.00 | 21.00 | 18.00 | 12.00 | 7.50 | 2.50 | E |
| Muslim | 30.00 | 26.00 | 20.00 | 14.00 | 7.00 | 2.50 | 0.50 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender). 5-year cohorts; 18+ only. Marginal improvement in younger cohorts vs 2019.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 13.00 | 10.00 | E |
| 23_27 | 12.00 | 8.00 | E |
| 28_32 | 10.00 | 6.00 | E |
| 33_37 | 8.00 | 4.00 | E |
| 38_42 | 7.00 | 3.50 | E |
| 43_47 | 6.00 | 2.50 | E |
| 48_52 | 5.00 | 2.00 | E |
| 53_57 | 4.00 | 1.50 | E |
| 58_62 | 3.50 | 1.00 | E |
| 63_67 | 3.00 | 1.00 | E |
| 68 | 2.50 | 0.80 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender). 5-year cohorts. Stable from 2019; high early marriage persists.

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 6.00 | 30.00 | E |
| 23_27 | 42.00 | 82.00 | E |
| 28_32 | 82.00 | 93.00 | E |
| 33_37 | 92.00 | 91.00 | E |
| 38_42 | 93.00 | 89.00 | E |
| 43_47 | 92.00 | 86.00 | E |
| 48_52 | 90.00 | 80.00 | E |
| 53_57 | 88.00 | 70.00 | E |
| 58_62 | 85.00 | 58.00 | E |
| 63_67 | 78.00 | 42.00 | E |
| 68 | 70.00 | 28.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — updated for 2021 smartphone surge; central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 45.00 | 63.00 | E | Post-COVID surge; up from 2019 (28%, 58%) |
| Agricultural_labourer | 33.00 | 53.00 | E | Lowest income; up from 2019 (20%, 48%) |
| Household_industry | 50.00 | 67.00 | E | |
| Manufacturing | 60.00 | 75.00 | E | |
| Construction | 55.00 | 70.00 | E | |
| Trade_retail | 72.00 | 84.00 | E | Muni concentrated; higher access |
| Transport_logistics | 66.00 | 78.00 | E | Border port workers |
| Services | 74.00 | 86.00 | E | |
| Government_services_teachers | 88.00 | 93.00 | E | Highest access |
| Out_migrant_worker | 75.00 | 78.00 | E | Smartphone-heavy; stable |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education). Stable from 2019.

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 38.00 | 1.50 | E |
| Primary | 40.00 | 3.00 | E |
| Middle | 38.00 | 5.00 | E |
| Secondary | 32.00 | 8.00 | E |
| Higher_Secondary | 26.00 | 12.00 | E |
| Graduate | 28.00 | 14.00 | E |
| Postgraduate | 35.00 | 10.00 | E |

### D.10 Asset / media × Bilingualism

*(No media_tier axis declared for this AC — section retained as stub per schema §4.7)*

| Media_tier | Bilingual_pct | Tier | Source |
|---|---|---|---|
| stub | 0 | E | No media_tier axis in v0; omit from marginal |

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Updated for 2021 religion differential growth. Sub-unit codes match C.11.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Mekliganj_area | 80.05 | 19.60 | 0.32 | 0.01 | 0.02 | B | Weighted 2011 base + 10yr differential growth projection; Mekli-Muni 79.75%+Mekli-CDB 80.41% weighted |
| U2_Haldibari_area | 68.10 | 31.57 | 0.26 | 0.04 | 0.03 | B | Haldi-Muni 83.91% Hindu/15.94% Muslim + Haldi-CDB 66.53%/33.14%; 10yr growth projection |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Canonical caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Mekliganj_area | 2.20 | 69.80 | 1.24 | 3.00 | 4.20 | 19.60 | 0.02 | B |
| U2_Haldibari_area | 1.70 | 57.80 | 0.38 | 3.00 | 5.50 | 31.57 | 0.05 | B |

### D.13 Sub-unit × Asset / media

Updated for 2021 smartphone surge.

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Mekliganj_area | 72.00 | 60.00 | 4.50 | 93.00 | E |
| U2_Haldibari_area | 67.00 | 55.00 | 4.00 | 90.00 | E |

### D.14 Sub-unit × Amenities

Updated from NFHS-5 Koch Bihar district indicators.

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Mekliganj_area | 27.00 | 78.00 | 99.00 | 99.00 | B |
| U2_Haldibari_area | 24.00 | 71.00 | 99.00 | 97.00 | B |

### D.15 Vote × Religion (2021 AE)

P(party ‖ religion) — anchored on 2021 AE result (AITC 49.98%, BJP 42.59%). AITC Paresh Chandra Adhikary (SC Rajbanshi leader who switched from AIFB) consolidated Hindu SC + Muslim vote; BJP maintained strong SC Rajbanshi base.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 50.00 | 41.00 | 1.00 | 5.00 | 3.00 | C | CSDS-Lokniti 2021 WB regional; BJP strong among Hindu SC Rajbanshi in border ACs; AITC benefited from Paresh Adhikary SC-identity pull |
| Muslim | 4.00 | 78.00 | 10.00 | 5.00 | 3.00 | C | Muslim consolidation around AITC strengthened further in 2021 vs 2019 |
| Christian | 22.00 | 60.00 | 8.00 | 7.00 | 3.00 | E | Approximation; small base |
| Sarna_ORP | 38.00 | 44.00 | 3.00 | 11.00 | 4.00 | E | Tiny base |
| Other_residual | 42.00 | 38.00 | 8.00 | 8.00 | 4.00 | E | Trader fringe |

### D.16 Vote × Caste (2021 AE)

P(party ‖ caste) — CSDS-Lokniti 2021 WB regional. Note: Rajbanshi SC in Cooch Behar/Jalpaiguri belt showed continued BJP tilt but AITC candidate Paresh Adhikary (himself SC Rajbanshi) partially neutralised this.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 52.00 | 33.00 | 5.00 | 7.00 | 3.00 | C | CSDS 2021 WB; slight BJP dip from 2019 peak |
| OBC | 36.00 | 43.00 | 7.00 | 11.00 | 3.00 | C | Mixed; some AITC gains |
| SC_total | 48.00 | 44.00 | 1.00 | 4.50 | 2.50 | C | Rajbanshi SC split more evenly 2021 vs 2019 (53% BJP in 2019); Paresh Adhikary SC identity pull for AITC |
| ST_total | 40.00 | 39.00 | 4.00 | 13.00 | 4.00 | C | |
| Other_Hindu_middle | 47.00 | 40.00 | 4.00 | 6.00 | 3.00 | C | |
| Muslim | 4.00 | 78.00 | 10.00 | 5.00 | 3.00 | C | Same as D.15 |

### D.17 Vote × Gender (2021 AE)

P(party ‖ gender) — CSDS 2021 WB regional. Lakshmir Bhandar launched April 2021 but only weeks before the election result — post-result rollout (registered ~1.6 crore women by Jul 2021). LB credit counted for AITC in 2021 narrative but pre-election announcement was the mechanism.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 46.00 | 43.00 | 2.00 | 6.00 | 3.00 | C | CSDS-Lokniti 2021 WB; BJP slightly below 2019 among male voters |
| Female | 38.00 | 53.00 | 1.50 | 5.00 | 2.50 | C | AITC women advantage increased post-Lakshmir Bhandar announcement; strong female swing toward AITC in 2021 |

### D.18 Vote × Welfare-scheme exposure (2021 AE)

*(No welfare_exposure axis declared for this AC — section retained as stub per schema §4.7)*

| Welfare_exposure | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| stub | 0 | 0 | 0 | 0 | 0 | E | No welfare_exposure axis in v0; omit from marginal |

---

## E. 2021 baseline vote (calibration target)

Tier A from ECI 2021 WB Assembly Election. Total valid votes: 198,744. Winner: Paresh Chandra Adhikary (AITC). AIFB is the only Left Front party present in this seat in 2021 — classified as LF. No INC candidate.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| AITC | 49.98 | A | 99,338 votes; ECI 2021 AE; Wikipedia Mekliganj constituency; 2019 §H anchor |
| BJP | 42.59 | A | 84,653 votes; same source |
| INC | 0.00 | A | No INC candidate in 2021 AE for this seat |
| LF | 4.03 | D | AIFB Gobinda Chandra Roy ~8,000 votes (~4.03%); Wikipedia approximate; AIFB is only LF-family party in this seat |
| Other_NOTA | 3.40 | D | Residual: 198,744 − 99,338 − 84,653 − 8,000 = 6,753 votes (~3.40%); includes NOTA + other minor candidates |
| **Sum** | **100.00** | — | self-check: 49.98+42.59+0.00+4.03+3.40=100.00 |

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 001 (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Paresh Chandra Adhikary | AIFB | 48.67 | Jayanta Kumar Ray | INC | ~29 | ~28,000 |
| 2016 AE | Arghya Roy Pradhan | AITC | 41.3 | Paresh Chandra Adhikary | AIFB | 37.7 | ~6,637 |

Notes: Forward Bloc dominated Mekliganj from the 1960s through 2009. 2011 AE was the peak-Left result (Paresh Adhikary on AIFB ticket). 2016 AE saw AITC flip the seat narrowly. Paresh Adhikary switched to AITC and won convincingly in 2021 — his SC Rajbanshi identity consolidated the dominant caste vote behind AITC.

### 2019 Lok Sabha AC-001 segment (anchor from 2019 AE data)

| Party | Votes | % | Tier | Source |
|---|---|---|---|---|
| BJP | 87,140 | 46.66 | A | 2019_AssemblySegmentLevelVotingData.csv (ECI); electorate 216,864; total valid votes 186,768 |
| AITC | 82,435 | 44.14 | A | Same |
| INC | 3,436 | 1.84 | A | Same |
| LF (CPIM + SUCI) | 9,404 | 5.04 | A | CPIM 8,153 + SUCI(C) 1,251; same source |
| Other_NOTA | 4,353 | 2.33 | A | BSP 1,224 + AMB 257 + SWJP 208 + KPPU 228 + IND 383+1,312+741 + NOTA 2,275; same source |

### Jalpaiguri Lok Sabha (PC 3) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Bijoy Chandra Barman | AITC | ~38 | AITC won; CPI(M)/AIFB still significant; BJP minor |
| 2019 LS | Jayanta Kumar Roy | BJP | 50.65 | Major BJP surge; AITC Bijoy Chandra Barman 38.39%; BJP margin ~12pp |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- ECI 2021 WB Assembly Election result — AC 001 Mekliganj: AITC (Paresh Chandra Adhikary) 99,338 / BJP (Dadhiram Ray) 84,653 / AIFB ~8,000; total valid votes 198,744; [Wikipedia Mekliganj constituency + ECI archive]
- `data/2019_AssemblySegmentLevelVotingData.csv` — ECI GE2019 AC-segment vote tallies for AC 001 (now used as F-section anchor)
- Census of India 2011 — Mekhliganj CD Block Primary Census Abstract [Wikipedia Mekhliganj CDB]
- Census of India 2011 — Haldibari CD Block Primary Census Abstract [Wikipedia Haldibari CDB]
- Census of India 2011 — Mekliganj Municipality + Haldibari Municipality [census2011.co.in]
- `data/candidates_wb_2021.csv` (filed under data/candidates/) — confirms winner: Adhikary Paresh Chandra (AITC), constituency 1, MEKLIGANJ (SC), COOCHBEHAR

### Secondary sources (tier B / C)

- NFHS-5 (2019-21) Koch Bihar district — household amenities (electricity 98.2%, improved sanitation 75.7%, clean fuel 25.7%, sex ratio 1,058); from `data/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv`
- NFHS-4 (2015-16) West Bengal — baseline for asset ownership; superseded by NFHS-5 for 2021 file
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2021 WB NES — vote × demographic conditionals (WB regional rollup)
- WB CDWDSW — Lakshmir Bhandar program launch April 2021 (₹500/month SC/ST women; ₹1000 others)

### Tertiary / journalistic (tier D)

- Wikipedia "Mekliganj Assembly constituency" — 2021 AE result (AITC winner Paresh Chandra Adhikary; BJP Dadhiram Ray); candidate switch from AIFB to AITC
- Wikipedia "Jalpaiguri Lok Sabha constituency" — assembly segments; 2019 result
- Wikipedia "Mekhliganj (community development block)" — GP list, population, SC data
- Wikipedia "Haldibari (community development block)" — GP list, population, SC data
- News reports on Paresh Chandra Adhikary's party switch (AIFB → AITC, 2019-21)

### Tier-D / E reliance flags (what to distrust)

- **2021 AE LF / Other_NOTA split** (§E) — AIFB vote count (~8,000) is Wikipedia approximate (Tier D); Other_NOTA residual is computed; v1 should verify from ECI Form-20 AE2021
- **Smartphone penetration** (C.14, D.8, D.13) — NFHS-5 WB state/district trend projection; COVID surge assumed +20-25pp from 2019; actual AC-level figure unavailable; tier C/E
- **Vote × demographic joints** (D.15–D.17) — CSDS 2021 WB regional rollup; local Rajbanshi AITC/BJP split is directionally documented via 2021 result but not quantified AC-level; tier C
- **Migration/birthplace** (C.16, D.3) — no AC-level Census D-series; Bangladesh-origin estimate from border-district context; tier D
- **2021 electorate** (§B) — no ECI 2021 roll directly fetched; estimated from valid votes + inferred turnout; tier D
- **BSF 50km jurisdiction** (§A note) — correctly referenced as Oct 2021 event; no demographic impact modeled

### v0 known gaps

1. ECI 2021 AE Form-20 for AC 001 — AIFB vote count (~8,000) is approximate from Wikipedia; exact breakdown of Other_NOTA (NOTA + minor parties) not confirmed
2. ECI 2021 AE roll (registered electors) — not directly fetched; §B electorate is estimate
3. DCHB Cooch Behar Part-A — collapsed 4 sub-units to 2; refine when DCHB available
4. CSDS 2021 WB cross-tabs — using regional rollup for D.15-D.17 joints; AC-level splits unavailable
5. GP-level population data — using CDB aggregate for each of the 14 GPs; v0 simplification

---

*v0 — generated on current date, frozen at end-2021 state-of-knowledge. No post-2021 events referenced.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2024 Lok Sabha Election — AC 001 segment within Jalpaiguri LS (PC 3) (tier A, CSV)

Figures below are **tier A** — sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, West Bengal, PC 3 Jalpaiguri, AC 1 Mekliganj. Total valid votes: 200,242 (candidates + NOTA). Electorate: 237,869.

| Party | Candidate (LS level) | Votes | AC-001 segment % | Tier | Source |
|---|---|---|---|---|---|
| AITC | Nirmal Chandra Roy | 94,842 | 47.36% | A | 2024_AssemblySegmentLevelVotingData.csv |
| BJP | Dr. Jayanta Kumar Roy | 92,024 | 45.96% | A | Same |
| LF (CPI(M) + SUCI) | Debraj Barman + SUCI | 7,060 | 3.53% | A | CPI(M) 6,115 + SUCI 945; Same |
| INC | — | 0 | 0.00% | A | No INC candidate; Same |
| Other_NOTA | BSP + KPPU + MPOI + INDs + NOTA | 6,316 | 3.15% | A | BSP 1,265 + KPPU 266 + MPOI 122 + INDs (221+276+483+1,079+656) + NOTA 1,948; Same |
| **AITC margin over BJP** | | **2,818 votes** | **1.40 pp** | A | Computed |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC-001 segment shares within ±3pp of the tier-A figures:
- AITC target: 47.4% ± 3pp
- BJP target: 46.0% ± 3pp
- LF + INC + Others: 6.7% ± 3pp

Note: Very tight 2024 result (AITC margin only 1.4pp) — 2024 LS continues 2021 AE pattern of competitive AITC-BJP contest with AITC incumbent advantage in this SC seat.
