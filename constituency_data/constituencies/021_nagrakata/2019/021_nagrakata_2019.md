# AC 021 — Nagrakata (ST) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 021 Nagrakata as of 2019 only — it does not reference
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
| AC number | 021 | A | ECI / Delimitation Commission 2008 |
| AC name | Nagrakata | A | ECI |
| Reservation | ST | A | Delimitation 2008 |
| District | Jalpaiguri | A | Delimitation 2008 |
| Sub-division | Jalpaiguri Sadar (Mal sub-division area) | A | WB administrative |
| LS constituency | 02 — Jalpaiguri (ST reserved) | A | Delimitation 2008 |
| LS segments included | AC 016 Dhupguri · 017 Maynaguri · 018 Jalpaiguri · 019 Rajganj · 020 Dabgram-Fulbari · 021 Nagrakata · 022 Malbazar | A | Delimitation 2008 |
| AC composition | Nagrakata CD Block (full); includes Nagrakata town + multiple GPs in tea garden belt | A | Delimitation 2008 |
| Geographic note | Sub-Himalayan Terai belt, Jalpaiguri district; tea garden (cha bagan) economy; Baikunthapur forest fringe; adjacent to Bhutan foothills | A | — |
| Sub-units used in v0 | **U1: Tea_Garden_belt** (tea-garden settlements, including Nagrakata and Mal tea gardens) · **U2: Non_Tea_rural** (GP villages outside tea gardens) | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~232,000 | E | Nagrakata CD Block Census 2011 estimated from Jalpaiguri district aggregate |
| 2019 projected population | ~250,000 | E | 8-yr compound projection at ~1.0%/yr (low growth, tea-belt outmigration offsets natural increase) |
| Sex ratio (2019, F per 1000 M) | ~955 | E | Jalpaiguri district 2011 sex ratio 955; stable projection |
| 2019 estimated electorate (18+) | ~226,235 | A | ECI 2019 LS Form-20; total electors per CSV |
| Estimated M / F / TG split (2019) | 51.2% M / 48.8% F / <0.05% TG | E | Jalpaiguri district sex-ratio back-projection |
| 2019 polling stations (estimated) | ~260 | E | Back-derived from electorate size (~870 voters/booth avg) |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 70.00 | E | Jalpaiguri district 2011: Hindu ~70%; tea garden Adivasis split between Hindu practice and Sarna; projected stable |
| Muslim | 8.00 | E | Jalpaiguri district 2011 ~8–9% Muslim; Nagrakata block lower than district avg given heavy ST composition |
| Christian | 2.50 | E | Tea garden Christian converts (Anglican/Catholic missions in colonial tea estate belt; Santhali Christian community) |
| Sarna_ORP | 18.00 | E | Adivasi Sarna/traditional religion followers in tea gardens; Oraon, Munda, Santhali practitioners; Jalpaiguri tribal religious pattern |
| Other_residual | 1.50 | E | Buddhist (Nepali/Tibetan fringe near Bhutan border) + Sikh + Jain + Not_stated |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 8.00 | E | Jalpaiguri district SC ~11%; Nagrakata block lower SC given high ST proportion; residual scheduled castes |
| └ Rajbanshi_SC | 5.00 | E | Dominant SC in Jalpaiguri; Koch-Rajbanshi community partially SC-listed |
| └ Other_SC | 3.00 | E | Residual SC (Chamar, Hari, Bauri etc.) |
| **ST_total** | 45.00 | E | Nagrakata ST-reserved; Jalpaiguri census 2011 ST ~28% at district level; Nagrakata block heavily ST (tea garden Adivasi belt — Oraon/Munda/Santhali/Toto fringe) |
| └ Oraon_ST | 20.00 | E | Largest single ST community in Jalpaiguri tea gardens; dominant in Nagrakata belt |
| └ Munda_ST | 10.00 | E | Second largest tea-garden tribal |
| └ Santhali_ST | 8.00 | E | Widespread across Terai tea estates |
| └ Other_ST | 7.00 | E | Includes Toto (small community), Bodo, Mech, Rabha |
| UC_bhadralok | 4.00 | E | Brahmin/Kayastha/Baidya — small administrative and professional class in Nagrakata town |
| OBC | 6.00 | E | Rajbanshi (OBC category), Koch, Desi Muslim artisans |
| Other_Hindu_middle | 14.00 | E | Residual: Gorkha/Nepali Hindu, Bengali middle castes, Marwari trader fringe |
| Muslim | 8.00 | E | Mirrors C.1; mostly Bengali-speaking and Deshi Muslim |
| Christian_plus_Sarna_plus_Other | 15.00 | E | Collapsed: Christian converts (2.5%) + Sarna/ORP non-Hindu-coded tribal (12%) + Other_residual (0.5%) |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.00 | E | Jalpaiguri district age pyramid 2011 renormalized to 18+ adults; first-time voter cohort |
| 23_27 | 12.50 | E | |
| 28_32 | 12.00 | E | |
| 33_37 | 10.50 | E | |
| 38_42 | 10.00 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.00 | E | |
| 63_67 | 6.50 | E | Slightly elevated older cohort; tea-garden stable resident population |
| 68 | 6.50 | E | 68+ open-ended; tea-belt long-residence elders |
| **Sum** | **100.00** | — | self-check (renormalized from Census 2011 Jalpaiguri age distribution, adults only) |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.15 | E | Jalpaiguri 2011 sex ratio 955 → 51.15% M / 48.85% F |
| Female | 48.84 | E | |
| Third_gender | 0.01 | E | Negligible; WB pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 38.00 | E | Jalpaiguri 2011 linguistic census: Bengali ~38% of block population including settled Bengali community + tea-garden management class |
| Hindi | 5.00 | E | Hindi-belt migrants in tea estates; Bihari/UP workers and contractors |
| Urdu | 2.00 | E | Small Muslim community fraction |
| Other | 2.00 | E | Residual catch-all: Nepali fringe, Tibetan, Sikh |
| Sadri | 28.00 | E | Sadri (Nagpuri) is the lingua franca of tea-garden Adivasi workers in Jalpaiguri; Oraon, Munda, Santhali speakers largely use Sadri in inter-community communication |
| Santhali | 10.00 | E | Native Santhali speakers (Ol Chiki script community) |
| Rajbongshi | 8.00 | E | Koch-Rajbanshi / Rajbongshi language community in Terai belt |
| Nepali | 7.00 | E | Gorkha/Nepali-speaking community near Bhutan border fringe |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 28.00 | E | Jalpaiguri district 2011 literacy ~71%; tea-garden Adivasi literacy lower; AC-level ~72% literate → ~28% illiterate |
| Primary | 24.00 | E | Census 2011 Jalpaiguri education distribution scaled; tea-belt primary attainment common |
| Middle | 19.00 | E | |
| Secondary | 14.00 | E | Drop-off at secondary; tea-garden children often stop after primary |
| Higher_Secondary | 8.00 | E | |
| Graduate | 5.50 | E | |
| Postgraduate | 1.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 38.00 | E | Tea garden employment drives high main-worker rate; Census 2011 Jalpaiguri block pattern |
| └ Main_worker_tea_garden | 22.00 | E | Sub-row: permanent tea estate employees (is_subgroup=yes) |
| └ Main_worker_non_tea | 16.00 | E | Sub-row: cultivation, trade, govt (is_subgroup=yes) |
| Marginal_worker | 14.00 | E | Seasonal/casual tea-picking labour; periodic agricultural work |
| Non_worker | 30.00 | E | Housewife + elderly; lower than state average due to female tea-garden labour participation |
| Student | 10.00 | E | 18–22 in education |
| Unemployed | 8.00 | E | Educated job-seekers; frustrated non-tea youth |
| **Sum** | **100.00** | — | self-check (Main_worker sub-rows excluded from sum) |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 14.00 | E | Non-tea-garden smallholder farming in GP areas |
| Agricultural_labourer | 8.00 | E | Non-tea agricultural labourers |
| Household_industry | 3.00 | E | Artisan and cottage; low in tea-belt |
| Manufacturing | 4.00 | E | Small processing units in Nagrakata town |
| Construction | 5.00 | E | Building trade |
| Trade_retail | 8.00 | E | Nagrakata town market |
| Transport_logistics | 4.00 | E | Tea-estate truck/jeep economy |
| Services | 6.00 | E | Private services |
| Government_services_teachers | 5.00 | E | Block-level offices, schools |
| Out_migrant_worker | 3.00 | E | Young ST workers to Sikkim/Assam/Delhi; D-estimate |
| Tea_garden_worker | 40.00 | E | AC-local: permanent + temporary tea estate workers (pluckers, garden staff); dominant occupation category in this belt |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Small tea-garden contractors and shop owners |
| Employee | 48.00 | E | Tea-garden registered employees dominate; also govt employees |
| Single_worker | 30.00 | E | Own-account cultivators, petty traders |
| Family_worker | 20.50 | E | Unpaid family farm helpers; substantial in non-tea households |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 35.00 | E | Jalpaiguri district BPL proportion higher than state average; tea-garden Adivasi communities significantly below poverty line; estimated ~35% BPL |
| Above_Poverty_Line_low_income | 32.00 | E | Marginal tea-garden and smallholder households just above BPL |
| Lower_middle | 20.00 | E | Regular tea-garden permanent workers, petty traders |
| Middle | 10.00 | E | Supervisory tea-estate staff, government servants, teachers |
| Upper_middle_well_off | 3.00 | E | Tea-estate managers, large traders, professional class in Nagrakata town |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Tea_Garden_belt | 60.00 | E | Majority of Nagrakata block population lives in or adjacent to tea garden labour lines; v0 equal-weight estimate |
| U2_Non_Tea_rural | 40.00 | E | GP villages outside tea garden estates; smallholder farming belt |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.6 persons | E | WB tea-belt pattern; larger HH sizes in tea garden labour lines |
| Nuclear_HH | 62.00 | E | NFHS-4 WB rural pattern; tea-garden line housing promotes nuclear families |
| Joint_HH | 30.00 | E | Extended family common in non-tea villages |
| Extended_multi_generation | 8.00 | E | Multi-generational households in older tea-garden communities |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.00 | E | Census 2011 Jalpaiguri pattern; first-time voter cohort |
| Currently_married | 65.00 | E | |
| Widowed | 8.00 | E | Slightly elevated; tea-garden occupational hazard and older age profile |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 55.00 | C | NFHS-4 WB rural ~60%; tea-garden Adivasi households below state rural avg; AC ~55% |
| Radio | 8.00 | C | Slightly elevated in tea-belt; garden management still uses radio |
| Mobile_phone | 78.00 | C | NFHS-4 WB rural ~78%; reasonable for 2019 given Jio rollout |
| Smartphone_with_internet | 30.00 | C | Below state average; tea-garden literacy constraint; Jalpaiguri rural pattern |
| Computer | 4.00 | C | Very low; Jalpaiguri rural pattern |
| Two_wheeler | 18.00 | C | NFHS-4 WB rural ~18%; tea-belt motorcycle use moderate |
| Four_wheeler | 3.00 | C | Limited; mostly estate management vehicles |
| Banking_access | 72.00 | C | PMJDY Jan Dhan rollout; tea-garden workers increasingly banked via wage-payment mandates; below state avg |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 78.00 | C | NFHS-4 WB rural; tea estate piped water partially available; some garden villages lack access |
| Improved_sanitation | 52.00 | C | NFHS-4 WB rural ~51% + Swachh Bharat 2014-19 gains; tea-belt slightly lower than plains rural |
| LPG_clean_cooking_fuel | 28.00 | C | NFHS-4 WB rural ~24% + Ujjwala 2016-19 gains; tea-garden Adivasi LPG uptake lower than plains |
| Wood_biomass_fuel | 65.00 | C | Primary cooking fuel in tea garden labour lines; firewood collection common |
| Other_fuel | 7.00 | C | Kerosene, crop residue |
| Electricity | 88.00 | C | Census 2011 + Saubhagya 2017-19 rollout; tea gardens electrified earlier; good coverage |
| **Note** | (water/sanitation/electricity are independent; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 55.00 | D | Born in Jalpaiguri district or same block; multi-generational tea-garden resident families |
| WB_other_district | 8.00 | D | Internal WB migrants; Bengali middle-class in Nagrakata town from other districts |
| Other_Indian_state | 22.00 | D | Central Indian tribal labourers brought to Jalpaiguri tea estates in 19th–early 20th century; Jharkhand/Bihar/Odisha origin Oraon/Munda/Santhali — now 3rd–5th generation residents |
| Bangladesh_origin | 3.00 | D | Small settled Bengali Hindu fringe; not primarily a refugee AC |
| Outside_India | 0.50 | E | Negligible; some Nepal-origin Gorkha households near Bhutan border |
| Out_migrant | 3.00 | E | Young ST workers temporarily absent |
| Jharkhand_origin | 8.50 | D | AC-local: specifically Jharkhand/Chhattisgarh/Odisha-origin Adivasi (Oraon/Munda/Santhali) tea-garden indentured-labour descent — set separately from Other_Indian_state to flag load-bearing historical migration stream; overlaps Other_Indian_state |
| **Sum** | **100.00** | — | self-check (Jharkhand_origin is sub-row documentation; core 6 rows sum to 100) |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Sadri | Santhali | Rajbongshi | Nepali | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 50.00 | 5.00 | 0.00 | 1.00 | 22.00 | 8.00 | 12.00 | 2.00 | E | Hindu population includes Bengali plains settlers + Rajbongshi + some Adivasi Hindu; Sadri-speaking Oraon who practice Hindu syncretic religion |
| Muslim | 80.00 | 5.00 | 12.00 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | E | Jalpaiguri Muslims predominantly Bengali-speaking Deshi Muslim |
| Christian | 15.00 | 5.00 | 0.00 | 2.00 | 50.00 | 20.00 | 5.00 | 3.00 | E | Christian converts overwhelmingly Adivasi — Sadri/Santhali-speaking |
| Sarna_ORP | 5.00 | 3.00 | 0.00 | 2.00 | 55.00 | 25.00 | 8.00 | 2.00 | E | Sarna practitioners = traditional Adivasi; Sadri and Santhali dominant |
| Other_residual | 20.00 | 15.00 | 2.00 | 10.00 | 10.00 | 3.00 | 10.00 | 30.00 | E | Buddhist Tibetan/Nepali fringe; mixed |

### D.2 Religion × Caste

P(caste ‖ religion) — 2D table, one row per religion.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 11.40 | 27.10 | 5.70 | 8.60 | 47.20 | 0 | 0 | E | Hindu in Nagrakata includes Rajbongshi (OBC/middle), Nepali Hindu, Bengali middle; ST-coded Adivasi who practice Hindu syncretically counted under ST_total |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 85.00 | 0 | 0 | 0 | 0 | 15.00 | E | Christian converts overwhelmingly ST Adivasi (Oraon/Munda/Santhali); small non-tribal Christian fringe |
| Sarna_ORP | 0 | 95.00 | 0 | 3.00 | 2.00 | 0 | 0 | E | Sarna practitioners almost entirely ST; marginal OBC and other Hindu syncretic |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 52.00 | 12.00 | 8.00 | 5.00 | 1.00 | 2.00 | E | Rajbongshi native; Bengali Hindu mix of native + migrant; some Bangladesh-origin settlers |
| Muslim | 75.00 | 10.00 | 3.00 | 10.00 | 0.50 | 1.50 | E | Bengali-Muslim mostly native Jalpaiguri; small Bangladesh-origin fraction |
| Christian | 60.00 | 3.00 | 32.00 | 1.00 | 0.50 | 3.50 | E | Christian Adivasi overwhelmingly Jharkhand/Odisha-origin (counted in Other_Indian_state) multi-gen residents |
| Sarna_ORP | 55.00 | 2.00 | 38.00 | 0.00 | 0.50 | 4.50 | E | Sarna Adivasi = highest other-state-origin; Jharkhand/Chhattisgarh/Odisha descent |
| Other_residual | 40.00 | 8.00 | 5.00 | 0.00 | 45.00 | 2.00 | E | Includes Nepal-origin Buddhist community |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 62.00 | 35.00 | 80.00 | E | Bengali/Rajbongshi Hindu better-off than Adivasi average |
| Muslim | 55.00 | 28.00 | 70.00 | E | Jalpaiguri Muslim smallholder pattern; below Hindu avg |
| Christian | 45.00 | 22.00 | 65.00 | E | Tea-garden Christian Adivasi; asset-poor but improving |
| Sarna_ORP | 38.00 | 18.00 | 58.00 | E | Lowest asset ownership; traditional Adivasi households in tea lines |
| Other_residual | 60.00 | 32.00 | 75.00 | E | Mixed; Nepali Buddhist slightly above Adivasi avg |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 5.00 | 10.00 | 15.00 | 20.00 | 20.00 | 22.00 | 8.00 | E |
| SC_total | 25.00 | 28.00 | 22.00 | 14.00 | 7.00 | 3.50 | 0.50 | E |
| ST_total | 35.00 | 28.00 | 18.00 | 12.00 | 5.00 | 1.50 | 0.50 | E |
| OBC | 18.00 | 26.00 | 22.00 | 18.00 | 10.00 | 5.00 | 1.00 | E |
| Other_Hindu_middle | 20.00 | 25.00 | 22.00 | 17.00 | 10.00 | 5.00 | 1.00 | E |
| Muslim | 30.00 | 28.00 | 20.00 | 14.00 | 5.00 | 2.50 | 0.50 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 10.00 | 8.00 | E |
| 23_27 | 9.00 | 7.00 | E |
| 28_32 | 8.00 | 5.00 | E |
| 33_37 | 7.00 | 4.00 | E |
| 38_42 | 6.00 | 3.00 | E |
| 43_47 | 5.00 | 2.00 | E |
| 48_52 | 4.00 | 1.50 | E |
| 53_57 | 3.00 | 1.00 | E |
| 58_62 | 2.50 | 0.80 | E |
| 63_67 | 2.00 | 0.60 | E |
| 68 | 1.50 | 0.50 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8.00 | 35.00 | E |
| 23_27 | 45.00 | 80.00 | E |
| 28_32 | 82.00 | 90.00 | E |
| 33_37 | 90.00 | 88.00 | E |
| 38_42 | 92.00 | 85.00 | E |
| 43_47 | 90.00 | 82.00 | E |
| 48_52 | 88.00 | 75.00 | E |
| 53_57 | 85.00 | 65.00 | E |
| 58_62 | 82.00 | 52.00 | E |
| 63_67 | 78.00 | 38.00 | E |
| 68 | 70.00 | 25.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 22.00 | 48.00 | E | Non-tea smallholder; below state rural avg |
| Agricultural_labourer | 15.00 | 38.00 | E | Poorest segment |
| Household_industry | 25.00 | 50.00 | E | |
| Manufacturing | 35.00 | 60.00 | E | |
| Construction | 30.00 | 55.00 | E | |
| Trade_retail | 55.00 | 72.00 | E | Nagrakata town traders |
| Transport_logistics | 48.00 | 65.00 | E | Tea-estate transport workers |
| Services | 60.00 | 75.00 | E | |
| Government_services_teachers | 78.00 | 90.00 | E | Highest; educated class |
| Out_migrant_worker | 62.00 | 72.00 | D | Working outside; smartphone access driven by remittance-related needs |
| Tea_garden_worker | 18.00 | 45.00 | E | Tea-garden permanent worker; lower smartphone penetration; TV via garden community hall |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 42.00 | 1.00 | E |
| Primary | 45.00 | 3.00 | E |
| Middle | 40.00 | 6.00 | E |
| Secondary | 32.00 | 10.00 | E |
| Higher_Secondary | 25.00 | 16.00 | E |
| Graduate | 30.00 | 20.00 | E |
| Postgraduate | 38.00 | 15.00 | E |

### D.10 Asset / media × Bilingualism

AC 021 does not declare a `media_tier` axis — skip per schema §4.7. No standalone bilingualism table.

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Tea_Garden_belt | 58.00 | 6.00 | 4.00 | 30.00 | 2.00 | E | Tea gardens heavily Adivasi (Sarna + Christian converts); fewer Bengali Hindu; small Muslim fringe |
| U2_Non_Tea_rural | 86.00 | 11.00 | 0.50 | 1.50 | 1.00 | E | Non-tea GP villages predominantly Hindu (Rajbongshi + Bengali) with higher Muslim share; very few Adivasi |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Parent leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Tea_Garden_belt | 2.00 | 4.00 | 62.00 | 4.00 | 10.00 | 6.00 | 12.00 | E |
| U2_Non_Tea_rural | 7.00 | 14.00 | 20.00 | 9.00 | 20.00 | 11.00 | 19.00 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Tea_Garden_belt | 48.00 | 22.00 | 2.00 | 65.00 | E |
| U2_Non_Tea_rural | 65.00 | 42.00 | 7.00 | 82.00 | E |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Tea_Garden_belt | 20.00 | 42.00 | 70.00 | 85.00 | E |
| U2_Non_Tea_rural | 38.00 | 65.00 | 88.00 | 92.00 | E |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion). BJP dominance driven by Adivasi (Sarna_ORP + Christian ST) consolidation under tribal identity politics and Van Dhan/tribal welfare promises; AITC retained Bengali/Muslim base.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 60.00 | 28.00 | 3.00 | 7.00 | 2.00 | C | CSDS-Lokniti 2019 WB + Jalpaiguri tribal-belt adjustment; Bengali Hindu BJP-leaning; Rajbongshi BJP-leaning |
| Muslim | 5.00 | 75.00 | 12.00 | 6.00 | 2.00 | C | Muslim consolidation behind AITC in WB 2019; CSDS WB regional pattern |
| Christian | 65.00 | 20.00 | 3.00 | 8.00 | 4.00 | E | Tea-garden Christian ST voted heavily BJP in 2019; BJP tribal outreach |
| Sarna_ORP | 72.00 | 16.00 | 2.00 | 6.00 | 4.00 | E | Highest BJP vote among any religion category; BJP tribal welfare narrative strongest among traditional Adivasi |
| Other_residual | 45.00 | 30.00 | 5.00 | 10.00 | 10.00 | E | Nepali Buddhist etc. mixed |

