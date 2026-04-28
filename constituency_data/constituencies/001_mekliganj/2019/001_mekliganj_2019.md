# AC 001 — Mekliganj (SC) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 001 Mekliganj as of 2019 only — it does not reference
> any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 001 | A | ECI / Delimitation Commission 2008 |
| AC name | Mekliganj | A | ECI |
| Reservation | SC | A | Delimitation 2008 |
| District | Cooch Behar | A | Delimitation 2008 |
| Sub-division | Mekhliganj | A | WB administrative |
| LS constituency | 3 — Jalpaiguri (GEN) | A | Delimitation 2008; confirmed from 2019_AssemblySegmentLevelVotingData.csv |
| LS segments included | AC 1 Mekliganj · AC 2 Dhupguri · AC 3 Maynaguri · AC 4 Jalpaiguri · AC 5 Rajganj · AC 6 Dabgram-Phulbari · AC 7 Mal (ST) | A | Delimitation 2008 |
| AC composition | Mekliganj Municipality + Mekliganj CDB (8 GPs: Bagdokra Fulkadabri, Bhotbari, Changrabandha, Jamaldaha, Kuchlibari, Niztaraf, Ranirhat, Uchalpukuri) + Haldibari Municipality + Haldibari CDB (6 GPs: Baxiganj, Daxin Bara Haldibari, Dewanganj, Hemkumari, Per Mekhliganj, Uttar Bara Haldibari) | A | Delimitation 2008; Wikipedia CDB articles |
| Geographic note | Southern tip of Jalpaiguri LS; enclaved by Bangladesh on west, Bhutan corridor on north; Haldibari is an India-Bangladesh rail terminus; Changrabandha is a key land-port on Bangladesh border | A | — |
| Sub-units used in v0 | **U1: Mekliganj_area** (Mekliganj Muni + Mekliganj CDB, ~58.1% pop) · **U2: Haldibari_area** (Haldibari Muni + Haldibari CDB, ~41.9% pop) | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~282,750 (Mekliganj Muni 9,127 + Mekliganj CDB 155,250 + Haldibari Muni 14,404 + Haldibari CDB 103,969) | A | Census 2011 (Wikipedia CDB articles + census2011.co.in) |
| 2019 projected population | ~308,600 | E | 8-yr compound ~1.1%/yr growth from 2011 base |
| Sex ratio (2019, F per 1000 M) | ~951 | E | Cooch Behar district 2011 baseline ~948; minimal projection drift |
| 2019 electorate (registered voters) | 216,864 | A | 2019_AssemblySegmentLevelVotingData.csv (ECI) |
| Estimated M / F / TG split (2019) | ~51.2% M / 48.8% F / ~0.01% TG | E | District sex ratio back-projection |
| 2019 total valid votes | 186,768 | A | 2019_AssemblySegmentLevelVotingData.csv |
| 2019 turnout | 86.1% | A | Derived: 186,768 / 216,864 |
| 2019 polling stations (estimated) | ~230 | E | Back-projection from electorate size; ~940 voters per booth |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

Weighted from four sub-units at 2011 Census; projected forward at religion-differential growth rate (+0.3pp Muslim share gain per decade as per Pew WB pattern).

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 75.25 | B | Weighted 2011: Mekli-Muni 79.75%, Mekli-CDB 80.41%, Haldi-Muni 83.91%, Haldi-CDB 66.53%; AC weighted ~75.46%; adjusted -0.21pp for 8yr differential growth |
| Muslim | 24.42 | B | Weighted 2011: ~24.21%; adjusted +0.21pp for 8yr differential growth |
| Christian | 0.29 | B | Weighted from four sub-units 2011 |
| Sarna_ORP | 0.02 | E | Negligible in Cooch Behar CDBs; set near-zero |
| Other_residual | 0.02 | E | Sikh + Jain + Buddhist + Not_stated; residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

