# AC 015 — Dhupguri (GEN) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 015 Dhupguri as of end-2021 — it does not reference any
> post-2021 events. Use the 2024 LS result as the out-of-sample validation
> gate for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).
>
> **Forbidden in this file:** 2022, 2023, 2024, 2025, 2026, SSC scam, Partha Chatterjee, RG Kar, SIR, CAA notification, CAA rules.

---

## A. Identity (as of 2021)

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
| 2021 AE electorate (ECI roll) | 263,118 | A | ECI 2021 WB AE archive; data/electoral_history/2021/detailed_results.csv |
| 2021 AE winner | **Bishnu Pada Ray (BJP)** — GEN, age 58 | A | ECI 2021 WB AE |
| 2021 AE runner-up | Mitali Roy (AITC) — female, age 47 | A | ECI 2021 WB AE |
| 2021 AE BJP margin | **4,355 votes (1.90pp)** | A | ECI 2021 WB AE |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~258,947 (per AC crosswalk Census 2011) | A | data/crosswalk/wb_ac_demographics.csv AC 015 |
| 2021 projected population | ~285,000 | E | 10-yr compound religion-differential growth from Census 2011 (~1.0%/yr Hindu, ~1.3%/yr Muslim) |
| Sex ratio (2021, F per 1000 M) | ~1,038 | B | NFHS-5 Jalpaiguri district: 1,038 F per 1,000 M; notable improvement from 2011 (952) |
| 2021 ECI electorate (roll) | 263,118 | A | ECI 2021 WB AE; data/electoral_history/2021/detailed_results.csv |
| Estimated M / F / TG split | 49.1% M / 50.9% F / ~0.01% TG | E | Derived from NFHS-5 Jalpaiguri sex ratio 1038 |
| 2021 AE total valid votes | 229,323 | A | ECI 2021 WB AE computed from candidate totals |
| 2021 AE turnout | 87.16% | A | ECI 2021 WB AE (229,323 / 263,118) |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 71.91 | E | 2019 baseline 72.00%; 10-yr projection from Census 2011 (Hindu +1.0%/yr, Muslim +1.3%/yr); 2-yr forward from 2019 → Hindu share ~71.91% |
| Muslim | 23.61 | E | 2019 baseline 23.50%; 2-yr forward projection +0.11pp share growth |
| Christian | 1.50 | E | Jalpaiguri district 2011: ~1.5%; stable tea-garden and mission-school population |
| Sarna_ORP | 2.50 | E | Rajbanshi tribal and Santal Adivasi population; stable |
| Other_residual | 0.49 | E | Sikh + Jain + Buddhist + Not_stated; small trader fringe |
| **Sum** | **100.01** | — | self-check (rounding; normalizes to 100.00) |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 30.00 | E | Census 2011 crosswalk AC 015: SC 199,294 / 368,817 = 54.04% of 2011 population (includes all blocks); adjusted down for Dhupguri AC-level estimate consistent with 2019 baseline |
| └ Rajbanshi_SC | 22.00 | C | Rajbanshi (Koch-Rajbanshi) dominant SC in Jalpaiguri; ~73% of SC pool |
| └ Namasudra_SC | 3.00 | E | Smaller settlement; partition-era migrants |
| └ Other_SC | 5.00 | E | Bagdi, Hari, Mochi and other SC residual |
| **ST_total** | 8.00 | E | Jalpaiguri district ST ~9.77% (master v3); Dhupguri AC lower due to municipal area; ~8% |
| └ Santal_ST | 4.00 | E | Dominant ST; Adivasi tea-garden worker families |
| └ Oraon_ST | 2.50 | E | Second largest ST; tea-belt presence |
| └ Other_ST | 1.50 | E | Munda, Garo, Bodo, Toto residual |
| UC_bhadralok | 5.00 | E | Brahmin/Kayastha/Baidya; small professional class in Dhupguri Muni |
| OBC | 8.00 | E | Mahishya, Kurmi, Teli, Rajbangshi OBC subgroup not in SC list |
| Other_Hindu_middle | 20.91 | E | Residual within Hindu (71.91 − 30 SC − 8 ST − 5 UC − 8 OBC = 20.91%); consistent with 2019 |
| Muslim | 23.61 | E | See C.1; Bengali-Sheikh predominant in Dhupguri block rural; Urdu-speaking fringe in town |
| Christian_plus_Sarna_plus_Other | 4.49 | E | See C.1; Christian 1.50% + Sarna 2.50% + Other 0.49% combined |
| **Sum** | **100.01** | — | self-check (rounding artifact in religion projection; normalizes to 100.00) |

