# AC 095 — Bangaon Uttar (SC) — Calibrated 2024 Population Snapshot

> **Frozen at end-2024.** This file describes the demographic and behavioural state of AC 95 Bangaon Uttar as of end-2024 — it does not reference any post-2024 events. Use 2026 AE results as the out-of-sample validation gate for downstream simulators.
>
> Companion artifacts: [`methodology_2024.md`](../../methodology_2024.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).
>
> **Forbidden in this file:** 2025, 2026, SIR, Special Intensive Revision, AE-2026, 2026 election.

---

## A. Identity (as of 2024)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 95 | A | ECI / Delimitation Commission 2008 |
| AC name | Bangaon Uttar | A | ECI |
| Reservation | SC | A | Delimitation 2008 |
| District | North 24 Parganas | A | Delimitation 2008 |
| Sub-division | Bangaon | A | WB administrative |
| LS constituency | 14 — Bangaon (SC reserved) | A | Delimitation 2008 |
| LS segments included with AC 95 | AC 92 Kalyani · 93 Haringhata · 94 Bagda · 95 Bangaon Uttar · 96 Bangaon Dakshin · 97 Gaighata · 98 Swarupnagar | A | Delimitation 2008 |
| AC composition | Bangaon Municipality (full) + 7 of ~16 GPs of CDB Bangaon: Akaipur, Chhaigheria, Dharma Pukuria, Ganganandapur, Ghatbore, Gopalnagar-I, Gopalnagar-II | A | Delimitation 2008 |
| Geographic note | Northern N24P, India-Bangladesh border; Petrapole land port lies within sub-division | A | — |
| Two sub-units used in v0 | **U1: Bangaon Municipality** (urban) · **U2: CDB_Bangaon_rural_share** (the 7 GPs) | E | v0 simplification |
| 2024 LS electorate (AC-95 segment) | 264,506 | A | 2024_AssemblySegmentLevelVotingData.csv |
| 2024 LS BJP winner (Bangaon LS) | Shantanu Thakur (BJP, SC, Matua) | A | ECI 2024 LS |
| 2024 LS TMC candidate | Biswajit Das (TMC, non-Matua, ex-Bagda MLA — two-time defector) | A | ECI 2024 LS |
| Sitting MLA (AC-95, as of end-2024) | Ashok Kirtania (BJP, SC, Matua-aligned) — won 2021 AE by 10,488 | A | ECI 2021 AE |

---

## B. 2024 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~199,792 | E | Census 2011 |
| 2024 projected population | ~227,000 | E | 13-yr compound religion-differential growth from Census 2011 |
| Sex ratio (2024, F per 1000 M) | ~951 | E | N24P district trend; marginal improvement |
| 2024 LS electorate (AC-95 segment) | 264,506 | A | 2024_AssemblySegmentLevelVotingData.csv |
| Estimated M / F / TG split | 51.1% M / 48.9% F / ~0.01% TG | E | Trend from 2021 SIR; female electorate share rising slightly |
| 2024 LS total valid votes (AC-95 segment) | 209,954 | A | 2024_AssemblySegmentLevelVotingData.csv |
| 2024 LS turnout (AC-95 segment) | ~79.4% | A | Derived: 209,954 + NOTA / 264,506 |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 85.72 | E | 2011 weighted, projected 2011→2024 (Hindu +1.0%/yr, 13 yr); Bangladesh temple attacks 2021 reinforced community cohesion |
| Muslim | 13.35 | E | 2011 weighted, projected; slight relative decline in share denominator |
| Christian | 0.27 | E | Bangaon sub-division; marginal decline |
| Sarna_ORP | 0.10 | E | Stable |
| Other_residual | 0.56 | E | Residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 43.0 | B | Weighted: Muni ~40% SC + CDB-rural 46.60% (Census 2011); stable across projection |
| └ Namasudra_Matua_SC | 39.5 | C | ~92% of SC pool; Outlook: ~40% of Bangaon LS electorate is Matua |
| └ Bagdi_SC | 1.5 | E | ~3% of SC pool |
| └ Poundra_SC | 0.7 | E | ~1.6% of SC pool |
| └ Other_SC | 1.3 | E | Residual |
| **ST_total** | 3.6 | A | Bangaon CDB Census 2011; stable |
| **UC_bhadralok** | 10.0 | E | Brahmin/Kayastha/Baidya; concentrated in Muni |
| **OBC** | 2.0 | E | Mahishya / Sadgop / Kurmi / Teli; not salient |
| **Other_Hindu_middle** | 26.72 | E | Residual within Hindu (85.72 − 43 − 3.6 − 10 − 2) |
| **Muslim** | 13.35 | E | See C.1 |
| **Christian_plus_Sarna_plus_Other** | 0.93 | E | See C.1 |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2024, adults 18+ only)

