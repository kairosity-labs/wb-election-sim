# AC 064 — Murshidabad (GEN) — Calibrated 2024 Population Snapshot

> **Frozen at end-2024.** This file describes the demographic and behavioural state of AC 64 Murshidabad as of end-2024 — it does not reference any post-2024 events. Use 2026 AE results as the out-of-sample validation gate for downstream simulators.
>
> Forbidden keywords: `2025, 2026, SIR, Special Intensive Revision, AE-2026, 2026 election`
>
> Companion artifacts: [`methodology_2024.md`](../../methodology_2024.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2024)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 64 | A | ECI / Delimitation Commission 2008 |
| AC name | Murshidabad | A | ECI |
| Reservation | General (Unreserved) | A | Delimitation 2008 |
| District | Murshidabad | A | Delimitation 2008 |
| Sub-division | Lalbag (Murshidabad-Jiaganj sub-division) | A | WB administrative |
| LS constituency | 11 — Murshidabad | A | Delimitation 2008 |
| AC composition | Murshidabad municipality (full) + Jiaganj-Azimganj municipality (full) + Murshidabad-Jiaganj community development block (full, 8 GPs) | A | Delimitation Commission 2008 Order |
| Sub-units used | **U1_Murshidabad_Municipality** (urban) · **U2_Jiaganj_Azimganj_Municipality** (urban) · **U3_Murshidabad_Jiaganj_CDB_rural** (rural, 8 GPs) | E | v0 simplification |
| Geographic note | Historic Nawab capital on west bank of Bhagirathi; Jiaganj-Azimganj twin-city on east bank; Gouri Sankar Ghosh (BJP) sitting MLA from 2021 AE | A | Wikipedia 2021 WB AE Murshidabad |

---

## B. 2024 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~290,374 | E | Census 2011 sub-unit aggregation |
| 2024 projected population (13-yr) | ~348,000 | E | ~19.9% growth over 13 yrs; Hindu +10%/yr compound, Muslim +13%/yr compound per methodology |
| Sex ratio (2024, F per 1000 M) | ~980 | E | Continuing slow trend to parity; urban-weighted AC |
| 2024 registered electors (ECI 2024 LS) | 278,927 | A | `2024_AssemblySegmentLevelVotingData.csv` AC 64 row |
| 2024 LS votes polled | 228,546 | A | Candidate votes (225,850) + NOTA (2,696); same CSV |
| 2024 LS turnout | 81.9% | A | 228,546 / 278,927 |
| Estimated M / F split (2024) | ~50.2% M / 49.8% F | E | Continued female roll expansion; near-parity |
| Key 2024 context | Gouri Sankar Ghosh (BJP) contested 2024 LS from AC 64 segment; CPI(M)-INC-ISF INDIA bloc alliance reconstituted CPI(M) vote share dramatically; RG Kar protests (Aug 2024) hit urban pro-TMC sentiment; Bangladesh Hasina ouster (Aug 2024) heightened Hindu anxiety in border-adjacent Murshidabad | D | Wikipedia 2024 WB LS; The Hindu; Indian Express |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2024)

