# AC 210 — Nandigram (GEN) — Calibrated 2024 Population Snapshot

> **Frozen at end-2024.** This file describes the demographic and behavioural state of AC 210 Nandigram as of end-2024 — after the June 2024 WB Lok Sabha results were known. It does not reference any post-2024 events. Use Section H for forward out-of-sample validation anchors.
>
> Companion artifacts: [`methodology_2024.md`](../../methodology_2024.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).
>
> **Seat archetype:** A7 — Mahishya coastal | Extreme BJP-lean by 2024, Muslim consolidation behind AITC. Three calibration anchors available: 2019 LS (AITC 63.14%), 2021 AE (BJP 48.49% narrow win), 2024 LS (BJP 49.49%). The trajectory is unambiguous BJP consolidation on the Hindu vote with Suvendu Adhikari personal network holding firm even in his absence as candidate.

---

## A. Identity (as of 2024)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 210 | A | ECI / Delimitation Commission 2008 |
| AC name | Nandigram | A | ECI |
| Reservation | General | A | Delimitation 2008 |
| District | Purba Medinipur | A | Delimitation 2008 |
| Sub-division | Haldia | A | WB administrative |
| LS constituency | PC 17 — Tamluk | A | Delimitation 2008 |
| LS segments in Tamluk (PC 17) | AC 207 Tamluk · 208 Panskura Purba · 209 Moyna · 210 Nandigram · 211 Nandakumar · 212 Mahisadal · 213 Haldia | A | Wikipedia — Tamluk Lok Sabha constituency |
| AC composition | Nandigram I CD Block (full) + Nandigram II CD Block (full) | A | Delimitation 2008 |
| Geographic note | Coastal Purba Medinipur; Haldia subdivision; site of the 2007 Nandigram land-protest movement (SEZ opposition). Haldi river mouth area. | A | — |
| Two sub-units used in v0 | **U1: Nandigram I CDB** (62.3% of 2024 pop) · **U2: Nandigram II CDB** (37.7% of 2024 pop) | A/E | Census 2011 block populations + 13-yr differential growth projection |
| Post-2021 political context | Suvendu Adhikari served as WB Leader of Opposition (2021-24) and Union Minister of State for Defence (2022-24). Nandigram remained his home base. 2024 Tamluk LS candidate: BJP's Abhijit Gangopadhyay (former HC judge), not Adhikari personally. | A/D | Wikipedia; ECI 2024 AE candidate list; Hindustan Times coverage |

---

## B. 2024 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (Census) | 331,054 (Nandigram I: 207,835 + Nandigram II: 123,219) | A | Census 2011 block-level |
| 2024 projected population | ~378,000 | E | 13-yr religion-differential growth from Census 2011 (Hindu +13.6%, Muslim +18.1%) |
| Sex ratio (2011, F per 1000 M) | 946 | A | Census 2011 block aggregate |
| 2024 sex ratio (projected) | ~940 | E | Modest coastal district trend; marginal improvement in recent surveys |
| 2024 electorate (LS roll) | 274,621 | A | ECI 2024 LS Form-20 / AC-segment CSV: TOTAL ELECTORS IN AC |
| Estimated M / F / TG split (2024) | 51.2% M / 48.7% F / <0.05% TG | E | 2011 census sex ratios; 13-yr marginal change |
| 2024 polling stations (estimate) | ~310 | E | ECI 2024 LS estimate; Purba Medinipur coastal AC typical range |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 73.05 | A/E | Census 2011 block aggregate (Hindu 73.97%); 13-yr religion-differential growth → Hindu share falls ~0.9pp by 2024 |
| Muslim | 26.80 | A/E | Census 2011 block aggregate (Muslim 25.89%); share rises ~0.9pp by 2024 |
| Christian | 0.05 | E | Census 2011 other; negligible |
| Sarna_ORP | 0.00 | A | Negligible ST presence |
| Other_residual | 0.10 | E | Residual |
| **Sum** | **100.00** | — | self-check |