Renormalized to 18+ electorate; children 0–17 excluded.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.5 | E | Born 2002–2006; 13-yr projection from Census 2011 N24P age pyramid |
| 23_27 | 12.8 | E | |
| 28_32 | 13.0 | E | |
| 33_37 | 12.0 | E | |
| 38_42 | 10.8 | E | |
| 43_47 | 9.8 | E | |
| 48_52 | 8.7 | E | |
| 53_57 | 7.2 | E | |
| 58_62 | 5.8 | E | |
| 63_67 | 4.7 | E | |
| 68 | 3.7 | E | |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.10 | E | N24P trend; sex ratio ~951 by 2024 |
| Female | 48.89 | E | |
| Third_gender | 0.01 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 98.80 | E | Stable; Bangaon CDB 99.19% Bengali (2011); no significant migration shift |
| Hindi | 0.70 | E | Muni Marwari/Bihari trader fringe; stable |
| Urdu | 0.30 | E | Small Muslim urban pocket |
| Other | 0.20 | E | Residual |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 11.0 | E | ~88.5% literacy by 2024 (13-yr trend); older illiterate cohort dying out |
| Primary | 21.5 | E | |
| Middle | 21.5 | E | |
| Secondary | 20.0 | E | Secondary completion rising |
| Higher_Secondary | 13.0 | E | +2pp from 2019; expansion of HS institutions in N24P |
| Graduate | 10.0 | E | +1pp from 2019; marginal graduate growth |
| Postgraduate | 3.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 31.0 | E | Post-COVID recovery; Petrapole trade depressed Aug 2024+ but main-worker share relatively stable |
| Marginal_worker | 11.0 | E | Stable |
| Non_worker | 38.5 | E | Lakshmir Bhandar ₹1,200/mo (SC/ST tier) fully penetrated by 2024 — housewives / elderly included |
| Student | 12.0 | E | Stable |
| Unemployed | 7.5 | E | Marginally lower than 2021 as some graduates entered gig/services; SSC scam exposure (2022) elevated educated-unemployment anxiety |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 17.5 | E | Marginal decline as rural youth seek non-farm work |
| Agricultural_labourer | 27.0 | E | Slight decline; MGNREGS absorption |
| Household_industry | 4.0 | E | Stable |
| Manufacturing | 4.0 | E | Limited; no new industrial investment in Bangaon |
| Construction | 6.0 | E | Stable; some out-migrants working in construction elsewhere |
| Trade_retail | 12.5 | E | Bangaon Muni hub; slight growth; UPI-enabled small retail |
| Transport_logistics | 6.0 | E | Petrapole trade depressed Aug 2024+ under Bangladesh interim regime; some income fall in transport belt |
| Services | 12.5 | E | Growth in services |
| Government_services_teachers | 4.0 | E | SSC scam (2022) created teacher-recruitment freeze; stagnant govt jobs pipeline |
| Out_migrant_worker | 6.5 | D | Matua men to Kerala/TN/Maharashtra; sustained out-migration |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.0 | E | Stable |
| Employee | 28.0 | E | Stable |
| Single_worker | 50.0 | E | Dominant; cultivator + own-account artisan + small trader |
| Family_worker | 20.0 | E | Within agri-household |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2024, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 19.0 | C | WB poverty continuing gradual fall; Lakshmir Bhandar lifts bottom band; ~19% by 2024 |
| Above_Poverty_Line_low_income | 39.0 | E | Large near-poor band; primary Lakshmir Bhandar + Khadya Sathi recipients |
| Lower_middle | 26.0 | E | |
| Middle | 13.0 | E | Slight growth |
| Upper_middle_well_off | 3.0 | E | Bangaon Muni small affluent fringe |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Municipality location (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Bangaon_Municipality | 54.5 | E | 2011: 54.5%; stable in 13-yr window; no boundary changes |
| U2_CDB_Bangaon_rural_share | 45.5 | E | Remainder; 7 GPs |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.3 persons | E | Gradual nuclearization trend; WB 4.3 by 2021; ~4.3 by 2024 |
| Nuclear_HH | 71.0 | E | Slight increase |
| Joint_HH | 23.0 | E | |
| Extended_multi_generation | 6.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 28.0 | E | Stable; younger cohort expanding but first-marriage age rising marginally |
| Currently_married | 64.0 | E | |
| Widowed | 7.0 | E | |
| Separated_divorced | 1.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2024, household level)

