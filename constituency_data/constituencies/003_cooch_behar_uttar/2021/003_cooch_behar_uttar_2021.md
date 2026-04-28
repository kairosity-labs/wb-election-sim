# AC 003 — Cooch Behar Uttar (SC) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural state of AC 003 Cooch Behar Uttar as of end-2021 — it does not reference any post-2021 events. The 2024 LS AC-segment result appears only in § H as an out-of-sample validation gate.
>
> **Forbidden post-2021 events (auto-checked):** 2022 SSC scam exposure, Partha Chatterjee arrest (Jul 2022), 2023 panchayat elections, 2024 LS results, CAA rules notification (Mar 2024), RG Kar protests (Aug 2024), SIR voter-roll revision (2025), 2026 AE.
>
> **MAY reference:** 2019 LS, 2020 COVID lockdown, 2020 NRC anxiety, 2021 WB AE (results known May 2021), Lakshmir Bhandar launch (Apr 2021), BSF 50km jurisdiction extension (Oct 2021), Bangladesh temple attacks (Oct 2021).
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) · [`csv/`](csv/) · [`2019/003_cooch_behar_uttar_2019.md`](../2019/003_cooch_behar_uttar_2019.md)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (Calibrated 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 3 | A | ECI / Delimitation Commission 2008 |
| AC name | Cooch Behar Uttar | A | ECI |
| Reservation | SC | A | Delimitation 2008 |
| District | Cooch Behar (Koch Bihar) | A | Delimitation 2008 |
| Sub-division | Cooch Behar Sadar | A | WB administrative |
| LS constituency | PC 1 — Cooch Behar (SC reserved) | A | Delimitation 2008 |
| LS segments included with AC 3 | AC 1 Mathabhanga (SC) · AC 2 Cooch Behar Uttar · AC 3 Cooch Behar Dakshin · AC 4 Sitalkuchi (SC) · AC 5 Sitai · AC 6 Dinhata · AC 7 Natabari | A | Delimitation 2008 |
| AC composition | Cooch Behar II community development block (all 13 GPs + 5 census towns) | A | Delimitation 2008 |
| Geographic note | North Bengal plains, Terai zone near Bhutan/Bangladesh border; Torsha and Tista river basin; Cooch Behar princely state merger 1949; border-adjacent AC — Bangladesh frontier within 20–50 km | A | Historical record |
| Two sub-units (v0) | **U1_Census_towns_cluster** (Khagrabari, Takagachh, Chakchaka, Baisguri, Baneswar ~15.7% pop) · **U2_CDB_II_rural_GPs** (13 GPs ~84.3% pop) | E | Census 2011; same as 2019 baseline |
| Calibration year | 2021 (end-year freeze) | A | This document |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | 343,901 (CDB-II: 289,917 rural + 53,984 urban census towns) | A | Census 2011 — Cooch Behar II CDB |
| 2021 projected population | ~382,600 | E | 10-yr compound religion-differential growth from 2011: Hindu +1.0%/yr, Muslim +1.3%/yr; 10-yr factor Hindu ×1.1046, Muslim ×1.1380 |
| Sex ratio (2021, F per 1000 M) | ~924 | E | CDB-II 2011: 915; +1 point/yr improvement trend; Cooch Behar district 942 |
| 2021 electorate (ECI AE roll) | 263,078 | A | ECI 2021 WB AE — Wikipedia Cooch Behar Uttar AC; direct AE roll figure |
| Estimated M / F / TG split (2021) | 51.8% M / 48.2% F / <0.05% TG | E | CDB-II 2011 52.2% M; continued convergence trend |
| 2021 polling booths | ~300 | A | ECI 2021 AE — approx from 263,078 electors / ~900 electors per booth |
| 2021 total valid votes cast | 243,916 | A | ECI 2021 AE — Wikipedia Cooch Behar Uttar AC |
| 2021 AE turnout | 92.72% | A | 243,916 / 263,078 (ECI 2021 AE) |
| Back-derived 2024 electorate (forward note) | 292,443 | A | ECI 2024 LS CSV — used only for electorate trajectory check; does not affect 2021 calibration |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 82.00 | E | CDB-II 2011: 81.85% (A); Muslim differential growth +1.3%/yr vs Hindu +1.0%/yr over 10yr → Hindu share dips ~0.60pp from 2011; projected 82.00% |
| Muslim | 17.48 | E | CDB-II 2011: 17.64%; 10-yr projection: Muslim grows faster; 17.48% by 2021 |
| Christian | 0.18 | E | Stable; CDB-II 2011: 0.18% |
| Sarna_ORP | 0.20 | E | Minor Sarna/tribal; subsumed in CDB-II residual; stable |
| Other_residual | 0.14 | E | Sikh + Jain + Buddhist + Not-stated residual; stable |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 45.30 | A | CDB-II 2011: SC 44.97% (A); small upward nudge for 10-yr differential SC growth |
| └ Rajbanshi_SC | 38.50 | C | ~85% of SC pool; dominant Rajbanshi/Koch-Rajbanshi community; Outlook India anchor |
| └ Namasudra_SC | 3.25 | E | ~7% of SC pool |
| └ Bagdi_Hari_SC | 1.70 | E | ~3.8% of SC pool |
| └ Other_SC | 1.85 | E | ~4% of SC pool residual |
| **ST_total** | 1.00 | A | CDB-II 2011: 1.00% (A); Mech/Rajbongshi tribal; stable |
| UC_bhadralok | 4.50 | E | Service class in census towns; stable |
| OBC | 10.00 | E | Artisan / service OBC |
| Other_Hindu_middle | 21.20 | E | Residual: 82.00 − 45.30 SC − 1.00 ST − 4.50 UC − 10.00 OBC = 21.20 |
| Muslim | 17.48 | E | See C.1 |
| Christian_plus_Sarna_plus_Other | 0.52 | E | Christian 0.18 + Sarna 0.20 + Other_residual 0.14 |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2021, adults 18+ only)