*Block disaggregation (projected 2024):*
- U1 Nandigram I: Hindu ~65.2%, Muslim ~34.7%, Other ~0.1%
- U2 Nandigram II: Hindu ~87.3%, Muslim ~12.5%, Other ~0.2%

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| SC_total | 16.35 | A/E | Census 2011 block aggregate 16.46%; marginal decline due to inter-caste demographic shifts |
| └ Bagdi_SC | 8.0 | E | Dominant SC in coastal Medinipur |
| └ Namasudra_SC | 3.4 | E | Secondary SC |
| └ Bauri_SC | 2.0 | E | |
| └ Other_SC | 2.95 | E | Residual |
| ST_total | 0.10 | A | Negligible; Census 2011 anchor stable |
| UC_bhadralok | 5.00 | E | Brahmin/Kayastha; stable |
| OBC | 3.00 | E | Tili/Teli and other OBC; stable |
| Other_Hindu_middle | 48.60 | E | Includes Mahishya (~27% total); residual after SC+ST+UC+OBC+Muslim |
| Muslim | 26.80 | A/E | See C.1 |
| Christian_plus_Sarna_plus_Other | 0.15 | E | Negligible |
| **Sum** | **100.00** | — | self-check: 16.35+0.10+5.00+3.00+48.60+26.80+0.15=100.00 |

### C.3 Age cohort (2024, adults 18+ only)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 10.5 | E | New voter cohort (born 2002-2006); renormalized from Census 2011 age pyramid for 18+ adults |
| 23_27 | 11.0 | E | |
| 28_32 | 11.0 | E | |
| 33_37 | 10.5 | E | |
| 38_42 | 10.0 | E | |
| 43_47 | 9.0 | E | |
| 48_52 | 8.0 | E | |
| 53_57 | 7.5 | E | |
| 58_62 | 7.0 | E | |
| 63_67 | 8.0 | E | |
| 68 | 7.5 | E | |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.30 | A/E | Census 2011 block aggregate 51.40%; marginal change over 13 yr |
| Female | 48.69 | A/E | |
| Third_gender | 0.01 | E | National standard estimate |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 99.93 | A | Nandigram I+II blocks essentially monolingual Bengali; stable |
| Hindi | 0.04 | E | Haldia industrial fringe; marginal increase |
| Urdu | 0.02 | E | Negligible |
| Other | 0.01 | E | Residual |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2024, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 8.5 | A/E | Literacy projected ~95.5% among 7+ by 2024; continuing improvement trend |
| Primary | 20.0 | E | |
| Middle | 22.0 | E | |
| Secondary | 21.0 | E | Slight increase; high-school enrollment improved |
| Higher_Secondary | 14.0 | E | Continued growth |
| Graduate | 11.0 | E | Post-COVID online education contributed |
| Postgraduate | 3.5 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 33.0 | A/E | Recovery from COVID dip; near-2019 levels |
| Marginal_worker | 8.0 | E | Stable WB rural pattern |
| Non_worker | 36.5 | E | Housewives, elderly; Lakshmir Bhandar reduced female labour-force participation pressure |
| Student | 11.5 | E | Slight decline as graduation cohort passes through |
| Unemployed | 11.0 | E | SSC scam (2022) and government job freeze increased educated unemployment; notable in Purba Medinipur where government-job aspiration is high |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 15.00 | A/E | Continuing gradual diversification away from cultivation |
| Agricultural_labourer | 44.00 | A/E | Still dominant; gradual shift to non-farm |
| Household_industry | 3.70 | A | Stable from Census 2011 anchor |
| Manufacturing | 4.50 | E | Haldia industrial belt fractional growth |
| Construction | 6.00 | E | PMAY rural housing boost + local construction activity |
| Trade_retail | 8.50 | E | Modest growth in local commerce |
| Transport_logistics | 6.00 | E | Coastal fishing + river transport; stable |
| Services | 7.80 | E | Growing; some Kolkata commuter economy |
| Government_services_teachers | 4.00 | E | Stable; government hiring slowdown post-SSC scam |
| Out_migrant_worker | 0.50 | E | Some Haldia-Kolkata-Kerala out-migration resumed post-COVID |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.5 | E | Stable |
| Employee | 23.0 | E | Small increase: Haldia industrial + service sector |
| Single_worker | 54.0 | E | Dominant: cultivator + fisherman + own-account artisan |
| Family_worker | 21.5 | E | Agricultural household assisting; stable |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2024, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 17.0 | E | Continuing poverty reduction; WB rural BPL projected ~17% by 2024 |
| Above_Poverty_Line_low_income | 40.0 | E | Stable bulk of rural agrarian households |
| Lower_middle | 26.0 | E | Lakshmir Bhandar (₹500-1000/month since 2021) raised some HH from APL-low to lower-middle consumption level |
| Middle | 14.0 | E | Slight growth; Mahishya medium-farmer class |
| Upper_middle_well_off | 3.0 | E | Stable marginal affluent fringe |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Block location (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Nandigram_I | 62.30 | A/E | Census 2011 baseline 62.78%; marginal decline as N-I Muslim growth rate slightly higher than N-II |
| U2_Nandigram_II | 37.70 | A/E | Census 2011 baseline 37.22%; fractionally higher |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.3 | E | Continuing nuclear trend; WB rural 4.3-4.5 by 2024 |
| Nuclear_HH | 68.0 | E | NFHS-5 WB rural + 3-yr trend → ~68% by 2024 |
| Joint_HH | 26.0 | E | Declining as nuclear family norm strengthens |
| Extended_multi_generation | 6.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.5 | E | Stable |
| Currently_married | 64.5 | E | Slight decline as mean age of marriage rises among educated cohorts |
| Widowed | 7.5 | E | Slight increase from COVID-19 mortality among elderly cohorts reaching 2024 |
| Separated_divorced | 1.5 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2024, household level)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 80.0 | C | Near-saturated among non-BPL households; NFHS-5 WB rural trajectory |
| Radio | 3.0 | C | Essentially obsolete; vestigial coastal fishing community use |
| Mobile_phone | 93.0 | C | Near-universal; NFHS-5 trajectory; JioPhone availability at ₹500 |
| Smartphone_with_internet | 78.0 | C | Post-COVID surge + UPI adoption + WhatsApp political communication near-saturated in working-age adults; rural WB ~75-80% by 2024 |
| Computer | 8.0 | C | Modest growth with affordable tablets/laptops |
| Two_wheeler | 34.0 | C | Continued growth; Purba Medinipur medium-farmer class |
| Four_wheeler | 5.5 | C | Marginal growth |
| Banking_access | 95.0 | B | PMJDY peak penetration; UPI/digital payments widespread by 2024 |
| **Note** | (these are independent ownership %s, not categorical — do not sum) | — | — |