AC 001 is reserved SC. SC share is extraordinarily high (~65%) — Cooch Behar is the only district in India where SCs form a majority. Dominant SC sub-group is Rajbanshi (Koch-Rajbanshi), classified SC in WB.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 65.00 | B | Weighted 2011: Mekli-Muni 48.98%, Mekli-CDB 71.24%, Haldi-Muni 35.47%, Haldi-CDB 61.18%; AC weighted 65.00% |
| └ Rajbanshi_SC | 58.50 | C | Koch-Rajbanshi SC dominant sub-group in Cooch Behar; ~90% of SC pool; Cooch Behar district Rajbanshi concentration (journalistic + Cooch Behar Govt) |
| └ Namasudra_SC | 4.55 | E | Smaller pool; ~7% of SC pool |
| └ Other_SC | 1.95 | E | Residual SC sub-castes |
| **ST_total** | 0.88 | B | Weighted 2011: Mekli-CDB 1.24%, Haldi-CDB 0.30%; AC weighted 0.88% |
| UC_bhadralok | 2.00 | E | Very small bhadralok fraction in Cooch Behar frontier AC |
| OBC | 3.00 | E | Small OBC fraction; Cooch Behar OBC pool (Sutradhar, Teli, etc.) |
| Other_Hindu_middle | 4.37 | E | Residual within Hindu non-SC/ST/UC/OBC: 75.25 Hindu − 65.0 SC − 0.88 ST − 2.0 UC − 3.0 OBC = 4.37 |
| Muslim | 24.42 | B | See C.1; all sub-castes pooled |
| Christian_plus_Sarna_plus_Other | 0.33 | E | See C.1 |
| **Sum** | **100.00** | — | self-check: 65.00+0.88+2.00+3.00+4.37+24.42+0.33=100.00 (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

Renormalized from Cooch Behar district age pyramid (Census 2011); children 0–17 excluded; 11 cohorts sum to 100.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.50 | E | Cooch Behar district age pyramid Census 2011; first-time voter cohort |
| 23_27 | 11.00 | E | |
| 28_32 | 10.50 | E | |
| 33_37 | 10.00 | E | |
| 38_42 | 9.50 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.50 | E | |
| 63_67 | 4.50 | E | |
| 68 | 12.50 | E | 68+ open-ended cohort; includes widowed elderly |
| **Sum** | **100.00** | — | self-check (18+ adults only) |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.20 | E | Cooch Behar district 2011 sex ratio ~948 F per 1000 M → 51.31% M; slight adjustment to 51.20 for projection |
| Female | 48.79 | E | |
| Third_gender | 0.01 | E | State-level trace |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 88.00 | B | Mekliganj CDB 93.9% Bengali; Cooch Behar district 94.79%; Haldibari CDB has higher Rajbongshi share; AC weighted ~88% |
| Hindi | 1.20 | B | Cooch Behar district ~1.17% Hindi; slightly higher in border/transit zones |
| Urdu | 0.50 | E | Small Muslim pocket in Haldibari (33% Muslim); some Urdu-speakers |
| Other | 0.30 | E | Residual catch-all |
| Rajbongshi | 10.00 | C | Rajbanshi (Koch-Rajbanshi) community speaks Rajbongshi dialect; distinct from Bengali; Mekliganj CDB 2.34% (Wikipedia) but likely under-counted as many register as Bengali; AC-local estimate |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

Baseline: AC literacy ~70.2% (weighted 2011). Projected +4pp to ~74% literate by 2019 → ~26% illiterate among age 7+.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 26.00 | B | Weighted CDB literacy ~70.2% (2011); adjusted for 8yr trend; below WB state average of 76% |
| Primary | 24.00 | E | Census 2011 WB education distribution scaled for Cooch Behar |
| Middle | 20.00 | E | |
| Secondary | 14.00 | E | |
| Higher_Secondary | 9.00 | E | |
| Graduate | 5.50 | E | Lower than state average given frontier rural AC |
| Postgraduate | 1.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

Highly agricultural AC; Mekliganj CDB had 82% of workers in cultivator + ag-labourer categories (Census 2011).

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 35.00 | E | Census 2011 Mekliganj CDB pattern; rural dominance |
| Marginal_worker | 13.00 | E | High marginal-worker share typical in agrarian Cooch Behar |
| Non_worker | 37.00 | E | Housewife + elderly + retired; large non-worker share in female-heavy rural HHs |
| Student | 9.00 | E | 18–22 in education cohort |
| Unemployed | 6.00 | E | Educated job-aspirant pool; lower than urban ACs |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

Mekliganj CDB 2011: cultivator 48.22%, ag-labourer 34.04%, household industry 1.70%, other workers 16.03%. Haldibari CDB similar profile. Weighted and diluted slightly by Muni households.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 40.00 | B | Mekli CDB 48.22% (A); weighted down by Haldibari higher Muslim ag-labourer share and Muni dilution |
| Agricultural_labourer | 33.00 | B | Mekli CDB 34.04% (A); high landless SC-labourer pool given 65% SC |
| Household_industry | 3.00 | B | Mekli CDB 1.70%; slightly higher in Haldibari |
| Manufacturing | 2.50 | E | Limited; some rice mills in Haldibari area |
| Construction | 5.00 | E | Seasonal migrant construction workers |
| Trade_retail | 8.00 | E | Muni-based retail; Changrabandha border trade; Haldibari market |
| Transport_logistics | 3.00 | E | Haldibari rail terminus; Changrabandha land-port logistics |
| Services | 3.00 | E | Private services |
| Government_services_teachers | 2.50 | E | Government teachers, block-level admin |
| Out_migrant_worker | 0.00 | E | Low out-migration; set to residual 0 here (absorbed into other categories) |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Very low; some small traders and landowners |
| Employee | 18.00 | E | Govt employees + regular-wage workers |
| Single_worker | 52.00 | E | Own-account cultivator + petty trader + artisan; high in SC cultivator community |
| Family_worker | 28.50 | E | Unpaid family farm labour; high given ag dominance and joint-family farming |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2019, household level)

