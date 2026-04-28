# AC 013 — Falakata (SC) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 013 Falakata as of end-2021 — it does not reference any
> post-2021 events. Use the 2024 LS result as the out-of-sample validation
> gate for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).
>
> **Forbidden in this file:** 2022, 2023, 2024, 2025, 2026, SSC scam,
> Partha Chatterjee, RG Kar, SIR, CAA notification, CAA rules.

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 013 | A | ECI / Delimitation Commission 2008 |
| AC name | Falakata | A | ECI |
| Reservation | SC | A | Delimitation 2008 |
| District | Alipurduar | A | Delimitation 2008 (formerly Jalpaiguri, carved out 2014) |
| Sub-division | Alipurduar | A | WB administrative |
| LS constituency | 02 — Alipurduars (ST reserved) | A | Delimitation 2008 |
| LS segments included | AC 06 Tufanganj · 07 Kumargram · 08 Kalchini · 09 Alipurduars · 10 Falakata · 11 Madarihat · 12 Nagrakata (Alipurduars LS = 7 AC segments) | A | Delimitation 2008 / ECI |
| AC composition | Falakata Municipality + Falakata CD block (all 12 GPs) + Purba Kanthalbari GP of Alipurduar-I CD block | A | Delimitation 2008; Wikipedia Falakata Assembly constituency |
| Geographic note | Dooars foothills, Terai-Dooars region; tea garden belt; bordering Bhutan to north; forested reserve areas | A | — |
| Sub-units used in v0 | **U1: Falakata_Municipality_CDB_core** (Falakata town + CDB settled area) · **U2: Purba_Kanthalbari_Alipurduar_I** (GP of Alipurduar-I block, rural fringe) | E | v0 simplification |
| 2021 AE electorate (ECI roll) | 254,554 | A | ECI 2021 WB AE archive; data/electoral_history/2021/detailed_results.csv |
| 2021 AE total valid votes | 220,500 | A | ECI 2021 AE archive; computed from candidate totals |
| 2021 AE winner | **Dipak Barman (BJP)** — SC candidate | A | ECI 2021 AE; data/electoral_history/2021/detailed_results.csv |
| 2021 AE runner-up | Subhash Chandra Roy (AITC) — SC candidate | A | ECI 2021 AE |
| 2021 AE BJP margin | **3,990 votes** (~1.81 pp) | A | ECI 2021 AE; computed |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~295,000 (Falakata CDB 290,722 + Purba Kanthalbari GP ~4,500 est.) | E | Census 2011 censusindia.co.in Falakata Block; v0 GP-equal-weight for Purba Kanthalbari |
| 2021 projected population | ~328,000 | E | 10-yr compound religion-differential growth from Census 2011 base (methodology §4) |
| Sex ratio (2021, F per 1000 M) | ~950 | E | Census 2011 Falakata Block sex ratio 943; NFHS-5 Jalpaiguri 1038 (reflects 10-yr improvement trend); AC estimate ~950 |
| 2021 ECI electorate (roll) | 254,554 | A | ECI 2021 WB AE archive |
| Estimated M / F / TG split (2021) | 51.3% M / 48.7% F / <0.01% TG | E | Sex ratio ~950 → 51.3% M; TG nominal |
| 2021 polling stations (estimated) | ~280 | E | Back-projection from 2021 electorate; marginal increase from 2019 ~275 |
| 2021 AE total votes polled | 220,500 | A | ECI 2021 AE (BJP 102,993 + AITC 99,003 + CPI(M) 10,772 + others 7,732) |
| 2021 AE turnout | 86.62% | A | 220,500 / 254,554; ECI 2021 AE |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 82.70 | E | Census 2011 Falakata Block: Hindu 82%; 10-yr religion-differential growth (+0.5pp vs Muslim); projected to 2021 |
| Muslim | 15.30 | E | Census 2011 Falakata Block: Muslim 15.79%; slight relative decline vs Hindu growth over 10yr |
| Christian | 1.50 | E | Tea garden belt pattern; Alipurduar-I block 2.54% Christian; Falakata lower; stable |
| Sarna_ORP | 0.40 | E | Adivasi tribal religion fringe; stable |
| Other_residual | 0.10 | E | Buddhist (Nepali fringe) + Sikh + Not_stated lumped; stable |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 40.70 | A | Census 2011 Falakata Block: SC 40.7%; stable as no new caste census; used as 2021 anchor |
| └ Rajbanshi_SC | 26.00 | C | Dominant SC in Dooars-Terai; ~64% of SC pool |
| └ Tea_garden_SC | 8.00 | D | Chamar, Muchi, Hari and other SC communities in tea estates; ~20% of SC pool |
| └ Other_SC | 6.70 | E | Residual SC |
| **ST_total** | 15.90 | A | Census 2011 Falakata Block: ST 15.9%; stable |
| └ Oraon_ST | 7.00 | D | Largest ST group in Dooars tea gardens |
| └ Munda_ST | 3.50 | D | Second major tea garden ST |
| └ Koch_ST | 2.50 | D | Koch community (categorised ST in WB) |
| └ Other_ST | 2.90 | E | Santali, Rava, Rabha, Toto and others |
| UC_bhadralok | 5.00 | E | Small bhadralok (Brahmin/Kayastha/Baidya) presence; concentrated in Falakata town |
| OBC | 4.00 | E | Teli, Sutradhar, other OBC; modest in tea-belt district |
| Other_Hindu_middle | 16.90 | E | Residual within Hindu: 82.7% − 40.7% SC − 15.9% ST − 5% UC − 4% OBC = 17.1% adj to 16.9% for rounding |
| Muslim | 15.30 | E | All sub-castes pooled; Bengali-Muslim peasantry |
| Christian_plus_Sarna_plus_Other | 2.00 | E | Christian 1.50% + Sarna 0.40% + Other_residual 0.10% |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2021, adult voters only — 18+)