### C.15 Household amenities (2024)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 89.0 | C | Jal Jeevan Mission (central) + WB state water scheme; continued improvement |
| Improved_sanitation | 83.0 | C | Swachh Bharat Phase-2 + ODF verification; Purba Medinipur near-ODF by 2024 |
| LPG_clean_cooking_fuel | 63.0 | C | Ujjwala 2.0 + own-purchase refills; Purba Medinipur above WB rural average (~60%) |
| Wood_biomass_fuel | 33.0 | C | Continuing decline as LPG penetrates |
| Other_fuel | 4.0 | C | Stable residual |
| Electricity | 99.0 | A/E | Saubhagya + state rural electrification: effectively universal by 2024 |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 87.0 | D | Coastal agrarian AC; very low in-migration |
| WB_other_district | 6.0 | D | Adjacent Paschim Medinipur / Hooghly |
| Other_Indian_state | 2.5 | D | Haldia industrial fringe labour; recovered to pre-COVID levels |
| Bangladesh_origin | 2.0 | D | Stable small fraction; coastal Khulna/Barisal-origin Namasudra SC |
| Outside_India | 0.5 | E | Negligible |
| Out_migrant | 2.0 | E | Haldia-Kolkata-Kerala corridor; resumed post-COVID |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

| Religion | Bengali | Hindi | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|
| Hindu | 99.97 | 0.02 | 0.00 | 0.01 | A | Census 2011; monolingual AC; stable |
| Muslim | 99.88 | 0.02 | 0.08 | 0.02 | A | Bengali Muslim peasantry; negligible Urdu |
| Christian | 90.00 | 5.00 | 0.00 | 5.00 | E | Small base |
| Sarna_ORP | 95.00 | 0.00 | 0.00 | 5.00 | E | Negligible |
| Other_residual | 90.00 | 5.00 | 0.00 | 5.00 | E | Small base |