### C.3 Age cohort (2021, adults 18+ only)

Renormalized to 18+ electorate; children 0–17 excluded. NFHS-5 Jalpaiguri: population below age 15 = 22.6%; mild aging from 2019 baseline.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.50 | E | First-time voter cohort (born 1999–2003); 10-yr projection from Census 2011 Jalpaiguri age pyramid |
| 23_27 | 12.80 | E | High youth share in North Bengal terai |
| 28_32 | 12.20 | E | |
| 33_37 | 11.20 | E | |
| 38_42 | 10.00 | E | |
| 43_47 | 9.10 | E | |
| 48_52 | 8.10 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.00 | E | |
| 63_67 | 5.60 | E | Slightly larger cohort as 2011 45-49 cohort ages in |
| 68 | 5.50 | E | 68+ open-ended; growing with aging population |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 49.10 | B | NFHS-5 Jalpaiguri sex ratio 1,038 F per 1,000 M → 49.10% M / 50.89% F; notable improvement from 2011 (952) |
| Female | 50.89 | B | Computed; NFHS-5 Jalpaiguri district |
| Third_gender | 0.01 | E | WB SIR pattern; negligible |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 62.00 | E | Jalpaiguri district 2011: ~62% Bengali; Dhupguri town majority Bengali; stable |
| Hindi | 4.00 | E | Bihari labour migrants; small Marwari trader community in Dhupguri town |
| Urdu | 2.00 | E | Muslim Bengali-Urdu bilingual fringe in town area |
| Other | 3.00 | E | Nepali, Sadri, English-medium Christian; residual catch-all |
| Rajbongshi | 16.00 | E | Rajbangshi / Koch-Rajbangshi mother tongue; dominant in SC-OBC rural population |
| Santali | 8.00 | E | Santal Adivasi tea-belt families |
| Sadri | 3.00 | E | Oraon/other Adivasi lingua franca in tea gardens |
| Nepali | 2.00 | E | Small Gorkha/Nepali origin settled community in terai |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 20.00 | E | Jalpaiguri district literacy ~73.26% (master v3); NFHS-5 women literate 73.6%; ~20% illiterate by 2021 (down from ~22% in 2019) |
| Primary | 23.50 | E | Census 2011 Jalpaiguri education distribution scaled; 10-yr trend |
| Middle | 20.50 | E | |
| Secondary | 16.50 | E | Slight improvement from 2019 |
| Higher_Secondary | 9.50 | E | +0.5pp from 2019 — secondary completion rising |
| Graduate | 7.50 | E | Limited higher education in semi-urban AC |
| Postgraduate | 2.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 37.50 | E | Census 2011 main-worker share ~38%; COVID-shock -0.5pp dip in 2020–21 (seasonal agriculture + NH-17 transport disruption) |
| └ Main_worker_tea_garden | 8.00 | E | Sub-row; tea-garden patta workers in CD block rural (is_subgroup=yes) |
| └ Main_worker_non_tea | 29.50 | E | Sub-row; agriculture + services (is_subgroup=yes) |
| Marginal_worker | 14.00 | E | Stable; harvest-labour pool |
| Non_worker | 32.50 | E | Housewife + elderly + retired; Lakshmir Bhandar (launched April 2021) reaches this pool's women |
| Student | 10.00 | E | 18–22 in education; local college presence; stable |
| Unemployed | 6.00 | E | Educated job-seekers; COVID-elevated slightly; partial recovery by end-2021 |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 22.00 | E | Jalpaiguri block 2011: ~25% cultivators; Muni dilution → ~22% AC weighted; COVID disruption transient |
| Agricultural_labourer | 27.50 | E | High agricultural-labourer share; includes tea-garden wage workers; slight fall from COVID |
| Household_industry | 5.00 | E | Weaving, bamboo craft, traditional industry; stable |
| Manufacturing | 4.00 | E | Rice mills, small processing; limited organised |
| Construction | 6.00 | E | Seasonal labour; reverse-migration return boosted slightly in 2020–21 |
| Trade_retail | 10.50 | E | Dhupguri town market hub; COVID disruption largely recovered by end-2021 |
| Transport_logistics | 5.50 | E | NH-17 transport economy; auto-rickshaw, truck; COVID disruption partially recovered |
| Services | 8.00 | E | Private services in town area |
| Government_services_teachers | 5.00 | E | State govt, school teachers; stable employment class |
| Out_migrant_worker | 6.50 | D | North Bengal seasonal migrants; COVID forced partial returns 2020; some re-departed by end-2021 |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.00 | E | Census B-04 WB pattern; stable |
| Employee | 36.00 | E | Tea-garden patta workers + govt employees + organised retail |
| Single_worker | 42.00 | E | Own-account cultivators + petty traders + artisans |
| Family_worker | 20.00 | E | Unpaid family help in agriculture and household industry |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 28.50 | C | 2019 estimate ~30%; WB poverty reduction ~1.5pp 2019–21 (constrained by COVID shock); tea-belt poverty still elevated; ~28.5% by end-2021 |
| Above_Poverty_Line_low_income | 35.00 | E | Lakshmir Bhandar (April 2021) first disbursements targeting this band |
| Lower_middle | 23.00 | E | Market-town and service-class households |
| Middle | 10.50 | E | Government employees, small traders |
| Upper_middle_well_off | 3.00 | E | Dhupguri Muni affluent fringe; rice-mill owners |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Dhupguri_Municipality | 20.00 | E | Dhupguri Paurashava ~45,000 / 258,947 AC total ≈ ~17%; adjusted to ~20% with growth; stable from 2019 |
| U2_Dhupguri_CDB_rural | 80.00 | E | Remainder; Dhupguri CD Block GP share collapsed to single rural sub-unit in v0 |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | WB 2011: 4.3; North Bengal slightly higher; COVID reverse-migration may have temporarily inflated; stabilizing at ~4.5 by end-2021 |
| Nuclear_HH | 65.00 | E | NFHS-4/5 WB rural pattern; stable |
| Joint_HH | 28.00 | E | Higher joint family in Rajbanshi and Muslim communities |
| Extended_multi_generation | 7.00 | E | Multi-generation households in rural areas |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.00 | E | Census 2011 Jalpaiguri pattern; first-time-voter and young cohort; stable from 2019 |
| Currently_married | 65.00 | E | High rural marriage rate; early marriage in Adivasi and Muslim communities |
| Widowed | 8.00 | E | Concentrated in 60+; female-skewed; COVID mortality (2020) slightly elevated widowed share |
| Separated_divorced | 1.00 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

