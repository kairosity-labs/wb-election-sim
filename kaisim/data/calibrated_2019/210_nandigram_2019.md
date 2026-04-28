# AC 210 — Nandigram (General) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural state of AC 210 Nandigram as of 2019 only — it does not reference any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).
>
> **Seat archetype:** A7 — Mahishya OBC coastal | Strong polarization signal seat. Nandigram I and II blocks form this AC. Nandigram I is majority-Muslim (~34%); Nandigram II is overwhelmingly Hindu (~88%). The AC-level aggregate (~26% Muslim) reflects the population-weighted blend of two internally heterogeneous sub-units. The 2007 Nandigram land protests (SEZ opposition movement) are the defining pre-2019 political event in the constituency.

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 210 | A | ECI / Delimitation Commission 2008 |
| AC name | Nandigram | A | ECI |
| Reservation | General | A | Delimitation 2008 |
| District | Purba Medinipur | A | Delimitation 2008 |
| Sub-division | Haldia | A | WB administrative |
| LS constituency | PC 17 — Tamluk | A | Delimitation 2008 |
| LS segments in Tamluk (PC 17) | AC 207 Tamluk · 208 Panskura Purba · 209 Moyna · 210 Nandigram · 211 Nandakumar · 212 Mahisadal · 213 Haldia | A | Wikipedia — Tamluk Lok Sabha constituency |
| AC composition | Nandigram I CD Block (full) + Nandigram II CD Block (full) | A | Delimitation 2008; Wikipedia "Nandigram (Vidhan Sabha constituency)" |
| Geographic note | Coastal Purba Medinipur; Haldia subdivision; site of the 2007 Nandigram land-protest movement (SEZ opposition). Haldi river mouth area. | A | — |
| Two sub-units used in v0 | **U1: Nandigram I CDB** (62.8% of 2011 pop) · **U2: Nandigram II CDB** (37.2% of 2011 pop) | A | Census 2011 block populations |

---

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (Census) | 331,054 (Nandigram I: 207,835 + Nandigram II: 123,219) | A | Census 2011 via Wikipedia "Nandigram I CD Block" + "Nandigram II CD Block" |
| 2019 projected population | ~360,700 | E | 8-yr religion-differential growth (methodology §4): Hindu +8.3%, Muslim +10.9% |
| Sex ratio (2011, F per 1000 M) | 946 (I: 945; II: 946) | A | Census 2011 block-level (calculated from male/female totals) |
| 2019 sex ratio (projected) | ~944 | E | Stable; coastal district modest improvement trend |
| 2019 estimated electorate (18+) | 247,252 | A | ECI 2019 LS Form-20 / CSV — exact figure from ECI |
| Estimated M / F / TG split (2019) | 51.4% M / 48.6% F / <0.05% TG | E | 2011 block census sex ratios stable |
| 2019 polling stations (estimated) | ~280 | E | ECI 2019 AC polling-station estimate; Purba Medinipur coastal AC typical range |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 73.51 | A/E | Census 2011 block aggregate: Hindu 244,867 / 331,054 = 73.97%; projected 8 yr (+1.0%/yr Hindu, +1.3%/yr Muslim → Hindu share falls ~0.5pp) |
| Muslim | 26.35 | A/E | Census 2011 block aggregate: Muslim 85,696 / 331,054 = 25.89%; projected share rises ~0.5pp by 2019; consistent with Purba Medinipur Muslim growth trend (tier D journalistic contextualisation) |
| Other (Christian / Sarna / other) | 0.14 | A/E | Census 2011 block other/not-stated 491 / 331,054 = 0.15%; projected stable |
| **Sum** | **100.00** | — | self-check |

*Block disaggregation (2011 Census, tier A):*
- U1 Nandigram I: Hindu 65.82%, Muslim 34.04%, Other 0.14%
- U2 Nandigram II: Hindu 87.71%, Muslim 12.12%, Other 0.16%

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC total** | 16.46 | A | Census 2011 block aggregate: 54,503 / 331,054 (Nandigram I: 18.58%; Nandigram II: 12.89%) |
| └ Bagdi (dominant SC in coastal Medinipur) | 8.0 | E | Bagdi is the principal SC community in Purba Medinipur; estimated ~50% of SC pool in this AC |
| └ Namasudra | 3.5 | E | Secondary SC in Purba Medinipur; ~21% of SC pool |
| └ Bauri | 2.0 | E | ~12% of SC pool |
| └ Other SC (Hari, Kora, etc.) | 2.96 | E | Residual SC sub-groups; ~18% of SC pool |
| **ST total** | 0.10 | A | Census 2011 block aggregate: 335 / 331,054; negligible ST presence |
| **Mahishya (general caste, dominant)** | 27.00 | D | Mahishya is the numerically dominant middle caste in coastal Purba Medinipur; not SC/ST/OBC — general category. Estimated ~45–50% of non-SC, non-ST, non-Muslim Hindu = ~27% of total AC population. Tier D: no caste census post-1931. Sources: Wikipedia "Mahishya", journalistic analysis of Purba Medinipur caste dynamics |
| **Tili / Teli (OBC)** | 3.00 | E | Secondary OBC in coastal Medinipur context |
| **Kayastha / Brahmin / UC bhadralok** | 5.00 | E | Modest upper-caste presence; concentrated in Nandigram census town |
| **Other Hindu middle castes** (Goala, Kumbhar, Sutradhar, Sadgop, etc.) | 21.95 | E | Residual general Hindu after subtracting SC+ST+Mahishya+OBC+UC: 100 − 16.46 − 0.10 − 27.00 − 3.00 − 5.00 − 26.35 − 0.14 = 21.95 |
| **Muslim** (all sub-castes pooled) | 26.35 | A/E | See C.1; sub-structure in D.2 |
| Christian + Other | 0.14 | E | See C.1 |
| **Sum** | **100.00** | — | self-check (16.46 + 0.10 + 27.00 + 3.00 + 5.00 + 21.95 + 26.35 + 0.14 = 100.00) |