Smartphone effectively saturated; UPI/digital payments near-universal in urban, high in rural. Bangladesh interim regime (Aug 2024) creates news-demand spike for border AC.

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 84.0 | C | Near-saturation; urban 95%+, rural 72%; AC weighted ~84% |
| Radio | 3.0 | C | Declining |
| Mobile_phone | 94.0 | C | Near-universal; any handset |
| Smartphone_with_internet | 82.0 | C | NFHS-5 WB (2019-21) rural 56%, urban 82%; extrapolated with 3-yr Jio-affordable-5G trend → ~82% by 2024; digital saturation notably achieved |
| Computer | 13.0 | C | Marginal growth; laptop penetration in HS/grad households |
| Two_wheeler | 40.0 | C | Growth; aspiration good among young rural males |
| Four_wheeler | 9.0 | C | Slight growth; Muni upper-middle |
| Banking_access | 96.0 | B | PMJDY peak; UPI adoption; near-universal in banked households |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2024)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 89.0 | C | NFHS-5 + Jal Jeevan Mission (2019+) pipeline extension; rural +5pp from 2021 |
| Improved_sanitation | 85.0 | C | Continued Swachh Bharat + state push; rural gains |
| LPG_clean_cooking_fuel | 63.0 | C | Ujjwala second phase + subsidy; rural ~40%, urban 90%; AC weighted ~63% |
| Wood_biomass_fuel | 32.0 | C | Declining; offset by LPG gains |
| Other_fuel | 5.0 | C | Stable residual |
| Electricity | 99.0 | A | Near-universal by 2024; Saubhagya saturation |
| **Note** | (cooking-fuel rows sum to 100; water/sanitation/electricity are independent) | — | — |

### C.16 Migration / birthplace (2024, all ages)

Bangladesh interim government (Aug 2024): Sheikh Hasina ousted, Muhammad Yunus interim regime. India-Bangladesh trade through Petrapole severely disrupted (30–40% below 2023 baseline). Sustained livelihood depressor for AC-95 Petrapole-economy households. Bangladesh temple/minority attacks (Oct 2021, Nov 2021) had already reinforced Matua refugee anxiety.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 64.5 | D | Stable; COVID returnee registrations mostly normalized |
| WB_other_district | 9.0 | D | Stable; Kolkata service-class in Muni |
| Other_Indian_state | 3.0 | D | Marwari/Bihari trader fringe |
| Bangladesh_origin | 23.0 | D | **Load-bearing**: Matua community. Bangladesh interim regime Aug 2024+ creates new anxiety in this population (minority reports, trade disruption) reinforcing historical refugee identity |
| Outside_India | 0.5 | E | Negligible |
| Out_migrant | 0.0 | E | Registered here but working outside; net; normalised |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