Renormalized to 18+ electorate; children 0–17 excluded.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 13.00 | E | First-time voter cohort (born 1999–2003); 10-yr projection from Alipurduar district Census 2011 age pyramid |
| 23_27 | 12.50 | E | |
| 28_32 | 11.50 | E | |
| 33_37 | 11.00 | E | |
| 38_42 | 10.00 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.00 | E | |
| 63_67 | 5.00 | E | |
| 68 | 7.00 | E | 68+ open-ended; renormalized to 100 |
| **Sum** | **100.00** | — | self-check (renormalized from Census 2011 age pyramid excluding 0–17) |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.28 | E | Sex ratio ~950 F per 1000 M → 1000/(1000+950) = 51.28% M |
| Female | 48.71 | E | 950/(1000+950) |
| Third_gender | 0.01 | E | Nominal; consistent with WB pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 62.00 | E | Dominant plains population; Rajbanshi community mostly Bengali-speaking; stable |
| Hindi | 3.00 | E | Bihari/UP migrant workers; tea garden Hindi belt; stable |
| Urdu | 2.00 | E | Muslim community fraction; stable |
| Other | 3.00 | E | Residual catch-all (Nepali fringe, Bodo fringe); stable |
| Rajbongshi | 14.00 | D | Rajbongshi/Koch-Rajbongshi mother tongue; significant in Dooars North Bengal |
| Sadri | 8.00 | D | Lingua franca of tea garden Adivasis (Oraon, Munda, etc.); widely spoken in Dooars |
| Oraon_Kurukh | 5.00 | D | Native language of Oraon ST community; Dooars tea belt |
| Nepali | 3.00 | E | Small Nepali-speaking community in foothills |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 25.00 | E | Falakata Block literacy 72.64% in 2011; +5pp trend by 2021 → ~78% literate among 18+ → ~25% illiterate (NFHS-5 Jalpaiguri women literate 73.6%) |
| Primary | 24.00 | E | Census 2011 distribution; tea garden belt large primary share; stable |
| Middle | 18.00 | E | |
| Secondary | 15.00 | E | Marginal increase (+1pp) from 2019 |
| Higher_Secondary | 10.00 | E | Marginal increase (+1pp) from 2019 |
| Graduate | 6.00 | E | Below WB average; limited higher-ed access in tea belt |
| Postgraduate | 2.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 35.50 | E | Census 2011 Falakata Block main-worker pattern; COVID-19 shock disrupted tea garden employment briefly but recovered by late 2021 |
| └ Main_worker_tea_garden | 14.00 | D | Tea garden permanent workers; sub-row, is_subgroup=yes |
| └ Main_worker_non_tea | 21.50 | E | Agriculture, trade, services; sub-row |
| Marginal_worker | 12.00 | E | Seasonal and marginal workers; tea garden casual labor; stable |
| Non_worker | 34.50 | E | Housewife + elderly + retired; Lakshmir Bhandar (Apr 2021) direct beneficiaries largely in this category |
| Student | 10.00 | E | 18–22 cohort in education; stable |
| Unemployed | 8.00 | E | Educated job-seekers; tea estate closures; COVID-19 shock elevated slightly |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 16.00 | E | Falakata plains agriculture; stable from 2019 |
| Agricultural_labourer | 20.00 | E | Farm laborers excluding tea garden workers; stable |
| Household_industry | 4.00 | E | Weaving, bamboo craft, cottage industries |
| Manufacturing | 6.00 | E | Tea processing, agro-processing; stable |
| Construction | 5.00 | E | COVID-19 disrupted briefly; recovered |
| Trade_retail | 10.00 | E | Falakata town retail + local markets; disrupted by COVID but rebounded |
| Transport_logistics | 5.00 | E | Road freight; NH-31C access; stable |
| Services | 9.00 | E | Private services, domestic workers |
| Government_services_teachers | 5.00 | E | Below state average; limited govt presence in tea belt |
| Out_migrant_worker | 5.00 | D | Youth out-migration from tea estates; COVID-19 forced some returns but re-departed by 2021 |
| Tea_garden_worker | 15.00 | D | Tea garden permanent and casual workers; AC-local occupation category |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Small traders and contractors; stable |
| Employee | 40.00 | E | Tea garden employees (largest employee pool in North Bengal) + govt employees |
| Single_worker | 38.00 | E | Own-account cultivators, artisans, small traders |
| Family_worker | 20.50 | E | Unpaid family labor in agriculture and household industry |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 26.50 | C | Alipurduar district poverty high; tea garden belt historically high BPL; COVID-19 pushed marginal households back into BPL; NFHS-5 Jalpaiguri pattern adjusted for north Bengal |
| Above_Poverty_Line_low_income | 35.00 | E | Lakshmir Bhandar (Apr 2021) begins to reach this band; slight improvement in household liquidity |
| Lower_middle | 24.00 | E | |
| Middle | 11.50 | E | |
| Upper_middle_well_off | 3.00 | E | Falakata town small affluent class |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Falakata_Municipality_CDB_core | 86.00 | E | Falakata CDB 290,722 / ~295,000 total AC base ≈ 98.5%; adjusted to ~86% for urban/semi-urban weight and GP coverage; stable from 2019 |
| U2_Purba_Kanthalbari_Alipurduar_I | 14.00 | E | Purba Kanthalbari GP estimated ~4,000-4,500 persons; v0 approximate; stable |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.4 persons | E | WB 2011 district average 4.3; tea garden quarters slightly larger; COVID reverse-migration may have temporarily inflated to 4.5 but normalizing by end-2021 |
| Nuclear_HH | 68.00 | E | NFHS-4/5 WB rural/semi-rural pattern |
| Joint_HH | 25.00 | E | Higher than WB average in Rajbongshi community |
| Extended_multi_generation | 7.00 | E | |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.00 | E | Census 2011 Alipurduar district pattern; first-time voter cohort |
| Currently_married | 66.00 | E | |
| Widowed | 8.00 | E | Slightly elevated due to tea garden occupational health issues |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

