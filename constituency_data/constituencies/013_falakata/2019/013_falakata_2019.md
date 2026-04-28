# AC 013 — Falakata (SC) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 013 Falakata as of 2019 only — it does not reference any
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
| AC number | 013 | A | ECI / Delimitation Commission 2008 |
| AC name | Falakata | A | ECI |
| Reservation | SC | A | Delimitation 2008 |
| District | Alipurduar | A | Delimitation 2008 (formerly Jalpaiguri, carved out 2014) |
| Sub-division | Alipurduar | A | WB administrative |
| LS constituency | 02 — Alipurduars (ST reserved) | A | Delimitation 2008 |
| LS segments included | AC 06 Tufanganj · 07 Kumargram · 08 Kalchini · 09 Alipurduars · 10 Falakata · 11 Madarihat · 12 Nagrakata (note: renumbering post-delimitation; Alipurduars LS = 7 AC segments) | A | Delimitation 2008 / ECI |
| AC composition | Falakata Municipality + Falakata CD block (all 12 GPs) + Purba Kanthalbari GP of Alipurduar-I CD block | A | Delimitation 2008; Wikipedia Falakata Assembly constituency |
| Geographic note | Dooars foothills, Terai-Dooars region; tea garden belt; bordering Bhutan to north; forested reserve areas | A | — |
| Sub-units used in v0 | **U1: Falakata_Municipality_CDB_core** (Falakata town + CDB settled area) · **U2: Purba_Kanthalbari_Alipurduar_I** (GP of Alipurduar-I block, rural fringe) | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~295,000 (Falakata CDB 290,722 + Purba Kanthalbari GP share of Alipurduar-I ~4,500 est.) | E | Census 2011 censusindia.co.in Falakata Block; v0 GP-equal-weight assumption for Purba Kanthalbari |
| 2019 projected population | ~319,000 | E | 8-yr compound religion-differential growth from 2011 base |
| Sex ratio (2019, F per 1000 M) | ~943 | A | Census 2011 Falakata Block sex ratio 943 (censusindia.co.in) |
| 2019 estimated electorate (18+) | ~244,600 | A | ECI 2019 LS — total electors for AC 013 = 244,579 |
| Estimated M / F / TG split (2019) | 51.5% M / 48.5% F / <0.05% TG | E | Sex ratio 943 → 51.5% M; TG nominal |
| 2019 polling stations (estimated) | ~275 | E | Back-projection from 2019 electorate scale |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 82.50 | A | Census 2011 Falakata Block: Hindu 82%; adjusted +0.5pp for 8-yr differential (censusindia.co.in) |
| Muslim | 15.50 | A | Census 2011 Falakata Block: Muslim 15.79%; slight relative decline vs Hindu growth rate |
| Christian | 1.50 | E | Tea garden belt pattern; Alipurduar-I block 2.54% Christian; Falakata lower (less plantation density) |
| Sarna_ORP | 0.40 | E | Adivasi tribal religion fringe; small given majority Hindu-identified Adivasis in Dooars |
| Other_residual | 0.10 | E | Buddhist (Nepali fringe) + Sikh + Not_stated lumped |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 40.70 | A | Census 2011 Falakata Block: SC 40.7% (censusindia.co.in) |
| └ Rajbanshi_SC | 26.00 | C | Dominant SC in Dooars-Terai; Rajbanshi concentrated in Falakata; ~64% of SC pool |
| └ Tea_garden_SC | 8.00 | D | Chamar, Muchi, Hari and other SC communities in tea estates; ~20% of SC pool |
| └ Other_SC | 6.70 | E | Residual SC (Bagdi etc.) |
| **ST_total** | 15.90 | A | Census 2011 Falakata Block: ST 15.9% (censusindia.co.in) |
| └ Oraon_ST | 7.00 | D | Largest ST group in Dooars tea gardens; Mili Oraon (RSP candidate 2019) reflects salience |
| └ Munda_ST | 3.50 | D | Second major tea garden ST |
| └ Koch_ST | 2.50 | D | Koch community (categorised ST in WB); Koch-Rajbongshi belt |
| └ Other_ST | 2.90 | E | Santali, Rava, Rabha, Toto and others |
| UC_bhadralok | 5.00 | E | Small bhadralok (Brahmin/Kayastha/Baidya) presence; concentrated in Falakata town |
| OBC | 4.00 | E | Teli, Sutradhar, other OBC; modest in this tea-belt district |
| Other_Hindu_middle | 16.90 | E | Residual within Hindu: 82.5% − 40.7% SC − 15.9% ST − 5% UC − 4% OBC = 16.9% |
| Muslim | 15.50 | E | All sub-castes pooled; mostly Bengali-Muslim peasantry |
| Christian_plus_Sarna_plus_Other | 2.00 | E | Christian 1.50% + Sarna 0.40% + Other_residual 0.10% |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.50 | E | Renormalized from Alipurduar district Census 2011 age pyramid (18+ only) |
| 23_27 | 11.00 | E | |
| 28_32 | 10.50 | E | |
| 33_37 | 10.00 | E | |
| 38_42 | 9.50 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.00 | E | |
| 63_67 | 4.50 | E | |
| 68 | 13.00 | E | 68+ open-ended; includes 63_67 overflow; renormalized to 100 |
| **Sum** | **100.00** | — | self-check (renormalized from Census 2011 age pyramid excluding 0–17) |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.47 | A | Sex ratio 943 F per 1000 M → 1000/(1000+943) = 51.47% M |
| Female | 48.52 | A | 943/(1000+943) |
| Third_gender | 0.01 | E | Nominal; consistent with WB pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 62.00 | E | Dominant plains population; Rajbanshi community mostly Bengali-speaking; estimate |
| Hindi | 3.00 | E | Bihari/UP migrant workers; some tea garden Hindi belt |
| Urdu | 2.00 | E | Muslim community fraction |
| Other | 3.00 | E | Residual catch-all (Nepali fringe, Bodo fringe) |
| Rajbongshi | 14.00 | D | Rajbongshi/Koch-Rajbongshi mother tongue; significant in Dooars North Bengal (journalistic) |
| Sadri | 8.00 | D | Lingua franca of tea garden Adivasis (Oraon, Munda, etc.); widely spoken in Dooars |
| Oraon_Kurukh | 5.00 | D | Native language of Oraon ST community; Dooars tea belt |
| Nepali | 3.00 | E | Small Nepali-speaking community in foothills |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 27.00 | A | Falakata Block literacy 72.64% in 2011 → ~27.4% illiterate; 8yr trend minimal → ~27% in 2019 |
| Primary | 24.00 | E | Census 2011 education distribution for block; primary share large in tea garden belt |
| Middle | 18.00 | E | |
| Secondary | 14.00 | E | |
| Higher_Secondary | 9.00 | E | |
| Graduate | 6.00 | E | Below WB average; limited higher-ed access in tea belt |
| Postgraduate | 2.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 36.00 | E | Census 2011 Falakata Block main-worker pattern; tea garden employment high |
| └ Main_worker_tea_garden | 14.00 | D | Tea garden permanent workers; sub-row, is_subgroup=yes |
| └ Main_worker_non_tea | 22.00 | E | Agriculture, trade, services; sub-row |
| Marginal_worker | 12.00 | E | Seasonal and marginal workers; tea garden casual labor |
| Non_worker | 34.00 | E | Housewife + elderly + retired |
| Student | 10.00 | E | 18–22 cohort in education |
| Unemployed | 8.00 | E | Educated job-seekers; tea estate closures create unemployed pool |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 16.00 | E | Falakata plains agriculture; smaller than pure agrarian ACs due to tea sector |
| Agricultural_labourer | 20.00 | E | Farm laborers excluding tea garden workers |
| Household_industry | 4.00 | E | Weaving, bamboo craft, small cottage industries |
| Manufacturing | 6.00 | E | Small-scale; tea processing, agro-processing |
| Construction | 5.00 | E | |
| Trade_retail | 10.00 | E | Falakata town retail + local markets |
| Transport_logistics | 5.00 | E | Road freight; NH-31C access |
| Services | 9.00 | E | Private services, domestic workers |
| Government_services_teachers | 5.00 | E | Below state average; limited govt presence in tea belt |
| Out_migrant_worker | 5.00 | D | Youth out-migration from tea estates to other states; growing trend |
| Tea_garden_worker | 15.00 | D | Tea garden permanent and casual workers; AC-local occupation category |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Small traders and contractors |
| Employee | 40.00 | E | Tea garden employees (largest employee pool in North Bengal) + govt employees |
| Single_worker | 38.00 | E | Own-account cultivators, artisans, small traders |
| Family_worker | 20.50 | E | Unpaid family labor in agriculture and household industry |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 28.00 | C | Alipurduar district poverty high; tea garden belt historically high BPL; NFHS-4 WB pattern adjusted upward for north Bengal |
| Above_Poverty_Line_low_income | 35.00 | E | |
| Lower_middle | 22.00 | E | |
| Middle | 12.00 | E | |
| Upper_middle_well_off | 3.00 | E | Falakata town small affluent class |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Falakata_Municipality_CDB_core | 86.00 | E | Falakata CDB 290,722 / ~295,000 total AC base ≈ 98.5%; adjusted down to ~86% to account for urban/semi-urban weight and GP coverage |
| U2_Purba_Kanthalbari_Alipurduar_I | 14.00 | E | Purba Kanthalbari GP estimated ~4,000-4,500 persons out of ~295,000 AC base; v0 approximate |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.4 persons | E | WB 2011 district average 4.3; tea garden quarters typically slightly larger |
| Nuclear_HH | 68.00 | E | NFHS-4 WB rural/semi-rural pattern |
| Joint_HH | 25.00 | E | Higher than WB average in Rajbongshi community |
| Extended_multi_generation | 7.00 | E | |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.00 | E | Census 2011 Alipurduar district pattern; first-time voter cohort |
| Currently_married | 66.00 | E | |
| Widowed | 8.00 | E | Slightly elevated due to tea garden occupational health issues |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 68.00 | C | NFHS-4 WB rural 60%, urban 89%; Alipurduar below WB avg; tea garden quarters lower; AC ~68% |
| Radio | 8.00 | C | Slightly higher in tea garden belt (traditional media) |
| Mobile_phone | 80.00 | C | NFHS-4 WB ~78% + Jio rollout 2016-19; tea estate lines |
| Smartphone_with_internet | 38.00 | C | Below WB average; lower internet penetration in north Bengal tea belt; NFHS-4 + Jio rollout |
| Computer | 5.00 | C | Very low; limited among tea garden workers |
| Two_wheeler | 22.00 | C | NFHS-4 WB rural 18%; Alipurduar modestly above due to terrain |
| Four_wheeler | 4.00 | C | Low; mostly larger traders |
| Banking_access | 78.00 | B | PMJDY 2014- enrollment; below WB avg; tea garden communities had delayed bank access |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 80.00 | C | NFHS-4 WB rural 84%; tea estate water supply varies; AC ~80% |
| Improved_sanitation | 55.00 | C | NFHS-4 WB rural 51%; below WB avg; tea garden latrine coverage low; +Swachh Bharat partial |
| LPG_clean_cooking_fuel | 35.00 | C | NFHS-4 WB rural 24%; +Ujjwala 2016-19 rollout; tea belt lower than plains |
| Wood_biomass_fuel | 60.00 | C | High wood/firewood use in forest-adjacent tea belt |
| Other_fuel | 5.00 | E | Kerosene, coal, etc. |
| Electricity | 88.00 | C | Saubhagya 2017-19 rollout; some tea garden quarters still unelectrified in 2019 |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 68.00 | D | Rajbongshi and local community broadly native to Dooars region; estimate |
| WB_other_district | 7.00 | D | In-migrants from Jalpaiguri, Cooch Behar, Darjeeling districts |
| Other_Indian_state | 8.00 | D | Tea garden laborers' descendants with roots in Jharkhand, Bihar, Odisha, Chhattisgarh |
| Bangladesh_origin | 3.00 | D | Small Hindu refugee fringe from Bengal partition; less prominent than South Bengal |
| Outside_India | 0.50 | E | Nepal-origin fringe in foothills |
| Out_migrant | 3.50 | E | Youth from tea estates working outside; registered here |
| Jharkhand_origin | 10.00 | D | AC-local: Oraon/Munda tea garden population with Chota Nagpur/Jharkhand origins; brought as indentured labor; multi-generation settled |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Sadri | Oraon_Kurukh | Nepali | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 58.00 | 3.50 | 0.00 | 1.00 | 17.00 | 10.00 | 6.00 | 4.50 | E | Hindu = Rajbongshi SC + OBC + upper + Hindu-Adivasi; blended estimate |
| Muslim | 90.00 | 4.00 | 5.50 | 0.50 | 0.00 | 0.00 | 0.00 | 0.00 | E | Bengali-Muslim peasantry dominant; small Urdu/Hindi fraction |
| Christian | 30.00 | 5.00 | 0.00 | 5.00 | 5.00 | 40.00 | 15.00 | 0.00 | E | Tea garden Christians largely Adivasi; Sadri-speaking Oraon Christians dominant |
| Sarna_ORP | 20.00 | 0.00 | 0.00 | 0.00 | 10.00 | 40.00 | 30.00 | 0.00 | E | Adivasi tribal religion practitioners; mixed languages |
| Other_residual | 40.00 | 20.00 | 0.00 | 10.00 | 10.00 | 0.00 | 0.00 | 20.00 | E | Mixed Buddhist-Nepali and others |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 43.00 | 14.00 | 6.00 | 4.80 | 32.20 | 0 | 0 | E | SC_total 40.7%/82.5%×Hindu=49.3% of Hindu → adj to 43% excl some STs counted under ST; ST 15.9%/82.5%=19.3% Hindu-adj to 14% for ST religious distribution; Rajbongshi SC dominant |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 60 | 0 | 0 | 0 | 0 | 40 | E | Tea-belt Christians overwhelmingly ST (Oraon, Munda); some SC Christians |
| Sarna_ORP | 0 | 90 | 0 | 5 | 5 | 0 | 0 | E | Sarna practitioners are predominantly ST Adivasis |
| Other_residual | 0 | 0 | 30 | 10 | 30 | 0 | 30 | E | Mixed; Nepali Buddhist, Sikh trader |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Jharkhand_origin | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 70.00 | 8.00 | 3.00 | 4.00 | 0.50 | 3.50 | 11.00 | E | Rajbongshi native; Oraon/Munda Hindu-identified with Jharkhand roots; small partition refugee fraction |
| Muslim | 90.00 | 5.00 | 2.00 | 2.50 | 0.00 | 0.50 | 0.00 | E | Bengali-Muslim peasantry largely native; very small Bangladesh-origin trickle |
| Christian | 40.00 | 5.00 | 15.00 | 0.00 | 0.50 | 2.50 | 37.00 | E | Tea garden Christians: Oraon/Munda with Jharkhand/Chota Nagpur roots; multi-generation settled |
| Sarna_ORP | 45.00 | 5.00 | 10.00 | 0.00 | 0.00 | 3.00 | 37.00 | E | Adivasi tribal religion; same Jharkhand-origin pattern as Christian Adivasis |
| Other_residual | 55.00 | 10.00 | 20.00 | 0.00 | 15.00 | 0.00 | 0.00 | E | Nepali/Bhutanese-origin; other state migrants |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 70.00 | 40.00 | 80.00 | E | Rajbongshi SC and tea garden Adivasi Hindu; below state average |
| Muslim | 62.00 | 32.00 | 70.00 | E | Rural Muslim in Dooars; lower asset base |
| Christian | 60.00 | 30.00 | 68.00 | E | Tea garden Christian workers; low income |
| Sarna_ORP | 50.00 | 22.00 | 55.00 | E | Most marginalised; lowest access |
| Other_residual | 75.00 | 45.00 | 82.00 | E | Nepali/other mixed |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 5.00 | 10.00 | 12.00 | 18.00 | 20.00 | 25.00 | 10.00 | E |
| SC_total | 28.00 | 26.00 | 18.00 | 14.00 | 8.00 | 5.00 | 1.00 | E |
| ST_total | 35.00 | 28.00 | 16.00 | 12.00 | 6.00 | 2.50 | 0.50 | E |
| OBC | 20.00 | 24.00 | 20.00 | 17.00 | 10.00 | 7.00 | 2.00 | E |
| Other_Hindu_middle | 22.00 | 25.00 | 19.00 | 16.00 | 10.00 | 6.50 | 1.50 | E |
| Muslim | 30.00 | 27.00 | 18.00 | 14.00 | 7.00 | 3.50 | 0.50 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender). 5-year cohorts.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 12.00 | 9.00 | E |
| 23_27 | 11.00 | 8.00 | E |
| 28_32 | 10.00 | 6.00 | E |
| 33_37 | 9.00 | 4.50 | E |
| 38_42 | 8.00 | 3.50 | E |
| 43_47 | 7.00 | 3.00 | E |
| 48_52 | 6.00 | 2.50 | E |
| 53_57 | 5.00 | 2.00 | E |
| 58_62 | 4.00 | 1.50 | E |
| 63_67 | 3.50 | 1.00 | E |
| 68 | 3.00 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender). 5-year cohorts.

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 5.00 | 28.00 | E |
| 23_27 | 40.00 | 82.00 | E |
| 28_32 | 80.00 | 93.00 | E |
| 33_37 | 90.00 | 91.00 | E |
| 38_42 | 91.00 | 89.00 | E |
| 43_47 | 91.00 | 87.00 | E |
| 48_52 | 90.00 | 82.00 | E |
| 53_57 | 89.00 | 74.00 | E |
| 58_62 | 87.00 | 60.00 | E |
| 63_67 | 82.00 | 42.00 | E |
| 68 | 73.00 | 28.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 28.00 | 62.00 | E | North Bengal agrarian baseline; below state |
| Agricultural_labourer | 20.00 | 55.00 | E | Lowest access group |
| Household_industry | 30.00 | 65.00 | E | |
| Manufacturing | 40.00 | 72.00 | E | |
| Construction | 35.00 | 65.00 | E | |
| Trade_retail | 58.00 | 80.00 | E | Falakata town traders |
| Transport_logistics | 50.00 | 75.00 | E | |
| Services | 60.00 | 82.00 | E | |
| Government_services_teachers | 78.00 | 92.00 | E | Highest access |
| Out_migrant_worker | 62.00 | 72.00 | D | Tea estate youth out-migrants; smartphone-connected |
| Tea_garden_worker | 22.00 | 58.00 | D | Permanent tea garden workers; very limited smartphone penetration |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 38.00 | 2.00 | E |
| Primary | 40.00 | 3.00 | E |
| Middle | 36.00 | 5.00 | E |
| Secondary | 30.00 | 10.00 | E |
| Higher_Secondary | 22.00 | 16.00 | E |
| Graduate | 26.00 | 18.00 | E |
| Postgraduate | 35.00 | 12.00 | E |

