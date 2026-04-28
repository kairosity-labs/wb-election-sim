# AC 016 — Maynaguri (SC) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 016 Maynaguri as of end-2021 only — it does not reference any
> post-2021 events. Use post-2021 outcomes as out-of-sample validation gates
> for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 016 | A | ECI / Delimitation Commission 2008 |
| AC name | Maynaguri | A | ECI |
| Reservation | SC | A | Delimitation 2008 |
| District | Jalpaiguri | A | Delimitation 2008 |
| Sub-division | Maynaguri | A | WB administrative |
| LS constituency | 3 — Jalpaiguri (SC reserved) | A | Delimitation 2008 |
| LS segments included with AC 016 | AC 13 Mekliganj · 14 Dhupguri · 15 Phalakata · 16 Maynaguri · 17 Mal · 18 Nagrakata · 19 Jalpaiguri | A | Delimitation 2008 |
| AC composition | Mainaguri census town + Maynaguri community development block (rural GPs) | A | Delimitation 2008 |
| Geographic note | Northern Jalpaiguri district, terai-foothills transition zone; borders Dhupguri block to west and Rajganj block to east | A | — |
| Sub-units used in v0 | **U1: Mainaguri_town** (census town / proto-urban) · **U2: Maynaguri_CDB_rural** (rural GPs of CDB Maynaguri) | E | v0 simplification |

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~337,251 (Maynaguri CDB total; Census 2011 PCA; ~30,490 in Mainaguri census town) | A | Census 2011 Maynaguri Block PCA; wb_ac_master_v3.csv |
| 2021 projected population | ~378,000 | E | 10-yr compound growth ~1.15%/yr from 2011 base (Jalpaiguri district trend) |
| Sex ratio (2021, F per 1000 M) | ~945 | E | Block 2011: 935; NFHS-5 Jalpaiguri: 1,038 — convergence trend; mid-point ~945 for 2021 |
| 2021 estimated electorate (18+) | 264,265 | A | ECI 2021 AE roll — AC 016 total electors; wb_ac_master_v3.csv |
| Estimated M / F / TG split (2021) | 51.3% M / 48.7% F / <0.05% TG | E | Block sex ratio 945 → projection; TG from WB SIR pattern |
| 2021 polling stations (estimated) | ~295 | E | Back-derived from electorate growth 2016→2021 (236,663→264,265); +~10 stations |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 90.00 | A | Maynaguri CDB 2011: 90.02%; 10-yr differential growth (Hindu ~1.1%/yr, Muslim ~1.3%/yr) → slight convergence; ~89.95% rounded to 90.00% |
| Muslim | 9.75 | A | Maynaguri CDB 2011: 9.79%; slight relative gain vs 2019 as Muslim growth marginally faster; +0.2pp from 2019 |
| Christian | 0.06 | E | CDB 2011: 0.03%; continued small upward trend to 2021 |
| Sarna_ORP | 0.10 | E | Tribal religion; ST population 1.33% with fraction Sarna; stable |
| Other_residual | 0.09 | E | Sikh + Jain + Buddhist + Not_stated, lumped; slight compression |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 70.97 | A | Census 2011 Maynaguri Block: SC 239,342/337,251 = 70.97% — direct Census figure; stable to 2021 |
| └ Rajbanshi_SC | 64.50 | C | Rajbanshi dominant SC in northern Jalpaiguri; ~91% of SC pool; slight downward adjustment for inter-SC demographic mix |
| └ Other_SC | 6.47 | E | Residual SC sub-castes (Namasudra, Bagdi, etc.) |
| **ST_total** | 1.33 | A | Census 2011: ST 4,492/337,251 = 1.33% — direct Census figure; stable |
| └ Other_ST | 1.33 | E | Small adivasi pockets; Boro/Rabha community traces |
| UC_bhadralok | 3.00 | E | Low bhadralok presence; SC-dominant AC; Brahmin/Kayastha/Baidya minimal; unchanged from 2019 |
| OBC | 4.00 | E | OBC Hindus including Kurmi, Mahishya fringe; Jalpaiguri district pattern |
| Other_Hindu_middle | 10.70 | E | Residual within Hindu (90.00 − 70.97 SC − 1.33 ST − 3.0 UC − 4.0 OBC = 10.70; residual Hindu middle) |
| Muslim | 9.75 | E | See C.1 |
| Christian_plus_Sarna_plus_Other | 0.25 | E | Sarna_ORP + Christian + Other_residual combined |
| **Sum** | **100.00** | — | self-check (70.97+1.33+3.00+4.00+10.70+9.75+0.25=100.00 ✓) |