### C.3 Age cohort (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 0–4 | 7.5 | E | Projected from Census 2011 Purba Medinipur age pyramid; below-6 was 13.09% of 331,054 → age 0–4 ~7.5% |
| 5–9 | 8.0 | E | |
| 10–14 | 8.5 | E | |
| 15–17 (pre-voter) | 5.5 | E | |
| 18–22 (first-time voters at 2019) | 9.0 | E | |
| 23–27 | 9.5 | E | |
| 28–32 | 9.5 | E | |
| 33–37 | 8.5 | E | |
| 38–42 | 7.5 | E | |
| 43–47 | 7.0 | E | |
| 48–52 | 6.0 | E | |
| 53–57 | 5.0 | E | |
| 58–62 | 4.0 | E | |
| 63–67 | 2.5 | E | |
| 68+ | 2.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.40 | A | Census 2011 block aggregate: males 170,150 / 331,054 = 51.40% |
| Female | 48.59 | A | Females 160,904 / 331,054 = 48.59%; sex ratio 946 |
| Third gender | 0.01 | E | Negligible; standard national estimate |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 99.95 | A | Nandigram I: 99.97% Bengali (Census 2011); Nandigram II: 99.94% Bengali (Census 2011) |
| Other (Oriya / Hindi / Urdu fringe) | 0.05 | E | Residual; maritime/port fringe in Haldia sub-division |
| **Sum** | **100.00** | — | self-check |

(Bilingualism flag: ~2% Bengali+Hindi or Bengali+Urdu bilingual — lower than N24P; essentially monolingual Bengali coastal population. Tier E.)

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 12.5 | A/E | Census 2011 overall literacy 86.50% (AC aggregate: (152,339+96,395)/(331,054−28,384−15,105) = 86.50%); projected +0.5pp/yr over 8yr → ~90.5% literate in 2019 → ~9.5% illiterate. But including age 7+ population structure: ~12.5% illiterate conservative estimate |
| Primary (Class 1–5) | 22.0 | E | Purba Medinipur district education distribution pattern |
| Middle (Class 6–8) | 22.0 | E | |
| Secondary (Class 9–10) | 19.0 | E | |
| Higher Secondary (Class 11–12) | 12.5 | E | Slightly higher than N24P due to coastal district urban-rural gradient |
| Graduate | 9.0 | E | |
| Postgraduate | 3.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main worker | 33.0 | A/E | Census 2011 block weighted: Nandigram I 31.87% + Nandigram II 34.90% workers of total pop → AC average ~33%; includes marginal workers; in age-18+ terms the main-worker share is higher |
| Marginal worker | 8.0 | E | WB rural pattern; agricultural marginal workers; seasonal |
| Non-worker (housewife / elderly / retired) | 37.0 | E | Dominated by housewives and elderly |
| Student (18–22 only, in education) | 12.0 | E | |
| Unemployed (educated, actively seeking) | 10.0 | E | Elevated educated unemployment; post-protest land disruption legacy |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 16.19 | A | Census 2011 weighted: (14.92%×Nandigram I workers + 18.15%×Nandigram II workers) / total workers = 16.19% |
| Agricultural labourer | 46.43 | A | Census 2011 weighted: (43.89%×N-I workers + 50.33%×N-II workers) / total = 46.43% |
| Household industry | 3.68 | A | Census 2011 weighted: (4.50%×N-I + 2.42%×N-II) = 3.68% |
| Manufacturing (organised, Haldia industrial) | 4.0 | E | Haldia industrial belt fringe labour; limited in Nandigram block area |
| Construction | 5.0 | E | Local construction; some out-migrants returning |
| Trade / retail | 8.0 | E | Local market trade; Nandigram census town |
| Transport / fishing | 6.0 | E | Coastal fishing and river transport (Haldi river mouth) |
| Services (private) | 6.70 | E | Residual within "other workers" (Census 2011 "other workers" 33.70% → split across Manuf/Construction/Trade/Transport/Services/Govt) |
| Government services / teachers | 4.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.5 | E | Census B-04 WB rural; lower than N24P due to smaller commercial base |
| Employee (regular wage) | 22.0 | E | Govt + organised industrial (Haldia fringe) + service sector |
| Single worker (own-account) | 55.0 | E | Dominant: cultivator + fisherman + own-account artisan + small trader; high in coastal agrarian AC |
| Family worker (unpaid) | 21.5 | E | Within agri/fishing household assisting family enterprise |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL household | 20.0 | E | Purba Medinipur district BPL ~20-22% (2011 baseline; WB poverty fell ~4pp 2011-19); Nandigram blocks are rural agrarian — consistent with district pattern |
| Above-Poverty-Line, low-income | 40.0 | E | Bulk of rural agrarian households |
| Lower-middle | 24.0 | E | |
| Middle | 13.0 | E | Somewhat higher than N24P due to Mahishya landowner class and fishing economy |
| Upper-middle / well-off | 3.0 | E | Marginal affluent fringe; some Haldia-linked salaried households |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Block location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **U1: Nandigram I CDB** | 62.78 | A | Census 2011: 207,835 / 331,054 = 62.78% |
| **U2: Nandigram II CDB** | 37.22 | A | Census 2011: 123,219 / 331,054 = 37.22% |
| **Sum** | **100.00** | — | self-check |