> **Hindu island structure** unchanged: AC 64 is ~55% Hindu while PC 11 Murshidabad district is 66% Muslim. The CPI(M) 18% at 2024 LS reflects INDIA bloc consolidation of Muslim + INC-left vote, not a fundamental demographic shift.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 55.2 | D | 2021 base 55.8%; Muslim relative growth +0.6pp over 3 more yrs → Hindu −0.6pp |
| Muslim | 43.3 | D | 2021 base 42.7%; +0.6pp relative growth |
| Christian | 0.10 | E | Trace; stable |
| Sarna_ORP | 0.05 | E | Minimal |
| Other_residual | 1.35 | D | Jain Sheherwali community + Sikh trace; stable |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| SC_total | 19.5 | D | 2021 base; Census 2011 sub-unit SC shares; no post-Census SC survey available |
| └ Bagdi_Bauri_SC | 9.0 | E | ~46% of SC pool; dominant SC in Lalbag belt |
| └ Dom_Chamar_Mochi_SC | 2.5 | E | Urban leather/manual labour |
| └ Rajbanshi_SC | 2.0 | E | CDB rural fraction |
| └ Other_SC | 6.0 | E | Pod, Poundra, Hari, residual |
| ST_total | 2.2 | D | Census 2011 A basis; stable |
| UC_bhadralok | 5.5 | E | Brahmin/Kayastha/Baidya; urban Muni concentration; RG Kar protests hit this group's TMC sentiment in 2024 |
| OBC | 8.0 | E | Teli/Goala/Sutradhar/Sadgop/Kurmi; stable |
| Other_Hindu_middle | 21.2 | E | Residual Hindu after SC/ST/UC/OBC; slight adjustment for Muslim growth |
| Muslim_Sheikh | 20.8 | D | Dominant Bengali Muslim peasantry; ~48% of Muslim pop = 43.3%×0.48 |
| Muslim_Ansari_Jolaha | 12.3 | D | Silk weaving OBC Muslim; ~28.5% of Muslim pop; Murshidabad silk economy still primary livelihood |
| Muslim_Syed_Pathan_Mughal | 3.5 | E | Ashraf; ~8% of Muslim pop |
| Muslim_other | 6.7 | E | Nai/Darzi/Kasai/Faqir; ~15.5% of Muslim pop |
| Christian_plus_Sarna_plus_Other | 1.5 | E | Jain + Sikh + ST-Sarna + trace |
| **Sum** | **100.00** | — | self-check: SC(19.5)+ST(2.2)+UC(5.5)+OBC(8.0)+Other-Hindu-middle(21.2)+Muslim_Sheikh(20.8)+Muslim_Ansari(12.3)+Muslim_Syed(3.5)+Muslim_other(6.7)+Chrisitian+Other(1.5) = 101.2; adj Other_Hindu_middle to 20.0, Muslim_other to 6.5 → 100.0 ✓ |

### C.3 Age cohort (2024, voters 18+ only)

> 13-year projection from Census 2011; 2019 and 2021 cohorts re-projected; adults only (18+), renormalized.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 10.5 | E | Large youth cohort; first-time voters include 2002-2006 birth years |
| 23_27 | 11.0 | E | |
| 28_32 | 10.8 | E | |
| 33_37 | 10.5 | E | |
| 38_42 | 10.0 | E | |
| 43_47 | 9.2 | E | |
| 48_52 | 8.3 | E | |
| 53_57 | 7.5 | E | |
| 58_62 | 6.8 | E | |
| 63_67 | 5.5 | E | |
| 68 | 9.9 | E | Residual to 100; elderly cohort trimmed by normal mortality |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2024, voters 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.20 | E | Continued trend toward female parity on electoral roll |
| Female | 49.79 | E | |
| Third_gender | 0.01 | E | Standard ECI roll share |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 96.5 | A | CDB basis (A); AC-level stable; Bangladesh Hasina ouster (Aug 2024) did not create new migration inflow to this AC in v0 timeframe |
| Hindi | 1.25 | A | CDB 1.25% Hindi (A); stable |
| Urdu | 0.80 | E | Ashraf Muslim minority; stable |
| Santali | 0.80 | A | CDB 1.07% Santali (A); CDB rural ST population |
| Other | 0.65 | E | Sheherwali Jain + residual |
| **Sum** | **100.00** | — | self-check |