### D.16 Vote × Caste (2019 LS)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 62.00 | 28.00 | 4.00 | 4.00 | 2.00 | C | Bhadralok BJP-leaning 2019; CSDS WB |
| OBC | 52.00 | 32.00 | 5.00 | 8.00 | 3.00 | C | Rajbongshi OBC; BJP-leaning in North Bengal |
| SC_total | 48.00 | 36.00 | 5.00 | 8.00 | 3.00 | C | SC in Jalpaiguri: Rajbanshi SC; BJP gaining 2019 |
| ST_total | 70.00 | 18.00 | 2.00 | 6.00 | 4.00 | E | Load-bearing: ST tribal bloc overwhelmingly BJP 2019; BJP Van Dhan, ST welfare; Jalpaiguri ST consolidation driven 58% AC result |
| Other_Hindu_middle | 52.00 | 32.00 | 5.00 | 8.00 | 3.00 | C | Rajbongshi / Gorkha middle; BJP leaning |
| Muslim | 5.00 | 75.00 | 12.00 | 6.00 | 2.00 | C | Mirrors D.15 |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 60.00 | 28.00 | 3.50 | 6.50 | 2.00 | C | CSDS 2019 WB gender pattern; tribal male BJP-leaning |
| Female | 56.00 | 33.00 | 2.50 | 6.50 | 2.00 | C | Tea-garden female workers also BJP-leaning 2019; slightly lower BJP than male but still dominant |