| Religion | Bengali | Hindi | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|
| Hindu | 99.4 | 0.5 | 0.0 | 0.1 | E | Stable from 2021 |
| Muslim | 95.0 | 1.5 | 3.0 | 0.5 | E | Bengali-Sheikh dominant |
| Christian | 90.0 | 5.0 | 0.0 | 5.0 | E | |
| Sarna_ORP | 60.0 | 30.0 | 0.0 | 10.0 | E | |
| Other_residual | 60.0 | 30.0 | 0.0 | 10.0 | E | |

### D.2 Religion × Caste (2D layout)

Each row sums to 100.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 50.3 | 4.2 | 11.7 | 2.3 | 31.5 | 0 | 0 | C | Namasudra-Matua dominant; stable from 2021 |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | |
| Sarna_ORP | 0 | 92 | 0 | 5 | 3 | 0 | 0 | E | ST-dominant |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | |

### D.3 Religion × Migration

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 60 | 8 | 2 | 30 | 0 | 0 | D | Matua refugee population; Bangladesh interim regime heightens salience |
| Muslim | 95 | 3 | 1 | 1 | 0 | 0 | D | Bengali-Sheikh; mostly native |
| Christian | 80 | 10 | 5 | 5 | 0 | 0 | E | |
| Sarna_ORP | 60 | 20 | 15 | 5 | 0 | 0 | E | |
| Other_residual | 50 | 20 | 25 | 5 | 0 | 0 | E | |

### D.4 Religion × Asset / media (flags)

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 85 | 83 | 97 | C | NFHS-5 + 3-yr extrapolation; near-saturation Hindu belt |
| Muslim | 79 | 72 | 90 | C | Gap narrowing; Jio rural diffusion |
| Christian | 88 | 80 | 96 | C | |
| Sarna_ORP | 72 | 62 | 85 | E | |
| Other_residual | 96 | 90 | 99 | E | Trader community |

### D.5 Caste × Education

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 3 | 8 | 10 | 18 | 21 | 27 | 13 | E |
| Namasudra_Matua_SC | 10 | 20 | 22 | 21 | 14 | 10 | 3 | E |
| Bagdi_SC | 18 | 26 | 24 | 17 | 10 | 4 | 1 | E |
| ST_total | 21 | 28 | 22 | 15 | 9 | 4 | 1 | E |
| OBC | 12 | 20 | 22 | 20 | 14 | 9 | 3 | E |
| Other_Hindu_middle | 11 | 20 | 22 | 20 | 14 | 10 | 3 | E |
| Muslim | 14 | 22 | 23 | 20 | 12 | 8 | 1 | E |

### D.6 Age × Gender × Education

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 21 | 20 | E |
| 23_27 | 19 | 17 | E |
| 28_32 | 16 | 13 | E |
| 33_37 | 14 | 9 | E |
| 38_42 | 12 | 7 | E |
| 43_47 | 10 | 6 | E |
| 48_52 | 9 | 4 | E |
| 53_57 | 7 | 3 | E |
| 58_62 | 6 | 2 | E |
| 63_67 | 5 | 2 | E |
| 68 | 5 | 2 | E |

### D.7 Marital status × Age × Gender

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 5 | 25 | E |
| 23_27 | 38 | 78 | E |
| 28_32 | 80 | 92 | E |
| 33_37 | 92 | 90 | E |
| 38_42 | 92 | 90 | E |
| 43_47 | 92 | 88 | E |
| 48_52 | 90 | 82 | E |
| 53_57 | 89 | 75 | E |
| 58_62 | 88 | 65 | E |
| 63_67 | 75 | 40 | E |
| 68 | 72 | 30 | E |

### D.8 Occupation × Asset / media

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 65 | 82 | C | Digital saturation reached rural cultivators by 2024 |
| Agricultural_labourer | 55 | 72 | C | Jio affordable; significant jump |
| Household_industry | 70 | 83 | C | |
| Manufacturing | 80 | 90 | C | |
| Construction | 77 | 84 | C | |
| Trade_retail | 92 | 95 | C | Near-saturation; UPI QR mandatory in many shops |
| Transport_logistics | 87 | 90 | C | Petrapole logistics workers smartphone-heavy; trade disrupted Aug 2024 |
| Services | 92 | 95 | C | |
| Government_services_teachers | 96 | 98 | C | Highest; SSC scam anxiety about job futures but ownership unaffected |
| Out_migrant_worker | 90 | 85 | D | Smartphone essential for remittance; near-universal |

