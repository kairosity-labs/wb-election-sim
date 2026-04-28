# AC 143 — Diamond Harbour (General) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural state of AC 143 Diamond Harbour as of 2019 only — it does not reference any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 143 | A | ECI / Delimitation Commission 2008 |
| AC name | Diamond Harbour | A | ECI |
| Reservation | General (Unreserved) | A | Delimitation 2008 |
| District | South 24 Parganas | A | Delimitation 2008 |
| Sub-division | Diamond Harbour | A | WB administrative |
| LS constituency | PC 20 — Diamond Harbour | A | Delimitation 2008 |
| LS segments included with PC 20 | AC 143 Diamond Harbour · 144 Falta · 145 Satgachhia · 146 Bishnupur (SC) · 147 Maheshtala · 148 Budge Budge · 149 Metiaburuz | A | Delimitation 2008 / Wikipedia |
| AC composition | Diamond Harbour Municipality (full) + 7 of 8 GPs of CDB Diamond Harbour I (Basuldanga, Bolsiddhi Kalinagar, Derak, Harindanga, Kanpur Dhanaberia, Mashat, Parulia) + 6 of 8 GPs of CDB Diamond Harbour II (Kamarpole, Khorda, Mathur, Nurpur, Patra, Sarisa) | A | Delimitation 2008 / Wikipedia "Diamond Harbour (Vidhan Sabha constituency)" |
| Geographic note | Hugli (Hooghly) river estuary; Diamond Harbour town on east bank of Hugli ~50 km south of Kolkata; river-dependent economy (fishing, ferries, port); Sundarban-fringe ecology to the south | A | — |
| Archetype | A6 — South Bengal TMC heartland; Abhishek Banerjee's LS bastion; candidate-effect differential key | D | Project classification |
| Two primary CDBs contributing to AC | **CDB-I**: Diamond Harbour I (HQ Diamond Harbour town) · **CDB-II**: Diamond Harbour II (HQ Sarisha) | A | Wikipedia CDB articles |
| Three sub-units used in v0 | **U1: Diamond Harbour Municipality** (urban) · **U2: CDB-I rural GP share** (7 of 8 GPs) · **U3: CDB-II rural GP share** (6 of 8 GPs) | E | v0 simplification — see methodology §3 |

---

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~299,423 (Municipality 41,802 + CDB-I rural 7/8 share 118,265 + CDB-II rural 6/8 share 139,356) | E | Census 2011 Wikipedia CDB articles; v0 GP-equal-weight assumption |
| 2019 projected population | ~327,000 | E | 8-yr compound religion-differential growth (methodology §4); net ~9.2% over 2011 base |
| Sex ratio (2019, F per 1000 M) | ~959 | E | Weighted from Census 2011: Muni 986 + CDB-I 957 + CDB-II 953; minimal projection drift |
| 2019 estimated electorate (18+) | 241,842 | A | `2019_AssemblySegmentLevelVotingData.csv` (TOTAL ELECTORS column, AC_NO=143) |
| 2019 polling stations (estimated) | ~260 | E | Back-derived from 2021 AE turnout pattern; Census CDB station density |
| Estimated M / F / TG split (2019) | ~51.0% M / 49.0% F / <0.05% TG | E | 2011 sex ratio 959 (A) → F/M+F = 959/1959 = 48.95% F; TG from WB state rate |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

**Key finding**: AC 143 is one of the more Muslim-majority ACs in South 24 Parganas. CDB-I has 52% Muslim; CDB-II has 40% Muslim; the municipality is ~14% Muslim. Weighted AC total is markedly different from the district average.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 58.11 | B | Weighted 2011 data: Muni 85.98% + CDB-I 47.72% + CDB-II 59.77%; projected 2011→2019 with Hindu +1.0%/yr (Pew India 2021) |
| Muslim | 41.57 | B | Weighted 2011 data: Muni 13.75% + CDB-I 52.16% + CDB-II 39.68%; projected Muslim +1.3%/yr |
| Christian | 0.20 | E | South 24P fringe; CDB data shows negligible Christian |
| Other (Sikh / Jain / Buddhist / Sarna) | 0.12 | E | CDB-II "Others" 0.55%; CDB-I 0.12%; weighted down at AC level |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC total** | 21.46 | B | Weighted from Census 2011: Muni 12.49% + CDB-I 18.63% + CDB-II 26.55%; GP-equal-weight assumption within each CDB |
| └ Namasudra / Bagdi | 9.0 | D | South 24P coastal SC: Namasudra (fishers/farmers), Bagdi (agricultural labourers) are primary SC communities; Namasudra dominant in river-delta belt |
| └ Munda / other SC | 3.0 | E | Munda and other SC in CDB-II rural pockets |
| └ Scheduled Caste unclassified | 9.46 | E | Residual within SC total |
| **ST total** | 0.05 | A | Census 2011 CDB-I ST 0.01%; CDB-II ST 0.04%; weighted AC ~0.05% (negligible) |
| **Upper-caste bhadralok** (Brahmin / Kayastha / Baidya) | 5.0 | E | Concentrated in Diamond Harbour Municipality; smaller presence than North 24P border ACs |
| **OBC specific** (Mahishya / Sadgop / Teli / Kurmi) | 6.0 | E | Mahishya fishing caste historically significant in Hugli delta areas; Sadgop farming OBC |
| **Other Hindu middle castes** (Goala / Pod / Sutradhar / Kaibarta / unclassified Hindu) | 25.60 | E | Residual within Hindu (58.11 − 21.46 SC − 0.05 ST − 5.0 UC − 6.0 OBC = 25.60% other Hindu middle castes; Kaibarta fishing caste significant in Hugli delta) |
| **Muslim (all sub-castes pooled)** | 41.57 | B | See C.1; sub-structure in joint table D.2 |
| Christian + Other | 0.32 | E | See C.1 |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 0–4 | 8.0 | E | Projected from S24P district Census 2011 age pyramid; higher fertility in Muslim-majority rural CDB-I |
| 5–9 | 8.5 | E | |
| 10–14 | 8.5 | E | |
| 15–17 (pre-voter) | 5.5 | E | |
| 18–22 (first-time voters at 2019) | 9.0 | E | |
| 23–27 | 9.5 | E | |
| 28–32 | 9.0 | E | |
| 33–37 | 8.0 | E | |
| 38–42 | 7.5 | E | |
| 43–47 | 6.5 | E | |
| 48–52 | 6.0 | E | |
| 53–57 | 5.0 | E | |
| 58–62 | 3.5 | E | |
| 63–67 | 2.5 | E | |
| 68+ | 3.0 | E | Slightly higher 68+ vs N24P (S24P older rural cohort) |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.06 | E | Sex ratio 959 → F/total = 959/1959 = 48.95%; M = 51.05% — rounded to 51.06 for sum |
| Female | 48.93 | E | |
| Third gender | 0.01 | E | WB state rate from 2011 Census |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 99.44 | A | CDB-I 99.83% Bengali (A); CDB-II 99.7% Bengali (A); Muni ~98.5% Bengali (E); weighted AC ~99.4% |
| Urdu | 0.30 | E | Small Muslim Urdu-speaker pocket in municipality and CDB-II; CDB data shows 0.02% Urdu — slightly higher in urban fraction |
| Hindi | 0.20 | E | CDB-I 0.14%, CDB-II 0.32%; Muni trader/migrant Hindi fringe |
| Other | 0.06 | E | Residual |
| **Sum** | **100.00** | — | self-check |