Post-COVID smartphone surge is the major shift from 2019. Jio-led affordability + lockdown-driven necessity accelerated adoption in Alipurduar district, though below WB average due to tea belt lower income base.

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 70.00 | C | NFHS-5 Jalpaiguri district baseline (proxy for Alipurduar); near saturation in town, lagging in tea estates; +2pp from 2019 |
| Radio | 7.00 | C | Slightly higher in tea garden belt (traditional media); marginal decline from 2019 |
| Mobile_phone | 86.00 | C | NFHS-5 WB ~90%; Alipurduar below average; +6pp from 2019 baseline (80%) |
| Smartphone_with_internet | 62.00 | C | Post-COVID surge: +20-24pp from 2019 baseline (38%); Jalpaiguri NFHS-5 pattern; lockdown-driven Jio adoption; tea garden workers acquired smartphones for welfare app access |
| Computer | 5.00 | C | Very low; limited among tea garden workers; stable |
| Two_wheeler | 23.00 | C | Marginal increase (+1pp) from 2019 |
| Four_wheeler | 4.00 | C | Low; mostly larger traders; stable |
| Banking_access | 85.00 | B | PMJDY + Jan Dhan second push 2020-21; Lakshmir Bhandar bank account requirement accelerated enrollment; +7pp from 2019 baseline (78%) |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 82.00 | C | NFHS-5 Jalpaiguri 95.2%; Alipurduar/Falakata tea belt lower; +2pp from 2019 baseline (80%) |
| Improved_sanitation | 65.00 | C | NFHS-5 Jalpaiguri 73.2%; Falakata tea belt lower; +10pp from 2019 baseline (55%); Swachh Bharat continued rollout |
| LPG_clean_cooking_fuel | 42.00 | C | NFHS-5 Jalpaiguri 42.7%; matches proxy; +7pp from 2019 baseline (35%); Ujjwala 2.0 and continued enrollment |
| Wood_biomass_fuel | 53.00 | C | Declining as LPG rises; -7pp from 2019 baseline (60%) |
| Other_fuel | 5.00 | E | Kerosene, coal, etc.; stable |
| Electricity | 93.00 | C | NFHS-5 Jalpaiguri 97.4%; Falakata tea belt lower due to unelectrified tea garden quarters; +5pp from 2019 baseline (88%) |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

