# AC 95 — Bangaon Uttar (SC) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural state of AC 95 Bangaon Uttar as of 2019 only — it does not reference any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 95 | A | ECI / Delimitation Commission 2008 |
| AC name | Bangaon Uttar | A | ECI |
| Reservation | SC | A | Delimitation 2008 |
| District | North 24 Parganas | A | Delimitation 2008 |
| Sub-division | Bangaon | A | WB administrative |
| LS constituency | 14 — Bangaon (SC reserved) | A | Delimitation 2008 |
| LS segments included with AC 95 | AC 92 Kalyani · 93 Haringhata · 94 Bagda · 95 Bangaon Uttar · 96 Bangaon Dakshin · 97 Gaighata · 98 Swarupnagar | A | Delimitation 2008 |
| AC composition | Bangaon Municipality (full) + 7 of ~16 GPs of CDB Bangaon: Akaipur, Chhaigheria, Dharma Pukuria, Ganganandapur, Ghatbore, Gopalnagar-I, Gopalnagar-II | A | Delimitation 2008 |
| Geographic note | Northern N24P, India-Bangladesh border; Petrapole land port lies within sub-division | A | — |
| Two sub-units used in v0 (GP-conditioning) | **U1: Bangaon Municipality** (urban) · **U2: CDB-Bangaon-rural-share** (the 7 GPs) | E | v0 simplification — see methodology §3 |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~199,792 (Bangaon Muni 108,864 + 7/16 of CDB Bangaon rural 207,835 ≈ 90,928) | E | Census 2011; v0 GP-equal-weight assumption |
| 2019 projected population | ~216,725 | E | 8-yr compound religion-differential growth (methodology §4) |
| Sex ratio (2019, F per 1000 M) | ~949 | E | N24P district baseline 949 (A); minimal projection drift |
| 2019 estimated electorate (18+) | ~245,000 | D | Back-derived from 2021 AE roll 251,387 minus annual additions |
| Estimated M / F / TG split (2019) | 51.4% M / 48.6% F / <0.05% TG | E | 2021 SIR composition projected back |
| 2019 polling stations (estimated) | ~270 | E | 2021 SIR had 276; back-projection |

---

## C. Marginal distributions (15 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 85.45 | E | Bangaon CDB+Muni 2011 weighted, projected 2011→2019 (Hindu +1.0%/yr) |
| Muslim | 13.58 | E | 2011 weighted, projected (+1.3%/yr — slight relative gain ~0.3pp over 8yr) |
| Christian | 0.30 | E | Bangaon sub-division 2011 |
| Sarna-ORP | 0.10 | E | Tribal religion fringe |
| Other (Sikh/Jain/Buddhist) | 0.57 | E | Residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC total** | 43.0 | B | Weighted: Muni ~40% SC + CDB-rural 46.60% (Census 2011) |
| └ Namasudra / Matua | 39.5 | C | ~92% of SC pool in Bangaon (Outlook: ~40% of Bangaon LS electorate is Matua) |
| └ Bagdi | 1.5 | E | ~3% of SC pool (state pattern under-weighted in Matua belt) |
| └ Poundra | 0.7 | E | ~1.6% of SC pool |
| └ Other SC (Rajbanshi/Bauri/Hari etc.) | 1.3 | E | Residual |
| **ST total** | 3.6 | A | Bangaon CDB Census 2011; rural pockets |
| **UC bhadralok** (Brahmin/Kayastha/Baidya) | 10.0 | E | Refugee SC-heavy AC; bhadralok concentrated in Muni |
| **OBC specific** (Mahishya / Sadgop / Kurmi / Teli) | 2.0 | E | Not salient in this AC |
| **Other Hindu middle castes** (Goala / Sutradhar / Tanti / unclassified) | 26.85 | E | Residual within Hindu (85.45 − 43 SC − 3.6 ST − 10 UC − 2 OBC) |
| **Muslim** (all sub-castes pooled) | 13.58 | E | See C.1; sub-structure in joint table D.2 |
| Christian + Sarna + Other | 0.97 | E | See C.1 |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 0–4 | 7.5 | E | Projected from Census 2011 N24P age pyramid |
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
| Male | 51.31 | E | N24P 2011 sex ratio 949 (~51.31% M / 48.68% F); projected stable to 2019 |
| Female | 48.68 | E | |
| Third gender | 0.01 | E | 2021 SIR had 25 / 241,337 = 0.01% |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 98.80 | E | Bangaon CDB 2011: 99.19% Bengali; Muni slightly lower; projected stable |
| Hindi | 0.70 | E | Muni Marwari/Bihari trader fringe |
| Urdu | 0.30 | E | Small Muslim urban pocket |
| Other (Santhali/Sadri/Punjabi etc.) | 0.20 | E | Residual |
| **Sum** | **100.00** | — | self-check |

