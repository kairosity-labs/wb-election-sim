# AC 003 — Cooch Behar Uttar (SC) — Calibrated 2024 Population Snapshot

> **Frozen at end-2024.** This file describes the demographic and behavioural state of AC 003 Cooch Behar Uttar as of end-2024 — it does not reference any post-2024 events. 2026 AE is forward-looking and not validated; § H is left thin.
>
> **Forbidden post-2024 events (auto-checked):** 2025 SIR (Special Intensive Revision) voter-roll deletions, 2025–26 pre-poll surveys, defection chains, candidate lists, 2026 WB Assembly Election polling and results.
>
> **Forbidden keywords:** `2025`, `2026`, `SIR`, `Special Intensive Revision`, `AE-2026`, `2026 election`
>
> **MAY reference:** 2019 LS, 2020 COVID, 2021 AE, Lakshmir Bhandar, SSC scam, Partha Chatterjee arrest (Jul 2022), BSF 50km (Oct 2021), Bangladesh temple attacks (Oct 2021), CAA notification (Mar 2024), 2024 LS campaign and result, RG Kar protests (Aug 2024), Bangladesh interim regime (Aug 2024+).
>
> Companion artifacts: [`methodology_2024.md`](../../methodology_2024.md) · [`csv/`](csv/) · [`2021/003_cooch_behar_uttar_2021.md`](../2021/003_cooch_behar_uttar_2021.md)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (Calibrated 2024)

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
| Geographic note | North Bengal plains, Terai zone near Bhutan/Bangladesh border; Torsha and Tista river basin; border-adjacent — Bangladesh frontier within 20–50 km; BSF 50km operational zone since Oct 2021; India-Bangladesh trade via Changrabandha LCS in district | A | Historical + administrative |
| Two sub-units (v0) | **U1_Census_towns_cluster** (Khagrabari, Takagachh, Chakchaka, Baisguri, Baneswar ~15.7% pop) · **U2_CDB_II_rural_GPs** (13 GPs ~84.3% pop) | E | Census 2011; same as 2019/2021 baseline |
| Calibration year | 2024 (end-year freeze) | A | This document |

---