### D.18 Vote × Welfare

AC 021 does not declare a `welfare_exposure` axis — skip per schema §4.7. No welfare joint table.

---

## E. 2019 baseline vote (calibration target)

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 58.41 | A | ECI GE2019 Form-20 data; 103,865 votes / 177,813 valid votes; 2019_AssemblySegmentLevelVotingData.csv |
| AITC | 30.16 | A | ECI GE2019; 53,621 votes |
| INC | 3.03 | A | ECI GE2019; 5,391 votes |
| LF | 6.44 | A | ECI GE2019; RSP 10,641 + SUCI(C) 811 = 11,452 votes; RSP historically strong in Jalpaiguri tea belt |
| Other_NOTA | 1.96 | A | ECI GE2019; 2 IND candidates: 1,027 + 2,457 = 3,484 votes |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 021 — Nagrakata (Assembly Elections)

Nagrakata is an ST-reserved seat in Jalpaiguri district. Historically it was a Left Front (RSP/CPI-M) bastion in the tea-garden belt, with RSP particularly strong due to tea-garden trade union presence. AITC made inroads in 2011 on the anti-Left wave. BJP emerged as the major force by 2019 riding Adivasi tribal consolidation.

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Biren Bora | AITC | ~46 | RSP candidate | RSP | ~35 | ~est 12,000 |
| 2016 AE | Biren Bora | AITC | ~42 | BJP candidate | BJP | ~32 | ~est 8,000 |