(Bilingualism flag: ~3% of population is Bengali+Urdu or Bengali+Hindi bilingual; AC is more Bengali-monolingual than North 24P ACs; tier E.)

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 20.5 | E | AC 2011 literacy weighted 77.70% (B); age-7+ base → illiteracy ~22.3%; improve +1pp/yr for 8 yrs → ~20.5% illiterate by 2019 |
| Primary (Class 1–5) | 25.0 | E | Census 2011 S24P education distribution scaled |
| Middle (Class 6–8) | 22.0 | E | |
| Secondary (Class 9–10) | 16.0 | E | |
| Higher Secondary (Class 11–12) | 9.5 | E | |
| Graduate | 5.5 | E | Lower than North 24P; rural-delta deprivation |
| Postgraduate | 1.5 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main worker | 30.0 | E | CDB-I+II combined main-worker share; lower female workforce participation |
| Marginal worker | 13.0 | E | Higher marginal worker share than N24P due to fishing seasonality |
| Non-worker (housewife / elderly / retired) | 38.0 | E | Heavy female non-worker share in Muslim-majority rural blocks |
| Student (18–22 only, in education) | 11.0 | E | |
| Unemployed (educated, actively seeking) | 8.0 | E | Job-aspirant pool concentrated in Muni and educated CDB-II youth |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator (own-land) | 6.5 | B | Census 2011 CDB-I 6.87% + CDB-II 7.27%; Muni minimal ~2%; AC weighted ~6.5% by 2019 |
| Agricultural labourer | 19.0 | B | Census 2011 CDB-I 22.32% + CDB-II 21.69%; Muni dilution; AC weighted ~19% |
| Fishing / pisciculture | 12.0 | D | River-delta economy: Hugli tidal fishing, prawn cultivation, brackish-water aquaculture; S24P has >4.5L pisciculture workers (2001 state data); Coastal Frontiers blog; Namasudra + Mahishya caste occupational pattern |
| Household industry (mat-weaving, coir, bidi) | 6.5 | B | Census 2011 CDB-I 7.22% + CDB-II 6.24%; weighted ~6.5% |
| Construction | 5.0 | E | Includes seasonal out-migrant returnees |
| Trade / retail | 11.0 | E | Diamond Harbour Muni commercial hub; river-trade |
| Transport (ferry / road / river) | 7.0 | D | River ferry economy significant; Hugli crossings; auto-rickshaw |
| Services (private) | 10.0 | E | |
| Government services / teachers | 6.0 | E | Slightly higher than N24P rural average due to subdivisional HQ |
| Out-migrant (registered here, working outside) | 13.0 | D | South 24P out-migration for fishing labour (deep-sea), Kolkata daily commuters, construction migrant workers; S24P district MIS + journalistic; higher than N24P due to deep-sea fishing seasonal absence |
| Tourism / hospitality | 2.0 | D | Diamond Harbour waterfront tourism (Kolkata day-trip destination) |
| Manufacturing / other organised | 2.0 | E | Small-scale factory and organised sector in Muni fringe |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.5 | E | Census B-04 WB rural pattern; lower in fishing-dependent AC |
| Employee (regular wage) | 24.0 | E | Govt + organised + services employees |
| Single worker / own-account | 52.0 | E | Fishermen (own boat/net), cultivator-owners, small traders |
| Family worker (unpaid) | 22.5 | E | Fishing household family helpers; female family workers in cultivation |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL household | 28.0 | D | S24P district BPL share historically ~30%; river-delta ACs with fishery dependence and Muslim-majority rural blocks have above-district BPL rates; ~28% projected 2019 |
| Above-Poverty-Line, low-income | 36.0 | E | |
| Lower-middle | 22.0 | E | |
| Middle | 11.0 | E | |
| Upper-middle / well-off | 3.0 | E | Diamond Harbour Muni small affluent/service-class fringe |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Municipality location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **U1: Diamond Harbour Municipality** (urban) | 13.9 | E | 2011 Muni 41,802 / AC total ~299,423 = 13.97%; projected slightly declining share as rural grows faster |
| **U2: CDB-I rural GP share** (7 of 8 GPs of CDB Diamond Harbour I) | 39.5 | E | 118,265 / 299,423 = 39.5%; Note: CDB-I is Muslim-majority (52% Muslim) — this is the load-bearing heterogeneity cell |
| **U3: CDB-II rural GP share** (6 of 8 GPs of CDB Diamond Harbour II) | 46.6 | E | 139,356 / 299,423 = 46.5%; CDB-II Hindu majority (60% Hindu) but with 40% Muslim; Sarisa, Nurpur, Khorda, Mathur, Patra, Kamarpole GPs |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg HH size | 4.5 persons | E | S24P 2011: HH size ~4.5 (higher than state avg of 4.3 due to rural Muslim HH); Muni closer to 4.2 (10,048 HH / 41,802 pop = 4.16 — A) |
| Nuclear HH | 65.0 | E | NFHS-4 WB rural pattern; slightly lower nuclear in Muslim-dominant CDB-I |
| Joint HH | 26.0 | E | |
| Extended / multi-generation | 9.0 | E | Higher than N24P due to fishing economy household structure |
| **Sum** | **100.00** | — | self-check |

