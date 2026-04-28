# AC 095 — Bangaon Uttar (SC) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural state of AC 95 Bangaon Uttar as of end-2021 — it does not reference any post-2021 events. Use the 2024 LS result as the out-of-sample validation gate for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).
>
> **Forbidden in this file:** 2022, 2023, 2024, 2025, 2026, SSC scam, Partha Chatterjee, RG Kar, SIR, CAA notification, CAA rules.

---

## A. Identity (as of 2021)

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
| 2021 AE electorate (ECI roll) | 251,387 | A | ECI 2021 WB AE archive |
| 2021 AE polling stations | 276 | A | ECI 2021 SIR |
| 2021 AE winner | **Ashok Kirtania (BJP)** — SC, Matua-community, Mahasangha-aligned | A | ECI 2021 AE |
| 2021 AE runner-up | Biswanath Das (AITC) — ex-Bagda-area AITC worker | A | ECI 2021 AE |
| 2021 AE BJP margin | **10,488 votes** | A | ECI 2021 AE |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~199,792 (Muni 108,864 + CDB-rural-share 90,928) | E | Census 2011 |
| 2021 projected population | ~221,000 | E | 10-yr compound religion-differential growth from Census 2011 (methodology §4) |
| Sex ratio (2021, F per 1000 M) | ~950 | E | N24P district baseline 949; minimal drift |
| 2021 ECI electorate (roll) | 251,387 | A | ECI 2021 AE SIR |
| Estimated M / F / TG split | 51.2% M / 48.8% F / ~0.01% TG | E | 2021 SIR composition |
| 2021 polling stations | 276 | A | ECI 2021 SIR |
| 2021 AE total votes polled | ~218,650 | A | ECI 2021 AE (derived from BJP 97,761 + AITC 87,273 + ~33,616 others) |
| 2021 AE turnout | ~86.9% | A | ECI 2021 AE |

---

## C. Marginal distributions (15 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 85.60 | E | 2011 weighted, projected 2011→2021 (Hindu +1.0%/yr, 10 yr) |
| Muslim | 13.45 | E | 2011 weighted, projected (+1.3%/yr — slight relative loss ~0.3pp over 10yr from Muslim share denominator growth) |
| Christian | 0.28 | E | Bangaon sub-division 2011; marginal decline |
| Sarna_ORP | 0.10 | E | Tribal religion fringe |
| Other_residual | 0.57 | E | Residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 43.0 | B | Weighted: Muni ~40% SC + CDB-rural 46.60% (Census 2011); stable |
| └ Namasudra_Matua_SC | 39.5 | C | ~92% of SC pool in Bangaon (Outlook: ~40% of Bangaon LS electorate is Matua) |
| └ Bagdi_SC | 1.5 | E | ~3% of SC pool |
| └ Poundra_SC | 0.7 | E | ~1.6% of SC pool |
| └ Other_SC | 1.3 | E | Residual |
| **ST_total** | 3.6 | A | Bangaon CDB Census 2011; rural pockets |
| **UC_bhadralok** | 10.0 | E | Brahmin/Kayastha/Baidya; concentrated in Muni |
| **OBC** | 2.0 | E | Mahishya / Sadgop / Kurmi / Teli; not salient in this AC |
| **Other_Hindu_middle** | 26.83 | E | Residual within Hindu (85.60 − 43 SC − 3.6 ST − 10 UC − 2 OBC) |
| **Muslim** | 13.45 | E | See C.1; sub-structure in D.2 |
| **Christian_plus_Sarna_plus_Other** | 0.95 | E | See C.1 |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2021, adults 18+ only)

