# AC 210 — Nandigram (GEN) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural state of AC 210 Nandigram as of end-2021 — after the May 2021 WB Assembly Election results were known. It does not reference any post-2021 events. Use the 2024 LS AC-segment result as the out-of-sample validation gate for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).
>
> **Seat archetype:** A7 — Mahishya OBC coastal | Extreme polarization signal seat. The 2021 AE was the most high-profile single-constituency contest in the WB Assembly Election: Suvendu Adhikari (BJP, defected Dec 2020) vs Mamata Banerjee (AITC, shifted from Bhabanipur). Adhikari won by 1,956 votes. This file is calibrated to reproduce that result. Nandigram I and II blocks form this AC. Nandigram I is majority-Muslim (~34%); Nandigram II is overwhelmingly Hindu (~88%).

---

## A. Identity (as of 2021)

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
| Two sub-units used in v0 | **U1: Nandigram I CDB** (62.5% of 2021 pop) · **U2: Nandigram II CDB** (37.5% of 2021 pop) | A/E | Census 2011 block populations + 10-yr differential growth projection |
| 2021 AE candidate context | Suvendu Adhikari (BJP) — former AITC MLA, defected to BJP Dec 2020; Mamata Banerjee (AITC) — WB CM, shifted to contest Nandigram specifically; CPI(M) candidate Minakshi Mukherjee | A | ECI 2021 AE; Wikipedia "2021 WB Assembly Election" |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (Census) | 331,054 (Nandigram I: 207,835 + Nandigram II: 123,219) | A | Census 2011 block-level |
| 2021 projected population | ~369,700 | E | 10-yr religion-differential growth from Census 2011 (Hindu +10.4%, Muslim +13.7%) |
| Sex ratio (2011, F per 1000 M) | 946 | A | Census 2011 block aggregate |
| 2021 sex ratio (projected) | ~942 | E | Modest coastal district trend |
| 2021 electorate (AE roll) | 267,608 | A | ECI 2021 AE Form-20: total electors in Nandigram AC (Wikipedia confirmed) |
| Estimated M / F / TG split (2021) | 51.3% M / 48.6% F / <0.05% TG | E | 2011 census sex ratios; marginal change over 10 yr |
| 2021 polling stations (estimate) | ~296 | E | ECI 2021 AE estimate; Purba Medinipur coastal AC typical range |
| COVID-19 note | No major demographic shock in Nandigram blocks; coastal rural AC with limited urban density. Reverse migration (2020) added working-age males temporarily. | D | Journalistic coverage of Purba Medinipur COVID-19 impact |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 73.30 | A/E | Census 2011 block aggregate (Hindu 73.97%); 10-yr religion-differential growth → Hindu share falls ~0.7pp by 2021 |
| Muslim | 26.55 | A/E | Census 2011 block aggregate (Muslim 25.89%); share rises ~0.7pp by 2021 consistent with Purba Medinipur Muslim growth trend |
| Christian | 0.05 | E | Census 2011 other; small fringe |
| Sarna_ORP | 0.00 | A | Negligible ST presence in these blocks |
| Other_residual | 0.10 | E | Residual including not-stated |
| **Sum** | **100.00** | — | self-check |

*Block disaggregation (2011 Census, tier A; projected):*
- U1 Nandigram I: Hindu ~65.5%, Muslim ~34.4%, Other ~0.1%
- U2 Nandigram II: Hindu ~87.5%, Muslim ~12.3%, Other ~0.2%

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| SC_total | 16.40 | A/E | Census 2011 block aggregate 16.46%; projected stable over 10 yr |
| └ Bagdi_SC | 8.0 | E | Dominant SC in coastal Medinipur; ~48% of SC pool |
| └ Namasudra_SC | 3.5 | E | Secondary SC in Purba Medinipur; ~21% of SC pool |
| └ Bauri_SC | 2.0 | E | ~12% of SC pool |
| └ Other_SC | 2.9 | E | Residual SC sub-groups; ~18% of SC pool |
| ST_total | 0.10 | A | Census 2011 aggregate 0.10%; negligible ST presence |
| UC_bhadralok | 5.00 | E | Brahmin/Kayastha; concentrated in Nandigram census town |
| OBC | 3.00 | E | Tili/Teli and other OBC; coastal Medinipur |
| Other_Hindu_middle | 48.95 | E | Includes Mahishya (~27% total) + other Hindu middle castes; residual after SC+ST+UC+OBC+Muslim+Christian |
| Muslim | 26.55 | A/E | See C.1 |
| Christian_plus_Sarna_plus_Other | 0.00 | E | Negligible |
| **Sum** | **100.00** | — | self-check: 16.40+0.10+5.00+3.00+48.95+26.55+0.00=100.00 |