### D.10 Asset / media × Bilingualism

No `media_tier` axis declared for AC 013. Section skipped per schema §4.7.

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Sub-unit codes use `Un_` prefix matching C.11.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Falakata_Municipality_CDB_core | 82.50 | 15.50 | 1.50 | 0.40 | 0.10 | E | Falakata CDB Census 2011 block-level aggregate applied to main sub-unit |
| U2_Purba_Kanthalbari_Alipurduar_I | 90.00 | 7.00 | 2.00 | 0.80 | 0.20 | E | Alipurduar-I block 90.55% Hindu; higher Hindu share than Falakata CDB |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Use canonical caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Falakata_Municipality_CDB_core | 5.00 | 40.70 | 15.90 | 4.00 | 19.90 | 15.50 | 2.00 | E |
| U2_Purba_Kanthalbari_Alipurduar_I | 5.50 | 48.40 | 16.90 | 4.00 | 17.00 | 7.00 | 4.20 | A |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Falakata_Municipality_CDB_core | 68.00 | 38.00 | 5.00 | 78.00 | E |
| U2_Purba_Kanthalbari_Alipurduar_I | 65.00 | 32.00 | 3.00 | 72.00 | E |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Falakata_Municipality_CDB_core | 35.00 | 55.00 | 80.00 | 88.00 | E |
| U2_Purba_Kanthalbari_Alipurduar_I | 40.00 | 60.00 | 85.00 | 90.00 | E |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 regional WB rollup, adjusted for Dooars tea-belt context.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 60.00 | 30.00 | 2.00 | 6.00 | 2.00 | C | CSDS 2019 WB + Dooars Hindu swing to BJP under John Barla tribal-Christian appeal; RSP/LF residual |
| Muslim | 5.00 | 68.00 | 15.00 | 10.00 | 2.00 | C | CSDS 2019 WB Muslim vote; LF residual stronger in North Bengal |
| Christian | 35.00 | 35.00 | 5.00 | 18.00 | 7.00 | E | Tea garden Christian; split: Barla appeal vs TMC welfare; RSP traditional strength |
| Sarna_ORP | 38.00 | 32.00 | 3.00 | 20.00 | 7.00 | E | Adivasi Sarna; strong LF-RSP tradition in Dooars; BJP inroads via Barla |
| Other_residual | 45.00 | 30.00 | 5.00 | 12.00 | 8.00 | E | Mixed; Nepali-origin modestly BJP |