### C.3 Age cohort (2021, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.20 | E | Jalpaiguri district 2011 age pyramid; 2-yr shift of 2019 cohorts; renormalised to 18+ adults; NFHS-5 Jalpaiguri under-15 = 22.6% |
| 23_27 | 11.50 | E | |
| 28_32 | 11.70 | E | 2019 18-22 cohort aged up |
| 33_37 | 11.20 | E | |
| 38_42 | 10.50 | E | |
| 43_47 | 9.70 | E | |
| 48_52 | 8.90 | E | |
| 53_57 | 7.60 | E | |
| 58_62 | 6.50 | E | |
| 63_67 | 5.30 | E | |
| 68 | 5.90 | E | 68+ open-ended; slight compression as older survivors diminish |
| **Sum** | **100.00** | — | self-check (renormalised from Census 2011 age pyramid excluding 0–17) |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.38 | E | Sex ratio 945 (F per 1000 M) → 945/1945 = 48.59% F → 51.41% M; slight improvement from 2019 (935); rounded |
| Female | 48.61 | E | Complement |
| Third_gender | 0.01 | E | WB SIR pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 84.04 | A | Maynaguri Block 2011: 84.26%; slight compression as Rajbongshi-speaking Rajbanshi community grows; -0.2pp |
| Hindi | 0.80 | E | Small trader/migrant Hindi-speaking minority; stable |
| Urdu | 0.52 | E | Muslim population Bengali-dominant; tiny Urdu fringe; marginal increase with Muslim share |
| Other | 2.12 | E | Residual catch-all (Nepali, Sadri fringe not listed) |
| Rajbongshi | 5.20 | A | Maynaguri Block 2011: 5.08%; Rajbanshi SC growth trajectory; +0.12pp |
| Sadri | 1.02 | A | Maynaguri Block 2011: 1.02%; tea garden worker language; stable |
| Nepali | 6.30 | E | Nepali-speaking community in terai zone; slight growth from natural increase |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 21.00 | E | Maynaguri Block 2011 literacy 75.42%; NFHS-5 Jalpaiguri female literacy 73.6%; +2pp/yr improvement trend → ~21% illiterate by 2021 |
| Primary | 25.50 | E | Education distribution scaled; primary share contracting as middle/secondary expands |
| Middle | 21.50 | E | |
| Secondary | 16.00 | E | Modest gains from mid-day meal + SC incentive programmes |
| Higher_Secondary | 9.00 | E | |
| Graduate | 5.50 | E | Slight improvement; SC quota graduates increasing |
| Postgraduate | 1.50 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 35.50 | E | COVID-19 disruption (Mar-Aug 2020) suppressed formal employment; slight recovery by end-2021; vs 2019 ~36% |
| Marginal_worker | 13.50 | E | Seasonal agricultural marginal workers; slight increase post-COVID return migration |
| Non_worker | 37.00 | E | Housewives + elderly + retired; stable |
| Student | 8.00 | E | 18–22 in education; stable despite school disruption (COVID schooling gap) |
| Unemployed | 6.00 | E | Educated job-seekers; rural economy remained depressed through 2021 |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 28.00 | E | Stable; COVID disruption minimal in agriculture |
| Agricultural_labourer | 33.00 | E | Slight increase; COVID return migration added agrarian labour supply |
| Household_industry | 5.00 | E | Bidi-rolling, weaving; stable |
| Manufacturing | 2.50 | E | COVID disruption hit organised manufacturing; slight fall from 2019 |
| Construction | 5.50 | E | Disrupted by COVID lockdown; partial recovery by end-2021 |
| Trade_retail | 10.00 | E | Mainaguri town retail; resilient |
| Transport_logistics | 4.00 | E | NH-27 corridor; recovery by 2021 |
| Services | 7.00 | E | Stable |
| Government_services_teachers | 3.00 | E | SC-reserved positions; stable |
| Out_migrant_worker | 2.00 | D | COVID return-migration partially reversed by end-2021; net stable |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Census B-04 WB rural pattern; stable |
| Employee | 21.50 | E | Slight fall from COVID disruption in organised employment |
| Single_worker | 48.50 | E | Own-account cultivators + petty traders; slightly higher post-COVID |
| Family_worker | 28.50 | E | High unpaid family worker share; stable |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 27.00 | D | Jalpaiguri rural BPL ~28% at 2019; COVID reverse migration slightly worsened near-BPL; SC-dominated AC; slight improvement from Lakshmir Bhandar (Apr 2021) and welfare stack |
| Above_Poverty_Line_low_income | 37.00 | E | Near-poor agrarian households; stable |
| Lower_middle | 22.50 | E | |
| Middle | 11.00 | E | Mainaguri town / government employee households; stable |
| Upper_middle_well_off | 2.50 | E | Very limited affluent class; marginal growth |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Mainaguri_town | 9.00 | E | Mainaguri census town ~30,490 pop (2011); minor growth to 2021; ~34,000 → 34,000/378,000 ≈ 9.0%; slight urban proportion fall as rural grows faster |
| U2_Maynaguri_CDB_rural | 91.00 | E | Remainder: rural GPs of Maynaguri CDB; dominant share |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | WB 2011: 4.3 state average; Jalpaiguri rural slightly higher; marginal decline toward 4.5 by 2021 |
| Nuclear_HH | 66.00 | E | NFHS-5 WB rural pattern; slight increase in nuclear households |
| Joint_HH | 27.00 | E | Slight decline; COVID-era household restructuring |
| Extended_multi_generation | 7.00 | E | Stable |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.00 | E | Stable from 2019; rural SC community |
| Currently_married | 66.00 | E | High marriage rate in rural SC communities |
| Widowed | 7.50 | E | COVID-19 excess mortality slightly elevated widowed share; concentrated in 60+ cohort |
| Separated_divorced | 1.50 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 70.00 | C | NFHS-5 Jalpaiguri implied ~70% (extrapolated from NFHS-4 WB rural 60% + upward trend; TV penetration plateauing); stable relative to 2019 |
| Radio | 7.00 | C | Declining; slightly lower than 2019 (8%) |
| Mobile_phone | 87.00 | C | COVID surge in mobile usage; further Jio penetration 2020-21; +5pp from 2019 |
| Smartphone_with_internet | 58.00 | C | COVID-era smartphone surge (+20pp from 2019's 38%); WhatsApp/YouTube primary news vector in rural North Bengal by 2021 |
| Computer | 4.00 | C | Unchanged; rural SC-dominant AC |
| Two_wheeler | 24.00 | C | Modest growth; +2pp from 2019 |
| Four_wheeler | 3.00 | E | Minimal; stable |
| Banking_access | 91.00 | B | PMJDY + Jan Dhan saturation; Lakshmir Bhandar (Apr 2021) required bank account → further push; +6pp from 2019; NFHS-5 Jalpaiguri banking gains pattern |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 93.00 | C | NFHS-5 Jalpaiguri: 95.2% (2019-21 survey); AC-level slightly lower than district; ~93% for rural-dominant AC |
| Improved_sanitation | 68.00 | C | NFHS-5 Jalpaiguri: 73.2%; AC-level rural lag; ~68% accounting for rural-dominant composition |
| LPG_clean_cooking_fuel | 42.00 | C | NFHS-5 Jalpaiguri: 42.7% clean fuel; direct district anchor; Ujjwala scheme expansion 2019-21 |
| Wood_biomass_fuel | 53.00 | C | Declining as LPG rises; terai forest access still drives biomass use |
| Other_fuel | 5.00 | E | Kerosene + dung; residual; stable |
| Electricity | 97.00 | C | NFHS-5 Jalpaiguri: 97.4%; Saubhagya saturation by 2021; direct district anchor |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 81.00 | E | Predominantly native Rajbanshi SC community; COVID return-migration temporarily swelled native register by ~1pp but mostly returned by end-2021 |
| WB_other_district | 5.00 | E | Stable; in-migrants from Cooch Behar, Darjeeling |
| Other_Indian_state | 2.50 | E | Hindi/Bihari trader fringe; stable |
| Bangladesh_origin | 4.00 | D | Smaller refugee fraction than South Bengal; some Namasudra/SC partition-era inflow; stable |
| Outside_India | 0.50 | E | Negligible; Nepal-origin registered households |
| Out_migrant | 4.00 | E | COVID return-migration visible in register; higher than 2019 (~3%) as some returned and re-registered; partially reversed by end-2021 |
| Nepal_Bhutan_origin | 3.00 | E | AC-local: Nepali-speaking settled community in terai zone; stable |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Sadri | Nepali | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 80.50 | 0.80 | 0.10 | 1.10 | 5.60 | 1.10 | 10.80 | E | Rajbanshi SC = Rajbongshi-speaking; Nepali within Hindu; district language pattern; marginal Rajbongshi/Nepali growth within Hindu |
| Muslim | 97.00 | 0.50 | 1.50 | 0.50 | 0.50 | 0.00 | 0.00 | E | Maynaguri Muslims are Bengali-dominant peasantry; tiny Urdu fringe; stable |
| Christian | 70.00 | 5.00 | 0.00 | 10.00 | 5.00 | 5.00 | 5.00 | E | Small base; mixed language |
| Sarna_ORP | 30.00 | 0.00 | 0.00 | 20.00 | 20.00 | 30.00 | 0.00 | E | Tribal; Sadri + Rajbongshi dominant |
| Other_residual | 60.00 | 10.00 | 0.00 | 10.00 | 5.00 | 5.00 | 10.00 | E | Mixed residual |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion. 2D canonical layout.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 78.86 | 1.48 | 3.33 | 4.44 | 11.89 | 0.00 | 0.00 | E | SC_total 70.97%/90.00% Hindu = 78.86%; ST 1.33%/90.00% = 1.48%; UC, OBC, Other scaled to Hindu total |
| Muslim | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 100.00 | 0.00 | A | self-evident |
| Christian | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 100.00 | A | self-evident |
| Sarna_ORP | 10.00 | 80.00 | 0.00 | 5.00 | 5.00 | 0.00 | 0.00 | E | Tribal religion routes mostly to ST; small SC fraction |
| Other_residual | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 100.00 | E | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 81.00 | 4.50 | 2.50 | 4.50 | 0.50 | 3.50 | E | Rajbanshi SC native-dominant; some Bangladesh partition inflow; COVID return-migration |
| Muslim | 88.00 | 5.00 | 1.00 | 3.00 | 0.50 | 2.50 | E | Mostly native Bengali Muslim peasantry; stable |
| Christian | 75.00 | 10.00 | 5.00 | 5.00 | 0.00 | 5.00 | E | Mixed base |
| Sarna_ORP | 90.00 | 5.00 | 2.00 | 0.00 | 0.00 | 3.00 | E | Tribal; predominantly native |
| Other_residual | 40.00 | 15.00 | 35.00 | 3.00 | 2.00 | 5.00 | E | Nepali/Hindi trade/service migrants |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 71.00 | 59.00 | 92.00 | C | Dominant group; near AC average; Lakshmir Bhandar bank-account push |
| Muslim | 62.00 | 48.00 | 83.00 | C | Slightly below Hindu; NFHS-5 WB religion gap narrowing |
| Christian | 76.00 | 55.00 | 93.00 | E | Small base; slightly higher asset access |
| Sarna_ORP | 46.00 | 28.00 | 75.00 | E | Tribal fringe; lower access |
| Other_residual | 81.00 | 65.00 | 95.00 | E | Mostly better-off Nepali/Hindi migrants |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 7.00 | 14.00 | 15.00 | 20.00 | 18.00 | 20.00 | 6.00 | E |
| SC_total | 23.00 | 27.00 | 22.00 | 15.00 | 8.00 | 4.00 | 1.00 | E |
| ST_total | 28.00 | 27.00 | 21.00 | 13.00 | 7.00 | 3.00 | 1.00 | E |
| OBC | 16.00 | 24.00 | 23.00 | 19.00 | 10.00 | 6.50 | 1.50 | E |
| Other_Hindu_middle | 16.00 | 24.00 | 23.00 | 19.00 | 10.00 | 6.50 | 1.50 | E |
| Muslim | 20.00 | 26.00 | 23.00 | 17.00 | 9.00 | 4.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share within age-gender cell.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 11.00 | 9.00 | E |
| 23_27 | 10.00 | 8.00 | E |
| 28_32 | 9.00 | 6.00 | E |
| 33_37 | 8.00 | 4.50 | E |
| 38_42 | 6.50 | 3.50 | E |
| 43_47 | 5.50 | 2.50 | E |
| 48_52 | 5.00 | 2.00 | E |
| 53_57 | 4.50 | 1.50 | E |
| 58_62 | 4.00 | 1.00 | E |
| 63_67 | 3.50 | 1.00 | E |
| 68 | 3.00 | 0.50 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 6.00 | 28.00 | E |
| 23_27 | 42.00 | 82.00 | E |
| 28_32 | 82.00 | 93.00 | E |
| 33_37 | 92.00 | 91.00 | E |
| 38_42 | 93.00 | 89.00 | E |
| 43_47 | 92.00 | 85.00 | E |
| 48_52 | 91.00 | 78.00 | E |
| 53_57 | 90.00 | 67.00 | E |
| 58_62 | 87.00 | 53.00 | E |
| 63_67 | 81.00 | 36.00 | E |
| 68 | 71.00 | 20.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 42.00 | 63.00 | C | COVID smartphone surge; rural cultivator catch-up |
| Agricultural_labourer | 32.00 | 54.00 | C | Lowest income; lowest smartphone; +12pp from 2019 |
| Household_industry | 48.00 | 68.00 | C | Cottage industry; +13pp |
| Manufacturing | 62.00 | 80.00 | C | |
| Construction | 55.00 | 71.00 | C | |
| Trade_retail | 78.00 | 87.00 | C | Mainaguri town concentration |
| Transport_logistics | 73.00 | 82.00 | C | NH-27 corridor workers |
| Services | 82.00 | 90.00 | C | Private services |
| Government_services_teachers | 92.00 | 96.00 | C | Highest access |
| Out_migrant_worker | 78.00 | 74.00 | D | Working outside; smartphone-dependent for remittances; very high penetration |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 38.00 | 1.50 | E |
| Primary | 40.00 | 3.00 | E |
| Middle | 37.00 | 5.00 | E |
| Secondary | 30.00 | 8.00 | E |
| Higher_Secondary | 22.00 | 12.00 | E |
| Graduate | 25.00 | 14.00 | E |
| Postgraduate | 35.00 | 10.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 016. See NORMALIZED_SCHEMA.md §4.7.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Mainaguri_town | 86.50 | 11.50 | 0.50 | 0.20 | 1.30 | E | Town slightly higher Muslim presence than rural; marginal change from 2019 |
| U2_Maynaguri_CDB_rural | 90.20 | 9.57 | 0.05 | 0.08 | 0.10 | E | Rural CDB; approximates block-level Census 2011 adjusted for differential growth |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit).

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Mainaguri_town | 6.00 | 60.00 | 1.00 | 6.00 | 15.00 | 11.50 | 0.50 | E |
| U2_Maynaguri_CDB_rural | 2.50 | 72.50 | 1.35 | 3.75 | 10.90 | 8.75 | 0.25 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Mainaguri_town | 84.00 | 72.00 | 10.00 | 96.00 | C |
| U2_Maynaguri_CDB_rural | 68.00 | 55.00 | 3.00 | 90.00 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Mainaguri_town | 72.00 | 82.00 | 97.00 | 99.00 | C |
| U2_Maynaguri_CDB_rural | 38.00 | 64.00 | 92.00 | 97.00 | C |