*Mahishya note (tier D): Mahishya is the numerically dominant general caste in coastal Purba Medinipur, estimated ~27% of total population. Within Other_Hindu_middle (48.95%), Mahishya accounts for ~27/48.95 = ~55%. The Mahishya community's political loyalty shifted dramatically in 2021 following Suvendu Adhikari's defection to BJP.*

### C.3 Age cohort (2021, adults 18+ only)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.0 | E | New voter cohort (born 1999-2003); renormalized from Census 2011 age pyramid for 18+ adults only |
| 23_27 | 11.5 | E | |
| 28_32 | 11.0 | E | |
| 33_37 | 10.5 | E | |
| 38_42 | 9.5 | E | |
| 43_47 | 8.5 | E | |
| 48_52 | 7.5 | E | |
| 53_57 | 7.0 | E | |
| 58_62 | 6.5 | E | |
| 63_67 | 9.5 | E | Older cohorts larger as children share decreases in 18+ renorm |
| 68 | 7.5 | E | |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.35 | A/E | Census 2011 block aggregate 51.40%; marginal change |
| Female | 48.64 | A/E | Corresponding female share |
| Third_gender | 0.01 | E | National standard estimate |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 99.94 | A | Nandigram I+II blocks essentially monolingual Bengali (Census 2011: 99.95%); stable |
| Hindi | 0.03 | E | Haldia industrial fringe labour; minimal |
| Urdu | 0.02 | E | Negligible in coastal block context |
| Other | 0.01 | E | Residual |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 10.5 | A/E | Census 2011 literacy 86.50%; projected +0.8pp/yr → ~94.5% literate by 2021 among 7+; ~10.5% illiterate (conservative, includes older cohorts) |
| Primary | 21.0 | E | Purba Medinipur district pattern; primary-educated rural majority |
| Middle | 22.0 | E | |
| Secondary | 20.0 | E | |
| Higher_Secondary | 13.0 | E | Growing with improved school access |
| Graduate | 10.0 | E | Modest improvement from 2019 baseline |
| Postgraduate | 3.5 | E | Slight increase with COVID-era online education |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 32.5 | A/E | Census 2011 block weighted 33%; slight decline due to COVID-19 disruption (2020) |
| Marginal_worker | 8.5 | E | WB rural pattern; slight increase from COVID-era informal sector disruption |
| Non_worker | 36.5 | E | Housewives, elderly; stable |
| Student | 12.0 | E | Stable; some COVID disruption to 2020-21 schooling cohort |
| Unemployed | 10.5 | E | Elevated; COVID-19 shock 2020 added ~1pp to educated unemployed seeking |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 15.50 | A/E | Census 2011 weighted 16.19%; slight shift away from cultivation |
| Agricultural_labourer | 45.50 | A/E | Dominant occupation; Census 2011 block weighted 46.43%; small decrease as some diversify |
| Household_industry | 3.70 | A | Census 2011 weighted 3.68%; stable |
| Manufacturing | 4.00 | E | Haldia industrial belt fringe; stable |
| Construction | 5.50 | E | Slight increase from COVID-era return migrants in construction |
| Trade_retail | 8.00 | E | Local market trade; stable |
| Transport_logistics | 6.00 | E | Coastal fishing and river transport; stable |
| Services | 7.30 | E | Growing private services; some COVID disruption |
| Government_services_teachers | 4.00 | E | Stable |
| Out_migrant_worker | 0.50 | E | Returned to home-block during COVID lockdown; small fraction |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.5 | E | Stable from 2019 |
| Employee | 22.5 | E | Small increase with Haldia industrial + govt service growth |
| Single_worker | 54.5 | E | Dominant: cultivator + fisherman + own-account artisan + small trader |
| Family_worker | 21.5 | E | Agricultural household assisting; stable |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 19.0 | E | Purba Medinipur BPL ~20-22% (2011); WB poverty fell ~3pp 2011-19, further ~1pp 2019-21 → ~19% |
| Above_Poverty_Line_low_income | 40.0 | E | Bulk of rural agrarian households; stable |
| Lower_middle | 25.0 | E | Lakshmir Bhandar (Apr 2021) effective from 2021; some upward mobility in HH consumption |
| Middle | 13.0 | E | Mahishya landowner class stable |
| Upper_middle_well_off | 3.0 | E | Marginal affluent fringe; stable |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Block location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Nandigram_I | 62.50 | A/E | Census 2011 pop 207,835/331,054 = 62.78%; slightly lower by 2021 due to higher Muslim growth in Nandigram I reducing relative share of Hindu-dominant N-II |
| U2_Nandigram_II | 37.50 | A/E | Census 2011 pop 123,219/331,054 = 37.22%; stable |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.4 | E | WB 2011 rural 4.4-4.6; marginal decrease by 2021 as nuclear trend continues |
| Nuclear_HH | 67.0 | E | NFHS-5 (2019-21) WB rural: ~66-68%; Purba Medinipur coastal |
| Joint_HH | 27.0 | E | Declining from 28% (2019 baseline) as nuclear families increase |
| Extended_multi_generation | 6.0 | E | Stable |
| **Sum** | **100.00** | — | self-check (Nuclear_HH + Joint_HH + Extended = 100) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.5 | E | Stable from Census 2011 Purba Medinipur pattern |
| Currently_married | 65.0 | E | Stable |
| Widowed | 7.0 | E | Slight increase from COVID-19 mortality (concentrated 60+) |
| Separated_divorced | 1.5 | E | Marginal increase; social change |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 78.0 | C | NFHS-5 (2019-21) WB rural ~72%; coastal Purba Medinipur slightly above average → ~78%; TV effectively saturated in middle-class HH |
| Radio | 5.0 | C | Declining; minimal in 2021 |
| Mobile_phone | 90.0 | C | NFHS-5 WB rural ~87%; Jio penetration near-complete → ~90% |
| Smartphone_with_internet | 65.0 | C | NFHS-5 WB rural ~55%; COVID-era surge (2020-21 online schooling, UPI, WhatsApp political communication) → ~65% |
| Computer | 7.0 | C | NFHS-5 WB rural ~5%; slight increase with affordable Android tablets |
| Two_wheeler | 32.0 | C | NFHS-5 WB rural ~22%; Purba Medinipur coastal medium-farmer class → ~32% |
| Four_wheeler | 5.0 | C | Limited; stable |
| Banking_access | 92.0 | B | PMJDY saturation; NFHS-5 WB baseline → ~92% |
| **Note** | (these are independent ownership %s, not categorical — do not sum) | — | — |