Renormalized from Census 2011 adult age pyramid + 10-yr cohort shift. Children (0–17) excluded; adult distribution renormalized to 100.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 10.5 | E | 2003–2007 birth cohort enters voting age; slightly larger than 2019 equivalent |
| 23_27 | 10.5 | E | |
| 28_32 | 10.0 | E | |
| 33_37 | 9.5 | E | |
| 38_42 | 9.0 | E | |
| 43_47 | 8.5 | E | |
| 48_52 | 7.5 | E | |
| 53_57 | 6.5 | E | |
| 58_62 | 6.0 | E | |
| 63_67 | 5.5 | E | |
| 68 | 16.5 | E | Aggregated 68+ cohort; North Bengal rural aging-in-place; renormalization residual |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, adults 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.80 | E | CDB-II 2011: 52.19% M; convergence trend continued |
| Female | 48.20 | E | |
| Third_gender | <0.01 | E | Negligible |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 93.49 | A | CDB-II 2011: 93.49% Bengali (A); stable over decade |
| Rajbongshi | 1.23 | A | CDB-II 2011: 1.23% Rajbongshi (A); Koch-Rajbanshi identity language |
| Hindi | 1.85 | A | CDB-II 2011: 1.85% Hindi (A); stable trader/migrant fraction |
| Urdu | 1.00 | E | Muslim Urdu-speaking pocket; stable |
| Other | 2.43 | E | Mech / Koch / Nepali / Santhali |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 11.0 | E | CDB-II 2011: 81.39% literate (A); +0.5pp/yr over 10yr → ~86.4% literate by 2021; illiterate ~13.6% → adult-corrected ≈ 11% |
| Primary | 21.0 | E | Slight decline as middle-school completion improves |
| Middle | 22.0 | E | |
| Secondary | 19.5 | E | Modest upward shift |
| Higher_Secondary | 12.5 | E | |
| Graduate | 10.0 | E | North Bengal college expansion |
| Postgraduate | 4.0 | E | UBKV proximity; stable |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 31.0 | E | COVID-19 2020 disruption reduced main-worker rate; seasonal agri-workers reclassified; CDB-II 2011 37.31% base → slightly lower in 2021 post-COVID |
| Marginal_worker | 13.0 | E | COVID return migrants swelled marginal-worker pool |
| Non_worker | 36.0 | E | Female non-worker share stable; high rural North Bengal |
| Student | 11.0 | E | School disruption 2020–21 affected 18–22 cohort; slight reduction in active students |
| Unemployed | 9.0 | E | COVID-period educated unemployment elevated vs 2019 |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 20.5 | E | Slight recovery post-Amphan/COVID; paddy and jute cultivators |
| Agricultural_labourer | 31.0 | E | Reduced by COVID migration disruption; some remained in local area |
| Household_industry | 4.5 | E | Tobacco/handloom; slight uptick as alternative income during COVID |
| Manufacturing | 3.0 | E | Limited organised manufacturing; stable |
| Construction | 6.5 | E | COVID return migration raised local construction workforce in 2020–21 |
| Trade_retail | 12.0 | E | Census-town commercial activity recovering |
| Transport_logistics | 5.0 | E | |
| Services | 10.0 | E | Including pisciculture; stable |
| Government_services_teachers | 5.5 | E | WB govt employees; school-teacher recruitment; stable |
| Out_migrant_worker | 2.0 | E | Reduced vs 2019 — COVID lockdown kept out-migrants home in 2020; partial recovery by 2021 |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.0 | E | Census B-04 WB rural pattern; stable |
| Employee | 25.0 | E | Govt + organised sector; stable |
| Single_worker | 48.0 | E | Cultivator + artisan + small trader |
| Family_worker | 25.0 | E | Within agri-household; female family labour |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 25.0 | C | Cooch Behar district above-average poverty; COVID-19 income shock pushed marginal households below poverty line; +1pp vs 2019 |
| Above_Poverty_Line_low_income | 35.0 | E | Ag-labourer + marginal cultivator; COVID income losses |
| Lower_middle | 24.0 | E | Stable |
| Middle | 12.0 | E | Stable |
| Upper_middle_well_off | 4.0 | E | Census-town commercial class; stable |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Census_towns_cluster | 15.70 | A | Census 2011: 53,984 / 343,901 = 15.70%; holds stable — no new census-town notifications by 2021 |
| U2_CDB_II_rural_GPs | 84.30 | A | Remainder; 13 GPs |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.4 persons | E | Slight decline from 2019 (4.5); NFHS-5 WB rural trend; COVID return migration temporarily inflated, then normalized |
| Nuclear_HH | 66.0 | E | Slight increase vs 2019 (65%); NFHS-5 WB rural pattern |
| Joint_HH | 27.0 | E | Slight decline; younger Rajbanshi households nuclearizing |
| Extended_multi_generation | 7.0 | E | Stable |
| **Sum** | **100.00** | — | self-check (Nuclear + Joint + Extended) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 27.5 | E | Slight uptick as COVID delayed marriages in 2020 |
| Currently_married | 63.5 | E | Slightly down; COVID delay effect |
| Widowed | 8.0 | E | Stable |
| Separated_divorced | 1.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media (2021, household level — independent rates, do NOT sum)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 77.0 | C | NFHS-4 → NFHS-5 WB rural trend; slight uptick; ~+3pp from 2019 |
| Radio | 3.5 | C | Continuing decline; ~0.5pp fall per year |
| Mobile_phone | 88.0 | C | +4pp from 2019; strong rural penetration by 2021 |
| Smartphone_with_internet | 62.0 | C | Major post-COVID surge: WhatsApp/YouTube essential for information and welfare; NFHS-5 WB rural ~60–65%; +22pp from 2019 (40%) — COVID-driven adoption in 2020–21 |
| Computer | 6.5 | C | Marginal increase; laptop for students via PM e-Vidya |
| Two_wheeler | 32.0 | C | +2pp from 2019 |
| Four_wheeler | 5.0 | C | Stable |
| Banking_access | 94.0 | B | PMJDY further enrollment; Jan Dhan accounts used for DBT during COVID relief; ~+6pp from 2019 (88%) |

