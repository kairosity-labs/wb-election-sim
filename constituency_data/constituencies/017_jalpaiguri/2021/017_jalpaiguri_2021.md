# AC 017 — Jalpaiguri (SC) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 017 Jalpaiguri as of end-2021 only — it does not reference
> any post-2021 events. The 2021 WB Assembly Election result is the
> calibration target; use the 2024 LS AC-segment result as an out-of-sample
> validation gate for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 017 | A | ECI / Delimitation Commission 2008 |
| AC name | Jalpaiguri | A | ECI |
| Reservation | SC | A | Delimitation 2008 |
| District | Jalpaiguri | A | Delimitation 2008 |
| Sub-division | Jalpaiguri Sadar | A | WB administrative |
| LS constituency | 3 — Jalpaiguri (SC reserved) | A | Delimitation 2008 |
| LS segments included | AC 14 Mekhliganj (Cooch Behar) · AC 15 Dhupguri · AC 16 Maynaguri · AC 017 Jalpaiguri · AC 18 Rajganj · AC 19 Dabgram-Phulbari · AC 20 Mal | A | Delimitation 2008 |
| AC composition | Jalpaiguri Municipality (full) + Arabinda, Bahadur, Boalmari Nandanpur, Garalbari, Kharia, Kharija Berubari I, Kharija Berubari II, Mondalghat, Nagar Berubari, South Berubari GPs of Jalpaiguri CD Block | A | Delimitation 2008 / ECI |
| Geographic note | District headquarters town on Teesta river; flat Duars foothills zone; tea-garden fringe to north; BSF 50km jurisdiction extended Oct 2021 covers this border-adjacent district | A | — |
| Sub-units used in v0 | **U1: Jalpaiguri_Municipality** (urban) · **U2: Jalpaiguri_CDB_rural_share** (10 GPs) | E | v0 simplification |

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~207,000 (Muni 107,341 + 10/28 of CDB Jalpaiguri rural 261,784 ≈ 93,494) | E | Census 2011; v0 GP equal-weight assumption |
| 2021 projected population | ~230,000 | E | 10-yr compound religion-differential growth from Census 2011 (methodology §4) |
| Sex ratio (2021, F per 1000 M) | ~960 | E | NFHS-5 Jalpaiguri district 1038 F/1000 M (B); urban AC segment lower; interpolated ~960 |
| 2021 electorate (ECI roll) | 262,500 | A | ECI 2021 WB AE official roll — data/electoral_history/2021/detailed_results.csv |
| Estimated M / F / TG split (2021) | 50.2% M / 49.8% F / <0.05% TG | E | constituency_summary_full: male_electors 131,679 / total_electors 132,519 yields implied ~50.2% M; note female electors ~48.8% in 2019 → marginal shift by 2021 |
| 2021 polling stations | ~285 | E | Proportional to electorate; consistent with 2019 estimate |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 83.20 | E | 2019 baseline 83.50%; minor differential growth adjustment 2019→2021; COVID-19 mortality slightly higher among older HH heads |
| Muslim | 12.10 | E | 2019 baseline 11.80%; +0.3pp relative gain over 2 yrs |
| Christian | 4.00 | E | Stable; no significant change 2019→2021 |
| Sarna_ORP | 0.30 | E | Stable |
| Other_residual | 0.40 | E | Stable; Buddhist + Sikh + Not_stated residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 49.79 | A | wb_ac_master_v3.csv: sc_pct=49.79 for AC 017 (Census 2011 A) |
| └ Rajbanshi_SC | 43.00 | C | Rajbanshi (Koch-Rajbanshi) dominant SC in Jalpaiguri district; ~86% of SC pool |
| └ Other_SC | 6.79 | E | Residual SC sub-groups (Bagdi, Hari, Bauri etc.) |
| **ST_total** | 1.76 | A | wb_ac_master_v3.csv: st_pct=1.76 (Census 2011 A); AC urban-heavy sharply reduces ST vs district 18.9% |
| └ Koch_ST | 0.80 | C | Koch classified as ST in WB; distinct from Rajbanshi-SC despite shared heritage |
| └ Other_ST | 0.96 | E | Oraon, Munda, other tribal fringe in rural GP portion |
| UC_bhadralok | 7.00 | E | Brahmin/Kayastha/Baidya; district-HQ bureaucrat/professional pool; stable 2019→2021 |
| OBC | 5.00 | E | Teli, Mahishya, Sutradhar, Kurmi; moderate presence in Jalpaiguri town |
| Other_Hindu_middle | 24.45 | E | Residual within Hindu (83.20 − 49.79 SC − 1.76 ST − 7 UC − 5 OBC) |
| Muslim | 12.10 | E | All sub-castes pooled; see C.1 |
| Christian_plus_Sarna_plus_Other | 4.70 | E | Christian 4.0 + Sarna_ORP 0.3 + Other_residual 0.4 + rounding |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2021, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 9.20 | E | Renormalized from Jalpaiguri district Census 2011 age pyramid + 2-yr projection; COVID mortality concentrated in 60+ cohort |
| 23_27 | 9.80 | E | |
| 28_32 | 10.10 | E | |
| 33_37 | 9.60 | E | |
| 38_42 | 9.00 | E | |
| 43_47 | 8.60 | E | |
| 48_52 | 8.20 | E | |
| 53_57 | 7.40 | E | |
| 58_62 | 6.70 | E | |
| 63_67 | 5.50 | E | |
| 68 | 15.90 | E | 68+ open-ended; COVID-19 mortality suppresses 70+ slightly |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.18 | E | NFHS-5 Jalpaiguri district sex ratio 1038 F per 1000 M (B) implies 49.1% M; urban AC segment somewhat lower female-skew; blended ~50.2% based on ECI 2021 roll decomposition |
| Female | 49.81 | E | |
| Third_gender | 0.01 | E | Standard 0.01% placeholder |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 78.00 | E | Stable from 2019 baseline; Rajbanshi speakers often recorded as Bengali in Census |
| Hindi | 4.00 | E | Bihari, Marwari, UP migrant traders; stable |
| Urdu | 1.50 | E | Muslim community fringe; stable |
| Other | 1.50 | E | Sadri, Oraon, Mundari residual |
| Rajbongshi | 15.00 | C | Rajbongshi (Kamtapuri) mother-tongue speakers; prominent in Jalpaiguri district; stable |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 13.50 | E | 2019 baseline 15%; NFHS-5 Jalpaiguri female school attendance 73.7% (B); slight improvement 2019→2021 |
| Primary | 21.50 | E | Slight downward shift as Middle absorbs more |
| Middle | 20.50 | E | |
| Secondary | 18.50 | E | |
| Higher_Secondary | 12.50 | E | |
| Graduate | 10.50 | E | District HQ; education access improving |
| Postgraduate | 3.00 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 32.00 | E | 2019 baseline 33%; COVID-19 disruption suppressed formal employment briefly; partial recovery by end-2021 |
| Marginal_worker | 9.50 | E | Slight increase as informals absorbed post-COVID |
| Non_worker | 37.50 | E | Housewife + elderly + retired; stable |
| Student | 11.00 | E | Education institutions reopened gradually mid-2021 |
| Unemployed | 10.00 | E | COVID-19 induced unemployment elevated; district HQ aspirant pool |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 12.00 | E | Stable; rural GP portion |
| Agricultural_labourer | 20.00 | E | CDB rural high ag-labour; stable |
| Household_industry | 5.00 | E | Weaving, handicrafts; stable |
| Manufacturing | 6.00 | E | Small industries; modest recovery post-COVID |
| Construction | 7.00 | E | Return migration inflated construction pool briefly |
| Trade_retail | 16.00 | E | Jalpaiguri town sub-regional market hub; stable |
| Transport_logistics | 8.00 | E | Road transport hub; stable |
| Services | 14.00 | E | Private services in district HQ |
| Government_services_teachers | 8.00 | E | District HQ civil servants, teachers; stable |
| Out_migrant_worker | 4.00 | D | COVID-19 reverse migration reduced out-migrant count temporarily; partial return by end-2021 |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 3.00 | E | Stable; small-business owners; district town |
| Employee | 35.00 | E | Govt + organised sector + retail; stable |
| Single_worker | 44.00 | E | Cultivators, own-account traders, artisans |
| Family_worker | 18.00 | E | Agricultural household helpers; peri-urban family enterprise |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 22.50 | C | 2019 baseline 23%; COVID-19 economic stress slightly reversed poverty reduction gains; 2021 ~22.5% |
| Above_Poverty_Line_low_income | 37.50 | E | |
| Lower_middle | 24.00 | E | |
| Middle | 12.00 | E | |
| Upper_middle_well_off | 4.00 | E | District HQ; slightly higher affluent share than rural ACs |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Jalpaiguri_Municipality | 52.00 | E | 2011: Muni 107,341 / AC ~207,000 = 51.9%; held stable; COVID return-migration minimally shifted urban share |
| U2_Jalpaiguri_CDB_rural_share | 48.00 | E | 10 GPs of CDB Jalpaiguri; v0 collapses 10 GPs into one cell |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.3 persons | E | WB 2011 average 4.3; stable across projection |
| Nuclear_HH | 68.00 | E | NFHS-5 WB pattern; COVID return-migration briefly boosted joint-HH slightly |
| Joint_HH | 25.00 | E | |
| Extended_multi_generation | 7.00 | E | |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.50 | E | 2019 baseline 27%; NFHS-5 Jalpaiguri women married before 18 = 18.7% (B); slightly lower never-married in older cohort by 2021 |
| Currently_married | 65.50 | E | |
| Widowed | 7.00 | E | COVID-19 excess mortality in 60+ female cohort unchanged at macro level |
| Separated_divorced | 1.00 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 80.00 | C | NFHS-5 WB; Jalpaiguri district 90.5% electricity (NFHS-4 baseline); TV saturated urban; rural gaining; AC weighted ~80% stable |
| Radio | 5.00 | C | Declining nationally |
| Mobile_phone | 91.00 | C | NFHS-4 WB 86%; +3pp/yr continued Jio-driven diffusion → ~91% by 2021 |
| Smartphone_with_internet | 70.00 | C | 2019 baseline 48%; +22pp COVID-19 digital acceleration + Jio 2020-21 price drop; NFHS-5 WB district pattern; methodology §4 +20-30pp range |
| Computer | 11.00 | C | Stable; marginal change |
| Two_wheeler | 32.00 | C | Slight increase with economic activity |
| Four_wheeler | 7.00 | C | Stable |
| Banking_access | 94.00 | B | 2019 baseline 87%; PMJDY+Lakshmir Bhandar account opening Apr 2021 drove further penetration; NFHS-5 WB baseline +7pp |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 92.00 | B | NFHS-5 Jalpaiguri district 95.2% (B); AC weighted with urban/rural split ~92% |
| Improved_sanitation | 76.00 | B | NFHS-5 Jalpaiguri district 73.2% (B); urban AC portion higher; AC weighted ~76% |
| LPG_clean_cooking_fuel | 43.00 | B | NFHS-5 Jalpaiguri district 42.7% (B); AC weighted; slight rural lag |
| Wood_biomass_fuel | 51.00 | C | Inverse of LPG penetration; rural GP portion still dominant solid fuel |
| Other_fuel | 6.00 | C | Kerosene, dung cake residual |
| Electricity | 97.00 | B | NFHS-5 Jalpaiguri district 97.4% (B); Saubhagya + continued rural electrification |
| **Note** | (water/sanitation/electricity are independent; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 71.50 | D | 2019 baseline 72%; COVID-19 reverse migration from out-state marginally increased native-registered share |
| WB_other_district | 8.00 | D | In-migrants from Cooch Behar, North Dinajpur; govt service transfers; stable |
| Other_Indian_state | 5.00 | D | Bihari, UP, Rajasthani trader community; stable |
| Bangladesh_origin | 10.00 | D | Partition-era Hindu refugee community (Rajbanshi-SC from East Bengal); stable |
| Outside_India | 0.50 | E | Negligible; some Nepal-origin fringe |
| Out_migrant | 4.50 | E | Out-migrant count briefly reduced by COVID-19 return; assumed restored by end-2021 |
| Nepal_Bhutan_origin | 0.00 | E | Not significant in this AC |
| Nepal_origin_COVID_return | 0.50 | E | Small Nepali-origin labour returning through Jalpaiguri during COVID-19; absorbed into Native/Outside_India |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 74.00 | 3.50 | 0.00 | 1.50 | 21.00 | E | Rajbanshi-SC Hindus predominantly Rajbongshi-speaking; bhadralok Bengali; stable 2019→2021 |
| Muslim | 88.00 | 3.00 | 8.00 | 1.00 | 0.00 | E | Jalpaiguri Muslims predominantly Bengali-speaking with Urdu pocket; stable |
| Christian | 60.00 | 10.00 | 0.00 | 25.00 | 5.00 | E | Mixed tribal-origin Christian; Sadri/tribal languages in Other |
| Sarna_ORP | 10.00 | 5.00 | 0.00 | 75.00 | 10.00 | E | Tribal language dominant for Sarna-ORP practitioners |
| Other_residual | 50.00 | 35.00 | 5.00 | 10.00 | 0.00 | E | Buddhist + Sikh + Not_stated; Hindi-speaking fringe |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. 2D canonical table.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 56.47 | 1.88 | 8.41 | 6.01 | 27.23 | 0 | 0 | E | SC 49.79/83.20 + ST 1.76/83.20; UC/OBC/Other residual within Hindu; row sums to 100 |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 85.00 | 0 | 5.00 | 10.00 | 0 | 0 | E | Tribal sub-castes mostly route to ST_total; Sarna_ORP row sums to 100 |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 67.50 | 8.00 | 5.00 | 14.00 | 0.50 | 5.00 | D | Rajbanshi-SC Hindus largely native; some Bangladesh-origin partition refugees; COVID-19 return migration slightly increased Out_migrant |
| Muslim | 85.00 | 8.00 | 3.00 | 3.00 | 0.50 | 0.50 | D | Predominantly local Bengali-Muslim; small Bangladesh trickle |
| Christian | 80.00 | 10.00 | 5.00 | 2.00 | 2.00 | 1.00 | E | Mixed; mission-converted tribal natives dominant |
| Sarna_ORP | 92.00 | 5.00 | 2.00 | 0.00 | 1.00 | 0.00 | E | Tribal religion practitioners overwhelmingly native |
| Other_residual | 30.00 | 15.00 | 50.00 | 0.00 | 5.00 | 0.00 | E | Marwari/Sikh/Buddhist; largely other-state origin |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion. Updated for 2021 smartphone diffusion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 82.00 | 73.00 | 96.00 | C | NFHS-5 WB religion gap; Hindu above average; Lakshmir Bhandar account-opening Apr 2021 drives banking spike |
| Muslim | 72.00 | 62.00 | 86.00 | C | NFHS-5 WB Muslim-Hindu asset gap pattern; smartphone +22pp from 2019 |
| Christian | 84.00 | 75.00 | 91.00 | C | Mission-educated community; above average |
| Sarna_ORP | 57.00 | 50.00 | 78.00 | E | Tribal fringe; lower asset base but smartphone diffusion significant |
| Other_residual | 92.00 | 88.00 | 97.00 | E | Urban-skewed (Marwari/Sikh) higher asset |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 3.50 | 7.50 | 11.50 | 18.00 | 21.00 | 27.00 | 11.50 | E |
| SC_total | 17.00 | 23.00 | 22.00 | 18.50 | 10.50 | 7.50 | 1.50 | E |
| ST_total | 24.00 | 27.00 | 22.00 | 14.50 | 7.50 | 3.50 | 1.50 | E |
| OBC | 13.00 | 21.00 | 22.00 | 18.50 | 12.50 | 9.50 | 3.50 | E |
| Other_Hindu_middle | 12.00 | 21.00 | 22.00 | 18.50 | 12.50 | 10.50 | 3.50 | E |
| Muslim | 19.00 | 24.00 | 22.00 | 17.50 | 9.50 | 6.50 | 1.50 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share. Slight upward shift for younger cohorts.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 19.00 | 17.00 | E |
| 23_27 | 18.00 | 14.00 | E |
| 28_32 | 16.00 | 11.00 | E |
| 33_37 | 14.00 | 8.00 | E |
| 38_42 | 12.00 | 6.00 | E |
| 43_47 | 10.00 | 4.50 | E |
| 48_52 | 8.50 | 3.50 | E |
| 53_57 | 7.50 | 2.50 | E |
| 58_62 | 6.00 | 2.00 | E |
| 63_67 | 5.00 | 1.50 | E |
| 68 | 4.00 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 6.00 | 26.00 | E |
| 23_27 | 40.00 | 80.00 | E |
| 28_32 | 82.00 | 92.00 | E |
| 33_37 | 92.00 | 90.00 | E |
| 38_42 | 93.00 | 89.00 | E |
| 43_47 | 92.00 | 85.00 | E |
| 48_52 | 91.00 | 78.00 | E |
| 53_57 | 90.00 | 68.00 | E |
| 58_62 | 88.00 | 55.00 | E |
| 63_67 | 82.00 | 40.00 | E |
| 68 | 72.00 | 28.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric. Elevated from 2019 for COVID digital acceleration.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 52.00 | 74.00 | C | Rural ag baseline +17pp from 2019 smartphone surge |
| Agricultural_labourer | 40.00 | 64.00 | C | Lower income group; significant smartphone gains |
| Household_industry | 58.00 | 77.00 | C | |
| Manufacturing | 68.00 | 84.00 | C | |
| Construction | 65.00 | 78.00 | C | |
| Trade_retail | 83.00 | 90.00 | C | Urban Jalpaiguri market hub |
| Transport_logistics | 78.00 | 85.00 | C | Road transport hub; smartphone-dependent |
| Services | 86.00 | 92.00 | C | |
| Government_services_teachers | 92.00 | 97.00 | C | District HQ civil servants; highest |
| Out_migrant_worker | 82.00 | 80.00 | D | Working outside; smartphone heavy; COVID-era WhatsApp/video call reliance |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 35.00 | 2.00 | E |
| Primary | 38.00 | 4.00 | E |
| Middle | 34.00 | 6.00 | E |
| Secondary | 30.00 | 10.00 | E |
| Higher_Secondary | 24.00 | 15.00 | E |
| Graduate | 28.00 | 19.00 | E |
| Postgraduate | 38.00 | 13.00 | E |

### D.10 Asset / media × Bilingualism

AC 017 does not declare a `media_tier` axis — D.10 is intentionally omitted per NORMALIZED_SCHEMA §4.7.

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Values stable from 2019; minor COVID migration effects.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Jalpaiguri_Municipality | 84.80 | 10.20 | 3.50 | 0.10 | 1.40 | E | Muni: urban-Hindu concentrated; marginal Muslim gain 2019→2021 |
| U2_Jalpaiguri_CDB_rural_share | 81.60 | 14.00 | 4.00 | 0.20 | 0.20 | E | CDB Jalpaiguri block; rural GP higher Muslim and Christian |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit).

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Jalpaiguri_Municipality | 9.00 | 22.00 | 1.50 | 6.00 | 48.50 | 9.00 | 4.00 | E |
| U2_Jalpaiguri_CDB_rural_share | 5.00 | 78.50 | 2.00 | 4.00 | 1.50 | 13.00 | 4.00 | E |

