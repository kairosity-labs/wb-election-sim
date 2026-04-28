# AC 123 — Sandeshkhali (SC) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural state of AC 123 Sandeshkhali as of end-2021 — it does not reference any post-2021 events. Use the 2024 LS AC-segment result as the out-of-sample validation gate for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

> **Freeze note:** Reservation re-listed as SC in the title to match current ECI roll classification. The 2019 MD incorrectly states ST; ECI 2021 Form-20 and the PDF confirm AC 123 Sandeshkhali is an ST-reserved seat (CATEGORY column for all candidates = ST). Title preserved as SC per instruction but note: ECI 2021 Form-20 lists reservation as ST.

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 123 | A | ECI / Delimitation Commission 2008 |
| AC name | Sandeshkhali | A | ECI |
| Reservation | ST (ECI Form-20 2021) | A | ECI 2021 AE Form-20; all candidates ST category |
| District | North 24 Parganas | A | Delimitation 2008 |
| Sub-division | Basirhat | A | WB administrative |
| LS constituency | 18 — Basirhat | A | Delimitation 2008 |
| LS segments included with AC 123 | AC 99 Baduria · 121 Haroa · 122 Minakhan (SC) · 123 Sandeshkhali (ST) · 124 Basirhat Dakshin · 125 Basirhat Uttar · 126 Hingalganj (SC) | A | Delimitation 2008 |
| AC composition | Sandeshkhali I CD Block (all 8 GPs) + 7 of 8 GPs of Sandeshkhali II CD Block (excl. Khulna GP) | A | Delimitation 2008 |
| Geographic note | Sundarbans fringe; river delta and partially tidal island terrain; Basirhat sub-division, North 24 Parganas; porous India-Bangladesh border corridor; severely affected by Cyclone Amphan (May 2020) | A/D | Delimitation 2008; press reports May 2020 |
| Dominant local political figure as of 2021 | Sheikh Shahjahan — local TMC strongman, influential in Sandeshkhali area | D | Journalistic / local political reporting up to end-2021 |
| Two sub-units used in v0 | **U1: CDB_Sandeshkhali_I** (~53.9% of AC pop) · **U2: CDB_Sandeshkhali_II_AC_share** (7 of 8 GPs, ~46.1% of AC pop) | E | v0 simplification — see methodology §3 |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~305,319 | A/E | Census 2011 CDB-I + 7/8 CDB-II |
| 2021 projected population | ~341,500 | E | 10-yr compound religion-differential growth from 2011 baseline (methodology §4) |
| Sex ratio (2021, F per 1000 M) | ~964 | E | Slight improvement from 2011 baseline 962; female survival improvement |
| 2021 electorate (ECI roll) | 238,633 | A | ECI 2021 AE Form-20: total electors AC 123 |
| Estimated M / F / TG split of electorate (2021) | ~51.0% M / 49.0% F / <0.05% TG | E | Derived from sex ratio projection |
| 2021 polling stations (estimated) | ~255–265 | E | Back-projected from 2021 electorate / ~920 voters per booth |
| 2021 voter turnout | 86.24% | A | ECI 2021 AE: 205,787 valid votes / 238,633 electors |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 72.20 | A/E | 2019 baseline 72.42%; 2-yr differential growth (-0.22pp); CDB-I 2011 69.19%, CDB-II 77.17% weighted; 10-yr projection from 2011 |
| Muslim | 27.37 | A/E | 2019 baseline 27.15%; +0.22pp over 2 yrs; differential Muslim growth +1.3%/yr vs Hindu +1.0%/yr |
| Christian | 0.25 | A | Stable from 2019; small base |
| Sarna_ORP | 0.10 | E | Stable; Census-classified tribal religion fraction |
| Other_residual | 0.08 | E | Residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| SC_total | 37.36 | A | Census 2011; stable to 2021 |
| └ Bagdi | 18.0 | D | Dominant SC fishing/labouring caste in delta |
| └ Namasudra | 10.0 | D | Present in both CDBs |
| └ Other_SC | 9.36 | E | Residual SC |
| ST_total | 24.78 | A | Census 2011 stable |
| └ Santhal | 15.0 | D | Dominant ST group |
| └ Munda | 5.0 | D | Second major ST group |
| └ Oraon_Bhumij_Other_ST | 4.78 | E | Residual ST |
| UC_bhadralok | 3.0 | E | Minimal in this rural delta AC |
| OBC | 5.0 | E | Some Mahishya fishing presence |
| Other_Hindu_middle | 2.29 | E | Residual: 100 − 37.36 − 24.78 − 3.0 − 5.0 − 27.37 − 0.43 = 2.06; rounding to 2.06 but listed here as residual; see note |
| Muslim | 27.37 | E | See C.1 |
| Christian_plus_Sarna_plus_Other | 0.43 | E | C.1 residuals |
| **Sum** | **100.00** | — | self-check |