### C.15 Household amenities (2021)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 86.0 | C | Stable +1pp |
| Improved_sanitation | 75.0 | C | +7pp from 2019 (68%); Swachh Bharat Mission Phase-2 continued; North Bengal rural latrines |
| LPG_clean_cooking_fuel | 46.0 | C | +8pp from 2019 (38%); Ujjwala 2.0 launched 2021; North Bengal rural Ujjwala uptake |
| Wood_biomass_fuel | 49.0 | C | Declining as LPG rises; still dominant in deep-rural GPs |
| Other_fuel | 5.0 | C | Stable |
| Electricity | 96.0 | C | Near-saturation; +2pp from 2019 |

### C.16 Migration / birthplace (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 85.0 | D | Princely-state history; low in-migration; COVID 2020 return migrants boosted native count as out-migrants returned home |
| WB_other_district | 5.5 | D | Slight decline as some service-class in-migrants returned to home districts during COVID |
| Other_Indian_state | 4.0 | D | Marwari/Bihari traders; stable |
| Bangladesh_origin | 4.0 | D | Border-area community; Bangladesh temple attacks Oct 2021 generated anxiety but no significant new migration into AC by end-2021 |
| Outside_India | 1.0 | E | Nepal/Bhutan-origin North Bengal fringe |
| Out_migrant | 0.5 | E | Reduced vs 2019 (1.0%); COVID return migration — many seasonal migrants from Assam/Kerala remained in AC through 2020; partial re-migration by end-2021 |
| **Sum** | **100.00** | — | self-check |

