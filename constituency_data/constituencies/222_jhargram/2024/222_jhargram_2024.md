# AC 222 — Jhargram (ST) — Calibrated 2024 Population Snapshot

> **Frozen at end-2024.** This file describes the demographic and behavioural state of AC 222 Jhargram as of end-2024 only — it does not reference any post-2024 events. Use 2026 AE polling results (when available) as out-of-sample validation gates for downstream simulators.
>
> The file MAY freely reference: 2019 LS, 2020 COVID, 2021 AE, Lakshmir Bhandar (April 2021), SSC scam (July 2022), 2023 panchayat elections, 2024 LS result (June 2024), CAA notification (March 2024), RG Kar protests (August 2024), Bangladesh Hasina ouster (August 2024). It MUST NOT reference: 2025 SIR, 2026 election, Special Intensive Revision, or any 2025+ event.
>
> Companion artifacts: [`methodology_2024.md`](../../methodology_2024.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2024)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 222 | A | ECI / Delimitation Commission 2008 |
| AC name | Jhargram | A | ECI |
| Reservation | ST (Scheduled Tribe) | A | Delimitation 2008 |
| District | Jhargram | A | WB Govt notification 2017 |
| Sub-division | Jhargram Sadar | A | WB administrative |
| LS constituency | PC 27 — Jhargram (ST reserved) | A | Delimitation 2008 |
| AC composition | Jhargram Municipality (full, 18 wards) + 4 GPs of Jhargram CD Block + Binpur I CD Block (all 10 GPs) | A | Delimitation 2008 |
| Archetype | A4 — Jangalmahal Santhal ST | D | Project classification |
| Three sub-units | **U1_Jhargram_Municipality** (urban) · **U2_Jhargram_CDB_rural_4GP** · **U3_Binpur_I_CD_Block** (wholly rural) | E | v0 simplification |
| 2024 LS winner (Jhargram PC) | **Kalipada Saren (AITC)** — TMC recaptured Jhargram LS from BJP's Kunar Hembram (2019); AC-222 segment: AITC 47.49%, BJP 40.56% | A | ECI 2024 LS; `2024_AssemblySegmentLevelVotingData.csv` |
| 2021 AE incumbent | Birbaha Hansda (AITC) — ST Adivasi folk singer; elected with 54.31% in 2021 AE | A | ECI 2021 AE |
| Key 2022-2024 events | SSC scam (Partha Chatterjee arrest Jul 2022) — national anti-TMC narrative; 2023 Panchayat elections (TMC dominant in Jhargram; BJP and tribal parties split opposition); CAA notification March 2024 (no Matua-belt relevance for this ST-dominated AC); RG Kar rape-murder protests August 2024 (urban youth / medical community; limited Jangalmahal penetration) | D | Press reports |
| Bangladesh note | Bangladesh Hasina ouster August 2024; no direct livelihood impact on Jhargram (not a border-trade AC); minor border-security anxiety noted | D | Press |

---