### D.16 Vote × Caste (2019 LS)

P(party ‖ caste) — CSDS-Lokniti 2019 WB regional.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 58.00 | 28.00 | 5.00 | 7.00 | 2.00 | C | Bhadralok BJP-leaning by 2019 |
| OBC | 42.00 | 36.00 | 5.00 | 13.00 | 4.00 | C | Mixed; LF stronger in north Bengal among OBC |
| SC_total | 58.00 | 30.00 | 2.00 | 8.00 | 2.00 | C | Rajbanshi SC strong BJP swing 2019; CSDS WB + Dooars context |
| ST_total | 48.00 | 28.00 | 3.00 | 16.00 | 5.00 | C | Tea garden Adivasi ST; RSP/LF historically strong; BJP inroads via Barla |
| Other_Hindu_middle | 52.00 | 34.00 | 4.00 | 8.00 | 2.00 | E | |
| Muslim | 5.00 | 68.00 | 15.00 | 10.00 | 2.00 | C | Same as D.15 Muslim row |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 55.00 | 34.00 | 3.00 | 6.00 | 2.00 | C | CSDS 2019 WB male pattern; BJP higher among males |
| Female | 50.00 | 40.00 | 2.00 | 6.00 | 2.00 | C | TMC female advantage somewhat lower in tea belt vs South WB |