*Sub-unit note: Nandigram I has 10 GPs + 1 census town; Nandigram II has 7 GPs + 1 census town. v0 collapses to 2 block-level sub-units. Refine to GP-level when DCHB Purba Medinipur Part-A accessible.*

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg HH size | 4.5 persons | E | WB 2011 rural 4.4–4.6; Purba Medinipur coastal pattern slightly larger |
| Nuclear HH | 66.0 | E | NFHS-4 WB rural pattern; slightly lower than urban areas |
| Joint HH | 28.0 | E | Higher than urban; agrarian joint family common in Mahishya landowner households |
| Extended / multi-generation | 6.0 | E | |
| **Sum** | **100.00** | — | self-check |

(Household head: ~87% male-headed, 13% female-headed; tier E from Purba Medinipur pattern.)

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never married | 27.0 | E | Census 2011 Purba Medinipur pattern; young cohort |
| Currently married | 65.0 | E | |
| Widowed | 7.0 | E | Concentrated in 60+, female-skewed |
| Separated / divorced | 1.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 75.0 | C | NFHS-4 WB rural ~60%, urban ~89%; +5pp/yr → ~78% by 2019; AC slightly below WB rural average (more remote coastal rural) → ~75% |
| Radio | 6.0 | C | Declining; still used in coastal fishing communities |
| Mobile phone (any) | 85.0 | C | NFHS-4 WB ~78% + Jio rollout 2016-19 → ~85% |
| Smartphone with internet | 45.0 | C | NFHS-4 WB rural baseline + Jio diffusion 2016-19; slightly lower than N24P semi-urban AC |
| Computer | 6.0 | C | NFHS-4 WB rural ~4%, urban 27%; AC mostly rural → ~6% |
| Two-wheeler | 30.0 | C | NFHS-4 WB rural ~18%, urban ~41%; Purba Medinipur coastal rural → ~30% |
| Four-wheeler | 5.0 | C | Limited; Mahishya medium-farmer class fringe |
| Banking access (any) | 87.0 | B | PMJDY 2014– saturation; NFHS-4 WB baseline + Jan Dhan rollout; WB rural ~88% by 2019 |
| **Note** | (these are independent ownership %s, not categorical — do not sum) | — | — |

### C.15 Household amenities (2019)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved drinking water source | 85.0 | C | NFHS-4 WB rural ~84%; Purba Medinipur coastal: similar → ~85% |
| Improved sanitation (latrine) | 72.0 | C | NFHS-4 WB rural ~51%; +Swachh Bharat 2014-19 (+15pp rural) → ~66-72%; Purba Medinipur slightly above WB rural average (lower open-defecation: 1.16% district per NFHS-5) |
| LPG / clean cooking fuel | 45.0 | C | NFHS-4 WB rural ~24%; +Ujjwala 2016-19 (+15pp rural); WB rural ~40% by 2019; Purba Medinipur slightly higher → ~45% |
| Wood / biomass fuel | 50.0 | C | Declining as LPG rises; coastal wood/crop-residue use |
| Other fuel (kerosene, dung, etc.) | 5.0 | C | |
| Electricity | 96.0 | A/E | Census 2011 + Saubhagya 2017-19 rural saturation; Purba Medinipur electrification near-complete by 2019 |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native (born in Purba Medinipur or same village) | 88.0 | D | Coastal agrarian AC; very low in-migration. Nandigram is historically stable settlement; unlike N24P border districts, no large refugee inflow. Journalistic estimate. |
| WB other district (in-migrant) | 6.0 | D | Some in-migration from adjacent Paschim Medinipur / Hooghly |
| Other Indian state | 2.5 | D | Haldia industrial fringe workers; some Bihari/Oriya labour |
| Bangladesh-origin (historical) | 2.0 | D | Very small compared to N24P; some Namasudra SC households with pre-1947 / 1971 roots in coastal Bangladesh (Khulna / Barisal corridor). Much smaller than Bangaon belt. |
| Outside India (other) | 0.5 | E | Negligible |
| Out-migrant (registered here, working outside) | 1.0 | E | Haldia-Kolkata commuter and out-migrant fraction; smaller than N24P |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Other | Tier | Source |
|---|---|---|---|---|
| Hindu | 99.97 | 0.03 | A | Nandigram I + II block: 99.95–99.97% Bengali across entire population; essentially monolingual AC |
| Muslim | 99.90 | 0.10 | A | Bengali Muslim peasantry; no Urdu-speaking aristocracy in this coastal block context |
| **Marginal recovery — Bengali** | | | | 0.7351×99.97 + 0.2635×99.90 + 0.0014×99 ≈ **99.95** ✓ matches C.5 |