(Household head: ~87% male-headed, 13% female-headed; tier E from S24P pattern; higher female-headed in fishing households with seasonal male absence.)

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never married | 25.0 | E | Census 2011 S24P pattern; slightly lower than N24P due to younger marriage age in rural Muslim communities |
| Currently married | 66.0 | E | |
| Widowed | 8.0 | E | Concentrated in 60+; higher widow share in fishing families (occupational hazard) |
| Separated / divorced | 1.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 72.0 | C | NFHS-4 WB rural ~60%, urban 89%; AC weighted ~66% baseline + growth; Muslim-majority CDB-I slightly lower → ~72% AC |
| Radio | 5.0 | C | Declining nationally |
| Mobile phone (any) | 85.0 | C | NFHS-4 WB ~78%; +growth via Jio 2016-19 → ~85% by 2019; slightly lower than N24P due to rural depth |
| Smartphone with internet | 42.0 | C | NFHS-4 baseline + Jio rollout 2016-19; Muslim-majority rural CDB-I dampens to ~42% AC weighted |
| Computer | 8.0 | C | NFHS-4 WB rural 4%, urban 27%; AC weighted lower than N24P (no Petrapole port bonus) |
| Two-wheeler | 25.0 | C | NFHS-4 WB rural 18%, urban 41%; lower than N24P — boat/ferry more salient than bike in delta |
| Four-wheeler | 5.0 | C | Limited |
| Banking access (any) | 82.0 | B | PMJDY 2014- saturation; S24P lower banking density than N24P historically; ~82% by 2019 |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved drinking water source | 82.0 | C | NFHS-4 WB rural 84%, urban 93%; AC slightly lower due to riverine geography (well + river water common) |
| Improved sanitation (latrine) | 65.0 | C | NFHS-4 WB rural 51%, urban 84%; +Swachh Bharat 2014-19 (+12pp rural); Muslim-majority CDB-I slightly lower uptake |
| LPG / clean cooking fuel | 42.0 | C | NFHS-4 WB rural 24%, urban 81%; +Ujjwala 2016-19 (+14pp rural); lower than N24P — fishing economy uses wood/coal more |
| Wood / biomass fuel | 50.0 | C | Higher biomass than N24P due to delta mangrove-fringe firewood access |
| Other fuel (kerosene, dung, etc.) | 8.0 | C | |
| Electricity | 92.0 | C | Census 2011 + Saubhagya 2017-19; slightly lower than N24P rural (~95%) due to delta geography connectivity gap |
| **Note** | (cooking-fuel rows sum to 100; water/sanitation/electricity are independent %s) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native (born in S24P or same village/town) | 80.0 | D | Diamond Harbour sub-division is predominantly native-rooted; Muslim peasantry is indigenous to this riverine delta; unlike N24P border ACs, there is minimal refugee-resettlement stream |
| WB other district (in-migrant) | 6.0 | D | Kolkata suburb commuter class in Muni; some Kolkata-overspill in CDB-II |
| Other Indian state | 2.0 | D | Marwari/Bihari trader fringe in Muni; construction migrant workers |
| Bangladesh-origin (migrant Hindu, small stream) | 3.0 | D | Much smaller Bangladesh-origin fraction than N24P border ACs; mainly pre-1971 Namasudra fraction in CDB-II; no Matua concentration |
| Outside India (other than Bangladesh) | 0.5 | E | Negligible |
| **Seasonal out-migrant (registered here, currently absent)** | 8.5 | D | **Load-bearing**: significant seasonal fishing-labour out-migration from S24P coast (deep-sea fishing boats, Kolkata daily commuters, construction migrants); registered voter but seasonally absent — affects actual polling booth presence |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Urdu | Hindi | Other | Tier | Source |
|---|---|---|---|---|---|---|
| Hindu | 99.7 | 0.0 | 0.2 | 0.1 | A | CDB-I+II 99.83%/99.7% Bengali overall; Hindu fringe Hindi-traders in Muni |
| Muslim | 98.5 | 0.9 | 0.5 | 0.1 | E | Bengali-Muslim (Sheikh) peasantry overwhelmingly Bengali-speaking; small Urdu pocket in Muni |
| Christian | 92.0 | 0.0 | 5.0 | 3.0 | E | Tiny base |
| Other | 70.0 | 0.0 | 25.0 | 5.0 | E | Marwari/Bihari traders |
| **Marginal recovery — Bengali** | | | | | | Hindu(58.11)×0.997 + Muslim(41.57)×0.985 + Christian(0.20)×0.92 + Other(0.12)×0.70 = 57.94 + 40.95 + 0.18 + 0.08 = **99.15** vs C.5 marginal **99.44** — within ±0.5 ✓ |

### D.2 Religion × Caste (Hindu-internal sub-structure)

P(caste ‖ Hindu) — % within Hindu population only (58.11% of AC).