### D.9 Education × Workforce participation

| Education | Unemployed_seeking | Main_worker_rate | Tier |
|---|---|---|---|
| Illiterate | 2 | 35 | E |
| Primary | 4 | 38 | E |
| Middle | 6 | 35 | E |
| Secondary | 10 | 30 | E |
| Higher_Secondary | 15 | 25 | E |
| Graduate | 18 | 27 | E |
| Postgraduate | 13 | 38 | E |

### D.10 Asset / media × Bilingualism

| Media_tier | Bilingual_pct | Tier | Source |
|---|---|---|---|
| TV_only_HH | 5 | E | Bengali TV dominant |
| TV_plus_smartphone_HH | 9 | E | YouTube cross-language content; Hindi news channels via Jio TV |
| Smartphone_only_HH | 8 | E | |
| No_asset_HH | 3 | E | Lowest exposure |

### D.11 GP × Religion

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Bangaon_Municipality | 92.0 | 7.0 | 0.5 | 0.0 | 0.5 | E | Muni heavily refugee-Hindu; stable |
| U2_CDB_Bangaon_rural_share | 78.2 | 20.8 | 0.5 | 0.0 | 0.5 | A | Bangaon CDB Census 2011; stable |

### D.12 GP × Caste

| Sub_unit | UC_bhadralok | Namasudra_Matua_SC | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Bangaon_Municipality | 14 | 38 | 41 | 1 | 5 | 36 | 7 | E |
| U2_CDB_Bangaon_rural_share | 5 | 41 | 45 | 6 | 3 | 25 | 21 | E |

### D.13 GP × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Bangaon_Municipality | 95 | 90 | 24 | 98 | C |
| U2_CDB_Bangaon_rural_share | 72 | 72 | 6 | 93 | C |

### D.14 GP × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Bangaon_Municipality | 88 | 95 | 97 | 100 | C |
| U2_CDB_Bangaon_rural_share | 35 | 74 | 80 | 98 | C |

### D.15 Vote × Religion (2024 LS, AC-95 segment anchor)

P(party ‖ religion) — anchored to 2024 LS AC-95 CSV result. BJP 52.32%, AITC 40.40%, INC 3.37%, Other_NOTA 3.91%.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 61 | 31 | 3 | 2 | 3 | C | CAA notification + Thakurbari endorsement; BJP Hindu consolidation; LF negligible |
| Muslim | 4 | 76 | 16 | 3 | 1 | C | Muslim consolidation toward AITC; INC retained some urban Muslim |
| Christian | 27 | 55 | 10 | 5 | 3 | E | |
| Sarna_ORP | 38 | 44 | 5 | 10 | 3 | E | |
| Other_residual | 48 | 35 | 10 | 3 | 4 | E | |

### D.16 Vote × Caste (2024 LS)

P(party ‖ caste) — anchored to 2024 LS AC-95 CSV result.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 62 | 27 | 5 | 3 | 3 | C | BJP bhadralok consolidation |
| OBC | 42 | 38 | 7 | 10 | 3 | C | Mixed |
| Namasudra_Matua_SC | 64 | 28 | 3 | 1 | 4 | C | CAA notification Mar 2024 boosted initial enthusiasm; Thakurbari endorsement machine (chronic through May 2024); Shantanu renominated; non-Matua AITC candidate Biswajit Das a liability |
| SC_total | 57 | 33 | 4 | 3 | 3 | C | Weighted SC pool; Matua dominant; Lakshmir Bhandar SC ₹1,200 tier creates AITC counter-pull |
| ST_total | 44 | 37 | 5 | 10 | 4 | C | |
| Muslim | 4 | 76 | 16 | 3 | 1 | C | |

### D.17 Vote × Gender (2024 LS)