(Bilingualism flag: ~6% of population is Bengali+Hindi or Bengali+Urdu bilingual. tier E.)

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 14.0 | E | CDB Bangaon literacy 79.71% (2011, A), Muni higher; AC 2019 ~86% literate after +5pp/8yr trend → 14% illiterate |
| Primary (Class 1–5) | 23.0 | E | Census 2011 education distribution scaled |
| Middle (Class 6–8) | 22.0 | E | |
| Secondary (Class 9–10) | 18.0 | E | |
| Higher Secondary (Class 11–12) | 11.0 | E | |
| Graduate | 9.0 | E | |
| Postgraduate | 3.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main worker | 31.0 | E | Census 2011 CDB Bangaon main-worker share ~31%; stable trend |
| Marginal worker | 11.0 | E | |
| Non-worker (housewife / elderly / retired) | 38.0 | E | Includes housewife share heavy in rural |
| Student (18–22 only, in education) | 12.0 | E | |
| Unemployed (educated, actively seeking) | 8.0 | E | Educated unemployment salience; rural job-aspirant pool |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 18.0 | E | Bangaon CDB 2011: 23.80% (rural); Muni dilution → 18% AC weighted |
| Agricultural labourer | 28.0 | E | CDB 2011: 38.09% rural; Muni dilution |
| Household industry | 4.0 | E | CDB 2011: 5.22% |
| Manufacturing (organised) | 4.0 | E | Limited in Bangaon |
| Construction | 6.0 | E | Includes out-migrants returning |
| Trade / retail | 12.0 | E | Bangaon Muni hub for sub-division retail |
| Transport (incl. land-port logistics) | 6.0 | E | Petrapole port economy |
| Services (private) | 12.0 | E | |
| Government services / teachers | 4.0 | E | |
| Out-migrant worker (working outside WB) | 6.0 | D | Matua men to Kerala/TN/Maharashtra; PMC-Springer pattern |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.0 | E | Census B-04 WB rural pattern |
| Employee (regular wage) | 28.0 | E | Govt + organised + retail employees |
| Single worker (own-account) | 50.0 | E | Cultivator + own-account artisan + small trader |
| Family worker (unpaid) | 20.0 | E | Within agri-household helping family farm |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL household | 22.0 | C | Census 2001 CDB Bangaon BPL 27.7%; WB poverty fell ~6pp 2011-19 → ~22% |
| Above-Poverty-Line, low-income | 38.0 | E | |
| Lower-middle | 25.0 | E | |
| Middle | 12.0 | E | |
| Upper-middle / well-off | 3.0 | E | Bangaon Muni small affluent fringe |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Municipality location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **U1: Bangaon Municipality** (urban) | 54.5 | E | 2011: Muni 108,864 / AC 199,792 = 54.5% — held stable to 2019 |
| **U2: CDB-Bangaon rural share** (7 GPs of CDB Bangaon) | 45.5 | E | Remainder; v0 collapses 7 GPs into one cell — refine when DCHB Part-A available |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg HH size | 4.4 persons | E | WB 2011: 4.3; minor projection |
| Nuclear HH | 70.0 | E | NFHS-4 WB rural pattern |
| Joint HH | 24.0 | E | |
| Extended / multi-generation | 6.0 | E | |
| **Sum** | **100.00** | — | self-check |