| Caste sub-group | % of Hindu | Tier | Source |
|---|---|---|---|
| **SC: Namasudra / Bagdi (river-delta fishing/farming SC)** | 15.5 | D | 9.0% of AC total / 58.11% Hindu = 15.5% of Hindu pop; Namasudra+Bagdi are riverine SC in S24P delta — smaller Matua refugee stream than N24P |
| SC: Munda / other SC | 5.2 | E | 3.0% of AC / 58.11% |
| SC: Unclassified remainder | 16.3 | E | Residual: AC SC total 21.46% - 12.0% named = 9.46%; / 58.11% = 16.3% |
| ST | 0.1 | A | Negligible — 0.05% total / 58.11% Hindu |
| UC bhadralok (Brahmin/Kayastha/Baidya) | 8.6 | E | 5.0% / 58.11% |
| OBC specific (Mahishya / Sadgop) | 10.3 | E | 6.0% / 58.11%; Mahishya and Sadgop are salient OBC in S24P fishing + farming belt |
| Other Hindu middle castes (Pod, Goala, Sutradhar, etc.) | 44.0 | E | Residual: 100 − 15.5 − 5.2 − 16.3 − 0.1 − 8.6 − 10.3 = 44.0 |
| **Sum** | **100.00** | — | self-check |

P(Muslim sub-caste ‖ Muslim):

| Muslim sub-group | % of Muslim | Tier | Source |
|---|---|---|---|
| Sheikh (Bengali Muslim peasantry) | 85 | D | Dominant in Bengali-Muslim riverine delta — CDB-I and CDB-II Muslim majority is largely Bengali-Sheikh peasantry |
| OBC Muslim (Jolaha, Nai, Darzi, Mochi) | 10 | D | Artisan and service-caste Muslim presence |
| Pathan / Sayyid / Mughal | 3 | D | Small elite fringe in Muni |
| Nasya-Sheikh / Other | 2 | D | |
| **Sum** | **100** | — | self-check |

### D.3 Religion × Migration / birthplace

P(birthplace ‖ religion) — % within each religion.

| Religion | Native S24P | WB-other-dist | Other state | Bangladesh-origin | Out-migrant | Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| **Hindu** | 77 | 7 | 2 | 5 | 8 | 1 | D | Hindu SC population includes small Namasudra Bangladesh-origin fraction (smaller than Bangaon); Mahishya + Sadgop are indigenous S24P; significant seasonal fishing out-migration |
| **Muslim** | 85 | 4 | 1 | 1 | 9 | 0 | D | Bengali-Sheikh Muslim is indigenous S24P peasantry; Bangladesh-origin negligible; seasonal out-migration for fishing/labour |
| Christian | 80 | 10 | 5 | 5 | 0 | 0 | E | |
| Other | 50 | 15 | 30 | 5 | 0 | 0 | E | Marwari/Bihari traders |
| **Marginal recovery — Bangladesh-origin** | | | | | | | | Hindu(58.11)×0.05 + Muslim(41.57)×0.01 = 2.91 + 0.42 = **3.33** vs C.16 marginal **3.0** ✓ within ±0.5 |

### D.4 Religion × Asset / media (TV, smartphone, banking)

P(owns asset ‖ religion) — % within each religion.

| Religion | TV | Smartphone-internet | Banking | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 76 | 47 | 87 | C | NFHS-4 WB religion pattern; S24P Hindu in Muni and CDB-II |
| Muslim | 66 | 35 | 75 | C | NFHS-4 WB Muslim rural gap; CDB-I Muslim-majority rural block lower asset |
| Christian | 82 | 55 | 90 | E | Small base |
| Other | 90 | 70 | 95 | E | Trader class |

### D.5 Caste × Education

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Sec | HS | Grad | PG | Tier |
|---|---|---|---|---|---|---|---|---|
| UC bhadralok | 4 | 10 | 12 | 18 | 20 | 26 | 10 | E |
| Mahishya / Sadgop OBC | 12 | 22 | 23 | 20 | 12 | 9 | 2 | E |
| Namasudra / Bagdi SC | 20 | 26 | 24 | 16 | 8 | 5 | 1 | E |
| Other SC | 25 | 28 | 22 | 14 | 7 | 3 | 1 | E |
| Muslim (all) | 24 | 27 | 24 | 15 | 7 | 3 | 0.5 | E |
| Other Hindu middle | 15 | 24 | 23 | 18 | 11 | 7 | 2 | E |

(Muslim literacy gap in CDB-I is notable — female literacy in CDB-I 70.06% (A). The Illiterate row for Muslim is higher than N24P baseline, reflecting CDB-I rural Muslim communities with lower schooling completion rates among women over 40.)

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Cohort | Male grad+ | Female grad+ | Tier | Source |
|---|---|---|---|---|
| 18–22 | 12 | 10 | E | Lower than N24P; S24P delta deprivation; expanding but slower |
| 23–27 | 13 | 9 | E | |
| 28–32 | 10 | 6 | E | |
| 33–42 | 8 | 3 | E | |
| 43–57 | 5 | 1 | E | Older female cohort very low — S24P rural Muslim communities |
| 58+ | 4 | 1 | E | |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender).

| Age | Male married | Female married | Tier |
|---|---|---|---|
| 18–22 | 8 | 35 | E |
| 23–27 | 45 | 85 | E |
| 28–32 | 83 | 92 | E |
| 33–47 | 93 | 90 | E |
| 48–62 | 91 | 78 | E |
| 63+ | 75 | 30 | E (widows concentrate; fishing hazard; higher widow share) |