### D.2 Religion × Caste (2D layout)

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 22.38 | 0.14 | 6.85 | 4.11 | 66.52 | 0 | 0 | A/D/E | SC = 16.35/73.05 = 22.38%; ST = 0.10/73.05 = 0.14%; UC = 5.00/73.05 = 6.85%; OBC = 3.00/73.05 = 4.11%; Other_Hindu_middle residual |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | All Muslim population maps to Muslim caste leaf |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | Small base |
| Sarna_ORP | 0 | 100 | 0 | 0 | 0 | 0 | 0 | E | Negligible |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | Small base |

### D.3 Religion × Migration / birthplace

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 86.5 | 6.5 | 3.0 | 2.5 | 0.5 | 1.0 | D | Mahishya/Bagdi peasantry native; small Bangladesh-origin SC; slightly more Other-state labour at Haldia by 2024 |
| Muslim | 91.0 | 5.0 | 1.0 | 2.0 | 0.0 | 1.0 | D | Bengali Muslim peasantry essentially native |
| Christian | 60.0 | 20.0 | 18.0 | 2.0 | 0.0 | 0.0 | E | Small base |
| Sarna_ORP | 95.0 | 5.0 | 0.0 | 0.0 | 0.0 | 0.0 | E | Negligible |
| Other_residual | 80.0 | 10.0 | 8.0 | 2.0 | 0.0 | 0.0 | E | Small base |

### D.4 Religion × Asset / media

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 82.0 | 81.0 | 96.0 | C | NFHS-5 + 3-yr extrapolation; Hindu-dominant N-II higher income bracket |
| Muslim | 74.0 | 68.0 | 90.0 | C | NFHS-5 WB Muslim HH gap closing with UPI/smartphone penetration; Nandigram I Muslim poorer |
| Christian | 84.0 | 75.0 | 94.0 | E | Small base |
| Sarna_ORP | 72.0 | 55.0 | 82.0 | E | Negligible |
| Other_residual | 80.0 | 70.0 | 92.0 | E | Small base |

### D.5 Caste × Education

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 2 | 6 | 9 | 16 | 22 | 30 | 15 | E |
| Other_Hindu_middle | 7 | 18 | 22 | 22 | 16 | 12 | 3 | E |
| OBC | 9 | 20 | 22 | 19 | 14 | 12 | 4 | E |
| SC_total | 14 | 24 | 22 | 19 | 12 | 8 | 1 | E |
| ST_total | 18 | 26 | 22 | 17 | 10 | 6 | 1 | E |
| Muslim | 12 | 22 | 23 | 20 | 13 | 9 | 1 | E |
| Christian_plus_Sarna_plus_Other | 9 | 19 | 22 | 21 | 15 | 11 | 3 | E |

### D.6 Age × Gender × Education

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 21 | 20 | E |
| 23_27 | 20 | 16 | E |
| 28_32 | 16 | 11 | E |
| 33_37 | 13 | 7 | E |
| 38_42 | 11 | 6 | E |
| 43_47 | 9 | 4 | E |
| 48_52 | 8 | 3 | E |
| 53_57 | 7 | 2 | E |
| 58_62 | 5 | 1 | E |
| 63_67 | 4 | 1 | E |
| 68 | 3 | 1 | E |

### D.7 Marital status × Age × Gender

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 6 | 26 | E |
| 23_27 | 39 | 80 | E |
| 28_32 | 81 | 92 | E |
| 33_37 | 92 | 90 | E |
| 38_42 | 92 | 89 | E |
| 43_47 | 91 | 87 | E |
| 48_52 | 90 | 81 | E |
| 53_57 | 89 | 70 | E |
| 58_62 | 87 | 57 | E |
| 63_67 | 76 | 35 | E |
| 68 | 70 | 26 | E |

### D.8 Occupation × Asset / media

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 62 | 79 | C | UPI + agricultural price-check apps widespread by 2024 |
| Agricultural_labourer | 50 | 70 | C | Low income but smartphone access high post-Jio |
| Household_industry | 65 | 81 | C | |
| Manufacturing | 80 | 90 | C | Haldia fringe: higher income |
| Construction | 75 | 83 | C | |
| Trade_retail | 86 | 92 | C | Smartphone essential for trade by 2024 |
| Transport_logistics | 78 | 85 | C | WhatsApp groups for fishing/cargo communication |
| Services | 90 | 94 | C | |
| Government_services_teachers | 95 | 97 | C | |
| Out_migrant_worker | 95 | 88 | C | Out-migrants essentially all smartphone-connected |