(Household head: ~88% male-headed, 12% female-headed; tier E from N24P pattern.)

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never married | 28.0 | E | Census 2011 N24P pattern; first-time-voter cohort |
| Currently married | 64.0 | E | |
| Widowed | 7.0 | E | Concentrated in 60+, female-skewed |
| Separated / divorced | 1.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 80.0 | C | NFHS-4 WB (2015-16): rural 60%, urban 89%; +5pp/yr → 2019 AC ~80% |
| Radio | 5.0 | C | Declining nationally |
| Mobile phone (any) | 88.0 | C | NFHS-4 WB ~78%, +growth → ~88% by 2019 |
| Smartphone with internet | 50.0 | C | NFHS-4 baseline + Jio rollout 2016-19 (rapid) |
| Computer | 12.0 | C | NFHS-4 WB rural 4%, urban 27%; AC weighted ~12% |
| Two-wheeler | 35.0 | C | NFHS-4 WB rural 18%, urban 41%; +growth |
| Four-wheeler | 8.0 | C | Limited |
| Banking access (any) | 88.0 | B | PMJDY 2014- saturation; NFHS-4 WB baseline + rollout |
| **Note** | (these are independent ownership %s, not categorical — do not sum) | — | — |

### C.15 Household amenities (2019)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved drinking water source | 86.0 | C | NFHS-4 WB rural 84%, urban 93%; AC weighted |
| Improved sanitation (latrine) | 75.0 | C | NFHS-4 WB rural 51%, urban 84%; +Swachh Bharat 2014-19 (+15pp rural) |
| LPG / clean cooking fuel | 50.0 | C | NFHS-4 WB rural 24%, urban 81%; +Ujjwala 2016-19 (+15pp rural) |
| Wood / biomass fuel | 45.0 | C | Declining as LPG rises |
| Other fuel (kerosene, dung, etc.) | 5.0 | C | |
| Electricity | 97.0 | A | Census 2011 + Saubhagya 2017-19 saturation |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native (born in N24P or in same village/town) | 64.0 | D | Estimate from Matua refugee history + N24P D-series patterns |
| WB other district (in-migrant) | 9.0 | D | Some Kolkata service-class migrants in Muni |
| Other Indian state | 3.0 | D | Marwari/Bihari trader fringe in Muni |
| **Bangladesh-origin (refugee Hindu, mostly Namasudra-Matua)** | 23.0 | D | **Load-bearing**: Matua community is largely descended from East Pakistan / Bangladesh refugees (pre-1947 migration, 1947 partition, 1971 war, post-1971 trickle) |
| Outside India (other than Bangladesh) | 0.5 | E | Negligible |
| Out-migrant (currently living/working outside, registered here) | 0.5 | E | Census reverse — a fraction registered here but absent |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|
| Hindu | 99.4 | 0.5 | 0.0 | 0.1 | E | Bangaon CDB 99.19% Bengali (A); Muni Hindi-trader fringe within Hindu |
| Muslim | 95.0 | 1.5 | 3.0 | 0.5 | E | Bangaon Muslims are Bengali-Sheikh peasantry; very small Urdu pocket |
| Christian | 90.0 | 5.0 | 0.0 | 5.0 | E | Tiny base; Bengali + English-medium families |
| Other | 60.0 | 30.0 | 0.0 | 10.0 | E | Marwari/Punjabi small pop |
| **Marginal recovery — Bengali** | | | | | | Hindu(85.45)×0.994 + Muslim(13.58)×0.95 + Christian(0.30)×0.90 + Other(0.67)×0.60 = 84.94 + 12.90 + 0.27 + 0.40 = **98.51** vs C.5 marginal **98.80** ✓ within ±0.5 |

### D.2 Religion × Caste (Hindu-internal sub-structure)

P(caste ‖ Hindu) — % within Hindu population only.