(Note: Higher female marriage rate at 18–22 vs N24P reflects earlier marriage norms in rural Muslim-majority CDB-I. This is a pre-2019 frozen observation.)

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone-internet | TV | Tier | Source |
|---|---|---|---|---|
| Cultivator | 30 | 68 | C | Rural ag; delta region; lower than N24P cultivators |
| Ag-labourer | 22 | 58 | C | Lowest income bracket |
| Fisher / pisciculture | 35 | 65 | D | Working-boat fishermen carry phones for communication; seasonally high usage |
| Household industry | 38 | 70 | C | |
| Construction | 45 | 72 | C | |
| Trade / retail | 65 | 88 | C | Muni concentrated |
| Transport (river/ferry) | 55 | 78 | D | |
| Services (private) | 72 | 90 | C | |
| Govt services | 85 | 95 | C | Highest |
| Out-migrant | 68 | 75 | D | Working outside; smartphone for remittances |
| Tourism / hospitality | 62 | 88 | D | Muni hotel/ghat economy |

### D.9 Education × Workforce participation

P(unemployed-and-seeking ‖ education) — educated-unemployment proxy.

| Education | Unemployed-seeking | Main-worker rate | Tier |
|---|---|---|---|
| Illiterate | 1 | 32 | E |
| Primary | 3 | 35 | E |
| Middle | 5 | 32 | E |
| Secondary | 8 | 28 | E |
| Higher Secondary | 13 | 22 | E |
| Graduate | 15 | 25 | E (job-aspirant pool) |
| Postgraduate | 10 | 35 | E |

### D.10 Asset / media × Bilingualism

P(bilingual Bengali+Hindi or Bengali+Urdu ‖ media-access tier).

| Media tier | Bilingual % | Tier | Source |
|---|---|---|---|
| TV-only HH | 2 | E | Bengali TV overwhelmingly dominant |
| TV + smartphone HH | 5 | E | Some YouTube cross-language |
| Smartphone-only HH | 4 | E | |
| No-asset HH | 1 | E | |
| **Population-wide bilingual rate** | ~3 | E | C.5 anchor: ~0.5% Urdu + 0.2% Hindi = ~0.7% primary non-Bengali; bilingual pool ~3× that |

### D.11 GP / Sub-unit × Religion

P(religion ‖ sub-unit location).

| Sub-unit | Hindu | Muslim | Other | Tier | Source |
|---|---|---|---|---|---|
| **U1: Diamond Harbour Municipality** (13.9% pop) | 85.98 | 13.75 | 0.27 | A | Census 2011 Municipality Wikipedia |
| **U2: CDB-I rural GP share** (39.5% pop) | 47.72 | 52.16 | 0.12 | A | Census 2011 CDB-I Wikipedia (Muslim-majority) |
| **U3: CDB-II rural GP share** (46.6% pop) | 59.77 | 39.68 | 0.55 | A | Census 2011 CDB-II Wikipedia |
| **Marginal recovery — Hindu** | | | | | 0.139×85.98 + 0.395×47.72 + 0.466×59.77 = 11.95 + 18.85 + 27.85 = **58.65** vs C.1 **58.11** — within ±0.6 (post-projection drift acceptable) ✓ |
| **Marginal recovery — Muslim** | | | | | 0.139×13.75 + 0.395×52.16 + 0.466×39.68 = 1.91 + 20.60 + 18.49 = **41.00** vs C.1 **41.57** — within ±0.6 ✓ |

### D.12 GP / Sub-unit × Caste (within sub-unit, key categories)

P(caste ‖ sub-unit).

| Sub-unit | UC | SC (all) | ST | OBC+Mahishya | Muslim | Other Hindu | Tier |
|---|---|---|---|---|---|---|---|
| Muni (U1) | 8 | 12.49 | 0.17 | 7 | 13.75 | 58.6 | B/A |
| CDB-I rural (U2) | 2 | 18.63 | 0.01 | 5 | 52.16 | 22.2 | B/A |
| CDB-II rural (U3) | 4 | 26.55 | 0.04 | 7 | 39.68 | 22.7 | B/A |
| Source | Muni bhadralok concentration | Census 2011 SC data (A) | negligible ST | Mahishya/Sadgop fishing+farming OBC | CDB-I majority Muslim | residual | |

### D.13 GP / Sub-unit × Asset / media

| Sub-unit | TV | Smartphone-internet | Computer | Banking | Tier |
|---|---|---|---|---|---|
| Muni (U1) | 88 | 60 | 18 | 92 | C |
| CDB-I rural (U2) | 63 | 32 | 4 | 73 | C |
| CDB-II rural (U3) | 70 | 38 | 5 | 80 | C |
| Source | NFHS-4 WB urban/rural gradient | Jio rollout pace differential | | PMJDY; lower S24P rural rate than N24P | |

### D.14 GP / Sub-unit × Amenities

| Sub-unit | LPG | Improved sanitation | Improved water | Electricity | Tier |
|---|---|---|---|---|---|
| Muni (U1) | 72 | 88 | 93 | 97 | C |
| CDB-I rural (U2) | 30 | 55 | 78 | 88 | C |
| CDB-II rural (U3) | 38 | 62 | 80 | 90 | C |
| Source | NFHS-4/5 urban-rural + Ujjwala/Swachh Bharat 2016-19 rollout; CDB-I lower uptake due to Muslim-majority rural bloc | | | Saubhagya less complete in riverine delta | |

### D.15 Vote × Religion (2019 LS, AC 143 regional anchor)

P(party ‖ religion) — calibrated to AC 143 segment result (AITC 52.86%, BJP 35.69%, CPI(M) 8.19%); religion weights: Hindu 58.11%, Muslim 41.57%.

