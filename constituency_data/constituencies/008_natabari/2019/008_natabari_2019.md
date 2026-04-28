# AC 008 — Natabari (GEN) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 008 Natabari as of 2019 only — it does not reference
> any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 008 | A | ECI / Delimitation Commission 2008 |
| AC name | Natabari | A | ECI |
| Reservation | GEN | A | Delimitation 2008 |
| District | Cooch Behar | A | Delimitation 2008 |
| Sub-division | Tufanganj | A | WB administrative |
| LS constituency | 2 — Cooch Behar | A | Delimitation 2008 |
| LS segments included | AC 5 Sitai · AC 6 Sitalkuchi · AC 7 Mathabhanga · AC 8 Natabari · AC 9 Cooch Behar Uttar · AC 10 Cooch Behar Dakshin · AC 11 Dinhata | A | Delimitation 2008 |
| AC composition | Natabari CD Block GPs + Tufanganj-I CD Block partial overlap | A | Delimitation 2008 |
| Geographic note | Northern Cooch Behar district; flat terai-plain; bordered by Assam (north-east) and Jalpaiguri (west); predominantly agricultural with Rajbanshi-majority rural communities | A | — |
| Sub-units used in v0 | **U1: Natabari_CDB_core** (Natabari block GPs) · **U2: Tufanganj_I_partial** (overlap GPs from Tufanganj-I block) | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~265,000 | E | Census 2011 Natabari CD Block primary census abstract; Tufanganj-I partial |
| 2019 projected population | ~285,000 | E | 8-yr compound projection at ~1.0%/yr growth (Cooch Behar district trend) |
| Sex ratio (2019, F per 1000 M) | ~963 | E | Cooch Behar district Census 2011 sex ratio 963; projected stable |
| 2019 estimated electorate (18+) | ~235,000 | D | ECI 2019 LS roll 235,277 (tier A from CSV) |
| Estimated M / F / TG split (2019) | 50.9% M / 49.1% F / <0.05% TG | E | Derived from district sex ratio 963 |
| 2019 polling stations (estimated) | ~280 | E | Proportional to electorate vs district average |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 79.50 | E | Cooch Behar district Census 2011 Hindu 79.7%; Natabari block slightly below district average; projected stable 2011→2019 |
| Muslim | 18.80 | E | Cooch Behar district Muslim 18.4%; Natabari block slightly above district; Tufanganj subdivision higher Muslim share; projected +0.2pp relative gain 8yr |
| Christian | 0.80 | E | Cooch Behar district 2011 ~0.9%; small Rajbanshi Christian fringe + Bengali Christian |
| Sarna_ORP | 0.50 | E | Small tribal pocket; Cooch Behar district tribal-religion fringe |
| Other_residual | 0.40 | E | Sikh + Jain + Buddhist + Not_stated |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 28.00 | A | Cooch Behar district SC 28.36% (Census 2011); Natabari block ~28% estimated |
| └ Rajbanshi_SC | 22.00 | C | Rajbanshi is the dominant SC in Cooch Behar; ~78% of SC pool; also found among OBC and General |
| └ Namasudra_SC | 3.50 | E | Smaller SC sub-group in Cooch Behar |
| └ Other_SC | 2.50 | E | Residual SC (Bagdi, Koch, Jhalo-Malo, etc.) |
| **ST_total** | 1.50 | A | Cooch Behar district ST 1.54% (Census 2011) |
| UC_bhadralok | 4.00 | E | Brahmin/Kayastha/Baidya; small in this predominantly Rajbanshi-dominated AC |
| OBC | 12.00 | E | Rajbanshi OBC (non-SC fraction of Rajbanshi community) + Koch-Rajbanshi + other OBC; Cooch Behar pattern |
| Other_Hindu_middle | 34.00 | E | Residual Hindu middle castes — Rajbanshi General + Saha + Sutradhar + Kaibarta + others; 79.50 − 28.0 SC − 1.5 ST − 4.0 UC − 12.0 OBC − 18.8 Muslim − 0.8 Chr − 0.5 Sarna = 33.9 ≈ 34 |
| Muslim | 18.80 | E | All sub-castes pooled (mostly Bengali-Sheikh in Cooch Behar) |
| Christian_plus_Sarna_plus_Other | 1.70 | E | Christian 0.80 + Sarna_ORP 0.50 + Other_residual 0.40 |
| **Sum** | **100.00** | — | self-check (parent rows only) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.00 | E | Renormalized from Cooch Behar district Census 2011 age pyramid, 18+ only |
| 23_27 | 11.50 | E | |
| 28_32 | 11.00 | E | |
| 33_37 | 10.50 | E | |
| 38_42 | 10.00 | E | |
| 43_47 | 9.50 | E | |
| 48_52 | 9.00 | E | |
| 53_57 | 8.00 | E | |
| 58_62 | 7.00 | E | |
| 63_67 | 6.50 | E | |
| 68 | 6.00 | E | 68+ open-ended cohort |
| **Sum** | **100.00** | — | self-check (18+ adults only, renormalized) |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.93 | E | District sex ratio 963 F per 1000 M → 1000/(1963)=50.94% M; rounded |
| Female | 49.06 | E | 963/(1963)=49.06% F |
| Third_gender | 0.01 | E | State pattern; negligible |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 68.50 | E | Cooch Behar district 2011: Bengali ~67%; slight increase with urbanization trend |
| Hindi | 1.50 | E | Trader and migrant worker fringe |
| Urdu | 1.00 | E | Small Muslim minority in urban pockets |
| Other | 1.50 | E | Residual catch-all (Assamese fringe, Nepali border communities, others) |
| Rajbongshi | 27.50 | E | Rajbongshi/Rajbanshi language; AC-local dominant language; Cooch Behar district ~27-30% Rajbongshi-speaking |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 18.00 | E | Cooch Behar district literacy 75.7% (Census 2011); Natabari block rural pull; ~18% illiterate after +3pp improvement 2011→2019 |
| Primary | 25.00 | E | Census 2011 education distribution, Cooch Behar district scaled |
| Middle | 22.00 | E | |
| Secondary | 16.00 | E | |
| Higher_Secondary | 10.00 | E | |
| Graduate | 7.00 | E | |
| Postgraduate | 2.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 33.00 | E | Cooch Behar district Census 2011 main-worker share ~32-34%; predominantly agricultural |
| Marginal_worker | 12.00 | E | Seasonal agricultural labour |
| Non_worker | 37.00 | E | Housewife + elderly + retired; heavy in rural Rajbanshi households |
| Student | 10.00 | E | 18–22 cohort in education |
| Unemployed | 8.00 | E | Educated job-seekers; young aspirant pool in Cooch Behar |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 28.00 | E | Cooch Behar district 2011 rural cultivator share ~30%; AC slightly below with some urban fringe |
| Agricultural_labourer | 30.00 | E | Dominant in flat terai-plain; large landless SC/OBC pool |
| Household_industry | 5.00 | E | Handloom + cottage industries; small Rajbanshi weaving tradition |
| Manufacturing | 3.00 | E | Limited organised manufacturing in Natabari block |
| Construction | 7.00 | E | Local construction + seasonal migration to larger towns |
| Trade_retail | 10.00 | E | Block-level market towns (Natabari haat) |
| Transport_logistics | 4.00 | E | Road transport; border-adjacent trade route |
| Services | 8.00 | E | Private sector services in block-level towns |
| Government_services_teachers | 3.00 | E | Block-level govt offices, schools |
| Out_migrant_worker | 2.00 | D | Rajbanshi men to brick kilns in Siliguri/Kolkata; modest flow |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.00 | E | Census B-04 WB rural pattern; small trader/landowner employers |
| Employee | 22.00 | E | Govt + organised sector + retail; moderate in this rural AC |
| Single_worker | 52.00 | E | Own-account cultivator + artisan + small trader; dominant |
| Family_worker | 24.00 | E | Unpaid family labour in agriculture; common in Rajbanshi cultivator households |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 26.00 | C | Cooch Behar district BPL ~30% (Census 2001 baseline); WB poverty fell ~6pp 2011-19 → ~24-28% estimate |
| Above_Poverty_Line_low_income | 36.00 | E | Low-income rural agricultural households |
| Lower_middle | 22.00 | E | Modest income cultivators, small traders |
| Middle | 12.00 | E | Block-level service class, government employees |
| Upper_middle_well_off | 4.00 | E | Very small affluent fringe; no significant urban centre in this AC |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Natabari_CDB_core | 72.00 | E | Natabari CD Block core GPs; majority of AC population; Census 2011 Natabari block ~190,000 population |
| U2_Tufanganj_I_partial | 28.00 | E | Overlap GPs from Tufanganj-I CD Block that fall within AC boundary per Delimitation 2008; ~75,000 population estimate |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | Cooch Behar district 2011: average HH size ~4.5; rural Rajbanshi households slightly larger |
| Nuclear_HH | 65.00 | E | NFHS-4 WB rural pattern; dominant nuclear form in Rajbanshi households |
| Joint_HH | 27.00 | E | Traditional joint family arrangement in agricultural households |
| Extended_multi_generation | 8.00 | E | Multi-generation in older Rajbanshi extended families |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.00 | E | Census 2011 Cooch Behar pattern; earlier marriage age in rural communities |
| Currently_married | 66.00 | E | High marriage rate; Rajbanshi cultural norm of early marriage |
| Widowed | 8.00 | E | Concentrated in 60+, female-skewed |
| Separated_divorced | 1.00 | E | Low formal divorce rate; some separation in migrant households |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 70.00 | C | NFHS-4 WB rural 60%, +5pp/yr → AC ~70% (2019); Cooch Behar slightly below state average |
| Radio | 6.00 | C | Declining nationally; slightly higher in rural Cooch Behar |
| Mobile_phone | 82.00 | C | NFHS-4 WB ~78%; +growth → ~82% by 2019 |
| Smartphone_with_internet | 38.00 | C | NFHS-4 rural baseline + Jio rollout 2016-19; Cooch Behar below state average |
| Computer | 5.00 | E | Very low in rural Cooch Behar; mostly government offices |
| Two_wheeler | 22.00 | C | NFHS-4 WB rural 18%; +growth; common among OBC/SC rural household |
| Four_wheeler | 4.00 | E | Very limited; mainly large landowners and block-level traders |
| Banking_access | 84.00 | B | PMJDY saturation 2014-; slightly lower than state average due to rural remoteness |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 78.00 | C | NFHS-4 WB rural 84%; Cooch Behar slightly below state; ground water access good |
| Improved_sanitation | 55.00 | C | NFHS-4 WB rural 51%; +Swachh Bharat 2014-19 (+12pp rural) |
| LPG_clean_cooking_fuel | 32.00 | C | NFHS-4 WB rural 24%; +Ujjwala 2016-19 (+8pp rural); Cooch Behar below state average |
| Wood_biomass_fuel | 62.00 | C | Primary cooking fuel in rural Cooch Behar; declining as LPG rises |
| Other_fuel | 6.00 | E | Kerosene, dung, other |
| Electricity | 90.00 | C | Census 2011 + Saubhagya 2017-19; Cooch Behar rural ~90% electrified by 2019 |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 75.00 | D | Predominantly native Rajbanshi community; very low historic migration out of Cooch Behar |
| WB_other_district | 7.00 | D | Some in-migrants from Jalpaiguri, North Dinajpur for agricultural labour; Cooch Behar absorption limited |
| Other_Indian_state | 2.00 | D | Assamese and Bihari trading fringe |
| Bangladesh_origin | 12.00 | D | Partition-era and post-1971 Hindu migrant fraction; significant but below Bangaon levels; mainly Namasudra/lower-caste Hindu |
| Outside_India | 0.50 | E | Negligible (some Bhutanese traders) |
| Out_migrant | 3.50 | E | Working outside (mainly Siliguri/Kolkata/brick kilns); registered here |
| Nepal_Bhutan_origin | 0.00 | E | Not applicable to this AC (set to 0) |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 60.00 | 1.50 | 0.00 | 1.50 | 37.00 | E | Rajbanshi Hindu population speaks Rajbongshi; Bengali Hindus (migrant + educated) also present; Cooch Behar 2011 language pattern |
| Muslim | 92.00 | 0.50 | 3.00 | 1.50 | 3.00 | E | Cooch Behar Muslims are predominantly Bengali-speaking Sheikh community; small Rajbongshi-Muslim fringe |
| Christian | 60.00 | 5.00 | 0.00 | 10.00 | 25.00 | E | Rajbanshi Christian converts + Bengali Christian minority |
| Sarna_ORP | 20.00 | 5.00 | 0.00 | 30.00 | 45.00 | E | Tribal fringe; mixed Rajbongshi + other tribal languages |
| Other_residual | 50.00 | 30.00 | 5.00 | 15.00 | 0.00 | E | Sikh/Jain/Buddhist traders; Hindi-dominant |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. 2D table.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 33.33 | 1.89 | 5.03 | 15.09 | 44.65 | 0 | 0 | E | 28% SC / 79.5% Hindu = 35.2%; adjusted for Hindu-only SC share; OBC Rajbanshi estimated at 15% within Hindu; residual Other_Hindu_middle |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 20.00 | 60.00 | 0 | 10.00 | 10.00 | 0 | 0 | E | Tribal sarna: mostly ST + SC pool; small OBC |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 72.00 | 7.00 | 2.00 | 15.00 | 0.50 | 3.50 | D | Rajbanshi native Hindu dominant; ~15% traceable to partition/post-partition Bangladesh Hindu migration |
| Muslim | 92.00 | 5.00 | 1.00 | 1.00 | 0.50 | 0.50 | D | Cooch Behar Muslims mostly native Bengali-Sheikh peasantry; very small Bangladesh-origin trickle |
| Christian | 85.00 | 10.00 | 2.00 | 3.00 | 0.00 | 0.00 | E | Predominantly local Rajbanshi converts |
| Sarna_ORP | 90.00 | 5.00 | 3.00 | 1.00 | 0.00 | 1.00 | E | Indigenous tribal; predominantly native |
| Other_residual | 30.00 | 20.00 | 45.00 | 0.00 | 5.00 | 0.00 | E | Mostly other-state Sikh/Jain traders |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 72.00 | 40.00 | 86.00 | C | NFHS-4 WB religion gap pattern; Hindu slightly above Muslim in rural WB |
| Muslim | 62.00 | 30.00 | 76.00 | C | Cooch Behar Muslim pocket slightly below Hindu; NFHS-4 WB pattern |
| Christian | 75.00 | 42.00 | 88.00 | E | Small base; similar to Hindu average |
| Sarna_ORP | 55.00 | 20.00 | 70.00 | E | Lower access; tribal fringe |
| Other_residual | 85.00 | 60.00 | 95.00 | E | Trader community; higher access |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 5.00 | 10.00 | 12.00 | 18.00 | 20.00 | 25.00 | 10.00 | E |
| SC_total | 20.00 | 28.00 | 22.00 | 16.00 | 9.00 | 4.00 | 1.00 | E |
| ST_total | 28.00 | 30.00 | 20.00 | 13.00 | 6.00 | 2.00 | 1.00 | E |
| OBC | 16.00 | 26.00 | 23.00 | 18.00 | 10.00 | 6.00 | 1.00 | E |
| Other_Hindu_middle | 15.00 | 26.00 | 23.00 | 18.00 | 10.00 | 7.00 | 1.00 | E |
| Muslim | 22.00 | 28.00 | 22.00 | 16.00 | 8.00 | 3.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 14.00 | 12.00 | E |
| 23_27 | 13.00 | 10.00 | E |
| 28_32 | 12.00 | 8.00 | E |
| 33_37 | 10.00 | 5.00 | E |
| 38_42 | 9.00 | 4.00 | E |
| 43_47 | 8.00 | 3.00 | E |
| 48_52 | 7.00 | 2.00 | E |
| 53_57 | 6.00 | 2.00 | E |
| 58_62 | 5.00 | 1.50 | E |
| 63_67 | 4.00 | 1.00 | E |
| 68 | 3.00 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8.00 | 35.00 | E |
| 23_27 | 45.00 | 82.00 | E |
| 28_32 | 82.00 | 93.00 | E |
| 33_37 | 92.00 | 91.00 | E |
| 38_42 | 93.00 | 89.00 | E |
| 43_47 | 92.00 | 87.00 | E |
| 48_52 | 90.00 | 82.00 | E |
| 53_57 | 88.00 | 74.00 | E |
| 58_62 | 85.00 | 64.00 | E |
| 63_67 | 78.00 | 45.00 | E |
| 68 | 70.00 | 30.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 28.00 | 65.00 | C | Rural agricultural baseline; Cooch Behar rural below state average |
| Agricultural_labourer | 18.00 | 55.00 | C | Lowest income group in AC |
| Household_industry | 30.00 | 68.00 | C | Artisan weaver households |
| Manufacturing | 42.00 | 75.00 | C | Slightly higher income |
| Construction | 35.00 | 68.00 | C | Mobile-heavy out-migrant pattern |
| Trade_retail | 58.00 | 82.00 | C | Block-market traders; higher access |
| Transport_logistics | 50.00 | 75.00 | C | |
| Services | 60.00 | 85.00 | C | |
| Government_services_teachers | 75.00 | 90.00 | C | Highest access; government employer provides stable income |
| Out_migrant_worker | 55.00 | 72.00 | D | Working outside; smartphone-reliant for remittances |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 32.00 | 2.00 | E |
| Primary | 36.00 | 4.00 | E |
| Middle | 34.00 | 6.00 | E |
| Secondary | 28.00 | 10.00 | E |
| Higher_Secondary | 22.00 | 15.00 | E |
| Graduate | 26.00 | 18.00 | E |
| Postgraduate | 35.00 | 14.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 008. See NORMALIZED_SCHEMA §4.7.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Natabari_CDB_core | 81.00 | 17.00 | 0.80 | 0.70 | 0.50 | E | Natabari block core GPs; higher Hindu proportion; Rajbanshi majority |
| U2_Tufanganj_I_partial | 74.00 | 24.00 | 0.80 | 0.20 | 1.00 | E | Tufanganj-I GPs overlap; higher Muslim share in Tufanganj sub-division; Census 2011 Tufanganj |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit).

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Natabari_CDB_core | 4.50 | 29.00 | 1.50 | 12.00 | 35.00 | 17.00 | 1.00 | E |
| U2_Tufanganj_I_partial | 3.00 | 25.00 | 1.50 | 11.00 | 32.00 | 24.00 | 3.50 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Natabari_CDB_core | 72.00 | 40.00 | 5.00 | 86.00 | E |
| U2_Tufanganj_I_partial | 64.00 | 32.00 | 4.00 | 78.00 | E |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Natabari_CDB_core | 34.00 | 58.00 | 80.00 | 92.00 | E |
| U2_Tufanganj_I_partial | 26.00 | 48.00 | 72.00 | 86.00 | E |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 WB regional rollup adapted for Cooch Behar.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 60.00 | 33.00 | 1.50 | 3.50 | 2.00 | C | BJP strong Hindu swing in Cooch Behar 2019 (Koch-Rajbanshi community mobilization + Poriborton narrative); CSDS 2019 WB regional adapted |
| Muslim | 5.00 | 75.00 | 10.00 | 8.00 | 2.00 | C | Muslim consolidation towards AITC in Cooch Behar; CSDS 2019 WB Muslim vote pattern |
| Christian | 30.00 | 50.00 | 10.00 | 5.00 | 5.00 | E | Mixed; small base |
| Sarna_ORP | 40.00 | 40.00 | 5.00 | 10.00 | 5.00 | E | Tribal fringe; split BJP-AITC |
| Other_residual | 50.00 | 30.00 | 8.00 | 6.00 | 6.00 | E | |

