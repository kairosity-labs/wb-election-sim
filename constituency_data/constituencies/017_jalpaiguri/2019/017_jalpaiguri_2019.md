# AC 017 — Jalpaiguri (SC) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 017 Jalpaiguri as of 2019 only — it does not reference
> any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

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
| Geographic note | District headquarters town on Teesta river; flat Duars foothills zone; tea-garden fringe to north | A | — |
| Sub-units used in v0 | **U1: Jalpaiguri_Municipality** (urban) · **U2: Jalpaiguri_CDB_rural_share** (10 GPs) | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~207,000 (Muni 107,341 + 10/28 of CDB Jalpaiguri rural 261,784 ≈ 93,494) | E | Census 2011; v0 GP equal-weight assumption |
| 2019 projected population | ~224,500 | E | 8-yr compound religion-differential growth (methodology §4) |
| Sex ratio (2019, F per 1000 M) | ~953 | E | Jalpaiguri district baseline 953 (A); minimal projection drift |
| 2019 estimated electorate (18+) | ~248,000 | D | Back-derived from 2019 ECI roll 255,369 |
| Estimated M / F / TG split (2019) | 51.2% M / 48.8% F / <0.05% TG | E | District sex ratio back-projection |
| 2019 polling stations (estimated) | ~285 | E | Proportional from 2019 electorate |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 83.50 | E | Jalpaiguri district 81.51% Hindu (Census 2011 A); municipality skews slightly higher Hindu; projected 2011→2019 |
| Muslim | 11.80 | E | District 11.51% (A); AC municipal segment slightly higher; projected +1.3%/yr relative gain |
| Christian | 4.00 | E | District 4.81% (A); urban municipality dilutes Christian share vs tea-belt blocks |
| Sarna_ORP | 0.30 | E | Small tribal community fringe; district ST 18.9% but AC is district-HQ urban-heavy |
| Other_residual | 0.40 | E | Buddhist 1.31% district but low in urban AC; Sikh+Jain+Not_stated residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 42.00 | B | Jalpaiguri municipality 22.14% SC (Census 2011 A); CDB Jalpaiguri block 60.8% SC (A); AC weighted ~42% |
| └ Rajbanshi_SC | 36.00 | C | Rajbanshi (Koch-Rajbanshi) dominant SC in Jalpaiguri district; largest SC community in North Bengal |
| └ Other_SC | 6.00 | E | Residual SC sub-groups (Bagdi, Hari, Bauri etc.) |
| **ST_total** | 4.50 | B | District 18.9% ST but AC is urban/peri-urban; Muni ST 0.91% (A); CDB rural fringe ~8% ST |
| └ Koch_ST | 2.00 | C | Koch classified as ST in WB; distinct from Rajbanshi-SC despite shared heritage |
| └ Other_ST | 2.50 | E | Oraon, Munda, other tribal fringe in rural GP portion |
| UC_bhadralok | 7.00 | E | Brahmin/Kayastha/Baidya; district-HQ bureaucrat/professional pool |
| OBC | 5.00 | E | Teli, Mahishya, Sutradhar, Kurmi; moderate presence in Jalpaiguri town |
| Other_Hindu_middle | 24.00 | E | Residual within Hindu (83.50 − 42 SC − 4.5 ST − 7 UC − 5 OBC) |
| Muslim | 11.80 | E | All sub-castes pooled; see C.1 |
| Christian_plus_Sarna_plus_Other | 5.70 | E | Christian 4.0 + Sarna_ORP 0.3 + Other_residual 0.4 + rounding |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 9.40 | E | Renormalized from Jalpaiguri district Census 2011 age pyramid, adults 18+ only |
| 23_27 | 10.00 | E | |
| 28_32 | 10.20 | E | |
| 33_37 | 9.50 | E | |
| 38_42 | 8.80 | E | |
| 43_47 | 8.50 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.20 | E | |
| 58_62 | 6.80 | E | |
| 63_67 | 5.60 | E | |
| 68 | 16.00 | E | 68+ open-ended; renormalized from Census 2011 after excluding 0–17 |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.18 | E | Jalpaiguri district sex ratio 953 F per 1000 M → 51.18% M / 48.81% F; projected stable |
| Female | 48.81 | E | |
| Third_gender | 0.01 | E | Standard 0.01% placeholder |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 78.00 | E | Jalpaiguri district Bengali-dominant; Rajbanshi speakers often recorded as Bengali in Census; projected stable |
| Hindi | 4.00 | E | Bihari, Marwari, UP migrant traders in Jalpaiguri town |
| Urdu | 1.50 | E | Muslim community, district town fringe |
| Other | 1.50 | E | Sadri, Oraon, Mundari residual |
| Rajbongshi | 15.00 | C | Rajbongshi (Kamtapuri) mother-tongue speakers; often self-identify separately from Bengali; prominent in Jalpaiguri |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 15.00 | E | Jalpaiguri district literacy ~72% (Census 2011 A); urban AC slightly better; 2019 ~85% literate → 15% illiterate |
| Primary | 22.00 | E | Census 2011 education distribution scaled for district |
| Middle | 20.00 | E | |
| Secondary | 18.00 | E | |
| Higher_Secondary | 12.00 | E | |
| Graduate | 10.00 | E | District HQ; higher graduate share than rural ACs |
| Postgraduate | 3.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 33.00 | E | Jalpaiguri CDB main-worker share ~33%; urban municipality boosts this slightly |
| Marginal_worker | 9.00 | E | Lower than purely rural ACs due to urban permanency |
| Non_worker | 37.00 | E | Housewife + elderly + retired |
| Student | 11.00 | E | 18–22 cohort in education; urban college access |
| Unemployed | 10.00 | E | Educated unemployment; district HQ job-aspirant pool |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 12.00 | E | Jalpaiguri CDB rural GP portion; Muni dilutes farm share |
| Agricultural_labourer | 20.00 | E | CDB rural high ag-labour; urban portion lower |
| Household_industry | 5.00 | E | Weaving, handicrafts in peri-urban |
| Manufacturing | 6.00 | E | Small industries in Jalpaiguri town |
| Construction | 7.00 | E | Town expansion; migrant labour |
| Trade_retail | 16.00 | E | Jalpaiguri town is sub-regional market hub |
| Transport_logistics | 8.00 | E | Road transport hub; Teesta bridge; trucking |
| Services | 14.00 | E | Private services in district HQ |
| Government_services_teachers | 8.00 | E | District HQ civil servants, teachers |
| Out_migrant_worker | 4.00 | D | Out-migration to tea belt, construction elsewhere; relatively low vs coastal ACs |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 3.00 | E | Small-business owners; district town |
| Employee | 35.00 | E | Govt + organised sector + retail; elevated by district HQ |
| Single_worker | 44.00 | E | Cultivators, own-account traders, artisans |
| Family_worker | 18.00 | E | Agricultural household helpers; peri-urban family enterprise |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 23.00 | C | Jalpaiguri district poverty ~28% (2011); urban dilution; 2019 ~23% |
| Above_Poverty_Line_low_income | 37.00 | E | |
| Lower_middle | 24.00 | E | |
| Middle | 12.00 | E | |
| Upper_middle_well_off | 4.00 | E | District HQ; slightly higher affluent share than rural ACs |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Jalpaiguri_Municipality | 52.00 | E | 2011: Muni 107,341 / AC ~207,000 = 51.9%; held stable to 2019 |
| U2_Jalpaiguri_CDB_rural_share | 48.00 | E | 10 GPs of CDB Jalpaiguri; v0 collapses 10 GPs into one cell |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.3 persons | E | WB 2011 average 4.3; Jalpaiguri district baseline |
| Nuclear_HH | 68.00 | E | NFHS-4 WB pattern; slightly lower joint HH in urban setting |
| Joint_HH | 25.00 | E | |
| Extended_multi_generation | 7.00 | E | |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 27.00 | E | Census 2011 Jalpaiguri district pattern; large first-time-voter cohort |
| Currently_married | 65.00 | E | |
| Widowed | 7.00 | E | Concentrated in 60+, female-skewed |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 78.00 | C | NFHS-4 WB rural 60%, urban 89%; AC mixed urban-rural weighted ~78% |
| Radio | 6.00 | C | Declining nationally |
| Mobile_phone | 86.00 | C | NFHS-4 WB baseline + Jio rollout 2016-19 |
| Smartphone_with_internet | 48.00 | C | NFHS-4 baseline + Jio diffusion; slightly lower than Kolkata-belt |
| Computer | 11.00 | C | NFHS-4 WB rural 4%, urban 27%; AC weighted |
| Two_wheeler | 30.00 | C | NFHS-4 WB pattern; moderate in North Bengal |
| Four_wheeler | 7.00 | C | District HQ commercial and official vehicles |
| Banking_access | 87.00 | B | PMJDY saturation; NFHS-4 WB baseline + rollout |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 84.00 | C | NFHS-4 WB rural 84%, urban 93%; AC weighted |
| Improved_sanitation | 72.00 | C | NFHS-4 WB + Swachh Bharat 2014-19 rollout |
| LPG_clean_cooking_fuel | 46.00 | C | NFHS-4 WB rural 24%, urban 81%; +Ujjwala 2016-19 (+15pp rural) |
| Wood_biomass_fuel | 48.00 | C | Declining as LPG rises |
| Other_fuel | 6.00 | C | Kerosene, dung cake residual |
| Electricity | 96.00 | A | Census 2011 + Saubhagya 2017-19; high urban electrification |
| **Note** | (water/sanitation/electricity are independent; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 72.00 | D | Jalpaiguri HQ predominantly long-settled Rajbanshi and Bengali native population |
| WB_other_district | 8.00 | D | In-migrants from Cooch Behar, North Dinajpur, other WB districts; govt service transfers |
| Other_Indian_state | 5.00 | D | Bihari, UP, Rajasthani trader community in Jalpaiguri town |
| Bangladesh_origin | 10.00 | D | Partition-era Hindu refugee community (Rajbanshi-SC from East Bengal); moderate presence |
| Outside_India | 0.50 | E | Negligible; some Nepal-origin in fringe |
| Out_migrant | 4.50 | E | Registered here but working elsewhere |
| Nepal_Bhutan_origin | 0.00 | E | Not significant in this AC (more prominent in Darjeeling belt) |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 74.00 | 3.50 | 0.00 | 1.50 | 21.00 | E | Rajbanshi-SC Hindus predominantly Rajbongshi-speaking; bhadralok Bengali; blended estimate |
| Muslim | 88.00 | 3.00 | 8.00 | 1.00 | 0.00 | E | Jalpaiguri Muslims predominantly Bengali-speaking with Urdu pocket |
| Christian | 60.00 | 10.00 | 0.00 | 25.00 | 5.00 | E | Mixed tribal-origin Christian; Sadri/tribal languages in Other |
| Sarna_ORP | 10.00 | 5.00 | 0.00 | 75.00 | 10.00 | E | Tribal language dominant for Sarna-ORP practitioners |
| Other_residual | 50.00 | 35.00 | 5.00 | 10.00 | 0.00 | E | Buddhist + Sikh + Not_stated; Hindi-speaking fringe |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. 2D canonical table.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 46.70 | 4.80 | 8.38 | 5.99 | 28.73 | 0 | 5.40 | E | SC 42/83.5 + ST 4.5/83.5; UC/OBC/Other residual within Hindu |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 85.00 | 0 | 5.00 | 10.00 | 0 | 0 | E | Tribal sub-castes mostly route to ST_total |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 68.00 | 8.00 | 5.00 | 14.00 | 0.50 | 4.50 | D | Rajbanshi-SC Hindus largely native; some Bangladesh-origin partition refugees |
| Muslim | 85.00 | 8.00 | 3.00 | 3.00 | 0.50 | 0.50 | D | Predominantly local Bengali-Muslim; small Bangladesh trickle |
| Christian | 80.00 | 10.00 | 5.00 | 2.00 | 2.00 | 1.00 | E | Mixed; mission-converted tribal natives dominant |
| Sarna_ORP | 92.00 | 5.00 | 2.00 | 0.00 | 1.00 | 0.00 | E | Tribal religion practitioners overwhelmingly native |
| Other_residual | 30.00 | 15.00 | 50.00 | 0.00 | 5.00 | 0.00 | E | Marwari/Sikh/Buddhist; largely other-state origin |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 80.00 | 50.00 | 89.00 | C | NFHS-4 WB religion gap; Hindu slightly above average |
| Muslim | 70.00 | 40.00 | 78.00 | C | NFHS-4 WB Muslim-Hindu asset gap pattern |
| Christian | 82.00 | 52.00 | 88.00 | C | Mission-educated community; slightly above average |
| Sarna_ORP | 55.00 | 28.00 | 70.00 | E | Tribal fringe; lower asset base |
| Other_residual | 90.00 | 70.00 | 95.00 | E | Urban-skewed (Marwari/Sikh) higher asset |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4.00 | 8.00 | 12.00 | 18.00 | 20.00 | 26.00 | 12.00 | E |
| SC_total | 18.00 | 24.00 | 22.00 | 18.00 | 10.00 | 7.00 | 1.00 | E |
| ST_total | 25.00 | 28.00 | 22.00 | 14.00 | 7.00 | 3.00 | 1.00 | E |
| OBC | 14.00 | 22.00 | 22.00 | 18.00 | 12.00 | 9.00 | 3.00 | E |
| Other_Hindu_middle | 13.00 | 22.00 | 22.00 | 18.00 | 12.00 | 10.00 | 3.00 | E |
| Muslim | 20.00 | 25.00 | 22.00 | 17.00 | 9.00 | 6.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 18.00 | 16.00 | E |
| 23_27 | 17.00 | 13.00 | E |
| 28_32 | 15.00 | 10.00 | E |
| 33_37 | 13.00 | 7.00 | E |
| 38_42 | 11.00 | 5.00 | E |
| 43_47 | 9.00 | 4.00 | E |
| 48_52 | 8.00 | 3.00 | E |
| 53_57 | 7.00 | 2.50 | E |
| 58_62 | 6.00 | 2.00 | E |
| 63_67 | 5.00 | 1.50 | E |
| 68 | 4.00 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 6.00 | 28.00 | E |
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

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 35.00 | 72.00 | C | Rural ag baseline; North Bengal pattern |
| Agricultural_labourer | 25.00 | 62.00 | C | Lowest income group |
| Household_industry | 40.00 | 75.00 | C | |
| Manufacturing | 52.00 | 82.00 | C | |
| Construction | 48.00 | 76.00 | C | |
| Trade_retail | 68.00 | 88.00 | C | Urban Jalpaiguri market hub |
| Transport_logistics | 62.00 | 83.00 | C | Road transport hub; smartphone-dependent |
| Services | 72.00 | 90.00 | C | |
| Government_services_teachers | 85.00 | 95.00 | C | District HQ civil servants; highest |
| Out_migrant_worker | 68.00 | 78.00 | D | Working outside; smartphone-heavy for remittance |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 35.00 | 2.00 | E |
| Primary | 38.00 | 4.00 | E |
| Middle | 34.00 | 6.00 | E |
| Secondary | 30.00 | 10.00 | E |
| Higher_Secondary | 24.00 | 15.00 | E |
| Graduate | 28.00 | 18.00 | E |
| Postgraduate | 38.00 | 12.00 | E |

### D.10 Asset / media × Bilingualism

AC 017 does not declare a `media_tier` axis — D.10 is intentionally omitted per NORMALIZED_SCHEMA §4.7.

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Jalpaiguri_Municipality | 85.00 | 10.00 | 3.50 | 0.10 | 1.40 | E | Muni: SC 22.14% (A); more Hindu-concentrated urban core |
| U2_Jalpaiguri_CDB_rural_share | 82.00 | 13.50 | 4.00 | 0.20 | 0.30 | E | CDB Jalpaiguri block; higher Muslim and Christian fringe in rural GPs |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit).

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Jalpaiguri_Municipality | 9.00 | 22.00 | 2.00 | 6.00 | 47.00 | 10.00 | 4.00 | E |
| U2_Jalpaiguri_CDB_rural_share | 5.00 | 62.00 | 7.00 | 4.00 | 5.50 | 12.00 | 4.50 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Jalpaiguri_Municipality | 90.00 | 62.00 | 20.00 | 95.00 | C |
| U2_Jalpaiguri_CDB_rural_share | 64.00 | 32.00 | 4.00 | 78.00 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Jalpaiguri_Municipality | 75.00 | 90.00 | 95.00 | 99.00 | C |
| U2_Jalpaiguri_CDB_rural_share | 15.00 | 52.00 | 72.00 | 93.00 | C |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 WB regional rollup, adjusted for local Rajbanshi-heavy Hindu bloc.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 60.00 | 27.00 | 5.00 | 6.00 | 2.00 | C | CSDS 2019 WB; Rajbanshi SC heavily BJP-leaning in North Bengal per journalistic consensus |
| Muslim | 5.00 | 68.00 | 20.00 | 5.00 | 2.00 | C | CSDS 2019 WB Muslim vote distribution |
| Christian | 28.00 | 48.00 | 12.00 | 8.00 | 4.00 | E | Christian community split; INC incumbent stronghold effect |
| Sarna_ORP | 40.00 | 35.00 | 10.00 | 12.00 | 3.00 | E | Tribal vote; slightly more distributed |
| Other_residual | 50.00 | 28.00 | 10.00 | 8.00 | 4.00 | E | Urban non-Hindu fringe; BJP-tilted |