### D.15 Vote × Religion (2021 AE anchor)

P(party ‖ religion) — calibrated to 2021 AE AC-016 result (BJP 48.84%, AITC 43.79%; LF+Others ~7.37%).

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 53.00 | 39.00 | 0.50 | 3.50 | 4.00 | C | BJP retained Rajbanshi SC consolidation from 2019; AITC recovered ~1pp among Hindu vs 2019 LS; CSDS 2021 WB regional pattern |
| Muslim | 5.00 | 82.00 | 3.00 | 6.00 | 4.00 | C | Muslim AITC bloc strengthened vs 2019 LS; +2pp AITC; Mamata appeal |
| Christian | 20.00 | 62.00 | 4.00 | 7.00 | 7.00 | E | Small base; AITC gains among non-Hindu minorities |
| Sarna_ORP | 40.00 | 47.00 | 2.00 | 6.00 | 5.00 | E | Tribal mixed; slight AITC recovery |
| Other_residual | 45.00 | 37.00 | 4.00 | 5.00 | 9.00 | E | Nepali/Hindi fringe; BJP-leaning |

### D.16 Vote × Caste (2021 AE anchor)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 62.00 | 28.00 | 3.00 | 5.00 | 2.00 | C | UC BJP-leaning; stable |
| OBC | 44.00 | 40.00 | 3.00 | 7.00 | 6.00 | C | Slight AITC recovery vs 2019 LS |
| SC_total | 51.50 | 40.00 | 0.50 | 4.00 | 4.00 | C | Rajbanshi SC BJP consolidation maintained but slight AITC recovery; calibrated to AC result; BJP margin ~5pp in 2021 AE |
| ST_total | 40.00 | 43.00 | 2.00 | 9.00 | 6.00 | C | Tribal; slight AITC lead |
| Other_Hindu_middle | 47.00 | 42.00 | 2.00 | 5.00 | 4.00 | E | Residual Hindu middle |
| Muslim | 5.00 | 82.00 | 3.00 | 6.00 | 4.00 | C | Same as D.15 Muslim row |