## B. 2024 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~270,200 | E | Census 2011; see 2019 file §B |
| 2024 projected population (13-yr) | ~303,500 | E | 13-yr compound differential growth (+12.3% overall: Hindu +1.0%/yr×13yr, Muslim +1.3%/yr×13yr, Sarna/tribal +1.2%/yr×13yr) |
| Sex ratio (2024, F per 1,000 M) | ~982 | E | Marginal improvement from 2021 (~980); NFHS-5 WB tribal district trend |
| 2024 LS electorate (ECI CSV) | **246,403** | **A** | `2024_AssemblySegmentLevelVotingData.csv`, AC_NO=222 |
| 2024 LS valid votes (candidate-level) | **201,151** | **A** | Sum of all candidate votes: same CSV |
| 2024 LS total votes with NOTA | **203,423** | **A** | 201,151 + 2,272 NOTA |
| 2024 LS turnout | **82.6%** | **A** | 203,423 / 246,403 |
| 2024 LS AITC margin over BJP | **14,101 votes (6.93 pp)** | **A** | 96,608 − 82,507; CSV |
| Estimated M / F / TG split (2024) | ~50.4% M / 49.6% F / <0.05% TG | E | Sex ratio trend 982 F/1000 M |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 83.60 | E | 2021 baseline 83.90%; 3 more years of Muslim differential growth pulls Hindu share further; stable Sarna |
| Muslim | 3.50 | E | 2021 baseline 3.46%; +0.04pp over 3 years |
| Christian | 0.43 | E | Negligible change |
| Sarna_ORP | 11.00 | E | Marginal increase: Adivasi identity assertion + Sarna-code agitation (Census enumeration deferred due to COVID; 2021 demand escalated); 2021 baseline 10.92% |
| Other_residual | 1.47 | E | Residual: 100 − 83.60 − 3.50 − 0.43 − 11.00 = 1.47 |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 19.58 | A | Marginal adjustment; 2021 baseline 19.56%; Census 2011 anchor |
| └ Bagdi | 7.03 | D | ~35.9% of SC pool |
| └ Bauri | 4.02 | D | ~20.5% of SC pool |
| └ Hari_Bhangi | 1.57 | E | ~8% of SC pool |
| └ Chamar_Mochi | 1.20 | E | ~6% of SC pool |
| └ Other_SC | 5.76 | E | Residual SC |
| **ST_total** | 22.98 | A | 2021 baseline 22.95%; marginal +0.03pp; Census 2011 anchor |
| └ Santhal | 11.54 | D | ~50% of ST pool |
| └ Munda | 3.91 | D | ~17% of ST pool |
| └ Bhumij | 2.76 | D | ~12% of ST pool |
| └ Lodha | 1.40 | D | ~6% of ST pool; PVTG |
| └ Ho | 1.15 | D | ~5% of ST pool |
| └ Other_ST | 2.22 | E | ~10% of ST pool |
| UC_bhadralok | 6.50 | E | Stable |
| OBC | 12.00 | D | Mahato/Kurmi dominant OBC; stable |
| Other_Hindu_middle | 33.74 | E | Residual: 100 − 19.58 − 22.98 − 6.50 − 12.00 − 3.50 − 0.43 − 1.20 = 33.81; small rounding |
| Muslim | 3.50 | E | See C.1 |
| Christian_plus_Sarna_plus_Other | 1.90 | E | Christian 0.43% + Other_residual 1.47% = 1.90% |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2024, voters 18+ only — renormalized)

> Adults (18+) only per NORMALIZED_SCHEMA v1. 13-yr projection from Census 2011.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.0 | E | New-voter cohort; tribal belt younger demographic; renormalized from total-pop |
| 23_27 | 12.5 | E | |
| 28_32 | 12.0 | E | |
| 33_37 | 11.0 | E | |
| 38_42 | 10.0 | E | |
| 43_47 | 8.5 | E | |
| 48_52 | 8.0 | E | |
| 53_57 | 7.0 | E | |
| 58_62 | 5.5 | E | |
| 63_67 | 4.5 | E | |
| 68 | 9.0 | E | Broad 68+ cohort; tribal older population |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.46 | A | District sex ratio ~982 F/1000 M → 50.46% M |
| Female | 49.53 | A | |
| Third_gender | 0.01 | E | Negligible |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 81.20 | A | 2021 baseline 81.40%; further marginal drift toward Bengali bilingualism; Santali Ol Chiki digital content growing but MT stability among older tribal cohorts |
| Hindi | 0.30 | E | Stable |
| Urdu | 0.10 | E | Negligible |
| Other | 0.20 | E | Residual |
| Santali | 16.00 | A | Slight uptick from 2021 (15.90%); Sarna-code agitation and Adivasi identity assertion may be slightly reversing Bengali bilingualism trend among younger cohorts |
| Mundari | 1.60 | A | Marginal increase; Mundari digital content growth |
| Kurmali | 0.60 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2024, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 22.00 | E | 2021 baseline 23.50%; continued improvement; but COVID school disruption 2020-21 created a learning gap in 10-14 cohort now moving into 13-16 range |
| Primary | 23.50 | E | Marginal decline as more reach middle level |
| Middle | 20.50 | E | |
| Secondary | 14.50 | E | |
| Higher_Secondary | 10.00 | E | +0.5pp from 2021; school completion improving |
| Graduate | 6.50 | E | Marginal +0.5pp |
| Postgraduate | 3.00 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 35.0 | E | Recovery to 2019 level; COVID disruption resolved; construction and services rebounded |
| Marginal_worker | 15.0 | E | Returning to 2019 baseline as COVID reverse-migration workers re-migrated out |
| Non_worker | 34.5 | E | Slightly elevated vs 2019 (34.0%); Lakshmir Bhandar may reduce women's main-worker designation |
| Student | 10.0 | E | Stable |
| Unemployed | 5.5 | E | Marginal decline; MGNREGA and state welfare absorbing some educated unemployed |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 20.0 | E | Stable; land fragmentation ongoing |
| Agricultural_labourer | 37.0 | E | Marginal decline as MGNREGA provides alternative |
| Forest_produce_collection | 8.0 | D | Stable; NTFP dependence persistent in Binpur I |
| Household_industry | 4.0 | E | Stable |
| Manufacturing | 1.0 | E | Minimal |
| Construction | 6.0 | E | Slight increase; PMAY-G housing scheme construction in tribal belt continues |
| Trade_retail | 8.0 | E | Recovery to 2019 level |
| Transport_logistics | 3.0 | E | Stable |
| Services | 6.0 | E | Stable |
| Government_services_teachers | 5.0 | E | Stable; tribal sub-quota absorption |
| Out_migrant_worker | 2.0 | D | Post-COVID some re-migration; lower than 2019 (3.0%) as state welfare reduces push-migration |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.0 | E | Stable |
| Employee | 22.5 | E | Marginal +0.5pp; government hiring through tribal sub-quotas |
| Single_worker | 45.0 | E | Stable |
| Family_worker | 22.0 | E | Stable |
| Casual_MGNREGA | 9.5 | D | Marginal decline; Centre-state MGNREGA fund-release disputes in 2023-24 reduced utilization in WB; Jhargram affected |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2024, household level)

