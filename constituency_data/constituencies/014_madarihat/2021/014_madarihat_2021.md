# AC 014 — Madarihat (ST) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 014 Madarihat as of end-2021 — it does not reference any
> post-2021 events. Use post-2021 elections (2024 LS) as out-of-sample
> validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../NORMALIZED_SCHEMA.md)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 014 | A | ECI / Delimitation Commission 2008 |
| AC name | Madarihat | A | ECI |
| Reservation | ST | A | Delimitation 2008 |
| District | Alipurduar | A | Delimitation 2008 (Alipurduar district formed 2014 from Jalpaiguri) |
| Sub-division | Alipurduar | A | WB administrative |
| LS constituency | 01 — Alipurduar (ST reserved) | A | Delimitation 2008 |
| LS segments included | AC 01 Kumargram · 02 Kalchini · 03 Alipurduar · 04 Falakata · 05 Madarihat · 06 Dhupguri · 07 Nagrakata | A | Delimitation 2008 |
| AC composition | Madarihat-Birpara CD Block (part) covering Madarihat GP, Birpara GP, Jaigaon GP area and forest/tea-garden tracts near Buxa Tiger Reserve | A | Delimitation 2008 |
| Geographic note | Easternmost Dooars foothills bordering Bhutan; Buxa Tiger Reserve covers significant area; economy dominated by tea gardens; Jaigaon is a major India-Bhutan border trade town | A | — |
| Sub-units used in v0 | **U1: Tea_garden_belt** (Birpara–Madarihat tea estates) · **U2: Non_tea_forest_fringe** (Jaigaon border area + forest fringe villages) | E | v0 simplification |

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~220,000 | E | Census 2011 Madarihat-Birpara CD Block; v0 proportional to electorate |
| 2021 projected population | ~242,000 | E | 10-yr compound growth ~0.9%/yr from 2011; tribal belt lower growth than state average |
| Sex ratio (2021, F per 1000 M) | ~1038 | B | NFHS-5 Jalpaiguri district (2019-21): 1038 F/1000 M; used as Alipurduar proxy |
| 2021 estimated electorate (18+) | 212,651 | A | ECI 2021 WB AE official roll (104,559 M + 107,358 F + 10 TG + 724 postal) |
| Estimated M / F / TG split (2021) | 49.2% M / 50.5% F / <0.01% TG | A | ECI 2021 AE roll: 104,559 M / 107,358 F / 10 TG out of 212,651 (excluding 724 service voters) |
| 2021 polling stations | ~210 | E | Proportional to electorate vs 2019 baseline; no official PS count sourced |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 71.50 | E | Alipurduar district 2011: ~74% Hindu; 10-yr projection with slight Adivasi Sarna drift; tribal Sarna-ORP split uncertain |
| Muslim | 9.00 | E | Alipurduar district 2011: ~9% Muslim; Jaigaon border area; stable share |
| Christian | 2.80 | E | Slight increase from 2019 (2.5%) due to continued missionary conversions in tribal belt |
| Sarna_ORP | 15.70 | E | Substantial Adivasi (Oraon, Munda, Santhali) tea-garden workers; marginal increase from 2019 |
| Other_residual | 1.00 | E | Buddhist (Bhutia/Nepali), Sikh, Jain, not-stated; stable |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 8.00 | E | Alipurduar district SC share ~7–9%; stable 2019→2021 |
| └ Rajbanshi_SC | 4.00 | E | Dominant SC sub-group in Dooars |
| └ Other_SC | 4.00 | E | Residual (Bagdi, Hari, Dome) |
| **ST_total** | 35.00 | E | Very high tribal share: Oraon, Munda, Santhali, Kurmi tea-garden Adivasi; also Toto, Koch-Rajbanshi ST; stable |
| └ Oraon_ST | 15.00 | E | Largest ST sub-group in Dooars tea gardens |
| └ Munda_ST | 8.00 | E | Second Adivasi sub-group in tea estates |
| └ Santhali_ST | 6.00 | E | Present in tea belt and forest fringe |
| └ Other_ST | 6.00 | E | Toto (endangered tribe near Totopara), Koch, Rajbanshi-ST, Bhutia |
| UC_bhadralok | 4.00 | E | Small bhadralok fraction; tea-company managerial class, Bengali settlers |
| OBC | 8.00 | E | Rajbanshi (OBC), Kurmi, Teli, Chamar-OBC fraction |
| Other_Hindu_middle | 27.00 | E | Nepali/Gorkha Hindu (Bahun, Chhetri), Marwari trader, Bengali settled middle |
| Muslim | 9.00 | E | See C.1 |
| Christian_plus_Sarna_plus_Other | 9.00 | E | Christian 2.8% + Sarna routed here; Sarna_ORP in C.1 is tribal-religion residual |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2021, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.50 | E | Alipurduar district age pyramid, Census 2011; projected 2 more years; renormalized to 18+ voters only |
| 23_27 | 12.50 | E | New voter cohort slightly larger as 2019 first-timers age in |
| 28_32 | 12.00 | E | |
| 33_37 | 10.50 | E | |
| 38_42 | 10.00 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.50 | E | |
| 63_67 | 6.50 | E | |
| 68 | 6.50 | E | 68+ open-ended; renormalized from Census 2011 adult cohort |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 49.20 | A | ECI 2021 AE roll: 104,559 M / 212,651 total |
| Female | 50.79 | A | ECI 2021 AE roll: 107,358 F / 212,651 total; female-majority electorate reflects NFHS-5 Jalpaiguri sex ratio 1038 |
| Third_gender | 0.01 | A | ECI 2021 AE roll: 10 TG / 212,651 |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 35.00 | E | Bengali settlers + Rajbanshi first-language some consider Bengali; Alipurduar district complex |
| Hindi | 5.00 | E | Marwari traders, Hindi-belt migrant workers, some Bihar-origin tea-garden workers |
| Urdu | 1.00 | E | Muslim traders in Jaigaon border belt |
| Other | 4.00 | E | Residual (Bhutia, Nepali sub-groups, etc.) |
| Rajbongshi | 15.00 | E | Rajbanshi/Rajbongshi — historically dominant Dooars language |
| Sadri | 20.00 | E | Sadri (Nagpuri) — lingua franca of tea-garden Adivasi workers (Oraon, Munda, Kurmi) |
| Nepali | 10.00 | E | Gorkha/Nepali speakers in foothills fringe |
| Santali | 7.00 | E | Santhali speakers in tea belt |
| Mundari | 3.00 | E | Munda-language speakers |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 24.00 | E | NFHS-5 Jalpaiguri women literate 73.6%; tribal belt below district; ~24% illiterate by 2021 vs 26% in 2019 |
| Primary | 24.00 | E | Census 2011 distribution with upward literacy trend |
| Middle | 20.00 | E | |
| Secondary | 16.00 | E | Modest improvement; secondary completion expanding in tribal belt |
| Higher_Secondary | 9.00 | E | |
| Graduate | 5.50 | E | Limited higher education access in remote Dooars |
| Postgraduate | 1.50 | E | Concentrated in managerial/teacher class |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 37.00 | E | COVID-19 lockdown disruption reduced formal main-worker rate slightly from 38% (2019); tea-garden permanent labour dominant |
| └ Main_worker_tea_garden | 21.00 | E | Tea-estate permanent labour (Adivasi-dominated); slight reduction due to COVID-19 closures in 2020 |
| └ Main_worker_non_tea | 16.00 | E | Agricultural, trade, forest, services |
| Marginal_worker | 13.00 | E | Slightly elevated post-COVID-19 as workers shift to marginal status |
| Non_worker | 32.00 | E | Housewife-heavy; tribal women high household economy contribution |
| Student | 10.00 | E | 18–22 cohort in colleges/schools; disruption from COVID-19 closures |
| Unemployed | 8.00 | E | Educated job-aspirants; COVID-19 recession increased educated unemployment |
| **Sum** | **100.00** | — | self-check (sub-rows under Main_worker are is_subgroup=yes) |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 10.00 | E | Limited cultivable land (forest reserve + tea estate); smallholder patches |
| Agricultural_labourer | 43.00 | E | Tea-garden labourers; slight drop from 44% (2019) due to COVID-19 disruptions |
| Household_industry | 4.00 | E | Bamboo, bidi rolling, handloom fringe |
| Manufacturing | 3.00 | E | Tea factory processing workers |
| Construction | 6.00 | E | Slight uptick; post-COVID-19 infrastructure work |
| Trade_retail | 10.00 | E | Jaigaon border market, Madarihat town bazaar; Bhutan trade somewhat disrupted in 2020 |
| Transport_logistics | 4.00 | E | Bhutan trade transit, truck operators, jeep services |
| Services | 8.00 | E | Private services including tourism, forest-sector |
| Government_services_teachers | 6.00 | E | School teachers, forest department, block office |
| Out_migrant_worker | 6.00 | D | COVID-19 reverse migration brought some back; but by 2021 AE outmigration resumed |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Tea-garden managers, large traders |
| Employee | 54.00 | E | Tea-estate regular wage labour; slight decrease as COVID-19 disrupted formal contracts |
| Single_worker | 29.00 | E | Own-account cultivators, small traders; slightly increased post-COVID-19 |
| Family_worker | 15.50 | E | Unpaid family labour in agriculture and household industry |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 34.00 | E | COVID-19 recession compressed some APL into BPL temporarily; tea-garden Adivasi workers historically poor |
| Above_Poverty_Line_low_income | 35.00 | E | Tea-estate permanent workers above BPL but low income |
| Lower_middle | 18.00 | E | Petty traders, some teachers, skilled workers |
| Middle | 9.50 | E | Small business owners, mid-level govt employees; slight increase from Lakshmir Bhandar supplementary income |
| Upper_middle_well_off | 3.50 | E | Tea-company managerial staff, Jaigaon exporters |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Tea_garden_belt | 65.00 | E | Birpara-Madarihat tea estate zone: majority of electorate |
| U2_Non_tea_forest_fringe | 35.00 | E | Jaigaon border area, forest-fringe villages, Buxa BTR buffer zone settlements |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | Slight decrease from 4.6 (2019); WB 2011: 4.3 average; tribal belt larger HH trend declining gradually |
| Nuclear_HH | 61.00 | E | NFHS-5 WB tribal/rural pattern; slight increase |
| Joint_HH | 29.00 | E | Slight decline from 30% (2019); younger generation separating households |
| Extended_multi_generation | 10.00 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.00 | E | Census 2011 Alipurduar pattern; NFHS-5 Jalpaiguri: women married before 18 fell to 18.7% (NFHS-4: 34.5%); later marriage trend |
| Currently_married | 66.00 | E | |
| Widowed | 8.00 | E | Slightly elevated in older tribal female cohort |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 58.00 | C | NFHS-4 ~55% (2019 baseline); TV growth slow in tribal belt; +3pp to 2021 |
| Radio | 7.00 | C | Slight decline; replaced by mobile audio |
| Mobile_phone | 85.00 | C | NFHS-5 Jalpaiguri pattern; Jio + COVID-19 acceleration; +5pp from 2019 |
| Smartphone_with_internet | 52.00 | C | Post-COVID-19 smartphone surge: +22pp from 2019 (30% → 52%); NFHS-5 period 2019-21 captures Jio 4G boom in tribal belt; methodology_2021 §C.14: +20-30pp |
| Computer | 4.00 | C | Minimal change; only managerial/teacher households |
| Two_wheeler | 21.00 | C | Marginal increase from 20% (2019) |
| Four_wheeler | 3.00 | C | Stable; tea-garden managers and Jaigaon traders |
| Banking_access | 82.00 | B | PMJDY further penetration 2019→2021; Lakshmir Bhandar DBT required bank account; +7pp from 75% (2019); methodology_2021 §C.14: +5-10pp |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 78.00 | B | NFHS-5 Jalpaiguri 95.2%; Alipurduar sub-district lower due to forest/tea-garden stream reliance; ~78% estimate |
| Improved_sanitation | 58.00 | B | NFHS-5 Jalpaiguri 73.2%; Swachh Bharat Phase-2 continued gains; tea-garden line housing improved; ~58% for AC-level |
| LPG_clean_cooking_fuel | 35.00 | B | NFHS-5 Jalpaiguri clean fuel 42.7%; Ujjwala 2.0 + Pradhan Mantri Ujjwala Yojana expansion; tea-garden lower; ~35% estimate |
| Wood_biomass_fuel | 58.00 | C | Declining from 68% (2019) as LPG adoption rises |
| Other_fuel | 7.00 | C | Kerosene, dung-cake; stable |
| Electricity | 88.00 | B | NFHS-5 Jalpaiguri 97.4%; Saubhagya 2017-19 + post-completion coverage; some forest-fringe villages still off-grid; ~88% |
| **Note** | (water/sanitation/electricity are independent; cooking-fuel rows LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 55.00 | D | Second/third-generation Adivasi tea-garden workers born in WB; Rajbanshi native; COVID-19 return migrants added some temporarily |
| WB_other_district | 5.00 | D | Bengali settlers from other WB districts |
| Other_Indian_state | 5.00 | D | Marwari traders; some Bihar-origin workers |
| Bangladesh_origin | 2.00 | D | Small; some Hindu refugees in border belt; not a primary refugee AC |
| Outside_India | 1.00 | E | Bhutia/Nepali-origin from Bhutan side |
| Out_migrant | 2.00 | E | COVID-19 brought some back in 2020; by end-2021 outmigration partially resumed |
| Jharkhand_origin | 25.00 | D | Adivasi ancestors brought from Chota Nagpur Plateau as tea-garden indentured labour from 19th century; multi-generational now WB-born |
| Nepal_Bhutan_origin | 5.00 | D | Nepali and Bhutia communities in foothills fringe |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Sadri | Nepali | Santali | Mundari | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 30.00 | 6.00 | 0.50 | 2.50 | 22.00 | 18.00 | 13.00 | 5.00 | 3.00 | E | Blend: Bengali-Hindu settlers + Rajbanshi + Nepali-Hindu; Sadri-speaking Oraon/Munda partly Hindu |
| Muslim | 50.00 | 8.00 | 15.00 | 5.00 | 15.00 | 3.00 | 4.00 | 0.00 | 0.00 | E | Jaigaon Bengali-Muslim dominant; some Urdu-speaking traders |
| Christian | 20.00 | 5.00 | 0.00 | 5.00 | 5.00 | 50.00 | 5.00 | 10.00 | 0.00 | E | Converted Adivasi; Sadri lingua franca for tribal Christians |
| Sarna_ORP | 5.00 | 3.00 | 0.00 | 2.00 | 5.00 | 55.00 | 0.00 | 25.00 | 5.00 | E | Sarna practitioners: overwhelmingly Adivasi; Sadri + Santali + Mundari dominant |
| Other_residual | 10.00 | 15.00 | 0.00 | 30.00 | 5.00 | 5.00 | 30.00 | 3.00 | 2.00 | E | Buddhist/Bhutia: Nepali + Other dominant |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. 2D table.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 10.00 | 20.00 | 5.50 | 10.00 | 54.50 | 0.00 | 0.00 | E | Hindu includes Rajbanshi, Nepali, Bengali settlers; lower ST share of Hindu vs total because Sarna-ORP captured separately |
| Muslim | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 100.00 | 0.00 | A | self-evident |
| Christian | 0.00 | 70.00 | 0.00 | 5.00 | 0.00 | 0.00 | 25.00 | E | Converted Adivasi mostly ST; some OBC |
| Sarna_ORP | 0.00 | 92.00 | 0.00 | 5.00 | 3.00 | 0.00 | 0.00 | E | Sarna adherents are overwhelmingly ST; small OBC-tribal fringe |
| Other_residual | 0.00 | 15.00 | 0.00 | 0.00 | 0.00 | 0.00 | 85.00 | E | Buddhist Bhutia / Nepali-Hindu fringe |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 50.00 | 7.00 | 6.00 | 3.00 | 2.00 | 2.00 | D | Hindu includes Bengali settlers (less native) + Rajbanshi (native) + Nepali (Outside_India origin) |
| Muslim | 65.00 | 5.00 | 5.00 | 20.00 | 5.00 | 0.00 | D | Jaigaon Muslim some Bangladesh-origin border traders |
| Christian | 70.00 | 5.00 | 5.00 | 0.00 | 0.00 | 0.00 | E | Converted tribal — native or Jharkhand-origin |
| Sarna_ORP | 60.00 | 3.00 | 5.00 | 0.00 | 0.00 | 2.00 | E | Adivasi tea-garden — multi-gen WB-born but Jharkhand ancestral |
| Other_residual | 30.00 | 5.00 | 5.00 | 0.00 | 57.00 | 3.00 | E | Buddhist/Bhutia largely Nepal/Bhutan origin |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion. Updated for 2021 smartphone surge.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 65.00 | 62.00 | 87.00 | E | Higher-income Hindu settlers (Nepali, Bengali, Rajbanshi); smartphone +26pp from 2019 baseline |
| Muslim | 63.00 | 60.00 | 85.00 | E | Jaigaon trader class; better connectivity than tea-garden population |
| Christian | 53.00 | 45.00 | 76.00 | E | Converted tribal; lower income base; smartphone adoption accelerated via Lakshmir Bhandar DBT |
| Sarna_ORP | 42.00 | 35.00 | 68.00 | E | Poorest segment; tea-garden Adivasi; lowest asset access; notable smartphone gain from COVID-19 era |
| Other_residual | 58.00 | 48.00 | 72.00 | E | Mixed Buddhist/other |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4.00 | 9.00 | 12.00 | 20.00 | 21.00 | 26.00 | 8.00 | E |
| SC_total | 18.00 | 24.00 | 22.00 | 19.00 | 10.00 | 5.50 | 1.50 | E |
| ST_total | 30.00 | 26.00 | 20.00 | 14.00 | 7.00 | 2.50 | 0.50 | E |
| OBC | 18.00 | 24.00 | 22.00 | 19.00 | 10.00 | 5.50 | 1.50 | E |
| Other_Hindu_middle | 20.00 | 24.00 | 22.00 | 18.00 | 10.00 | 5.00 | 1.00 | E |
| Muslim | 23.00 | 26.00 | 22.00 | 17.00 | 8.00 | 3.50 | 0.50 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share within cohort.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 11.00 | 9.00 | E |
| 23_27 | 11.00 | 8.00 | E |
| 28_32 | 9.50 | 6.50 | E |
| 33_37 | 8.00 | 5.00 | E |
| 38_42 | 7.00 | 4.00 | E |
| 43_47 | 6.00 | 3.00 | E |
| 48_52 | 5.00 | 2.50 | E |
| 53_57 | 4.00 | 2.00 | E |
| 58_62 | 3.50 | 1.50 | E |
| 63_67 | 3.00 | 1.00 | E |
| 68 | 2.50 | 0.80 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8.00 | 28.00 | E |
| 23_27 | 44.00 | 80.00 | E |
| 28_32 | 82.00 | 92.00 | E |
| 33_37 | 92.00 | 90.00 | E |
| 38_42 | 93.00 | 87.00 | E |
| 43_47 | 92.00 | 83.00 | E |
| 48_52 | 91.00 | 77.00 | E |
| 53_57 | 90.00 | 69.00 | E |
| 58_62 | 88.00 | 61.00 | E |
| 63_67 | 82.00 | 47.00 | E |
| 68 | 72.00 | 31.00 | E |

### D.8 Occupation × Asset / media

P(owns asset ‖ occupation) — central media-access metric. Updated for 2021 smartphone surge.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 38.00 | 52.00 | C | Rural smallholder; notable smartphone gain post-Jio 4G |
| Agricultural_labourer | 32.00 | 44.00 | C | Tea-garden pluckers; lowest but increased from 18% (2019) |
| Household_industry | 40.00 | 54.00 | C | |
| Manufacturing | 48.00 | 62.00 | C | Tea-factory workers; better connectivity |
| Construction | 46.00 | 56.00 | C | |
| Trade_retail | 68.00 | 78.00 | C | Jaigaon border market traders; high smartphone penetration |
| Transport_logistics | 64.00 | 72.00 | C | Truck/jeep operators; WhatsApp-dependent |
| Services | 62.00 | 70.00 | C | |
| Government_services_teachers | 82.00 | 90.00 | C | Highest access; online work during COVID-19 |
| Out_migrant_worker | 72.00 | 68.00 | D | Remittance income; smartphone for family contact |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 44.00 | 1.50 | E |
| Primary | 41.00 | 3.00 | E |
| Middle | 37.00 | 5.50 | E |
| Secondary | 31.00 | 9.00 | E |
| Higher_Secondary | 27.00 | 13.00 | E |
| Graduate | 29.00 | 16.00 | E |
| Postgraduate | 37.00 | 11.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for this AC. See NORMALIZED_SCHEMA.md §4.7.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Tea_garden_belt | 64.00 | 7.00 | 3.50 | 22.50 | 3.00 | E | Tea-garden belt: high Adivasi Sarna; slight Christian increase; low Muslim |
| U2_Non_tea_forest_fringe | 85.00 | 13.00 | 1.00 | 0.50 | 0.50 | E | Border/forest fringe: more Rajbanshi/Bengali Hindu + Muslim traders near Jaigaon |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Canonical parent leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Tea_garden_belt | 3.00 | 7.00 | 48.00 | 8.00 | 17.00 | 7.00 | 10.00 | E |
| U2_Non_tea_forest_fringe | 6.00 | 10.00 | 12.00 | 8.00 | 44.00 | 13.00 | 7.00 | E |

### D.13 Sub-unit × Asset / media

Updated for 2021 smartphone surge (+20-25pp across both sub-units).

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Tea_garden_belt | 51.00 | 44.00 | 2.00 | 75.00 | E |
| U2_Non_tea_forest_fringe | 70.00 | 62.00 | 8.00 | 90.00 | E |

### D.14 Sub-unit × Amenities

Updated for 2021 NFHS-5 period (Jalpaiguri proxy).

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Tea_garden_belt | 25.00 | 48.00 | 70.00 | 80.00 | E |
| U2_Non_tea_forest_fringe | 48.00 | 70.00 | 88.00 | 96.00 | E |

### D.15 Vote × Religion (2021 AE anchor)

P(party ‖ religion) — anchored on 2021 AE result; BJP 54.35%, AITC 36.56%, LF 4.24%, Other_NOTA 4.85%.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 68.00 | 24.00 | 1.00 | 3.50 | 3.50 | C | BJP dominant among non-tribal Hindu in Alipurduar ST seat; Rajbanshi-Hindu BJP-leaning; Lakshmir Bhandar softened AITC gap slightly |
| Muslim | 5.00 | 72.00 | 12.00 | 6.00 | 5.00 | C | CSDS 2021 WB Muslim vote pattern; Jaigaon Muslim AITC-leaning; INC declined further |
| Christian | 42.00 | 37.00 | 5.00 | 10.00 | 6.00 | E | Converted tribal split; BJP retained base via tribal welfare and Manoj Tigga identity politics |
| Sarna_ORP | 65.00 | 26.00 | 1.00 | 5.00 | 3.00 | E | BJP mobilised Adivasi Sarna voters; RSP (LF) has traditional tea-garden base; AITC gained marginally |
| Other_residual | 46.00 | 32.00 | 2.00 | 10.00 | 10.00 | E | Nepali/Bhutia: BJP-leaning |

### D.16 Vote × Caste (2021 AE anchor)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 65.00 | 27.00 | 2.00 | 4.00 | 2.00 | C | Bhadralok BJP-leaning; stable from 2019 |
| OBC | 55.00 | 32.00 | 3.00 | 7.00 | 3.00 | C | Rajbanshi OBC BJP-leaning in Dooars |
| SC_total | 52.00 | 36.00 | 3.00 | 6.00 | 3.00 | C | SC BJP-leaning in Dooars belt; AITC gained slightly via welfare |
| ST_total | 62.00 | 29.00 | 1.00 | 5.00 | 3.00 | C | BJP ST dominance in Alipurduar 2021 — key calibration point; RSP (LF) has old tea-garden base |
| Other_Hindu_middle | 60.00 | 29.00 | 2.00 | 6.00 | 3.00 | E | Nepali/Rajbanshi Hindu middle; BJP-leaning |
| Muslim | 5.00 | 72.00 | 12.00 | 6.00 | 5.00 | C | CSDS 2021 WB |

### D.17 Vote × Gender (2021 AE anchor)

Post-Lakshmir Bhandar (launched April 2021): female voters shifted slightly toward AITC.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 60.00 | 30.00 | 2.00 | 5.00 | 3.00 | C | Adjusted from CSDS 2021 WB regional for ST-belt BJP advantage |
| Female | 49.00 | 43.00 | 1.50 | 3.50 | 3.00 | C | Lakshmir Bhandar (Apr 2021 launch) narrowed BJP-AITC gap among women vs 2019; AITC boosted among female voters |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for this AC. See NORMALIZED_SCHEMA.md §4.7.)