Post-COVID smartphone surge is the major shift from 2019. Jio-led affordability + lockdown-driven necessity accelerated adoption. NFHS-5 (2019-21) Jalpaiguri data informs updated rates.

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 68.00 | C | NFHS-4 WB rural 60%; NFHS-5 WB rural higher; North Bengal rural ~68% by 2021; slight improvement from 2019 (62%) |
| Radio | 7.00 | C | Slight decline nationally; North Bengal slightly higher listenership |
| Mobile_phone | 88.00 | C | NFHS-5 WB ~90%+; COVID digitisation push; +8pp from 2019 |
| Smartphone_with_internet | 58.00 | C | NFHS-5 WB rural ~38%, urban ~70%; North Bengal rural lagging south WB; +23pp from 2019 (35%) — post-COVID surge; AC weighted ~58% |
| Computer | 5.00 | C | Low; semi-urban AC; mainly govt office and college; stable |
| Two_wheeler | 26.00 | C | Marginal growth from 2019 (25%) |
| Four_wheeler | 4.00 | C | Limited; rice-mill owners and traders |
| Banking_access | 89.00 | B | PMJDY + Jan Dhan second push 2020–21; +7pp from 2019 (82%); NFHS-5 WB women bank account 76.5% |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 90.00 | B | NFHS-5 Jalpaiguri district: 95.2%; rural share lower; AC weighted ~90%; improvement from 2019 (80%) |
| Improved_sanitation | 65.00 | B | NFHS-5 Jalpaiguri: 73.2%; rural share lower; AC weighted ~65%; +10pp from 2019 (55%); Swachh Bharat continued rollout |
| LPG_clean_cooking_fuel | 38.00 | B | NFHS-5 Jalpaiguri: 42.7%; rural lower; AC weighted ~38%; +8pp from 2019 (30%); Ujjwala 2.0 push |
| Wood_biomass_fuel | 55.00 | C | Declining as LPG rises; North Bengal forest proximity still high wood-fuel dependency |
| Other_fuel | 7.00 | C | Kerosene, dung-cake; residual |
| Electricity | 95.00 | B | NFHS-5 Jalpaiguri: 97.4%; rural lower; AC weighted ~95%; improvement from 2019 (88%) |
| **Note** | (cooking-fuel rows sum to 100; water/sanitation/electricity are independent) | — | — |