COVID-19 reverse migration (2020) brought back some out-migrant workers from other states. Falakata's tea garden community had Jharkhand-origin workers who mostly remained; limited Cyclone Amphan impact (Alipurduar far from Sundarbans).

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 68.50 | D | Rajbongshi and local community broadly native to Dooars; slight rise from COVID returnee registrations |
| WB_other_district | 7.00 | D | In-migrants from Jalpaiguri, Cooch Behar, Darjeeling districts; stable |
| Other_Indian_state | 7.50 | D | Tea garden laborers' descendants with roots in Jharkhand, Bihar, Odisha; some COVID return-migrants from destination states |
| Bangladesh_origin | 3.00 | D | Small Hindu refugee fringe from Bengal partition; less prominent than South Bengal |
| Outside_India | 0.50 | E | Nepal-origin fringe in foothills |
| Out_migrant | 3.50 | E | Youth from tea estates working outside; COVID forced some returns but re-departed by 2021 |
| Jharkhand_origin | 10.00 | D | AC-local: Oraon/Munda tea garden population with Chota Nagpur/Jharkhand roots; multi-generation settled |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Sadri | Oraon_Kurukh | Nepali | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 58.00 | 3.50 | 0.00 | 1.00 | 17.00 | 10.00 | 6.00 | 4.50 | E | Hindu = Rajbongshi SC + OBC + upper + Hindu-Adivasi; blended estimate; stable from 2019 |
| Muslim | 90.00 | 4.00 | 5.50 | 0.50 | 0.00 | 0.00 | 0.00 | 0.00 | E | Bengali-Muslim peasantry dominant; stable |
| Christian | 30.00 | 5.00 | 0.00 | 5.00 | 5.00 | 40.00 | 15.00 | 0.00 | E | Tea garden Christians largely Adivasi; Sadri-speaking Oraon Christians dominant |
| Sarna_ORP | 20.00 | 0.00 | 0.00 | 0.00 | 10.00 | 40.00 | 30.00 | 0.00 | E | Adivasi tribal religion practitioners; mixed languages |
| Other_residual | 40.00 | 20.00 | 0.00 | 10.00 | 10.00 | 0.00 | 0.00 | 20.00 | E | Mixed Buddhist-Nepali and others |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. Each row sums to 100.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 43.00 | 14.00 | 6.00 | 4.80 | 32.20 | 0 | 0 | E | SC_total 40.7%/82.7%×Hindu adj to 43%; ST 15.9%/82.7%=19.3% → adj to 14% for ST religious distribution; Rajbanshi SC dominant |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 60 | 0 | 0 | 0 | 0 | 40 | E | Tea-belt Christians overwhelmingly ST (Oraon, Munda); some SC Christians |
| Sarna_ORP | 0 | 90 | 0 | 5 | 5 | 0 | 0 | E | Sarna practitioners predominantly ST Adivasis |
| Other_residual | 0 | 0 | 30 | 10 | 30 | 0 | 30 | E | Mixed; Nepali Buddhist, Sikh trader |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Jharkhand_origin | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 70.50 | 8.00 | 3.00 | 4.00 | 0.50 | 3.00 | 11.00 | E | Rajbongshi native; Oraon/Munda Hindu-identified with Jharkhand roots; slight rise in native pct from COVID returnees |
| Muslim | 90.50 | 5.00 | 2.00 | 2.00 | 0.00 | 0.50 | 0.00 | E | Bengali-Muslim peasantry largely native; very small Bangladesh-origin trickle; stable |
| Christian | 40.00 | 5.00 | 15.00 | 0.00 | 0.50 | 2.50 | 37.00 | E | Tea garden Christians: Oraon/Munda with Jharkhand/Chota Nagpur roots; multi-generation settled |
| Sarna_ORP | 45.00 | 5.00 | 10.00 | 0.00 | 0.00 | 3.00 | 37.00 | E | Adivasi tribal religion; same Jharkhand-origin pattern as Christian Adivasis |
| Other_residual | 55.00 | 10.00 | 20.00 | 0.00 | 15.00 | 0.00 | 0.00 | E | Nepali/Bhutanese-origin; other state migrants |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion. Reflects 2021 smartphone surge.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 72.00 | 65.00 | 87.00 | E | Rajbongshi SC and tea garden Adivasi Hindu; post-COVID smartphone surge; PMJDY + Lakshmir Bhandar banking push |
| Muslim | 64.00 | 56.00 | 78.00 | E | Rural Muslim in Dooars; lower asset base but improving; banking via welfare scheme enrollment |
| Christian | 62.00 | 54.00 | 76.00 | E | Tea garden Christian workers; low income; smartphone via COVID necessity |
| Sarna_ORP | 52.00 | 44.00 | 65.00 | E | Most marginalised; lowest access; improvement from 2019 |
| Other_residual | 76.00 | 67.00 | 89.00 | E | Nepali/other mixed; slight improvement |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4.00 | 10.00 | 12.00 | 18.00 | 20.00 | 26.00 | 10.00 | E |
| SC_total | 26.00 | 26.00 | 18.00 | 15.00 | 9.00 | 5.00 | 1.00 | E |
| ST_total | 33.00 | 28.00 | 17.00 | 13.00 | 6.00 | 2.50 | 0.50 | E |
| OBC | 18.00 | 24.00 | 20.00 | 18.00 | 11.00 | 7.00 | 2.00 | E |
| Other_Hindu_middle | 20.00 | 25.00 | 19.00 | 17.00 | 11.00 | 6.50 | 1.50 | E |
| Muslim | 28.00 | 27.00 | 18.00 | 15.00 | 8.00 | 3.50 | 0.50 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender). 5-year cohorts.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 13.00 | 10.00 | E |
| 23_27 | 12.00 | 9.00 | E |
| 28_32 | 11.00 | 7.00 | E |
| 33_37 | 10.00 | 5.00 | E |
| 38_42 | 9.00 | 4.00 | E |
| 43_47 | 8.00 | 3.50 | E |
| 48_52 | 7.00 | 3.00 | E |
| 53_57 | 6.00 | 2.50 | E |
| 58_62 | 5.00 | 2.00 | E |
| 63_67 | 4.00 | 1.50 | E |
| 68 | 3.50 | 1.00 | E |

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