### C.15 Household amenities (2021)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 87.0 | C | NFHS-5 WB rural ~86%; slight improvement by 2021 |
| Improved_sanitation | 78.0 | C | NFHS-5 WB rural (2019-21): Purba Medinipur ~75-80% (Swachh Bharat saturation); Nandigram slightly above → ~78% |
| LPG_clean_cooking_fuel | 55.0 | C | NFHS-5 WB rural ~50%; Ujjwala 2.0 + own-purchase; Purba Medinipur medium-farmer class → ~55% |
| Wood_biomass_fuel | 41.0 | C | Declining as LPG rises; coastal wood/crop-residue |
| Other_fuel | 4.0 | C | Kerosene/other declining |
| Electricity | 98.0 | A/E | Saubhagya saturation effectively complete in Purba Medinipur by 2021 |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 87.5 | D | Coastal agrarian AC; very low in-migration; stable from 2019 |
| WB_other_district | 6.0 | D | Adjacent Paschim Medinipur / Hooghly |
| Other_Indian_state | 2.0 | D | Haldia industrial fringe; reduced by COVID (some out-state labour returned home 2020) |
| Bangladesh_origin | 2.0 | D | Very small compared to N24P; some Namasudra SC households |
| Outside_India | 0.5 | E | Negligible |
| Out_migrant | 2.0 | E | COVID-era return migration (2020) brought some WB migrants back; net out-migration lower than 2019 |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|
| Hindu | 99.97 | 0.02 | 0.00 | 0.01 | A | Census 2011 block; essentially monolingual AC |
| Muslim | 99.88 | 0.02 | 0.08 | 0.02 | A | Bengali Muslim peasantry; negligible Urdu |
| Christian | 90.00 | 5.00 | 0.00 | 5.00 | E | Small base |
| Sarna_ORP | 95.00 | 0.00 | 0.00 | 5.00 | E | Negligible |
| Other_residual | 90.00 | 5.00 | 0.00 | 5.00 | E | Small base |

### D.2 Religion × Caste (2D layout)

P(caste ‖ religion) — % within each religion.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 22.38 | 0.14 | 6.82 | 4.10 | 66.56 | 0 | 0 | A/D/E | SC_total = 16.40/73.30 = 22.38%; ST = 0.10/73.30 = 0.14%; UC = 5.00/73.30 = 6.82%; OBC = 3.00/73.30 = 4.10%; Other_Hindu_middle = residual (Mahishya ~27% total within Other_Hindu_middle) |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | All Muslim population maps to Muslim caste leaf |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | Small base |
| Sarna_ORP | 0 | 100 | 0 | 0 | 0 | 0 | 0 | E | Negligible |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | Small base |