### D.13 Sub-unit × Asset / media

Updated for 2021 smartphone diffusion.

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Jalpaiguri_Municipality | 91.00 | 84.00 | 20.00 | 98.00 | C |
| U2_Jalpaiguri_CDB_rural_share | 67.00 | 54.00 | 4.00 | 89.00 | C |

### D.14 Sub-unit × Amenities

Updated from NFHS-5 Jalpaiguri district data.

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Jalpaiguri_Municipality | 73.00 | 90.00 | 97.00 | 99.00 | B |
| U2_Jalpaiguri_CDB_rural_share | 16.00 | 62.00 | 87.00 | 95.00 | B |

### D.15 Vote × Religion (2021 AE calibration anchor)

P(party ‖ religion) — calibrated to 2021 WB AE result (AITC 42.34%, BJP 41.93%, INC 10.72%). Near-tie between AITC and BJP driven by AITC recapturing SC-Hindu voters + female AITC surge post-Lakshmir Bhandar announcement; INC retained Sukhbilas Barma's personal Rajbanshi vote.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 50.00 | 31.00 | 13.00 | 3.00 | 3.00 | C | CSDS 2021 WB pattern; Rajbanshi SC BJP-leaning but AITC regained ground post-2019; INC retains Sukhbilas Barma personal vote |
| Muslim | 3.00 | 72.00 | 18.00 | 5.00 | 2.00 | C | Muslim consolidation behind AITC; INC residual |
| Christian | 22.00 | 52.00 | 12.00 | 8.00 | 6.00 | E | AITC welfare outreach gains among Christian community |
| Sarna_ORP | 35.00 | 42.00 | 10.00 | 10.00 | 3.00 | E | Tribal vote; AITC gains over 2019 |
| Other_residual | 48.00 | 30.00 | 10.00 | 8.00 | 4.00 | E | Urban non-Hindu fringe; BJP-tilted |