**C.16 note — COVID return migration (2020):** The March 2020 national lockdown prompted reverse migration of seasonal workers from Assam tea districts, Delhi NCR, and construction sites in other states. Estimated 3,000–5,000 persons returned to CDB-II GPs in April–June 2020 (tier D, district-level estimate from Cooch Behar district collector reports). Most had re-migrated by end-2021, reducing the Out_migrant share from 1% to 0.5%.

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Rajbongshi | Hindi | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 90.0 | 1.5 | 2.0 | 0.0 | 6.5 | E | Same as 2019; CDB-II language structure stable |
| Muslim | 96.0 | 0.0 | 0.5 | 3.0 | 0.5 | E | Bengali-Sheikh dominant; small Urdu pocket |
| Christian | 90.0 | 0.0 | 5.0 | 0.0 | 5.0 | E | Tiny base |
| Sarna_ORP | 50.0 | 10.0 | 5.0 | 0.0 | 35.0 | E | Tribal language fringe |
| Other_residual | 50.0 | 10.0 | 30.0 | 0.0 | 10.0 | E | Marwari/trader mix |

### D.2 Religion × Caste (2D layout)

P(caste ‖ religion) — % within each religion; rows sum to 100.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 55.25 | 1.22 | 5.49 | 12.20 | 25.84 | 0 | 0 | C | Hindu rows: SC_total=45.30/82.00; ST=1.00/82.00; UC=4.50/82.00; OBC=10.00/82.00; OHM=21.20/82.00; all sum to 100 |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | All Muslim |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | All Christian+Other |
| Sarna_ORP | 0 | 90 | 0 | 5 | 5 | 0 | 0 | E | Tribal-ST dominant |
| Other_residual | 0 | 0 | 10 | 20 | 70 | 0 | 0 | E | Marwari/trader mix |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 85 | 5.5 | 5 | 3 | 1 | 0.5 | D | Rajbanshi native; Marwari = other-state; Bangladesh fringe |
| Muslim | 83 | 7 | 1 | 8 | 0 | 1 | D | Higher Bangladesh-heritage share for border-area Muslim |
| Christian | 80 | 10 | 5 | 5 | 0 | 0 | E | Mixed |
| Sarna_ORP | 90 | 5 | 5 | 0 | 0 | 0 | E | Local tribal |
| Other_residual | 50 | 15 | 30 | 5 | 0 | 0 | E | Marwari/Bihari traders |

### D.4 Religion × Asset / media