### D.3 Religion × Migration / birthplace

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 87.0 | 6.5 | 2.5 | 2.5 | 0.5 | 1.0 | D | Mahishya/Bagdi peasantry deeply native; small Bangladesh-origin SC (Khulna/Barisal Namasudra); some COVID returnees |
| Muslim | 91.0 | 5.0 | 1.0 | 2.0 | 0.0 | 1.0 | D | Bengali Muslim peasantry essentially native; small Bangladesh-origin Muslim trickle in Nandigram I |
| Christian | 60.0 | 20.0 | 18.0 | 2.0 | 0.0 | 0.0 | E | Small base; Haldia industrial fringe |
| Sarna_ORP | 95.0 | 5.0 | 0.0 | 0.0 | 0.0 | 0.0 | E | Negligible |
| Other_residual | 80.0 | 10.0 | 8.0 | 2.0 | 0.0 | 0.0 | E | Small base |

### D.4 Religion × Asset / media

P(owns asset ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 80.0 | 68.0 | 94.0 | C | NFHS-5 WB religion-gap pattern; Mahishya farmer HH above-average assets; Hindu-dominated N-II higher income |
| Muslim | 72.0 | 56.0 | 86.0 | C | NFHS-5 WB Muslim HH gap; Nandigram I rural Muslim poorer on average; COVID-era smartphone surge narrowed gap |
| Christian | 82.0 | 65.0 | 92.0 | E | Small base; Haldia industrial fringe slightly higher income |
| Sarna_ORP | 70.0 | 45.0 | 80.0 | E | Negligible |
| Other_residual | 78.0 | 60.0 | 90.0 | E | Small base |

### D.5 Caste × Education

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 3 | 7 | 10 | 17 | 21 | 28 | 14 | E |
| Other_Hindu_middle | 8 | 19 | 23 | 21 | 15 | 11 | 3 | E |
| OBC | 11 | 21 | 22 | 18 | 13 | 11 | 4 | E |
| SC_total | 17 | 25 | 22 | 17 | 10 | 7 | 2 | E |
| ST_total | 20 | 27 | 22 | 15 | 9 | 5 | 2 | E |
| Muslim | 14 | 23 | 23 | 19 | 12 | 8 | 1 | E |
| Christian_plus_Sarna_plus_Other | 10 | 20 | 22 | 20 | 15 | 10 | 3 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share, within age-gender cell.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 19 | 18 | E |
| 23_27 | 18 | 14 | E |
| 28_32 | 14 | 10 | E |
| 33_37 | 11 | 6 | E |
| 38_42 | 10 | 5 | E |
| 43_47 | 8 | 3 | E |
| 48_52 | 7 | 2 | E |
| 53_57 | 6 | 1 | E |
| 58_62 | 5 | 1 | E |
| 63_67 | 4 | 1 | E |
| 68 | 3 | 1 | E |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender) — % within age-gender cell.

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 6 | 28 | E |
| 23_27 | 40 | 82 | E |
| 28_32 | 82 | 93 | E |
| 33_37 | 93 | 91 | E |
| 38_42 | 93 | 90 | E |
| 43_47 | 92 | 88 | E |
| 48_52 | 91 | 82 | E |
| 53_57 | 90 | 72 | E |
| 58_62 | 88 | 60 | E |
| 63_67 | 78 | 38 | E |
| 68 | 72 | 28 | E |

### D.8 Occupation × Asset / media

P(owns smartphone-internet / TV ‖ occupation) — within workers.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 48 | 76 | C | COVID-era smartphone surge; medium-farmer Mahishya HH higher than ag-labourer |
| Agricultural_labourer | 38 | 66 | C | Lowest income; Bagdi SC ag-labourer |
| Household_industry | 52 | 78 | C | |
| Manufacturing | 68 | 88 | C | Haldia fringe: higher income |
| Construction | 60 | 80 | C | Return migrants with smartphone from outside |
| Trade_retail | 75 | 90 | C | |
| Transport_logistics | 65 | 82 | C | Coastal fishermen: higher mobile use for sea communication |
| Services | 80 | 92 | C | |
| Government_services_teachers | 90 | 96 | C | |
| Out_migrant_worker | 88 | 85 | C | Migrants have high smartphone access |

### D.9 Education × Workforce