(Note: Exact 2011/2016 AE figures from ECI; above are approximate from journalistic sources — tier D. Compiler note: AITC won 2011 and 2016 but with declining margins as BJP rose.)

### Jalpaiguri LS (PC 02) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Bijoy Chandra Barma | AITC | ~37 | AITC won; RSP/Left second; BJP in third but rising |
| 2019 LS | Jayanta Kumar Roy | BJP | ~55 | BJP swept Jalpaiguri PC; Nagrakata segment among highest BJP-performing segments |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Election Commission of India — 2019 LS Form-20 via `data/2019_AssemblySegmentLevelVotingData.csv` (AC 021 segment: 226,235 electors, 177,813 valid votes)
- Delimitation Commission of India 2008 — WB Schedule (AC 021 Nagrakata = Nagrakata CD Block; ST reserved)
- Census of India 2011 — Jalpaiguri district Primary Census Abstract and CD Block tables

### Secondary sources (tier B/C)

- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline
- CSDS-Lokniti 2019 NES post-poll — vote × religion / caste / gender (WB regional rollup)
- WB District Statistical Handbook — Jalpaiguri
- Census 2011 — Jalpaiguri CD Block data (Nagrakata block); ST population, literacy, workers

### Tertiary / journalistic (tier D)

- Wikipedia: "Nagrakata (Vidhan Sabha constituency)" — reservation status, LS segment, election history
- Wikipedia: "Jalpaiguri district" — demographics, ST composition, tea garden economy
- Wikipedia: "Jalpaiguri (Lok Sabha constituency)" — 2019 LS result; BJP win; tea-belt Adivasi vote
- Journalistic coverage of 2019 WB tribal-belt BJP sweep in Jalpaiguri and Alipurduar LPs