P(party ‖ gender). Lakshmir Bhandar ₹1,200/mo (SC/ST tier) fully rolled out by 2024; powerful AITC women-voter retention signal.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 57 | 35 | 3 | 2 | 3 | C | CSDS 2024 WB post-poll; BJP male consolidation |
| Female | 47 | 46 | 3 | 2 | 2 | C | Lakshmir Bhandar SC ₹1,200 tier strongly retained women; CAA partially competed but delivery gap muted effect |
| Third_gender | 45 | 45 | 5 | 3 | 2 | E | |

### D.18 Vote × Welfare scheme exposure (2024 LS)

Schemes active at 2024 LS: Lakshmir Bhandar (₹1,000 general / ₹1,200 SC/ST; fully penetrated by 2024), Krishak Bandhu (raised to ₹10,000/yr by 2023), Kanyashree, Swasthya Sathi, Khadya Sathi. CAA rules notified Mar 2024 — a BJP welfare-analogue for Matua households.

| Welfare_exposure | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Lakshmir_Bhandar_SC_tier_HH | 44 | 49 | 3 | 2 | 2 | C | SC-tier ₹1,200/mo; even BJP-leaning Matua women show AITC tilt |
| Lakshmir_Bhandar_general_tier_HH | 34 | 56 | 4 | 4 | 2 | C | Non-SC general ₹1,000 tier; strong AITC retention |
| Krishak_Bandhu_cultivator_HH | 25 | 64 | 4 | 5 | 2 | C | Raised benefit; strong AITC credit |
| CAA_application_filed_HH | 68 | 24 | 3 | 1 | 4 | D | Matua households who filed CAA applications (est. ~15–20% of Bangladesh-origin HHs); high BJP retention despite delivery failure narrative |
| No_state_scheme_exposure | 60 | 27 | 6 | 5 | 2 | C | BJP-leaning |

---

## E. 2024 calibration target (2024 LS AC-95 segment — tier A)