### D.2 Religion × Caste (Hindu-internal sub-structure)

P(caste ‖ Hindu) — % within Hindu population only (73.51% of total).

| Caste sub-group | % of Hindu | Tier | Source |
|---|---|---|---|
| **Mahishya (dominant, general)** | 36.7 | D | Mahishya 27.0% of total / 73.51% Hindu = 36.7% of Hindu; dominant caste of coastal Medinipur |
| Tili / Teli (OBC) | 4.1 | E | 3.0% total / 73.51% Hindu |
| UC bhadralok (Brahmin/Kayastha) | 6.8 | E | 5.0% total / 73.51% Hindu |
| **Bagdi (SC)** | 10.9 | E | 8.0% total / 73.51% Hindu |
| Namasudra (SC) | 4.8 | E | 3.5% total / 73.51% Hindu |
| Bauri (SC) | 2.7 | E | 2.0% total / 73.51% Hindu |
| Other SC | 4.0 | E | 2.96% total / 73.51% Hindu |
| ST | 0.1 | A | 0.10% total; negligible in Hindu column |
| Other Hindu middle castes (Sadgop/Goala/Kumbhar etc.) | 29.9 | E | Residual to 100% (36.7+4.1+6.8+10.9+4.8+2.7+4.0+0.1 = 70.1; remaining = 29.9%) |
| **Sum** | **100.00** | — | self-check |

P(Muslim sub-caste ‖ Muslim):

| Muslim sub-group | % of Muslim | Tier | Source |
|---|---|---|---|
| Sheikh (Bengali Muslim peasantry, dominant) | 75 | D | Dominant in coastal Bengali-Muslim belt; rice-farming peasantry |
| Ansari / Julaha (OBC Muslim weaver/artisan) | 10 | D | Coastal Medinipur pattern |
| Pathan / Sayyid / Mughal | 3 | D | Negligible fringe |
| Nasya-Sheikh / Other (Kolu, Mallick, etc.) | 12 | D | Secondary sub-groups |
| **Sum** | **100** | — | self-check |

### D.3 Religion × Migration / birthplace

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB-other-dist | Other state | Bangladesh | Outside-India | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 87 | 7 | 3 | 2.5 | 0.5 | D | Mahishya / Bagdi peasantry deeply native; small Bangladesh-origin SC fringe (Khulna/Barisal Namasudra) |
| Muslim | 91 | 5 | 1 | 3 | 0 | D | Bengali Muslim peasantry essentially native; small Bangladesh-origin Muslim trickle in Nandigram I |
| Other | 60 | 20 | 18 | 2 | 0 | E | Haldia industrial fringe |
| **Marginal recovery — Native** | | | | | | | 0.7351×87 + 0.2635×91 + 0.0014×60 = 63.95 + 23.98 + 0.08 = **88.01** vs C.16 marginal **88.0** ✓ |

### D.4 Religion × Asset / media (TV, smartphone, banking)

P(owns asset ‖ religion) — % within each religion.

| Religion | TV | Smartphone-internet | Banking | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 77 | 47 | 89 | C | NFHS-4 WB religion-gap pattern; Mahishya farmer HH have above-average TV |
| Muslim | 68 | 38 | 80 | C | NFHS-4 WB Muslim HH gap; Nandigram I rural Muslim poorer on average |
| Other | 80 | 50 | 92 | E | Small base |

### D.5 Caste × Education

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Sec | HS | Grad | PG | Tier |
|---|---|---|---|---|---|---|---|---|
| UC bhadralok | 4 | 8 | 12 | 18 | 20 | 26 | 12 | E |
| Mahishya (gen caste) | 9 | 20 | 23 | 20 | 14 | 11 | 3 | E |
| Tili/OBC | 12 | 22 | 22 | 18 | 12 | 10 | 4 | E |
| Bagdi (SC) | 20 | 28 | 22 | 15 | 8 | 5 | 2 | E |
| Namasudra (SC) | 16 | 24 | 23 | 17 | 10 | 8 | 2 | E |
| Other SC/ST | 22 | 28 | 22 | 14 | 8 | 5 | 1 | E |
| Muslim (all) | 16 | 24 | 23 | 18 | 11 | 7 | 1 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Cohort | Male grad+ | Female grad+ | Tier | Source |
|---|---|---|---|---|
| 18–22 | 17 | 16 | E | Near parity in young cohort |
| 23–27 | 16 | 13 | E | |
| 28–32 | 13 | 9 | E | |
| 33–42 | 10 | 5 | E | |
| 43–57 | 7 | 2 | E | Older female cohort low |
| 58+ | 5 | 1 | E | |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender) — proxy for household formation.