| Religion | BJP | AITC | CPI(M)+LF | INC | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 58 | 31 | 8 | 1 | 2 | C | CSDS-Lokniti 2019 WB; Bangaon comparator; S24P Hindu leans BJP in 2019 LS wave |
| Muslim | 2 | 82 | 12 | 2 | 2 | C | Muslim bloc-vote TMC in S24P; significant CPI(M) Muslim residual in this AC (higher than state avg given 2016 result history) |
| Other | 40 | 45 | 5 | 5 | 5 | E | Small base; mixed |
| **Recovery check** | 58×0.5811+2×0.4157 = 33.71+0.83 = **34.54%** BJP | 31×0.5811+82×0.4157 = 18.01+34.09 = **52.10%** AITC | 8×0.5811+12×0.4157 = **9.64%** LF | — | — | — | Recovers: BJP 34.5% (vs CSV 35.69%, Δ=1.2pp); AITC 52.1% (vs CSV 52.86%, Δ=0.8pp) — within ±2pp ✓ |

### D.16 Vote × Caste (2019 LS, AC 143)

P(party ‖ caste) — CSDS-Lokniti 2019 WB regional, adjusted for AC context.

| Caste | BJP | AITC | CPI(M)+LF | INC | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC bhadralok | 58 | 27 | 10 | 3 | 2 | C | BJP-leaning UC in 2019 |
| OBC (Mahishya/Sadgop) | 45 | 38 | 12 | 3 | 2 | C | Mahishya fishing OBC: somewhat BJP-leaning in 2019; historically LF in S24P |
| SC (Namasudra/Bagdi — delta type) | 52 | 35 | 10 | 2 | 1 | C | S24P SC leans BJP in 2019; smaller Matua-refugee BJP push than Bangaon but still BJP |
| Other Hindu middle | 50 | 35 | 10 | 3 | 2 | C | |
| Muslim (all sub-castes) | 2 | 82 | 12 | 2 | 2 | C | Near-unanimous TMC |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

P(party ‖ gender). Lakshmir Bhandar does NOT exist in 2019 calibration — this is the pre-LB gender-vote baseline the simulator uses to detect post-LB shift.

| Gender | BJP | AITC | CPI(M)+LF | INC | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 40 | 47 | 10 | 2 | 1 | C | CSDS 2019 WB; male slightly more BJP; TMC still leads male |
| Female | 30 | 59 | 8 | 2 | 1 | C | +12pp TMC women advantage in 2019; pre-LB already strong female TMC lean in S24P |

(Note: The female TMC tilt is notably stronger in S24P than in N24P, reflecting different welfare-scheme salience — Kanyashree and Swasthya Sathi are more penetrative in Muslim-majority rural areas with healthcare gaps. The pre-LB female TMC lean here is modelled as the 2019 baseline.)

### D.18 Vote × Welfare-scheme exposure (2019)

P(party ‖ household has scheme exposure). Schemes available in 2019: Krishak Bandhu (TMC, Jan 2019), Kanyashree (TMC, 2013), Swasthya Sathi (TMC, 2016), Sabuj Sathi (TMC, 2015), Khadya Sathi (TMC, 2016). **Lakshmir Bhandar does NOT exist in 2019.**

| Exposure | BJP | AITC | CPI(M)+LF | INC | Tier | Source |
|---|---|---|---|---|---|---|
| Krishak Bandhu (cultivator HH) | 30 | 55 | 12 | 2 | C | TMC welfare credit; CPI(M) residual higher here than Bangaon |
| Kanyashree (girl-student HH) | 25 | 62 | 10 | 2 | C | Strong TMC tilt; female welfare reach into Muslim communities |
| Swasthya Sathi enrollee | 35 | 52 | 10 | 2 | C | Broad-based; higher Muslim uptake due to healthcare gap |
| Sabuj Sathi (bicycle HH) | 28 | 58 | 11 | 2 | C | |
| Khadya Sathi (PDS) | 40 | 46 | 10 | 3 | C | Universal-coverage; weakest TMC tilt |
| **No state-scheme exposure** | 52 | 33 | 11 | 3 | C | BJP-leaning but lower than N24P |

---

## E. 2019 baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp.

### Whole Diamond Harbour LS (PC 20) — 2019 result (tier A, ECI)

| Party | Candidate | Votes | % |
|---|---|---|---|
| AITC | **Abhishek Banerjee** | 791,127 | **~56.15** |
| BJP | Nilanjan Roy | 470,533 | **~33.44** |
| CPI(M) | Dr. Fuad Halim | ~125,000 est. | **~8.9** |
| Others / NOTA | various | — | ~1.5 |
| **Margin** | AITC over BJP | **320,594** | ~22.7 pp |

Source: Wikipedia "Diamond Harbour Lok Sabha constituency" (tier A); exact CPI(M) + minor party figures pending Form-20.

### AC 143 segment — 2019 LS result (tier A, CSV)

> Figures are **tier A** — sourced directly from `/home/ubuntu/wb-election-sim/2019_AssemblySegmentLevelVotingData.csv`, AC_NO=143, Diamond Harbour. Total electors: 241,842; total valid votes incl. NOTA: 206,451; turnout: **85.4%**.

| Party | Candidate | Votes | AC-143 segment % | Tier | Source |
|---|---|---|---|---|---|
| AITC | Abhishek Banerjee | 109,134 | **52.86%** | A | `2019_AssemblySegmentLevelVotingData.csv` |
| BJP | Nilanjan Roy | 73,673 | **35.69%** | A | Same |
| CPI(M) | Dr. Fuad Halim | 16,904 | **8.19%** | A | Same |
| INC | Soumya Aich Roy | 2,046 | **0.99%** | A | Same |
| NOTA | — | 2,202 | **1.07%** | A | Same (NOTA column) |
| Others (BSP, SUCI, SHS, BNARP, IND×2) | various | 2,492 | **1.21%** | A | Same |
| **AITC margin over BJP** | | **35,461 votes** | **17.18 pp** | A | Computed from CSV |