Cooch Behar is one of WB's poorer districts; high SC and agricultural-labourer concentration implies high poverty headcount.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 30.00 | C | Cooch Behar district high poverty; census 2001-based BPL estimates ~35%; projected down ~5pp by 2019 given PMJDY/welfare rollout |
| Above_Poverty_Line_low_income | 35.00 | E | Near-poor households |
| Lower_middle | 22.00 | E | |
| Middle | 10.00 | E | |
| Upper_middle_well_off | 3.00 | E | Thin upper stratum; some Muni-based traders and govt employees |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Mekliganj_area | 58.10 | A | Mekliganj Muni (9,127) + Mekliganj CDB (155,250) = 164,377 of 282,750 total; Census 2011 |
| U2_Haldibari_area | 41.90 | A | Haldibari Muni (14,404) + Haldibari CDB (103,969) = 118,373 of 282,750; Census 2011 |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | Cooch Behar district slightly above WB state average 4.3 |
| Nuclear_HH | 65.00 | E | NFHS-4 WB rural pattern; slightly lower joint-HH share in SC Rajbanshi community vs Bengal average |
| Joint_HH | 28.00 | E | |
| Extended_multi_generation | 7.00 | E | |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.00 | E | Census 2011 Cooch Behar pattern; first-time voter cohort 18–22 |
| Currently_married | 64.00 | E | |
| Widowed | 8.50 | E | Slightly higher than WB average; older demographic + lower life expectancy in poor rural AC |
| Separated_divorced | 1.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