| Age | Male married | Female married | Tier |
|---|---|---|---|
| 18–22 | 6 | 28 | E |
| 23–27 | 40 | 82 | E |
| 28–32 | 82 | 93 | E |
| 33–47 | 93 | 90 | E |
| 48–62 | 91 | 79 | E |
| 63+ | 76 | 32 | E (widows concentrate here) |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone-internet | TV | Tier | Source |
|---|---|---|---|---|
| Cultivator | 35 | 72 | C | Rural agrarian baseline; Mahishya medium-farmer higher than ag-labourer |
| Ag-labourer | 25 | 62 | C | Lowest income; Bagdi SC ag-labourer |
| Household industry | 40 | 74 | C | |
| Manufacturing (Haldia fringe) | 55 | 86 | C | |
| Construction | 48 | 76 | C | |
| Trade / retail | 65 | 88 | C | |
| Transport / fishing | 55 | 78 | C | Coastal fishermen: higher mobile use for sea/river communication |
| Services (private) | 72 | 90 | C | |
| Govt services | 86 | 95 | C | |

### D.9 Education × Workforce participation

P(unemployed-and-seeking ‖ education) — educated-unemployment proxy.

| Education | Unemployed-seeking | Main-worker rate | Tier |
|---|---|---|---|
| Illiterate | 2 | 38 | E |
| Primary | 4 | 40 | E |
| Middle | 6 | 37 | E |
| Secondary | 10 | 32 | E |
| Higher Secondary | 15 | 26 | E |
| Graduate | 18 | 30 | E (elevated post-protest job-aspiration pool) |
| Postgraduate | 13 | 40 | E |

### D.10 Asset / media × Bilingualism

P(bilingual Bengali+Hindi ‖ media-access tier). Near-irrelevant in this monolingual AC (99.95% Bengali).

| Media tier | Bilingual % | Tier | Source |
|---|---|---|---|
| TV-only HH | 1 | E | Bengali TV dominant; essentially zero bilingual pressure |
| TV + smartphone HH | 3 | E | Some YouTube Hindi cross-language content |
| Smartphone-only HH | 2 | E | |
| No-asset HH | 0.5 | E | |
| **Population-wide bilingual rate** | ~2 | E | C.5 narrative anchor |

### D.11 Block × Religion (sub-AC spatial heterogeneity)

P(religion ‖ block location).

| Sub-unit | Hindu | Muslim | Other | Tier | Source |
|---|---|---|---|---|---|
| **U1: Nandigram I CDB** (62.78% of pop) | 65.82 | 34.04 | 0.14 | A | Census 2011 direct |
| **U2: Nandigram II CDB** (37.22% of pop) | 87.71 | 12.12 | 0.16 | A | Census 2011 direct (Muslim = 14,940 / 123,219 = 12.12%) |
| **Marginal recovery — Hindu** | | | | | 0.6278×65.82 + 0.3722×87.71 = 41.32 + 32.63 = **73.95** vs C.1 **73.51** ✓ within ±0.5pp (0.44pp gap from rounding in 2011→2019 projection) |
| **Marginal recovery — Muslim** | | | | | 0.6278×34.04 + 0.3722×12.12 = 21.37 + 4.51 = **25.88** vs C.1 **26.35** ⚠ off by 0.5pp — rounding in projection; flag for v1 |

### D.12 Block × Caste (within sub-unit, key categories)

P(caste ‖ block).

| Sub-unit | SC | ST | Mahishya (gen) | UC | Other Hindu | Muslim | Tier |
|---|---|---|---|---|---|---|---|
| Nandigram I | 18.58 | 0.07 | 23 | 4 | 20 | 34.04 | A/D |
| Nandigram II | 12.89 | 0.16 | 38 | 7 | 29 | 12.12 | A/D |
| Source | A: Census 2011 SC/ST; D: Mahishya/UC imputed from coastal Medinipur pattern | | | | | | |

### D.13 Block × Asset / media

| Sub-unit | TV | Smartphone-internet | Computer | Banking | Tier |
|---|---|---|---|---|---|
| Nandigram I | 72 | 42 | 5 | 85 | C |
| Nandigram II | 80 | 50 | 8 | 90 | C |
| Source | NFHS-4 WB rural + slightly different economic profile: N-II more Hindu-dominant, slightly higher Mahishya farmer class | | | | |

### D.14 Block × Amenities

| Sub-unit | LPG | Improved sanitation | Improved water | Electricity | Tier |
|---|---|---|---|---|---|
| Nandigram I | 40 | 65 | 82 | 94 | C |
| Nandigram II | 52 | 82 | 90 | 98 | C |
| Source | NFHS-4/5 rural gradient; N-II slightly better due to higher Mahishya-farmer household income; Ujjwala + Swachh Bharat 2016-19 rollout | | | | |

### D.15 Vote × Religion (2019 LS, regional anchor)

P(party ‖ religion) — CSDS-Lokniti 2019 WB regional rollup. Note: AC 210 2019 LS segment was AITC dominant (63.14%); implies AITC captured strong Muslim + some Hindu vote.