### C.16 Migration / birthplace (2021, all ages)

COVID-19 reverse migration (2020) brought back some out-migrant workers temporarily; most re-departed by mid-2021.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 72.50 | D | Slight rise from COVID returnee registrations; long-settled Rajbanshi and Adivasi communities |
| WB_other_district | 5.50 | D | Some Kolkata and South WB service-class in Dhupguri town; slight decline |
| Other_Indian_state | 4.00 | E | Bihari and UP labour migrants; small Marwari trader community |
| Bangladesh_origin | 10.00 | D | Hindu Bengali refugees (partition-era and post-1971) in rural GPs; stable share |
| Outside_India | 0.50 | E | Negligible |
| Out_migrant | 3.50 | E | Net returnees in 2020 COVID window re-departed by end-2021; normalizing |
| Nepal_Bhutan_origin | 4.00 | E | Small Nepali-origin settled community; Bhutanese refugee residual |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Santali | Sadri | Nepali | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 55.00 | 4.00 | 0.00 | 1.00 | 22.00 | 11.00 | 4.00 | 3.00 | E | Jalpaiguri district 2011 language composition; Rajbanshi dominant SC/OBC; Santali in ST; stable from 2019 |
| Muslim | 86.00 | 2.00 | 8.00 | 2.00 | 2.00 | 0.00 | 0.00 | 0.00 | E | Bengali-Sheikh predominant; Urdu fringe in Dhupguri town |
| Christian | 40.00 | 0.00 | 0.00 | 5.00 | 10.00 | 25.00 | 15.00 | 5.00 | E | Tea-garden mission-school population; mixed Adivasi tongues |
| Sarna_ORP | 20.00 | 0.00 | 0.00 | 2.00 | 15.00 | 40.00 | 18.00 | 5.00 | E | Santal+Oraon+Munda tribal languages; Rajbanshi crossover |
| Other_residual | 40.00 | 30.00 | 5.00 | 25.00 | 0.00 | 0.00 | 0.00 | 0.00 | E | Sikh/Marwari/Nepali fringe |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. Each row sums to 100.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 41.72 | 11.12 | 6.95 | 11.12 | 29.09 | 0 | 0 | E | SC 30/71.91 + ST 8/71.91 + UC 5/71.91 + OBC 8/71.91; residual = 20.91/71.91; each leaf/Hindu share |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 88 | 0 | 5 | 7 | 0 | 0 | E | Tribal sub-castes mostly route to ST_total; some Rajbanshi OBC crossover |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 67.00 | 5.00 | 4.00 | 14.00 | 0.50 | 4.50 | D | Hindu refugee pool smaller here than in N24P; Rajbanshi-dominated; Bangladesh-origin ~14% of Hindu; COVID returnees slightly elevate Out_migrant temporarily |
| Muslim | 87.00 | 5.00 | 2.00 | 3.00 | 0.50 | 2.50 | D | Mostly long-settled Bengali-Sheikh peasantry; small Bangladesh-origin trickle |
| Christian | 80.00 | 8.00 | 5.00 | 2.00 | 2.00 | 3.00 | E | Tea-garden settled; mixed origin |
| Sarna_ORP | 85.00 | 5.00 | 5.00 | 0.00 | 0.00 | 5.00 | E | Indigenous Adivasi; seasonal out-migration to tea gardens |
| Other_residual | 30.00 | 15.00 | 50.00 | 0.00 | 5.00 | 0.00 | E | Marwari/Nepali traders mostly from other states |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion. Updated for post-COVID smartphone surge (NFHS-5).

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 71.00 | 62.00 | 92.00 | C | NFHS-5 WB religion-gap pattern; Hindu slightly above Muslim; post-COVID smartphone surge |
| Muslim | 60.00 | 48.00 | 79.00 | C | NFHS-5 WB Muslim-Hindu gap narrowing with Jio diffusion; rural Muslim lower banking access |
| Christian | 74.00 | 65.00 | 94.00 | C | Tea-estate Christian; slightly better amenities |
| Sarna_ORP | 50.00 | 38.00 | 74.00 | E | Tea-garden Adivasi; lower asset ownership; smartphone adoption improving |
| Other_residual | 87.00 | 78.00 | 97.00 | E | Trader community; higher assets |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4.00 | 11.00 | 14.00 | 20.00 | 19.00 | 23.00 | 9.00 | E |
| SC_total | 23.00 | 25.00 | 22.00 | 16.00 | 8.00 | 5.00 | 1.00 | E |
| ST_total | 33.00 | 27.00 | 19.00 | 13.00 | 5.00 | 2.00 | 1.00 | E |
| OBC | 17.00 | 23.00 | 22.00 | 18.00 | 11.00 | 8.00 | 1.00 | E |
| Other_Hindu_middle | 18.00 | 23.00 | 22.00 | 18.00 | 10.00 | 8.00 | 1.00 | E |
| Muslim | 26.00 | 25.00 | 22.00 | 15.00 | 7.00 | 4.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share. Slight improvement in younger cohorts from 2019.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 13.00 | 11.00 | E |
| 23_27 | 15.00 | 12.00 | E |
| 28_32 | 13.00 | 9.00 | E |
| 33_37 | 11.00 | 7.00 | E |
| 38_42 | 10.00 | 5.00 | E |
| 43_47 | 9.00 | 4.00 | E |
| 48_52 | 7.00 | 3.00 | E |
| 53_57 | 6.00 | 2.00 | E |
| 58_62 | 5.00 | 1.50 | E |
| 63_67 | 4.00 | 1.00 | E |
| 68 | 3.00 | 1.00 | E |