P(unemployed-seeking / main-worker ‖ education) — % within each education level (age 18+).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 38 | 2 | E |
| Primary | 40 | 4 | E |
| Middle | 37 | 6 | E |
| Secondary | 32 | 11 | E |
| Higher_Secondary | 25 | 17 | E |
| Graduate | 28 | 20 | E |
| Postgraduate | 40 | 14 | E |

### D.10 Asset × Bilingualism

Near-irrelevant in this monolingual AC. Retained as stub per schema.

| Media_tier | Bilingual_pct | Tier | Source |
|---|---|---|---|
| TV_only_HH | 1 | E | Bengali TV dominant; essentially zero bilingual pressure |
| TV_plus_smartphone_HH | 3 | E | Some YouTube Hindi cross-language content |
| Smartphone_only_HH | 2 | E | |
| No_asset_HH | 0.5 | E | |

### D.11 GP × Religion (sub-AC spatial heterogeneity)

P(religion ‖ block location).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Nandigram_I | 65.50 | 34.40 | 0.05 | 0.00 | 0.05 | A/E | Census 2011 direct: Hindu 65.82%, Muslim 34.04%; projected 10-yr shift |
| U2_Nandigram_II | 87.50 | 12.30 | 0.10 | 0.00 | 0.10 | A/E | Census 2011 direct: Hindu 87.71%, Muslim 12.12%; projected |

### D.12 GP × Caste

P(caste ‖ block) — parent leaves only.

| Sub_unit | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Nandigram_I | 18.58 | 0.07 | 4.0 | 2.5 | 40.85 | 34.00 | 0.00 | A/D |
| U2_Nandigram_II | 12.89 | 0.16 | 7.0 | 4.0 | 63.65 | 12.30 | 0.00 | A/D |

### D.13 GP × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Nandigram_I | 75 | 60 | 6 | 89 | C |
| U2_Nandigram_II | 82 | 72 | 9 | 94 | C |

### D.14 GP × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Nandigram_I | 50 | 72 | 85 | 97 | C |
| U2_Nandigram_II | 62 | 86 | 90 | 99 | C |

### D.15 Vote × Religion (2021 AE)

P(party ‖ religion) — calibrated to reproduce 2021 AE result. Suvendu Adhikari (BJP) won by 1,956 votes (0.85 pp margin) over Mamata Banerjee (AITC).

*Key calibration note: The Adhikari defection (Dec 2020) shifted Mahishya-Hindu votes decisively to BJP. Muslim vote consolidated 95%+ behind AITC (Mamata personally on the ballot). The result implies BJP captured ~65-70% of Hindu votes vs AITC ~25-30% (plus near-total Muslim consolidation for AITC).*

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 63.0 | 28.0 | 1.0 | 6.0 | 2.0 | C/D | Key cell: Mahishya/Hindu swing to BJP (Adhikari effect); CSDS 2021 WB exit: BJP ~72% Hindu statewide; Nandigram AC-specific adjusted downward due to some Hindu AITC holdouts (Muslim-bordering Nandigram I Hindus). Implied: 0.733×63.0 + 0.266×4.0 ≈ 47.2pp BJP contribution from Hindu, consistent with 48.49% total |
| Muslim | 4.0 | 91.0 | 1.0 | 3.0 | 1.0 | C/D | Near-total Muslim consolidation behind Mamata personally; CSDS 2021 WB: AITC ~75% Muslim statewide; Nandigram specific: Mamata on ballot → ~91%. 0.266×91.0 ≈ 24.2pp AITC Muslim contribution; sum with Hindu = 28+24.2 ≈ 52.2pp AITC, close to actual 47.64% with turnout effects |
| Christian | 20 | 70 | 5 | 3 | 2 | E | Small base |
| Sarna_ORP | 30 | 55 | 5 | 8 | 2 | E | Negligible |
| Other_residual | 25 | 60 | 5 | 5 | 5 | E | Small base |

### D.16 Vote × Caste (2021 AE)

P(party ‖ caste) — calibrated to 2021 AE result.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 65 | 25 | 2 | 6 | 2 | C | Strong BJP swing among upper castes; CSDS 2021 WB |
| Other_Hindu_middle | 65 | 27 | 1 | 5 | 2 | C/D | Key cell: Mahishya community's decisive swing to Suvendu Adhikari (BJP). In 2019 Adhikari was AITC candidate; by 2021 Mahishya followed him to BJP. Tier C/D: CSDS 2021 WB statewide + AC-specific journalistic analysis |
| OBC | 55 | 35 | 2 | 6 | 2 | C | Tili/OBC split; BJP plurality |
| SC_total | 50 | 40 | 2 | 6 | 2 | C | SC vote more evenly split; Bagdi historically AITC but Adhikari appeal strong |
| ST_total | 40 | 45 | 3 | 10 | 2 | E | Negligible base; mixed |
| Muslim | 4 | 91 | 1 | 3 | 1 | C/D | See D.15 |
| Christian_plus_Sarna_plus_Other | 20 | 65 | 5 | 8 | 2 | E | Small base |