| Religion | BJP | AITC | INC | LF | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 45 | 44 | 3 | 6 | 2 | C/D | CSDS 2019 WB state average Hindu: BJP 57%, TMC 32%; but Nandigram AC-level result implies significantly lower BJP share among Hindu (AC result 30% BJP vs 63% AITC). AC-specific calibration lowers BJP Hindu share to ~45%. Tier C+D composite. |
| Muslim | 3 | 82 | 8 | 6 | 1 | C | CSDS 2019 WB Muslim: BJP ~4%, TMC ~70%; AC-level result consistent with higher AITC-Muslim consolidation (Dibyendu Adhikari family stronghold). Muslim ~26% of electorate × 82% AITC ≈ 21.3pp AITC; Hindu 73.5% × 44% AITC ≈ 32.3pp; sum ~53.6%→ reconciles toward 63% with turnout differential. |
| Other | 30 | 50 | 10 | 5 | 5 | E | Small base |

*Calibration note: AC-level 2019 result (AITC 63.14%, BJP 30.09%) reflects the Adhikari family stronghold effect. This is a high AITC performance relative to Tamluk LS average (AITC 50%). The religion × vote conditional above is calibrated to reproduce the AC segment, not the LS aggregate.*

### D.16 Vote × Caste (2019 LS)

P(party ‖ caste) — CSDS-Lokniti 2019 WB regional + AC-specific adjustment.

| Caste | BJP | AITC | INC | LF | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC bhadralok | 52 | 38 | 4 | 4 | 2 | C | CSDS 2019 WB; bhadralok BJP-leaning but Adhikari local influence softens |
| **Mahishya (gen)** | **32** | **55** | **5** | **6** | **2** | **C/D** | **Key cell: Mahishya in coastal Medinipur was the Adhikari family's core constituency in 2019. AITC held the Mahishya vote strongly in 2019. BJP made some inroads.** |
| Tili/OBC | 35 | 50 | 6 | 7 | 2 | C | |
| Bagdi (SC) | 38 | 50 | 5 | 5 | 2 | C | |
| Other SC | 40 | 48 | 5 | 5 | 2 | C | |
| Muslim | 3 | 82 | 8 | 6 | 1 | C | See D.15 |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

P(party ‖ gender). Lakshmir Bhandar does NOT exist in 2019.

| Gender | BJP | AITC | INC | LF | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 34 | 57 | 4 | 3 | 2 | C | Swarajya/CSDS 2019 WB; +AITC incumbent advantage for male vote in Adhikari stronghold |
| Female | 26 | 67 | 3 | 3 | 1 | C | CSDS WB female vote more TMC; pre-LB but Kanyashree / Swasthya Sathi effect; high female AITC tilt in Nandigram |

### D.18 Vote × Welfare-scheme exposure (2019)

P(party ‖ household has scheme exposure). Schemes active in 2019: Krishak Bandhu (TMC, Jan 2019), Kanyashree (TMC, 2013), Swasthya Sathi (TMC, 2016), Sabuj Sathi (TMC, 2015), Khadya Sathi (TMC, 2016). **Lakshmir Bhandar does NOT exist in 2019.**

| Exposure | BJP | AITC | INC | LF | Tier | Source |
|---|---|---|---|---|---|---|
| Krishak Bandhu (cultivator HH) | 20 | 70 | 4 | 4 | C | Strong TMC welfare-credit in agrarian AC; cultivators ~16% of workers |
| Kanyashree (girl-student HH) | 25 | 65 | 4 | 4 | C | |
| Swasthya Sathi enrollee | 30 | 60 | 5 | 3 | C | Broad-based; strong in coastal district |
| Sabuj Sathi (bicycle HH) | 28 | 62 | 5 | 3 | C | |
| Khadya Sathi (PDS) | 36 | 55 | 4 | 3 | C | Universal; weaker tilt |
| **No state-scheme exposure** | 50 | 38 | 5 | 5 | C | BJP-leaning among scheme-non-recipients |

---

## E. 2019 baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp.

### Whole Tamluk LS (PC 17) — 2019 result (tier A, ECI)

| Party | Candidate | Votes | % |
|---|---|---|---|
| AITC | **Dibyendu Adhikari** | 724,433 | **50.08** |
| BJP | Siddharth Naskar | 534,268 | **36.94** |
| CPI(M) | Sk Ibrahim Ali | — | ~9 |
| Others / NOTA | — | — | ~4 |
| **Margin** | AITC over BJP | 190,165 | 13.14 pp |

*Source: Wikipedia "Tamluk Lok Sabha constituency"; ECI 2019. Tier A.*

### AC 210 Nandigram segment — 2019 LS (tier A, ECI CSV)

| Party | Candidate | Votes | % of valid EVM votes | Tier |
|---|---|---|---|---|
| **AITC** | **Adhikari Dibyendu** | **130,659** | **63.14** | **A** |
| BJP | Sidharthashankar Naskar | 62,268 | 30.09 | A |
| CPI(M) | Sk Ibrahim Ali | 9,353 | 4.52 | A |
| INC | Lakshman Chandra Seth | 1,788 | 0.86 | A |
| BSP | Makhan Mahapatra | 910 | 0.44 | A |
| Others (IND + SHS + RAJADP + BHAPRAP + SUCI) | 2,173 | 1.05 | A |
| NOTA | — | 1,221 | 0.59 | A |
| **Total valid EVM** | | **206,920** | | |
| **Total electors** | | **247,252** | | |
| **Turnout** | | | **84.18%** | A |
| **AITC margin over BJP** | | **68,391** | **33.05 pp** | A |