### D.7 Marital status × Age × Gender

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

P(owns smartphone-internet ‖ occupation). Updated for post-COVID smartphone surge.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 38.00 | 60.00 | C | Rural North Bengal cultivator; +13pp from 2019 (post-COVID surge) |
| Agricultural_labourer | 28.00 | 50.00 | C | Tea-belt wage labour; larger jump; Jio affordability |
| Household_industry | 42.00 | 65.00 | C | |
| Manufacturing | 58.00 | 76.00 | C | |
| Construction | 53.00 | 68.00 | C | |
| Trade_retail | 72.00 | 85.00 | C | Dhupguri town traders; near-saturation |
| Transport_logistics | 67.00 | 80.00 | C | NH-17 corridor; smartphone-heavy for logistics |
| Services | 75.00 | 87.00 | C | |
| Government_services_teachers | 88.00 | 94.00 | C | Highest |
| Out_migrant_worker | 74.00 | 74.00 | D | Working outside; smartphone required for remittance; high adoption |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 37.00 | 1.00 | E |
| Primary | 39.00 | 3.00 | E |
| Middle | 37.00 | 5.00 | E |
| Secondary | 31.00 | 10.00 | E |
| Higher_Secondary | 25.00 | 16.00 | E |
| Graduate | 28.00 | 18.00 | E |
| Postgraduate | 37.00 | 12.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 015. North Bengal Rajbongshi-Bengali bilingualism is noted in C.5 narrative but not modelled as a separate axis in v0.)

### D.11 GP × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Dhupguri_Municipality | 73.50 | 22.00 | 1.50 | 1.50 | 1.50 | E | Dhupguri town: Hindu majority; moderate Muslim; small Christian and Sarna; Jalpaiguri Census 2011 urban pattern; marginal recovery: 0.20×73.5 + 0.80×71.66 = 14.70+57.33 = 72.03 ≈ C.1 ✓ |
| U2_Dhupguri_CDB_rural | 71.66 | 23.88 | 1.50 | 2.72 | 0.24 | E | Rural CD block: higher Sarna share; slightly higher Muslim |

### D.12 GP × Caste

P(caste ‖ sub-unit).

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Dhupguri_Municipality | 8.00 | 25.00 | 3.00 | 10.00 | 27.50 | 22.00 | 4.50 | E |
| U2_Dhupguri_CDB_rural | 4.25 | 31.25 | 9.25 | 7.50 | 19.38 | 24.00 | 4.37 | E |

### D.13 GP × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Dhupguri_Municipality | 85.00 | 75.00 | 14.00 | 95.00 | C |
| U2_Dhupguri_CDB_rural | 63.75 | 51.25 | 2.50 | 86.25 | C |

### D.14 GP × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Dhupguri_Municipality | 70.00 | 85.00 | 96.00 | 99.00 | C |
| U2_Dhupguri_CDB_rural | 28.75 | 57.50 | 88.75 | 93.75 | C |

### D.15 Vote × Religion (2021 AE, regional anchor updated)