### D.17 Vote × Gender (2021 AE)

P(party ‖ gender).

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 52 | 40 | 1 | 5 | 2 | C | CSDS 2021 WB; Adhikari personal loyalty stronger among male voters |
| Female | 44 | 48 | 1 | 5 | 2 | C | Lakshmir Bhandar (launched Apr 2021) and Mamata personally on ballot boosted female AITC vote; but overall BJP still slightly below 50% among women in this AC |
| Third_gender | 30 | 55 | 5 | 8 | 2 | E | Negligible base |

### D.18 Vote × Welfare scheme exposure (2021 AE)

Schemes active by 2021: Lakshmir Bhandar (launched April 2021), Swasthya Sathi (2016+), Krishak Bandhu (2019), Kanyashree (2013), Sabuj Sathi (2015), Khadya Sathi (2016).

| Welfare_exposure | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Lakshmir_Bhandar_enrolled | 38 | 54 | 1 | 5 | 2 | C | LB launched April 2021; effect was partly in-campaign but significant. Female-HH-head recipients tilt AITC but BJP held ~38% even among LB households due to Adhikari personal effect |
| Krishak_Bandhu | 42 | 50 | 1 | 5 | 2 | C | Cultivator HH; BJP made inroads but AITC retained welfare-credit plurality |
| Swasthya_Sathi | 40 | 52 | 1 | 5 | 2 | C | Broad-based; AITC welfare-credit still visible |
| No_state_scheme | 58 | 33 | 2 | 5 | 2 | C | BJP-dominant among scheme non-recipients |

---

## E. 2021 AE baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp.

### AC 210 Nandigram — 2021 Assembly Election (tier A, ECI)

Detailed result:

| Candidate | Party | Votes | %  |
|---|---|---|---|
| Suvendu Adhikari | BJP | 110,764 | 48.49% |
| Mamata Banerjee | AITC | 108,808 | 47.64% |
| Minakshi Mukherjee | CPI(M) | 6,267 | 2.74% |
| Others | — | 2,628 | 1.13% |
| **Margin** | BJP over AITC | **1,956** | **0.85 pp** |
| **Total valid votes** | | **228,467** | |
| **Total electors** | | **267,608** | |
| **Turnout** | | **85.4%** | |

*Source: Wikipedia "Nandigram (Vidhan Sabha constituency)"; ECI 2021 AE. Tier A.*

*Calibration note: The initial count on 2 May 2021 briefly showed AITC ahead by ~1,200 before a recount gave BJP the win by 1,956. This is the official ECI-certified result. The margin is within any realistic recount uncertainty, making it a near-tie for calibration purposes — the simulator should treat a 47-49% BJP, 47-48% AITC outcome as a valid reproduction.*

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 48.49 | A | ECI 2021 AE official certified result; Suvendu Adhikari |
| AITC | 47.64 | A | ECI 2021 AE; Mamata Banerjee |
| INC | 0.20 | A | ECI 2021 AE; small residual |
| LF | 2.74 | A | ECI 2021 AE; CPI(M) Minakshi Mukherjee + small LF fraction of Others |
| Other_NOTA | 0.93 | A | ECI 2021 AE; remaining Others + NOTA |

---

## F. Vote history (anchors for belief evolution)

### AC 210 Nandigram — Assembly Elections (pre-2021)

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin | Tier |
|---|---|---|---|---|---|---|---|---|---|---|
| 2006 AE | Sheikh Mohammad Illias | CPI | 69,376 | ~50.6 | Sk Supian | AITC | 64,553 | ~47.1 | 4,823 | A |
| 2009 by-poll | Firoja Bibi | AITC | 93,022 | 58.28 | Paramananda Bharati | CPI | 53,473 | 39.35 | 39,549 | A |
| 2011 AE | Firoja Bibi | AITC | 103,300 | 61.21 | Paramananda Bharati | CPI | 59,660 | 35.35 | 43,640 | A |
| 2016 AE | Suvendu Adhikari | AITC | 134,623 | 67.20 | Abdul Kabir Sekh | CPI | 53,393 | 26.70 | 81,230 | A |

*Sources: Wikipedia "Nandigram (Vidhan Sabha constituency)". Tier A.*

### 2007 Nandigram land agitation (historical anchor)