**Calibration note**: AITC wins this AC segment comfortably at 52.86%. This is substantially below the LS-whole-PC share (~56%) due to constituency-level heterogeneity. The AC 143 Hindu share (~58%) and BJP's Hindu consolidation produces a BJP floor of ~36% — higher than in other Diamond Harbour LS ACs with higher Muslim share. The CPI(M) retains 8.2% reflecting legacy LF strength in this specific AC (Dipak Kumar Halder won for AITC only in 2011, displacing CPI(M); CPI(M) was 40%+ in 2011 AE).

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 143 specifically (Assembly Elections)

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin | Tier |
|---|---|---|---|---|---|---|---|---|---|---|
| 2006 AE | Rishi Halder | CPI(M) | — | — | Subhashis Chakraborty | AITC | — | — | — | D |
| 2011 AE | Dipak Kumar Halder | AITC | 87,645 | **53.37** | Subhra Sau | CPI(M) | 66,871 | **40.72** | 20,774 | A |
| 2016 AE | Dipak Kumar Halder | AITC | 96,833 | **48.58** | Abul Hasnat | CPI(M) | 81,796 | **41.03** | 15,037 | A |

**Key pattern**: CPI(M) retained >40% vote share as recently as 2016 in this AC — among the highest CPI(M) AE residuals in South Bengal. This reflects: (a) organised Left-leaning Muslim voter base in CDB-I; (b) Abul Hasnat as a strong CPI(M) candidate with Muslim community linkage; (c) relatively late TMC consolidation in this delta AC compared to Kolkata-adjacent seats. BJP was marginal in 2011 (~3%) and 2016 (~7%), making the 2019 LS swing to 35.69% a dramatic three-election arc.

### Diamond Harbour Lok Sabha (PC 20) historical

| Year | Winner | Party | Votes | % | Runner-up | Party | % | Notes | Tier |
|---|---|---|---|---|---|---|---|---|---|
| 2009 LS | Abul Hasnat | AITC | — | — | CPI(M) | — | — | AITC gain from CPI(M); Hasnat switched to TMC | D |
| 2014 LS | **Abhishek Banerjee** | AITC | 508,481 | **40.31** | Dr. Abul Hasnat | CPI(M) | 437,187 | **34.66** | 71,294 margin | A |
| 2019 LS | **Abhishek Banerjee** | AITC | 791,127 | **~56.15** | Nilanjan Roy | BJP | 470,533 | **~33.44** | 320,594 margin | A |

**2014 context**: Abhishek Banerjee's first LS victory was narrow (~5.65pp margin) with CPI(M) still competitive at 34.66% and BJP minimal. The 2019 result (22.7pp margin) reflects both Abhishek's incumbency consolidation and the national BJP wave being partially offset by TMC's strong performance in Muslim-majority segments of this constituency.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- `2019_AssemblySegmentLevelVotingData.csv` — ECI GE2019 AC-segment vote tallies; AC_NO=143 Diamond Harbour (calibration target)
- Census of India 2011 — Diamond Harbour Municipality (Wikipedia rollup: pop 41,802; religion; SC; literacy; sex ratio)
- Census of India 2011 — Diamond Harbour I CD Block (Wikipedia rollup: pop 156,166; religion 52.16% Muslim; SC 18.63%; literacy 75.72%; language 99.83% Bengali; occupation)
- Census of India 2011 — Diamond Harbour II CD Block (Wikipedia rollup: pop 190,801; religion 59.77% Hindu; SC 26.55%; literacy 76.91%; language 99.7% Bengali; occupation)
- ECI 2011 AE, 2016 AE results for AC 143 Diamond Harbour (Wikipedia "Diamond Harbour Assembly constituency")
- ECI 2014 LS, 2019 LS results for Diamond Harbour PC 20 (Wikipedia "Diamond Harbour Lok Sabha constituency")
- Delimitation Commission of India 2008 — WB schedule: AC 143 = Diamond Harbour Municipality + 7 GPs of CDB-I + 6 GPs of CDB-II (Wikipedia "Diamond Harbour (Vidhan Sabha constituency)")

### Secondary sources (tier B/C)
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2019 NES post-poll (national rollup with WB regional summary)
- Census 2011 South 24 Parganas District — aggregate (religion 35.57% Muslim, SC 30.19%, literacy 77.51%); used as cross-check
- Diamond Harbour subdivision Wikipedia — 9 CDBs; demographic range across blocks
- `censusindia.co.in` secondary aggregations of Census 2011 for CDB-I and CDB-II blocks

### Tertiary / journalistic (tier D)
- Wikipedia "Diamond Harbour, India" — port economy, fishing, tourism
- Coastal Frontiers blog (Birkbeck) — Diamond Harbour fishing industry description
- S24P District Coastal Zone Livelihood Survey (dstbt.bangla.gov.in) — SC fishing communities livelihood
- Diamond Harbour BDO website (bdodh1.in) — block profile reference
- Indiastatpublications.com Diamond Harbour Assembly Factbook — 2016/2021 AE results cross-check

### Tier-D/E reliance flags (what to distrust)
- **Religion share projection 2011→2019** (C.1) — GP-equal-weight assumption within each CDB; refine when individual GP Census data accessible
- **Caste sub-group shares within Hindu and Muslim** (D.2) — no post-1931 caste census for OBC; no sub-community breakdowns in public Census tables; tier D/E throughout
- **Fishing occupation share** (C.8 — 12%) — estimated from district-level pisciculture data + CDB occupational patterns; no AC-level fishing census
- **Migration/birthplace** (C.16, D.3) — no public AC-level Census D-series; tier D from geographic/demographic reasoning; out-migration share (8.5%) is modelled, not measured
- **Asset/media sub-unit splits** (D.13) — NFHS-4 WB urban/rural averages applied at sub-unit level; no sub-block survey data
- **Vote × demographic conditionals** (D.15–D.18) — CSDS 2019 WB regional rollup calibrated to AC 143 CSV result; the D.15 recovery check passes but Hindu/Muslim split within that aggregate is modelled (tier C)
- **CDB-I "Netra" GP exclusion** — the one CDB-I GP NOT in AC 143 is "Netra"; assumed equal-weight to remaining 7 GPs (no GP-level population data in public Census tables)