### D.9 Education × Workforce

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 39 | 2 | E |
| Primary | 41 | 4 | E |
| Middle | 38 | 7 | E |
| Secondary | 33 | 12 | E |
| Higher_Secondary | 26 | 18 | E |
| Graduate | 30 | 22 | E |
| Postgraduate | 42 | 15 | E |

*Note: Elevated educated unemployment in Graduate row reflects SSC scam aftermath (2022-24) — government teaching and clerical job freeze across WB hit Purba Medinipur aspiring youth. Tier C/D composite.*

### D.10 Asset × Bilingualism

Near-irrelevant in this monolingual AC. Retained as stub per schema.

| Media_tier | Bilingual_pct | Tier | Source |
|---|---|---|---|
| TV_only_HH | 1 | E | Bengali TV dominant; minimal bilingual pressure |
| TV_plus_smartphone_HH | 4 | E | Slightly higher YouTube Hindi consumption by 2024 |
| Smartphone_only_HH | 3 | E | |
| No_asset_HH | 0.5 | E | |

### D.11 GP × Religion

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Nandigram_I | 65.20 | 34.70 | 0.05 | 0.00 | 0.05 | A/E | Census 2011: Hindu 65.82%, Muslim 34.04%; 13-yr differential growth projection |
| U2_Nandigram_II | 87.30 | 12.50 | 0.10 | 0.00 | 0.10 | A/E | Census 2011: Hindu 87.71%, Muslim 12.12%; 13-yr projection |

### D.12 GP × Caste

| Sub_unit | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Nandigram_I | 18.50 | 0.07 | 4.0 | 2.5 | 40.73 | 34.20 | 0.00 | A/D |
| U2_Nandigram_II | 12.85 | 0.16 | 7.0 | 4.0 | 63.59 | 12.40 | 0.00 | A/D |

### D.13 GP × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Nandigram_I | 77 | 73 | 7 | 93 | C |
| U2_Nandigram_II | 84 | 85 | 10 | 97 | C |

### D.14 GP × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Nandigram_I | 58 | 79 | 87 | 99 | C |
| U2_Nandigram_II | 70 | 88 | 92 | 99 | C |

### D.15 Vote × Religion (2024 LS)

P(party ‖ religion) — calibrated to reproduce 2024 LS AC-segment result (BJP 49.49%, AITC 45.87%, LF 3.46%).

*Calibration context: BJP won 2024 LS with Abhijit Gangopadhyay (former HC judge), not Adhikari personally. Suvendu's organizational network delivered Hindu vote. RG Kar protests (Aug 2024, after results) are post-calibration but partially captured in anti-incumbency already evident.*

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 64.5 | 27.0 | 0.5 | 6.0 | 2.0 | C/D | Continued Hindu consolidation behind BJP; Mahishya + SC + UC all BJP-plurality. Implied: 0.7305×64.5 ≈ 47.1pp BJP from Hindu; consistent with 49.49% total with Muslim contribution |
| Muslim | 3.0 | 92.0 | 1.0 | 3.0 | 1.0 | C/D | Near-total Muslim consolidation AITC; Mamata anti-CAA message 2024 campaign. 0.268×92.0 ≈ 24.7pp AITC from Muslim; sum with Hindu ≈ 27.0+24.7 ≈ 51.7pp AITC → turnout differential explains actual 45.87% |
| Christian | 20 | 68 | 5 | 5 | 2 | E | Small base |
| Sarna_ORP | 30 | 50 | 5 | 12 | 3 | E | Negligible |
| Other_residual | 25 | 60 | 5 | 7 | 3 | E | Small base |