### D.16 Vote × Caste (2019 LS)

P(party ‖ caste) — CSDS 2019 WB regional.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 58.00 | 28.00 | 6.00 | 6.00 | 2.00 | C | CSDS 2019; bhadralok BJP-leaning |
| OBC | 42.00 | 35.00 | 8.00 | 12.00 | 3.00 | C | CSDS 2019 |
| SC_total | 58.00 | 28.00 | 7.00 | 5.00 | 2.00 | C | Rajbanshi-SC strongly BJP in 2019; INC incumbent effect present but overridden by BJP surge |
| ST_total | 42.00 | 32.00 | 10.00 | 13.00 | 3.00 | C | CSDS 2019 tribal pattern |
| Other_Hindu_middle | 48.00 | 33.00 | 8.00 | 9.00 | 2.00 | C | CSDS 2019 |
| Muslim | 5.00 | 68.00 | 20.00 | 5.00 | 2.00 | C | Same as D.15 |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 55.00 | 29.00 | 7.00 | 7.00 | 2.00 | C | CSDS 2019 WB |
| Female | 49.00 | 37.00 | 6.00 | 6.00 | 2.00 | C | Higher female AITC tilt; no Lakshmir Bhandar in 2019 |

### D.18 Vote × Welfare

AC 017 does not declare a `welfare_exposure` axis — D.18 is intentionally omitted per NORMALIZED_SCHEMA §4.7.