Independent ownership rates — do NOT sum.

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 65.00 | C | NFHS-4 WB rural 60%; Cooch Behar below-average income → ~65% by 2019 |
| Radio | 7.00 | C | Slightly higher than WB average in rural Cooch Behar |
| Mobile_phone | 82.00 | C | NFHS-4 WB rural ~78%; +Jio expansion 2016-19 |
| Smartphone_with_internet | 35.00 | C | Lower than WB average; rural frontier AC; NFHS baseline + Jio rollout |
| Computer | 4.00 | C | NFHS-4 WB rural ~4% |
| Two_wheeler | 18.00 | C | NFHS-4 WB rural 18% |
| Four_wheeler | 3.00 | C | Limited |
| Banking_access | 85.00 | B | PMJDY saturation; NFHS-4 WB rural baseline + rollout; Cooch Behar PMJDY enrollment high |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 85.00 | C | NFHS-4 WB rural 84%; Cooch Behar CDB data slightly above average for drinking water |
| Improved_sanitation | 60.00 | C | NFHS-4 WB rural 51% + Swachh Bharat 2014-19 (+15pp rural); lower in Cooch Behar than urban |
| LPG_clean_cooking_fuel | 30.00 | C | NFHS-4 WB rural 24% + Ujjwala 2016-19 (+~10pp); rural Cooch Behar lag |
| Wood_biomass_fuel | 65.00 | C | Dominant in rural Cooch Behar; declining as LPG rises |
| Other_fuel | 5.00 | C | Kerosene, dung, etc. |
| Electricity | 90.00 | C | Census 2011 Cooch Behar + Saubhagya 2017-19 rollout; estimated ~90% by 2019 |
| **Note** | (water/sanitation/electricity are independent %s; LPG + Wood + Other fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

Cooch Behar is a border district with significant Bangladesh-origin Rajbanshi-SC community (partition displacement and pre-partition indigenous residents). Haldibari is an old train terminus connected to Bangladesh; Changrabandha is a land port.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 70.00 | D | Rajbanshi SC are mostly indigenous to Cooch Behar; high nativeness |
| WB_other_district | 6.00 | D | Limited in-migration from other WB districts |
| Other_Indian_state | 2.00 | D | Small trader fringe in Muni areas |
| Bangladesh_origin | 20.00 | D | Significant: Rajbanshi displaced in 1947 partition + subsequent Hindu refugee flows; Haldibari area heavily affected; journalistic and regional studies estimate |
| Outside_India | 0.50 | E | Bhutan / Nepal origin; minor |
| Out_migrant | 1.50 | E | Seasonal / permanent out-migrants registered here |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 82.00 | 1.20 | 0.00 | 0.30 | 16.50 | E | Rajbongshi-speaking Rajbanshi SC are predominantly Hindu; 65% SC pool skews language distribution toward Rajbongshi |
| Muslim | 95.00 | 1.00 | 3.50 | 0.50 | 0.00 | E | Cooch Behar Muslims are predominantly Bengali-speaking; tiny Urdu-speaking pocket |
| Christian | 85.00 | 5.00 | 0.00 | 10.00 | 0.00 | E | Tiny base; Bengali + English-medium |
| Sarna_ORP | 50.00 | 10.00 | 0.00 | 40.00 | 0.00 | E | Negligible population; mixed |
| Other_residual | 60.00 | 30.00 | 0.00 | 10.00 | 0.00 | E | Marwari/other traders |

### D.2 Religion × Caste

P(caste ‖ religion) — 2D table; one row per religion.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 79.50 | 1.17 | 2.66 | 3.99 | 12.68 | 0 | 0 | E | SC_total/Hindu: 65.0/75.25 = 86.4% of Hindu is SC; distributed among leaves; Hindu row sums to 100 |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 90 | 0 | 5 | 5 | 0 | 0 | E | Mostly ST affiliation |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | Residual |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 65.00 | 6.00 | 2.00 | 25.50 | 0.50 | 1.00 | D | Hindu Rajbanshi have significant Bangladesh-origin fraction (1947 partition + subsequent flows); bulk native |
| Muslim | 86.00 | 6.00 | 2.00 | 4.00 | 1.50 | 0.50 | D | Cooch Behar Muslims mostly indigenous; smaller Bangladesh-origin fraction; small Bihar/UP trader subset |
| Christian | 80.00 | 10.00 | 5.00 | 5.00 | 0.00 | 0.00 | E | Mixed |
| Sarna_ORP | 90.00 | 5.00 | 5.00 | 0.00 | 0.00 | 0.00 | E | Mostly indigenous tribal |
| Other_residual | 40.00 | 15.00 | 40.00 | 5.00 | 0.00 | 0.00 | E | Trader/service migrants mostly from other states |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 67.00 | 37.00 | 86.00 | E | Slightly above AC average; Hindu Rajbanshi includes both landed SC and landless labourers |
| Muslim | 58.00 | 29.00 | 81.00 | E | Below-average asset access; higher Muslim concentration in poorer Haldibari rural area |
| Christian | 72.00 | 42.00 | 89.00 | E | Small base; approximation |
| Sarna_ORP | 50.00 | 20.00 | 70.00 | E | Negligible base; lower asset access |
| Other_residual | 85.00 | 55.00 | 95.00 | E | Trader/affluent fringe |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Rows sum to 100.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 8.00 | 12.00 | 15.00 | 20.00 | 20.00 | 18.00 | 7.00 | E |
| SC_total | 28.00 | 25.00 | 20.00 | 14.00 | 8.00 | 4.00 | 1.00 | E |
| ST_total | 32.00 | 26.00 | 20.00 | 12.00 | 6.00 | 3.00 | 1.00 | E |
| OBC | 20.00 | 22.00 | 20.00 | 18.00 | 12.00 | 6.00 | 2.00 | E |
| Other_Hindu_middle | 18.00 | 22.00 | 21.00 | 18.00 | 12.00 | 7.00 | 2.00 | E |
| Muslim | 32.00 | 26.00 | 20.00 | 13.00 | 6.00 | 2.50 | 0.50 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender). 5-year cohorts; 18+ only.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 12.00 | 9.00 | E |
| 23_27 | 11.00 | 7.00 | E |
| 28_32 | 9.00 | 5.00 | E |
| 33_37 | 8.00 | 4.00 | E |
| 38_42 | 7.00 | 3.00 | E |
| 43_47 | 6.00 | 2.50 | E |
| 48_52 | 5.00 | 2.00 | E |
| 53_57 | 4.00 | 1.50 | E |
| 58_62 | 3.50 | 1.00 | E |
| 63_67 | 3.00 | 1.00 | E |
| 68 | 2.50 | 0.80 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender). 5-year cohorts.

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