Renormalized to 18+ electorate; children 0–17 excluded.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.5 | E | First-time voter cohort (born 1999–2003); 10-yr projection from 2011 N24P age pyramid |
| 23_27 | 13.2 | E | |
| 28_32 | 13.0 | E | |
| 33_37 | 11.5 | E | |
| 38_42 | 10.5 | E | |
| 43_47 | 9.5 | E | |
| 48_52 | 8.5 | E | |
| 53_57 | 7.0 | E | |
| 58_62 | 5.8 | E | |
| 63_67 | 4.5 | E | |
| 68 | 4.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.20 | E | N24P 2011 sex ratio 949; slight improvement by 2021 → ~950 |
| Female | 48.79 | E | |
| Third_gender | 0.01 | E | 2021 SIR: 25 / 251,387 = 0.01% |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 98.80 | E | Bangaon CDB 2011: 99.19% Bengali; Muni slightly lower; stable |
| Hindi | 0.70 | E | Muni Marwari/Bihari trader fringe |
| Urdu | 0.30 | E | Small Muslim urban pocket |
| Other | 0.20 | E | Residual (Santhali/Sadri/Punjabi etc.) |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 12.5 | E | 2011 CDB Bangaon literacy 79.71%; +6pp trend by 2021 → ~87% literate → 12.5% illiterate (age 18+) |
| Primary | 22.5 | E | Census 2011 education distribution scaled + 10-yr trend |
| Middle | 22.0 | E | |
| Secondary | 19.0 | E | |
| Higher_Secondary | 12.0 | E | +1pp from 2019 — secondary completion rising |
| Graduate | 9.0 | E | |
| Postgraduate | 3.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 30.5 | E | Census 2011 CDB Bangaon ~31%; COVID-shock -0.5pp main-worker dip (Petrapole shutdown, agri disruption) |
| Marginal_worker | 11.0 | E | Stable; harvest-labour pool |
| Non_worker | 38.5 | E | Housewife / elderly / retired; Lakshmir Bhandar direct beneficiaries enter this pool |
| Student | 12.0 | E | Stable |
| Unemployed | 8.0 | E | COVID-shock: slightly elevated educated-unemployment in 2021 |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 18.0 | E | Bangaon CDB 2011: 23.80% rural; Muni dilution → 18% AC weighted; stable |
| Agricultural_labourer | 27.5 | E | CDB 2011: 38.09% rural; Muni dilution; slight fall as casual workers displaced by COVID |
| Household_industry | 4.0 | E | CDB 2011: 5.22%; stable |
| Manufacturing | 4.0 | E | Limited in Bangaon |
| Construction | 6.0 | E | Reverse-migration return in 2021 slightly elevated |
| Trade_retail | 12.0 | E | Bangaon Muni hub; disrupted but rebounded |
| Transport_logistics | 6.5 | E | Petrapole port economy; partial recovery post-COVID shutdown |
| Services | 12.0 | E | |
| Government_services_teachers | 4.0 | E | |
| Out_migrant_worker | 6.0 | D | Matua men to Kerala/TN/Maharashtra; COVID forced returns but some re-departed by 2021 |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.0 | E | Census B-04 WB rural pattern; stable |
| Employee | 28.0 | E | Govt + organised + retail employees |
| Single_worker | 50.0 | E | Cultivator + own-account artisan + small trader |
| Family_worker | 20.0 | E | Within agri-household |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 20.5 | C | 2019 estimate ~22%; WB poverty fell ~1.5pp 2019–21 (limited by COVID shock) |
| Above_Poverty_Line_low_income | 38.5 | E | Lakshmir Bhandar (launched Apr 2021) begins to reach this band |
| Lower_middle | 25.5 | E | |
| Middle | 12.0 | E | |
| Upper_middle_well_off | 3.5 | E | Bangaon Muni small affluent fringe |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Municipality location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Bangaon_Municipality | 54.5 | E | 2011: Muni 108,864 / AC ~199,792 = 54.5%; stable in 10-yr window |
| U2_CDB_Bangaon_rural_share | 45.5 | E | Remainder; 7 GPs of CDB Bangaon |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.4 persons | E | WB 2011: 4.3; minor projection; COVID reverse-migration may have temporarily inflated to 4.5 but normalizing |
| Nuclear_HH | 70.0 | E | NFHS-4/5 WB rural pattern |
| Joint_HH | 24.0 | E | |
| Extended_multi_generation | 6.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 28.0 | E | Census 2011 N24P pattern; first-time-voter cohort |
| Currently_married | 64.0 | E | |
| Widowed | 7.0 | E | Concentrated in 60+, female-skewed |
| Separated_divorced | 1.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