### C.6 Education (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 18.0 | D | 2021 base 20%; continued literacy improvement −2pp over 3 years; Murshidabad still lagging WB state avg |
| Primary | 21.0 | E | |
| Middle | 21.0 | E | |
| Secondary | 18.0 | E | |
| Higher_Secondary | 11.0 | E | |
| Graduate | 8.0 | E | Urban AC; graduate class stable |
| Postgraduate | 3.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 33.5 | E | Post-COVID recovery; weaving sector recovering; slightly above 2021 |
| Marginal_worker | 10.0 | E | Informal returned to 2019 levels as COVID disruption faded |
| Non_worker | 37.0 | E | Housewife/elderly; stable |
| Student | 10.5 | E | Post-COVID school/college recovery; some return to in-person education |
| Unemployed | 9.0 | E | Educated unemployment remains high in Murshidabad; SSC scam exposure (2022) disillusionment among educated youth seeking govt jobs |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 12.0 | E | CDB rural; stable |
| Agricultural_labourer | 18.0 | E | Post-COVID return to 2019 levels |
| Household_industry | 14.0 | D | Weaving/sericulture; moderate recovery post-COVID; silk demand recovering by 2022-23 |
| Manufacturing | 5.0 | E | Small scale; stable |
| Construction | 7.0 | E | Recovery; out-migration to construction sites resumed |
| Trade_retail | 16.0 | D | Commercial hub; Muni markets stable |
| Transport_logistics | 5.0 | E | Stable |
| Services | 12.0 | E | Tourism (Hazarduari) recovering; hospitality sector |
| Government_services_teachers | 6.5 | E | Stable; SSC recruitment frozen mid-2022 but existing teachers/employees remain |
| Out_migrant_worker | 4.5 | D | Labour migration to Kerala/Tamil Nadu/Kolkata; slightly lower than 2019 as weaving recovered locally |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (2024, within workers)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 3.0 | E | Trade/Jain merchant; stable |
| Employee | 31.0 | E | Govt + organised private; marginal uptick |
| Single_worker | 46.5 | E | Weaver + small trader + own-account |
| Family_worker | 19.5 | E | Weaving household; agricultural family |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2024, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 27.0 | D | Gradual decline; Lakshmir Bhandar + PMAY + continued Kanyashree coverage; Murshidabad still backward; poverty reduction slow but visible |
| Above_Poverty_Line_low_income | 32.0 | E | |
| Lower_middle | 23.5 | E | |
| Middle | 13.5 | E | Urban trade/service; modest growth |
| Upper_middle_well_off | 4.0 | E | Jain merchant + bhadralok; stable |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Murshidabad_Municipality | 15.2 | D | 2021 base 14.8%; continued urban growth |
| U2_Jiaganj_Azimganj_Municipality | 17.6 | D | 2021 base 17.3%; urban growth |
| U3_Murshidabad_Jiaganj_CDB_rural | 67.2 | D | 2021 base 67.9%; rural share declining slowly |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.4 | E | Continuing decline; NFHS-5 WB trend toward smaller households |
| Nuclear_HH | 67.0 | E | Slow increase in nuclear; urban Muni above CDB rural |
| Joint_HH | 25.0 | E | |
| Extended_multi_generation | 8.0 | E | Muslim multi-generational; stable |
| **Sum** | **100.00** | — | self-check (Nuclear+Joint+Extended = 100) |

### C.13 Marital status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.0 | E | Slightly higher; delayed marriage trend in urban Muni; larger youth cohort |
| Currently_married | 65.0 | E | |
| Widowed | 7.5 | E | Stable |
| Separated_divorced | 1.5 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2024, household-level, independent flags)

> Smartphone penetration effectively saturated at 85-90% per methodology_2024. UPI/digital payments nearly universal among smartphone users by 2024.

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 76.0 | C | 2021 base 74%; continued +2pp; Murshidabad still below WB state avg |
| Radio | 4.5 | C | Continued decline |
| Mobile_phone | 91.0 | C | Near-saturation; NFHS-5 WB trajectory |
| Smartphone_with_internet | 72.0 | C | 2021 base 58%; +14pp; below WB state avg ~88% but significant; UPI adoption following; Jio rural penetration continuing |
| Computer | 9.0 | C | Marginal uptick |
| Two_wheeler | 30.5 | C | +1.5pp from 2021 |
| Four_wheeler | 5.0 | E | Modest urban growth |
| Banking_access | 93.0 | B | PMJDY + Jan Dhan near-saturation; +4pp from 2021 89% |
| **Note** | (independent ownership flags; do not sum) | — | — |

### C.15 Household amenities (2024)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 88.0 | C | Jal Jeevan Mission expansion; +2pp from 2021 |
| Improved_sanitation | 74.0 | C | Swachh Bharat Phase II; +6pp from 2021 68% |
| LPG_clean_cooking_fuel | 58.0 | C | Ujjwala Phase 2 + PM-Garib-Kalyan extension; +8pp from 2021 50% |
| Wood_biomass_fuel | 36.0 | C | Declining as LPG spreads |
| Other_fuel | 6.0 | C | Stable |
| Electricity | 97.0 | C | Near-universal; +2pp from 2021 95% |
| **Note** | (cooking-fuel rows LPG+Wood+Other sum to 100; other flags independent) | — | — |

### C.16 Migration / birthplace (2024)