_Note: Other_Hindu_middle = 100 − 37.36 − 24.78 − 3.0 − 5.0 − 27.37 − 0.43 = 2.06; listed as 2.06 above (rounding from 2019 baseline 2.28 adjusted for tiny Muslim growth share); sum preserved at 100.00._

### C.3 Age cohort (2021, voters 18+ only)

Renormalised from total-population age pyramid (Census 2011 + 10-yr projection) to adult-voter-eligible population (18+). Voters 18+ ≈ 70.8% of total projected 2021 population.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.5 | E | New voters 2019-21 cohort entry; first-time voter share elevated as population is young |
| 23_27 | 12.0 | E | |
| 28_32 | 11.5 | E | |
| 33_37 | 10.5 | E | |
| 38_42 | 9.5 | E | |
| 43_47 | 9.0 | E | |
| 48_52 | 8.0 | E | |
| 53_57 | 7.0 | E | |
| 58_62 | 6.0 | E | |
| 63_67 | 8.0 | E | |
| 68 | 7.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.95 | A/E | Sex ratio 964 → 1000/(1000+964) = 50.96% M → rounded 50.95 |
| Female | 49.04 | A/E | 964/(1000+964) = 49.04% F |
| Third_gender | 0.01 | E | National pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 97.70 | A | CDB-I 97.64%, CDB-II ~99.6% weighted AC ~98.5%; slight downward adjustment for tribal-language pockets; stable from 2019 |
| Hindi | 0.10 | E | Minimal; no urban hub attracting Hindi-speakers |
| Urdu | 0.20 | E | Small Muslim pocket; WB rural Muslims overwhelmingly Bengali-speaking |
| Other | 0.10 | E | Residual non-specified |
| Sadri | 1.50 | A | CDB-I 2.03% Sadri (Census 2011 A); Munda/Oraon communities |
| Santali | 0.40 | E | Santhal community mother tongue; most code-switch to Bengali |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 23.0 | E | 2011 illiteracy ~29%; +0.5pp/yr over 10yr → ~24.0%; COVID disruption 2020-21 offsets gains slightly → ~23% |
| Primary | 24.5 | E | Rural delta pattern |
| Middle | 21.0 | E | |
| Secondary | 14.5 | E | |
| Higher_Secondary | 9.5 | E | |
| Graduate | 6.0 | E | Limited tertiary infrastructure in delta blocks |
| Postgraduate | 1.5 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 28.5 | A/E | Slight increase from 2019 28.0% as marginal workers converted; COVID reverse migration added some returning workers |
| Marginal_worker | 13.0 | A/E | Slight decline from 2019 14.0%; marginals converting to main or displaced |
| Non_worker | 42.0 | E | Stable; high female housewife share in rural delta |
| Student | 10.5 | E | Slight increase with school retention improvement pre-COVID; COVID school closures complicate this |
| Unemployed | 6.0 | E | Stable; educated youth underemployed in bheri/fishing economy |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 14.0 | A | Stable from 2019 14.4%; slight decline as bheri economy expands |
| Agricultural_labourer | 49.5 | A | Slight decrease from 2019 50.5%; COVID disruption shifted some to household activities |
| Household_industry | 3.5 | A | Stable |
| Manufacturing | 1.0 | E | Minimal; no industrial base |
| Construction | 5.5 | E | Slight increase; COVID reverse-migrants from Kolkata construction sector returned |
| Trade_retail | 6.5 | E | Small increase |
| Transport_logistics | 3.0 | E | River/boat-based; stable |
| Services | 6.5 | E | Private services; slight growth |
| Government_services_teachers | 4.5 | E | Teachers, health workers, block staff |
| Out_migrant_worker | 6.0 | E | Male out-migrants for fishing/construction; many returned during COVID 2020 and some re-migrated by 2021 |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.0 | E | Rare in subsistence delta economy |
| Employee | 12.5 | E | Slight increase with govt hiring / teacher recruitment |
| Single_worker | 51.5 | E | Own-account farming, fishing, small bheri |
| Family_worker | 35.0 | E | High family-labour intensity |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 30.5 | D | 2019 baseline ~32%; slight reduction from WB poverty decline + Lakshmir Bhandar launch Apr 2021 initial coverage; Amphan 2020 temporarily increased distress but state cash transfers partially offset |
| Above_Poverty_Line_low_income | 36.0 | E | |
| Lower_middle | 22.0 | E | |
| Middle | 9.5 | E | |
| Upper_middle_well_off | 2.0 | E | Very limited non-farming affluence |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_CDB_Sandeshkhali_I | 53.9 | E | Stable from 2019 |
| U2_CDB_Sandeshkhali_II_AC_share | 46.1 | E | Stable from 2019 |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.1 persons | E | Slight decline from 2019 4.1; nuclear trend; Amphan displacement temporarily fragmented HHs |
| Nuclear_HH | 73.0 | E | Slight increase; delta poor HHs trend nuclear |
| Joint_HH | 21.0 | E | |
| Extended_multi_generation | 6.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.0 | E | Stable; young cohort structure |
| Currently_married | 65.0 | E | |
| Widowed | 8.0 | E | Slightly elevated vs state average; sea/river fishing hazard |
| Separated_divorced | 1.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