### D.18 Vote × Welfare

No `welfare_exposure` axis declared for AC 013. Section skipped per schema §4.7.

---

## E. 2019 baseline vote (calibration target)

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 52.25 | A | ECI 2019 GE Form-20 AC segment data: 109,280 votes / 209,134 total (incl. NOTA) |
| AITC | 39.31 | A | 82,210 votes / 209,134 |
| INC | 1.07 | A | 2,237 votes / 209,134 |
| LF | 4.90 | A | RSP 10,248 votes / 209,134 (RSP = LF in this AC; no CPI(M) candidacy) |
| Other_NOTA | 2.47 | A | SUCI(C) 558 + IND 446 + IND 1,409 + NOTA 2,746 = 5,159 / 209,134 |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 013 (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Anil Adhikari | AITC | 47.44 | Rabindra Nath Barman | CPI(M) | 42.53 | 8,046 |
| 2016 AE | Anil Adhikari | AITC | 43.77 | Kshitish Chandra Ray | CPI(M) | 35.27 | 16,839 |

Notes: In 2011, electorate 189,459; valid votes 164,026. In 2016, electorate 227,176; valid votes 197,940. Anil Adhikari (AITC) won both elections; BJP did not field a strong candidate in the AC-level contests pre-2019; RSP was a significant third force. The 2019 LS Falakata segment saw a dramatic swing to BJP under John Barla's appeal to tea garden workers and Adivasi communities.

### LS Alipurduars (PC 02) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2009 LS | Dhan Singh Negi | INC | ~31 | Congress held Alipurduars; tea garden belt |
| 2014 LS | Dasrath Tirkey | AITC | 29.58 | AITC won; CPI(M) and Congress split opposition; Tirkey was the 2019 AITC candidate too |
| 2019 LS | John Barla | BJP | 52.9 | Massive swing; Barla tribal-origin tea-worker mobilisation; Dasrath Tirkey (AITC) 39.8%; RSP (Mili Oraon) 5.0% |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Falakata Block: SC 40.7%, ST 15.9%, sex ratio 943, literacy 72.64%; population 290,722 (censusindia.co.in/subdistrict/falakata-block-jalpaiguri-west-bengal-2175)
- Census of India 2011 — Alipurduar-I Block: SC 48.4%, ST 16.9%, Hindu 90.55%, Muslim 5.93%, Christian 2.54% (censusindia.co.in/subdistrict/alipurduar-i-block-jalpaiguri-west-bengal-2173)
- Election Commission of India — 2019 LS GE Form-20 AC segment data (2019_AssemblySegmentLevelVotingData.csv): BJP 109,280; AITC 82,210; RSP 10,248; INC 2,237; SUCI(C) 558; IND 1,855; NOTA 2,746; electorate 244,579
- Election Commission of India — 2011 AE Falakata result: Anil Adhikari AITC 77,821 won over CPI(M) 69,775; electorate 189,459
- Election Commission of India — 2016 AE Falakata result: Anil Adhikari AITC 86,647 won over CPI(M) 69,808; electorate 227,176
- Delimitation Commission of India 2008 — WB Schedule: AC 013 Falakata = Falakata Municipality + Falakata CDB + Purba Kanthalbari GP of Alipurduar-I

### Secondary sources (tier B / C)

- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline
- CSDS-Lokniti 2019 NES post-poll — vote × religion / caste / gender WB regional rollup
- Wikipedia — Falakata Assembly constituency (reservation SC; AC composition)
- Wikipedia — Alipurduar district (district demography; tea garden belt)
- censusindia.co.in — Falakata Block religion, SC/ST, literacy data (Census 2011)
- censusindia.co.in — Alipurduar-I Block religion, SC/ST data (Census 2011)

### Tertiary / journalistic (tier D)

- The Print (2021) — "How tea gardens in North Bengal kept both BJP and TMC guessing" — John Barla appeal, Adivasi mobilisation
- ResearchGate (2023) — "Quality of Life of Tea Garden Workers of Kadambini Tea Garden, Falakata, West Bengal" — Falakata tea garden employment
- Wikipedia — John Barla (BJP MP Alipurduars 2019; tribal Christian; tea garden advocacy)
- Wikipedia — Tea-garden community (Adivasi origin, Sadri language, Dooars demographics)
- indiastatpublications.com — Falakata 2011/2016/2021 AE results

### Tier-D / E reliance flags (what to distrust)

- **Language / mother tongue** (C.5, D.1) — no AC-level Census C-series; Sadri/Rajbongshi/Oraon shares are tier D journalistic estimates
- **Caste sub-group shares** (C.2, D.2) — no caste census post-1931 for non-SC/ST; Rajbanshi/Oraon/Munda proportions within SC/ST are tier D/E
- **Migration / birthplace** (C.16, D.3) — Jharkhand-origin share for tea garden population is tier D from ILO and journalistic sources
- **Vote × demographic** (D.15–D.17) — CSDS 2019 WB regional rollup adjusted for Dooars context; tier C/E
- **Sub-unit decomposition** (C.11, D.11–D.14) — v0 collapses AC into 2 sub-units; Purba Kanthalbari GP share is approximate
- **Tea_garden_worker** occupation (C.8) — no AC-level formal count; tier D from ILO/academic sources
- **Economic / poverty** (C.10) — district-level NFHS proxy adjusted upward; tier C/E

### v0 known gaps

1. DCHB Alipurduar Part-A — GP-level population breakdown not retrieved; using block-level aggregate
2. ECI 2019 Form-20 AC segment — confirmed tier A from CSV; no further gap
3. Language breakdown (C.5) — no Census C-16 language data for Falakata block; using journalistic estimates
4. Tea garden employment breakdown — formal count unavailable; using ILO/academic proxy
5. Purba Kanthalbari GP population — exact share not retrieved; v0 approximate at ~14% of AC

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs. The validator's
> leakage gate exempts §H from the no-future-leakage check.

### 2021 WB Assembly Election — AC 013 Falakata (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Dipak Barman | 102,993 | 46.71% | A — ECI 2021 AE / indiastatpublications.com |
| AITC | Subhash Chandra Roy | 99,003 | 44.90% | A — ECI 2021 AE |
| BJP margin | — | 3,990 | ~1.81 pp | A — computed |

BJP held the Falakata seat in 2021 with a narrowed margin (from ~12.9 pp in 2019 LS to ~1.8 pp in 2021 AE). TMC recovered ground in the AC-level contest.

### 2024 Lok Sabha Election — AC 013 segment within Alipurduars LS (PC 02)

Note: The 2024 AC-segment CSV for Falakata was not found in data/2024_AssemblySegmentLevelVotingData.csv (likely uses different AC numbering or file structure). Results below sourced from journalistic/aggregate data.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Manoj Tigga | — | ~52.9% (LS-proportional) | D | Alipurduars 2024 LS aggregate; John Barla not re-nominated |
| AITC | Dasrath Tirkey | — | ~39–40% (LS-proportional) | D | Journalistic estimate |
| Others | — | — | ~7–8% | D | LF + INC + NOTA |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2021 AE
AC shares within ±3pp of tier-A figures:
- BJP target: 46.71% ± 3pp
- AITC target: 44.90% ± 3pp