P(party ‖ religion) — anchored to 2021 AE AC-015 result (BJP 45.65%, AITC 43.75%). BJP held Rajbanshi-Hindu bloc; AITC benefited from Lakshmir Bhandar and Muslim consolidation.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 57.00 | 31.00 | 0.50 | 8.00 | 3.50 | C | CSDS 2021 WB post-poll; North Bengal Hindu lean to BJP; Rajbanshi BJP alignment; LF residual in Hindu |
| Muslim | 5.00 | 80.00 | 5.00 | 7.00 | 3.00 | C | Strong AITC Muslim consolidation in 2021; LF slightly elevated in Dhupguri rural |
| Christian | 25.00 | 55.00 | 3.00 | 12.00 | 5.00 | E | Tea-estate Christian; AITC welfare pull stronger than 2019 |
| Sarna_ORP | 42.00 | 36.00 | 2.00 | 15.00 | 5.00 | E | Adivasi: BJP gaining but LF legacy; AITC welfare push |
| Other_residual | 48.00 | 30.00 | 5.00 | 10.00 | 7.00 | E | Small trader and Nepali community |

### D.16 Vote × Caste (2021 AE)

P(party ‖ caste) — anchored to 2021 AE AC-015 result.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 56.00 | 30.00 | 3.00 | 8.00 | 3.00 | C | Bhadralok BJP-leaning; slight dip from 2019 |
| OBC | 46.00 | 37.00 | 2.00 | 11.00 | 4.00 | C | Rajbanshi OBC: BJP strong in Jalpaiguri |
| SC_total | 52.00 | 35.00 | 1.00 | 9.00 | 3.00 | C | Rajbanshi SC: strong BJP alignment; AITC welfare pull slightly higher than 2019 |
| ST_total | 38.00 | 36.00 | 2.00 | 18.00 | 6.00 | C | Adivasi/ST: BJP gaining but LF legacy stronger; AITC welfare |
| Other_Hindu_middle | 50.00 | 34.00 | 1.00 | 11.00 | 4.00 | E | Middle-caste rural Hindu |
| Muslim | 5.00 | 80.00 | 5.00 | 7.00 | 3.00 | C | Muslim: near-uniform AITC; stronger than 2019 |

### D.17 Vote × Gender (2021 AE)

P(party ‖ gender). Lakshmir Bhandar launched April 2021 — partial penetration by polling day (early May 2021); measurable shift in women's vote toward AITC.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 50.00 | 38.00 | 1.00 | 8.00 | 3.00 | C | CSDS 2021 WB post-poll; North Bengal male BJP lean |
| Female | 42.00 | 49.00 | 0.50 | 5.00 | 3.50 | C | Lakshmir Bhandar launch + Duare Sarkar outreach shifted women toward AITC vs 2019 baseline |
| Third_gender | 44.00 | 44.00 | 3.00 | 6.00 | 3.00 | E | |

### D.18 Vote × Welfare scheme exposure (2021 AE)

(Skipped — no `welfare_exposure` axis declared for AC 015 in v0. Welfare-scheme penetration in North Bengal terai follows state rural pattern; document in §F / §H narrative.)

---

## E. 2021 calibration target (2021 AE — tier A)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.** Source: ECI 2021 WB AE; `data/electoral_history/2021/detailed_results.csv`, AC 15 Dhupguri.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 45.65 | A | ECI 2021 WB AE — Bishnu Pada Ray (BJP) 104,688 votes of 229,323 total valid |
| AITC | 43.75 | A | ECI 2021 WB AE — Mitali Roy (AITC) 100,333 votes |
| INC | 0.00 | A | ECI 2021 WB AE — no INC candidate fielded |
| LF | 6.42 | A | ECI 2021 WB AE — CPI(M) 13,107 + SUCI 1,613 = 14,720 votes |
| Other_NOTA | 4.18 | A | ECI 2021 WB AE — BSP 2,178 + IND(1) 2,169 + KPPU 2,155 + NOTA 1,984 + IND(2) 1,096 = 9,582 votes |
| **Sum** | **100.00** | — | self-check |

> ECI 2021 AE AC-015 Dhupguri: BJP 104,688 | AITC 100,333 | BJP margin 4,355 votes (1.90pp) | electorate 263,118 | turnout 87.16%

---

## F. Vote history (pre-2021 anchors for belief evolution)

### AC 015 Assembly Elections

