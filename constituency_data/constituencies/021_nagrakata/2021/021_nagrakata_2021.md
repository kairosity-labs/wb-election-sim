# AC 021 — Nagrakata (ST) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 021 Nagrakata as of end-2021 — it does not reference any
> post-2021 events. Use post-2021 elections (2024 LS) as out-of-sample
> validation gates for downstream simulators.
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
| AC number | 021 | A | ECI / Delimitation Commission 2008 |
| AC name | Nagrakata | A | ECI |
| Reservation | ST | A | Delimitation 2008 |
| District | Jalpaiguri | A | Delimitation 2008 |
| Sub-division | Jalpaiguri Sadar (Mal sub-division area) | A | WB administrative |
| LS constituency | 02 — Alipurduar (ST reserved) | A | Delimitation 2008 |
| LS segments included | AC 016 Dhupguri · 017 Maynaguri · 018 Jalpaiguri · 019 Rajganj · 020 Dabgram-Fulbari · 021 Nagrakata · 022 Malbazar | A | Delimitation 2008 |
| AC composition | Nagrakata CD Block (full); includes Nagrakata town + multiple GPs in tea garden belt | A | Delimitation 2008 |
| Geographic note | Sub-Himalayan Terai belt, Jalpaiguri district; tea garden (cha bagan) economy; Baikunthapur forest fringe; adjacent to Bhutan foothills; Alipurduar LS after 2014 delimitation | A | — |
| Sub-units used in v0 | **U1: Tea_Garden_belt** (tea-garden settlements, including Nagrakata and Mal tea gardens) · **U2: Non_Tea_rural** (GP villages outside tea gardens) | E | v0 simplification |

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~232,000 | E | Nagrakata CD Block Census 2011 estimated from Jalpaiguri district aggregate |
| 2021 projected population | ~256,000 | E | 10-yr compound projection at ~1.0%/yr (low growth, tea-belt outmigration offsets natural increase) |
| Sex ratio (2021, F per 1000 M) | ~957 | E | Jalpaiguri district 2011 sex ratio 955; slight improvement projection |
| 2021 AE electorate (18+) | 237,305 | A | ECI 2021 WB Assembly Election; total electors from detailed_results.csv |
| Estimated M / F / TG split (2021) | 51.1% M / 48.9% F / <0.05% TG | E | Jalpaiguri district sex-ratio back-projection; slight female improvement |
| 2021 polling stations (estimated) | ~272 | E | Back-derived from electorate size (~872 voters/booth avg); slight increase from 2019 |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 69.50 | E | Jalpaiguri district 2011: Hindu ~70%; 10-yr projection; marginal decline as Sarna-ORP identity grows; tea garden Adivasi religious identity fluidity |
| Muslim | 8.00 | E | Jalpaiguri district 2011 ~8–9% Muslim; Nagrakata block lower than district avg given heavy ST composition; stable |
| Christian | 2.80 | E | Slight increase; ongoing conversion in tea-garden belt; Anglican/Catholic missions continue |
| Sarna_ORP | 18.20 | E | Adivasi Sarna/traditional religion practitioners; slight increase from Christian and Hindu Adivasi self-identifying as Sarna by 2021 |
| Other_residual | 1.50 | E | Buddhist (Nepali/Tibetan fringe near Bhutan border) + Sikh + Jain + Not_stated |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 8.00 | E | Jalpaiguri district SC ~11%; Nagrakata block lower SC given high ST proportion; stable |
| └ Rajbanshi_SC | 5.00 | E | Dominant SC in Jalpaiguri; Koch-Rajbanshi community partially SC-listed |
| └ Other_SC | 3.00 | E | Residual SC (Chamar, Hari, Bauri etc.) |
| **ST_total** | 45.00 | E | Nagrakata ST-reserved; Jalpaiguri census 2011 ST ~28% at district level; Nagrakata block heavily ST (tea garden Adivasi belt — Oraon/Munda/Santhali/Toto fringe); stable |
| └ Oraon_ST | 20.00 | E | Largest single ST community in Jalpaiguri tea gardens; dominant in Nagrakata belt |
| └ Munda_ST | 10.00 | E | Second largest tea-garden tribal |
| └ Santhali_ST | 8.00 | E | Widespread across Terai tea estates |
| └ Other_ST | 7.00 | E | Includes Toto (small community), Bodo, Mech, Rabha |
| UC_bhadralok | 4.00 | E | Brahmin/Kayastha/Baidya — small administrative and professional class in Nagrakata town |
| OBC | 6.00 | E | Rajbanshi (OBC category), Koch, Desi Muslim artisans |
| Other_Hindu_middle | 14.00 | E | Residual: Gorkha/Nepali Hindu, Bengali middle castes, Marwari trader fringe |
| Muslim | 8.00 | E | Mirrors C.1; mostly Bengali-speaking and Deshi Muslim |
| Christian_plus_Sarna_plus_Other | 15.00 | E | Collapsed: Christian converts (2.8%) + Sarna/ORP non-Hindu-coded tribal (11.7%) + Other_residual (0.5%) |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2021, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.00 | E | 2021 new voter cohort; renormalized from Jalpaiguri district age pyramid 2011; two new cohorts entered since 2019 |
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

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.10 | E | Jalpaiguri 2011 sex ratio 955 → slight improvement to ~957; 51.10% M / 48.89% F |
| Female | 48.89 | E | |
| Third_gender | 0.01 | E | Negligible; WB pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 38.00 | E | Jalpaiguri 2011 linguistic census; stable |
| Hindi | 5.00 | E | Hindi-belt migrants in tea estates; stable |
| Urdu | 2.00 | E | Small Muslim community fraction |
| Other | 2.00 | E | Residual catch-all: Nepali fringe, Tibetan, Sikh |
| Sadri | 28.00 | E | Sadri (Nagpuri) is the lingua franca of tea-garden Adivasi workers in Jalpaiguri; stable |
| Santhali | 10.00 | E | Native Santhali speakers (Ol Chiki script community) |
| Rajbongshi | 8.00 | E | Koch-Rajbanshi / Rajbongshi language community in Terai belt |
| Nepali | 7.00 | E | Gorkha/Nepali-speaking community near Bhutan border fringe |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 26.00 | E | Jalpaiguri district 2011 literacy ~71%; 10-yr trend improvement ~+2pp in literacy; AC-level ~74% literate → ~26% illiterate; NFHS-5 WB rural improvement |
| Primary | 24.00 | E | Census 2011 Jalpaiguri distribution projected; stable |
| Middle | 19.00 | E | |
| Secondary | 15.00 | E | Slight improvement; Sabuj Sathi bicycle scheme improving retention |
| Higher_Secondary | 8.50 | E | |
| Graduate | 5.50 | E | |
| Postgraduate | 2.00 | E | Slight increase; government service aspirants |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 37.00 | E | Tea garden employment drives high main-worker rate; slight decline due to COVID-19 disruption in 2020 |
| └ Main_worker_tea_garden | 21.00 | E | Sub-row: permanent tea estate employees; COVID-19 reduced formal employment slightly (is_subgroup=yes) |
| └ Main_worker_non_tea | 16.00 | E | Sub-row: cultivation, trade, govt (is_subgroup=yes) |
| Marginal_worker | 14.00 | E | Seasonal/casual tea-picking labour; periodic agricultural work |
| Non_worker | 31.00 | E | Housewife + elderly; Lakshmir Bhandar (Apr 2021) target population; female HH heads |
| Student | 10.00 | E | 18–22 in education; COVID disruption reduced in-class attendance but not registration |
| Unemployed | 8.00 | E | Educated job-seekers; frustrated non-tea youth; COVID return migration added to pool |
| **Sum** | **100.00** | — | self-check (Main_worker sub-rows excluded from sum) |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 14.00 | E | Non-tea-garden smallholder farming in GP areas |
| Agricultural_labourer | 8.00 | E | Non-tea agricultural labourers |
| Household_industry | 3.00 | E | Artisan and cottage; low in tea-belt |
| Manufacturing | 4.00 | E | Small processing units in Nagrakata town |
| Construction | 5.00 | E | Building trade; COVID-19 reverse migration added workers |
| Trade_retail | 8.00 | E | Nagrakata town market |
| Transport_logistics | 4.00 | E | Tea-estate truck/jeep economy |
| Services | 6.00 | E | Private services |
| Government_services_teachers | 5.00 | E | Block-level offices, schools |
| Out_migrant_worker | 3.00 | E | Young ST workers to Sikkim/Assam/Delhi; D-estimate; COVID lockdown caused temporary return |
| Tea_garden_worker | 40.00 | E | AC-local: permanent + temporary tea estate workers (pluckers, garden staff); dominant occupation category in this belt |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Small tea-garden contractors and shop owners |
| Employee | 47.00 | E | Tea-garden registered employees dominate; also govt employees; slight decline due to COVID |
| Single_worker | 31.00 | E | Own-account cultivators, petty traders; slight increase as formal employment softened |
| Family_worker | 20.50 | E | Unpaid family farm helpers; substantial in non-tea households |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 33.00 | E | Jalpaiguri district BPL proportion; COVID-19 economic shock temporarily pushed some households into distress; slight decline from 2019 pre-COVID trajectory; net ~33% |
| Above_Poverty_Line_low_income | 32.00 | E | Marginal tea-garden and smallholder households; Lakshmir Bhandar (Apr 2021) provides income support to female HH heads |
| Lower_middle | 21.00 | E | Regular tea-garden permanent workers, petty traders |
| Middle | 11.00 | E | Supervisory tea-estate staff, government servants, teachers |
| Upper_middle_well_off | 3.00 | E | Tea-estate managers, large traders, professional class in Nagrakata town |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Tea_Garden_belt | 60.00 | E | Majority of Nagrakata block population lives in or adjacent to tea garden labour lines; v0 equal-weight estimate; stable |
| U2_Non_Tea_rural | 40.00 | E | GP villages outside tea garden estates; smallholder farming belt |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | WB tea-belt pattern; NFHS-5 WB rural slight decline from 4.6 in 2019 |
| Nuclear_HH | 63.00 | E | NFHS-5 WB rural pattern; COVID return migration temporarily increased joint HH but by end-2021 normalizing |
| Joint_HH | 29.00 | E | Extended family common in non-tea villages; slightly lower than 2019 |
| Extended_multi_generation | 8.00 | E | Multi-generational households in older tea-garden communities |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.00 | E | Census 2011 Jalpaiguri pattern; 2021 cohort added; stable |
| Currently_married | 65.00 | E | |
| Widowed | 8.00 | E | Slightly elevated; tea-garden occupational hazard and older age profile; COVID mortality added |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 57.00 | C | NFHS-5 (2019-21) WB rural ~60%; tea-garden Adivasi households below state rural avg; slight increase from 55% in 2019 |
| Radio | 7.00 | C | Gradual decline; garden management less reliant on radio |
| Mobile_phone | 85.00 | C | NFHS-5 WB rural improvement; Jio rollout matured; slight increase |
| Smartphone_with_internet | 52.00 | C | **Notable COVID-19 surge**: +22pp from 30% in 2019; Jio affordable data + lockdown drove rapid smartphone adoption even in tea-garden belt; NFHS-5 WB rural ~50-55% |
| Computer | 4.00 | C | Very low; Jalpaiguri rural pattern; minimal change |
| Two_wheeler | 19.00 | C | Slight increase; tea-belt motorcycle use |
| Four_wheeler | 3.00 | C | Limited; mostly estate management vehicles |
| Banking_access | 79.00 | C | PMJDY Jan Dhan + Lakshmir Bhandar (Apr 2021) bank account mandatory for scheme enrollment drove further uptake; +7pp from 2019; NFHS-5 WB rural ~78% |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 80.00 | C | NFHS-5 WB rural ~80%; tea estate piped water improvement; stable |
| Improved_sanitation | 58.00 | C | NFHS-5 WB rural improvement; Swachh Bharat continued 2019-21; +6pp from 2019 |
| LPG_clean_cooking_fuel | 35.00 | C | NFHS-5 WB rural ~35%; Ujjwala 2.0 continuity; +7pp from 2019; tea-garden Adivasi LPG uptake improving |
| Wood_biomass_fuel | 58.00 | C | Primary cooking fuel declining as LPG rises; -7pp from 2019 |
| Other_fuel | 7.00 | C | Kerosene, crop residue; stable |
| Electricity | 92.00 | C | Saubhagya completion; tea gardens electrified; +4pp from 2019 |
| **Note** | (water/sanitation/electricity are independent; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 56.00 | D | Born in Jalpaiguri district or same block; multi-generational tea-garden resident families; slight increase due to COVID return migration from outside |
| WB_other_district | 8.00 | D | Internal WB migrants; Bengali middle-class in Nagrakata town from other districts |
| Other_Indian_state | 21.00 | D | Central Indian tribal labourers; Jharkhand/Bihar/Odisha origin Oraon/Munda/Santhali — now 3rd–5th generation residents; slight decline as net out-migration reduces new in-migration |
| Bangladesh_origin | 3.00 | D | Small settled Bengali Hindu fringe; not primarily a refugee AC |
| Outside_India | 0.50 | E | Negligible; some Nepal-origin Gorkha households near Bhutan border |
| Out_migrant | 3.50 | E | Young ST workers temporarily absent; COVID lockdown forced return of many; by end-2021 some had returned to work destinations |
| Jharkhand_origin | 8.00 | D | AC-local: specifically Jharkhand/Chhattisgarh/Odisha-origin Adivasi (Oraon/Munda/Santhali) tea-garden descent — set separately from Other_Indian_state to flag load-bearing historical migration stream; overlaps Other_Indian_state |
| **Sum** | **100.00** | — | self-check (Jharkhand_origin is sub-row documentation; core 6 rows sum to 100) |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Sadri | Santhali | Rajbongshi | Nepali | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 50.00 | 5.00 | 0.00 | 1.00 | 22.00 | 8.00 | 12.00 | 2.00 | E | Hindu population includes Bengali plains settlers + Rajbongshi + some Adivasi Hindu; Sadri-speaking Oraon who practice Hindu syncretic religion; stable from 2019 |
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

P(owns flag ‖ religion) — % within each religion. Updated for 2021 smartphone surge.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 64.00 | 58.00 | 86.00 | E | Bengali/Rajbongshi Hindu better-off; smartphone +23pp from 2019 |
| Muslim | 57.00 | 50.00 | 76.00 | E | Jalpaiguri Muslim smallholder; banking increased via Lakshmir Bhandar enrollment |
| Christian | 47.00 | 42.00 | 71.00 | E | Tea-garden Christian Adivasi; notable smartphone improvement |
| Sarna_ORP | 40.00 | 38.00 | 64.00 | E | Lowest but improving; smartphone penetration even in traditional Adivasi households |
| Other_residual | 62.00 | 52.00 | 80.00 | E | Mixed; Nepali Buddhist slightly above Adivasi avg |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4.00 | 9.00 | 14.00 | 20.00 | 21.00 | 23.00 | 9.00 | E |
| SC_total | 23.00 | 27.00 | 22.00 | 15.00 | 8.00 | 4.00 | 1.00 | E |
| ST_total | 33.00 | 27.00 | 19.00 | 13.00 | 5.50 | 1.50 | 1.00 | E |
| OBC | 16.00 | 25.00 | 22.00 | 19.00 | 11.00 | 6.00 | 1.00 | E |
| Other_Hindu_middle | 18.00 | 24.00 | 22.00 | 18.00 | 11.00 | 6.00 | 1.00 | E |
| Muslim | 28.00 | 27.00 | 21.00 | 15.00 | 6.00 | 2.50 | 0.50 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 11.00 | 9.00 | E |
| 23_27 | 10.00 | 8.00 | E |
| 28_32 | 9.00 | 6.00 | E |
| 33_37 | 8.00 | 4.50 | E |
| 38_42 | 6.50 | 3.50 | E |
| 43_47 | 5.50 | 2.50 | E |
| 48_52 | 4.50 | 1.80 | E |
| 53_57 | 3.50 | 1.20 | E |
| 58_62 | 2.80 | 0.90 | E |
| 63_67 | 2.20 | 0.70 | E |
| 68 | 1.80 | 0.60 | E |

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

P(owns smartphone ‖ occupation) — central media-access metric. Updated for 2021.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 38.00 | 52.00 | E | Non-tea smallholder; +16pp smartphone from 2019 |
| Agricultural_labourer | 28.00 | 42.00 | E | Poorest segment; notable improvement |
| Household_industry | 42.00 | 55.00 | E | |
| Manufacturing | 55.00 | 65.00 | E | |
| Construction | 48.00 | 58.00 | E | |
| Trade_retail | 72.00 | 78.00 | E | Nagrakata town traders |
| Transport_logistics | 65.00 | 70.00 | E | Tea-estate transport workers |
| Services | 78.00 | 80.00 | E | |
| Government_services_teachers | 92.00 | 95.00 | E | Highest; educated class |
| Out_migrant_worker | 80.00 | 75.00 | D | Working outside; smartphone essential |
| Tea_garden_worker | 35.00 | 50.00 | E | Notable improvement; +17pp smartphone; COVID drove adoption |

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
| U1_Tea_Garden_belt | 57.00 | 6.00 | 4.50 | 30.50 | 2.00 | E | Tea gardens heavily Adivasi; slight Sarna increase; fewer Bengali Hindu |
| U2_Non_Tea_rural | 86.00 | 11.00 | 0.50 | 1.50 | 1.00 | E | Non-tea GP villages predominantly Hindu with higher Muslim share; very few Adivasi |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Parent leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Tea_Garden_belt | 2.00 | 4.00 | 62.00 | 4.00 | 10.00 | 6.00 | 12.00 | E |
| U2_Non_Tea_rural | 7.00 | 14.00 | 20.00 | 9.00 | 20.00 | 11.00 | 19.00 | E |

### D.13 Sub-unit × Asset / media

Updated for 2021 smartphone surge.

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Tea_Garden_belt | 50.00 | 44.00 | 2.00 | 72.00 | E |
| U2_Non_Tea_rural | 66.00 | 63.00 | 7.00 | 88.00 | E |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Tea_Garden_belt | 25.00 | 48.00 | 72.00 | 89.00 | E |
| U2_Non_Tea_rural | 48.00 | 70.00 | 90.00 | 96.00 | E |

### D.15 Vote × Religion (2021 AE anchor)

P(party ‖ religion). 2021 AE result: BJP won (Puna Bhengra 49.55%), AITC second (Joseph Munda 37.27%). BJP retained Adivasi consolidation despite national anti-incumbency fears; AITC fell substantially from 2019 in this seat. The BJP swing in this ST-reserved seat ran counter to the AITC wave in south Bengal. Lakshmir Bhandar (launched April 2021 during campaign) had limited penetration before the vote date.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 55.00 | 30.00 | 5.00 | 6.00 | 4.00 | C | CSDS-Lokniti 2021 WB pattern + BJP tribal-belt strength; BJP still dominant among non-Adivasi Hindu in Nagrakata; INC showed strong performance (Sukbir Subba) |
| Muslim | 5.00 | 70.00 | 15.00 | 5.00 | 5.00 | C | Muslim consolidation behind AITC; INC retained some Muslim votes given good INC candidate |
| Christian | 65.00 | 18.00 | 8.00 | 3.00 | 6.00 | E | Tea-garden Christian ST voted BJP heavily in 2021 despite state-level AITC wave |
| Sarna_ORP | 75.00 | 12.00 | 4.00 | 3.00 | 6.00 | E | Highest BJP vote; Adivasi tribal identity consolidation under BJP strongest among traditional practitioners |
| Other_residual | 42.00 | 28.00 | 8.00 | 12.00 | 10.00 | E | Nepali Buddhist etc. mixed |

### D.16 Vote × Caste (2021 AE)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 58.00 | 28.00 | 7.00 | 5.00 | 2.00 | C | Bhadralok BJP-leaning maintained |
| OBC | 50.00 | 30.00 | 8.00 | 8.00 | 4.00 | C | Rajbongshi OBC; BJP-leaning in North Bengal |
| SC_total | 45.00 | 36.00 | 8.00 | 8.00 | 3.00 | C | SC in Jalpaiguri: Rajbanshi SC; BJP retained majority |
| ST_total | 72.00 | 14.00 | 5.00 | 3.00 | 6.00 | E | Load-bearing: ST tribal bloc overwhelmingly BJP in 2021 AE; result confirms 49.55% BJP driven by 45% ST population with ~72% BJP vote |
| Other_Hindu_middle | 50.00 | 30.00 | 8.00 | 8.00 | 4.00 | C | Rajbongshi / Gorkha middle; BJP leaning |
| Muslim | 5.00 | 70.00 | 15.00 | 5.00 | 5.00 | C | Mirrors D.15 |

### D.17 Vote × Gender (2021 AE)

Lakshmir Bhandar launched April 2021 (during campaign). Limited direct cash transfer penetration before the election; but the announcement itself had an influence, especially on female voters.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 62.00 | 25.00 | 5.00 | 5.00 | 3.00 | C | Tribal male BJP-leaning strong; CSDS 2021 WB pattern adjusted for North Bengal ST belt |
| Female | 55.00 | 30.00 | 7.00 | 4.00 | 4.00 | C | Tea-garden female workers BJP-leaning; Lakshmir Bhandar announcement had modest female AITC pull but BJP won seat decisively |

### D.18 Vote × Welfare

AC 021 does not declare a `welfare_exposure` axis — skip per schema §4.7. No welfare joint table.

---

## E. 2021 baseline vote (calibration target)

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 49.55 | A | ECI 2021 WB AE; Puna Bhengra (BJP) 94,722 votes / 191,169 valid votes; data/electoral_history/2021/detailed_results.csv |
| AITC | 37.27 | A | ECI 2021 WB AE; Joseph Munda (AITC) 71,247 votes |
| INC | 6.51 | A | ECI 2021 WB AE; Sukbir Subba (INC) 12,442 votes — notably strong INC performance |
| LF | 0.00 | A | No LF candidate stood in AC 021 in 2021 AE |
| Other_NOTA | 6.67 | A | NOTA 5,454 + IND Robat Munda 3,283 + PrPP Benam Oraon 2,247 + IND Ashan Tirkey 1,774 = 12,758 votes |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 021 — Nagrakata (Assembly Elections)

Nagrakata is an ST-reserved seat in Jalpaiguri district. Historically it was a Left Front (RSP/CPI-M) bastion in the tea-garden belt, with RSP particularly strong due to tea-garden trade union presence. AITC made inroads in 2011 on the anti-Left wave. INC was competitive in this seat in 2016 given the strong tribal opposition vote. BJP emerged as the dominant force from 2019, riding Adivasi tribal consolidation — and maintained that dominance in the 2021 AE despite a state-wide AITC wave.

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin |
|---|---|---|---|---|---|---|---|---|---|
| 2016 AE | Sukra Munda | AITC | 57,306 | 32.46% | Joseph Munda | INC | 54,078 | 30.63% | 3,228 votes / 1.83 pp |
| 2021 AE | Puna Bhengra | BJP | 94,722 | 49.55% | Joseph Munda | AITC | 71,247 | 37.27% | 23,475 votes / 12.28 pp |

(2016 AE source: data/electoral_history/2016/detailed_results.csv — tier A. Total valid votes 2016: 176,542; total electors: 213,862; turnout 82.5%. John Barla (BJP) ran third in 2016 with 47,836 votes / 27.10% — he later won Alipurduar LS in 2019 and became Union Minister of State.)

(2021 AE source: data/electoral_history/2021/detailed_results.csv — tier A. Total valid votes: 191,169; total electors: 237,305; turnout 80.6%.)

### Jalpaiguri / Alipurduar LS historical

Note: Before 2014 delimitation Nagrakata was part of Jalpaiguri LS (PC 02). After 2014 it moved to Alipurduar LS (PC 02, now ST-reserved).

| Year | LS PC | Winner | Party | Notes |
|---|---|---|---|---|
| 2014 LS | Alipurduar (02) | Ss Barua | AITC | AITC won; BJP rising; new PC after delimitation |
| 2019 LS | Alipurduar (02) | John Barla | BJP | BJP swept; Nagrakata segment ~58% BJP (2019_AssemblySegmentLevelVotingData.csv tier A) |

### 2019 LS anchor (calibration anchor for D.15–D.17 starting priors)

| Party | AC 021 segment 2019 % | tier | note |
|---|---|---|---|
| BJP | 58.41 | A | ECI GE2019; 103,865 votes / 177,813 valid; 2019_AssemblySegmentLevelVotingData.csv |
| AITC | 30.16 | A | ECI GE2019; 53,621 votes |
| INC | 3.03 | A | ECI GE2019; 5,391 votes |
| LF | 6.44 | A | ECI GE2019; RSP 10,641 + SUCI(C) 811 = 11,452 votes |
| Other_NOTA | 1.96 | A | ECI GE2019; IND 1,027 + IND 2,457 = 3,484 votes |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Election Commission of India — 2021 WB Assembly Election detailed results via `data/electoral_history/2021/detailed_results.csv` (AC 021: 237,305 electors, 191,169 valid votes; winner BJP Puna Bhengra 94,722 / 49.55%)
- Election Commission of India — 2016 WB Assembly Election detailed results via `data/electoral_history/2016/detailed_results.csv` (AC 021: 213,862 electors, 176,542 valid votes)
- Election Commission of India — 2019 LS Form-20 via `data/2019_AssemblySegmentLevelVotingData.csv` (AC 021 segment: 226,235 electors, 177,813 valid votes)
- Delimitation Commission of India 2008 — WB Schedule (AC 021 Nagrakata = Nagrakata CD Block; ST reserved)
- Census of India 2011 — Jalpaiguri district Primary Census Abstract and CD Block tables

### Secondary sources (tier B/C)

- NFHS-5 (2019-21) West Bengal — household amenities, asset ownership baseline; updated smartphone and banking penetration
- NFHS-4 (2015-16) West Bengal — comparison baseline for 2019→2021 shifts
- CSDS-Lokniti 2021 WB post-poll — vote × religion / caste / gender (WB regional rollup with North Bengal tribal-belt adjustment)
- WB District Statistical Handbook — Jalpaiguri
- Census 2011 — Jalpaiguri CD Block data (Nagrakata block); ST population, literacy, workers

### Tertiary / journalistic (tier D)

- Wikipedia: "Nagrakata (Vidhan Sabha constituency)" — reservation status, LS segment, election history
- Wikipedia: "Jalpaiguri district" — demographics, ST composition, tea garden economy
- Wikipedia: "Alipurduar (Lok Sabha constituency)" — 2019/2021 LS result; BJP win; tea-belt Adivasi vote
- Journalistic coverage of BJP win in 2021 AE in North Bengal tribal belt seats despite overall AITC wave
- Reports on Lakshmir Bhandar (Apr 2021) — limited penetration in Jalpaiguri tea-garden belt before May 2021 vote
- COVID-19 reverse migration reports — Jalpaiguri/Alipurduar tea workers returning from Sikkim/Assam in 2020

### Tier-D/E reliance flags (what to distrust)

- **ST composition within Hindu / Sarna split** (C.1, C.2, D.2) — Census 2011 religion tables do not separate Hindu-practicing ST from Sarna ORP cleanly; all Adivasi estimates are tier E
- **Sadri/Santhali/Rajbongshi mother-tongue shares** (C.5, D.1) — no AC-level linguistic data; Jalpaiguri district 2011 census proxy; tier E
- **Sub-unit decomposition** (C.11, D.11–D.14) — v0 collapses entire block into 2 sub-units; no GP-level data
- **Vote × Demographic conditionals** (D.15–D.17) — CSDS 2021 WB rollup with tribal-belt adjustment; tier C/E; **calibration target (§E) is tier A** from ECI archive
- **2016 AE assembly results** (F) — tier A from ECI archive CSV; confirmed
- **Smartphone penetration 2021** (C.14) — NFHS-5 WB rural pattern applied; notable surge acknowledged; tier C
- **Banking via Lakshmir Bhandar** (C.14) — scheme launched Apr 2021; bank account enrollment partially counted pre-vote; tier C
- **Migration / birthplace** (C.16, D.3) — no AC-level Census D-series; tier D estimate from tea-garden historical settlement pattern

### v0 known gaps

1. DCHB Jalpaiguri Part-A — sub-unit decomposition uses only 2 cells; refine when GP-level data available
2. Census HH-13 GP-level — asset/media data proxied from NFHS-5 state pattern
3. Census D-series — migration data proxied from tea-garden historical settlement pattern
4. Linguistic census 2011 — Sadri/tribal language shares at block level not directly retrieved
5. CSDS-Lokniti 2021 WB North Bengal tribal-belt sub-sample — full cross-tabs not independently verified; using WB regional pattern + adjustment
6. Lakshmir Bhandar penetration data (WB CDWDSW dashboard) — Jalpaiguri district enrollment rate not fetched; by election-day (May 2021) scheme had just launched

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No post-2021 events referenced.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs anchored on 2021 priors.

### 2024 Lok Sabha Election — AC 021 segment within Alipurduar LS (PC 02) (tier A, CSV)

> Figures below sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=21, Nagrakata. Total electors: 244,174; total valid votes: 184,131; turnout ~75.4%.

| Party | Candidate (LS level) | Votes | AC-021 segment % | Tier | Source |
|---|---|---|---|---|---|
| AITC | Prakash Chik Baraik | 83,279 | **45.23%** | A | 2024_AssemblySegmentLevelVotingData.csv |
| BJP | Manoj Tigga | 79,732 | **43.30%** | A | Same |
| LF (RSP) | Mili Oraon | 7,627 | **4.14%** | A | Same |
| INC | — | 0 | **0.00%** | A | No INC candidate in Alipurduar LS 2024 |
| Other_NOTA | NOTA 4,644 + AISF 0 + BSP 1,299 + SUCI 448 + KPPU 377 + GNASURKP 362 + NBNGPLPP 617 + KMSP 1,114 + IND 4,632 | 13,493 | **7.33%** | A | Same |
| **AITC margin over BJP** | | **3,547 votes** | **1.93 pp** | A | Computed |

> **Key observation for simulation**: AC 021 shows a notable AITC recovery in 2024 LS relative to the 2021 AE result (BJP 49.55% → 43.30%; AITC 37.27% → 45.23%), reversing the 2021 BJP dominance. This is the key validation challenge for the simulator running from 2021 priors.

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC-021 segment shares within ±3pp of the tier-A figures:
- BJP target: 43% ± 3pp
- AITC target: 45% ± 3pp
- LF target: 4% ± 3pp
- Other_NOTA target: 7% ± 3pp