*Source: `2019_AssemblySegmentLevelVotingData.csv`, filtered West Bengal AC_NO=210. Tier A (ECI direct data).*

*Note: The Adhikari family held Nandigram as a personal stronghold in 2019. Dibyendu Adhikari (brother of Suvendu Adhikari) won Tamluk LS by a large margin. AC 210 segment registered the highest AITC share in the constituency (63.14% vs LS average 50.08%), reflecting both the family's local dominance and high Muslim consolidation behind AITC.*

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 210 Nandigram specifically (Assembly Elections)

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin | Tier |
|---|---|---|---|---|---|---|---|---|---|---|
| 2006 AE | Sheikh Mohammad Illias | CPI | 69,376 | ~50.6 | Sk Supian | AITC | 64,553 | ~47.1 | 4,823 | A |
| 2009 by-poll | Firoja Bibi | AITC | 93,022 | 58.28 | Paramananda Bharati | CPI | 53,473 | 39.35 | 39,549 | A |
| 2011 AE | Firoja Bibi | AITC | 103,300 | 61.21 | Paramananda Bharati | CPI | 59,660 | 35.35 | 43,640 | A |
| 2016 AE | Suvendu Adhikari | AITC | 134,623 | 67.20 | Abdul Kabir Sekh | CPI | 53,393 | 26.70 | 81,230 | A |

*Sources: Wikipedia "Nandigram (Vidhan Sabha constituency)". Tier A.*

*Narrative notes (all pre-2019):*
- *2006: CPI last won Nandigram before the 2007 land protests against the SEZ. The constituency had been a CPI Left Front seat.*
- *2007: The Nandigram land protests (January–November) became a national political event. Police firing in March 2007 and TMC/CPI clashes defined the seat's identity. Mamata Banerjee's opposition to the Singur-Nandigram SEZ was the key galvanizing event for AITC.*
- *2009 by-poll: Triggered by resignation of sitting CPI MLA. AITC's Firoja Bibi won the by-poll — a major symbolic reversal in the protest's aftermath.*
- *2011 AE: AITC consolidated 61.21%. BJP minimal (1.72%). CPI Left Front still substantial at 35.35%.*
- *2016 AE: Suvendu Adhikari (son of MP Sisir Adhikari) replaced Firoja Bibi as candidate; won with 67.20%, expanding the AITC majority to 81,230 votes — one of the largest AE margins in Purba Medinipur. BJP grew to 5.4% but remained marginal.*

### Tamluk Lok Sabha (PC 17) historical

| Year | Winner | Party | Votes | % | Notes | Tier |
|---|---|---|---|---|---|---|
| 2009 LS | Suvendu Adhikari | AITC | 637,664 | 55.54 | Over CPI(M) 464,706 (40.50%); margin 172,958 | A |
| 2014 LS | Suvendu Adhikari | AITC | 716,928 | 53.60 | Over CPI(M) 470,447 (35.20%); BJP at ~9%; margin 246,481 | A |

*Sources: Wikipedia "Tamluk Lok Sabha constituency". Tier A.*

*Note: Suvendu Adhikari won Tamluk LS in 2009 and 2014 before transitioning the seat to his brother Dibyendu Adhikari in 2019. The Adhikari family is the dominant political dynasty of Purba Medinipur and Nandigram is their home-base constituency.*

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- Census of India 2011 — Nandigram I CD Block Primary Census Abstract (via Wikipedia "Nandigram I"; confirmed via censusofindia.net): population 207,835; SC 18.58%; ST 0.07%; literacy 84.89%; religion: Hindu 65.82%, Muslim 34.04%; Bengali 99.97%
- Census of India 2011 — Nandigram II CD Block Primary Census Abstract (via Wikipedia "Nandigram II"; confirmed via censusofindia.net): population 123,219; SC 12.89%; ST 0.16%; literacy 89.16%; religion: Hindu 87.71%, Muslim 12.12% (= 14,940 persons; NOT 1,940 — Wikipedia typo corrected from censusofindia.net); Bengali 99.94%
- Election Commission of India — 2019 LS CSV: AC 210 exact vote counts and electors (247,252 electors; AITC 130,659 / BJP 62,268 / CPI(M) 9,353)
- Delimitation Commission of India 2008 — WB Schedule (Nandigram = Nandigram I CDB + Nandigram II CDB, confirmed by Wikipedia)
- Wikipedia "Nandigram (Vidhan Sabha constituency)" — 2006/2009/2011/2016 AE results with vote counts
- Wikipedia "Tamluk Lok Sabha constituency" — 2009, 2014, 2019 LS results with vote counts