### v0 known gaps (cross-reference methodology §7)
1. GP-level population data — collapsed to 3 sub-units (Muni + CDB-I rural share + CDB-II rural share); individual GP populations unknown → GP-equal-weight assumption may be off
2. ECI 2019 LS Form-20 AC-segment data — CSV provides tier-A aggregate; sub-polling-booth breakdown not used
3. CDB-I GP: Netra excluded from AC — equal-weight assumption; if Netra is atypically large or small, religion/SC/literacy weighted averages shift
4. Fishing occupation share — needs Fisheries Dept S24P block-level data for AC-level precision
5. Out-migration magnitude (C.16) — the 8.5% seasonal-out-migrant cell is the highest model uncertainty; affects effective turnout denominator
6. CSDS WB regional cross-tabs — using WB summary-level; Diamond Harbour PC may differ from state average; no Diamond Harbour-specific CSDS published data

---

*v0 — generated 2026-04-27, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **These are OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> The simulator must reproduce these results from 2019 priors + narrative injection without these figures being baked into the calibration input.

### 2021 WB Assembly Election — AC 143 Diamond Harbour (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| AITC | Pannalal Halder | 98,478 | **43.69%** | A — ECI 2021 AE / Wikipedia |
| BJP | Dipak Kumar Halder | 81,482 | **36.15%** | A — ECI 2021 AE / Wikipedia |
| CPI(M) | Pratik Ur Rahaman | 38,719 | **17.18%** | A — ECI 2021 AE / Wikipedia |
| **AITC margin** | | **16,996 votes** | **7.54 pp** | A |
| Turnout | 88.37% | | | A |

**Candidate-effect differential — critical model note**: The TMC AC-level result (43.69%) is dramatically lower than Abhishek Banerjee's 2019 LS AC-143 segment (52.86%) and the 2016 AE result (48.58%). The CPI(M) at 17.18% is extraordinarily high for a 2021 AE — the highest CPI(M) AE performance among surveyed South Bengal ACs. This signals:
1. **Abhishek Banerjee's personal vote does not transfer fully** to the TMC AC candidate. The LS vs. AE differential here is ~9pp.
2. **CPI(M)-Muslim residual held**: The Left's Muslim base in CDB-I (52% Muslim) did not fully consolidate with TMC in the 2021 AE in the way it did in the 2019 LS. Abul Hasnat (2016 CPI(M) AE candidate) had built a Muslim-Left base that partially persisted.
3. **BJP consolidated the Hindu vote**: BJP's 36.15% in 2021 AE is virtually identical to its 2019 LS AC-143 segment share (35.69%), confirming that the BJP's Hindu consolidation was durable across election types in this AC.
4. The simulator must account for the LS→AE candidate-effect differential and the CPI(M) Muslim residual as distinct model components.

### 2024 Lok Sabha Election — AC 143 segment within Diamond Harbour LS (PC 20) (tier A, CSV)

> Figures below are **tier A** — sourced directly from `/home/ubuntu/wb-election-sim/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=143, Diamond Harbour. Total electors: 265,214; total valid votes incl. NOTA: 213,296; turnout: **80.4%**.

| Party | Candidate (LS level) | Votes | AC-143 segment % | Tier | Source |
|---|---|---|---|---|---|
| AITC | Abhishek Banerjee | 147,343 | **69.08%** | A | `2024_AssemblySegmentLevelVotingData.csv` |
| BJP | Abhijit Das (Bobby) | 43,176 | **20.24%** | A | Same |
| AISF (Abdul Hasnat) | Majnu Laskar | 9,918 | **4.65%** | A | Same |
| CPI(M) | Pratik Ur Rahaman | 7,360 | **3.45%** | A | Same |
| NOTA | — | 1,303 | **0.61%** | A | Same |
| Others (BSP, INSAF, SUCI, IND×5) | various | 4,196 | **1.97%** | A | Same |
| **AITC margin over BJP** | | **104,167 votes** | **48.84 pp** | A | Computed |

**2024 interpretation**: Abhishek Banerjee's 2024 LS performance (69.08% at AC-143 level) is dramatically above the 2021 AE AC result (43.69%), confirming the massive candidate-effect differential. BJP collapsed from 36.15% (2021 AE) to 20.24% (2024 LS). The AISF (Majnu Laskar, likely connected to Abul Hasnat's network) captured 4.65% — indicating a third-force Muslim/Left split survived even in 2024. CPI(M) dropped to 3.45%.

### Calibration test
The simulator is considered validated on this seat if it:
1. Reproduces 2019 LS AC-143 shares within ±1pp of the CSV tier-A figures (primary calibration gate):
   - AITC target: 52.86% ± 1pp
   - BJP target: 35.69% ± 1pp
   - CPI(M) target: 8.19% ± 1pp
2. Reproduces 2021 AE within ±3pp after narrative injection (LS→AE candidate-effect shock + Left Muslim retention shock):
   - AITC target: 43.69% ± 3pp
   - BJP target: 36.15% ± 3pp
   - CPI(M) target: 17.18% ± 3pp (hard test — model must generate Left resurgence from Muslim residual)
3. Reproduces 2024 LS within ±3pp after narrative injection (Abhishek incumbency consolidation + BJP soft Hindu peel + AISF split):
   - AITC target: 69.08% ± 3pp
   - BJP target: 20.24% ± 3pp

### Section G gap note (for v1)
The following sources are used in Section H and should be migrated to Section G in a future v1 edit:
- `2024_AssemblySegmentLevelVotingData.csv` — ECI GE2024 AC-segment vote tallies (tier A; used in Section H above)
- Wikipedia "Diamond Harbour Assembly constituency" — 2021 AE results (tier A as sourced from ECI)