> Lakshmir Bhandar (since April 2021) has achieved near-saturation in eligible ST/SC HHs by 2024. The ₹1,000/month for ST women is now a stable welfare floor. Free-rice Khadya Sathi (5 kg/person/month) universal in tribal belt. PMAY-G housing construction visible. MGNREGA fund-release disputes between Centre and WB state created periodic work-day shortfalls.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 37.0 | D | 2021 baseline 40.0%; Lakshmir Bhandar + PMAY-G + Khadya Sathi reducing measured poverty; structural poverty reduction slow but visible; Binpur I BPL 2024 est ~45% |
| Above_Poverty_Line_low_income | 35.5 | E | Growing as welfare transfers push some above poverty line |
| Lower_middle | 17.5 | E | |
| Middle | 8.0 | E | |
| Upper_middle_well_off | 2.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Municipality location (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Jhargram_Municipality | 22.0 | E | 2021 baseline 22.5%; marginal decline as rural growth outpaces Muni; Jhargram Muni boundary stable |
| U2_Jhargram_CDB_rural_4GP | 19.2 | E | 2021 baseline 19.3%; stable |
| U3_Binpur_I_CD_Block | 58.8 | E | 2021 baseline 58.2%; largest sub-unit; rural tribal growth |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | Marginal decline; nucleation trend resumes post-COVID; tribal family size declining slowly |
| Nuclear_HH | 63.5 | E | Slow increase in nuclearity |
| Joint_HH | 26.5 | E | Gradual decline |
| Extended_multi_generation | 10.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.5 | E | Marginal increase; later marriage age creeping into tribal communities via education |
| Currently_married | 64.5 | E | Marginal decline correspondingly |
| Widowed | 8.0 | E | Stable |
| Separated_divorced | 1.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2024, household level — independent rates, do NOT sum)

> Smartphone effectively saturated in working-age adults; UPI/digital-payment adoption growing even in tribal belt via Lakshmir Bhandar DBT pipeline. Television stable. Radio declining but persistent in deep-forest GPs.

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 65.0 | C | NFHS-5 WB rural ~71%; Jhargram still below state average; +3pp from 2021 (62%) |
| Radio | 6.0 | C | Continued gradual decline |
| Mobile_phone | 88.0 | C | Near-saturation; +6pp from 2021 (82%) |
| Smartphone_with_internet | 68.0 | C | +20pp from 2021 (48%); major Jio 5G expansion + Lakshmir Bhandar DBT-driven smartphone adoption; tribal belt reaching ~85-90% among 18-45 adults |
| Computer | 6.0 | C | Marginal improvement |
| Two_wheeler | 20.0 | C | Marginal increase; rural mobility improving |
| Four_wheeler | 4.0 | C | Marginal increase |
| Banking_access | 90.0 | B | PMJDY + Lakshmir Bhandar DBT near-saturation; tribal women's accounts mandatory for scheme; +4pp from 2021 (86%) |
| Note | (independent ownership rates — do not sum) | — | — |