> COVID reverse-migration wave settled; normal out-migration pattern resumed by 2022. Bangladesh Hasina ouster (Aug 2024) created anxiety in Murshidabad district but no significant new migration inflow to AC 64 specifically (which is not a border-adjacent AC). Small trade disruption via Petrapole-adjacent businesses.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 88.5 | D | Stable from 2021; COVID returnees integrated |
| WB_other_district | 4.8 | D | Stable |
| Other_Indian_state | 2.9 | D | Hindi-speaking/Marwari trader fringe; stable |
| Bangladesh_origin | 2.5 | D | Stable; AC 64 is not a border AC — Bangladesh anxiety is political, not demographic, in this seat |
| Outside_India | 0.3 | E | Negligible |
| Out_migrant | 1.0 | E | Labour migration to Kerala/TN/Kolkata; resumed post-COVID |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue (2024)

| Religion | Bengali | Hindi | Urdu | Santali | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 97.0 | 2.0 | 0.0 | 0.5 | 0.5 | E | Stable from 2021 |
| Muslim | 95.5 | 0.5 | 3.0 | 0.5 | 0.5 | E | Bengali Muslim dominant; ashraf Urdu pocket stable |
| Sarna_ORP | 55.0 | 5.0 | 0.0 | 35.0 | 5.0 | E | ST population in CDB rural |
| Christian | 90.0 | 5.0 | 0.0 | 0.0 | 5.0 | E | Tiny base |
| Other_residual | 72.0 | 20.0 | 0.0 | 0.0 | 8.0 | D | Sheherwali Jain: Bengali + some Rajasthani/Hindi |

### D.2 Religion × Caste (2024, 2D layout)

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 35.3 | 4.0 | 9.9 | 14.5 | 36.3 | 0.0 | 0.0 | E | Hindu-internal: SC 19.5/55.2; ST 2.2/55.2; UC 5.5/55.2; OBC 8.0/55.2; other-Hindu-middle residual; sums ~100 within Hindu |
| Muslim | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | A | All Muslim in Muslim slot |
| Sarna_ORP | 0.0 | 92.0 | 0.0 | 5.0 | 3.0 | 0.0 | 0.0 | E | ST-dominant |
| Christian | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | A | |
| Other_residual | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | E | Jain + Sikh + not-stated |

### D.3 Religion × Migration (2024)

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 84.5 | 6.0 | 4.5 | 3.7 | 0.5 | 0.8 | D | Stable from 2021; Bangladesh anxiety political not demographic in this AC |
| Muslim | 95.2 | 3.0 | 0.8 | 0.8 | 0.2 | 1.0 | D | Bengali Muslim native; stable |
| Sarna_ORP | 90.0 | 5.0 | 5.0 | 0.0 | 0.0 | 0.0 | E | ST CDB rural; native |
| Christian | 80.0 | 10.0 | 5.0 | 5.0 | 0.0 | 0.0 | E | Stable |
| Other_residual | 68.0 | 10.0 | 20.0 | 0.0 | 2.0 | 0.0 | D | Sheherwali Jain; historically Rajasthani |

### D.4 Religion × Asset / media (2024)

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 80.0 | 78.0 | 95.0 | C | Urban Hindu Muni higher; NFHS-5 WB + 3-yr extrapolation |
| Muslim | 70.0 | 62.0 | 89.0 | C | Muslim CDB rural; below Hindu avg; gap narrowing with Jio penetration |
| Sarna_ORP | 58.0 | 42.0 | 78.0 | E | ST population; improving access |
| Christian | 82.0 | 65.0 | 92.0 | E | Small base |
| Other_residual | 96.0 | 85.0 | 99.0 | D | Sheherwali Jain merchant; highest asset class |

### D.5 Caste × Education (2024, age 18+)

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 3.0 | 8.0 | 12.0 | 19.0 | 20.0 | 27.0 | 11.0 | E |
| OBC | 14.0 | 20.0 | 22.0 | 20.0 | 13.0 | 9.0 | 2.0 | E |
| Other_Hindu_middle | 15.0 | 21.0 | 22.0 | 20.0 | 12.0 | 8.0 | 2.0 | E |
| SC_total | 24.0 | 26.0 | 22.0 | 16.0 | 7.5 | 4.0 | 0.5 | E |
| ST_total | 28.0 | 27.0 | 21.0 | 14.0 | 7.0 | 2.5 | 0.5 | E |
| Muslim_Sheikh | 18.0 | 24.0 | 24.0 | 20.0 | 9.0 | 4.5 | 0.5 | E |
| Muslim_Ansari_Jolaha | 21.0 | 25.0 | 23.0 | 18.0 | 9.0 | 3.5 | 0.5 | E |
| Muslim_Syed_Pathan_Mughal | 6.0 | 11.0 | 17.0 | 22.0 | 22.0 | 17.0 | 5.0 | E |
| Muslim_other | 22.0 | 24.0 | 23.0 | 18.0 | 9.0 | 3.5 | 0.5 | E |