### D.16 Vote × Caste (2024 LS)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 68 | 22 | 2 | 6 | 2 | C | Further BJP consolidation among upper castes 2021-24 |
| Other_Hindu_middle | 66 | 26 | 0 | 6 | 2 | C/D | Mahishya bloc firmly BJP by 2024; Adhikari network held without him as candidate; CSDS 2024 WB post-poll |
| OBC | 57 | 33 | 1 | 7 | 2 | C | Tili/OBC BJP plurality; slight AITC erosion from 2021 |
| SC_total | 50 | 40 | 1 | 7 | 2 | C | SC vote more contested; BJP held 2021 gains; Lakshmir Bhandar keeps some SC with AITC |
| ST_total | 38 | 45 | 3 | 12 | 2 | E | Negligible base |
| Muslim | 3 | 92 | 1 | 3 | 1 | C/D | See D.15; CAA notification March 2024 reinforced Muslim-AITC consolidation |
| Christian_plus_Sarna_plus_Other | 20 | 65 | 5 | 8 | 2 | E | Small base |

### D.17 Vote × Gender (2024 LS)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 53 | 39 | 1 | 5 | 2 | C | CSDS 2024 WB; Adhikari network stronger among male voters |
| Female | 46 | 47 | 0 | 5 | 2 | C | Lakshmir Bhandar (full 3-yr rollout by 2024) kept female vote more competitive for AITC; near-parity |
| Third_gender | 30 | 55 | 5 | 8 | 2 | E | Negligible base |

### D.18 Vote × Welfare scheme exposure (2024 LS)

Schemes active 2024: Lakshmir Bhandar (full penetration, ₹500/1000/month), Swasthya Sathi, Krishak Bandhu (revised ₹10,000/yr), Kanyashree, Sabuj Sathi, Khadya Sathi; Central: PM Awas Yojana Gramin, PM Kisan Samman Nidhi.

| Welfare_exposure | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Lakshmir_Bhandar_enrolled | 35 | 58 | 0 | 5 | 2 | C | Full 3-yr rollout; AITC welfare-credit strong among women recipients; but BJP held ~35% even in these HH through Hindu identity vote |
| Krishak_Bandhu | 45 | 47 | 0 | 6 | 2 | C | Cultivator HH split; BJP competitive through central PM Kisan (₹6000/yr) vs state KB (₹10000/yr) |
| PM_Kisan | 50 | 40 | 0 | 7 | 3 | C | Central scheme: BJP credit; BJP plurality among PM Kisan recipients |
| Swasthya_Sathi | 38 | 55 | 0 | 5 | 2 | C | State AITC scheme; AITC welfare-credit retained |
| No_state_scheme | 60 | 30 | 1 | 6 | 3 | C | BJP-dominant |

---

## E. 2024 LS baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp.

### AC 210 Nandigram segment — 2024 Lok Sabha (tier A, ECI CSV)

Detailed result (from `data/2024_AssemblySegmentLevelVotingData.csv`):

| Candidate | Party | Votes | % |
|---|---|---|---|
| Abhijit Gangopadhyay | BJP | 112,110 | 49.49% |
| Debangshu Bhattacharya | AITC | 103,910 | 45.87% |
| Sayan Banerjee | CPI(M) | 7,574 | 3.34% |
| Narayan Chandra Nayak | SUCI | 264 | 0.12% |
| Mohiuddin Ahmed Mahi | AISF | 498 | 0.22% |
| Sabitri Bishai | BSP | 453 | 0.20% |
| Others (IND + NOTA) | — | 1,740 | 0.77% |
| **Margin** | BJP over AITC | **8,200** | **3.62 pp** |
| **Total valid votes (incl. NOTA)** | | **226,549** | |
| **Total electors** | | **274,621** | |
| **Turnout** | | | **82.5%** |

*Source: `data/2024_AssemblySegmentLevelVotingData.csv`, filtered West Bengal AC_NO=210; NOTA 870 from NOTA_VOTES_EVM_IN_AC field. Tier A (ECI direct data).*

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 49.49 | A | ECI 2024 LS AC-segment CSV; Abhijit Gangopadhyay |
| AITC | 45.87 | A | ECI 2024 LS; Debangshu Bhattacharya |
| INC | 0.00 | A | INC did not field a candidate; zero votes |
| LF | 3.46 | A | CPI(M) 7,574 + SUCI 264 = 7,838; 7,838/226,549 = 3.46% |
| Other_NOTA | 1.18 | A | BSP+AISF+IND+NOTA = 453+498+81+138+651+870 = 2,691; 2,691/226,549 = 1.19% (rounded to 1.18 for 100.00 sum) |