---

## E. 2021 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 54.35 | A | ECI 2021 AE: Manoj Tigga 90,718 votes / 166,920 total valid |
| AITC | 36.56 | A | ECI 2021 AE: Rajesh Lakra 61,033 votes |
| INC | 0.00 | A | No INC candidate contested in Madarihat 2021 AE |
| LF | 4.24 | A | ECI 2021 AE: RSP (Mili Oraon) 7,077 votes (4.24% of 166,920) — only LF candidate |
| Other_NOTA | 4.85 | A | Remaining candidates + NOTA: 8,092 votes; includes SUCI, IND, smaller parties |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 014 Madarihat (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Mangal Singh Subba | GNLF | ~35 | (CPI-M candidate) | CPI(M) | ~28 | ~7,000 est. |
| 2016 AE | Manoj Tigga | BJP | ~44 | (AITC candidate) | AITC | ~30 | ~17,000 est. |

Note: Madarihat was a Gorkha National Liberation Front (GNLF) stronghold in the 1980s–2000s. BJP began challenging seriously by 2014 under the tribal mobilisation agenda; Manoj Tigga (BJP) won AC 014 in 2016 AE. The 2019 LS result (BJP 60.2%) reflected peak BJP consolidation in the Dooars Adivasi belt. The 2021 AE result (BJP 54.35%) shows BJP retained the seat but AITC closed the gap from the 2019 LS peak, partly due to COVID-19 economic stress and Lakshmir Bhandar launch in April 2021.

### LS 01 Alipurduar (ST reserved) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2009 LS | Paban Singh Ghatowar | INC | ~40 | Congress historically strong in Dooars ST seat; RSP/LF also competitive |
| 2014 LS | Dasrath Tirkey | BJP | ~36 | First BJP win; Congress declined |
| 2019 LS | John Barla | BJP | — | BJP won Alipurduar LS; AC-014 segment: BJP 60.19%, AITC 31.97%, INC 2.19%, LF (RSP) 3.60% |

RSP (Revolutionary Socialist Party) historically organised tea-garden labour in Dooars; the 2021 AE result (RSP 4.24%) shows a modest LF recovery vs the 2019 LS trough (3.60%), reflecting tea-garden worker solidarity reviving somewhat post-COVID-19.

Note: John Barla (BJP Alipurduar MP) joined the Union cabinet in July 2021 as a Minister of State, a visible reward to the Dooars tribal constituency. This was a known fact by end-2021 and may have reinforced BJP tribal-identity narrative.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Election Commission of India — 2021 WB AE results: Madarihat AC 014: Manoj Tigga (BJP) 90,718; Rajesh Lakra (AITC) 61,033; Mili Oraon (RSP) 7,077; total valid 166,920; electorate 212,651 (104,559 M + 107,358 F + 10 TG); turnout 78.14%
- Election Commission of India — 2019 LS AC-segment vote tallies (`2019_AssemblySegmentLevelVotingData.csv`; AC 14: BJP 93,488; AITC 49,650; RSP 5,586; INC 3,396; total valid 155,313; electorate 203,374)
- Delimitation Commission of India 2008 — WB Schedule (AC 014 Madarihat = ST reserved; Alipurduar LS PC 01)
- Census of India 2011 — Alipurduar district (formed from Jalpaiguri)

### Secondary sources (tier B / C)

- NFHS-5 (2019-21) Jalpaiguri district — household amenities, asset ownership; used as Alipurduar proxy (Alipurduar not separately reported)
- NFHS-4 (2015-16) West Bengal — baseline asset/media ownership
- CSDS-Lokniti 2021 WB regional post-poll — vote × religion / caste / gender cross-tabs (WB regional)
- WB District Statistical Handbook — Alipurduar / Jalpaiguri
- Census 2011 Primary Census Abstract — Madarihat-Birpara CD Block

### Tertiary / journalistic (tier D)

- Wikipedia: "Madarihat (Vidhan Sabha constituency)" — reservation status ST, 2021 AE result (Manoj Tigga BJP 90,718; Rajesh Lakra AITC 61,033; margin 29,685)
- Wikipedia: "Alipurduar district" — demographics, tribal composition, Buxa Tiger Reserve
- Wikipedia: "Manoj Tigga" — BJP MLA Madarihat, cabinet minister July 2021
- Wikipedia: "Alipurduar (Lok Sabha constituency)" — historical results
- IndiaTV News: Madarihat constituency profile — 2021 electorate 212,651; vote shares AITC 36.56%, BJP 54.35%, RSP 4.24%

### Tier-D / E reliance flags (what to distrust)

- **Religion shares** (C.1): no direct AC-level Census religion table; derived from Alipurduar district aggregate — tier E
- **Caste sub-group shares** (C.2, D.2): no caste census post-1931 for non-SC/ST; tribal sub-group split is modeled — tier E
- **Mother tongue** (C.5, D.1): Alipurduar is linguistically very complex; all shares tier E
- **Migration / birthplace** (C.16, D.3): Jharkhand-origin Adivasi history well-documented but current-share tier D
- **Sub-unit decomposition** (D.11–D.14): collapsed to 2 units; no GP-level Census data — tier E
- **Vote × Demographic** (D.15–D.17): CSDS 2021 WB regional rollup adjusted for ST-belt BJP dominance; tier C/E
- **Asset/media 2021 projections** (C.14, D.4, D.8, D.13): smartphone surge anchored on NFHS-5 period 2019-21; methodology §C.14 rule +20-30pp applied; tier C

### v0 known gaps

1. No GP-level Census data — sub-units collapsed to 2 (tea-garden belt vs fringe)
2. Religion shares from district-level; no AC-level source
3. Caste sub-group shares fully modeled; tribal composition estimate
4. Mother tongue split tier E across the board
5. NFHS-5 uses Jalpaiguri district as Alipurduar proxy; Alipurduar not separately published
6. Candidate-level 2021 AE vote breakdown for all smaller parties (NOTA figure) estimated from total valid minus top 3 parties

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No post-2021 events referenced.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs. The
> validator's leakage gate exempts §H from the no-future-leakage check.

### 2024 Lok Sabha Election — AC 014 segment within Alipurduar LS (PC 01) (tier A)

> Figures below are **tier A** — sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=14, Madarihat. Total valid votes (candidates only): 159,378; electorate 220,466.

| Party | Candidate (LS level) | Votes | AC-014 segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Manoj Tigga | 79,921 | 50.15% | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Prakash Chik Baraik | 68,858 | 43.20% | A | Same |
| INC | (no INC candidate) | 0 | 0.00% | A | Same |
| LF (RSP) | Mili Oraon | 4,043 | 2.54% | A | Same |
| Other_NOTA | BSP 926 + SUCI 308 + KPPU 297 + GNASURKP 255 + NBNGPLPP 433 + KMSP 828 + IND 1,565 + IND 1,944 + (NOTA not in CSV) | 6,556 | 4.11% | A | Same |
| **Total** | | **159,378** | **100.00%** | A | — |

Note: BJP retained Alipurduar LS (Manoj Tigga re-elected as MP). AITC closed the gap: BJP margin shrank from 29,685 (2021 AE) to 11,063 votes in the 2024 LS segment at AC-014 level. This is the out-of-sample validation target.

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC-014 segment shares within ±3pp of the tier-A figures:
- BJP target: 50.15% ± 3pp
- AITC target: 43.20% ± 3pp
- LF + others target: 6.65% ± 3pp