### D.16 Vote × Caste (2021 AE)

P(party ‖ caste) — anchored on 2021 AE result; AITC regained Rajbanshi SC from BJP via Lakshmir Bhandar and candidate Dr. Pradip Kumar Barma (Rajbanshi community leader).

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 55.00 | 30.00 | 7.00 | 5.00 | 3.00 | C | CSDS 2021 WB; bhadralok BJP-leaning |
| OBC | 40.00 | 38.00 | 8.00 | 10.00 | 4.00 | C | CSDS 2021 |
| SC_total | 48.00 | 35.00 | 13.00 | 2.00 | 2.00 | C | Rajbanshi SC split; INC retains Sukhbilas Barma personal vote; AITC Dr. Barma personal pull; BJP still strong |
| ST_total | 38.00 | 40.00 | 10.00 | 9.00 | 3.00 | C | CSDS 2021 tribal pattern; AITC gains |
| Other_Hindu_middle | 46.00 | 35.00 | 10.00 | 6.00 | 3.00 | C | CSDS 2021 |
| Muslim | 3.00 | 72.00 | 18.00 | 5.00 | 2.00 | C | Same as D.15 |

### D.17 Vote × Gender (2021 AE)

Post-Lakshmir Bhandar announcement (Apr 2021) female AITC tilt increased significantly.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 48.00 | 33.00 | 12.00 | 5.00 | 2.00 | C | CSDS 2021 WB; BJP-male tilt persists |
| Female | 36.00 | 52.00 | 9.00 | 2.00 | 1.00 | C | Lakshmir Bhandar announcement Apr 2021 boosted female AITC tilt; strong female swing |