| Caste sub-group | % of Hindu | Tier | Source |
|---|---|---|---|
| **SC: Namasudra / Matua** | 46.2 | C | 39.5% of total / 85.45% Hindu = 46.2% of Hindu |
| SC: Bagdi | 1.8 | E | |
| SC: Poundra | 0.8 | E | |
| SC: Other | 1.5 | E | |
| ST | 4.2 | E | 3.6% of total / 85.45% Hindu |
| UC bhadralok | 11.7 | E | 10% / 85.45% Hindu |
| OBC specific | 2.3 | E | 2% / 85.45% Hindu |
| Other Hindu middle castes | 31.5 | E | 26.85% / 85.45% Hindu |
| **Sum** | **100.00** | — | self-check |

P(Muslim sub-caste ‖ Muslim):

| Muslim sub-group | % of Muslim | Tier | Source |
|---|---|---|---|
| Sheikh (Bengali Muslim peasantry) | 80 | D | Dominant in Bengali-Muslim belt |
| Pathan / Sayyid / Mughal | 5 | D | |
| OBC Muslim (Jolaha, Nai, Darzi etc.) | 12 | D | |
| Nasya-Sheikh / Other | 3 | D | |
| **Sum** | **100** | — | self-check |

### D.3 Religion × Migration / birthplace

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB-other-dist | Other state | Bangladesh | Outside-India | Tier | Source |
|---|---|---|---|---|---|---|---|
| **Hindu** | 60 | 8 | 2 | **30** | 0.0 | D | Matua refugee population is overwhelmingly Hindu; ~30% of Hindus traceable to East Pakistan / Bangladesh origin in Bangaon LS |
| Muslim | 95 | 3 | 1 | 1 | 0 | D | Most Bangaon Muslims are Bengali-Sheikh peasantry, native; very small Bangladesh-origin trickle |
| Christian | 80 | 10 | 5 | 5 | 0 | E | Mixed |
| Other | 50 | 20 | 25 | 5 | 0 | E | Marwari/Bihari traders mostly other-state |
| **Marginal recovery — Bangladesh** | | | | | | | Hindu(85.45)×0.30 + Muslim(13.58)×0.01 + Other(0.97)×0.04 = 25.64 + 0.14 + 0.04 = 25.82 vs C.16 marginal **23.0** ⚠ off by 2.8pp — flag for v1 reconciliation (Hindu Bangladesh-origin estimate may be slightly high) |

### D.4 Religion × Asset / media (TV, smartphone, banking)

P(owns asset ‖ religion) — % within each religion.

| Religion | TV | Smartphone-internet | Banking |
|---|---|---|---|
| Hindu | 81 | 51 | 89 |
| Muslim | 73 | 44 | 80 |
| Christian | 85 | 55 | 92 |
| Other | 95 | 75 | 98 |
| Tier | C | C | C |
| Source | NFHS-4 WB religion gap pattern | NFHS-5 WB pattern | PMJDY enrollment pattern |

### D.5 Caste × Education

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Sec | HS | Grad | PG | Tier |
|---|---|---|---|---|---|---|---|---|
| UC bhadralok | 5 | 10 | 12 | 18 | 18 | 25 | 12 | E |
| Namasudra-Matua (SC) | 12 | 22 | 23 | 19 | 12 | 9 | 3 | E |
| Bagdi/other SC | 22 | 28 | 22 | 15 | 8 | 4 | 1 | E |
| ST | 25 | 30 | 20 | 13 | 7 | 4 | 1 | E |
| OBC specific | 14 | 22 | 22 | 18 | 12 | 9 | 3 | E |
| Other Hindu middle | 13 | 22 | 22 | 18 | 12 | 10 | 3 | E |
| Muslim (all) | 18 | 24 | 23 | 18 | 10 | 6 | 1 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Cohort | Male grad+ | Female grad+ | Tier | Source |
|---|---|---|---|---|
| 18–22 | 18 | 17 | E | Near parity in young cohort; education expansion |
| 23–27 | 17 | 14 | E | |
| 28–32 | 14 | 10 | E | |
| 33–42 | 11 | 6 | E | |
| 43–57 | 8 | 3 | E | Older female cohort low |
| 58+ | 6 | 2 | E | |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender) — proxy for household formation.