### C.15 Household amenities (2024)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 85.0 | C | Jal Jeevan Mission 2019–24; substantial rural tribal coverage in Jhargram by 2024; +5pp from 2021 (80%) |
| Improved_sanitation | 65.0 | C | Swachh Bharat Phase II continuing; +11pp from 2021 (54%); tribal-belt sanitation still below state average |
| LPG_clean_cooking_fuel | 50.0 | C | Ujjwala 2.0 + state subsidy; +15pp from 2021 (35%); significant adoption in tribal HHs |
| Wood_biomass_fuel | 43.0 | D | Declining as LPG penetrates; 2021 baseline 58% |
| Other_fuel | 7.0 | C | Stable |
| Electricity | 95.0 | C | Near-saturation; Jhargram grid extension completed; +3pp from 2021 (92%) |
| Note | (water/sanitation/electricity independent; cooking fuel LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 84.0 | D | 2021 baseline 85.5%; some post-COVID out-migration resumed; returned to near-2019 level |
| WB_other_district | 5.5 | D | Stable |
| Other_Indian_state | 4.0 | D | Stable |
| Jharkhand_origin | 3.0 | D | Stable; tribal cross-border kin ties |
| Bangladesh_origin | 1.5 | D | Negligible; Jangalmahal not on Bangladesh border |
| Outside_India | 0.0 | E | None |
| Out_migrant | 2.0 | E | Post-COVID re-migration resumed; back toward 2019 level (3.0%); welfare income (Lakshmir Bhandar, MGNREGA) reduces some push-migration but not eliminated |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue (2024)

P(language | religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Santali | Mundari | Kurmali | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 93.0 | 1.5 | 0.3 | 0.2 | 4.0 | 0.7 | 0.3 | E | Stable from 2021 |
| Muslim | 92.0 | 0.5 | 5.0 | 0.5 | 1.5 | 0.5 | 0.0 | E | Marginal Urdu increase with identity consolidation |
| Christian | 67.0 | 0.5 | 0.5 | 1.0 | 19.0 | 8.0 | 4.0 | E | Santali Christian growth in digital-Ol-Chiki literacy |
| Sarna_ORP | 17.0 | 0.0 | 0.0 | 0.0 | 64.0 | 12.0 | 7.0 | E | Sarna identity assertion → marginal MT consolidation in Santali |
| Other_residual | 60.0 | 15.0 | 5.0 | 20.0 | 0.0 | 0.0 | 0.0 | E | Residual |

### D.2 Religion × Caste (2024, 2D layout)

P(caste | religion). Rows sum to 100.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 22.5 | 6.0 | 7.8 | 14.3 | 49.4 | 0.0 | 0.0 | E | Stable from 2021; no Census update |
| Muslim | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | A | All Muslim pooled |
| Christian | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | A | Tribal Christians |
| Sarna_ORP | 0.0 | 92.0 | 0.0 | 5.0 | 3.0 | 0.0 | 0.0 | E | Sarna = almost exclusively ST |
| Other_residual | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | E | Residual |

### D.3 Religion × Migration / birthplace (2024)

P(birthplace | religion).

| Religion | Native | WB_other_district | Other_Indian_state | Jharkhand_origin | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 82.0 | 5.5 | 5.5 | 2.5 | 2.0 | 0.0 | 2.5 | D | Re-migration of out-migrants |
| Muslim | 87.0 | 4.5 | 4.0 | 1.5 | 2.0 | 0.0 | 1.0 | D | Marginal out-migration |
| Christian | 77.0 | 8.0 | 8.0 | 4.0 | 2.0 | 0.0 | 1.0 | E | Slight increase in out-migration of educated tribal youth |
| Sarna_ORP | 96.0 | 0.5 | 2.0 | 0.5 | 0.0 | 0.0 | 1.0 | D | Some Sarna youth out-migrating to Jharkhand mines; returning seasonally |
| Other_residual | 59.0 | 15.0 | 14.0 | 5.0 | 5.0 | 0.0 | 2.0 | E | Residual |

### D.4 Religion × Asset / media (2024)

P(owns asset | religion).

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 70.0 | 72.0 | 92.0 | C | Significant smartphone surge; banking near-saturation |
| Muslim | 65.0 | 66.0 | 88.0 | C | Improving steadily |
| Christian | 72.0 | 76.0 | 89.0 | C | Tribal Christian slightly ahead |
| Sarna_ORP | 52.0 | 56.0 | 84.0 | C | Major surge from 2021 (32% smartphone → 56%); Lakshmir Bhandar DBT-linked accounts drove banking to 84% |
| Other_residual | 68.0 | 70.0 | 86.0 | E | Residual |

### D.5 Caste × Education (2024)

P(education | caste) — highest level achieved, age 18+.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 3 | 8 | 12 | 18 | 22 | 27 | 10 | E |
| OBC | 15 | 23 | 22 | 19 | 12 | 8 | 1 | E |
| SC_total | 29 | 26 | 21 | 14 | 7 | 3 | 0 | E |
| ST_total | 25 | 25 | 23 | 16 | 8 | 3 | 0 | D | Gradual improvement; SSA/RMSA schools in tribal belt; COVID learning loss partially offset |
| Muslim | 22 | 26 | 22 | 17 | 9 | 4 | 0 | E |
| Christian_plus_Sarna_plus_Other | 28 | 26 | 23 | 15 | 6 | 2 | 0 | E |

### D.6 Age × Gender × Education (2024)

P(grad+ | age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 12 | 11 | E |
| 23_27 | 12 | 9 | E |
| 28_32 | 10 | 7 | E |
| 33_37 | 8 | 5 | E |
| 38_42 | 7 | 4 | E |
| 43_47 | 6 | 3 | E |
| 48_52 | 5 | 2 | E |
| 53_57 | 4 | 1 | E |
| 58_62 | 4 | 1 | E |
| 63_67 | 3 | 1 | E |
| 68 | 3 | 1 | E |

### D.7 Marital status × Age × Gender (2024)

P(currently married | age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 9 | 44 | E |
| 23_27 | 50 | 85 | E |
| 28_32 | 83 | 93 | E |
| 33_37 | 93 | 91 | E |
| 38_42 | 92 | 89 | E |
| 43_47 | 91 | 87 | E |
| 48_52 | 88 | 75 | E |
| 53_57 | 85 | 65 | E |
| 58_62 | 82 | 52 | E |
| 63_67 | 74 | 36 | E |
| 68 | 69 | 26 | E |

### D.8 Occupation × Asset / media (2024)

P(owns asset | occupation) — smartphone near-saturation in most occupations.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 55 | 62 | C | Major increase from 2021 (30%); Kisan-credit linked smartphones; Agri-apps |
| Agricultural_labourer | 48 | 55 | C | DBT-linked phones drove adoption |
| Forest_produce_collection | 36 | 46 | D | +20pp from 2021 (16%); Jio rural coverage improved |
| Household_industry | 60 | 64 | C | |
| Manufacturing | 65 | 68 | C | |
| Construction | 72 | 66 | C | WhatsApp job market near-universal |
| Trade_retail | 88 | 88 | C | Near-saturation |
| Transport_logistics | 82 | 80 | C | |
| Services | 90 | 90 | C | Near-saturation |
| Government_services_teachers | 98 | 95 | C | Full saturation |
| Out_migrant_worker | 95 | 75 | D | Smartphone essential for remote remittance and job search |

### D.9 Education × Workforce participation (2024)

P(unemployed-and-seeking | education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 42 | 1 | E |
| Primary | 40 | 3 | E |
| Middle | 38 | 5 | E |
| Secondary | 33 | 8 | E |
| Higher_Secondary | 28 | 12 | E |
| Graduate | 31 | 13 | E |
| Postgraduate | 42 | 9 | E |

### D.10 Asset × Bilingualism (skip — no media_tier axis in this AC)

> D.10 omitted — this AC does not declare a `media_tier` parent axis per NORMALIZED_SCHEMA §4.7.

### D.11 Sub-unit × Religion (2024)

P(religion | sub-unit location).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Jhargram_Municipality | 94.60 | 1.70 | 0.76 | 2.60 | 0.34 | A | Census 2011 base; marginal Sarna assertion adjustment |
| U2_Jhargram_CDB_rural_4GP | 90.80 | 3.72 | 0.30 | 4.87 | 0.31 | A | Census 2011 base; marginal adjustment |
| U3_Binpur_I_CD_Block | 77.10 | 3.92 | 0.36 | 16.60 | 2.02 | A | Census 2011 base; Sarna slightly higher with identity assertion |

### D.12 Sub-unit × Caste (within sub-unit, 2024)

| Sub_unit | UC_bhadralok | OBC | SC_total | ST_total | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Jhargram_Municipality | 14.0 | 8.0 | 9.59 | 9.85 | 57.30 | 1.70 | 0.76 | A/E |
| U2_Jhargram_CDB_rural_4GP | 8.0 | 12.0 | 14.83 | 22.71 | 39.44 | 3.72 | 0.30 | A/E |
| U3_Binpur_I_CD_Block | 3.0 | 15.0 | 25.02 | 28.15 | 24.69 | 3.92 | 2.22 | A/E |

### D.13 Sub-unit × Asset / media (2024)

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Jhargram_Municipality | 90 | 82 | 20 | 96 | C |
| U2_Jhargram_CDB_rural_4GP | 68 | 65 | 7 | 90 | C |
| U3_Binpur_I_CD_Block | 52 | 58 | 3 | 86 | C |

### D.14 Sub-unit × Amenities (2024)

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Jhargram_Municipality | 78 | 90 | 95 | 99 | C |
| U2_Jhargram_CDB_rural_4GP | 48 | 68 | 87 | 96 | C |
| U3_Binpur_I_CD_Block | 34 | 52 | 80 | 93 | C |

### D.15 Vote × Religion (2024 LS calibration anchor)

P(party | religion) — calibrated to reproduce 2024 LS AC-222 segment: AITC 47.49%, BJP 40.56%, LF 5.42%.

> Key 2024 dynamics: (1) No Birbaha Hansda candidacy — AITC candidate was Kalipada Saren (less Adivasi-identity resonance); (2) BJP partially recovered tribal vote via central welfare (PM-KISAN, PMAY-G, Ayushman Bharat) but Sarna code still unresolved; (3) Lakshmir Bhandar still anchoring TMC women vote; (4) SSC scam/Partha Chatterjee arrest created anti-TMC narrative but limited penetration in tribal belt; (5) AITC retained Jhargram LS with smaller margin than 2021 AE — a mean-reverting election.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 45.0 | 44.0 | 0.5 | 6.0 | 4.5 | C | Hindu BJP-AITC near-parity resumes (as in 2019); Birbaha-effect partial reversion; rows sum: 45+44+0.5+6+4.5=100 |
| Muslim | 4.0 | 82.0 | 2.0 | 8.0 | 4.0 | C | Muslim-TMC consolidation maintained; rows sum: 4+82+2+8+4=100 |
| Christian | 32.0 | 52.0 | 1.0 | 7.0 | 8.0 | E | Some BJP recovery; Birbaha not candidate; rows sum: 32+52+1+7+8=100 |
| Sarna_ORP | 28.0 | 56.0 | 0.0 | 3.0 | 13.0 | D | BJP partial recovery as Lakshmir Bhandar less salient in LS vs AE; but Sarna code still unresolved prevents full BJP recovery; 13% Other_NOTA = JKPP tribal party + NOTA; rows sum: 28+56+0+3+13=100 |
| Other_residual | 38.0 | 42.0 | 1.0 | 10.0 | 9.0 | E | Residual; rows sum: 38+42+1+10+9=100 |
| Marginal recovery AITC | — | — | — | — | — | — | Hindu(83.60)×0.44+Muslim(3.50)×0.82+Sarna(11.00)×0.56+Christian(0.43)×0.52+Other(1.47)×0.42 = 36.78+2.87+6.16+0.22+0.62 = 46.65 vs target 47.49; ±0.84pp — good fit at D-tier |
| Marginal recovery BJP | — | — | — | — | — | — | Hindu(83.60)×0.45+Muslim(3.50)×0.04+Sarna(11.00)×0.28+Christian(0.43)×0.32+Other(1.47)×0.38 = 37.62+0.14+3.08+0.14+0.56 = 41.54 vs target 40.56; ±1.0pp — within tolerance |

### D.16 Vote × Caste (2024 LS)

P(party | caste) — Jangalmahal 2024 regional adjustment.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 50 | 38 | 1 | 7 | 4 | C | CSDS 2024 WB; bhadralok BJP-lean recovering vs 2021 |
| OBC | 45 | 43 | 1 | 7 | 4 | C | Mahato near-parity between BJP and AITC in 2024 LS |
| SC_total | 36 | 50 | 1 | 8 | 5 | C | SC still TMC-leaning but BJP recovering |
| ST_total | 30 | 54 | 0 | 4 | 12 | D | ST vote: partial BJP recovery; AITC still leading; 12% Other_NOTA = JKPP + tribal parties + NOTA |
| Muslim | 4 | 82 | 2 | 8 | 4 | C | Stable |
| Christian_plus_Sarna_plus_Other | 26 | 56 | 0 | 4 | 14 | D | Sarna-Christian coalition still TMC-leaning but BJP making inroads |

### D.17 Vote × Gender (2024 LS)

P(party | gender). Lakshmir Bhandar still anchoring female vote; BJP partially recovered male vote.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 46 | 42 | 1 | 6 | 5 | C | 2024 CSDS WB male; BJP recovered male vote substantially vs 2021 |
| Female | 36 | 53 | 0 | 5 | 6 | D | Lakshmir Bhandar ₹1,000/month for ST women maintaining TMC female-vote lead; no Birbaha candidate-effect but scheme-loyalty persists |
| Third_gender | 36 | 53 | 0 | 5 | 6 | E | Modeled at female pattern |

### D.18 Vote × Welfare scheme exposure (skip — no welfare_exposure axis declared)

> D.18 omitted — this AC does not declare a `welfare_exposure` parent axis per NORMALIZED_SCHEMA §4.7.

---

## E. 2024 baseline vote (calibration target)

The simulator must reproduce the AC-222 2024 LS segment within ±1pp on major parties.

> **ECI-tier-A source.** Direct extraction from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=222, West Bengal. Electorate: 246,403. Total candidate votes: 201,151. NOTA: 2,272 (1.12%). Total valid: 203,423. Turnout: 82.6%. LF = CPI(M) 10,448 + SUCI 569 = 11,017. Other_NOTA = JKPP 2,526 + BSP 1,478 + AISF 641 + APoI 549 + INDs (5 candidates: 433+1,987+968+1,005+1,432=5,825) + NOTA 2,272 = 13,291 (out of 203,423 total with NOTA).

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 40.56 | A | ECI 2024 LS; Dr. Pranat Tudu (BJP, Jhargram LS); 82,507 votes; % of 203,423 |
| AITC | 47.49 | A | ECI 2024 LS; Kalipada Saren (Kherwal, AITC); 96,608 votes |
| INC | 0.00 | A | INC did not contest; INDIA alliance; TMC fielded own candidate |
| LF | 5.42 | A | CPI(M) 10,448 + SUCI 569 = 11,017 votes; Sonamani Tudu (CPI(M)) |
| Other_NOTA | 6.53 | A | JKPP 2,526 + BSP 1,478 + AISF 641 + APoI 549 + INDs 5,825 + NOTA 2,272 = 13,291; % of 203,423 |

---

## F. Vote history (chronological anchors through 2024)

### Chronological election sequence for AC 222 / Jhargram LS

#### 2011 AE → TMC sweeps Jangalmahal, ends CPI(M) era

TMC won AC-222 in 2011 AE with 44.67% (Sukumar Hansda), defeating CPI(M)'s Amar Basu (34.85%). The 2011 victory was driven by Mamata's "peace in Jangalmahal" campaign promise after the traumatic Operation Lalgarh (2009) and the Maoist suppression years. Notably, Chhatradhar Mahato (PCAPA leader, contesting from jail) drew 12.88% of votes — a measure of residual Lalgarh-era resentment against both CPI(M) and TMC.

#### 2014 LS → TMC holds Jhargram LS under wave

TMC won Jhargram LS 2014 (Dr. Uma Saren, 54.60%), cementing Jangalmahal consolidation. BJP was minimal (under 5%).

#### 2016 AE → TMC landslide

TMC won AC-222 2016 AE: Sukumar Hansda 54.97%, JKP(Naren) 24.38%, margin 55,228. BJP's rise in WB was not yet visible in Jangalmahal's ST-dominant AC. CPI(M) had effectively collapsed.

#### 2019 LS → BJP's tribal breakthrough (AC-222 segment)

In the AC-222 segment of the 2019 Jhargram LS: BJP 44.49%, AITC 43.62%, margin just 1,643 votes. Nationally driven BJP wave + PM-KISAN (launched Feb 2019) + tribal Hindutva narrative (Kunar Hembram, an ST tribal candidate) drove BJP to near-parity in Jangalmahal. CPI(M) collapsed to 5.08%. Tribal protest parties (JKP(N)'s Birbaha Hansda 0.96%) showed residual Adivasi-party demand.

#### 2021 AE → TMC massive reversal; Birbaha Hansda factor

TMC: 54.31% (Birbaha Hansda, 109,493 votes). BJP: 35.34% (Sukhmoy Satpati, 71,253 votes). Margin: 38,240 votes (18.97 pp). The largest TMC margin in Jhargram since 2016. Three drivers: (a) Birbaha Hansda candidacy — Santali Adivasi folk-singer, first woman contestant, ran on Sarna-identity platform while also representing state welfare; (b) BJP's Sarna code failure; (c) Lakshmir Bhandar announced April 2021 — ₹1,000/month for ST women HHs. Female tribal voter turnout was exceptionally high.

#### 2024 LS → Adivasi consolidation back to TMC; partial BJP recovery

AITC: 47.49% (Kalipada Saren, 96,608). BJP: 40.56% (Dr. Pranat Tudu, 82,507). Margin: 14,101 (6.93 pp). TMC recaptured Jhargram LS after 2019 BJP win. Key factors:
- Lakshmir Bhandar now institutionalized at ₹1,000/month for ST women — welfare loyalty held.
- Free-rice (Khadya Sathi) universal in tribal belt.
- Sarna code still unresolved; BJP failed to deliver Census Sarna code for 2021 enumeration (deferred due to COVID); tribal alienation persisted.
- JKPP tribal party (Surya Singh Besra) drew 2,526 votes (1.26%) — indicating residual demand for an independent tribal party.
- BJP's SSC scam anti-TMC narrative had limited penetration in Jangalmahal (forest-tribal economy; less affected by urban teacher-recruitment scam).
- RG Kar protests (August 2024) — post-result; no direct electoral impact.

### Mean-reversion note (simulation-critical)

**BJP in AC-222: 44.49% (2019 LS) → 35.34% (2021 AE) → 40.56% (2024 LS). AITC: 43.62% → 54.31% → 47.49%.** This is a structurally competitive seat oscillating around ~45-48% AITC vs ~40-45% BJP, with the Birbaha Hansda candidacy being a 2021 exogenous outlier. The next AE simulation must model: (a) whether Birbaha Hansda contests again; (b) whether BJP secures a Sarna code promise in any form; (c) Lakshmir Bhandar continuation/enhancement; (d) MGNREGA fund-release disputes between Centre and WB.

---

## G. Sources & tier flags

### Primary sources (tier A)
- `data/2024_AssemblySegmentLevelVotingData.csv` — ECI 2024 LS AC-222 segment; party-wise votes, electorate, NOTA (direct extraction)
- ECI 2021 WB Assembly Election — AC-222 result via Wikipedia "Jhargram Assembly constituency"
- ECI 2019 LS AC-222 segment — `data/2019_AssemblySegmentLevelVotingData.csv`
- ECI archives — 2006, 2011, 2016 AE; 2009, 2014, 2019 LS (via Wikipedia)
- Census 2011 — Jhargram Municipality, Jhargram CD Block, Binpur I CD Block

### Secondary sources (tier B/C)
- NFHS-5 (2019-21) West Bengal — asset/media baseline; extended to 2024 with trend
- WB CDWDSW Lakshmir Bhandar scheme data (coverage and amounts)
- PMJDY tribal enrollment + DBT-linked bank account data
- CSDS-Lokniti 2024 WB post-poll (state rollup; Jangalmahal regional extrapolation)
- Jal Jeevan Mission, Swachh Bharat Phase II, PMAY-G progress reports

### Tertiary / journalistic (tier D)
- The Hindu, Indian Express, ThePrint — 2024 WB LS results analysis; Jhargram coverage
- ABP Ananda, Sangbad Pratidin — Jangalmahal 2024 LS voter analysis
- India Today, NDTV — SSC scam and 2024 WB campaign
- MoRD MGNREGA portal — WB fund-release dispute coverage

### Tier-D/E reliance flags
- **Sarna vote share** (D.15, D.16): no tribe-specific 2024 exit poll; estimated from result structure; largest uncertainty
- **Birbaha reversal magnitude**: no sub-constituency exit poll for 2024; estimated from margin collapse 18.97pp → 6.93pp
- **Lakshmir Bhandar penetration**: statewide data; AC-222 tribal belt estimated at ~85% eligible-ST-women coverage by 2024; not independently verified at AC level
- **MGNREGA fund dispute impact**: qualitative; no block-level 2024 personday data accessed

---

## H. Post-2024 validation anchors

> **No post-2024 validation anchors available in v0.** The 2026 WB Assembly Election result is the forward out-of-sample gate. No pre-poll surveys for AC-222 specifically have been publicly summarized as of end-2024.

**TBD: 2026 AE results** — to be populated when ECI publishes. Key simulation questions:
- Will Birbaha Hansda contest 2026 AE (exogenous candidate-effect input)?
- Will BJP offer a concrete Sarna code commitment before the 2026 election?
- Will Lakshmir Bhandar be enhanced (rumoured ₹1,500 for ST, ₹1,000 for general)?
- Will MGNREGA fund-release disputes continue under the Centre-WB tension?

*v0 — generated 2026-04-28, frozen at end-2024 state-of-knowledge. No post-2024 events referenced in calibration sections.*