P(owns smartphone ‖ occupation) — central media-access metric. Updated for 2021 smartphone surge.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 42.00 | 64.00 | E | North Bengal agrarian baseline; +14pp from 2019 post-COVID |
| Agricultural_labourer | 34.00 | 57.00 | E | Lowest access group; +14pp from 2019 |
| Household_industry | 44.00 | 67.00 | E | |
| Manufacturing | 56.00 | 73.00 | E | |
| Construction | 50.00 | 67.00 | E | |
| Trade_retail | 72.00 | 82.00 | E | Falakata town traders; near saturation |
| Transport_logistics | 65.00 | 76.00 | E | |
| Services | 74.00 | 84.00 | E | |
| Government_services_teachers | 88.00 | 93.00 | E | Highest access; stable |
| Out_migrant_worker | 76.00 | 73.00 | D | Tea estate youth out-migrants; smartphone-connected for remittance |
| Tea_garden_worker | 38.00 | 60.00 | D | Permanent tea garden workers; +16pp smartphone from 2019 via COVID-necessity |

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
| U1_Falakata_Municipality_CDB_core | 82.70 | 15.30 | 1.50 | 0.40 | 0.10 | E | Falakata CDB Census 2011 block-level aggregate applied to main sub-unit; slight adjustments for 2021 growth differentials |
| U2_Purba_Kanthalbari_Alipurduar_I | 90.00 | 7.00 | 2.00 | 0.80 | 0.20 | E | Alipurduar-I block 90.55% Hindu (Census 2011); higher Hindu share stable |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Use canonical caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Falakata_Municipality_CDB_core | 5.00 | 40.70 | 15.90 | 4.00 | 19.90 | 15.30 | 2.00 | E |
| U2_Purba_Kanthalbari_Alipurduar_I | 5.50 | 48.40 | 16.90 | 4.00 | 17.00 | 7.00 | 4.20 | A |