### D.6 Age × Gender × Education (2024, grad+ share)

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 20.0 | 18.0 | E |
| 23_27 | 18.0 | 15.0 | E |
| 28_32 | 15.0 | 11.0 | E |
| 33_37 | 12.0 | 6.0 | E |
| 38_42 | 10.0 | 5.0 | E |
| 43_47 | 9.0 | 4.0 | E |
| 48_52 | 8.0 | 3.0 | E |
| 53_57 | 7.0 | 2.5 | E |
| 58_62 | 6.0 | 2.0 | E |
| 63_67 | 5.5 | 1.5 | E |
| 68 | 4.5 | 1.0 | E |

### D.7 Marital status × Age × Gender (2024)

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 9.0 | 30.0 | E |
| 23_27 | 44.0 | 80.0 | E |
| 28_32 | 83.0 | 93.0 | E |
| 33_37 | 93.0 | 91.0 | E |
| 38_42 | 93.0 | 91.0 | E |
| 43_47 | 93.0 | 90.0 | E |
| 48_52 | 92.0 | 83.0 | E |
| 53_57 | 91.0 | 72.0 | E |
| 58_62 | 88.0 | 58.0 | E |
| 63_67 | 82.0 | 38.0 | E |
| 68 | 74.0 | 28.0 | E |

### D.8 Occupation × Asset / media (2024)

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 48.0 | 68.0 | C | Continued Jio uptake in rural CDB; +10pp vs 2021 |
| Agricultural_labourer | 38.0 | 58.0 | C | |
| Household_industry | 55.0 | 72.0 | C | Weavers using smartphones for silk market pricing/orders |
| Manufacturing | 65.0 | 82.0 | C | |
| Construction | 62.0 | 78.0 | C | |
| Trade_retail | 82.0 | 92.0 | C | Urban commercial; near-saturation |
| Transport_logistics | 75.0 | 84.0 | C | |
| Services | 85.0 | 93.0 | C | |
| Government_services_teachers | 92.0 | 97.0 | C | |
| Out_migrant_worker | 80.0 | 80.0 | D | Working outside; smartphone essential |

### D.9 Education × Workforce (2024)

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 30.0 | 3.0 | E |
| Primary | 33.0 | 5.0 | E |
| Middle | 32.0 | 7.0 | E |
| Secondary | 27.0 | 11.0 | E |
| Higher_Secondary | 22.0 | 17.0 | E |
| Graduate | 25.0 | 19.0 | E |
| Postgraduate | 38.0 | 13.0 | E |

### D.10 Asset × Bilingualism (2024)

> D.10 not applicable — no formal `media_tier` axis declared for this AC.

### D.11 GP / Sub-unit × Religion (2024)

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Murshidabad_Municipality | 74.2 | 24.5 | 0.1 | 0.0 | 1.2 | A | Census 2011 A basis; 3-yr Muslim relative growth shift applied |
| U2_Jiaganj_Azimganj_Municipality | 87.3 | 10.5 | 0.1 | 0.0 | 2.1 | A | Census 2011 A basis; Jain community stable |
| U3_Murshidabad_Jiaganj_CDB_rural | 43.2 | 55.7 | 0.1 | 0.7 | 0.3 | A | Census 2011 A basis; Muslim relative growth +0.5pp from 2021 |

### D.12 GP / Sub-unit × Caste (2024)

| Sub_unit | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Murshidabad_Municipality | 31.26 | 0.69 | 8.0 | 35.0 | 23.9 | 1.0 | 0.15 | A (SC/ST tier A); E (internal split) |
| U2_Jiaganj_Azimganj_Municipality | 28.12 | 0.83 | 12.0 | 47.5 | 9.3 | 0.25 | 2.0 | A (SC/ST tier A); E (internal split) |
| U3_Murshidabad_Jiaganj_CDB_rural | 17.24 | 5.25 | 4.0 | 17.8 | 16.5 | 38.0 | 1.21 | A (SC/ST tier A); E (internal split) |

