# AC 015 — Dhupguri (GEN) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 015 Dhupguri as of 2019 only — it does not reference any
> post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../NORMALIZED_SCHEMA.md) (canonical schema)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 015 | A | ECI / Delimitation Commission 2008 |
| AC name | Dhupguri | A | ECI |
| Reservation | GEN (unreserved) | A | Delimitation 2008 |
| District | Jalpaiguri | A | Delimitation 2008 |
| Sub-division | Dhupguri | A | WB administrative |
| LS constituency | 03 — Jalpaiguri | A | Delimitation 2008 |
| LS segments included | AC 013 Mal · 014 Nagrakata · 015 Dhupguri · 016 Maynaguri · 017 Jalpaiguri · 018 Rajganj · 019 Dabgram-Fulbari | A | Delimitation 2008 |
| AC composition | Dhupguri Municipality (Dhupguri Paurashava) + portions of Dhupguri CD Block GPs | A | Delimitation 2008 |
| Geographic note | North Bengal foothills; Jalpaiguri district terai zone; NH-17 corridor; former tea-belt fringe transitioning to market-town economy | A | — |
| Sub-units used in v0 | **U1: Dhupguri_Municipality** (urban) · **U2: Dhupguri_CDB_rural** (CD Block GP share) | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~230,000 (Dhupguri Muni ~45,000 + CD Block rural share ~185,000) | E | Census 2011 Jalpaiguri district; Dhupguri block Primary Census Abstract |
| 2019 projected population | ~250,000 | E | 8-yr compound religion-differential growth (~1.0%/yr Hindu, ~1.3%/yr Muslim) |
| Sex ratio (2019, F per 1000 M) | ~950 | E | Jalpaiguri district 2011 sex ratio 954; minimal projection drift |
| 2019 estimated electorate (18+) | ~251,681 | A | 2019_AssemblySegmentLevelVotingData.csv (TOTAL ELECTORS) |
| Estimated M / F / TG split (2019) | 51.3% M / 48.7% F / <0.05% TG | E | Jalpaiguri district 2011 sex ratio back-projection |
| 2019 polling stations (estimated) | ~280 | E | Proportional from electorate size; 2021 SIR back-projection |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 72.00 | E | Jalpaiguri district 2011 Census: Hindu 72.6%; Dhupguri block ~72%; projected stable; Muslim growth +0.3pp over 8yr |
| Muslim | 23.50 | E | Jalpaiguri district 2011: ~23%; Dhupguri block slightly higher; projected +0.3pp over 8yr |
| Christian | 1.50 | E | Jalpaiguri district 2011: ~1.5%; tea-garden and mission-school population |
| Sarna_ORP | 2.50 | E | Rajbanshi tribal and Santal Adivasi population in CD block rural areas |
| Other_residual | 0.50 | E | Sikh + Jain + Buddhist + Not_stated; small trader fringe |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 30.00 | E | Jalpaiguri district SC share ~28%; Dhupguri block slightly higher; Census 2011 |
| └ Rajbanshi_SC | 22.00 | C | Rajbanshi (Koch-Rajbanshi) dominant SC in Jalpaiguri; ~73% of SC pool |
| └ Namasudra_SC | 3.00 | E | Smaller settlement; partition-era migrants |
| └ Other_SC | 5.00 | E | Bagdi, Hari, Mochi and other SC residual |
| **ST_total** | 8.00 | E | Jalpaiguri district ST ~12%; Dhupguri block lower due to municipal area; ~8% |
| └ Santal_ST | 4.00 | E | Dominant ST; Adivasi tea-garden worker families |
| └ Oraon_ST | 2.50 | E | Second largest ST; tea-belt presence |
| └ Other_ST | 1.50 | E | Munda, Garo, Bodo, Toto residual |
| UC_bhadralok | 5.00 | E | Brahmin/Kayastha/Baidya; small professional class in Dhupguri Muni |
| OBC | 8.00 | E | Mahishya, Kurmi, Teli, Rajbangshi OBC subgroup not in SC list |
| Other_Hindu_middle | 21.00 | E | Residual within Hindu (72% − 30 SC − 8 ST − 5 UC − 8 OBC) = 21% |
| Muslim | 23.50 | E | See C.1; Bengali-Sheikh predominant in Dhupguri block rural; Urdu-speaking fringe in town |
| Christian_plus_Sarna_plus_Other | 4.50 | E | See C.1; Christian 1.5% + Sarna 2.5% + Other 0.5% combined |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.00 | E | Renormalized from Census 2011 Jalpaiguri age pyramid (18+ adults only; 0–17 excluded) |
| 23_27 | 12.50 | E | High youth share in North Bengal terai |
| 28_32 | 12.00 | E | |
| 33_37 | 11.00 | E | |
| 38_42 | 10.00 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.00 | E | |
| 63_67 | 6.50 | E | |
| 68 | 6.00 | E | 68+ open-ended |
| **Sum** | **100.00** | — | self-check (renormalized from Census 2011 after excluding 0–17) |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.27 | E | Jalpaiguri district sex ratio 954 F per 1000 M → 51.27% M |
| Female | 48.72 | E | Computed residual |
| Third_gender | 0.01 | E | WB SIR pattern; negligible in rural-semi-urban AC |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 62.00 | E | Jalpaiguri district 2011: ~62% Bengali; Dhupguri town majority Bengali |
| Hindi | 4.00 | E | Bihari labour migrants; small Marwari trader community in Dhupguri town |
| Urdu | 2.00 | E | Muslim Bengali-Urdu bilingual fringe in town area |
| Other | 3.00 | E | Nepali, Sadri, English-medium Christian; residual catch-all |
| Rajbongshi | 16.00 | E | Rajbangshi / Koch-Rajbangshi mother tongue; dominant in SC-OBC rural population |
| Santali | 8.00 | E | Santal Adivasi tea-belt families |
| Sadri | 3.00 | E | Oraon/other Adivasi lingua franca in tea gardens |
| Nepali | 2.00 | E | Small Gorkha/Nepali origin settled community in terai |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 22.00 | E | Jalpaiguri district literacy 73.8% (2011); Dhupguri block slightly lower; ~26% illiterate 2011; trend to ~22% by 2019 |
| Primary | 24.00 | E | Census 2011 Jalpaiguri education distribution scaled |
| Middle | 20.00 | E | |
| Secondary | 16.00 | E | |
| Higher_Secondary | 9.00 | E | |
| Graduate | 7.00 | E | Limited higher education in semi-urban AC |
| Postgraduate | 2.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 38.00 | E | Jalpaiguri district Census 2011 main-worker share ~38%; tea-garden and agriculture dominant |
| └ Main_worker_tea_garden | 8.00 | E | Sub-row; tea-garden patta workers in CD block rural (is_subgroup=yes) |
| └ Main_worker_non_tea | 30.00 | E | Sub-row; agriculture + services (is_subgroup=yes) |
| Marginal_worker | 14.00 | E | High marginal-worker share typical in North Bengal terai |
| Non_worker | 32.00 | E | Housewife + elderly + retired |
| Student | 10.00 | E | 18–22 in education; local college presence |
| Unemployed | 6.00 | E | Educated job-seekers; limited local white-collar absorption |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 22.00 | E | Jalpaiguri block 2011: ~25% cultivators; Muni dilution → ~22% AC weighted |
| Agricultural_labourer | 28.00 | E | High agricultural-labourer share in rural terai; includes tea-garden wage workers |
| Household_industry | 5.00 | E | Weaving, bamboo craft, traditional industry |
| Manufacturing | 4.00 | E | Rice mills, small processing; limited organised |
| Construction | 6.00 | E | Seasonal labour; NH-17 corridor construction |
| Trade_retail | 10.00 | E | Dhupguri town market hub; retail traders |
| Transport_logistics | 5.00 | E | NH-17 transport economy; auto-rickshaw, truck |
| Services | 8.00 | E | Private services in town area |
| Government_services_teachers | 5.00 | E | State govt, school teachers; stable employment class |
| Out_migrant_worker | 7.00 | D | North Bengal seasonal migrants to Kerala/Andhra for construction; also tea-estate closures push out-migration |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.00 | E | Census B-04 WB pattern |
| Employee | 36.00 | E | Tea-garden patta workers + govt employees + organised retail |
| Single_worker | 42.00 | E | Own-account cultivators + petty traders + artisans |
| Family_worker | 20.00 | E | Unpaid family help in agriculture and household industry |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 30.00 | C | Jalpaiguri district BPL ~32% (Census 2001 baseline); WB poverty fell ~6pp 2011–19 → ~30% by 2019; tea-belt poverty elevated |
| Above_Poverty_Line_low_income | 35.00 | E | |
| Lower_middle | 22.00 | E | Market-town and service-class households |
| Middle | 10.00 | E | Government employees, small traders |
| Upper_middle_well_off | 3.00 | E | Dhupguri Muni affluent fringe; rice-mill owners |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Dhupguri_Municipality | 20.00 | E | Dhupguri Paurashava ~45,000 / 230,000 AC total ≈ 20%; Census 2011 Jalpaiguri district municipality |
| U2_Dhupguri_CDB_rural | 80.00 | E | Remainder; Dhupguri CD Block GP share collapsed to single rural sub-unit in v0 |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | WB 2011: 4.3; North Bengal slightly higher; projection |
| Nuclear_HH | 65.00 | E | NFHS-4 WB rural pattern; slightly lower joint family in North Bengal terai |
| Joint_HH | 28.00 | E | Higher joint family in Rajbanshi and Muslim communities |
| Extended_multi_generation | 7.00 | E | Multi-generation households in rural areas |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.00 | E | Census 2011 Jalpaiguri pattern; first-time-voter and young cohort |
| Currently_married | 65.00 | E | High rural marriage rate; early marriage in Adivasi and Muslim communities |
| Widowed | 8.00 | E | Concentrated in 60+; female-skewed; tea-garden mortality slightly elevated |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 62.00 | C | NFHS-4 WB rural 60%, urban 89%; North Bengal rural-dominated AC ~62% by 2019 |
| Radio | 8.00 | C | Slightly higher than south WB; North Bengal radio listenership |
| Mobile_phone | 80.00 | C | NFHS-4 WB ~78%; Jio rollout 2016–19; ~80% by 2019 |
| Smartphone_with_internet | 35.00 | C | NFHS-4 baseline + Jio rollout; rural North Bengal lagging south WB |
| Computer | 5.00 | C | Low; semi-urban AC; mainly govt office and college |
| Two_wheeler | 25.00 | C | NFHS-4 WB rural 18%; market-town effect → ~25% |
| Four_wheeler | 4.00 | C | Limited; rice-mill owners and traders |
| Banking_access | 82.00 | B | PMJDY 2014-19 saturation; NFHS-4 WB baseline |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 80.00 | C | NFHS-4 WB rural 84%; North Bengal slightly lower ground-water quality issues → ~80% |
| Improved_sanitation | 55.00 | C | NFHS-4 WB rural 51%; +Swachh Bharat 2014–19 (+8pp rural in lower-income ACs) |
| LPG_clean_cooking_fuel | 30.00 | C | NFHS-4 WB rural 24%; +Ujjwala 2016–19 (+8pp); North Bengal rural lower than south |
| Wood_biomass_fuel | 64.00 | C | High wood-fuel dependency in North Bengal rural; forest proximity |
| Other_fuel | 6.00 | C | Kerosene, dung-cake; residual |
| Electricity | 88.00 | C | Census 2011 + Saubhagya 2017–19 rollout; North Bengal slightly behind south WB |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 72.00 | D | Estimate from Jalpaiguri district Census D-series pattern; long-settled Rajbanshi and Adivasi communities |
| WB_other_district | 6.00 | D | Some Kolkata and South WB service-class in Dhupguri town |
| Other_Indian_state | 4.00 | E | Bihari and UP labour migrants; small Marwari trader community |
| Bangladesh_origin | 10.00 | D | Hindu Bengali refugees (partition-era and post-1971) in rural GPs; lower concentration than in border districts |
| Outside_India | 0.50 | E | Negligible |
| Out_migrant | 3.50 | E | Seasonal workers registered here but working outside; tea-estate displacement |
| Nepal_Bhutan_origin | 4.00 | E | Small Nepali-origin settled community; Bhutanese refugee residual in North Bengal |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Santali | Sadri | Nepali | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 55.00 | 4.00 | 0.00 | 1.00 | 22.00 | 11.00 | 4.00 | 3.00 | E | Jalpaiguri district 2011 language composition; Rajbanshi dominant SC/OBC; Santali in ST |
| Muslim | 86.00 | 2.00 | 8.00 | 2.00 | 2.00 | 0.00 | 0.00 | 0.00 | E | Bengali-Sheikh predominant; Urdu fringe in Dhupguri town |
| Christian | 40.00 | 0.00 | 0.00 | 5.00 | 10.00 | 25.00 | 15.00 | 5.00 | E | Tea-garden mission-school population; mixed Adivasi tongues |
| Sarna_ORP | 20.00 | 0.00 | 0.00 | 2.00 | 15.00 | 40.00 | 18.00 | 5.00 | E | Santal+Oraon+Munda tribal languages; Rajbanshi crossover |
| Other_residual | 40.00 | 30.00 | 5.00 | 25.00 | 0.00 | 0.00 | 0.00 | 0.00 | E | Sikh/Marwari/Nepali fringe |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 38.89 | 8.33 | 6.94 | 11.11 | 34.72 | 0 | 0 | E | SC 28/72 + ST 6/72 + UC 5/72 + OBC 8/72 + residual; each leaf/Hindu share |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 88 | 0 | 5 | 7 | 0 | 0 | E | Tribal sub-castes mostly route to ST_total; some Rajbanshi OBC crossover |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 67.00 | 5.00 | 4.00 | 14.00 | 0.50 | 4.00 | D | Hindu refugee pool smaller here than in N24P; Rajbanshi-dominated; Bangladesh-origin ~14% of Hindu |
| Muslim | 87.00 | 5.00 | 2.00 | 3.00 | 0.50 | 2.50 | D | Mostly long-settled Bengali-Sheikh peasantry; small Bangladesh-origin trickle |
| Christian | 80.00 | 8.00 | 5.00 | 2.00 | 2.00 | 3.00 | E | Tea-garden settled; mixed origin |
| Sarna_ORP | 85.00 | 5.00 | 5.00 | 0.00 | 0.00 | 5.00 | E | Indigenous Adivasi; seasonal out-migration to tea gardens |
| Other_residual | 30.00 | 15.00 | 50.00 | 0.00 | 5.00 | 0.00 | E | Marwari/Nepali traders mostly from other states |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 65.00 | 38.00 | 85.00 | C | NFHS-4 WB religion gap; Hindu slightly above Muslim |
| Muslim | 55.00 | 28.00 | 72.00 | C | NFHS-4 WB Muslim-Hindu gap; rural Muslim lower banking access |
| Christian | 70.00 | 40.00 | 88.00 | C | Tea-estate Christian; slightly better amenities |
| Sarna_ORP | 42.00 | 18.00 | 65.00 | E | Tea-garden Adivasi; lower asset ownership |
| Other_residual | 82.00 | 60.00 | 95.00 | E | Trader community; higher assets |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 5.00 | 12.00 | 15.00 | 20.00 | 18.00 | 22.00 | 8.00 | E |
| SC_total | 25.00 | 26.00 | 22.00 | 15.00 | 7.00 | 4.00 | 1.00 | E |
| ST_total | 35.00 | 28.00 | 18.00 | 12.00 | 5.00 | 2.00 | 0.00 | E |
| OBC | 18.00 | 24.00 | 22.00 | 18.00 | 10.00 | 7.00 | 1.00 | E |
| Other_Hindu_middle | 20.00 | 24.00 | 22.00 | 17.00 | 9.00 | 7.00 | 1.00 | E |
| Muslim | 28.00 | 26.00 | 22.00 | 14.00 | 6.00 | 3.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 12.00 | 10.00 | E |
| 23_27 | 14.00 | 11.00 | E |
| 28_32 | 12.00 | 8.00 | E |
| 33_37 | 10.00 | 6.00 | E |
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
| 18_22 | 8.00 | 30.00 | E |
| 23_27 | 42.00 | 80.00 | E |
| 28_32 | 82.00 | 92.00 | E |
| 33_37 | 91.00 | 90.00 | E |
| 38_42 | 92.00 | 88.00 | E |
| 43_47 | 91.00 | 82.00 | E |
| 48_52 | 90.00 | 74.00 | E |
| 53_57 | 88.00 | 62.00 | E |
| 58_62 | 85.00 | 50.00 | E |
| 63_67 | 80.00 | 38.00 | E |
| 68 | 70.00 | 25.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 25.00 | 55.00 | C | Rural North Bengal cultivator; lower than south WB |
| Agricultural_labourer | 18.00 | 45.00 | C | Tea-belt wage labour; lowest income |
| Household_industry | 30.00 | 60.00 | C | |
| Manufacturing | 45.00 | 72.00 | C | |
| Construction | 40.00 | 65.00 | C | |
| Trade_retail | 60.00 | 82.00 | C | Dhupguri town traders |
| Transport_logistics | 55.00 | 78.00 | C | NH-17 corridor |
| Services | 65.00 | 85.00 | C | |
| Government_services_teachers | 80.00 | 92.00 | C | Highest |
| Out_migrant_worker | 62.00 | 72.00 | D | Working outside; smartphone-heavy for remittance |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 38.00 | 1.00 | E |
| Primary | 40.00 | 3.00 | E |
| Middle | 38.00 | 5.00 | E |
| Secondary | 32.00 | 10.00 | E |
| Higher_Secondary | 26.00 | 16.00 | E |
| Graduate | 30.00 | 18.00 | E |
| Postgraduate | 38.00 | 12.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 015. North Bengal Rajbongshi-Bengali bilingualism is noted in C.5 narrative but not modelled as a separate axis in v0.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Dhupguri_Municipality | 74.00 | 22.00 | 1.50 | 1.00 | 1.50 | E | Dhupguri town: Hindu majority; moderate Muslim; small Christian and Sarna; Jalpaiguri Census 2011 urban pattern |
| U2_Dhupguri_CDB_rural | 71.50 | 23.88 | 1.50 | 2.88 | 0.25 | E | Rural CD block: higher Sarna share; slightly higher Muslim; marginal recovery check: 0.2×74 + 0.8×71.5 = 14.8 + 57.2 = 72.0 ✓ |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit).

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Dhupguri_Municipality | 8.00 | 25.00 | 3.00 | 10.00 | 28.00 | 22.00 | 4.00 | E |
| U2_Dhupguri_CDB_rural | 4.25 | 31.25 | 9.25 | 7.50 | 19.75 | 23.75 | 4.25 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Dhupguri_Municipality | 80.00 | 52.00 | 14.00 | 92.00 | C |
| U2_Dhupguri_CDB_rural | 57.50 | 30.00 | 2.50 | 78.75 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Dhupguri_Municipality | 60.00 | 78.00 | 92.00 | 98.00 | C |
| U2_Dhupguri_CDB_rural | 22.50 | 47.50 | 77.50 | 85.00 | C |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 WB rollup calibrated to AC 015 vote anchors.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 60.00 | 30.00 | 1.00 | 6.50 | 2.50 | C | CSDS-Lokniti 2019 WB; North Bengal Hindu lean to BJP stronger than state average; Rajbanshi BJP alignment |
| Muslim | 5.00 | 78.00 | 8.00 | 6.00 | 3.00 | C | Strong AITC Muslim consolidation; INC residual; LF decline |
| Christian | 28.00 | 48.00 | 8.00 | 12.00 | 4.00 | E | Tea-estate Christian; mixed lean |
| Sarna_ORP | 45.00 | 32.00 | 3.00 | 15.00 | 5.00 | E | Adivasi: BJP gaining but LF legacy; CPIM had Adivasi base |
| Other_residual | 50.00 | 28.00 | 5.00 | 10.00 | 7.00 | E | Small trader and Nepali community |