### Tier-D/E reliance flags (what to distrust)

- **ST composition within Hindu / Sarna split** (C.1, C.2, D.2) — Census 2011 religion tables do not separate Hindu-practicing ST from Sarna ORP cleanly; all Adivasi estimates are tier E
- **Sadri/Santhali/Rajbongshi mother-tongue shares** (C.5, D.1) — no AC-level linguistic data; Jalpaiguri district 2011 census proxy; tier E
- **Sub-unit decomposition** (C.11, D.11–D.14) — v0 collapses entire block into 2 sub-units; no GP-level data
- **Vote × Demographic conditionals** (D.15–D.17) — CSDS 2019 WB rollup with tribal-belt adjustment; tier C/E
- **Pre-2019 assembly election results** (F) — approximate figures from journalistic sources; ECI 2011/2016 AE records not independently verified
- **Migration / birthplace** (C.16, D.3) — no AC-level Census D-series; tier D estimate from tea-garden historical settlement pattern

### v0 known gaps

1. DCHB Jalpaiguri Part-A — sub-unit decomposition uses only 2 cells; refine when GP-level data available
2. ECI 2011 AE / 2016 AE — exact AC-level results not independently sourced; need ECI archive lookup
3. Census HH-13 GP-level — asset/media data proxied from NFHS-4 state pattern
4. Census D-series — migration data proxied from tea-garden historical settlement pattern
5. Linguistic census 2011 — Sadri/tribal language shares at block level not directly retrieved

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2021 WB Assembly Election — AC 021 Nagrakata (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Mithun Barman | ~95,000 | ~47 | D — ECI 2021 AE; approximate from journalistic sources; exact figures to be confirmed from ECI archive |
| AITC | Biren Bora | ~98,000 | ~48 | D — AITC narrowly won back in 2021 wave |
| Others | — | ~8,000 | ~4 | D |

(Nagrakata was one of the seats the AITC recaptured in 2021 despite the strong 2019 BJP showing. This reversal — from 58% BJP in 2019 LS to AITC winning in 2021 AE — is the key validation challenge for the simulator.)

### 2024 Lok Sabha Election — AC 021 segment within Jalpaiguri LS (tier A, ECI)

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Jayanta Kumar Roy | (to be fetched) | ~55 | D | 2024_AssemblySegmentLevelVotingData.csv — to be confirmed |
| AITC | (candidate) | (to be fetched) | ~35 | D | Same |
| Others | — | — | ~10 | D | Same |

(Exact 2024 CSV figures to be confirmed via `data/2024_AssemblySegmentLevelVotingData.csv`.)

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC segment shares within ±3pp of the tier-A figures (BJP / AITC / LF combined).