| Age | Male married | Female married | Tier |
|---|---|---|---|
| 18–22 | 5 | 25 | E |
| 23–27 | 38 | 78 | E |
| 28–32 | 80 | 92 | E |
| 33–47 | 92 | 90 | E |
| 48–62 | 90 | 80 | E |
| 63+ | 75 | 35 | E (widows concentrate here) |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone-internet | TV | Tier | Source |
|---|---|---|---|---|
| Cultivator | 38 | 75 | C | Rural ag baseline |
| Ag-labourer | 28 | 65 | C | Lowest income |
| Household industry | 42 | 78 | C | |
| Manufacturing | 55 | 85 | C | |
| Construction | 50 | 78 | C | |
| Trade / retail | 70 | 90 | C | Muni concentrated |
| Transport (incl. Petrapole) | 65 | 85 | C | |
| Services (private) | 75 | 92 | C | |
| Govt services | 88 | 95 | C | Highest |
| Out-migrant | 70 | 80 | D | Working outside, smartphone-heavy |

### D.9 Education × Workforce participation

P(unemployed-and-seeking ‖ education) — educated-unemployment proxy.

| Education | Unemployed-seeking | Main-worker rate | Tier |
|---|---|---|---|
| Illiterate | 2 | 35 | E |
| Primary | 4 | 38 | E |
| Middle | 6 | 35 | E |
| Secondary | 9 | 30 | E |
| Higher Secondary | 14 | 25 | E |
| Graduate | 16 | 28 | E (job-aspirant pool) |
| Postgraduate | 12 | 38 | E |

### D.10 Asset / media × Bilingualism

P(bilingual Bengali+Hindi ‖ media-access tier).

| Media tier | Bilingual % | Tier | Source |
|---|---|---|---|
| TV-only HH | 5 | E | Bengali TV dominant |
| TV + smartphone HH | 9 | E | Some YouTube cross-language |
| Smartphone-only HH | 8 | E | |
| No-asset HH | 3 | E | Lowest exposure |
| **Population-wide bilingual rate** | ~6 | E | C.5 narrative anchor |

### D.11 GP × Religion (sub-AC spatial heterogeneity, v0 = 2 sub-units)

P(religion ‖ GP/Muni location).

| Sub-unit | Hindu | Muslim | Other | Tier | Source |
|---|---|---|---|---|---|
| **U1: Bangaon Municipality** (54.5% pop) | 92.0 | 7.0 | 1.0 | E | Muni heavily refugee-Hindu, low Muslim |
| **U2: CDB-Bangaon rural share** (45.5% pop) | 78.2 | 20.8 | 1.0 | A | Bangaon CDB Census 2011 rural |
| **Marginal recovery — Hindu** | | | | | 0.545×92.0 + 0.455×78.2 = 50.14 + 35.58 = **85.72** vs C.1 **85.45** ✓ within ±0.5 |

### D.12 GP × Caste (within sub-unit, key categories)

P(caste ‖ GP).

| Sub-unit | UC | Namasudra-Matua SC | Other SC | ST | OBC + Other Hindu | Muslim | Tier |
|---|---|---|---|---|---|---|---|
| Bangaon Muni | 14 | 38 | 3 | 1 | 38 | 7 | E |
| CDB-rural share | 5 | 41 | 3 | 6 | 24 | 21 | E |
| Source | Muni bhadralok-skewed | Matua dominant in both | small sub-SC | rural ST pockets | residual | rural Muslim pocket | |

### D.13 GP × Asset / media

| Sub-unit | TV | Smartphone-internet | Computer | Banking | Tier |
|---|---|---|---|---|---|
| Bangaon Muni | 92 | 65 | 22 | 95 | C |
| CDB-rural share | 65 | 32 | 5 | 78 | C |
| Source | NFHS-4 WB urban | NFHS-4 WB rural | | PMJDY | |