P(owns smartphone ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 28.00 | 58.00 | E | Rural ag baseline; below WB average |
| Agricultural_labourer | 20.00 | 48.00 | E | Lowest income; lowest access |
| Household_industry | 32.00 | 62.00 | E | |
| Manufacturing | 42.00 | 72.00 | E | |
| Construction | 38.00 | 65.00 | E | |
| Trade_retail | 58.00 | 80.00 | E | Muni concentrated; higher access |
| Transport_logistics | 52.00 | 74.00 | E | Border port workers |
| Services | 60.00 | 82.00 | E | |
| Government_services_teachers | 78.00 | 90.00 | E | Highest access |
| Out_migrant_worker | 65.00 | 75.00 | E | Smartphone-heavy |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 38.00 | 1.50 | E |
| Primary | 40.00 | 3.00 | E |
| Middle | 38.00 | 5.00 | E |
| Secondary | 32.00 | 8.00 | E |
| Higher_Secondary | 26.00 | 12.00 | E |
| Graduate | 28.00 | 14.00 | E |
| Postgraduate | 35.00 | 10.00 | E |

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Sub-unit codes match C.11.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Mekliganj_area | 80.37 | 19.29 | 0.32 | 0.01 | 0.01 | B | Weighted: Mekli-Muni 79.75% Hindu / 19.86% Muslim + Mekli-CDB 80.41% / 19.26%; Census 2011 |
| U2_Haldibari_area | 68.64 | 31.05 | 0.25 | 0.03 | 0.03 | B | Weighted: Haldi-Muni 83.91% Hindu / 15.94% Muslim + Haldi-CDB 66.53% / 33.14%; Census 2011 |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Canonical caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Mekliganj_area | 2.20 | 70.00 | 1.24 | 3.00 | 4.25 | 19.29 | 0.02 | B |
| U2_Haldibari_area | 1.70 | 58.05 | 0.38 | 3.00 | 5.79 | 31.05 | 0.03 | B |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Mekliganj_area | 67.00 | 36.00 | 4.00 | 86.00 | E |
| U2_Haldibari_area | 62.00 | 33.00 | 3.50 | 83.00 | E |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Mekliganj_area | 32.00 | 62.00 | 86.00 | 91.00 | E |
| U2_Haldibari_area | 27.00 | 57.00 | 83.00 | 88.00 | E |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 regional WB rollup with local adjustment for high-SC Rajbanshi AC.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 55.00 | 35.00 | 2.00 | 6.00 | 2.00 | C | CSDS-Lokniti 2019 WB; BJP did strongly among Hindu SC Rajbanshi in border ACs |
| Muslim | 5.00 | 72.00 | 15.00 | 6.00 | 2.00 | C | CSDS 2019 WB; Muslim consolidation around AITC |
| Christian | 25.00 | 55.00 | 10.00 | 8.00 | 2.00 | E | Approximation; small base |
| Sarna_ORP | 40.00 | 40.00 | 5.00 | 12.00 | 3.00 | E | Tiny base |
| Other_residual | 45.00 | 35.00 | 8.00 | 8.00 | 4.00 | E | Trader fringe |

### D.16 Vote × Caste (2019 LS)

P(party ‖ caste) — CSDS-Lokniti 2019 WB regional. Note: Rajbanshi SC in Cooch Behar/Jalpaiguri belt showed BJP tilt by 2019 (Nisith Pramanik BJP win in Cooch Behar LS + Jayanta Kumar Roy BJP win in Jalpaiguri LS).

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 55.00 | 30.00 | 5.00 | 8.00 | 2.00 | C | CSDS 2019 WB |
| OBC | 38.00 | 40.00 | 8.00 | 11.00 | 3.00 | C | Mixed |
| SC_total | 53.00 | 37.00 | 2.50 | 5.50 | 2.00 | C | Rajbanshi SC BJP-leaning in 2019; BJP's alliance with KPP (Koch-Rajbanshi party) and Rajbanshi identity politics |
| ST_total | 42.00 | 36.00 | 5.00 | 14.00 | 3.00 | C | |
| Other_Hindu_middle | 50.00 | 38.00 | 4.00 | 6.00 | 2.00 | C | |
| Muslim | 5.00 | 72.00 | 15.00 | 6.00 | 2.00 | C | Same as D.15 |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

P(party ‖ gender) — CSDS 2019 WB regional.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 48.00 | 42.00 | 2.50 | 5.50 | 2.00 | C | CSDS-Lokniti 2019 WB |
| Female | 42.00 | 48.00 | 2.00 | 6.00 | 2.00 | C | AITC women advantage pre-LB |

---

## E. 2019 baseline vote (calibration target)

Tier A from ECI CSV (2019_AssemblySegmentLevelVotingData.csv, AC_NO=1). Total valid votes: 186,768. NOTA: 2,275 (included in Other_NOTA).

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 46.66 | A | 87,140 votes; ECI 2019_AssemblySegmentLevelVotingData.csv |
| AITC | 44.14 | A | 82,435 votes; same source |
| INC | 1.84 | A | 3,436 votes; same source |
| LF | 5.04 | A | CPIM 8,153 + SUCI(C) 1,251 = 9,404 votes; same source |
| Other_NOTA | 2.33 | A | BSP 1,224 + AMB 257 + SWJP 208 + KPPU 228 + IND 383+1,312+741 + NOTA 2,275 = 6,628 votes; same source |
| **Sum** | **100.01** | — | rounding; within ±0.5 |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 001 (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Paresh Chandra Adhikary | AIFB | 48.67 | Jayanta Kumar Ray | INC | ~29 | ~28,000 |
| 2016 AE | Arghya Roy Pradhan | AITC | 41.3 | Paresh Chandra Adhikary | AIFB | 37.7 | ~6,637 |

Notes: Forward Bloc dominated Mekliganj from the 1960s through 2009. 2011 AE was the peak-Left result (Paresh winning on AIFB ticket). 2016 AE saw AITC flip the seat with a narrow majority. Paresh Adhikary, the dominant figure, contested on AIFB ticket in 2011 and 2016. The constituency has historically competitive multi-party contests (AIFB, Congress, AITC).

### Jalpaiguri Lok Sabha (PC 3) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Bijoy Chandra Barman | AITC | ~38 | AITC won; CPI(M)/AIFB still significant; BJP minor |
| 2019 LS | Jayanta Kumar Roy | BJP | 50.65 | Major BJP surge; AITC Bijoy Chandra Barman 38.39%; BJP margin ~12pp |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- `data/2019_AssemblySegmentLevelVotingData.csv` — ECI GE2019 AC-segment vote tallies for AC 001 (BJP 87,140 / AITC 82,435 / CPIM 8,153 / INC 3,436 / SUCI 1,251 + minor; electorate 216,864; NOTA 2,275)
- Census of India 2011 — Mekhliganj CD Block Primary Census Abstract (population 155,250; SC 71.24%; ST 1.24%; religion; literacy 69.34%; workforce distribution) [Wikipedia Mekhliganj CDB]
- Census of India 2011 — Haldibari CD Block Primary Census Abstract (population 103,969; SC 61.18%; ST 0.30%; religion; literacy 69.22%) [Wikipedia Haldibari CDB]
- Census of India 2011 — Mekliganj Municipality (population 9,127; SC 48.98%) [census2011.co.in]
- Census of India 2011 — Haldibari Municipality (population 14,404; SC 35.47%) [census2011.co.in]
- Delimitation Commission of India 2008 — WB Schedule (AC 001 Mekliganj SC; LS 3 Jalpaiguri; composition = Mekliganj Muni + Mekliganj CDB + Haldibari Muni + Haldibari CDB) [Wikipedia Mekliganj Assembly constituency]

### Secondary sources (tier B / C)

- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2019 NES — vote × demographic conditionals (WB regional rollup)
- Cooch Behar district government — demography; SC majority note
- WB District Statistical Handbook — Cooch Behar

### Tertiary / journalistic (tier D)

- Wikipedia "Mekliganj Assembly constituency" — election results 2011, 2016, 2021; reservation; LS segment composition
- Wikipedia "Jalpaiguri Lok Sabha constituency" — assembly segments; 2019 result
- Wikipedia "Mekhliganj (community development block)" — GP list, population, SC data
- Wikipedia "Haldibari (community development block)" — GP list, population, SC data

### Tier-D / E reliance flags (what to distrust)

- **Rajbongshi language share** (C.5, D.1) — CDB article gives 2.34% but likely under-counted vs. community size; tier C/E; used 10% estimate
- **Caste sub-group shares within SC** (C.2, D.2) — no post-1931 caste census; Rajbanshi dominance estimated from district ethnography; tier C/E
- **Vote × demographic joints** (D.15–D.17) — CSDS 2019 WB regional rollup; local Rajbanshi BJP-tilt is directionally documented but not quantified AC-level; tier C
- **Migration/birthplace** (C.16, D.3) — no AC-level Census D-series; Bangladesh-origin estimate from border-district context; tier D
- **Asset/media** (C.14, D.13) — NFHS-4 state-level pattern projected to rural frontier AC; tier C
- **Age distribution** (C.3) — Cooch Behar district pattern applied; no AC-specific age pyramid; tier E
- **Out_migrant_worker** (C.8) — set to zero/absorbed; Cooch Behar not a high out-migration district; v0 simplification

### v0 known gaps

1. DCHB Cooch Behar Part-A — collapsed 4 sub-units to 2 (Mekliganj area + Haldibari area); refine when DCHB available
2. ECI GE2019 Form-20 — segment vote by candidate already tier A from CSV; NOTA 2,275 confirmed
3. GP-level population data — using CDB aggregate for each of the 14 GPs; v0 simplification
4. CSDS WB regional cross-tabs — using published summary not full dataset
5. Rajbongshi language / Rajbanshi caste sub-structure — requires field survey or linguistics source

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2021 WB Assembly Election — AC 001 Mekliganj (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| AITC | Paresh Chandra Adhikary | 99,338 | 49.98 | A — ECI 2021 AE; Wikipedia Mekliganj constituency |
| BJP | Dadhiram Ray | 84,653 | 42.59 | A — ECI 2021 AE |
| AIFB | Gobinda Chandra Roy | ~8,000 | ~4.0 | D — Wikipedia approximate |
| **AITC margin** | | **14,685 votes** | **7.39 pp** | A |
| Total valid votes | | 198,744 | | A |

Note: Paresh Chandra Adhikary had switched from AIFB (2011 winner) to AITC and consolidated incumbent advantage. BJP maintained a strong second-place position consistent with 2019 LS result.

### 2024 Lok Sabha Election — AC 001 segment within Jalpaiguri LS (PC 3)

Data from `data/2024_AssemblySegmentLevelVotingData.csv` if available, or ECI Form-20. Full breakdown to be added when CSV is processed for this AC.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Jayanta Kumar Roy | (pending) | (pending) | A | 2024_AssemblySegmentLevelVotingData.csv — to be fetched |
| AITC | (candidate) | (pending) | (pending) | A | Same |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC segment shares within ±3pp of the tier-A figures (BJP / AITC / INC / LF combined). Reference: 2019 LS AC-001 actual = BJP 46.66%, AITC 44.14%.