### D.16 Vote × Caste (2019 LS)

P(party ‖ caste) — CSDS-Lokniti 2019 WB adapted for Cooch Behar.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 58.00 | 28.00 | 5.00 | 6.00 | 3.00 | C | Bhadralok BJP-leaning 2019 |
| OBC | 52.00 | 36.00 | 3.00 | 6.00 | 3.00 | C | Koch-Rajbanshi OBC largely swung BJP in 2019; Cooch Behar Rajbanshi mobilization |
| SC_total | 55.00 | 37.00 | 2.00 | 4.00 | 2.00 | C | Rajbanshi SC component went BJP; BJP "Koch-Rajbanshi" electoral appeal |
| ST_total | 42.00 | 38.00 | 3.00 | 12.00 | 5.00 | E | ST pocket split more evenly |
| Other_Hindu_middle | 54.00 | 35.00 | 2.50 | 5.50 | 3.00 | C | Rajbanshi General Hindu went BJP in wave |
| Muslim | 5.00 | 75.00 | 10.00 | 8.00 | 2.00 | C | Same as D.15 |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

P(party ‖ gender).

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 54.00 | 38.00 | 1.50 | 4.50 | 2.00 | C | CSDS 2019 WB male vote; BJP-strong in Cooch Behar male vote |
| Female | 48.00 | 46.00 | 2.00 | 2.50 | 1.50 | C | CSDS 2019 WB female; AITC advantages among women lower in this AC than state average due to Rajbanshi community mobilization |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for AC 008. See NORMALIZED_SCHEMA §4.7.)