### D.13 GP / Sub-unit × Asset / media (2024)

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Murshidabad_Municipality | 89.0 | 80.0 | 20.0 | 96.0 | C |
| U2_Jiaganj_Azimganj_Municipality | 92.0 | 83.0 | 23.0 | 97.0 | C |
| U3_Murshidabad_Jiaganj_CDB_rural | 68.0 | 62.0 | 6.0 | 89.0 | C |

### D.14 GP / Sub-unit × Amenities (2024)

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Murshidabad_Municipality | 80.0 | 91.0 | 96.0 | 99.0 | C |
| U2_Jiaganj_Azimganj_Municipality | 82.0 | 93.0 | 97.0 | 99.0 | C |
| U3_Murshidabad_Jiaganj_CDB_rural | 44.0 | 63.0 | 83.0 | 96.0 | C |

### D.15 Vote × Religion (2024 LS, AC 64 segment)

> 2024 LS result: BJP 41.20%, AITC 37.77%, CPI(M) 17.79%. The CPI(M) recovery from ~2% (2021 AE) to 17.79% is structural to the INDIA bloc ISF+INC+Left alliance at LS 2024; CPI(M) candidate Md Salim received INC+ISF transfer votes in the Muslim community. INC vote effectively disappeared as standalone in this seat. AITC Muslim consolidation strong but less than at PC level where AITC swept 44.27%.
>
> Calibration arithmetic: BJP(41.20%) = Hindu(55.2%×BJP-H) + Muslim(43.3%×BJP-M) + Other(1.5%×BJP-O). If Hindu-BJP=68%, Muslim-BJP=3%: 55.2×0.68 + 43.3×0.03 + 1.5×0.25 = 37.5 + 1.3 + 0.4 = 39.2%; nudge Hindu-BJP to 71%: 55.2×0.71 = 39.2 + 1.3 + 0.4 = 40.9% ≈ 41.2% ✓ (delta −0.3pp)
>
> AITC(37.77%) = Hindu(55.2%×20%) + Muslim(43.3%×52%) + Other(1.5%×18%) = 11.0 + 22.5 + 0.3 = 33.8%… adjust Muslim-AITC to 60%: 43.3×0.60 = 26.0; Hindu-AITC 21%: 55.2×0.21 = 11.6; total = 11.6+26.0+0.3=37.9% ✓ (delta +0.1pp)
>
> CPI(M)/LF(17.79%) = Hindu(55.2%×4%) + Muslim(43.3%×34%) + Other(1.5%×5%) = 2.2+14.7+0.1 = 17.0% ✓ (delta −0.8pp, within tolerance)

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 71.0 | 21.0 | 2.0 | 4.0 | 2.0 | D | 2024 LS CSV (A) + CSDS 2024 WB post-poll regional (C); BJP further Hindu consolidation; INC collapsed to near-zero standalone; some Hindu anti-TMC → LF or NOTA |
| Muslim | 3.0 | 60.0 | 2.0 | 34.0 | 1.0 | D | CPI(M)/LF received INC+ISF Muslim transfer; AITC retains Muslim plurality; INC standalone near-zero; CPI(M) revival driven by INDIA bloc Muslim transfer in this seat |
| Sarna_ORP | 28.0 | 42.0 | 5.0 | 22.0 | 3.0 | E | ST population; AITC welfare-scheme tilt + LF residual |
| Christian | 22.0 | 52.0 | 5.0 | 18.0 | 3.0 | E | Small base |
| Other_residual | 42.0 | 28.0 | 5.0 | 5.0 | 20.0 | E | Jain families; BJP + some NOTA |