### D.17 Vote × Gender (2021 AE anchor)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 51.00 | 41.00 | 0.80 | 3.50 | 3.70 | C | CSDS 2021 WB; male BJP-leaning; slight AITC recovery vs 2019 |
| Female | 46.00 | 48.00 | 0.70 | 2.30 | 3.00 | C | Women more AITC-leaning; Lakshmir Bhandar (Apr 2021) announcement effect on AE campaign |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for AC 016. See NORMALIZED_SCHEMA.md §4.7.)

---

## E. 2021 baseline vote (calibration target)

> **Calibration target: 2021 WB Assembly Election, AC 016 Maynaguri.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 48.84 | A | ECI 2021 AE; Kaushik Roy 115,306 votes / 236,093 total valid; wb_ac_master_v3.csv |
| AITC | 43.79 | A | Manoj Roy 103,395 votes; wb_ac_master_v3.csv |
| INC | 0.60 | D | INC candidate; estimated from residual allocation; sub-1% in most North Bengal ACs 2021 |
| LF | 4.77 | D | CPI(M) + SUCI(C) + other LF; residual of total valid minus BJP − AITC − INC − NOTA = 17,392 votes; ~7.37% total non-BJP/AITC; split LF ~4.77% / NOTA+others ~2.60% estimate |
| Other_NOTA | 2.00 | D | NOTA + minor parties (BSP, AMB, IND); estimated from residual |
| **Sum** | **100.00** | — | self-check; total valid votes 236,093; electorate 264,265; turnout ~89.3% |

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 016 (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Dinabandhu Roy (Palu) | RSP | ~48 | AITC candidate | AITC | ~36 | ~est. 15,000 |
| 2014 by-election | Ananta Deb Adhikari | AITC | — | Dinabandhu Roy (Palu) | RSP | — | ~31,790 |
| 2016 AE | Ananta Deb Adhikari | AITC | ~54 | Chhaya Dey (Roy) | RSP | ~35 | 34,907 |

Notes: Maynaguri was an RSP (Left Front) stronghold in 2011, reversing to AITC in the 2014 by-election. AITC held comfortably in 2016 (electorate 236,663; margin 34,907). The RSP-to-AITC-to-BJP trajectory mirrors the North Bengal pattern of Left erosion followed by BJP surge.

### 2019 LS Anchor (AC 016 segment within Jalpaiguri LS PC 3)

| Party | Candidate | Votes | AC-016 segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Dr Jayanta Kumar Roy | 110,819 | 49.58% | A | data/2019_AssemblySegmentLevelVotingData.csv |
| AITC | Bijoy Chandra Barman | 96,072 | 42.98% | A | Same |
| INC | Mani Kumar Darnal | 1,705 | 0.76% | A | Same |
| LF | CPIM + SUCI(C) | 6,360 | 2.85% | A | Same |
| Other_NOTA | BSP + IND + NOTA | 8,564 | 3.83% | A | Same |

The 2019 LS result showed BJP surge to ~49.6% against AITC ~43%, mirroring the North Bengal BJP wave. The 2021 AE result (BJP 48.84% vs AITC 43.79%) represented a modest AITC recovery of ~0.8pp in an Assembly election context where AITC won 213/294 seats statewide.

### LS 3 Jalpaiguri — historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2011 AE (constituency) | Dinabandhu Roy | RSP | ~48 | RSP Left Front hold |
| 2014 LS | Bijoy Chandra Barman | AITC | ~39 | AITC won; CPI(M) ~22%; BJP ~25% |
| 2016 AE | Ananta Deb Adhikari | AITC | ~54 | AITC consolidated |
| 2019 LS | Dr Jayanta Kumar Roy | BJP | ~50 | BJP wave in North Bengal |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Maynaguri CD Block Primary Census Abstract (pop_total 337,251; SC 239,342; ST 4,492; sex_ratio 935; literacy 75.42%; female literacy 68.61%; workers 123,042; cultivators 32,623; agri-labourers 29,240; hh_industry 1,386; other_workers 34,844; households 78,369)
- Census of India 2011 — Maynaguri Block language data (Bengali 84.26%, Rajbongshi 5.08%, Sadri 1.02%)
- Election Commission of India — 2021 WB AE AC 016 result (data/master/wb_ac_master_v3.csv: electors 264,265; winner Kaushik Roy BJP 115,306; runner-up AITC 103,395; margin 11,911)
- Election Commission of India — 2019 LS GE results for AC 016 (data/2019_AssemblySegmentLevelVotingData.csv)
- Delimitation Commission of India 2008 — WB Schedule (AC 016 Maynaguri SC reserved; part of PC 3 Jalpaiguri SC)
- Election Commission of India — 2016 AE result (electorate 236,663; margin 34,907); 2014 by-election

### Secondary sources (tier B / C)

- NFHS-5 (2019-21) Jalpaiguri District — electricity 97.4%; clean fuel 42.7%; improved water 95.2%; improved sanitation 73.2%; under-15 pct 22.6% (data/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv)
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline (urban/rural split)
- CSDS-Lokniti 2021 WB post-poll regional cross-tabs — vote × religion / caste / gender (used via published summaries)
- PMJDY enrollment data + Lakshmir Bhandar bank-account drive — banking access baseline
- Jalpaiguri District Census 2011: SC 37.7%, ST 18.9%, Hindu 82.41%, Muslim 13.25%

### Tertiary / journalistic (tier D)

- Resultuniversity.com / Oneindia — 2016 AE and 2014 by-election margin figures
- Jalpaiguri district BPL rate estimates (~35% rural 2012) via district statistical handbook pattern
- 2021 AE LF / INC / NOTA breakdown: residual from ECI total valid minus BJP − AITC; candidate-level breakdown not retrieved for v0
- data/candidates_2026/wb_2021_candidates.csv — Kaushik Roy (BJP) winner, age 37, 12th pass, assets ~Rs 42L

### Tier-D / E reliance flags (what to distrust)

- **Caste sub-group shares within SC** (C.2 sub-rows) — Rajbanshi share estimated from district journalistic pattern; no post-1931 caste census; tier C/D
- **Migration / birthplace shares** (C.16, D.3) — no public AC-level Census D-series; tier E/D from district pattern
- **GP-level detail** (D.11–D.14) — collapsed to 2 sub-units; refine when DCHB Part-A accessible
- **Vote × Demographic** (D.15–D.17) — CSDS 2021 WB regional rollup calibrated to AC result; tier C; INC/LF/Other splits (D.15–D.17) have tier-D calibration basis
- **INC / LF / Other_NOTA breakdown in §E** — residual only; no candidate-level data for non-BJP/AITC parties; tier D
- **Smartphone and banking asset** (C.14) — COVID surge estimated at +20pp smartphone; PMJDY + Lakshmir Bhandar banking push estimated at +6pp; no direct AC-level survey; tier C

### v0 known gaps

1. DCHB Jalpaiguri Part-A — sub-unit collapsed to 2 (town + CDB rural); GP-level decomposition deferred
2. Full candidate-level 2021 AE result — LF/INC/NOTA breakdown from residual only; ECI Form-20 for 2021 AE AC 016 not fetched
3. Census HH-13 block-level — using NFHS district-level proxy for asset/media
4. Census D-series — using qualitative/district-level anchor for migration
5. Full CSDS 2021 WB regional cross-tabs — using published summary for D.15–D.17
6. Lakshmir Bhandar penetration data — WB CDWDSW dashboard not scraped; banking-access increase estimated from scheme design (+6pp)

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No post-2021 events referenced.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2021 WB Assembly Election result — used as §E calibration target above

(This was the calibration target for this file; it is NOT an out-of-sample gate.)

### 2024 Lok Sabha Election — AC 016 segment within Jalpaiguri LS (PC 3) (tier A, CSV)

> Figures below are **tier A** — sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=16, Maynaguri. Electors: 272,625.

| Party | Candidate (LS level) | Votes | AC-016 segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Dr Jayanta Kumar Roy | 112,763 | 48.47% | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Nirmal Chandra Roy | 108,018 | 46.43% | A | Same |
| CPI(M) | Debraj Barman | 5,988 | 2.57% | A | Same |
| NOTA | — | 2,224 | 0.96% | A | Same |
| Others (BSP, KPPU, SUCI, MPOI, IND) | various | 3,638 | 1.57% | A | Same |
| **BJP margin over AITC** | | **4,745 votes** | **2.04 pp** | A | Computed |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC-016 shares within ±3pp:
- BJP target: 48.5% ± 3pp
- AITC target: 46.4% ± 3pp
- LF + Others target: 5.1% ± 3pp

Note: The BJP margin narrowed sharply from 2021 AE (~5.05pp) to 2024 LS (~2.04pp), indicating continued AITC recovery. Simulator must model this as post-2021 narrative injection output, not as a pre-baked input.