| Year | Winner | Party | % | Runner-up | Party | % | Margin | Notes |
|---|---|---|---|---|---|---|---|---|
| 2011 AE | Mithileswar Burman | AITC | ~47 | CPI(M) candidate | CPI(M) | ~38 | ~12,000 est. | AITC stronghold; Left retreating in North Bengal |
| 2016 AE | Mithileswar Burman | AITC | ~46 | BJP candidate | BJP | ~34 | ~14,000 est. | AITC held; BJP making inroads in Jalpaiguri |
| **2021 AE** | **Bishnu Pada Ray** | **BJP** | **45.65** | Mitali Roy | AITC | 43.75 | **4,355** | **BJP flipped seat; narrow margin; Rajbanshi mobilisation** |

### 2019 LS — AC 015 segment within Jalpaiguri LS (PC 03) (anchor)

Source: `data/2019_AssemblySegmentLevelVotingData.csv`, AC NO = 15. Electorate: 251,681. Total valid votes: 215,128. Turnout: ~85.5%.

| Party | Votes | AC-015 segment % | Tier | Source |
|---|---|---|---|---|
| BJP | 105,729 | 49.15% | A | 2019_AssemblySegmentLevelVotingData.csv |
| AITC | 87,963 | 40.89% | A | Same |
| LF (CPIM 13,016 + SUCI 358) | 13,374 | 6.22% | A | Same |
| INC | 3,065 | 1.42% | A | Same |
| Other_NOTA | 4,981 | 2.32% | A | Same |

Note: 2019 LS BJP plurality (49.15%) stronger than 2021 AE BJP (45.65%), suggesting AITC recovered some ground in 2021 — consistent with TMC statewide landslide (213 seats) and Lakshmir Bhandar / welfare-outreach effect narrowing BJP's lead.

### Key narrative events (2019–2021)

- **2019 May**: BJP wins Jalpaiguri LS (Jayanta Kumar Roy) with strong North Bengal consolidation; AC-015 follows district BJP trend.
- **2020 Mar–Jun**: COVID-19 lockdown; reverse migration; North Bengal seasonal workers return from Kerala, Andhra Pradesh; NH-17 transport disrupted; tea-garden operations disrupted; tea-belt poverty temporarily elevated.
- **2020 May**: Cyclone Amphan — less severe in Jalpaiguri than in 24-Parganas; some peripheral impact in rural areas; state relief delivery seen as AITC positive.
- **2021 Mar–Apr**: WB Assembly Election campaign; BJP holds rallies in North Bengal; North Bengal branded as "BJP territory" by central leadership.
- **2021 Apr**: Lakshmir Bhandar scheme launched — ₹500/month (GEN women) and ₹1,000/month (SC/ST women) to household heads. AC-015 GEN constituency — most women qualify for ₹500 tier. Partial first-disbursement by polling day (May 2021); strong AITC belief vector especially among non-worker women (32.5% of adults).
- **2021 May 2**: WB AE results — TMC 213 / BJP 77 / others 4 statewide; BJP wins AC-015 by narrow 1.90pp margin despite statewide TMC landslide; North Bengal-belt seats were islands of BJP performance.
- **2021 Oct 11**: BSF jurisdiction extended to 50km from Bangladesh border; Jalpaiguri district falls within new zone; BJP framed as border security; TMC opposed as federal overreach.
- **2021 Oct 13–20**: Bangladesh Durga Puja temple attacks — communal violence in Bangladesh; Jalpaiguri/North Bengal Hindu community anxiety; reinforced border and Hindu-protection narrative beneficial to BJP.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Election Commission of India — `data/electoral_history/2021/detailed_results.csv` (AC 015 Dhupguri: Bishnu Pada Ray BJP 104,688; Mitali Roy AITC 100,333; margin 4,355; electorate 263,118; turnout 87.16%)
- Election Commission of India — `data/2019_AssemblySegmentLevelVotingData.csv` (AC NO=15; 2019 LS segment)
- ECI Delimitation Commission 2008 — WB Schedule (Jalpaiguri LS = PC 03; Dhupguri = AC 015)
- Census of India 2011 — `data/crosswalk/wb_ac_demographics.csv` (AC 015: pop 368,817; SC 199,294; ST 36,025; literates 236,297)
- `data/master/wb_ac_master_v3.csv` (AC 015: reservation GEN; 2021 winner Bishnu Pada Ray BJP; electorate 263,118; margin 4,355)

### Secondary sources (tier B / C)