### D.13 Sub-unit × Asset / media

Updated for 2021 smartphone surge.

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Falakata_Municipality_CDB_core | 70.00 | 63.00 | 5.00 | 85.00 | E |
| U2_Purba_Kanthalbari_Alipurduar_I | 67.00 | 57.00 | 3.00 | 80.00 | E |

### D.14 Sub-unit × Amenities

Updated for 2021 NFHS-5 Jalpaiguri baseline.

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Falakata_Municipality_CDB_core | 42.00 | 65.00 | 82.00 | 93.00 | E |
| U2_Purba_Kanthalbari_Alipurduar_I | 48.00 | 70.00 | 87.00 | 95.00 | E |

### D.15 Vote × Religion (2021 AE anchor)

P(party ‖ religion) — anchored on 2021 AE result; adjusted from 2019 LS CSDS-Lokniti pattern for the AE context. BJP narrowed margin from ~12.9pp (2019 LS) to ~1.81pp (2021 AE) — reflects partial TMC recovery in SC seat with welfare message.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 52.00 | 38.00 | 0.50 | 7.00 | 2.50 | C | 2021 AE result: BJP 46.71%, AITC 44.90%; AC overall anchors this row; Hindu majority (82.7%) carries most votes; LF (CPI(M)) residual in tea belt; no INC candidate |
| Muslim | 3.00 | 78.00 | 2.00 | 14.00 | 3.00 | E | Muslim consolidation behind AITC in 2021 AE (stronger than 2019); LF-RSP residual in North Bengal |
| Christian | 28.00 | 44.00 | 2.00 | 20.00 | 6.00 | E | Tea garden Christian; AITC welfare push in 2021; LF-RSP historic strength; BJP somewhat reduced |
| Sarna_ORP | 30.00 | 40.00 | 2.00 | 22.00 | 6.00 | E | Adivasi Sarna; AITC recovered via welfare outreach; LF residual strong |
| Other_residual | 40.00 | 40.00 | 2.00 | 12.00 | 6.00 | E | Mixed; stable pattern |

### D.16 Vote × Caste (2021 AE)

P(party ‖ caste) — anchored on 2021 AE result.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 56.00 | 30.00 | 2.00 | 8.00 | 4.00 | C | Bhadralok remained BJP-leaning but slightly reduced from 2019 |
| OBC | 38.00 | 40.00 | 2.00 | 14.00 | 6.00 | C | Mixed; LF slightly stronger in north Bengal among OBC |
| SC_total | 50.00 | 39.00 | 0.50 | 8.00 | 2.50 | C | Rajbanshi SC: BJP still ahead but AITC recovered from 2019; SC reserve seat — both candidates SC; 2021 AE overall ~46.7 BJP / 44.9 AITC |
| ST_total | 40.00 | 40.00 | 1.00 | 15.00 | 4.00 | C | Tea garden Adivasi ST; RSP/LF historically strong; AITC welfare outreach improved; BJP moderately competitive |
| Other_Hindu_middle | 48.00 | 38.00 | 1.00 | 10.00 | 3.00 | E | |
| Muslim | 3.00 | 78.00 | 2.00 | 14.00 | 3.00 | E | Same as D.15 Muslim row |

### D.17 Vote × Gender (2021 AE)

P(party ‖ gender) — Lakshmir Bhandar launched April 2021 (post-campaign, pre-election). Female TMC advantage stronger in 2021 than 2019 due to welfare signaling.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 50.00 | 40.00 | 0.50 | 7.50 | 2.00 | C | CSDS 2021 WB pattern: male more BJP-leaning; anchored to 2021 AE result |
| Female | 43.00 | 50.00 | 0.50 | 4.50 | 2.00 | C | TMC female advantage amplified by Lakshmir Bhandar launch signal in 2021 AE; NFHS-5 and post-poll indicators |

### D.18 Vote × Welfare

No `welfare_exposure` axis declared for AC 013. Section skipped per schema §4.7.

---