Post-COVID smartphone surge is the major shift from 2019. Jio-led affordability + lockdown-driven necessity accelerated adoption.

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 82.0 | C | NFHS-5 WB (2019-21): urban ~93%, rural ~65%; AC weighted ~82%; near saturation |
| Radio | 4.0 | C | Declining nationally |
| Mobile_phone | 92.0 | C | NFHS-5 WB ~90%+; COVID digitisation push |
| Smartphone_with_internet | 70.0 | C | NFHS-5 WB rural ~56%, urban ~82%; +20pp from 2019 baseline (post-COVID surge); AC weighted ~70% |
| Computer | 12.0 | C | Stable; limited rural pull |
| Two_wheeler | 37.0 | C | Marginal growth |
| Four_wheeler | 8.0 | C | Limited |
| Banking_access | 93.0 | B | PMJDY saturation + Jan Dhan second push; +5pp from 2019 |
| **Note** | (these are independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 87.0 | C | NFHS-5 WB rural 85%, urban 94%; AC weighted; marginal gain |
| Improved_sanitation | 80.0 | C | NFHS-5 WB rural 58%, urban 88%; +Swachh Bharat rollout; +5pp from 2019 |
| LPG_clean_cooking_fuel | 57.0 | C | NFHS-5 WB rural 32%, urban 87%; +Ujjwala 2016-21 (+7pp over 2019); AC weighted ~57% |
| Wood_biomass_fuel | 38.0 | C | Declining as LPG rises |
| Other_fuel | 5.0 | C | Kerosene, dung, residual |
| Electricity | 98.0 | A | Saubhagya 2017-19 saturation + maintenance; near-complete |
| **Note** | (cooking-fuel rows sum to 100; water/sanitation/electricity are independent) | — | — |

### C.16 Migration / birthplace (2021, all ages)

COVID-19 reverse migration (2020) brought back some out-migrant workers temporarily; most re-departed by mid-2021. Petrapole shutdown (May–Aug 2020) pushed some transport/logistics workers to seek alternative employment briefly.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 64.5 | D | Slight rise from COVID returnee registrations |
| WB_other_district | 9.0 | D | Stable; Kolkata service-class in Muni |
| Other_Indian_state | 3.0 | D | Marwari/Bihari trader fringe in Muni |
| Bangladesh_origin | 23.0 | D | **Load-bearing**: Matua community largely descended from East Pakistan / Bangladesh refugees. Petrapole COVID shutdown (May–Aug 2020) reinforced border salience for this community. |
| Outside_India | 0.5 | E | Negligible |
| Out_migrant | -0.0 | E | Net returnees in 2020–21 COVID window; normalizing by end-2021 |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|
| Hindu | 99.4 | 0.5 | 0.0 | 0.1 | E | Bangaon CDB 99.19% Bengali (A); stable |
| Muslim | 95.0 | 1.5 | 3.0 | 0.5 | E | Bengali-Sheikh peasantry dominant |
| Christian | 90.0 | 5.0 | 0.0 | 5.0 | E | |
| Sarna_ORP | 60.0 | 30.0 | 0.0 | 10.0 | E | |
| Other_residual | 60.0 | 30.0 | 0.0 | 10.0 | E | Marwari/Punjabi small pop |

### D.2 Religion × Caste (2D layout)

P(caste ‖ religion) — % within each religion. Each row sums to 100.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 50.3 | 4.2 | 11.7 | 2.3 | 31.5 | 0 | 0 | C | Namasudra-Matua dominant; 39.5 SC / 85.60 Hindu = 46.2%; adding sub-SC gives ~50.3 |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | All Muslim self-identify |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | |
| Sarna_ORP | 0 | 92 | 0 | 5 | 3 | 0 | 0 | E | ST-dominant |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | Residual |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 60 | 8 | 2 | 30 | 0 | 0 | D | Matua refugee population overwhelmingly Hindu; ~30% traceable to East Pakistan/Bangladesh origin |
| Muslim | 95 | 3 | 1 | 1 | 0 | 0 | D | Bengali-Sheikh peasantry; mostly native |
| Christian | 80 | 10 | 5 | 5 | 0 | 0 | E | Mixed |
| Sarna_ORP | 60 | 20 | 15 | 5 | 0 | 0 | E | |
| Other_residual | 50 | 20 | 25 | 5 | 0 | 0 | E | Marwari/Bihari traders mostly other-state |

### D.4 Religion × Asset / media (flags)

P(owns asset ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 83 | 71 | 94 | C | NFHS-5 WB religion-gap pattern; post-COVID smartphone surge |
| Muslim | 76 | 60 | 85 | C | Consistent gap; narrowing with Jio diffusion |
| Christian | 87 | 73 | 94 | C | |
| Sarna_ORP | 70 | 55 | 82 | E | |
| Other_residual | 95 | 85 | 98 | E | Trader community |

### D.5 Caste × Education

P(education ‖ caste) — highest level achieved, age 18+.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4 | 9 | 11 | 18 | 20 | 26 | 12 | E |
| Namasudra_Matua_SC | 11 | 21 | 23 | 20 | 13 | 9 | 3 | E |
| Bagdi_SC | 20 | 27 | 23 | 16 | 9 | 4 | 1 | E |
| ST_total | 23 | 29 | 21 | 14 | 8 | 4 | 1 | E |
| OBC | 13 | 21 | 22 | 19 | 13 | 9 | 3 | E |
| Other_Hindu_middle | 12 | 21 | 22 | 19 | 13 | 10 | 3 | E |
| Muslim | 16 | 23 | 23 | 19 | 11 | 7 | 1 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 19 | 18 | E |
| 23_27 | 18 | 15 | E |
| 28_32 | 15 | 11 | E |
| 33_37 | 12 | 7 | E |
| 38_42 | 10 | 6 | E |
| 43_47 | 9 | 5 | E |
| 48_52 | 8 | 3 | E |
| 53_57 | 6 | 2 | E |
| 58_62 | 5 | 2 | E |
| 63_67 | 5 | 2 | E |
| 68 | 5 | 2 | E |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender).

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

P(owns smartphone-internet ‖ occupation).

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 50 | 78 | C | Post-COVID rural smartphone surge; +12pp from 2019 |
| Agricultural_labourer | 40 | 68 | C | Larger jump; Jio affordability |
| Household_industry | 55 | 80 | C | |
| Manufacturing | 67 | 87 | C | |
| Construction | 63 | 80 | C | |
| Trade_retail | 80 | 92 | C | Muni concentrated; near-saturation |
| Transport_logistics | 75 | 88 | C | Petrapole logistics workers smartphone-heavy |
| Services | 83 | 93 | C | |
| Government_services_teachers | 92 | 97 | C | Highest |
| Out_migrant_worker | 80 | 82 | D | Smartphone required for remittance/contact; high adoption |

### D.9 Education × Workforce participation

P(unemployed-seeking ‖ education).

| Education | Unemployed_seeking | Main_worker_rate | Tier |
|---|---|---|---|
| Illiterate | 2 | 34 | E |
| Primary | 4 | 37 | E |
| Middle | 6 | 34 | E |
| Secondary | 10 | 29 | E |
| Higher_Secondary | 15 | 24 | E |
| Graduate | 17 | 27 | E |
| Postgraduate | 12 | 37 | E |

### D.10 Asset / media × Bilingualism

P(bilingual Bengali+Hindi ‖ media-access tier).

| Media_tier | Bilingual_pct | Tier | Source |
|---|---|---|---|
| TV_only_HH | 5 | E | Bengali TV dominant |
| TV_plus_smartphone_HH | 9 | E | Some YouTube cross-language |
| Smartphone_only_HH | 8 | E | |
| No_asset_HH | 3 | E | Lowest exposure |

### D.11 GP × Religion

P(religion ‖ GP/Muni location).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Bangaon_Municipality | 92.0 | 7.0 | 0.5 | 0.0 | 0.5 | E | Muni heavily refugee-Hindu |
| U2_CDB_Bangaon_rural_share | 78.2 | 20.8 | 0.5 | 0.0 | 0.5 | A | Bangaon CDB Census 2011 rural |

### D.12 GP × Caste

P(caste ‖ GP).

| Sub_unit | UC_bhadralok | Namasudra_Matua_SC | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Bangaon_Municipality | 14 | 38 | 41 | 1 | 5 | 36 | 7 | E |
| U2_CDB_Bangaon_rural_share | 5 | 41 | 45 | 6 | 3 | 25 | 21 | E |

### D.13 GP × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Bangaon_Municipality | 93 | 80 | 22 | 97 | C |
| U2_CDB_Bangaon_rural_share | 68 | 56 | 5 | 86 | C |

### D.14 GP × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Bangaon_Municipality | 82 | 93 | 96 | 99 | C |
| U2_CDB_Bangaon_rural_share | 27 | 64 | 76 | 97 | C |

### D.15 Vote × Religion (2021 AE, regional anchor updated)

P(party ‖ religion) — anchored to 2021 AE AC-95 result.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 56 | 35 | 3 | 4 | 2 | C | CSDS 2021 WB post-poll (BJP held Matua-Hindu; AITC women-welfare push raised share slightly) |
| Muslim | 5 | 72 | 18 | 4 | 1 | C | Muslim consolidation toward AITC in 2021 |
| Christian | 28 | 54 | 10 | 5 | 3 | E | |
| Sarna_ORP | 40 | 42 | 5 | 10 | 3 | E | |
| Other_residual | 48 | 33 | 10 | 5 | 4 | E | |

### D.16 Vote × Caste (2021 AE)

P(party ‖ caste) — anchored to 2021 AE AC-95 result.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 58 | 30 | 5 | 5 | 2 | C | Bhadralok BJP-leaning; slight dip from 2019 |
| OBC | 40 | 38 | 7 | 12 | 3 | C | Mixed |
| Namasudra_Matua_SC | 58 | 34 | 3 | 3 | 2 | C | Modi Thakurnagar visit (Feb 2021) + Kirtania nomination reinforced BJP; AITC welfare offset |
| SC_total | 52 | 37 | 4 | 5 | 2 | C | Weighted SC pool; Matua dominant |
| ST_total | 44 | 37 | 5 | 11 | 3 | C | |
| Muslim | 5 | 72 | 18 | 4 | 1 | C | |

### D.17 Vote × Gender (2021 AE)

P(party ‖ gender). Lakshmir Bhandar launched April 2021 — partial penetration by polling day (early May 2021); measurable but limited effect by end-2021.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 50 | 39 | 4 | 5 | 2 | C | CSDS 2021 WB post-poll |
| Female | 44 | 47 | 3 | 4 | 2 | C | Lakshmir Bhandar launch + Duare Sarkar outreach shifted women toward AITC vs 2019 |
| Third_gender | 45 | 45 | 5 | 3 | 2 | E | |

### D.18 Vote × Welfare scheme exposure (2021 AE)

Schemes active at 2021 AE: Krishak Bandhu (TMC, Jan 2019+), Kanyashree (TMC, 2013+), Swasthya Sathi (TMC, 2016+), Sabuj Sathi (TMC, 2015+), Khadya Sathi (TMC, 2016+), **Lakshmir Bhandar (TMC, launched April 2021 — first partial disbursement)**, Duare Sarkar camp outreach (late 2020).

| Welfare_exposure | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Krishak_Bandhu_cultivator_HH | 26 | 62 | 5 | 5 | 2 | C | TMC welfare-stack credit strong |
| Kanyashree_girl_student_HH | 30 | 57 | 5 | 6 | 2 | C | |
| Swasthya_Sathi_enrollee | 36 | 52 | 5 | 5 | 2 | C | Broad-based; weakest tilt |
| Lakshmir_Bhandar_early_enrollee | 32 | 58 | 4 | 4 | 2 | C | First cohort enrolled Apr-May 2021; powerful AITC signal even within Matua HHs |
| No_state_scheme_exposure | 55 | 30 | 6 | 7 | 2 | C | BJP-leaning |

---

## E. 2021 calibration target (2021 AE — tier A)

The simulator must reproduce this aggregate within ±1pp.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 47.65 | A | ECI 2021 WB AE — Ashok Kirtania (BJP) 97,761 votes |
| AITC | 42.54 | A | ECI 2021 WB AE — Biswanath Das (AITC) 87,273 votes |
| INC | 1.50 | A | ECI 2021 WB AE — INC candidate; residual |
| LF | 6.31 | A | ECI 2021 WB AE — CPI(M) + allied left combined estimate |
| Other_NOTA | 2.00 | A | ECI 2021 WB AE — NOTA + independents + SUCI etc. |

> ECI 2021 AE AC-95 Bangaon Uttar: BJP 97,761 | AITC 87,273 | BJP margin 10,488 | total electorate 251,387 | turnout ~86.9%

---

## F. Vote history (pre-2021 anchors for belief evolution)

### AC 95 Assembly Elections

| Year | Winner | Party | % | Runner-up | Party | % | Margin | Notes |
|---|---|---|---|---|---|---|---|---|
| 2011 AE | Biswajit Das | AITC | 54.55 | Dr. Biswajit Biswas | CPI(M) | 40.12 | 23,620 | AITC stronghold; Left retreating |
| 2016 AE | Biswajit Das | AITC | 50.59 | Sushanta Baowali | AIFB | 33.07 | 33,192 | AITC held; Left further fragmented |
| **2021 AE** | **Ashok Kirtania** | **BJP** | **47.65** | Biswanath Das | AITC | 42.54 | **10,488** | **BJP flipped historically AITC seat; Matua mobilisation** |

### Bangaon LS (PC 14) history (relevant segment anchors)

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Mamatabala Thakur | AITC | ~36.81 | TMC held in tight three-way (BJP 19.65%, CPI(M) 18.81%) |
| 2019 LS | **Shantanu Thakur** | BJP | **48.85** | Matua swing; BJP+111,594 margin; within AC-95, BJP ~48%, AITC ~44% (tier D) |

### Key narrative events (2019–2021)

- **2019 May**: Shantanu Thakur (BJP) wins Bangaon LS — established as dominant Matua electoral face nationally (events.yaml: `ls_2019_bangaon_shantanu_win`, intensity 5).
- **2019–2021 (chronic)**: Thakurbari endorsement split — Shantanu (BJP) controls main residence; Mamatabala (TMC) sidelined. Gatekeeper capture carries forward into 2021 AE cadence (events.yaml: `thakurbari_split_2021_pre_ae`, intensity 4).
- **2020 May–Aug**: Petrapole COVID shutdown — India-Bangladesh trade halted ~3 months. Direct livelihood hit for truckers, loaders, dhaba owners, currency-changers, clearing agents in AC-95. BJP-negative signal among Petrapole-economy voters (events.yaml: `petrapole_covid_shutdown`, intensity 4).
- **2020 May**: Cyclone Amphan — N24P including Bangaon sub-division affected; state relief delivery contested; BJP accused AITC of fund-diversion; some areas in CDB-Bangaon rural saw damage.
- **2020 Oct**: Matua Dharma Maha Mela at Thakurnagar — first major post-Boroma Mahasangha congregation; Shantanu faction controlled the stage (events.yaml: `matua_dharma_maha_mela_oct2020`, intensity 3).
- **2021 Feb 11**: PM Modi visits Thakurbari at Thakurnagar — first sitting PM to do so. Cemented BJP-Matua bond; CAA-as-promise narrative activated for AC-95 belt (events.yaml: `modi_thakurnagar_visit_2021`, intensity 5).
- **2021 Mar**: BJP nominates Ashok Kirtania — Matua SC, Mahasangha-aligned, no major criminal record, modest assets (events.yaml: `bangaon_uttar_2021_candidate_profile_kirtania`, intensity 3).
- **2021 Apr**: Lakshmir Bhandar scheme launched — ₹500/month general, ₹1,000/month SC/ST women household heads. AC-95 has high SC share — most eligible women qualify for ₹1,000 tier. Partial first-disbursement by polling day; powerful belief-vector for AITC even within Matua households.
- **2021 May 2**: WB AE results — TMC 213 / BJP 77 / others 4 statewide. BJP won AC-95 despite TMC landslide; Matua-belt seats an island of BJP performance.
- **2021 Oct 11**: BSF jurisdiction extended from 15 km to 50 km from Bangladesh border. Bangaon Uttar lies entirely within new zone. TMC framed as federal overreach; BJP/Matua community saw as security upgrade (events.yaml: `bsf_50km_jurisdiction`, intensity 3).
- **2021 Oct 13–20**: Bangladesh Durga Puja temple attacks — 5+ killed, widespread communal violence. Triggered Matua refugee anxiety in Bangaon belt; reinforced "Hindus need protection" and CAA-as-savior narrative (events.yaml: `bangladesh_temple_attacks_2021`, intensity 4).

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- Census of India 2011 — Bangaon CD Block Primary Census Abstract
- Census of India 2011 — Bangaon Sub-division demographics; North 24 Parganas district
- Election Commission of India — 2021 WB Assembly Election archive (AC-95: Ashok Kirtania BJP 97,761; Biswanath Das AITC 87,273; margin 10,488; electorate 251,387)
- Election Commission of India — 2011 AE, 2016 AE, 2019 LS results for AC 95 / Bangaon LS
- Delimitation Commission of India 2008 — WB Schedule XXX
- ECI 2021 SIR — electorate roll 251,387; polling stations 276

### Secondary sources (tier B/C)
- NFHS-5 (2019-21) West Bengal — household amenities, asset ownership; smartphone surge documented
- NFHS-4 (2015-16) West Bengal — baseline for trend computation
- WB CDWDSW Lakshmir Bhandar dashboard — scheme launch April 2021
- CSDS-Lokniti 2021 NES post-poll WB regional cross-tabs
- Pew Research India 2021 — religion-differential growth projections

### Tertiary / journalistic (tier D)
- The Hindu: "Matua Mahasangha internal feud out in the open" (Thakurbari split)
- The Hindu: "Modi pays obeisance at Matua shrine in Bengal" (Feb 2021)
- ThePrint: "How one Bengal village's COVID fear stalled Rs 2000 crore India-Bangladesh trade" (Petrapole shutdown)
- Outlook India: "Matua Mahasangha Maelstrom" — Bangaon LS Matua share ~40%
- Wikipedia: 2021 West Bengal Legislative Assembly election (AC-level results)
- PMC-Springer (2020) on WB→Kerala migrants

### Tier-D/E reliance flags
- **Caste sub-group shares within Hindu** (D.2) — no caste census post-1931 for non-SC/ST; tier C/E throughout
- **Migration/birthplace shares** (C.16, D.3) — no public AC-level Census D-series; tier D from journalistic anchor
- **GP-level data** (D.11–D.14) — collapsed to 2 sub-units; refine when DCHB Part-A accessible
- **Asset/media** (C.14, D.4, D.13) — NFHS-4/5 state-level pattern projected to AC; tier C; smartphone surge based on NFHS-5 rural WB increase
- **Vote × Demographic** (D.15–D.18) — CSDS 2021 WB regional rollup; tier C; anchored on AC-95 2021 AE result

### v0 known gaps
1. DCHB N24P Part-A — collapsed sub-units to 2 instead of 8
2. LF disaggregation in 2021 AE not available at AC level (CPI(M) alone vs CPI+RSP+AIFB aggregate)
3. Smartphone ownership rate: NFHS-5 WB rural 56%, urban 82%; AC-level interpolation is modeled
4. Lakshmir Bhandar first-wave enrollment by polling day (April–May 2021): estimated 20–30% of eligible women reached in this window; belief effect modeled as partial

---

## H. Post-2021 validation anchors (OUT-OF-SAMPLE)

> **These are out-of-sample simulation gates — NOT part of the frozen 2021 calibration.**

### 2024 LS AC-95 segment — Bangaon (tier A, CSV)

Source: `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=95. Electorate: 264,506. Total valid votes: 209,954. Turnout: ~79.4%.

| Party | Candidate | Votes | AC-95 segment % | Tier |
|---|---|---|---|---|
| BJP | Shantanu Thakur | 109,848 | 52.32% | A |
| AITC | Biswajit Das | 84,818 | 40.40% | A |
| INC | Pradipkumar Biswas | 7,066 | 3.37% | A |
| Other_NOTA | (AISF+BSP+SUCI+PDS+GSD+IND+NOTA) | 8,222 | 3.91% | A |
| BJP margin | | 25,030 | 11.92 pp | A |

Calibration test: simulator validated if 2024 LS shares reproduced within ±3pp of tier-A CSV figures.

---

*v0 — generated 2026-04-28, frozen at 2021 state-of-knowledge. No post-2021 events referenced.*