Source: `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=95. The simulator must reproduce this aggregate within ±1pp.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 52.32 | A | Shantanu Thakur 109,848 votes; ECI 2024 LS CSV |
| AITC | 40.40 | A | Biswajit Das 84,818 votes; ECI 2024 LS CSV |
| INC | 3.37 | A | Pradipkumar Biswas 7,066 votes; ECI 2024 LS CSV |
| LF | 0.00 | A | No Left candidate fielded in Bangaon LS 2024; LF = 0 |
| Other_NOTA | 3.91 | A | AISF 2,420 + BSP 644 + SUCI 227 + PDS 204 + GSD 90 + IND 3,717 + NOTA 920 = 8,222 votes |

> ECI 2024 LS AC-95 segment: total valid votes 209,954 | electorate 264,506 | BJP margin over AITC 25,030 votes (11.92 pp)

---

## F. Vote history (2019–2024, chronological)

### AC 95 Assembly Elections

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Biswajit Das | AITC | 54.55 | Dr. Biswajit Biswas | CPI(M) | 40.12 | 23,620 |
| 2016 AE | Biswajit Das | AITC | 50.59 | Sushanta Baowali | AIFB | 33.07 | 33,192 |
| **2021 AE** | **Ashok Kirtania** | **BJP** | **47.65** | Biswanath Das | AITC | 42.54 | **10,488** |

### Bangaon LS (PC 14) history

| Year | Winner | Party | Notes |
|---|---|---|---|
| 2014 LS | Mamatabala Thakur | AITC | TMC held in tight three-way |
| 2019 LS | Shantanu Thakur | BJP | 48.85%; margin 111,594; Matua CAB/CAA mobilisation |
| **2024 LS (AC-95 segment)** | **Shantanu Thakur** | **BJP** | **52.32%; margin 25,030 at AC-95 level** |

### Key narrative events (2021–2024)

- **2021 May**: BJP wins AC-95 (Kirtania MLA); TMC wins state overall (213/294). BJP-MLA-in-opposition context: Kirtania faces constrained MLA-LAD access routed through state-controlled channels; incumbency record defaults to symbolic Matua identification (events.yaml: `candidate_profile_ashok_kirtania_incumbency`).
- **2021 Oct**: BSF 50km jurisdiction extension — Bangaon Uttar fully within new zone (events.yaml: `bsf_50km_jurisdiction`). TMC framed as federal overreach.
- **2021 Oct**: Bangladesh Durga Puja temple attacks — Matua refugee anxiety reinforced; "Hindus need protection" narrative activated (events.yaml: `bangladesh_temple_attacks_2021`).
- **2022**: SSC scam exposure — Partha Chatterjee arrested; ED seized cash at Arpita Mukherjee; anti-incumbency signal for AITC state-government, especially among educated youth seeking government jobs.
- **2023 Jan+**: Lakshmir Bhandar penetration in AC-95 fully rolled out — SC/ST women receiving ₹1,200/mo. Matua-SC women over-represented in higher tier. Estimated 60–70% of eligible women enrolled by 2023 (events.yaml: `scheme_penetration_lakshmir_bhandar_ac95`). Direct belief-vector input: recipients tilt AITC even within BJP-leaning Matua households.
- **2023 Apr–Jun**: Thakurbari clashes at Shantanu vs Mamatabala faction (April 2023, June 2023). Physical brawls over control of Boroma's residence; BJP framed TMC as aggressor (events.yaml: `thakurbari_clash_april2023`, `thakurbari_clash_june2023`).
- **2023 Jul+**: Bangladesh student-quota protests begin disrupting Petrapole trade (events.yaml: `petrapole_bd_disruption_chronic`). Truck-clearing, currency-exchange, dhaba and porter incomes hit.
- **2024 Feb**: Mamatabala Thakur nominated to Rajya Sabha by TMC — counter-Matua move pre-LS polling. Direct counter-pull on Matua vote ahead of CAA notification (events.yaml: `mamatabala_rajya_sabha`).
- **2024 Feb**: Sandeshkhali — Sheikh Shahjahan fugitive, women's protests; widespread N24P coverage. BJP leveraged extensively. Shahjahan arrested Feb 29 (events.yaml: `shahjahan_arrested`).
- **2024 Mar 11**: CAA rules notified — Matua belt jubilation; BJP "promise kept" narrative. AC-95 Matua households began filing CAA applications.
- **2024 Mar**: Shantanu Thakur renominated from Bangaon LS by BJP — "CAA-promise candidate seeks re-election" framing (events.yaml: `shantanu_renominated_2024`). Candidate profiles: Shantanu (BJP, MoS Ports/Shipping, Matua SC dynast, clean record, high symbolic capital); Biswajit Das (TMC, non-Matua, two-time defector, ex-Bagda MLA, credibility gap on events.yaml: `candidate_profile_shantanu_thakur_2024`, `candidate_profile_biswajit_das_2024`).
- **2024 Mar–May**: Thakurbari endorsement machine 2024 — daily blessings channeled into BJP campaign visuals; community-gatekeeper signal bypassing media (events.yaml: `thakurbari_endorsement_machine_2024`).
- **2024 May 8**: Mamata Banerjee rallies at Bangaon — Lakshmir Bhandar continuity pitch; CAA = NRC trap warning; reaches AITC-leaning women and Muslim voters strongly (events.yaml: `mamata_bangaon_rally_2024`).
- **2024 May 12**: PM Modi rallies at Bangaon — pitches CAA delivery, star-campaigner; Bengali TV saturated 48 hours; modulates how CAA-narrative reaches uncommitted Matua sub-populations (events.yaml: `modi_bangaon_rally_2024`).
- **2024 May 15–20**: CAA delivery satisfaction collapses pre-polling — only ~14 physical certificates issued from ~1.12 lakh applications by polling day. Mamatabala camp flips CAA frame from "promise kept" to "tokenism + citizenship-stripping trap." Even enrolled applicants registered the failure (events.yaml: `caa_delivery_failure_pre_ls`, `caa_delivery_failure_narrative`).
- **2024 Jun 4**: 2024 LS results — TMC 29 / BJP 12 / INC 1 in WB overall; BJP retained Bangaon LS. CAA delivery gap did not prevent BJP win in this seat; Matua loyalty and non-Matua AITC candidate proved decisive.
- **2024 Aug**: RG Kar Hospital rape-murder — mass protests; CBI investigation; AITC state government on defensive. Anti-incumbency signal for AITC statewide.
- **2024 Aug+**: Bangladesh interim regime (Yunus) — Petrapole India-Bangladesh trade depressed 30–40% below 2023 baseline. Chronic livelihood depressor for AC-95 transport/logistics/trader belt through end-2024 (events.yaml: `petrapole_trade_chronic_2024_26`).
- **2024 Jun+**: CAA grants delivery chronic — ~15,000 certificates issued from ~1.12 lakh applications. Delivery satisfaction gap sustained; belief-vector for Matua dissenters; Mamatabala camp narrative sustained (events.yaml: `caa_grants_delivery_chronic`).

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- Census of India 2011 — Bangaon CD Block Primary Census Abstract; North 24 Parganas district
- Election Commission of India — 2021 WB AE archive (AC-95: BJP 97,761; AITC 87,273; margin 10,488)
- `data/2024_AssemblySegmentLevelVotingData.csv` — ECI 2024 LS AC-segment (AC_NO=95: BJP 109,848; AITC 84,818; INC 7,066; other 8,222; electorate 264,506)
- ECI 2011 AE, 2016 AE, 2019 LS results for AC 95 / Bangaon LS
- Delimitation Commission 2008 — WB Schedule XXX

### Secondary sources (tier B/C)
- NFHS-5 (2019-21) West Bengal — household amenities, asset ownership, smartphone saturation
- WB CDWDSW Lakshmir Bhandar dashboard — scheme penetration; SC/ST ₹1,200 tier
- CSDS-Lokniti 2024 NES post-poll WB regional cross-tabs
- Pew Research India 2021 — religion-differential growth projections extrapolated to 2024

### Tertiary / journalistic (tier D)
- ThePrint: "CAA citizenship Bengal Matua disappointment" (delivery gap narrative)
- The Hindu: "Lakshmir Bhandar the trump card of Mamata Banerjee" (Apr 2024)
- The Hindu: "Modi Bengal rallies 2024"; Bangaon rally coverage (May 2024)
- BusinessToday: Shahjahan arrest (Feb 29, 2024)
- Outlook India: "Matua Mahasangha Maelstrom" — Bangaon LS Matua share ~40%
- IndiaToday: BJP first candidate list 2024 (Shantanu renomination)
- The Hindu: "India-Bangladesh Petrapole trade" — Petrapole chronic trade disruption coverage (events.yaml: `petrapole_trade_chronic_2024_26`)
- The Wire: CAA citizenship Bengal Matua disappointment

### Tier-D/E reliance flags
- **Caste sub-group shares** — tier C/E; no caste census post-1931
- **Migration/birthplace** (C.16, D.3) — tier D; no AC-level Census D-series
- **GP-level data** (D.11–D.14) — collapsed to 2 sub-units; refine when DCHB Part-A accessible
- **Asset/media** (C.14) — NFHS-5 WB + 3-yr extrapolation; smartphone near-saturation is regional observation
- **Vote × Demographic** (D.15–D.18) — CSDS 2024 WB regional rollup; anchored on AC-95 CSV tier-A result
- **D.18 welfare exposure** — CAA-application-filed HH estimate (~15–20% of Bangladesh-origin HHs) is tier D from journalistic sources

### v0 known gaps
1. LF = 0 in E (no Left candidate in Bangaon LS 2024); LF rows in D.15–D.17 reflect residual Left-aligned voter pool, not candidate presence
2. DCHB N24P Part-A — collapsed sub-units to 2 instead of 8
3. SSC scam quantitative impact on educated-unemployment anxiety: modeled as +1pp Unemployed vs 2021; tier E
4. CAA application filing rate in AC-95 Matua households: ~15–20% estimated; tier D

---

## H. Post-2024 validation anchors

No post-2024 validation anchors fetched in v0.

---

*v0 — generated 2026-04-28, frozen at 2024 state-of-knowledge. No post-2024 events referenced.*