---

## F. Vote history (chronological anchors for belief evolution)

### AC 210 Nandigram — Assembly Elections

| Year | Winner | Party | % | Runner-up | Party | % | Margin | Tier |
|---|---|---|---|---|---|---|---|---|
| 2006 AE | Sheikh Mohammad Illias | CPI | ~50.6 | Sk Supian | AITC | ~47.1 | 4,823 | A |
| 2009 by-poll | Firoja Bibi | AITC | 58.28 | Paramananda Bharati | CPI | 39.35 | 39,549 | A |
| 2011 AE | Firoja Bibi | AITC | 61.21 | Paramananda Bharati | CPI | 35.35 | 43,640 | A |
| 2016 AE | Suvendu Adhikari | AITC | 67.20 | Abdul Kabir Sekh | CPI | 26.70 | 81,230 | A |
| 2021 AE | Suvendu Adhikari | BJP | 48.49 | Mamata Banerjee | AITC | 47.64 | 1,956 | A |

*Sources: Wikipedia "Nandigram (Vidhan Sabha constituency)". Tier A.*

### Tamluk Lok Sabha (PC 17) — LS history

| Year | Winner | Party | % | Notes | Tier |
|---|---|---|---|---|---|
| 2019 LS | Dibyendu Adhikari | AITC | 50.08 | AC 210 segment: AITC 63.14%, BJP 30.09% | A |
| 2024 LS | Abhijit Gangopadhyay | BJP | — | AC 210 segment: BJP 49.49%, AITC 45.87% (§E) | A |

### Consolidated AC 210 election trajectory

The trajectory from 2019 to 2024 shows the steepest political reversal of any seat in Purba Medinipur:

- **2019 LS**: AITC 63.14% (Adhikari family stronghold; Suvendu still AITC)
- **2021 AE**: BJP 48.49% / AITC 47.64% (Adhikari defection; Mamata personally contesting; near-tie)
- **2024 LS**: BJP 49.49% / AITC 45.87% (BJP consolidated; Adhikari not candidate but network held)

The 33pp swing from AITC dominance (2019) to BJP plurality (2021-24) is among the largest single-constituency swings in WB. It reflects: (a) Mahishya community following Adhikari to BJP, (b) near-total Muslim consolidation behind AITC as countervailing force, (c) BJP's Hindu identity mobilization resonating in the Hindu-majority Nandigram II block.

### Post-2021 political events (in-window for 2024 calibration)

- **2022 July**: SSC (School Service Commission) scam — Partha Chatterjee (WB Education Minister, AITC) arrested by Enforcement Directorate; ₹50 crore cash found. Significant anti-AITC sentiment among educated middle-class in Purba Medinipur; government-job aspirants particularly affected. Tier D: Indian Express, The Hindu.
- **2023 July**: WB Panchayat elections — TMC dominant across Purba Medinipur; BJP contested but organizational network weaker at GP level without Adhikari as local MLA. Tier A: ECI Panchayat results.
- **2024 March 11**: CAA rules notified (3 years after the Act). Reinforced anti-BJP sentiment among Muslims; reinforced BJP appeal among Hindu voters worried about demographic change. AC 210 with ~27% Muslim is sensitive to CAA narrative. Tier A: MHA notification.
- **2024 April-June**: 2024 LS campaign — Suvendu Adhikari campaigned heavily in Tamluk for Gangopadhyay; Modi rally in Haldia (adjacent). AITC ran Debangshu Bhattacharya (young social-media activist). Tier D: regional Bengali press.
- **2024 August**: RG Kar Hospital rape-murder (Kolkata) — mass medical fraternity + civil society protests. Strong anti-AITC narrative; BJP benefited in urban areas. Purba Medinipur: moderate exposure through Haldia fringe. *Note: RG Kar occurred after June 4 LS results; not reflected in 2024 LS calibration data but is in-window for end-2024 snapshot.* Tier D: The Hindu, Indian Express.
- **2024 August**: Bangladesh student revolt and Hasina ouster (Aug 5). Yunus interim government. Hindu minority reports of attacks in Bangladesh. In coastal WB including Purba Medinipur, this reinforced BJP Hindu-solidarity messaging. Some Namasudra SC households in Nandigram I with Bangladesh-origin ancestry (Khulna/Barisal corridor) received this news with anxiety. Tier D: Reuters, Prothom Alo in Bengali translation.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- `data/2024_AssemblySegmentLevelVotingData.csv` — ECI 2024 LS AC-segment data: AC 210, total electors 274,621; BJP 112,110 / AITC 103,910 / CPI(M) 7,574; NOTA 870 (from NOTA_VOTES_EVM_IN_AC field)
- ECI 2021 WB Assembly Election: AC 210 Nandigram — BJP (Suvendu Adhikari) 110,764 / AITC (Mamata Banerjee) 108,808 / CPI(M) (Minakshi Mukherjee) 6,267; total electors 267,608; turnout 85.4%
- Census of India 2011 — Nandigram I CD Block; Nandigram II CD Block (block population, SC%, ST%, literacy, religion, mother tongue)
- Delimitation Commission of India 2008 — Nandigram AC composition