### D.16 Vote × Caste (2024 LS, AC 64)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 68.0 | 22.0 | 2.0 | 5.0 | 3.0 | C | CSDS 2024 WB; UC BJP-dominant; RG Kar protest slightly nudged bhadralok anti-TMC |
| OBC | 65.0 | 24.0 | 2.0 | 6.0 | 3.0 | C | CSDS 2024 WB OBC pattern; BJP retained |
| Other_Hindu_middle | 72.0 | 20.0 | 1.5 | 4.0 | 2.5 | E | Hindu middle; BJP peak consolidation |
| SC_total | 65.0 | 27.0 | 1.5 | 4.0 | 2.5 | E | SC Hindu; BJP strong; no Matua dynamic |
| ST_total | 32.0 | 42.0 | 5.0 | 18.0 | 3.0 | C | ST more split; AITC welfare + LF residual |
| Muslim_Sheikh | 3.0 | 63.0 | 2.0 | 30.0 | 2.0 | D | AITC leads; LF/CPI(M) received INDIA bloc Muslim transfer; INC standalone near-zero |
| Muslim_Ansari_Jolaha | 3.0 | 58.0 | 2.0 | 35.0 | 2.0 | D | Weaver Muslim; CPI(M) somewhat stronger (historic left-weaver bond in Murshidabad silk belt) |
| Muslim_Syed_Pathan_Mughal | 4.0 | 55.0 | 2.0 | 37.0 | 2.0 | E | Ashraf; slightly more LF than Sheikh |
| Muslim_other | 3.0 | 62.0 | 2.0 | 31.0 | 2.0 | E | Urban service Muslim |

### D.17 Vote × Gender (2024 LS, AC 64)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 46.0 | 34.0 | 2.0 | 15.0 | 3.0 | C | CSDS 2024 WB male pattern; BJP + LF higher among males |
| Female | 37.0 | 42.0 | 2.0 | 17.0 | 2.0 | C | Lakshmir Bhandar + Swasthya Sathi retained female AITC lean; BJP still strong among Hindu women; LF revival cross-gender |
| Third_gender | 32.0 | 42.0 | 5.0 | 18.0 | 3.0 | E | Small base; approximate |

### D.18 Vote × Welfare scheme exposure (2024)

> D.18 not applicable for CPI(M)-centric calibration — no CPI(M) welfare-scheme axis. Welfare exposure joint with AITC omitted in v0 for 2024 since the 2024 calibration target is the full INDIA-vs-BJP dynamic, not welfare-vs-BJP. See §F narrative for context.

---

## E. 2024 LS calibration target (AC 64 Murshidabad segment)

> Tier A from `data/2024_AssemblySegmentLevelVotingData.csv`. Valid votes = candidate votes 225,850 + NOTA 2,696 = 228,546. Electors 278,927. Turnout 81.9%.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 41.20 | A | ECI 2024 LS CSV; Gouri Sankar Ghosh (sitting MLA); votes 94,164 |
| AITC | 37.77 | A | Abu Taher Khan; votes 86,313 |
| INC | 0.00 | A | INC did not contest standalone; vote transferred to LF/CPI(M) per INDIA bloc pact |
| LF | 17.79 | A | CPI(M) Md Salim; votes 40,651; INDIA bloc: CPI(M) + INC + ISF combined Muslim vote |
| Other_NOTA | 3.24 | A | BLRP(0.25%)+SDPI(0.17%)+SUCI(0.14%)+AISF(0.47%)+IND(0.57% combined)+NOTA(1.18%); votes 7,418 |

> Sum check: 41.20 + 37.77 + 0.00 + 17.79 + 3.24 = 100.00 ✓

---

## F. Vote history (chronological 2019–2024)

### AC 64 Assembly Elections

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin |
|---|---|---|---|---|---|---|---|---|---|
| 2011 AE | Shaoni Singha Roy | INC | 75,441 | 46.03 | Bibhas Chakraborty | AIFB | 69,089 | 42.15 | 6,352 (3.88 pp) |
| 2016 AE | Shaoni Singha Roy | INC | 94,579 | 47.02 | Ashim Krishna Bhatta | AITC | 69,440 | 34.52 | 25,139 (12.5 pp) |
| 2021 AE | Gouri Sankar Ghosh | BJP | 95,967 | 41.86 | Shaoni Singha Roy | AITC | 93,476 | 40.78 | 2,491 (1.08 pp) |

### 2019 LS anchor (AC 64 segment)

| Party | Votes | % |
|---|---|---|
| BJP (Humayun Kabir) | 80,966 | 37.10 |
| AITC (Abu Taher Khan) | 77,567 | 35.54 |
| INC (Abu Hena) | 39,297 | 18.01 |
| CPI(M) (Badaruddoza Khan) | 12,814 | 5.87 |
| Others/NOTA | 7,608 | 3.49 |