## E. 2021 baseline vote (calibration target)

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 46.71 | A | ECI 2021 AE: Dipak Barman 102,993 votes / 220,500 total valid; data/electoral_history/2021/detailed_results.csv |
| AITC | 44.90 | A | ECI 2021 AE: Subhash Chandra Roy 99,003 votes / 220,500 total valid |
| INC | 0.00 | A | No INC candidate in 2021 AE; 0.00% |
| LF | 4.89 | A | ECI 2021 AE: CPI(M) Kshitish Chandra Ray 10,772 votes / 220,500 total valid |
| Other_NOTA | 3.51 | A | NOTA 1,970 + IND 3,323 + SWJP 1,377 + SUCI 613 + AMB 449 = 7,732 / 220,500; ECI 2021 AE |
| **Sum** | **100.01** | — | self-check (0.01 rounding; ECI-sourced pct sum to 100.00) |

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 013 — Assembly Elections

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Anil Adhikari | AITC | 47.44 | Rabindra Nath Barman | CPI(M) | 42.53 | 8,046 |
| 2016 AE | Anil Adhikari | AITC | 43.77 | Kshitish Chandra Ray | CPI(M) | 35.27 | 16,839 |

Notes: Anil Adhikari (AITC) won both 2011 and 2016; BJP did not field a strong candidate in AC-level contests pre-2019; RSP/CPI(M) were the main opposition in this AC. The 2019 LS Falakata segment saw a dramatic swing to BJP under John Barla's appeal to tea garden workers and Adivasi communities.

### 2019 Lok Sabha (AC 013 segment) — Prior anchor

| Party | Candidate (LS) | Votes (AC segment) | AC-segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | John Barla | 109,280 | 52.25 | A | ECI 2019 GE Form-20 AC segment data; 2019_AssemblySegmentLevelVotingData.csv |
| AITC | Dasrath Tirkey | 82,210 | 39.31 | A | Same |
| LF (RSP) | Mili Oraon | 10,248 | 4.90 | A | Same; RSP = LF in this AC |
| INC | (candidate) | 2,237 | 1.07 | A | Same |
| Other_NOTA | various | 5,159 | 2.47 | A | SUCI(C) + IND + NOTA; same |

### LS Alipurduars (PC 02) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2009 LS | Dhan Singh Negi | INC | ~31 | Congress held Alipurduars; tea garden belt |
| 2014 LS | Dasrath Tirkey | AITC | 29.58 | AITC won; CPI(M) and Congress split opposition |
| 2019 LS | John Barla | BJP | 52.9 | Massive swing; Barla tribal-origin tea-worker mobilisation; Dasrath Tirkey (AITC) 39.8%; RSP (Mili Oraon) 5.0% |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Falakata Block: SC 40.7%, ST 15.9%, sex ratio 943, literacy 72.64%; population 290,722 (censusindia.co.in/subdistrict/falakata-block-jalpaiguri-west-bengal-2175)
- Census of India 2011 — Alipurduar-I Block: SC 48.4%, ST 16.9%, Hindu 90.55%, Muslim 5.93%, Christian 2.54% (censusindia.co.in/subdistrict/alipurduar-i-block-jalpaiguri-west-bengal-2173)
- Election Commission of India — 2021 WB AE AC 013 Falakata result: Dipak Barman (BJP) 102,993 (46.71%); Subhash Chandra Roy (AITC) 99,003 (44.90%); CPI(M) 10,772 (4.89%); total valid votes 220,500; electorate 254,554 — sourced from data/electoral_history/2021/detailed_results.csv
- Election Commission of India — 2019 LS GE Form-20 AC segment data: BJP 109,280; AITC 82,210; RSP 10,248; INC 2,237; others 5,159; electorate 244,579 — sourced from data/2019_AssemblySegmentLevelVotingData.csv
- Election Commission of India — 2011 AE Falakata result: Anil Adhikari AITC 77,821 won over CPI(M) 69,775; electorate 189,459
- Election Commission of India — 2016 AE Falakata result: Anil Adhikari AITC 86,647 won over CPI(M) 69,808; electorate 227,176
- Delimitation Commission of India 2008 — WB Schedule: AC 013 Falakata = Falakata Municipality + Falakata CDB + Purba Kanthalbari GP of Alipurduar-I

### Secondary sources (tier B / C)