### D.16 Vote × Caste (2019 LS)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 58.00 | 28.00 | 4.00 | 7.00 | 3.00 | C | Bhadralok BJP-leaning by 2019; CSDS WB 2019 |
| OBC | 48.00 | 35.00 | 3.00 | 10.00 | 4.00 | C | Rajbanshi OBC: BJP gaining in Jalpaiguri |
| SC_total | 55.00 | 32.00 | 2.00 | 8.00 | 3.00 | C | Rajbanshi SC: strong BJP alignment; North Bengal pattern |
| ST_total | 40.00 | 32.00 | 3.00 | 18.00 | 7.00 | C | Adivasi/ST: BJP gaining but LF legacy stronger |
| Other_Hindu_middle | 52.00 | 32.00 | 2.00 | 10.00 | 4.00 | E | Middle-caste rural Hindu |
| Muslim | 5.00 | 78.00 | 8.00 | 6.00 | 3.00 | C | Muslim: near-uniform AITC |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for AC 015 in v0. Welfare-scheme penetration in North Bengal terai follows state rural pattern; document in §F / §H narrative if needed.)

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 52.00 | 37.00 | 2.00 | 7.00 | 2.00 | C | CSDS-Lokniti 2019 WB gender cross-tab |
| Female | 46.00 | 44.00 | 1.00 | 6.00 | 3.00 | C | Female TMC advantage; North Bengal BJP slightly lower than state average for women |