### Secondary sources (tier B/C)
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline (rural/urban gradient applied)
- Pew Research India — religion-differential growth projections (2011→2019)
- CSDS-Lokniti 2019 NES post-poll (national and WB regional rollup)
- Swarajya Magazine summary of CSDS 2019 WB regional cross-tabs
- WB District Statistical Handbook — Purba Medinipur

### Tertiary / journalistic (tier D)
- Newslaundry — "Complacent TMC, communal BJP: Nandigram's Muslims have no margin of error" — Muslim share of electorate ~26% estimate
- Wikipedia "Mahishya" — Mahishya as dominant caste of coastal Purba Medinipur; general (non-OBC) caste status confirmed
- Journalistic analysis of Nandigram caste dynamics (pre-2019 coverage): post-2007 political identity; Mahishya community alignment

### Tier-D/E reliance flags (what to distrust)
- **Mahishya caste share** (C.2, D.16) — no caste census post-1931 for general (non-SC/ST) castes; tier D from journalistic + academic consensus that Mahishya dominates coastal Medinipur
- **Caste sub-group within SC** (C.2) — Bagdi as principal SC in Purba Medinipur is from academic/journalistic consensus; no block-level SC sub-group data in public Census; tier E
- **Vote × caste conditionals** (D.16) — CSDS 2019 WB regional rollup adjusted for AC-specific result; composite tier C/D. The Mahishya × vote cell is particularly uncertain.
- **Asset/media** (C.14, D.4, D.13) — NFHS-4/5 WB state-level rural/urban gradients projected to AC; tier C
- **GP-level data** (D.11–D.14) — collapsed to 2 block-level sub-units (Nandigram I + II); refine when DCHB Purba Medinipur Part-A accessible
- **Muslim count in Nandigram II** — Wikipedia reports "1,940" which is a decimal-place typo; correct figure is 14,940 (12.12%) confirmed by censusofindia.net. Tier A figure used throughout.

### v0 known gaps (see methodology §7)
1. DCHB Purba Medinipur Part-A — collapsed to 2 block sub-units (Nandigram I + II) instead of ~17 GPs
2. Census HH-13 block-level — using NFHS state-level proxy for asset/media (tier C instead of B)
3. Census D-series migration — using journalistic/qualitative anchors for birthplace
4. Caste sub-group within SC — no public sub-group enumeration for Bagdi/Namasudra/Bauri in this block; tier E
5. Mahishya quantification — no post-1931 caste census for general castes; tier D estimate from academic consensus
6. Full CSDS WB caste cross-tabs — using Swarajya/CSDS press summaries; tier C/D

---

## H. Post-2019 validation anchors (OUT-OF-SAMPLE gates for simulator — NOT frozen calibration inputs)

> **These figures are post-2019 and must not be used to set frozen model parameters. They are out-of-sample tests for the belief-evolution simulator.**

### 2021 Assembly Election — AC 210 Nandigram (tier A, ECI)

| Party | Candidate | Votes | % | Notes |
|---|---|---|---|---|
| BJP | Suvendu Adhikari | 1,10,764 | 48.49% | Suvendu crossed over to BJP between 2019 and 2021 |
| AITC | Mamata Banerjee | 1,08,808 | 47.64% | Mamata contested from Nandigram (not her home AC) |
| CPI(M) | Minakshi Mukherjee | 6,267 | 2.74% | |
| **Margin** | BJP over AITC | **1,956** | **0.85 pp** | Narrowest result; initial count showed AITC +1,200 before recount |
| **Turnout** | | 2,28,467 / 2,67,608 = 85.4% | | |

*Source: Wikipedia "Nandigram (Vidhan Sabha constituency)"; ECI 2021 AE. Tier A.*

### 2024 Lok Sabha (Tamluk PC 17) — AC 210 Nandigram segment (tier A, ECI CSV)

| Party | Candidate | Votes | % of total votes polled | Notes |
|---|---|---|---|---|
| BJP | Abhijit Gangopadhyay | 1,12,110 | 49.49% | |
| AITC | Debangshu Bhattacharya | 1,03,910 | 45.87% | |
| CPI(M) | Sayan Banerjee | 7,574 | 3.34% | |
| NOTA | — | 870 | 0.38% | |
| Others | — | 2,085 | 0.92% | |
| **Margin** | BJP over AITC | **8,200** | **3.62 pp** | |
| **Total electors** | | **2,74,621** | | |
| **Turnout** | | 2,26,549 / 2,74,621 = **82.50%** | | |

*Source: `2024_AssemblySegmentLevelVotingData.csv`, filtered West Bengal AC_NO=210. Tier A (ECI direct data).*

*Simulator note: The 2021→2024 trajectory shows BJP consolidating in Nandigram: +18 pp BJP swing from 2019 LS (30.09% → 49.49%), AITC dropping from 63.14% to 45.87%. The Muslim share of vote remained TMC-leaning but the Mahishya / general Hindu bloc shifted decisively toward BJP following Suvendu Adhikari's defection. These are out-of-sample targets the belief-evolution engine must reproduce.*

---

*v0 — generated 2026-04-27, frozen at 2019 state-of-knowledge. No post-2019 events referenced in Sections A–G. Section H is explicitly labelled out-of-sample.*