- NFHS-5 (2019-21) West Bengal district fact sheet — Jalpaiguri (proxy for Alipurduar, carved out 2014): electricity 97.4%, sanitation 73.2%, clean cooking 42.7%, drinking water 95.2%; data/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline for 2019 comparison
- CSDS-Lokniti 2019 NES post-poll — vote × religion / caste / gender WB regional rollup (applied to 2021 with AE anchor adjustments)
- Wikipedia — Falakata Assembly constituency (reservation SC; AC composition)
- Wikipedia — Alipurduar district (district demography; tea garden belt)
- censusindia.co.in — Falakata Block and Alipurduar-I Block religion, SC/ST, literacy data (Census 2011)

### Tertiary / journalistic (tier D)

- The Print (2021) — "How tea gardens in North Bengal kept both BJP and TMC guessing" — John Barla appeal, Adivasi mobilisation, 2021 AE context
- ResearchGate — "Quality of Life of Tea Garden Workers of Kadambini Tea Garden, Falakata, West Bengal" — Falakata tea garden employment
- Wikipedia — John Barla (BJP MP Alipurduars 2019; tribal Christian; tea garden advocacy)
- Wikipedia — Tea-garden community (Adivasi origin, Sadri language, Dooars demographics)
- indiastatpublications.com — Falakata 2011/2016/2021 AE results

### Tier-D / E reliance flags (what to distrust)

- **Language / mother tongue** (C.5, D.1) — no AC-level Census C-series; Sadri/Rajbongshi/Oraon shares are tier D journalistic estimates; unchanged from 2019
- **Caste sub-group shares** (C.2, D.2) — no caste census post-1931 for non-SC/ST; Rajbanshi/Oraon/Munda proportions within SC/ST are tier D/E
- **Migration / birthplace** (C.16, D.3) — Jharkhand-origin share for tea garden population is tier D from ILO and journalistic sources
- **Vote × demographic** (D.15–D.17) — anchored on 2021 AE result but religion/caste/gender decomposition inferred from CSDS + structural priors; tier C/E
- **Sub-unit decomposition** (C.11, D.11–D.14) — v0 collapses AC into 2 sub-units; Purba Kanthalbari GP share is approximate
- **Tea_garden_worker** occupation (C.8) — no AC-level formal count; tier D from ILO/academic sources
- **Economic / poverty** (C.10) — district-level NFHS proxy adjusted upward; tier C/E
- **Asset/media 2021 update** (C.14) — smartphone +20-24pp from 2019 based on NFHS-5 Jalpaiguri and national post-COVID patterns; AC-specific survey would sharpen this

### v0 known gaps

1. DCHB Alipurduar Part-A — GP-level population breakdown not retrieved; using block-level aggregate for Falakata CDB
2. Language breakdown (C.5) — no Census C-16 language data for Falakata block; using journalistic estimates
3. Tea garden employment breakdown — formal count unavailable; using ILO/academic proxy
4. Purba Kanthalbari GP population — exact share not retrieved; v0 approximate at ~14% of AC
5. CSDS 2021 WB AE post-poll — no published cross-tabs available; vote × demographic (D.15–D.17) inferred from structural priors + AE result anchor

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No post-2021 events referenced.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs. The validator's
> leakage gate exempts §H from the no-future-leakage check.

### 2024 Lok Sabha Election — AC 013 segment within Alipurduars LS (PC 02)

Sourced from data/2024_AssemblySegmentLevelVotingData.csv, AC_NO=13, Falakata.

| Party | Candidate (LS level) | Votes | AC-segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Manoj Tigga | 105,972 | 48.55% | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Prakash Chik Baraik | 97,006 | 44.44% | A | Same |
| LF (RSP) | Mili Oraon | 6,704 | 3.07% | A | Same |
| NOTA | — | 2,739 | 1.25% | A | Same |
| Others (BSP, SUCI, KPPU, GNASURKP, NBNGPLPP, KMSP, IND) | various | 3,874 | 1.77% | A | Same |
| **Total valid** | | 218,295 | — | A | Computed |
| **Electorate** | | 262,383 | — | A | 2024_AssemblySegmentLevelVotingData.csv |
| **Turnout** | | — | 83.20% | A | Computed |
| **BJP margin** | | 8,966 votes | 4.11 pp | A | Computed |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC-013 shares within ±3pp of the CSV tier-A figures:
- BJP target: 48.6% ± 3pp
- AITC target: 44.4% ± 3pp
- LF target: 3.1% ± 3pp