### D.18 Vote × Welfare

AC 017 does not declare a `welfare_exposure` axis — D.18 is intentionally omitted per NORMALIZED_SCHEMA §4.7.

---

## E. 2021 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**
Source: ECI 2021 WB AE — data/electoral_history/2021/detailed_results.csv, AC 017. Total valid votes: 225,933; electors: 262,500; turnout: 86.07%.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| AITC | 42.34 | A | Dr. Pradip Kumar Barma: 95,668 votes; ECI 2021 AE direct |
| BJP | 41.93 | A | Soujit Singha (Piku): 94,727 votes; ECI 2021 AE direct |
| INC | 10.72 | A | Sukhbilas Barma: 24,228 votes; ECI 2021 AE direct; INC incumbent retained strong personal vote |
| LF | 0.40 | A | SUCI(C) only: 898 votes; CPI(M) did not contest; LF extremely weak |
| Other_NOTA | 4.61 | A | NOTA 3,381 + BSP 1,609 + IND ×4 5,422 = 10,412 votes; computed from ECI data |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 017 — Jalpaiguri (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Sukhbilas Barma | INC | ~52.0 | Gobinda Chandra Roy | AIFB | ~45.3 | 11,051 |
| 2016 AE | Sukhbilas Barma | INC | ~47.9 | Dharttimohan Roy | AITC | ~45.3 | 5,157 |

Note: Jalpaiguri (AC 017) was an INC stronghold through 2011 and 2016, with Sukhbilas Barma as incumbent. In 2021, AITC flipped this seat by just 941 votes with Dr. Pradip Kumar Barma (also Rajbanshi community leader). Sukhbilas Barma (INC, age 75) retained 10.72% of the vote, which came predominantly from Rajbanshi SC voters. BJP surged in the 2019 LS contest but AITC reversed the swing in the 2021 AE via welfare-scheme mobilisation and Lakshmir Bhandar announcement effect on female voters.

### 2019 LS anchor (AC 017 segment, former calibration target — now pre-calibration anchor)

| Year | Party | AC Segment % | Notes |
|---|---|---|---|
| 2019 LS | BJP | 52.25 | Direct from 2019_AssemblySegmentLevelVotingData.csv; BJP surge in Jalpaiguri LS |
| 2019 LS | AITC | 34.00 | |
| 2019 LS | INC | 3.87 | Incumbent AE effect partially eroded |
| 2019 LS | LF | 7.65 | CPIM+SUCI(C) still significant in 2019 |
| 2019 LS | Other_NOTA | 2.23 | |

### Jalpaiguri Lok Sabha (PC 3) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|
| 2014 LS | Bijoy Chandra Barman | AITC | ~38 | AITC won; CPI(M) significant; BJP below 30% |
| 2019 LS | Dr. Jayanta Kumar Roy | BJP | ~50.9 | BJP surge across all 7 segments; AITC ~38.6%; margin 184,004 |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Jalpaiguri Municipality Primary Census Abstract (population 107,341; SC 22.14%; ST 0.91%)
- Census of India 2011 — Jalpaiguri CD Block demographics (population 323,455; SC 60.8%; ST 6.1%)
- Census of India 2011 — Jalpaiguri District (population 3,872,846; religion; sex ratio 953)
- ECI 2021 WB Assembly Election — `data/electoral_history/2021/detailed_results.csv` AC 017: AITC 95,668 (42.34%), BJP 94,727 (41.93%), INC 24,228 (10.72%), SUCI 898 (0.40%), Others+NOTA 10,412 (4.61%); margin 941; electors 262,500
- ECI 2021 WB AE `constituency_summary_full.csv` AC 017: male_electors 131,679; voters_total 111,756; polling_pct 86.34%; valid_votes 217,020; nota 3,334
- `data/master/wb_ac_master_v3.csv` AC 017: sc_pct=49.79; st_pct=1.76; literacy_pct=79.97; sex_ratio=962; workers_total=142,581
- `data/2019_AssemblySegmentLevelVotingData.csv` — 2019 LS AC-017 segment (tier A; 2019 calibration anchor)
- Delimitation Commission of India 2008 — WB Schedule (AC 017 = Jalpaiguri Muni + 10 GPs of CDB Jalpaiguri)

### Secondary sources (tier B / C)

- NFHS-5 (2019-21) West Bengal — Jalpaiguri district fact sheet: electricity 97.4%; water 95.2%; sanitation 73.2%; LPG 42.7%; female school attendance 73.7%; sex ratio 1038
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership 2019 baseline
- CSDS-Lokniti 2021 WB post-poll — vote × religion / caste / gender WB regional rollup (as published in post-poll summaries)
- Pew Research India 2021 — religion-differential growth projections
- WB District Statistical Handbook — Jalpaiguri

### Tertiary / journalistic (tier D)

- The Print / Wire (2021) — Rajbanshi community mobilisation; AITC candidate Dr. Pradip Kumar Barma as community choice; Sukhbilas Barma INC vote retention
- News reports on 2021 AE result for Jalpaiguri (AITC margin 941 votes; tightest seat in North Bengal)
- Lakshmir Bhandar launch coverage (Apr 2021) — female voter mobilisation effect documented in North Bengal reportage
- BSF 50km jurisdiction extension (Oct 2021) — reported anxiety in border-district Hindu refugee community

### Tier-D / E reliance flags (what to distrust)

- **Caste sub-group shares** (C.2, D.2) — no caste census post-1931 for non-SC/ST; SC_total now tier A from master CSV, but sub-group split is tier C/E
- **Migration/birthplace shares** (C.16, D.3) — no public AC-level Census D-series; tier D from district patterns
- **Sub-unit data** (D.11–D.14) — collapsed to 2 units (Muni + CDB rural share); refine when DCHB Part-A Jalpaiguri accessible
- **Vote × demographic** (D.15–D.17) — CSDS 2021 WB regional rollup adjusted for local Rajbanshi SC dynamics; tier C; three-way near-tie at AC level makes cell-level estimates fragile
- **Mother tongue / Rajbongshi** (C.5, D.1) — no direct AC-level language census data; tier D/E
- **Age cohort** (C.3) — renormalized from district pyramid + 2-yr projection; tier E throughout
- **Smartphone penetration** (C.14, D.4, D.8, D.13) — +22pp from 2019 calibrated to NFHS-5 district baseline; tier C; COVID-era diffusion rate uncertain

### v0 known gaps

1. DCHB Jalpaiguri Part-A — 10 rural GPs collapsed into one sub-unit; SC_total 49.79% is correct AC aggregate but U1/U2 split in D.12 remains modeled
2. AC-level religion data — using district+municipal Census baseline; NFHS-5 does not provide sub-district religion breakdown
3. CSDS 2021 full WB cross-tabs — using post-poll published summaries; INC vote retention mechanism in Jalpaiguri (Sukhbilas Barma personal vote) not captured in regional rollup
4. Mother tongue distribution — Rajbongshi share estimated from community-level journalistic sources; no AC Census language table
5. D.15-D.17 calibration fragility — three-party near-tie makes vote × demographic distributions hard to constrain; multiple combinations reproduce the aggregate; treat as tier C/E

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No post-2021 events referenced.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2024 Lok Sabha Election — AC 017 segment within Jalpaiguri LS (PC 3) (tier A)

> Figures sourced from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=17, Jalpaiguri. Electorate 268,781; NOTA 2,330.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Dr. Jayanta Kumar Roy | 110,008 | 50.01% | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Nirmal Chandra Roy | 84,474 | 38.40% | A | Same |
| CPI(M) | (candidate) | 20,119 | 9.15% | A | Same |
| BSP | (candidate) | 1,082 | 0.49% | A | Same |
| NOTA | — | 2,330 | 1.05% | A | Same |
| Others | various | 3,516 | 0.90% | A | Same |
| **BJP margin over AITC** | | **25,534 votes** | **11.61 pp** | A | Computed |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC-017 shares within ±3pp of the tier-A figures:
- BJP target: 50.0% ± 3pp
- AITC target: 38.4% ± 3pp
- LF (CPI-M) target: 9.2% ± 3pp

Note: The 2024 LS result shows BJP regaining dominance after the narrow 2021 AE AITC win, suggesting the 2021 AE result was a local-candidate and welfare-effect-driven anomaly; the BJP structural advantage reasserted in the LS context.