---

## E. 2019 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.** Source: ECI 2019_AssemblySegmentLevelVotingData.csv, AC NO = 15.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 49.15 | A | ECI GE2019 Form-20 via 2019_AssemblySegmentLevelVotingData.csv; 105,729 votes |
| AITC | 40.89 | A | 87,963 votes |
| INC | 1.42 | A | 3,065 votes |
| LF | 6.22 | A | CPIM 13,016 + SUCI(C) 358 = 13,374 votes |
| Other_NOTA | 2.32 | A | BSP 1,127 + AMB 296 + SWJP 276 + KPPU 378 + IND 2,904 = 4,981 votes |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 015 (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Mithileswar Burman | AITC | ~47 | CPI(M) candidate | CPI(M) | ~38 | ~12,000 est. |
| 2016 AE | Mithileswar Burman | AITC | ~46 | BJP candidate | BJP | ~34 | ~14,000 est. |

Note: AC 015 Dhupguri was an AITC stronghold in 2011 and 2016 AEs. BJP made significant inroads in North Bengal in the 2016–2019 period, converting Dhupguri to a BJP-plurality seat at the 2019 LS.

### LS 03 Jalpaiguri historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Bijoya Chakrabarti | BJP | ~35 | BJP won Jalpaiguri LS; AITC 2nd; North Bengal BJP early mover |
| 2019 LS | Jayanta Kumar Roy | BJP | ~49 | Strong BJP consolidation in Jalpaiguri LS; AITC 2nd; CPIM collapse |

Jalpaiguri LS (PC 03) has been a BJP-held seat since 2014. The 2019 LS saw BJP consolidate its lead with a ~9pp margin over AITC. Dhupguri AC segment (within Jalpaiguri LS) followed the district trend with BJP plurality at 49.15% vs AITC 40.89%.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Election Commission of India — `2019_AssemblySegmentLevelVotingData.csv` (AC 015 segment, GE2019)
- Delimitation Commission of India 2008 — WB Schedule (Jalpaiguri LS = PC 03; Dhupguri = AC 015)
- Census of India 2011 — Jalpaiguri district Primary Census Abstract

### Secondary sources (tier B / C)

- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2019 NES — vote × demographic conditionals (WB regional rollup)
- WB District Statistical Handbook — Jalpaiguri
- Swarajya/CSDS 2019 WB summary — vote × religion / caste / gender cross-tabs

### Tertiary / journalistic (tier D)

- Wikipedia "Dhupguri" and "Jalpaiguri district" — constituency composition, CD block structure
- Wikipedia "Jalpaiguri (Lok Sabha constituency)" — LS segment composition
- North Bengal newspaper reports on 2019 LS results and BJP consolidation in Jalpaiguri
- General journalistic record of Rajbanshi community BJP alignment in North Bengal

### Tier-D / E reliance flags (what to distrust)

- **Religion breakdown** (C.1, D.11) — Jalpaiguri district Census 2011 used as proxy; no AC-level religion Census table obtained; tier E
- **Caste sub-group shares** (C.2, D.2) — no post-1931 caste census for non-SC/ST; Rajbanshi dominance from journalistic record; tier C/E
- **Migration/birthplace** (C.16, D.3) — no AC-level Census D-series; tier D from district pattern and journalistic anchor
- **GP-level data** (D.11–D.14) — collapsed to 2 sub-units (Muni + CDB rural); refine when DCHB Jalpaiguri Part-A accessible
- **Asset/media** (C.14, D.4, D.13) — NFHS-4 state-level pattern projected to AC; tier C
- **Vote × Demographic** (D.15–D.17) — CSDS 2019 WB regional rollup; locally adjusted for Rajbanshi alignment; tier C
- **Assembly election history** (F) — approximate percentages from journalistic record; margin estimates

### v0 known gaps (see methodology §7)

1. DCHB Jalpaiguri Part-A — sub-units collapsed to 2 (Muni + CDB rural) instead of full GP disaggregation
2. Census 2011 AC-level religion table — using district-level proxy; AC boundary may differ from block boundary
3. Census HH-13 GP-level — using NFHS state-level proxy for asset/media
4. Census D-series — using qualitative/journalistic anchor for migration
5. Full CSDS WB regional cross-tabs — using Swarajya summary; no Jalpaiguri-specific sub-sample
6. 2011 and 2016 AE results — precise vote shares and candidate names not verified from ECI archive; estimates from Wikipedia/journalistic sources

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs. The
> validator's leakage gate exempts §H from the no-future-leakage check.

### 2021 WB Assembly Election — AC 015 Dhupguri (tier D, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Bishnu Prasad Sharma | ~est. | ~45–47% est. | D — ECI 2021 AE; precise figures to be fetched |
| AITC | Nirmal Chandra Roy | ~est. | ~47–49% est. | D — ECI 2021 AE; AITC recovered in 2021 AE across North Bengal |
| Note | Precise 2021 AE results pending ECI archive fetch | — | — | Placeholder; update to tier A when fetched |

### 2024 Lok Sabha Election — AC 015 segment within Jalpaiguri LS (PC 03) (tier A)

Source: `data/2024_AssemblySegmentLevelVotingData.csv`, AC NO = 15. Electorate: 269,522. Total valid votes: 223,799. Turnout: ~83.0%.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Dr Jayanta Kumar Roy | 106,651 | 47.65% | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Nirmal Chandra Roy | 100,322 | 44.83% | A | Same |
| LF (CPIM + SUCI) | Debraj Barman + SUCI | 10,043 | 4.49% | A | CPIM 9,733 + SUCI 310 |
| INC | (no INC candidate) | 0 | 0.00% | A | No INC entry in 2024 |
| Other_NOTA | BSP + KPPU + MPOI + IND×5 + NOTA | 6,783 | 3.03% | A | Computed residual |
| **BJP margin over AITC** | — | 6,329 votes | 2.82pp | A | Computed |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC-015 segment shares within ±3pp of the tier-A figures:

- BJP target: 47.65% ± 3pp
- AITC target: 44.83% ± 3pp
- LF target: 4.49% ± 3pp
- Other_NOTA target: 3.03% ± 3pp