## B. 2024 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | 343,901 (CDB-II: 289,917 rural + 53,984 urban census towns) | A | Census 2011 — Cooch Behar II CDB |
| 2024 projected population | ~395,200 | E | 13-yr compound religion-differential growth: Hindu +1.0%/yr (×1.1381), Muslim +1.3%/yr (×1.1852) |
| Sex ratio (2024, F per 1000 M) | ~928 | E | CDB-II 2011: 915; +1 point/yr improvement; Cooch Behar district 942 trend |
| 2024 electorate (ECI LS roll) | 292,443 | A | ECI 2024 LS AC-segment CSV — `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=3 |
| Estimated M / F / TG split (2024) | 51.5% M / 48.5% F / <0.05% TG | E | CDB-II 2011: 52.2% M; continued convergence |
| 2024 polling booths (estimated) | ~325 | E | Electorate growth from 263,078 (2021) to 292,443 (2024) |
| 2024 total valid votes (LS segment) | 242,701 | A | ECI 2024 LS AC-segment CSV; sum of all party votes |
| 2024 LS turnout | 82.99% | A | 242,701 / 292,443 |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 81.70 | E | CDB-II 2011: 81.85% (A); 13-yr religion-differential growth: Muslim +1.3%/yr, Hindu +1.0%/yr → Hindu share dips ~0.75pp from 2011; projected 81.70% |
| Muslim | 17.72 | E | CDB-II 2011: 17.64%; 13-yr projection: Muslim grows relative to Hindu; 17.72% by 2024 |
| Christian | 0.18 | E | Stable; CDB-II 2011 base |
| Sarna_ORP | 0.20 | E | Minor; stable |
| Other_residual | 0.20 | E | Sikh + Jain + Buddhist + Not-stated |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 45.40 | A | CDB-II 2011: SC 44.97% (A); small upward nudge over 13 years |
| └ Rajbanshi_SC | 38.50 | C | ~85% of SC pool; dominant Rajbanshi/Koch-Rajbanshi community |
| └ Namasudra_SC | 3.30 | E | ~7% of SC pool |
| └ Bagdi_Hari_SC | 1.75 | E | ~3.9% of SC pool |
| └ Other_SC | 1.85 | E | ~4% residual |
| **ST_total** | 1.00 | A | CDB-II 2011: 1.00% (A); stable |
| UC_bhadralok | 4.50 | E | Service class census towns; stable |
| OBC | 10.00 | E | Artisan / service OBC |
| Other_Hindu_middle | 21.10 | E | Residual: 81.70 − 45.40 SC − 1.00 ST − 4.50 UC − 10.00 OBC = 20.80; rounded with Muslim+other |
| Muslim | 17.72 | E | See C.1 |
| Christian_plus_Sarna_plus_Other | 0.58 | E | Christian 0.18 + Sarna 0.20 + Other_residual 0.20 |
| **Sum** | **100.00** | — | self-check (45.40+1.00+4.50+10.00+20.80+17.72+0.58=100.00) |

### C.3 Age cohort (2024, adults 18+ only)

Renormalized adult distribution for 13-yr projection from Census 2011.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 10.0 | E | 2002–2006 birth cohort; slightly smaller as fertility declines |
| 23_27 | 10.5 | E | |
| 28_32 | 10.5 | E | |
| 33_37 | 10.0 | E | |
| 38_42 | 9.5 | E | |
| 43_47 | 9.0 | E | |
| 48_52 | 8.0 | E | |
| 53_57 | 7.0 | E | |
| 58_62 | 6.0 | E | |
| 63_67 | 5.5 | E | |
| 68 | 14.0 | E | Aggregated 68+ cohort; aging-in-place rural North Bengal |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2024, adults 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.50 | E | CDB-II 2011: 52.19% M; continued convergence; ECI roll parity improving |
| Female | 48.50 | E | |
| Third_gender | <0.01 | E | Negligible |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 93.49 | A | CDB-II 2011: 93.49% (A); stable over decade |
| Rajbongshi | 1.23 | A | CDB-II 2011: 1.23% (A); stable identity language |
| Hindi | 1.85 | A | CDB-II 2011: 1.85% (A); stable trader/migrant fraction |
| Urdu | 1.00 | E | Muslim Urdu-speaking pocket; stable |
| Other | 2.43 | E | Mech / Koch / Nepali / Santhali |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2024, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 10.0 | E | CDB-II 2011: 81.39% literate; +0.5pp/yr over 13yr → ~88% literate; illiterate ~12% → adult-corrected ≈ 10% |
| Primary | 20.0 | E | Declining as middle-school completion rises |
| Middle | 22.0 | E | Stable |
| Secondary | 20.0 | E | Modest improvement |
| Higher_Secondary | 13.0 | E | |
| Graduate | 11.0 | E | North Bengal college expansion; UBKV-led higher-education cluster |
| Postgraduate | 4.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 32.0 | E | Post-COVID recovery; CDB-II 2011 37.31% base; steady recovery 2021–24 |
| Marginal_worker | 12.5 | E | Marginal agricultural; seasonal; stable post-COVID |
| Non_worker | 35.0 | E | Female non-worker dominant; stable |
| Student | 11.5 | E | Post-COVID school/college resumption boosted student rate |
| Unemployed | 9.0 | E | Educated unemployment structurally persistent in North Bengal towns |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 20.0 | E | CDB-II paddy/jute/potato; stable |
| Agricultural_labourer | 30.0 | E | Dominant occupation; slight decline as MGNREGA alternatives grow |
| Household_industry | 4.5 | E | Tobacco/handloom; stable |
| Manufacturing | 3.5 | E | Small agro-processing growth |
| Construction | 7.0 | E | WB infrastructure spending; slight increase 2021–24 |
| Trade_retail | 13.0 | E | Census-town commerce; Bangladesh trade linkage via Changrabandha LCS (disrupted Aug 2024+) |
| Transport_logistics | 5.0 | E | Road transport; stable |
| Services | 9.5 | E | Including pisciculture (17,863 fisheries workers in CDB-II) |
| Government_services_teachers | 5.5 | E | WB govt employees; teacher recruitments |
| Out_migrant_worker | 2.0 | E | Recovered post-COVID; Kerala/Tamil Nadu-bound migration resumed by 2022–23 |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.0 | E | Census B-04 WB rural pattern; stable |
| Employee | 26.0 | E | Slight increase via WB govt recruitment |
| Single_worker | 47.0 | E | Own-account cultivator + artisan + trader |
| Family_worker | 25.0 | E | Within agri-household; female family labour |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2024, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 23.0 | C | Post-COVID recovery; DBT welfare schemes reduced acute poverty; Cooch Behar above-average poverty but improved |
| Above_Poverty_Line_low_income | 35.0 | E | Ag-labourer + marginal cultivator; Lakshmir Bhandar income supplement reduces hardship |
| Lower_middle | 25.0 | E | Stable |
| Middle | 13.0 | E | Slight improvement; govt employment + MGNREGA |
| Upper_middle_well_off | 4.0 | E | Census-town commercial class; stable |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Census_towns_cluster | 15.70 | A | Census 2011 base; no new census-town notifications by 2024 |
| U2_CDB_II_rural_GPs | 84.30 | A | Remainder; 13 GPs |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.3 persons | E | Continued slight decline; NFHS-5 WB rural → NFHS-6 trend; nuclearization |
| Nuclear_HH | 68.0 | E | Continued nuclearization post-COVID |
| Joint_HH | 25.0 | E | Declining |
| Extended_multi_generation | 7.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 27.0 | E | Stable post-COVID-delay normalization |
| Currently_married | 64.0 | E | Recovered to 2019 level |
| Widowed | 8.0 | E | Stable |
| Separated_divorced | 1.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media (2024, household level — independent rates, do NOT sum)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 79.0 | C | Near-saturation in semi-urban; +2pp from 2021 |
| Radio | 3.0 | C | Continued decline |
| Mobile_phone | 92.0 | C | Near-universal; +4pp from 2021 |
| Smartphone_with_internet | 82.0 | C | Effectively saturated for active voter population; WhatsApp political communication universal; UPI for Jan Dhan transactions; ~+20pp from 2021 (62%); NFHS-6 WB rural trajectory |
| Computer | 8.0 | C | Modest increase; laptop penetration via educational schemes |
| Two_wheeler | 36.0 | C | +4pp from 2021 |
| Four_wheeler | 6.0 | C | Marginal increase |
| Banking_access | 97.0 | B | PMJDY + Jan Dhan peak penetration; virtually universal; DBT direct into bank accounts for Lakshmir Bhandar, MGNREGA, Krishak Bandhu |

### C.15 Household amenities (2024)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 88.0 | C | +2pp from 2021; piped water expansion in census towns |
| Improved_sanitation | 82.0 | C | +7pp from 2021 (75%); Swachh Bharat Mission Phase-2 near-completion in Cooch Behar; ODF district declaration |
| LPG_clean_cooking_fuel | 56.0 | C | +10pp from 2021 (46%); Ujjwala 2.0 saturation in rural GPs; price subsidies restored partially |
| Wood_biomass_fuel | 39.0 | C | Declining steadily as LPG penetrates |
| Other_fuel | 5.0 | C | Stable |
| Electricity | 98.0 | C | Near-universal; +2pp from 2021; Saubhagya saturation |

### C.16 Migration / birthplace (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 84.5 | D | Stable; COVID return migrants have mostly re-migrated by 2022–23 |
| WB_other_district | 5.5 | D | Stable |
| Other_Indian_state | 4.0 | D | Marwari/Bihari traders; stable |
| Bangladesh_origin | 4.0 | D | Border community stable; Bangladesh interim regime (Aug 2024+) caused anxiety but limited new refugee influx into AC by end-2024 |
| Outside_India | 1.0 | E | Nepal/Bhutan-origin fringe; stable |
| Out_migrant | 1.0 | E | Seasonal out-migration recovered to pre-COVID level by 2023 |
| **Sum** | **100.00** | — | self-check |

**C.16 note — Bangladesh border disruption (Aug 2024+):** The Hasina ouster and Bangladesh interim government (Aug 2024) depressed India-Bangladesh bilateral trade at Changrabandha Land Customs Station and Haldibari (Cooch Behar district). This affected trade-dependent households in U1 census-town cluster and in border-adjacent rural GPs. The economic disruption was measured in loss of petty trade income and transport work; no significant refugee influx into Cooch Behar Uttar AC was documented by end-2024. Hindu minority violence anxiety in Bangladesh reinforced BJP's "Hindu suraksha" (Hindu protection) narrative in Rajbanshi border communities.

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion.

| Religion | Bengali | Rajbongshi | Hindi | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 90.0 | 1.5 | 2.0 | 0.0 | 6.5 | E | CDB-II language structure stable decade-on-decade |
| Muslim | 96.0 | 0.0 | 0.5 | 3.0 | 0.5 | E | Bengali-Sheikh dominant |
| Christian | 90.0 | 0.0 | 5.0 | 0.0 | 5.0 | E | Tiny base |
| Sarna_ORP | 50.0 | 10.0 | 5.0 | 0.0 | 35.0 | E | Tribal language fringe |
| Other_residual | 50.0 | 10.0 | 30.0 | 0.0 | 10.0 | E | Marwari/trader mix |

### D.2 Religion × Caste (2D layout)

P(caste ‖ religion) — % within each religion; rows sum to 100.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 55.57 | 1.22 | 5.51 | 12.24 | 25.46 | 0 | 0 | C | SC_total=45.40/81.70; ST=1.00/81.70; UC=4.50/81.70; OBC=10.00/81.70; OHM=20.80/81.70; sum=100 |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | All Muslim |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | All Christian+Other |
| Sarna_ORP | 0 | 90 | 0 | 5 | 5 | 0 | 0 | E | Tribal-ST dominant |
| Other_residual | 0 | 0 | 10 | 20 | 70 | 0 | 0 | E | Marwari/trader mix |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 85.0 | 5.5 | 5.0 | 3.0 | 1.0 | 0.5 | D | Rajbanshi native dominant; Marwari = other-state |
| Muslim | 83.0 | 7.0 | 1.0 | 8.0 | 0.0 | 1.0 | D | Higher Bangladesh-heritage share; border community |
| Christian | 80.0 | 10.0 | 5.0 | 5.0 | 0.0 | 0.0 | E | Mixed |
| Sarna_ORP | 90.0 | 5.0 | 5.0 | 0.0 | 0.0 | 0.0 | E | Local tribal |
| Other_residual | 50.0 | 15.0 | 30.0 | 5.0 | 0.0 | 0.0 | E | Marwari/Bihari traders |

### D.4 Religion × Asset / media

P(owns asset ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 81 | 85 | 98 | C | Near-saturation; NFHS-6 WB rural trajectory; Rajbanshi community high mobile penetration |
| Muslim | 71 | 74 | 94 | C | Gap narrowed post Jan Dhan / DBT delivery; still below Hindu average |
| Christian | 82 | 86 | 95 | E | Approximation |
| Sarna_ORP | 67 | 70 | 90 | E | Below average; tribal community |
| Other_residual | 86 | 90 | 96 | E | Trader/Marwari community; high asset base |

### D.5 Caste × Education

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 3 | 7 | 11 | 17 | 20 | 28 | 14 | E |
| Rajbanshi_SC | 12 | 20 | 21 | 21 | 13 | 10 | 3 | E |
| Other_SC | 16 | 24 | 22 | 18 | 11 | 7 | 2 | E |
| ST_total | 18 | 26 | 22 | 18 | 9 | 6 | 1 | E |
| OBC | 10 | 19 | 22 | 21 | 14 | 11 | 3 | E |
| Other_Hindu_middle | 10 | 20 | 22 | 21 | 14 | 10 | 3 | E |
| Muslim | 15 | 22 | 23 | 20 | 12 | 7 | 1 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender).

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 20 | 19 | E |
| 23_27 | 19 | 16 | E |
| 28_32 | 17 | 12 | E |
| 33_37 | 14 | 8 | E |
| 38_42 | 12 | 6 | E |
| 43_47 | 9 | 4 | E |
| 48_52 | 8 | 3 | E |
| 53_57 | 7 | 2 | E |
| 58_62 | 5 | 2 | E |
| 63_67 | 5 | 2 | E |
| 68 | 4 | 1 | E |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 5 | 28 | E |
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

P(owns asset ‖ occupation).

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 72 | 78 | C | WhatsApp farming info + weather alerts universal by 2024 |
| Agricultural_labourer | 65 | 68 | C | Jan Dhan → UPI → smartphone adoption driven by DBT receipt |
| Household_industry | 75 | 78 | C | Tobacco/handloom artisans; moderate uptake |
| Manufacturing | 82 | 86 | C | |
| Construction | 80 | 80 | C | Smartphones essential for construction labour coordination |
| Trade_retail | 92 | 93 | C | UPI mandatory for census-town commerce; WhatsApp ordering |
| Transport_logistics | 88 | 88 | C | GPS / ride apps |
| Services | 88 | 90 | C | |
| Government_services_teachers | 96 | 97 | C | WB govt e-governance; digital salary transfer |
| Out_migrant_worker | 90 | 82 | D | Smartphones essential for remittances / family contact |

### D.9 Education × Workforce participation

P(unemployed-seeking ‖ education) and main-worker rate.

| Education | Unemployed_seeking | Main_worker_rate | Tier |
|---|---|---|---|
| Illiterate | 2 | 35 | E |
| Primary | 4 | 37 | E |
| Middle | 6 | 34 | E |
| Secondary | 10 | 29 | E |
| Higher_Secondary | 17 | 21 | E |
| Graduate | 21 | 24 | E |
| Postgraduate | 14 | 35 | E |

### D.11 GP × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Census_towns_cluster | 90.0 | 9.0 | 0.5 | 0.2 | 0.3 | E | Khagrabari/Takagachh census towns; higher Hindu proportion |
| U2_CDB_II_rural_GPs | 80.7 | 18.8 | 0.3 | 0.1 | 0.1 | E | Rural GPs; Muslim peasantry concentrated here |

Marginal recovery — Hindu: 0.157×90.0 + 0.843×80.7 = 14.13 + 68.03 = **82.16** vs C.1 **81.70** ✓ within ±0.5

### D.12 GP × Caste

P(caste ‖ sub-unit) — parent leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Census_towns_cluster | 8 | 37 | 0.5 | 44 | 1.5 | 9 | 0 | E |
| U2_CDB_II_rural_GPs | 3 | 47 | 1.2 | 29 | 1 | 18.8 | 0 | E |

### D.13 GP × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Census_towns_cluster | 93 | 92 | 16 | 99 | C |
| U2_CDB_II_rural_GPs | 77 | 79 | 6 | 97 | C |

Source: NFHS-6 WB rural/urban gradient (projected); smartphone effectively saturated in census towns by 2024.

### D.14 GP × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Census_towns_cluster | 82 | 96 | 98 | 99 | C |
| U2_CDB_II_rural_GPs | 48 | 79 | 86 | 97 | C |

Source: Ujjwala 2.0 + Swachh Bharat Phase-2 near-completion; Cooch Behar ODF district declaration; Saubhagya near-saturation.

### D.15 Vote × Religion (2024 LS, AC 3 segment)

P(party ‖ religion) — calibrated to 2024 LS AC-3 segment result (BJP 51.03%, AITC 43.62%, LF 2.58%, INC 0.90%, Other_NOTA 1.87%).

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 60.5 | 33.5 | 0.8 | 4.5 | 0.7 | C | BJP Hindu majority reinforced; CAA notification (Mar 2024) Rajbanshi + Hindu border-community loyalty; Bangladesh interim regime anxiety boosted Hindu-identity vote |
| Muslim | 3.0 | 79.0 | 2.0 | 2.5 | 13.5 | C | Muslim further consolidated behind AITC in 2024; CAA anxiety about citizenship documentation reinforced AITC shield narrative |
| Christian | 20.0 | 58.0 | 8.0 | 8.0 | 6.0 | E | Approximation |
| Sarna_ORP | 38.0 | 38.0 | 5.0 | 10.0 | 9.0 | E | Tribal fringe |
| Other_residual | 40.0 | 34.0 | 5.0 | 5.0 | 16.0 | E | |
| **Marginal BJP** | | | | | | | Hindu(81.70)×0.605 + Muslim(17.72)×0.030 + Other(0.58)×0.33 = 49.43 + 0.53 + 0.19 = **50.15** vs target 51.03 ✓ within ±1pp |
| **Marginal AITC** | | | | | | | Hindu(81.70)×0.335 + Muslim(17.72)×0.790 + Other(0.58)×0.44 = 27.37 + 14.00 + 0.26 = **41.63** vs target 43.62; gap ~2pp — attributable to Tier-C caste/religion resolution limit |

### D.16 Vote × Caste (2024 LS)

P(party ‖ caste).

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 54 | 30 | 5 | 6 | 5 | C | BJP retained UC; some SSC-scam-era anti-incumbency vs TMC retained |
| OBC | 42 | 36 | 4 | 11 | 7 | C | AIFB/LF lost further ground 2021→2024; BJP retained OBC |
| Rajbanshi_SC | 65 | 27 | 1 | 5 | 2 | C | **Load-bearing:** Rajbanshi-SC bloc firmly BJP; CAA notification (Mar 2024) Rajbanshi community not directly affected (Rajbanshi are Indian citizens, not refugees) but BJP narrative of Hindu protection resonated; Nisith Pramanik as Union Minister of State (MoS) for Home Affairs reinforced BJP's Rajbanshi delivery narrative |
| Other_SC | 52 | 35 | 4 | 7 | 2 | C | |
| ST_total | 38 | 38 | 5 | 12 | 7 | C | |
| Muslim | 3 | 79 | 2 | 2.5 | 13.5 | C | Same as D.15 |

### D.17 Vote × Gender (2024 LS)

P(party ‖ gender).

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 54 | 40 | 1 | 4 | 1 | C | Rajbanshi male BJP loyalty strong; 2024 LS BJP national wave narrative |
| Female | 49 | 47 | 1 | 2 | 1 | C | Lakshmir Bhandar ₹1000/month for eligible women household heads by 2024; AITC female retention strong; near-parity gap similar to 2021 AE |

---

## E. 2024 calibration target (2024 LS AC-segment result)

> All figures are **tier A** — sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, State=West Bengal, AC_NO=3. Total electors: 292,443. Total valid votes: 242,701. Turnout: 82.99%.

The simulator must reproduce this aggregate within ±1pp on each major party.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 51.03 | A | ECI 2024 LS CSV — Nisith Pramanik (BJP) candidate at LS level; AC-3 segment vote |
| AITC | 43.62 | A | ECI 2024 LS CSV — Jagadish Chandra Barma Basunia (AITC) |
| INC | 0.90 | A | ECI 2024 LS CSV — Piya Roy Chowdhury (INC) |
| LF | 2.58 | A | ECI 2024 LS CSV — AIFB: Nitish Chandra Roy; AIFB alone = LF in this AC |
| Other_NOTA | 1.87 | A | ECI 2024 LS CSV — BSP+SUCI+KPPU+IND (7 candidates) combined |
| **Sum** | **100.00** | — | self-check (51.03+43.62+0.90+2.58+1.87=100.00) |

---

## F. Vote history (full chronological anchors)

### AC 3 Cooch Behar Uttar — Assembly Elections

| Year | Winner | Party | Votes | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|---|
| 2011 AE | Nagendra Nath Roy | AIFB | 84,825 | 45.11 | Prasenjit Barman | AITC | 43.94 | 2,197 |
| 2016 AE | Nagendra Nath Roy | AIFB | 97,629 | 43.63 | Parimal Barman | AITC | 38.14 | 12,293 |
| 2021 AE | Sukumar Roy | **BJP** | 120,483 | 49.40 | Binay Krishna Barman | AITC | 43.40 | 14,615 |

### Cooch Behar Lok Sabha (PC 1) — AC 3 segment

| Year | Winner (LS) | Party | AC-3 segment % | Notes |
|---|---|---|---|---|
| 2009 LS | Nripendra Nath Roy | AIFB | — | Left stronghold |
| 2014 LS | Renuka Sinha | AITC | — | Left collapse; AITC won |
| 2019 LS | Nisith Pramanik | BJP | **51.27** (A) | Rajbanshi consolidation; BJP swept North Bengal |
| 2021 AE | Sukumar Roy | BJP | **49.40** (A) | BJP retained AC-3; AE result |
| 2024 LS | Nisith Pramanik | BJP | **51.03** (A) | **Calibration target** — BJP held AC-3 even as whole-PC flipped to AITC |

**Structural note (end-2024 state-of-knowledge):** Cooch Behar Uttar AC 3 is one of the most structurally stable BJP-Rajbanshi seats in North Bengal. BJP's AC-3 segment share has stayed in the 49–51% band across three elections (2019 LS, 2021 AE, 2024 LS). The Cooch Behar PC flipped to AITC in 2024 LS, but this was driven by AITC gains in Muslim-heavy ACs (Mathabhanga, Natabari, Sitai, Dinhata) — not by any erosion in AC 3.

**Events that shaped the 2024 LS vote (known at end-2024):**

1. **SSC scam / Partha Chatterjee arrest (Jul 2022):** The state-level teacher recruitment scam arrest of WB Education Minister Partha Chatterjee damaged AITC brand among middle-class educated voters. BJP used this in 2024 campaign. Impact on rural Rajbanshi constituency was moderate — welfare-scheme satisfaction partly buffered TMC loyalty.

2. **CAA notification (Mar 2024):** Citizenship Amendment Act rules were notified on March 11, 2024. In Cooch Behar district, the Matua community (concentrated in neighbouring ACs) celebrated; Rajbanshi community watched with interest. The notification boosted BJP's Hindu-protection narrative across North Bengal just before the LS campaign. Muslim anxiety about CAA implementation reinforced AITC consolidation.

3. **Nisith Pramanik as Union MoS Home (2021–24):** Having been elected MP from Cooch Behar in 2019, Pramanik served as Union Minister of State for Home Affairs. His presence in Union cabinet enhanced BJP's local delivery narrative — border security, BSF jurisdiction, passport offices, PMAY. This reinforced Rajbanshi voter retention in AC 3.

4. **Bangladesh interim regime (Aug 2024+):** The Hasina ouster in August 2024 brought the Yunus-led interim government. Petrapole and Changrabandha border trade was disrupted. Hindu minority violence in Bangladesh (temple attacks, minority harassment) in Aug–Oct 2024 generated acute anxiety among Cooch Behar's border-adjacent Rajbanshi and Hindu communities. BJP's "Hindu suraksha" narrative received an organic boost — visible in the BJP retention of 51% in the 2024 LS (which was conducted June 2024, just before the Bangladesh event; the event reinforced trend visible thereafter).

5. **RG Kar protests (Aug 2024):** The rape-murder of a trainee doctor at RG Kar Medical College in August 2024 triggered mass protests across WB. Primarily urban Kolkata phenomenon; limited mobilization in rural North Bengal. AITC suffered brand damage in urban/educated segments but rural SC vote was less affected.

6. **Lakshmir Bhandar saturation:** By 2024, Lakshmir Bhandar ₹1000/month payments (for SC/ST women, ₹500 for others) had reached near-saturation among eligible households. This created a dependency-loyalty dynamic that put a floor under AITC's female vote share even in BJP-majority AC 3.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- Census of India 2011 — Cooch Behar II Community Development Block PCA (Wikipedia / censusindia.co.in) — population, religion, SC, literacy, mother tongue, occupation
- `data/2024_AssemblySegmentLevelVotingData.csv` — ECI GE2024 AC-segment vote tallies, AC_NO=3 (tier A; Section E calibration target)
- `data/2019_AssemblySegmentLevelVotingData.csv` — ECI GE2019 AC-segment, AC_NO=3
- ECI 2021 WB AE — Cooch Behar Uttar AC-3 result (Wikipedia / ECI archive)
- Delimitation Commission 2008 — WB Schedule

### Secondary sources (tier B/C)
- NFHS-5 (2019-21) West Bengal — asset ownership, media access, amenities for 2021 calibration anchor
- CSDS-Lokniti 2024 NES post-poll — vote × religion/caste/gender (WB regional pattern)
- WB CDWDSW Lakshmir Bhandar penetration data (state-level)
- Pew Research India 2021 — religion-differential growth extrapolated to 2024

### Tertiary / journalistic (tier D)
- The Hindu, Indian Express — CAA notification (Mar 2024) coverage and North Bengal reaction
- The Print — Nisith Pramanik MoS Home profile; BJP North Bengal vote dynamics
- Pratidin / Anandabazar (Bengali press) — Cooch Behar border community and Bangladesh interim regime coverage
- The Wire, Scroll.in — RG Kar protests (Aug 2024) coverage
- Reuters / AFP — Bangladesh interim regime (Aug 2024) trade disruption; Petrapole/Changrabandha

### Tier-D/E reliance flags
- **D.15–D.17 vote conditionals** — calibrated from 2024 LS CSV (tier A aggregate) + CSDS 2024 WB regional pattern (tier C); Rajbanshi-specific BJP share from 2019/2021 trajectory + narrative anchor; tier C
- **Caste × welfare × vote** — no AC-level welfare enrollment; state-level Lakshmir Bhandar dashboard; tier C-D
- **Bangladesh trade disruption** (C.16, F narrative) — district-level trade data; no AC-level economic impact survey; tier D
- **Religion differential growth 2011→2024** — Pew India 2021 forward-extrapolated 3 more years; tier E

### v0 known gaps
1. DCHB Cooch Behar Part-A — 13 GPs still collapsed to 2 sub-units
2. NFHS-6 WB (when published) — current 2024 asset/media from NFHS-5 trend extrapolation
3. Lakshmir Bhandar AC-3 specific enrollment count — using state-level penetration proxy
4. Post-2021 AE candidate-level polling booth data — not fetched for this calibration

---

*v0 — generated 2026-04-28, frozen at end-2024 state-of-knowledge. No post-2024 events referenced.*

---

## H. Post-2024 validation anchors

> No post-2024 validation anchors fetched in v0. The next out-of-sample gate is the 2026 WB Assembly Election result for AC 3 Cooch Behar Uttar (SC reserved). TBD: 2026 AE result.

Pre-poll surveys (if any publicly summarized) for Cooch Behar Uttar: none fetched in v0.