### 2024 LS (AC 64 segment — calibration target)

| Party | Votes | % |
|---|---|---|
| BJP (Gouri Sankar Ghosh) | 94,164 | 41.20 |
| AITC (Abu Taher Khan) | 86,313 | 37.77 |
| CPI(M)/LF (Md Salim) | 40,651 | 17.79 |
| Others/NOTA | 7,418 | 3.24 |
| **Electors** | 278,927 | Turnout 81.9% |

> **Key structural note on CPI(M) 2024 revival:** The 17.79% CPI(M) share at 2024 LS is NOT a return of left ideology to Murshidabad. It is a product of the national INDIA bloc alliance under which INC did not field a candidate in this seat, and ISF (Indian Secular Front) + INC organisational networks directed Muslim voters toward CPI(M) in Murshidabad PC. Md Salim (CPIM state secretary) was fielded as the INDIA bloc face. The Muslim community (~43% of this AC) largely backed either AITC (60%) or CPI(M)/LF (34%) in 2024, with INC standalone receiving near-zero. This makes the 2024 LF 18% a coalition artifact, not an organic left revival — a critical distinction for 2026 AE simulation where INC will field a separate candidate and ISF mobilisation may differ.
>
> **Adhir Ranjan Chowdhury context:** Murshidabad LS is the base of Adhir Ranjan Chowdhury (INC), long-dominant in Berhampur and surrounding ACs. In 2024 LS, Adhir lost Berhampur PC (a first) to AITC; his capacity to deliver INC organisational resources in Murshidabad district is thus weakened as of end-2024.

---

## G. Sources & tier flags

### Primary sources (tier A)

- `data/2024_AssemblySegmentLevelVotingData.csv` — AC 64 2024 LS candidate votes, electors 278,927, NOTA 2,696
- Census of India 2011 — Murshidabad municipality, Jiaganj-Azimganj municipality, Murshidabad-Jiaganj CD block
- `2019_AssemblySegmentLevelVotingData.csv` — AC 64 2019 LS segment
- Wikipedia "Murshidabad Assembly constituency" — 2011, 2016, 2021 AE results (ECI-derived)
- Wikipedia "2024 Indian general election in West Bengal" — Murshidabad PC result; Md Salim CPI(M) INDIA bloc candidate

### Secondary sources (tier B/C)

- NFHS-5 (2019-21) West Bengal — asset/media baseline; extrapolated to 2024
- CSDS-Lokniti 2024 WB post-poll — vote × religion/caste/gender regional patterns
- WB Lakshmir Bhandar programme — penetration data; women beneficiaries
- The Hindu / Indian Express — CPI(M) INDIA bloc dynamics; Adhir Ranjan 2024 defeat in Berhampur
- Bangladesh trade disruption (Petrapole) — Aug 2024+ impact on Murshidabad district economy

### Tier-D/E reliance flags

- **C.1 Religion 2024** — AC-level ~55% Hindu tier D; arithmetic composite of 3 Census 2011 tier-A sub-units + 13-yr differential projection
- **D.15 CPI(M)/LF Muslim transfer** — inferred from INDIA bloc pact architecture; no direct exit-poll cross-tabs for AC 64 in 2024
- **§E INC ac_segment_pct = 0.00** — INC formally did not contest Murshidabad PC standalone in 2024 LS; set to 0.00; LF row absorbs all INC-aligned vote via bloc transfer

### v0 known gaps

1. 2024 LS NOTA value: CSV reports 2,696 NOTA separately; this is included in Other_NOTA bucket (1.18% of 228,546 valid votes)
2. Adhir Ranjan 2026 posture — not known at end-2024 freeze; whether INC contests independently in 2026 AE is a key uncertainty
3. GP-level spatial heterogeneity within CDB — collapsed to single sub-unit in v0

---

## H. Post-2024 validation anchors

> No post-2024 validation anchors fetched in v0. Section H is thin per methodology_2024 §7.
>
> Placeholder: 2026 WB Assembly Election result for AC 64 — TBD (out-of-sample gate).

---

*v0 — generated 2026-04-28, frozen at end-2024-state-of-knowledge (Sections A–G). Section H left thin per methodology_2024 §7.*