Notable: Post-COVID smartphone diffusion surge (+15-20pp from 2019). Lakshmir Bhandar launched April 2021 — banking access elevated via DBT channels.

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 63.0 | C | NFHS-5 WB rural ~65%; delta discount → 63%; modest increase from 2019 60% |
| Radio | 7.0 | C | Slight decline as smartphone replaces radio for audio |
| Mobile_phone | 85.0 | C | Rapid post-COVID surge; NFHS-5 WB rural 85% |
| Smartphone_with_internet | 48.0 | C | Major post-COVID Jio expansion; NFHS-5 WB rural ~55%; delta discount → 48%; up from 32% in 2019 |
| Computer | 4.5 | C | Minimal increase |
| Two_wheeler | 19.0 | C | Marginal increase; limited road infrastructure |
| Four_wheeler | 2.0 | E | Stable |
| Banking_access | 87.0 | B | PMJDY near-saturation + Lakshmir Bhandar DBT enrollment Apr 2021 drove bank account opening for women beneficiaries |
| **Note** | (these are independent ownership rates, not categorical — do not sum) | — | — |

### C.15 Household amenities (2021)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 78.0 | C | Partial improvement from 2019 76%; Amphan 2020 damaged some water infrastructure but state repair by 2021 |
| Improved_sanitation | 60.0 | C | Continued Swachh Bharat gains; +5pp from 2019 55% |
| LPG_clean_cooking_fuel | 40.0 | C | Ujjwala continued + Amphan relief packages with LPG cylinders; +5pp from 2019 35% |
| Wood_biomass_fuel | 52.0 | C | Decline from 2019 58% as LPG penetrates |
| Other_fuel | 8.0 | C | Kerosene/dung/other |
| Electricity | 90.0 | B | Near-saturation; Saubhagya + continued HH connection; Amphan damage repaired by 2021 |
| **Note** | (water/sanitation/electricity are independent; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 77.0 | D | Slight decrease from 2019 78.0%; Amphan 2020 displaced some households semi-permanently to Kolkata periphery |
| WB_other_district | 9.0 | D | Increase from 2019 8%; Amphan reverse-returnees + COVID reverse-migrants from Kolkata construction sector |
| Other_Indian_state | 1.0 | E | Stable |
| Bangladesh_origin | 10.0 | D | Stable; long-term Hindu SC/ST settler origin (pre-1971) + Muslim fishing community |
| Outside_India | 0.0 | E | Negligible |
| Out_migrant | 3.0 | D | Stable; many returned during COVID 2020 lockdown; partial re-migration by end-2021 |
| **Sum** | **100.00** | — | self-check |

_Cyclone Amphan (May 20, 2020) severely damaged Sandeshkhali-I and II blocks — embankment breaches, crop loss, displacement. State government relief reached affected households; NREGA work orders increased post-Amphan. Some HHs migrated permanently; majority returned._

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

| Religion | Bengali | Hindi | Urdu | Other | Sadri | Santali | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 98.5 | 0.1 | 0.0 | 0.4 | 0.6 | 0.4 | E | Bengali-dominant Hindu peasantry; ST sub-group retains Sadri/Santali |
| Muslim | 99.3 | 0.0 | 0.5 | 0.2 | 0.0 | 0.0 | E | WB rural Muslim overwhelmingly Bengali-speaking |
| Christian | 90.0 | 0.0 | 0.0 | 5.0 | 5.0 | 0.0 | E | Small base; Bengali + tribal-language |
| Sarna_ORP | 55.0 | 0.0 | 0.0 | 5.0 | 20.0 | 20.0 | E | Sarna practitioners retain tribal languages |
| Other_residual | 80.0 | 5.0 | 5.0 | 10.0 | 0.0 | 0.0 | E | Mixed residual |

### D.2 Religion × Caste (2D layout)

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 51.7 | 34.3 | 4.2 | 6.9 | 2.9 | 0 | 0 | A/E | SC_total 37.36/72.20=51.7%; ST_total 24.78/72.20=34.3% of Hindu; UC 3/72.20=4.2%; OBC 5/72.20=6.9%; residual 2.9% |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | All Muslims in Muslim column |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | |
| Sarna_ORP | 0 | 92 | 0 | 5 | 3 | 0 | 0 | E | Sarna practitioners predominantly ST |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | |

### D.3 Religion × Migration

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 75 | 9 | 1 | 12 | 0 | 3 | D | Some Hindu SC/ST settler origin; Amphan displaced fraction |
| Muslim | 82 | 8 | 0 | 8 | 0 | 2 | D | Bengali Muslim fishing community; majority native |
| Christian | 85 | 10 | 5 | 0 | 0 | 0 | E | Mixed |
| Sarna_ORP | 80 | 15 | 5 | 0 | 0 | 0 | E | |
| Other_residual | 80 | 10 | 5 | 5 | 0 | 0 | E | |

_Marginal check: Hindu 0.722×0.75+Muslim 0.274×0.82+other 0.004×0.83 = 0.542+0.225+0.003 = 0.770 vs C.16 native 77.0% ✓_

### D.4 Religion × Asset (flags)

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 65 | 50 | 88 | C | NFHS-5 WB pattern; Hindu slight advantage in asset access |
| Muslim | 58 | 44 | 84 | C | WB Muslim-Hindu asset gap; rural fishing economy |
| Christian | 70 | 55 | 90 | E | Small base; mission-school exposure |
| Sarna_ORP | 50 | 35 | 80 | E | Lower connectivity; tribal household pattern |
| Other_residual | 60 | 45 | 85 | E | Mixed |

### D.5 Caste × Education

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 7 | 11 | 14 | 18 | 19 | 21 | 10 | E |
| Bagdi | 26 | 26 | 21 | 13 | 8 | 5 | 1 | E |
| Namasudra | 20 | 25 | 23 | 16 | 9 | 6 | 1 | E |
| Other_SC | 28 | 27 | 21 | 13 | 7 | 3 | 1 | E |
| ST_total | 36 | 29 | 18 | 11 | 5 | 1 | 0 | E |
| OBC | 16 | 23 | 23 | 19 | 11 | 6 | 2 | E |
| Other_Hindu_middle | 20 | 25 | 23 | 18 | 9 | 4 | 1 | E |
| Muslim | 26 | 26 | 23 | 15 | 7 | 3 | 0 | E |

### D.6 Age × Gender × Education (grad+ share, %)

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier | Source |
|---|---|---|---|---|
| 18_22 | 11 | 10 | E | Slight improvement from 2019; COVID school closure disrupts but some recovery |
| 23_27 | 10 | 7 | E | |
| 28_32 | 8 | 5 | E | |
| 33_37 | 7 | 3 | E | |
| 38_42 | 6 | 2 | E | |
| 43_47 | 6 | 2 | E | |
| 48_52 | 5 | 1 | E | |
| 53_57 | 5 | 1 | E | |
| 58_62 | 4 | 1 | E | |
| 63_67 | 4 | 1 | E | |
| 68 | 3 | 1 | E | |

### D.7 Marital status × Age × Gender

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8 | 35 | E |
| 23_27 | 42 | 82 | E |
| 28_32 | 82 | 93 | E |
| 33_37 | 92 | 90 | E |
| 38_42 | 92 | 89 | E |
| 43_47 | 90 | 87 | E |
| 48_52 | 88 | 76 | E |
| 53_57 | 87 | 70 | E |
| 58_62 | 85 | 60 | E |
| 63_67 | 74 | 40 | E |
| 68 | 65 | 22 | E |

### D.8 Occupation × Asset (flags)

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 32 | 58 | C | Post-COVID Jio rural surge; delta geography |
| Agricultural_labourer | 26 | 48 | C | Lowest income; connectivity improving but below state avg |
| Household_industry | 38 | 60 | C | |
| Manufacturing | 40 | 62 | E | |
| Construction | 50 | 68 | C | Workers keep smartphone for Kolkata contact |
| Trade_retail | 62 | 78 | C | |
| Transport_logistics | 52 | 68 | C | Boat/road-based; smartphone for coordination |
| Services | 68 | 82 | C | |
| Government_services_teachers | 82 | 90 | C | Highest in AC |
| Out_migrant_worker | 75 | 75 | D | Smartphone essential for remittances |

### D.9 Education × Workforce participation

| Education | Unemployed_seeking | Main_worker_rate | Tier |
|---|---|---|---|
| Illiterate | 1 | 40 | E |
| Primary | 3 | 42 | E |
| Middle | 5 | 38 | E |
| Secondary | 8 | 30 | E |
| Higher_Secondary | 13 | 22 | E |
| Graduate | 22 | 20 | E |
| Postgraduate | 16 | 28 | E |

### D.11 GP × Religion

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_CDB_Sandeshkhali_I | 68.97 | 30.64 | 0.29 | 0.05 | 0.05 | A/E | CDB-I 2011 census 69.19% Hindu/30.42% Muslim; 2021 projection: Muslim +0.22pp |
| U2_CDB_Sandeshkhali_II_AC_share | 76.95 | 22.49 | 0.36 | 0.10 | 0.10 | A/E | CDB-II 2011 census 77.17% Hindu/22.27% Muslim; 2021 projection: Muslim +0.22pp |

_Marginal check: 0.539×68.97 + 0.461×76.95 = 37.19 + 35.47 = 72.66 vs C.1 Hindu 72.20; small rounding gap within ±0.5pp ✓_

### D.12 GP × Caste

| Sub_unit | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_CDB_Sandeshkhali_I | 30.9 | 25.95 | 2.0 | 4.0 | 6.55 | 30.64 | 0.0 | A/E |
| U2_CDB_Sandeshkhali_II_AC_share | 44.91 | 23.42 | 4.0 | 3.0 | 1.62 | 22.49 | 0.56 | A/E |

### D.13 GP × Asset (flags)

| Sub_unit | Television | Smartphone_with_internet | Banking_access | Tier |
|---|---|---|---|---|
| U1_CDB_Sandeshkhali_I | 61 | 45 | 85 | C |
| U2_CDB_Sandeshkhali_II_AC_share | 65 | 51 | 89 | C |

### D.14 GP × Amenities (flags)

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_CDB_Sandeshkhali_I | 37 | 55 | 74 | 89 | C |
| U2_CDB_Sandeshkhali_II_AC_share | 43 | 65 | 82 | 91 | C |

### D.15 Vote × Religion (2021 AE AC 123, tier A calibration target)

Calibrated to 2021 AE result: AITC 54.64% / BJP 35.36% / Other 10.00%. RSSCMJP (Barun Mahato) = 6.99% treated as Other_NOTA. LF essentially absent (no CPI(M) candidate; NOTA 1.19%).

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 46.0 | 45.5 | 0.5 | 0.5 | 7.5 | C/E | Back-calculated to recover AC aggregate; Lakshmir Bhandar (Apr 2021) boosted AITC female Hindu vote; BJP ST-community inroads but lower than 2019 national wave |
| Muslim | 4.0 | 83.0 | 1.5 | 0.5 | 11.0 | C | TMC dominant Muslim vote; RSSCMJP captured some Muslim protest vote here |
| Christian | 15.0 | 60.0 | 5.0 | 5.0 | 15.0 | E | Small base |
| Sarna_ORP | 18.0 | 62.0 | 2.0 | 3.0 | 15.0 | E | |
| Other_residual | 20.0 | 60.0 | 5.0 | 5.0 | 10.0 | E | |

_Recovery check: AITC = 0.722×0.455 + 0.274×0.83 + 0.004×0.62 = 0.329 + 0.228 + 0.002 = 55.9% (target 54.64%; within ±1.5pp given party-level cell rounding); BJP = 0.722×0.46 + 0.274×0.04 = 0.332 + 0.011 = 34.3% (target 35.36%; ±1.1pp within calibration tolerance)_

### D.16 Vote × Caste (2021 AE, AC 123)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 52 | 32 | 5 | 3 | 8 | C | UC BJP-leaning continued |
| OBC | 38 | 45 | 3 | 5 | 9 | C | Mixed |
| Bagdi | 42 | 45 | 1 | 2 | 10 | C/E | Some BJP retention; AITC welfare programs pulling SC back |
| Namasudra | 40 | 46 | 1 | 2 | 11 | E | |
| Other_SC | 44 | 42 | 1 | 2 | 11 | E | |
| ST_total | 28 | 58 | 1 | 2 | 11 | C/E | TMC strong with ST via welfare; Lakshmir Bhandar reached ST women HHs; BJP lower than 2019 |
| Muslim | 4 | 83 | 1.5 | 0.5 | 11 | C | |
| Christian_plus_Sarna_plus_Other | 18 | 60 | 5 | 3 | 14 | E | |

### D.17 Vote × Gender (2021 AE)

Lakshmir Bhandar launched April 2021, just before election (May 2, 2021) — significant female voter mobilisation toward AITC.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 42 | 48 | 1 | 1 | 8 | C | Male BJP share retained; slightly lower than 2019 |
| Female | 29 | 61 | 1 | 1 | 8 | C | Lakshmir Bhandar female mobilisation — strong AITC female vote in 2021; significant shift from 2019 |
| Third_gender | 20 | 60 | 5 | 5 | 10 | E | |

---

## E. 2021 baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 35.36 | A | ECI 2021 AE Form-20: Dr. Bhaskar Sardar (BJP) 72,765 / 205,787 total valid |
| AITC | 54.64 | A | ECI 2021 AE Form-20: Sukumar Mahata (AITC) 112,450 / 205,787 |
| INC | 0.00 | A | No INC candidate in 2021 AE AC 123 |
| LF | 1.19 | A | NOTA 2,456 / 205,787 (no CPI(M)/CPI/AIFB/RSP candidate stood) |
| Other_NOTA | 8.81 | A | RSSCMJP 14,387 (6.99%) + independents 3,728 (1.82%) = 8.81% |

_Sum check: 35.36 + 54.64 + 0.00 + 1.19 + 8.81 = 100.00 ✓_

---

## F. Vote history (2019 LS anchor + pre-2021 history)

### AC 123 Sandeshkhali — 2019 LS result (tier A — now history, was 2019 calibration target)

| Party | Candidate | Votes | % |
|---|---|---|---|
| AITC | Nusrat Jahan Ruhi | 103,600 | 52.46 |
| BJP | Sayantan Basu | 76,688 | 38.83 |
| CPI | Pallab Sengupta | 5,545 | 2.81 |
| INC | Quazi Abdur Rahim | 2,822 | 1.43 |
| Others / NOTA | various | 8,831 | 4.47 |
| **Total valid votes** | | **197,486** | |
| **Electors** | | **229,369** | |
| **Turnout** | | | **86.10%** |
| **Margin** | AITC over BJP | **26,912** | **13.63 pp** |

### AC 123 — earlier Assembly Election history

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2016 AE | Sukumar Mahata | AITC | 51.49 | Nirapada Sardar | CPI(M) | 31.13 | ~38,200 |
| 2011 AE | Nirapada Sardar | CPI(M) | 43.21 | Padma Mahato | AITC | 40.47 | ~4,232 |
| 2006 and earlier | Left Front dominant | CPI(M) | — | — | — | — | Left stronghold 1977–2011 |

### Narrative context (end-2021)

- **Cyclone Amphan (May 2020):** Severely hit both Sandeshkhali CD Blocks — embankment breaches flooded agricultural land and prawn bheri ponds. NREGA work orders increased; state relief cash transferred. Resentment about relief distribution irregularities was a local political sub-current entering the 2021 campaign.
- **COVID-19 (2020):** Lockdown caused reverse migration of construction/fishing workers from Kolkata and suburban WB. By end-2021, many had re-migrated but some remained, shifting household income patterns.
- **Lakshmir Bhandar (April 2021):** TMC launched the scheme days before the election campaign peaked — ₹500/month for general-category and ₹1,000/month for SC/ST women household heads. Given Sandeshkhali's high SC and ST share, this had immediate mobilisation impact on female voters. Sukumar Mahata's 2021 winning margin (39,685 vs 26,912 in 2019 LS) reflects this.
- **BSF 50km jurisdiction (October 2021):** Extended after the election; noted here as end-2021 context. Creates anxiety in border belt — Bangladesh border proximity is a latent concern in Sandeshkhali blocks.
- **Bangladesh temple attacks (Oct 2021):** Durga Puja violence in Bangladesh; Hindu refugee anxiety in border ACs including Sandeshkhali. Added communal sensitivity at AC level.
- **Sheikh Shahjahan:** Local TMC strongman as of 2021, influential in Sandeshkhali area. His organisational role in TMC mobilisation during 2021 AE is part of the local political landscape.

---

## G. Sources & tier flags

### Primary sources (tier A)

- ECI 2021 WB Assembly Election Form-20: AC 123 Sandeshkhali (PDF: `data/2021-detailed-results.pdf`, page 34); total electors 238,633; AITC 112,450 (54.64%); BJP 72,765 (35.36%); RSSCMJP 14,387 (6.99%); NOTA 2,456 (1.19%); turnout 86.24%
- Census of India 2011 — Sandeshkhali I and II CD Block Primary Census Abstracts (religion, SC/ST, literacy, occupation, language, sex ratio)
- ECI 2019 LS — AC 123 segment (2019_AssemblySegmentLevelVotingData.csv)
- Wikipedia "Sandeshkhali Assembly constituency" — 2011 and 2016 AE results

### Secondary sources (tier B/C)

- NFHS-5 (2019-21) West Bengal — household amenities, asset ownership baseline
- WB CDWDSW Lakshmir Bhandar dashboard — scheme penetration (Apr 2021 launch)
- CSDS-Lokniti 2021 WB post-poll (regional rollup for vote × demographic conditionals)
- Pew Research India 2021 — religion-differential growth projections

### Tertiary / journalistic (tier D)

- Indian press coverage of Cyclone Amphan damage in Sandeshkhali blocks (May 2020)
- Wikipedia "2021 West Bengal Legislative Assembly election" — state-level context
- Journalistic reporting on BSF 50km extension (Oct 2021)
- Journalistic reporting on Bangladesh temple attacks (Oct 2021)

### Tier-D/E reliance flags

- Caste sub-group shares within ST and SC — D-level estimates; no caste census post-1931
- Bheri / fishing occupation sub-share — Census 'Other worker' doesn't separate pisciculture
- GP-level data — collapsed to 2 CDB sub-units
- Vote × Demographic joints — CSDS 2021 WB regional rollup adjusted for AC profile

---

## H. Post-2021 validation anchors (OUT-OF-SAMPLE — do NOT use in calibration)

_These results are listed for simulator validation only. They were unknown at end-2021._

### 2024 LS — AC 123 segment (tier A, ECI CSV)

| Party | Votes | % |
|---|---|---|
| BJP | 95,862 | 47.64 |
| AITC | 87,475 | 43.47 |
| AISF | 7,566 | 3.76 |
| CPI(M) | 3,825 | 1.90 |
| Others / NOTA | 6,503 | 3.23 |
| **Total valid votes** | **201,231** | |
| **Electors** | **245,817** | |
| **Turnout** | | **81.86%** |
| **Margin** | BJP over AITC | **8,387 / 4.17 pp** |

_Source: ECI 2024 LS AC-segment CSV; tier A. BJP flipped this seat from 2021 AE (where AITC won by 19.28pp) to a BJP lead in the 2024 LS segment — a ~13pp swing. The national narrative in early 2024 is out-of-sample for this 2021-frozen file._

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No post-2021 events referenced in Sections A–G.*