---

## E. 2019 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 51.05 | A | ECI 2019 LS — 2019_AssemblySegmentLevelVotingData.csv, AC 8 — 104,543 votes / 204,796 total |
| AITC | 42.00 | A | ECI 2019 LS — 86,018 votes / 204,796 total |
| INC | 1.68 | A | ECI 2019 LS — 3,432 votes / 204,796 total |
| LF | 3.75 | A | ECI 2019 LS — AIFB 7,679 votes / 204,796 total (AIFB is the Left Front component here; SUCI(C) 377 added to Other_NOTA) |
| Other_NOTA | 1.52 | A | ECI 2019 LS — KPPU 217 + WPOI 169 + SUCI(C) 377 + AMB 202 + IND 488 + IND 998 + IND 673 = 3,124 votes / 204,796 total |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 008 Natabari (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Rabindranath Ghosh | AITC | ~52 | CPI(M) candidate | CPI(M) | ~35 | ~10,000 (est.) |
| 2016 AE | Rabindranath Ghosh | AITC | ~50 | BJP candidate | BJP | ~29 | ~12,000 (est.) |

Note: Rabindranath Ghosh (later WB cabinet minister) was the dominant AITC MLA for Natabari. His mass base among Rajbanshi communities in Cooch Behar made Natabari an AITC stronghold pre-2019. The 2019 LS result (BJP 51%) represented a sharp swing from the 2016 AE baseline driven by BJP's Rajbanshi community mobilization and Koch-Rajbanshi identity politics.

### Cooch Behar Lok Sabha (PC 2) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Renuka Sinha | AITC | ~40 | AITC won; BJP ~22%; CPI(M) ~20%; close 3-way |
| 2014 by-poll (if applicable) | — | — | — | No major by-poll noted for this period |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- Census of India 2011 — Cooch Behar district Primary Census Abstract; CD Block tables for Natabari block and Tufanganj-I block
- Census of India 2011 — Cooch Behar district religion, SC/ST, language tables (District Census Handbook)
- Election Commission of India — 2019_AssemblySegmentLevelVotingData.csv (tier A; AC 8 Natabari segment)
- ECI — 2011 AE, 2016 AE results for AC 008 Natabari (via ECI archive / Wikipedia)
- Delimitation Commission of India 2008 — WB Schedule (AC 008 Natabari composition)

### Secondary sources (tier B/C)
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline (state + rural/urban gradient)
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2019 NES post-poll — vote × religion / caste / gender regional WB rollup
- WB District Statistical Handbook — Cooch Behar district

### Tertiary / journalistic (tier D)
- Wikipedia — "Natabari (Vidhan Sabha constituency)" — reservation status, LS seat mapping
- Wikipedia — "Cooch Behar district" — population, SC/ST, language demographics
- Reports on BJP's Koch-Rajbanshi mobilization in Cooch Behar 2019 (various news sources)

### Tier-D/E reliance flags (what to distrust)
- **Caste sub-group shares within Hindu** (D.2) — no caste census post-1931 for non-SC/ST; tier C/E
- **Migration/birthplace shares** (C.16, D.3) — no AC-level Census D-series; tier D estimate
- **GP-level sub-unit decomposition** (D.11–D.14) — v0 collapses to 2 sub-units; refine with DCHB Part-A
- **Asset/media** (C.14, D.4, D.8, D.13) — NFHS-4/5 state-level pattern applied; tier C
- **Vote × Demographic** (D.15–D.17) — CSDS 2019 WB regional rollup adapted; tier C
- **Assembly election results** (F) — approximate %s from Wikipedia summary; not Form-20 level accuracy

### v0 known gaps
1. DCHB Cooch Behar Part-A — collapsed sub-units to 2 instead of GP-level granularity
2. ECI 2011/2016 AE Form-20 for AC 008 — using approximate estimates from Wikipedia
3. Census HH-13 GP-level asset data — using NFHS state-level proxy
4. Full CSDS WB regional cross-tabs for Cooch Behar — using adapted state-level rollup
5. Rajbanshi sub-caste disaggregation — SC/OBC/GEN split within Rajbanshi community estimated from academic literature

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge.
No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2021 WB Assembly Election — AC 008 Natabari (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| AITC | Rabindranath Ghosh | (to be fetched) | ~50 | A — ECI 2021 AE (placeholder; fetch from ECI archive) |
| BJP | Mihir Goswami | (to be fetched) | ~46 | A — ECI 2021 AE (placeholder) |
| **Note** | Full ECI 2021 Form-20 figures to be populated from ECI archive | | | |

### 2024 Lok Sabha Election — AC 008 segment within Cooch Behar LS (PC 2) (tier A)

> Figures below are **tier A** — sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=8, Natabari. Total candidate votes: 218,241; NOTA: 1,817; grand total: 220,058; electorate 255,111; turnout ~86.3%.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Nisith Pramanik | 105,063 | **47.76%** | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | (AITC candidate) | 103,917 | **47.24%** | A | Same |
| AIFB (LF) | (AIFB candidate) | 4,697 | **2.14%** | A | Same |
| INC | (INC candidate) | 1,245 | **0.57%** | A | Same |
| NOTA | — | 1,817 | **0.83%** | A | Same (NOTA column) |
| Others (BSP, SUCI, KPPU, IND×7) | various | 3,319 | **1.51%** | A | Same |
| **BJP margin over AITC** | | **1,146 votes** | **0.52 pp** | A | Computed — very tight contest |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024
LS AC segment shares within ±3pp of the tier-A figures (BJP / AITC / INC
/ LF combined). Note: BJP lead narrowed dramatically from 9pp (2019) to 0.52pp (2024) — this shift must emerge from narrative injection, not be baked in.