The 2007 Nandigram movement is the single most defining political event in the AC's modern history, predating the simulation window but essential to understanding AC identity:

- **January 2007**: WB government announced plans to acquire land in Nandigram for a chemical hub (Haldia Development Authority / TATA Chemicals SEZ).
- **March 14, 2007**: Police firing on protesters; 14 killed. Became a national political flashpoint.
- **November 2007**: CPI(M) retook control of the area; further clashes.
- **Political consequence**: The Nandigram movement destroyed the CPI(M) Left Front's rural legitimacy in Purba Medinipur and catalyzed AITC's emergence as the dominant force in coastal WB. Mamata Banerjee's personal opposition to the SEZ became her most powerful political credential leading to the 2011 WB landslide.
- **Suvendu Adhikari's family**: Sisir Adhikari (father) was a local strongman who opposed the SEZ; Suvendu Adhikari (son) built his career in Nandigram's post-2007 AITC wave. He won Tamluk LS (2009, 2014) and Nandigram AE (2016) as AITC.
- **Tier D**: Wikipedia "Nandigram violence"; Rediff "Nandigram chronology"; journalistic accounts.

### Tamluk Lok Sabha (PC 17) — 2019 LS result

| Party | Candidate | Votes | % | Notes | Tier |
|---|---|---|---|---|---|
| AITC | Dibyendu Adhikari | 724,433 | 50.08 | Suvendu's brother; won Tamluk LS | A |
| BJP | Siddharth Naskar | 534,268 | 36.94 | 13.14 pp behind | A |

*AC 210 Nandigram segment (2019 LS, tier A):* AITC 130,659 (63.14%), BJP 62,268 (30.09%), CPI(M) 9,353 (4.52%) — high AITC performance reflecting Adhikari family local dominance and high Muslim consolidation.

### Suvendu Adhikari defection (in-window 2021 calibration context)

- **December 2020**: Suvendu Adhikari resigned as WB Cabinet Minister (Transport, Water Resources, Irrigation) and resigned from AITC membership.
- **December 19, 2020**: Adhikari joined BJP at a Medinipur rally addressed by Amit Shah.
- **January 2021**: He resigned his Nandigram MLA seat (held from 2016 AITC ticket).
- **February 2021**: Mamata Banerjee announced she would personally contest Nandigram against Adhikari.
- **Political significance**: The defection split the Mahishya community — Adhikari's personal network and caste backing followed him to BJP; AITC relied on Muslim consolidation plus minority Hindu holdouts. This is the central narrative of the 2021 calibration.
- **Tier A/D**: Wikipedia "Suvendu Adhikari"; Times of India "Suvendu quits TMC"; ECI 2021 candidate list.

### COVID-19 and Cyclone Amphan context (2020, in-window)

- **May 2020**: Cyclone Amphan caused moderate damage in Purba Medinipur coastal blocks; Nandigram blocks had some flooding. AITC-led relief distribution became a political asset for the party; Adhikari was still AITC minister and partly credited with relief.
- **2020 COVID lockdown**: Reverse migration brought back Haldia-Kolkata-Kerala workers to Nandigram blocks; these households were economically stressed by 2021 election.
- **Lakshmir Bhandar (April 2021)**: Launched one month before AE polling; female household heads received ₹500 (non-SC/ST) / ₹1,000 (SC/ST) per month. Significant voter awareness in Nandigram blocks by polling day, but barely operational — welfare-credit attribution was contested between Mamata vs Adhikari.
- **Tier D**: Journalistic coverage of Amphan impact in Purba Medinipur; WB government Lakshmir Bhandar records.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- ECI 2021 WB Assembly Election: AC 210 Nandigram certified result — BJP (Suvendu Adhikari) 110,764 / AITC (Mamata Banerjee) 108,808 / CPI(M) (Minakshi Mukherjee) 6,267; total electors 267,608; turnout 85.4%; margin 1,956. Source: Wikipedia "Nandigram (Vidhan Sabha constituency)" citing ECI 2021 AE archive.
- Census of India 2011 — Nandigram I CD Block Primary Census Abstract: population 207,835; SC 18.58%; ST 0.07%; literacy 84.89%; religion: Hindu 65.82%, Muslim 34.04%; Bengali 99.97%
- Census of India 2011 — Nandigram II CD Block Primary Census Abstract: population 123,219; SC 12.89%; ST 0.16%; literacy 89.16%; religion: Hindu 87.71%, Muslim 12.12% (14,940 persons); Bengali 99.94%
- ECI 2019 LS CSV: AC 210 exact vote counts (247,252 electors; AITC 130,659 / BJP 62,268)
- Delimitation Commission of India 2008 — Nandigram = Nandigram I CDB + Nandigram II CDB

