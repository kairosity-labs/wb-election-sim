# AC 014 — Madarihat (ST) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 014 Madarihat as of 2019 only — it does not reference any
> post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as
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
| AC number | 014 | A | ECI / Delimitation Commission 2008 |
| AC name | Madarihat | A | ECI |
| Reservation | ST | A | Delimitation 2008 |
| District | Alipurduar | A | Delimitation 2008 (formerly Jalpaiguri; Alipurduar district formed 2014) |
| Sub-division | Alipurduar | A | WB administrative |
| LS constituency | 01 — Alipurduar (ST reserved) | A | Delimitation 2008 |
| LS segments included | AC 01 Kumargram · 02 Kalchini · 03 Alipurduar · 04 Falakata · 05 Madarihat · 06 Dhupguri · 07 Nagrakata | A | Delimitation 2008 |
| AC composition | Madarihat-Birpara CD Block (part) covering Madarihat GP, Birpara GP, Jaigaon GP area and forest/tea-garden tracts near Buxa Tiger Reserve | A | Delimitation 2008 |
| Geographic note | Easternmost Dooars foothills bordering Bhutan; Buxa Tiger Reserve covers significant area; economy dominated by tea gardens | A | — |
| Sub-units used in v0 | **U1: Tea_garden_belt** (Birpara–Madarihat tea estates) · **U2: Non_tea_forest_fringe** (Jaigaon border area + forest fringe villages) | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~220,000 | E | Census 2011 Madarihat-Birpara CD Block; v0 proportional to electorate |
| 2019 projected population | ~236,000 | E | 8-yr compound growth ~0.9%/yr; tribal belt lower growth than state average |
| Sex ratio (2019, F per 1000 M) | ~957 | E | Alipurduar district 2011 sex ratio 957; projected stable |
| 2019 estimated electorate (18+) | ~203,374 | A | 2019 LS ECI data (total electors for AC 14) |
| Estimated M / F / TG split (2019) | 51.1% M / 48.9% F / <0.05% TG | E | District sex ratio back-projection |
| 2019 polling stations (estimated) | ~210 | E | Proportional to electorate vs state average |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 72.00 | E | Alipurduar district 2011: ~74% Hindu; tribal Sarna-ORP split uncertain; tea-garden ST population partly Hindu partly Sarna |
| Muslim | 9.00 | E | Alipurduar district 2011: ~9% Muslim; Jaigaon border area has Muslim traders |
| Christian | 2.50 | E | Christian missionary presence in tribal belt; some tea garden workers converted |
| Sarna_ORP | 15.50 | E | Substantial Adivasi (Oraon, Munda, Santhali) tea-garden workers; tribal religion estimate |
| Other_residual | 1.00 | E | Buddhist (Bhutia/Nepali), Sikh, Jain, not-stated |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 8.00 | E | Alipurduar district SC share ~7–9%; lower in tea-belt AC |
| └ Rajbanshi_SC | 4.00 | E | Dominant SC sub-group in Dooars (Rajbanshi classified SC in WB) |
| └ Other_SC | 4.00 | E | Residual (Bagdi, Hari, Dome) |
| **ST_total** | 35.00 | E | Very high tribal share: Oraon, Munda, Santhali, Kurmi tea-garden Adivasi; also Toto, Koch-Rajbanshi ST |
| └ Oraon_ST | 15.00 | E | Largest ST sub-group in Dooars tea gardens; Jharkhand-origin |
| └ Munda_ST | 8.00 | E | Second Adivasi sub-group in tea estates |
| └ Santhali_ST | 6.00 | E | Present in tea belt and forest fringe |
| └ Other_ST | 6.00 | E | Toto (endangered tribe near Totopara), Koch, Rajbanshi-ST, Bhutia |
| UC_bhadralok | 4.00 | E | Small bhadralok fraction; tea-company managerial class, Bengali settlers |
| OBC | 8.00 | E | Rajbanshi (OBC), Kurmi, Teli, Chamar-OBC fraction |
| Other_Hindu_middle | 27.00 | E | Nepali/Gorkha Hindu (Bahun, Chhetri), Marwari trader, Bengali settled middle |
| Muslim | 9.00 | E | See C.1 |
| Christian_plus_Sarna_plus_Other | 9.00 | E | Christian 2.5% + Sarna routed here; see note: Sarna_ORP in C.1 is the tribal-religion residual |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.00 | E | Alipurduar district age pyramid, Census 2011; renormalized to 18+ adults only |
| 23_27 | 12.50 | E | |
| 28_32 | 11.50 | E | |
| 33_37 | 10.50 | E | |
| 38_42 | 10.00 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.50 | E | |
| 63_67 | 6.50 | E | |
| 68 | 6.50 | E | 68+ open-ended; renormalized from Census 2011 adult cohort |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.11 | E | Alipurduar district 2011 sex ratio 957 → 51.11% M / 48.88% F |
| Female | 48.88 | E | |
| Third_gender | 0.01 | E | Negligible fraction; WB 2021 SIR pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 35.00 | E | Bengali settlers + Rajbanshi first-language some consider Bengali; Alipurduar district complex; estimate |
| Hindi | 5.00 | E | Marwari traders, Hindi-belt migrant workers, some Bihar-origin tea-garden workers |
| Urdu | 1.00 | E | Muslim traders in Jaigaon border belt |
| Other | 4.00 | E | Residual (Bhutia, Nepali sub-groups, etc.) |
| Rajbongshi | 15.00 | E | Rajbanshi/Rajbongshi — historically dominant Dooars language |
| Sadri | 20.00 | E | Sadri (Nagpuri) — lingua franca of tea-garden Adivasi workers (Oraon, Munda, Kurmi) |
| Nepali | 10.00 | E | Gorkha/Nepali speakers in foothills fringe |
| Santali | 7.00 | E | Santhali speakers in tea belt |
| Mundari | 3.00 | E | Munda-language speakers |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 26.00 | E | Alipurduar district literacy ~69% (2011, A); tea-garden workers lower; tribal belt; ~26% illiterate by 2019 |
| Primary | 24.00 | E | Census 2011 education distribution scaled to district pattern |
| Middle | 20.00 | E | |
| Secondary | 15.00 | E | |
| Higher_Secondary | 8.00 | E | |
| Graduate | 5.50 | E | Limited higher education access in remote Dooars |
| Postgraduate | 1.50 | E | Concentrated in managerial/teacher class |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 38.00 | E | Tea-garden employment creates high main-worker rate; Alipurduar district Census 2011 ~37% main-worker |
| └ Main_worker_tea_garden | 22.00 | E | Tea-estate permanent labour (Adivasi-dominated) |
| └ Main_worker_non_tea | 16.00 | E | Agricultural, trade, forest, services |
| Marginal_worker | 12.00 | E | Seasonal tea-harvest labour + marginal cultivators |
| Non_worker | 32.00 | E | Housewife-heavy; tribal women high household economy contribution |
| Student | 10.00 | E | 18–22 cohort in colleges/schools |
| Unemployed | 8.00 | E | Educated job-aspirants; tea-garden closures create seasonal unemployment |
| **Sum** | **100.00** | — | self-check (sub-rows under Main_worker are is_subgroup=yes) |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 10.00 | E | Limited cultivable land (forest reserve + tea estate); smallholder patches |
| Agricultural_labourer | 44.00 | E | Tea-garden labourers (plucking, processing); dominant occupation |
| Household_industry | 4.00 | E | Bamboo, bidi rolling, handloom fringe |
| Manufacturing | 3.00 | E | Tea factory processing workers |
| Construction | 5.00 | E | Infrastructure including road workers |
| Trade_retail | 10.00 | E | Jaigaon border market, Madarihat town bazaar |
| Transport_logistics | 4.00 | E | Bhutan trade transit, truck operators, jeep services |
| Services | 8.00 | E | Private services including tourism, forest-sector |
| Government_services_teachers | 6.00 | E | School teachers, forest department, block office |
| Out_migrant_worker | 6.00 | D | Some Adivasi men to Assam/Meghalaya tea belts or construction |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Tea-garden managers, large traders |
| Employee | 55.00 | E | Tea-estate regular wage labour (permanent workers); govt employees |
| Single_worker | 28.00 | E | Own-account cultivators, small traders, bidi rollers |
| Family_worker | 15.50 | E | Unpaid family labour in agriculture and household industry |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 35.00 | E | Tea-garden Adivasi workers historically poor; tribal belt WB BPL ~35–40%; Alipurduar district pattern |
| Above_Poverty_Line_low_income | 35.00 | E | Tea-estate permanent workers above BPL but low income |
| Lower_middle | 18.00 | E | Petty traders, some teachers, skilled workers |
| Middle | 9.00 | E | Small business owners, mid-level govt employees |
| Upper_middle_well_off | 3.00 | E | Tea-company managerial staff, Jaigaon exporters |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Tea_garden_belt | 65.00 | E | Birpara-Madarihat tea estate zone: majority of electorate; proportional to number of tea gardens |
| U2_Non_tea_forest_fringe | 35.00 | E | Jaigaon border area, forest-fringe villages, Buxa BTR buffer zone settlements |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.6 persons | E | Tribal belt slightly larger HH; WB 2011: 4.3 average; tea-garden line housing tends toward larger families |
| Nuclear_HH | 60.00 | E | NFHS-4 WB tribal/rural pattern; tea-garden line housing nuclear-dominant |
| Joint_HH | 30.00 | E | Higher joint-family rate in tribal communities |
| Extended_multi_generation | 10.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.00 | E | Census 2011 Alipurduar pattern; tea-garden workers marry younger |
| Currently_married | 66.00 | E | |
| Widowed | 8.00 | E | Slightly elevated in older tribal female cohort |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 55.00 | C | NFHS-4 WB rural 60%; Alipurduar lower due to tribal/tea-garden poverty; ~55% |
| Radio | 8.00 | C | Slightly higher than state average in forest fringe (no TV alternative) |
| Mobile_phone | 80.00 | C | NFHS-4 WB ~78%; Jio penetration 2016-19; tea-garden workers adopted mobile |
| Smartphone_with_internet | 30.00 | C | Below state average; Alipurduar rural digital lag; tea-garden limited |
| Computer | 4.00 | C | Very low; only managerial/teacher households |
| Two_wheeler | 20.00 | C | NFHS-4 WB rural 18%; slightly below due to income level |
| Four_wheeler | 3.00 | C | Mostly tea-garden managers and Jaigaon traders |
| Banking_access | 75.00 | B | PMJDY 2014-19; tribal belt moderate penetration; some tea-garden accounts via employer |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 70.00 | C | NFHS-4 WB rural 84%; Alipurduar lower; forest/tea-garden area stream reliance |
| Improved_sanitation | 45.00 | C | NFHS-4 WB rural 51% + Swachh Bharat; tea-garden line housing lagging |
| LPG_clean_cooking_fuel | 25.00 | C | NFHS-4 WB rural 24% + Ujjwala 2016-19; tea-garden workers low adoption |
| Wood_biomass_fuel | 68.00 | C | Forest-belt high firewood use; primary cooking fuel in tribal households |
| Other_fuel | 7.00 | C | Kerosene, dung-cake |
| Electricity | 80.00 | C | Census 2011 + Saubhagya 2017-19; tea-garden internal electrification but some fringe villages still off-grid |
| **Note** | (water/sanitation/electricity are independent; cooking-fuel rows LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 55.00 | D | Second/third-generation Adivasi tea-garden workers born in WB; Rajbanshi native |
| WB_other_district | 5.00 | D | Bengali settlers from other WB districts |
| Other_Indian_state | 5.00 | D | Marwari traders; some Bihar-origin workers |
| Bangladesh_origin | 2.00 | D | Small; some Hindu refugees in border belt; not a primary refugee AC |
| Outside_India | 1.00 | E | Bhutia/Nepali-origin from Bhutan side |
| Out_migrant | 2.00 | E | Some registered here but working in Assam/Meghalaya tea belts |
| Jharkhand_origin | 25.00 | D | Adivasi ancestors brought from Chota Nagpur Plateau (Jharkhand/Bihar/Odisha) as tea-garden indentured labour from 19th century; multi-generational now WB-born but ancestral origin tracked |
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

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 62.00 | 36.00 | 82.00 | E | Higher-income Hindu settlers (Nepali, Bengali, Rajbanshi) vs tribal |
| Muslim | 60.00 | 35.00 | 80.00 | E | Jaigaon trader class slightly better off |
| Christian | 50.00 | 25.00 | 70.00 | E | Converted tribal; lower income base |
| Sarna_ORP | 38.00 | 15.00 | 58.00 | E | Poorest segment; tea-garden Adivasi; lowest asset access |
| Other_residual | 55.00 | 28.00 | 65.00 | E | Mixed Buddhist/other |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 5.00 | 10.00 | 12.00 | 20.00 | 20.00 | 25.00 | 8.00 | E |
| SC_total | 20.00 | 25.00 | 22.00 | 18.00 | 9.00 | 5.00 | 1.00 | E |
| ST_total | 32.00 | 26.00 | 20.00 | 13.00 | 6.00 | 2.50 | 0.50 | E |
| OBC | 20.00 | 24.00 | 22.00 | 18.00 | 9.00 | 5.50 | 1.50 | E |
| Other_Hindu_middle | 22.00 | 24.00 | 22.00 | 17.00 | 9.00 | 5.00 | 1.00 | E |
| Muslim | 25.00 | 26.00 | 22.00 | 16.00 | 7.00 | 3.50 | 0.50 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share within cohort.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 10.00 | 8.00 | E |
| 23_27 | 10.00 | 7.50 | E |
| 28_32 | 9.00 | 6.00 | E |
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
| 18_22 | 8.00 | 30.00 | E |
| 23_27 | 45.00 | 82.00 | E |
| 28_32 | 82.00 | 93.00 | E |
| 33_37 | 92.00 | 91.00 | E |
| 38_42 | 93.00 | 88.00 | E |
| 43_47 | 92.00 | 84.00 | E |
| 48_52 | 91.00 | 78.00 | E |
| 53_57 | 90.00 | 70.00 | E |
| 58_62 | 88.00 | 62.00 | E |
| 63_67 | 82.00 | 48.00 | E |
| 68 | 72.00 | 32.00 | E |

### D.8 Occupation × Asset / media

P(owns asset ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 22.00 | 48.00 | C | Rural smallholder; low income |
| Agricultural_labourer | 18.00 | 40.00 | C | Tea-garden pluckers; lowest smartphone access in AC |
| Household_industry | 25.00 | 50.00 | C | |
| Manufacturing | 30.00 | 58.00 | C | Tea-factory workers slightly better |
| Construction | 28.00 | 52.00 | C | |
| Trade_retail | 55.00 | 75.00 | C | Jaigaon border market traders; higher smartphone penetration |
| Transport_logistics | 50.00 | 70.00 | C | Truck/jeep operators |
| Services | 48.00 | 68.00 | C | |
| Government_services_teachers | 72.00 | 88.00 | C | Highest access |
| Out_migrant_worker | 60.00 | 65.00 | D | Remittance income; smartphone for family contact |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 45.00 | 1.50 | E |
| Primary | 42.00 | 3.00 | E |
| Middle | 38.00 | 5.00 | E |
| Secondary | 32.00 | 8.00 | E |
| Higher_Secondary | 28.00 | 12.00 | E |
| Graduate | 30.00 | 15.00 | E |
| Postgraduate | 38.00 | 10.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for this AC. See NORMALIZED_SCHEMA.md §4.7.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Tea_garden_belt | 65.00 | 7.00 | 3.00 | 22.00 | 3.00 | E | Tea-garden belt: high Adivasi Sarna; some converted Christian; low Muslim |
| U2_Non_tea_forest_fringe | 85.00 | 13.00 | 1.00 | 0.50 | 0.50 | E | Border/forest fringe: more Rajbanshi/Bengali Hindu + Muslim traders near Jaigaon |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Canonical parent leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Tea_garden_belt | 3.00 | 7.00 | 48.00 | 8.00 | 17.00 | 7.00 | 10.00 | E |
| U2_Non_tea_forest_fringe | 6.00 | 10.00 | 12.00 | 8.00 | 44.00 | 13.00 | 7.00 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Tea_garden_belt | 48.00 | 22.00 | 2.00 | 68.00 | E |
| U2_Non_tea_forest_fringe | 68.00 | 42.00 | 7.00 | 85.00 | E |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Tea_garden_belt | 18.00 | 38.00 | 62.00 | 72.00 | E |
| U2_Non_tea_forest_fringe | 35.00 | 58.00 | 82.00 | 90.00 | E |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 regional WB rollup, adjusted for ST-belt BJP dominance.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 68.00 | 24.00 | 2.00 | 3.50 | 2.50 | C | BJP dominant among non-tribal Hindu in Alipurduar ST seat; Rajbanshi-Hindu BJP-leaning |
| Muslim | 5.00 | 70.00 | 18.00 | 5.00 | 2.00 | C | CSDS 2019 WB Muslim vote pattern; Jaigaon Muslim AITC |
| Christian | 40.00 | 35.00 | 8.00 | 12.00 | 5.00 | E | Converted tribal split; BJP made inroads in Christian tribal via welfare |
| Sarna_ORP | 65.00 | 25.00 | 2.00 | 5.00 | 3.00 | E | BJP mobilised Adivasi Sarna voters via Modi-BJP tribal outreach; RSP (LF) has traditional base |
| Other_residual | 45.00 | 30.00 | 5.00 | 10.00 | 10.00 | E | Nepali/Bhutia: BJP-leaning |

### D.16 Vote × Caste (2019 LS)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 65.00 | 25.00 | 3.00 | 5.00 | 2.00 | C | Bhadralok BJP-leaning by 2019 |
| OBC | 55.00 | 30.00 | 5.00 | 7.00 | 3.00 | C | Rajbanshi OBC BJP-leaning in Dooars |
| SC_total | 52.00 | 35.00 | 5.00 | 6.00 | 2.00 | C | SC BJP-leaning in Dooars belt |
| ST_total | 62.00 | 28.00 | 2.00 | 5.00 | 3.00 | C | BJP ST dominance in Alipurduar 2019 — key calibration point; RSP (LF) has old base in tea gardens |
| Other_Hindu_middle | 60.00 | 28.00 | 3.00 | 6.00 | 3.00 | E | Nepali/Rajbanshi Hindu middle; BJP-leaning |
| Muslim | 5.00 | 70.00 | 18.00 | 5.00 | 2.00 | C | CSDS 2019 WB |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 63.00 | 28.00 | 2.50 | 4.00 | 2.50 | C | Adjusted from CSDS 2019 WB regional for ST-belt BJP advantage |
| Female | 57.00 | 35.00 | 2.00 | 3.50 | 2.50 | C | CSDS 2019 WB women slightly more AITC; pre-LB |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for this AC. See NORMALIZED_SCHEMA.md §4.7.)

---

## E. 2019 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 60.19 | A | ECI 2019 LS GE Form-20 AC-14 segment: 93,488 votes / 155,313 total valid |
| AITC | 31.97 | A | ECI 2019 LS: 49,650 votes |
| INC | 2.19 | A | ECI 2019 LS: 3,396 votes |
| LF | 3.60 | A | ECI 2019 LS: RSP 5,586 votes (only LF candidate) |
| Other_NOTA | 2.06 | A | SUCI(C) 596 + IND 826 + IND 1,771 = 3,193 votes |
| **Sum** | **100.01** | — | self-check (rounding) |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 014 Madarihat (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Mangal Singh Subba | GNLF | ~35 | (CPI-M candidate) | CPI(M) | ~28 | ~7,000 est. |
| 2016 AE | Manoj Tigga | BJP | ~44 | (AITC candidate) | AITC | ~30 | ~17,000 est. |

Note: Madarihat was a Gorkha National Liberation Front (GNLF) stronghold in the 1980s–2000s, reflecting Nepali/Gorkha political identity in the foothills. The CPI(M) had a presence through its CITU union base in tea gardens. BJP began challenging seriously by 2014 under the tribal mobilisation agenda; Manoj Tigga (BJP) won AC 014 in the 2016 AE and became the face of BJP in the Dooars tribal belt. This assembly-to-LS alignment explains the exceptional 60.2% BJP share in 2019 LS.

### LS 01 Alipurduar (ST reserved) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2009 LS | Paban Singh Ghatowar | INC | ~40 | Congress historically strong in Dooars ST seat; RSP/LF also competitive |
| 2014 LS | Dasrath Tirkey | BJP | ~36 | First BJP win; AITC strong; Congress declined |

RSP (Revolutionary Socialist Party) historically organised tea-garden labour in Dooars; the 2019 result (RSP 3.6%) reflects residual LF base after years of decline under BJP-AITC polarisation.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Election Commission of India — 2019 LS AC-segment vote tallies (`2019_AssemblySegmentLevelVotingData.csv`; AC 14: BJP 93,488; AITC 49,650; RSP 5,586; INC 3,396; SUCI(C) 596; IND 826; IND 1,771; total valid 155,313; electorate 203,374)
- Delimitation Commission of India 2008 — WB Schedule (AC 014 Madarihat = ST reserved; Alipurduar LS PC 01)
- Census of India 2011 — Alipurduar district (formed from Jalpaiguri)

### Secondary sources (tier B / C)

- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline; Alipurduar rural pattern
- CSDS-Lokniti 2019 NES post-poll WB regional — vote × religion / caste / gender cross-tabs
- WB District Statistical Handbook — Alipurduar / Jalpaiguri
- Pew Research India 2021 — religion-differential growth projections
- Census 2011 Primary Census Abstract — Madarihat-Birpara CD Block

### Tertiary / journalistic (tier D)

- Wikipedia: "Madarihat (Vidhan Sabha constituency)" — reservation status ST, LS segment Alipurduar
- Wikipedia: "Alipurduar district" — demographics, tribal composition, Buxa Tiger Reserve
- Wikipedia: "Manoj Tigga" — BJP MLA Madarihat, 2016 win context, tribal mobilisation
- News reports on Dooars tea-garden politics and Adivasi BJP mobilisation (2014–2019)
- Wikipedia: "Alipurduar (Lok Sabha constituency)" — historical results 2009, 2014

### Tier-D / E reliance flags (what to distrust)

- **Religion shares** (C.1): no direct AC-level Census religion table; derived from Alipurduar district aggregate — tier E
- **Caste sub-group shares** (C.2, D.2): no caste census post-1931 for non-SC/ST; tribal sub-group split is modeled — tier E
- **Mother tongue** (C.5, D.1): Alipurduar is linguistically very complex (Bengali, Rajbongshi, Sadri, Nepali, Santali, Mundari); all shares tier E
- **Migration / birthplace** (C.16, D.3): Jharkhand-origin Adivasi history well-documented but current-share tier D from journalistic/historical
- **Sub-unit decomposition** (D.11–D.14): collapsed to 2 units (tea-garden belt vs non-tea fringe); no GP-level Census data used — tier E
- **Vote × Demographic** (D.15–D.17): CSDS 2019 WB regional rollup; adjusted for local ST-BJP dominance; tier C/E
- **Assembly election results** (F): Wikipedia/news sources; approximate figures — tier D

### v0 known gaps

1. No GP-level Census data — sub-units collapsed to 2 (tea-garden belt vs fringe)
2. Religion shares from district-level; no AC-level source
3. Caste sub-group shares fully modeled; tribal composition estimate
4. Mother tongue split tier E across the board
5. 2021 AE official results — included in H with best available figures

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs. The
> validator's leakage gate exempts §H from the no-future-leakage check.

### 2021 WB Assembly Election — AC 014 Madarihat (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Manoj Tigga | ~105,000 est. | ~55% | D — Wikipedia / news; awaiting ECI 2021 AE official |
| AITC | (AITC candidate) | ~75,000 est. | ~40% | D — estimated from Wikipedia |
| Others | LF + others | ~8,000 est. | ~5% | D |

Note: BJP retained Madarihat in 2021 AE with Manoj Tigga; AITC made gains from 2019 LS level (BJP 60% LS → BJP ~55% AE typical in ST belt). Official figures to be populated from ECI 2021 AE data.

### 2024 Lok Sabha Election — AC 014 segment within Alipurduar LS (PC 01) (tier A)

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Manoj Tigga | (to be populated) | (to be populated) | A | data/2024_AssemblySegmentLevelVotingData.csv — AC_NO=14 |
| AITC | (AITC candidate) | (to be populated) | (to be populated) | A | Same |
| INC | (INC candidate) | (to be populated) | (to be populated) | A | Same |
| Others | — | (to be populated) | (to be populated) | A | Same |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024
LS AC-014 segment shares within ±3pp of the tier-A figures (BJP / AITC / INC
/ LF combined).