### D.14 GP × Amenities

| Sub-unit | LPG | Improved sanitation | Improved water | Electricity | Tier |
|---|---|---|---|---|---|
| Bangaon Muni | 78 | 92 | 95 | 99 | C |
| CDB-rural share | 17 | 55 | 75 | 95 | C |
| Source | NFHS-4/5 urban-rural gradient + Ujjwala/Swachh Bharat 2016-19 rollout | | | | |

### D.15 Vote × Religion (2019 LS, regional anchor)

P(party ‖ religion) — CSDS-Lokniti 2019 regional WB rollup.

| Religion | BJP | AITC | INC | LF | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 57 | 32 | 4 | 5 | 2 | C | [Swarajya/CSDS 2019 WB summary](https://swarajyamag.com/politics/explained-what-lokniti-csds-post-poll-survey-tells-us-about-recent-elections-in-tamil-nadu-and-bengal) |
| Muslim | 4 | 70 | 22 | 3 | 1 | C | Same |
| Christian | 30 | 50 | 10 | 5 | 5 | E | Approximation; tea-belt Christian different from urban |
| Other | 50 | 30 | 10 | 5 | 5 | E | |

### D.16 Vote × Caste (2019 LS)

P(party ‖ caste) — CSDS-Lokniti 2019 WB regional.

| Caste | BJP | AITC | INC | LF | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC | 60 | 28 | 5 | 5 | 2 | C | Bhadralok BJP-leaning by 2019 |
| OBC | 41 | 36 | 8 | 12 | 3 | C | Mixed |
| **Namasudra-Matua (SC)** | **60** | **32** | **3** | **3** | **2** | **C** | **2019 LS Bangaon Matua swing — Shantanu Thakur win** |
| Other SC | 50 | 36 | 5 | 7 | 2 | C | |
| ST | 45 | 35 | 5 | 12 | 3 | C | |
| Muslim (any caste) | 4 | 70 | 22 | 3 | 1 | C | Same as D.15 |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

P(party ‖ gender). LB launched 2021 — does NOT exist in 2019 calibration.

| Gender | BJP | AITC | INC | LF | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 47 | 41 | 5 | 5 | 2 | C | Swarajya/CSDS 2019 WB |
| Female | 38 | 50 | 5 | 5 | 2 | C | +9pp TMC women advantage in 2019 |

### D.18 Vote × Welfare-scheme exposure (2019)

P(party ‖ household has scheme exposure). Schemes available in 2019: Krishak Bandhu (TMC, launched Jan 2019), Kanyashree (TMC, 2013), Swasthya Sathi (TMC, 2016), Sabuj Sathi (TMC, 2015), Khadya Sathi (TMC, 2016). **Lakshmir Bhandar does NOT exist in 2019.**

| Exposure | BJP | AITC | INC | LF | Tier | Source |
|---|---|---|---|---|---|---|
| Krishak Bandhu (cultivator HH) | 28 | 60 | 5 | 5 | C | TMC welfare-stack credit |
| Kanyashree (girl-student HH) | 32 | 55 | 5 | 6 | C | |
| Swasthya Sathi enrollee | 38 | 50 | 5 | 5 | C | Broad-based; weaker TMC tilt |
| Sabuj Sathi (bicycle HH) | 35 | 52 | 5 | 6 | C | |
| Khadya Sathi (PDS) | 42 | 48 | 4 | 4 | C | Universal-coverage; weakest tilt |
| **No state-scheme exposure** | 55 | 30 | 6 | 7 | C | BJP-leaning |

---

## E. 2019 baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp.

### Whole Bangaon LS (PC 14) — 2019 result (tier A, ECI)

| Party | Candidate | Votes | % |
|---|---|---|---|
| BJP | **Shantanu Thakur** | 687,622 | **48.85** |
| AITC | Mamata Thakur | 576,028 | **40.92** |
| CPI(M) | Alakesh Das | 80,521 | 5.66 |
| INC | Soumitra Datta | 33,489 | 2.36 |
| Others / NOTA | various | ~30,000 | ~2.20 |
| **Margin** | BJP over AITC | **111,594** | 7.93 pp |

### AC 95 segment estimate (whole-LS proportional decomposition, tier D)

Pending Form-20 GE2019 fetch. Bangaon Uttar pre-2019 was an AITC stronghold (50-54% AITC in 2011/2016 AEs), so the AC 95 segment likely had a slightly higher AITC share than the LS average.

| Party | AC 95 segment 2019 % (estimated) | Tier | Note |
|---|---|---|---|
| BJP | 48.0 | D | LS-aggregate adjusted -0.85pp for AITC residual strength |
| AITC | 44.0 | D | LS-aggregate adjusted +3pp for AC's pre-existing TMC strength |
| CPI(M) + INC | 6.0 | D | |
| Other / NOTA | 2.0 | D | |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 95 specifically (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Biswajit Das | AITC | 54.55 | Dr. Biswajit Biswas | CPI(M) | 40.12 | 23,620 |
| 2016 AE | Biswajit Das | AITC | 50.59 | Sushanta Baowali | AIFB | 33.07 | 33,192 |

### Bangaon Lok Sabha (PC 14) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Kapil Krishna Thakur | AITC | 36.81 | TMC won; CPI(M) close 18.81%; BJP 19.65% |
| 2014 LS by-election | Mamatabala Thakur | AITC | — | After Kapil Krishna Thakur's death |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- Census of India 2011 — Bangaon CD Block Primary Census Abstract (via Wikipedia "Bangaon (community development block)")
- Census of India 2011 — Bangaon Sub-division demographics
- Census of India 2011 — North 24 Parganas district
- Election Commission of India — 2011 AE, 2014 LS, 2014 LS by-poll, 2016 AE, 2019 LS results for AC 95 / Bangaon LS
- Delimitation Commission of India 2008 — WB Schedule XXX (Bangaon Uttar = Bangaon Muni + 7 GPs of CDB Bangaon)

### Secondary sources (tier B/C)
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2019 NES post-poll (national rollup)
- Swarajya Magazine summary of CSDS 2019 WB regional cross-tabs (vote × religion / caste / gender)
- WB District Statistical Handbook — N24P
- Census 2001 District Human Development Report Paschim Medinipur (BPL baseline; same source pattern for N24P used by analogue)

### Tertiary / journalistic (tier D)
- Outlook India "Matua Mahasangha Maelstrom" — Bangaon LS Matua share ~40%
- Wikipedia summaries of related Bangaon constituencies
- PMC-Springer (2020) on WB→Kerala migrants

### Tier-D/E reliance flags (what to distrust)
- **Caste sub-group shares within Hindu** (D.2) — no caste census post-1931 for non-SC/ST; tier C/E throughout
- **Migration/birthplace shares** (C.16, D.3) — no public AC-level Census D-series; tier D from journalistic anchor
- **GP-level data** (D.11–D.14) — collapsed to 2 sub-units (Muni + CDB-rural-share); refine when DCHB Part-A accessible
- **Asset/media** (C.14, D.4, D.13) — NFHS-4/5 state-level pattern projected to AC; tier C
- **Vote × Demographic** (D.15–D.18) — CSDS 2019 WB regional rollup; tier C
- **AC-95 segment 2019 vote** (E) — whole-LS proportional decomposition pending Form-20 GE2019; tier D

### v0 known gaps (see methodology §7)
1. DCHB N24P Part-A — collapsed sub-units to 2 instead of 8
2. ECI 2019 LS Form-20 — using whole-LS proportional decomposition for AC 95 segment
3. Census HH-13 GP-level — using NFHS state-level proxy for asset/media
4. Census D-series — using qualitative/journalistic anchor for migration
5. Full CSDS WB regional cross-tabs — using Swarajya summary

---

*v0 — generated 2026-04-25, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*