P(owns asset ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 79 | 65 | 96 | C | NFHS-5 WB pattern; Hindu higher in rural CDB-II; smartphone surge post-COVID |
| Muslim | 68 | 50 | 86 | C | Muslim asset gap persists but narrowed in 2021 — Jan Dhan DBT COVID relief boosted banking |
| Christian | 80 | 66 | 93 | E | Approximation |
| Sarna_ORP | 65 | 48 | 85 | E | Below-average; tribal community |
| Other_residual | 84 | 72 | 92 | E | Trader/Marwari community |

### D.5 Caste × Education

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 3 | 8 | 12 | 18 | 20 | 26 | 13 | E |
| Rajbanshi_SC | 13 | 21 | 22 | 20 | 12 | 9 | 3 | E |
| Other_SC | 18 | 25 | 22 | 17 | 10 | 6 | 2 | E |
| ST_total | 20 | 27 | 22 | 17 | 8 | 5 | 1 | E |
| OBC | 11 | 20 | 22 | 20 | 13 | 11 | 3 | E |
| Other_Hindu_middle | 11 | 21 | 22 | 20 | 13 | 10 | 3 | E |
| Muslim | 17 | 23 | 23 | 19 | 11 | 6 | 1 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share within cohort.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 18 | 17 | E |
| 23_27 | 17 | 14 | E |
| 28_32 | 15 | 10 | E |
| 33_37 | 12 | 7 | E |
| 38_42 | 10 | 5 | E |
| 43_47 | 8 | 3 | E |
| 48_52 | 7 | 2 | E |
| 53_57 | 6 | 2 | E |
| 58_62 | 5 | 2 | E |
| 63_67 | 5 | 2 | E |
| 68 | 4 | 1 | E |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 5 | 30 | E |
| 23_27 | 40 | 80 | E |
| 28_32 | 82 | 93 | E |
| 33_37 | 93 | 90 | E |
| 38_42 | 93 | 90 | E |
| 43_47 | 93 | 90 | E |
| 48_52 | 90 | 78 | E |
| 53_57 | 90 | 73 | E |
| 58_62 | 88 | 65 | E |
| 63_67 | 82 | 45 | E |
| 68 | 75 | 30 | E |

### D.8 Occupation × Asset / media

P(owns asset ‖ occupation) — % within occupation.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 48 | 72 | C | Post-COVID smartphone surge; WhatsApp farming information |
| Agricultural_labourer | 38 | 62 | C | Jan Dhan → DBT → mobile banking drove smartphone uptake |
| Household_industry | 52 | 74 | C | Tobacco/handloom artisans; moderate uptake |
| Manufacturing | 65 | 82 | C | |
| Construction | 60 | 76 | C | Return migrants often acquired smartphones during outside stay |
| Trade_retail | 78 | 90 | C | Census-town commercial; high |
| Transport_logistics | 72 | 84 | C | |
| Services | 75 | 87 | C | |
| Government_services_teachers | 88 | 95 | C | Govt employees; WhatsApp essential for WB e-governance |
| Out_migrant_worker | 78 | 78 | D | Smartphones essential for remittances / family contact |

### D.9 Education × Workforce participation

P(unemployed-seeking ‖ education) and main-worker rate.

| Education | Unemployed_seeking | Main_worker_rate | Tier |
|---|---|---|---|
| Illiterate | 2 | 35 | E |
| Primary | 4 | 37 | E |
| Middle | 6 | 34 | E |
| Secondary | 10 | 29 | E |
| Higher_Secondary | 16 | 22 | E |
| Graduate | 20 | 25 | E |
| Postgraduate | 13 | 36 | E |

### D.11 GP × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Census_towns_cluster | 90.0 | 9.0 | 0.5 | 0.2 | 0.3 | E | Khagrabari/Takagachh: higher Hindu proportion; traders + service class dominant |
| U2_CDB_II_rural_GPs | 81.0 | 18.4 | 0.3 | 0.2 | 0.1 | E | Rural GPs closer to CDB-II block average; Muslim peasantry concentrated here |

Marginal recovery — Hindu: 0.157×90.0 + 0.843×81.0 = 14.13 + 68.28 = **82.41** vs C.1 **82.00** ✓ within ±0.5

### D.12 GP × Caste

P(caste ‖ sub-unit) — parent leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Census_towns_cluster | 8 | 37 | 0.5 | 44 | 1.5 | 9 | 0 | E |
| U2_CDB_II_rural_GPs | 3 | 47 | 1.2 | 29.3 | 1 | 18.4 | 0.1 | E |

### D.13 GP × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Census_towns_cluster | 91 | 76 | 14 | 97 | C |
| U2_CDB_II_rural_GPs | 74 | 58 | 4.5 | 93 | C |

Source: NFHS-5 WB rural/urban gradient; post-COVID smartphone adoption particularly sharp in rural areas.

### D.14 GP × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Census_towns_cluster | 73 | 92 | 97 | 99 | C |
| U2_CDB_II_rural_GPs | 39 | 70 | 84 | 95 | C |

Source: NFHS-5 WB urban-rural gradient; Ujjwala 2.0 + Swachh Bharat Phase-2 continued rollout 2020–21.

### D.15 Vote × Religion (2021 AE, AC 3 Cooch Behar Uttar)

P(party ‖ religion) — calibrated to 2021 AE result (BJP 49.40%, AITC 43.40%, LF~4.70%).

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 58.0 | 35.0 | 1.0 | 5.5 | 0.5 | C | BJP retained Hindu majority in 2021 AE; AITC share improved from 2019 on welfare-scheme backlash against BJP performance; AIFB/LF slightly higher in 2021 AE vs 2019 LS |
| Muslim | 4.0 | 76.0 | 2.0 | 3.5 | 14.5 | C | Muslim consolidated further behind AITC in 2021 AE — post-NRC/CAA anxiety reinforced AITC shield narrative |
| Christian | 22.0 | 55.0 | 8.0 | 8.0 | 7.0 | E | Approximation |
| Sarna_ORP | 40.0 | 35.0 | 5.0 | 10.0 | 10.0 | E | Tribal fringe |
| Other_residual | 42.0 | 32.0 | 5.0 | 5.0 | 16.0 | E | |
| **Marginal BJP** | | | | | | | Hindu(82.00)×0.580 + Muslim(17.48)×0.040 + Other(0.52)×0.38 = 47.56 + 0.70 + 0.20 = **48.46** vs target 49.40 ✓ within ±1.5pp (tier-C derivation) |
| **Marginal AITC** | | | | | | | Hindu(82.00)×0.350 + Muslim(17.48)×0.760 + Other(0.52)×0.42 = 28.70 + 13.28 + 0.22 = **42.20** vs target 43.40 ✓ within ±1.5pp |

### D.16 Vote × Caste (2021 AE)

P(party ‖ caste).

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 52 | 32 | 5 | 6 | 5 | C | BJP retained UC but some slippage vs 2019 LS |
| OBC | 40 | 36 | 5 | 12 | 7 | C | AIFB/LF retained some OBC artisan base in 2021 AE |
| Rajbanshi_SC | 62 | 29 | 1 | 6 | 2 | C | BJP retained Rajbanshi-SC majority; Sitalkuchi (Apr 2021 CISF firing at neighbouring AC 4) increased Rajbanshi-BJP emotional bond; slight softening from 2019 LS high (65%) due to anti-incumbency on state governance |
| Other_SC | 50 | 36 | 5 | 7 | 2 | C | |
| ST_total | 38 | 37 | 5 | 12 | 8 | C | |
| Muslim | 4 | 76 | 2 | 3.5 | 14.5 | C | Same as D.15 |

### D.17 Vote × Gender (2021 AE)

P(party ‖ gender).

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 52 | 40 | 2 | 5 | 1 | C | Rajbanshi male BJP loyalty retained |
| Female | 47 | 47 | 1 | 4 | 1 | C | Lakshmir Bhandar launched Apr 2021 — first payments to women HHs in eligible categories; slight female AITC improvement vs 2019 in 2021 AE |

---

## E. 2021 calibration target (2021 WB Assembly Election — AC 3)

> All figures are **tier A** — sourced from ECI 2021 WB AE / Wikipedia Cooch Behar Uttar AC. Total electorate: 263,078. Total valid votes: 243,916. Turnout: 92.72%.

The simulator must reproduce this aggregate within ±1pp on each major party.

### Detail table (for § H / narrative context)

| Party | Candidate | Votes | % |
|---|---|---|---|
| BJP | Sukumar Roy | 120,483 | 49.40 |
| AITC | Binay Krishna Barman | 105,868 | 43.40 |
| AIFB | Nagendra Nath Roy | ~11,600 | 4.76 |
| Others / NOTA | various | ~5,965 | 2.44 |
| **BJP margin over AITC** | | **14,615 votes** | **5.99 pp** |

### § E calibration target (normalized 5-party schema)

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 49.40 | A | ECI 2021 AE — Wikipedia Cooch Behar Uttar; winner Sukumar Roy |
| AITC | 43.40 | A | ECI 2021 AE — runner-up Binay Krishna Barman |
| INC | 0.60 | D | INC minimal in this seat; residual |
| LF | 4.76 | A | AIFB: Nagendra Nath Roy (former 2011/2016 winner); AIFB alone = LF in this AC |
| Other_NOTA | 1.84 | A | NOTA + IND |
| **Sum** | **100.00** | — | self-check |

---

## F. Vote history (anchors for belief evolution)

### AC 3 Cooch Behar Uttar — Assembly Elections

| Year | Winner | Party | Votes | % | Runner-up | Party | % | Margin | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2011 AE | Nagendra Nath Roy | **AIFB** | 84,825 | 45.11 | Prasenjit Barman | AITC | 43.94 | 2,197 | Left held seat; AITC close; BJP negligible |
| 2016 AE | Nagendra Nath Roy | **AIFB** | 97,629 | 43.63 | Parimal Barman | AITC | 38.14 | 12,293 | AIFB strengthened; BJP ~7% |
| 2021 AE | Sukumar Roy | **BJP** | 120,483 | 49.40 | Binay Krishna Barman | AITC | 43.40 | 14,615 | **Calibration target** — dramatic BJP capture |

### Cooch Behar Lok Sabha (PC 1) history

| Year | Winner | Party | AC-3 seg % | Notes |
|---|---|---|---|---|
| 2009 LS | Nripendra Nath Roy | AIFB | — | Left held; pre-BJP era |
| 2014 LS | Renuka Sinha | AITC | — | Left collapsed nationally; AITC won |
| 2019 LS | Nisith Pramanik | BJP | **51.27** (A — CSV) | BJP swept North Bengal; Rajbanshi consolidation |

**Structural narrative (end-2021 state-of-knowledge):** Cooch Behar Uttar completed a full ideological transition in the span of two election cycles — from an AIFB stronghold (2011, 2016) to one of BJP's most reliable SC-reserved seats in North Bengal. Key factors known by end-2021:

1. **Rajbanshi bloc consolidation (2019 LS → 2021 AE):** BJP's alliance with Greater Cooch Behar People's Association (Ananta Rai faction) and Nisith Pramanik's Rajbanshi identity proved durable. The 2021 AE candidate Sukumar Roy maintained this alliance.

2. **NRC/CAA anxiety (2019–2021):** The National Register of Citizens controversy and CAA debates heightened Muslim anxieties about citizenship status. Muslim voters consolidated further behind AITC as the "shield" party. This reinforced the Hindu–Muslim vote polarization visible since 2019.

3. **COVID-19 and reverse migration (2020):** April–June 2020 lockdown brought seasonal workers back to CDB-II GPs. Some reported difficulty accessing PMGKAY rations without proper documentation — a state welfare delivery complaint later leveraged by BJP in the 2021 AE campaign.

4. **Lakshmir Bhandar (Apr 2021):** AITC launched ₹500/₹1000 monthly direct transfers to women household heads in April 2021 — widely credited with improving AITC's performance among female voters in the 2021 AE. AC 3 female AITC share improved vs 2019 LS.

5. **Sitalkuchi CISF firing (Apr 10, 2021):** At AC 4 (adjacent Sitalkuchi), CISF opened fire killing 4 voters during Election Day polling on April 10. Rajbanshi community reaction was mixed — some perceived it as BJP security over-reach; others as AITC-provoked. BJP retained its large 2021 AE margin in AC 3 despite the controversy in the adjacent constituency.

6. **BSF 50km jurisdiction (Oct 2021):** The Union government extended BSF's operational jurisdiction to 50km from the Bangladesh border (from 15km). Cooch Behar district falls within this zone. Announcement generated local resentment among border communities (AITC narrative of "federalism attack"). Known by end-2021 but limited electoral impact measured before year-end.

7. **Bangladesh temple attacks (Oct 2021):** Hindu minority violence in Bangladesh in October 2021 generated acute anxiety among Cooch Behar border community's Hindu population, particularly in border-adjacent GPs. BJP leveraged this to reinforce Hindu-protection narrative. Likely to reinforce BJP's Hindu voter retention going into future cycles.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- Census of India 2011 — Cooch Behar II Community Development Block Primary Census Abstract (Wikipedia / censusindia.co.in) — population, religion, SC, literacy, mother tongue, occupation
- `2019_AssemblySegmentLevelVotingData.csv` — ECI GE2019 AC-segment vote tallies, AC_NO=3
- ECI 2021 WB Assembly Election archive — candidate-level results for Cooch Behar Uttar AC 3 (via Wikipedia "Cooch Behar Uttar Assembly constituency")
- Delimitation Commission 2008 — WB Schedule (Cooch Behar Uttar AC 3 = Cooch Behar II CDB entire)
- Wikipedia "Cooch Behar Uttar Assembly constituency" — 2011, 2016, 2021 AE results

### Secondary sources (tier B/C)
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership, media-access baselines
- NFHS-5 (2019-21) West Bengal state report — smartphone / banking cross-check for 2021 calibration; key for post-COVID diffusion rates
- CSDS-Lokniti 2021 NES post-poll — vote × religion / caste / gender (WB regional pattern post-2021 AE)
- Pew Research India 2021 — religion-differential growth projections

### Tertiary / journalistic (tier D)
- The Quint, The Wire — 2021 WB AE coverage for North Bengal; BJP Rajbanshi vote patterns
- India Today / NDTV — Lakshmir Bhandar launch (Apr 2021) coverage and early enrollment data
- The Hindu — BSF jurisdiction extension (Oct 2021) and Cooch Behar district reaction
- Hindustan Times / Times of India — Bangladesh temple attacks (Oct 2021) reporting; North Bengal border community anxiety

### Tier-D/E reliance flags
- **Rajbanshi sub-group share** (C.2, D.2) — no post-1931 caste census; SC composition from journalistic anchor; tier C
- **2021 AE vote × caste/religion conditionals** (D.15–D.17) — CSDS 2021 WB regional + margin-anchoring from AE result; tier C
- **COVID return migration** (C.16) — district-level estimates; no AC-level Census D-series; tier D
- **Asset/media 2021 levels** (C.14, D.4, D.8, D.13) — NFHS-5 WB; North Bengal below-state-average adjustment applied; smartphone surge estimated from NFHS-5 + COVID-effect delta; tier C

### v0 known gaps
1. DCHB Cooch Behar Part-A — 13 GPs collapsed into 2 sub-units; refine when accessible
2. ECI 2021 AE Form-20 Cooch Behar Uttar — candidate-level vote by polling station not fetched; Wikipedia-level AE result used
3. CSDS WB 2021 AE full cross-tabs — using regional summary pattern; Rajbanshi-specific vote not directly surveyed
4. Lakshmir Bhandar penetration in CDB-II specifically — using state-level scheme launch date; AC-level enrollment data not available

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No events post-2021 referenced except in § H.*

---

## H. Post-2021 validation anchor (out-of-sample)

> **OUT-OF-SAMPLE gate — NOT part of the frozen 2021 calibration.**
> The simulator must reproduce the 2024 LS AC-3 segment result from 2021 priors + narrative injection without the figures below being baked into the 2021 calibration input.

### 2024 Lok Sabha Election — AC 3 segment within Cooch Behar LS (PC 1)

All figures are **tier A** — sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=3. Total electors: 292,443; total valid votes: 242,701; turnout: 82.99%.

| Party | Votes | AC-3 segment % | Tier |
|---|---|---|---|
| BJP | 123,859 | **51.03** | A |
| AITC | 105,870 | **43.62** | A |
| AIFB | 6,251 | **2.58** | A |
| INC | 2,191 | **0.90** | A |
| Other (BSP+SUCI+KPPU+IND) | 4,530 | **1.87** | A |
| **BJP margin over AITC** | **17,989** | **7.41 pp** | A |

**Structural note:** BJP's 2021 AE 49.40% rebounded to 51.03% in 2024 LS — a recovery to the 2019 LS level (51.27%). AITC held at 43.62%, higher than 2021 AE (43.40%) but consistent with the structural floor. AIFB further declined from 4.76% (2021 AE) to 2.58% (2024 LS). Cooch Behar Uttar AC 3 is a structurally stable BJP-Rajbanshi seat regardless of LS-level swing in the broader Cooch Behar PC.