- NFHS-5 (2019-21) Jalpaiguri district — `data/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv` — sex ratio 1,038; electricity 97.4%; drinking water 95.2%; sanitation 73.2%; clean cooking 42.7%
- NFHS-4 (2015-16) West Bengal — baseline for trend computation
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2021 NES post-poll WB regional cross-tabs (vote × demographic conditionals)
- WB CDWDSW Lakshmir Bhandar dashboard — scheme launch April 2021
- WB District Statistical Handbook — Jalpaiguri

### Tertiary / journalistic (tier D)

- Wikipedia "Dhupguri" and "Jalpaiguri district" — constituency composition, CD block structure
- Wikipedia "2021 West Bengal Legislative Assembly election" (AC-level results cross-check)
- Wikipedia "Jalpaiguri (Lok Sabha constituency)" — LS segment composition
- North Bengal newspaper reports on 2021 AE results and BJP performance in Jalpaiguri
- General journalistic record of Rajbanshi community BJP alignment in North Bengal

### Tier-D/E reliance flags (what to distrust)

- **Religion breakdown** (C.1, D.11) — Jalpaiguri district Census 2011 used as proxy; no AC-level religion Census table obtained; 2-yr projection from 2019 baseline; tier E
- **Caste sub-group shares** (C.2, D.2) — no post-1931 caste census for non-SC/ST; Rajbanshi dominance from journalistic record; tier C/E
- **Migration/birthplace** (C.16, D.3) — no AC-level Census D-series; tier D from district pattern and journalistic anchor
- **GP-level data** (D.11–D.14) — collapsed to 2 sub-units (Muni + CDB rural); refine when DCHB Jalpaiguri Part-A accessible
- **Asset/media** (C.14, D.4, D.13) — NFHS-5 district-level Jalpaiguri pattern applied; post-COVID smartphone surge modelled from WB state trend; tier C
- **Vote × Demographic** (D.15–D.17) — CSDS 2021 WB regional rollup; locally adjusted for Rajbanshi alignment and 2021 AE result; tier C
- **Assembly election history 2011/2016** (F) — approximate percentages from journalistic record; margin estimates

### v0 known gaps

1. DCHB Jalpaiguri Part-A — sub-units collapsed to 2 (Muni + CDB rural) instead of full GP disaggregation
2. Census 2011 AC-level religion table — using district-level proxy; AC boundary may differ from block boundary
3. Census HH-13 GP-level — using NFHS-5 district-level proxy for asset/media
4. Census D-series — using qualitative/journalistic anchor for migration
5. Full CSDS WB 2021 regional cross-tabs — using WB state-level post-poll; no Jalpaiguri-specific sub-sample
6. 2011 and 2016 AE results — precise vote shares and candidate names not verified from ECI archive; estimates from Wikipedia/journalistic sources
7. LF disaggregation in 2021 AE: CSV shows CPI(M) 13,107 + SUCI 1,613 = 14,720 total LF; combined as single LF entry per schema

---

*v0 — generated 2026-04-28, frozen at 2021 state-of-knowledge. No post-2021 events referenced.*

---

## H. Post-2021 validation anchors (OUT-OF-SAMPLE)

> **These are out-of-sample simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs. The validator's
> leakage gate exempts §H from the no-future-leakage check.

### 2024 LS AC-015 segment within Jalpaiguri LS (PC 03) (tier A, CSV)

Source: `data/2024_AssemblySegmentLevelVotingData.csv`, AC NO = 15. Electorate: 269,522. Total valid votes: 223,799. Turnout: ~83.0%.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Dr Jayanta Kumar Roy | 106,651 | 47.65% | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Nirmal Chandra Roy | 100,322 | 44.83% | A | Same |
| LF (CPIM + SUCI) | Debraj Barman + SUCI | 10,043 | 4.49% | A | CPIM 9,733 + SUCI 310 |
| INC | (no INC candidate) | 0 | 0.00% | A | No INC entry in 2024 |
| Other_NOTA | BSP + KPPU + MPOI + IND×5 + NOTA | 6,783 | 3.03% | A | Computed residual |
| **BJP margin over AITC** | — | 6,329 votes | 2.82pp | A | Computed |

Calibration test: simulator validated if 2024 LS AC-015 shares reproduced within ±3pp of tier-A figures:
- BJP target: 47.65% ± 3pp
- AITC target: 44.83% ± 3pp
- LF target: 4.49% ± 3pp
- Other_NOTA target: 3.03% ± 3pp