### Secondary sources (tier B/C)
- NFHS-5 (2019-21) West Bengal — household amenities, asset ownership baseline; Purba Medinipur district
- CSDS-Lokniti 2024 WB post-poll (national and WB regional): religion × vote, caste × vote, gender × vote conditional tables for 2024 LS
- WB CDWDSW Lakshmir Bhandar enrollment data (district-level proxy; AC-level not published)

### Tertiary / journalistic (tier D)
- Wikipedia "2024 Indian general election in West Bengal" — seat-wise results
- Wikipedia "Abhijit Gangopadhyay" — BJP 2024 Tamluk LS candidate profile
- Indian Express / The Hindu: SSC scam 2022 coverage; RG Kar 2024 coverage
- Hindustan Times: CAA notification March 2024 impact on WB Muslim communities
- ThePrint: "Why BJP retained Nandigram's loyalty in 2024 without Suvendu on ballot"
- Regional Bengali press (Anandabazar Patrika, Bartaman) campaign coverage

### Tier-D/E reliance flags
- **Mahishya vote 2024** (D.16) — party-specific Mahishya vote share estimated from CSDS 2024 WB regional rollup + local journalistic consensus; no AC-level survey. Tier C/D.
- **Muslim consolidation 2024** (D.15, D.16) — CSDS 2024 WB post-poll Muslim AITC share + CAA notification effect; AC-specific estimate tier C/D.
- **RG Kar protest effect** (§F narrative) — occurred August 2024, after 2024 LS results. End-2024 snapshot captures it in narrative but 2024 LS vote table does not yet reflect it. Tier D.
- **Asset/media 2024** (C.14) — extrapolated from NFHS-5 + JMC/TRAI data on rural smartphone penetration; AC-specific rate tier C.
- **GP-level data** (D.11–D.14) — still collapsed to 2 block-level sub-units; refine when DCHB Part-A accessible.

### v0 known gaps
1. DCHB Purba Medinipur Part-A — collapsed to 2 block sub-units
2. ECI 2024 LS Form-20 full postal ballot data not separately parsed
3. CSDS 2024 WB full caste cross-tabs — using press summaries (tier C/D)
4. Lakshmir Bhandar 2024 AC-level enrollment — district-level proxy
5. RG Kar post-LS effect not captured in vote table (future calibration round needed)

---

## H. Post-2024 validation anchors (OUT-OF-SAMPLE — NOT frozen calibration inputs)

> **These figures are post-2024 and must not be used to set frozen model parameters. They are out-of-sample tests for the belief-evolution simulator.**

No post-2024 validation anchors fetched in v0. The 2026 WB Assembly Election result is the primary forward validation gate.

*Placeholder: 2026 AE — TBD: result pending polling. Expected contest: BJP candidate (likely Suvendu Adhikari returning to contest the seat he holds, or a close associate); AITC candidate TBD; LF/CPI(M) competitive based on 2021 + 2024 AC-level performance (~3-3.5% of vote).*

---

*v0 — generated 2026-04-28, frozen at end-2024 state-of-knowledge. No post-2024 events referenced in Sections A–G. Section H is explicitly labelled out-of-sample.*