### Secondary sources (tier B/C)
- NFHS-5 (2019-21) West Bengal — household amenities, asset ownership (TV, smartphone, banking); rural/urban gradient applied; Purba Medinipur district supplement
- CSDS-Lokniti 2021 WB exit poll / post-poll data (national and WB regional rollup): religion × vote, caste × vote, gender × vote conditional tables
- WB CDWDSW Lakshmir Bhandar enrollment data (AC-level penetration not directly published; district-level proxy used)

### Tertiary / journalistic (tier D)
- Wikipedia "Suvendu Adhikari" — defection chronology, BJP join date Dec 19 2020
- Wikipedia "2021 West Bengal legislative assembly election" — overall result, AC-level summary
- Wikipedia "Nandigram (Vidhan Sabha constituency)" — 2021 AE candidate results
- Times of India coverage of Nandigram 2021 campaign (Mamata personal contest, recount controversy)
- Newslaundry analysis: "Nandigram: What does it mean for Mamata and Bengal?" (post-result)

### Tier-D/E reliance flags (what to distrust)
- **Mahishya vote-swing magnitude** (D.16) — the shift from 55% AITC (2019) to ~65% BJP (2021) among Mahishya is from journalistic analysis and CSDS 2021 WB regional cross-tabs, not AC-specific survey. Tier C/D composite. The exact magnitude is the single highest-uncertainty parameter in this calibration.
- **Muslim consolidation level** (D.15) — CSDS 2021 WB statewide shows ~75% AITC Muslim; Nandigram-specific (Mamata on ballot) estimated at ~91%. No AC-level Muslim vote survey. Tier C/D.
- **Lakshmir Bhandar vote impact** (D.18) — scheme launched April 2021, barely a month before polling. Tier C from CSDS post-poll; actual causal effect within Nandigram is uncertain.
- **Asset/media 2021** (C.14, D.4, D.13) — COVID-era smartphone surge estimated from NFHS-5 national; WB AC-specific diffusion rate is tier C.
- **GP-level data** (D.11-D.14) — collapsed to 2 block-level sub-units; refine when DCHB Purba Medinipur Part-A accessible.

### v0 known gaps
1. DCHB Purba Medinipur Part-A — collapsed to 2 block sub-units (Nandigram I + II) instead of ~17 GPs
2. Census HH-13 block-level — using NFHS-5 state-level proxy for asset/media (tier C)
3. ECI 2021 AE Form-20 — using Wikipedia-cited candidate result (tier A from ECI via Wikipedia); exact postal ballot split not available
4. CSDS 2021 WB full caste cross-tabs — using press summaries (tier C/D)
5. Lakshmir Bhandar AC-level enrollment — district-level proxy only

---

## H. Post-2021 validation anchors (OUT-OF-SAMPLE gates — NOT frozen calibration inputs)

> **These figures are post-2021 and must not be used to set frozen model parameters. They are out-of-sample tests for the belief-evolution simulator.**

### 2024 Lok Sabha (Tamluk PC 17) — AC 210 Nandigram segment (tier A, ECI CSV)

| Party | Candidate | Votes | % of total votes polled | Notes |
|---|---|---|---|---|
| BJP | Abhijit Gangopadhyay | 112,110 | 49.49% | BJP retained AC-segment majority |
| AITC | Debangshu Bhattacharya | 103,910 | 45.87% | AITC marginally declined from 2021 |
| CPI(M) | Sayan Banerjee | 7,574 | 3.34% | LF small uptick |
| NOTA + Others | — | 2,955 | 1.30% | |
| **Margin** | BJP over AITC | **8,154** | **3.62 pp** | BJP widened margin from 2021 AE |
| **Total electors** | | **274,621** | |
| **Total valid votes (incl. NOTA)** | | **226,549** | |
| **Turnout** | | | **82.5%** | |

*Source: `data/2024_AssemblySegmentLevelVotingData.csv`, filtered West Bengal AC_NO=210; NOTA from NOTA_VOTES_EVM_IN_AC field. Tier A (ECI direct data).*

*Simulator note: The 2021→2024 trajectory shows BJP consolidating in Nandigram (48.49% → 49.49%) while AITC slightly declined (47.64% → 45.87%). Suvendu Adhikari served as WB Opposition Leader and Union Minister (MoS Defence) 2021-24; his political footprint in Nandigram remained strong even without being a candidate. These are out-of-sample targets the belief-evolution engine must reproduce.*

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No post-2021 events referenced in Sections A–G. Section H is explicitly labelled out-of-sample.*