---

## E. 2019 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 52.25 | A | ECI GE2019 Form-20 equivalent — direct from 2019_AssemblySegmentLevelVotingData.csv AC_NO=17 |
| AITC | 34.00 | A | Same source; 72,962 votes of 214,625 |
| INC | 3.87 | A | 8,311 votes; INC retained some vote share (incumbent AE effect) |
| LF | 7.65 | A | CPIM 16,412 + SUCI(C) 779 = 17,191 votes; CPIM still significant |
| Other_NOTA | 2.23 | A | BSP 1,009 + AMB 306 + SWJP 250 + KPPU 243 + IND 2,206 = 4,014 votes; NOTA not available in 2019 csv |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 017 — Jalpaiguri (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Sukhbilas Barma | INC | ~52.0 | Gobinda Chandra Roy | AIFB | ~45.3 | 11,051 |
| 2016 AE | Sukhbilas Barma | INC | ~47.9 | Dharttimohan Roy | AITC | ~45.3 | 5,157 |

Note: Jalpaiguri (AC 017) was an INC stronghold through 2011 and 2016, with CPIM/AIFB as runner-up in 2011 and AITC as runner-up in 2016. BJP was not the AE winner but surged in the 2019 LS contest. Sukhbilas Barma is a Rajbanshi community leader whose INC personal vote eroded as BJP absorbed Rajbanshi SC voters in 2019 LS.

### Jalpaiguri Lok Sabha (PC 3) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Bijoy Chandra Barman | AITC | ~38 | AITC won; CPI(M) significant; BJP below 30% |
| 2019 LS | Dr. Jayanta Kumar Roy | BJP | ~50.9 | BJP surge across all 7 segments; AITC ~38.6%; margin 184,004 |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Jalpaiguri Municipality Primary Census Abstract (population 107,341; SC 22.14%; ST 0.91%)
- Census of India 2011 — Jalpaiguri CD Block demographics (population 323,455; SC 60.8%; ST 6.1%)
- Census of India 2011 — Jalpaiguri District (population 3,872,846; religion; sex ratio 953)
- Election Commission of India — 2011 AE, 2016 AE, 2019 LS results for AC 017 / Jalpaiguri LS
- ECI GE2019 Assembly Segment Level Voting Data — AC 017, 12 parties, 214,625 valid votes, 255,369 electors
- Delimitation Commission of India 2008 — WB Schedule (AC 017 = Jalpaiguri Muni + 10 GPs of CDB Jalpaiguri)

### Secondary sources (tier B / C)

- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline
- CSDS-Lokniti 2019 NES post-poll — vote × religion / caste / gender WB regional rollup
- Pew Research India 2021 — religion-differential growth projections
- WB District Statistical Handbook — Jalpaiguri

### Tertiary / journalistic (tier D)

- The Print (2021) — Rajbanshi community identity and BJP-AITC competition in North Bengal
- Koch-Rajbanshi Centre for Studies — Rajbanshi SC classification and population estimates
- News reports on 2011 and 2016 AE results for Jalpaiguri (Sukhbilas Barma INC wins)
- IndiaVotes.com — 2019 LS Jalpaiguri constituency segment data

### Tier-D / E reliance flags (what to distrust)

- **Caste sub-group shares** (C.2, D.2) — no caste census post-1931 for non-SC/ST; Rajbanshi vs Other SC split is tier C/E
- **Migration/birthplace shares** (C.16, D.3) — no public AC-level Census D-series; tier D from district patterns
- **Sub-unit data** (D.11–D.14) — collapsed to 2 units (Muni + CDB rural share); refine when DCHB Part-A Jalpaiguri accessible
- **Vote × demographic** (D.15–D.17) — CSDS 2019 WB regional rollup adjusted for local Rajbanshi SC BJP swing; tier C
- **Mother tongue / Rajbongshi** (C.5, D.1) — no direct AC-level language census data; tier D/E
- **Age cohort** (C.3) — renormalized from district pyramid; tier E throughout

### v0 known gaps

1. DCHB Jalpaiguri Part-A — 10 rural GPs collapsed into one sub-unit; refine when PDF accessible
2. AC-level religion data — using district baseline; municipal SC 22.14% vs CDB SC 60.8% contrast requires GP-level disaggregation
3. ECI 2019 LS Form-20 per candidate — using assembly-segment CSV (tier A); adequate for calibration
4. Mother tongue distribution — Rajbongshi share estimated from community-level journalistic sources; no AC Census language table
5. CSDS full WB cross-tabs — using published Swarajya summary; INC vote share in Jalpaiguri (incumbent effect) not captured in regional rollup

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2021 WB Assembly Election — AC 017 Jalpaiguri (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| AITC | Dr. Pradip Kumar Barma | 95,668 | 42.34% | A — ECI 2021 AE |
| BJP | Sujit Singha (Piku) | 94,727 | 41.93% | A — ECI 2021 AE |
| INC | (candidate) | ~24,230 | 10.72% | A — ECI 2021 AE |
| Others | — | ~11,500 | ~5.01% | ECI 2021 AE |
| **AITC margin** | | **941 votes** | **0.41 pp** | A — one of tightest in 2021 WB AE |

Note: AITC flipped this INC-held seat with the narrowest margin. INC retained 10.7% from its 2016 AE base, drawing more from BJP than AITC.

### 2024 Lok Sabha Election — AC 017 segment within Jalpaiguri LS (PC 3) (tier A)

> Figures sourced from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=17, Jalpaiguri. Electorate 268,781; NOTA 2,330.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Dr. Jayanta Kumar Roy | 110,008 | 50.01% | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Nirmal Chandra Roy | 84,474 | 38.40% | A | Same |
| CPI(M) | (candidate) | 20,119 | 9.15% | A | Same |
| BSP | (candidate) | 1,082 | 0.49% | A | Same |
| NOTA | — | 2,330 | 1.05% | A | Same (NOTA column) |
| Others (KPPU, MPOI, SUCI, IND ×4) | various | 3,516 | 0.90% | A | Same |
| **BJP margin over AITC** | | **25,534 votes** | **11.61 pp** | A | Computed |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC-017 shares within ±3pp of the tier-A figures:
- BJP target: 50.0% ± 3pp
- AITC target: 38.4% ± 3pp
- LF (CPI-M) target: 9.2% ± 3pp
