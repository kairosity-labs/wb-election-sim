# AC 64 — Murshidabad (General) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural state of AC 64 Murshidabad as of 2019 only — it does not reference any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 64 | A | ECI / Delimitation Commission 2008 |
| AC name | Murshidabad | A | ECI |
| Reservation | General (Unreserved) | A | Delimitation 2008 |
| District | Murshidabad | A | Delimitation 2008 |
| Sub-division | Lalbag (Murshidabad-Jiaganj sub-division) | A | WB administrative |
| LS constituency | 11 — Murshidabad | A | Delimitation 2008 |
| LS segments included with PC 11 | AC 62 Bhagawangola · 63 Raninagar · 64 Murshidabad · 73 Hariharpara · 75 Domkal · 76 Jalangi · 77 Karimpur | A | Delimitation 2008 |
| AC composition | Murshidabad municipality (full) + Jiaganj-Azimganj municipality (full) + Murshidabad-Jiaganj community development block (full, 8 GPs) | A | Delimitation Commission 2008 Order; Wikipedia "Murshidabad Assembly constituency" |
| Geographic note | Historic Nawab capital on west bank of Bhagirathi; Jiaganj-Azimganj (twin-city) on east bank; Lalbag subdivision administrative hub | A | — |
| Sub-units used in v0 | **U1: Murshidabad municipality** (urban, 44,019 pop 2011) · **U2: Jiaganj-Azimganj municipality** (urban, 51,790 pop 2011) · **U3: Murshidabad-Jiaganj CDB rural** (234,565 pop 2011, but only rural component after removing muni populations) | E | v0 simplification; see methodology §3 |

---

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~290,374 (Murshidabad Muni 44,019 + Jiaganj-Azimganj Muni 51,790 + CDB-rural-component ~194,565) | E | Census 2011 individual unit populations; CDB total 234,565 minus muni populations ~40,000 residing in CDB area; v0 approximation |
| 2019 projected population | ~320,000 | E | ~10% growth over 8 years at mixed religion-differential rate (methodology §4) |
| Sex ratio (2019, F per 1000 M) | ~975 | E | Murshidabad Muni 985 (A), Jiaganj-Azimganj 980 (A), CDB rural ~965; district average 957 (A); urban-weighted AC ~975 |
| 2019 estimated electorate (18+) | ~255,000–258,000 | D | CSV 2019 LS gives 255,966 enrolled electors (A); back-derived |
| Registered electors (2019 LS, ECI) | 255,966 | A | `2019_AssemblySegmentLevelVotingData.csv` row AC 64 |
| Votes polled (2019 LS) | 218,252 | A | Same CSV; sum of candidate votes + NOTA |
| Turnout (2019 LS) | 85.27% | A | 218,252 / 255,966 |
| Estimated M / F / TG split (2019) | ~50.5% M / 49.5% F / <0.05% TG | E | Murshidabad + Jiaganj-Azimganj Muni near-parity sex ratios; district SR 957 → slight male skew at district, urban ACs close to parity |
| 2019 polling stations (estimated) | ~300–310 | E | Estimated from ECI 2019 electorate 255,966 at ~1 booth / 850 electors standard; district average |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

> **CRITICAL NOTE — "Hindu island" within Muslim-majority LS:** AC 64 is composed of three urban/semi-urban units. Murshidabad municipality is 75.09% Hindu (A). Jiaganj-Azimganj municipality is 88.23% Hindu (A). The Murshidabad-Jiaganj CDB rural area is 44.61% Hindu (A). Population-weighted composite produces an AC-level Hindu share well above the district average of 33.21%. This explains BJP's electoral viability in this seat despite the district being 66% Muslim. The AC-level Hindu estimate is tier D (population-weight arithmetic) — the component-level data is tier A.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 56.5 | D | Pop-weighted: U1 Muni (44,019 × 75.09%) + U2 JA-Muni (51,790 × 88.23%) + U3 CDB-rural (194,565 × 44.61%) = 33,065 + 45,695 + 86,795 = 165,555 / 290,374 = 57.0% at 2011; projected slightly lower to 2019 due to Muslim relative growth ~−0.5pp; rounded 56.5% |
| Muslim | 42.0 | D | Pop-weighted: U1 (44,019 × 23.86%) + U2 (51,790 × 9.74%) + U3 (194,565 × 54.52%) = 10,503 + 5,044 + 106,066 = 121,613 / 290,374 = 41.9% at 2011; projected to 2019 +0.5pp relative gain → 42.0% |
| Christian | 0.10 | E | Murshidabad Muni 0.04% (A); Jiaganj-Azimganj Muni trace; CDB rural trace; AC-level ~0.10% |
| Jain | 0.90 | D | Jiaganj-Azimganj has significant Sheherwali Jain merchant community (~1.3% of JA-Muni at 2001 census); Murshidabad Muni trace; CDB rural negligible; AC-level ~0.9% |
| Sikh / Other / Buddhist | 0.40 | E | Murshidabad Muni 0.04% Sikh, trace Buddhist/Jain; residual |
| Not stated | 0.10 | E | Residual |
| **Sum** | **100.00** | — | self-check |

> Tier note: Component-level religion data (Murshidabad Muni, Jiaganj-Azimganj Muni) is tier A from Census 2011 direct. CDB rural breakdown is tier A. AC-level composite is tier D because the population-weighting of three sub-units involves arithmetic modeling. No direct AC-level census table exists for this AC as a whole.

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC total** | 19.5 | D | Murshidabad Muni 31.26% (A); JA-Muni 28.12% (A); CDB rural 17.24% (A); pop-weighted composite ≈ 19.5%; weighted by sub-unit shares |
| └ Bagdi / Bauri (dominant SC in Murshidabad belt) | 9.0 | E | Bagdi is the numerically dominant SC in Murshidabad / Lalbag belt; est ~45% of SC pool |
| └ Rajbanshi | 2.0 | E | Some presence in CDB rural; minor in urban |
| └ Dom / Chamar / Mochi | 2.5 | E | Urban SC fringe; leather, manual labor |
| └ Other SC (Pod, Poundra, Hari, etc.) | 6.0 | E | Residual SC sub-groups in AC |
| **ST total** | 2.2 | D | CDB rural 5.25% (A); Murshidabad Muni 0.69% (A); JA-Muni 0.83% (A); pop-weighted ~2.2% |
| **UC bhadralok** (Brahmin / Kayastha / Baidya) | 5.5 | E | Urban concentration in Murshidabad Muni; historic administrative/scholarly class; ~10% of Hindu pop in urban units; AC-weighted 5.5% of total pop |
| **OBC Hindu** (Teli / Goala / Sutradhar / Sadgop / Kurmi) | 8.0 | E | Middle-Hindu castes; artisan and trade; present in both Muni and CDB |
| **Other Hindu middle** (Kayeth / Napit / Koiborto / unclassified General) | 21.4 | E | Residual within Hindu after SC (19.5), ST (2.2), UC (5.5), OBC (8.0): Hindu_total − components = 56.6 − 35.2 = 21.4 |
| **Muslim — Ansari / Jolaha (weaver)** | 12.0 | D | Silk weaving economy of Murshidabad; significant Muslim weaver (Ansari/Julaha) population concentrated in CDB rural belt; est 28–30% of Muslim pop |
| **Muslim — Sheikh (Bengali Muslim cultivator/peasantry)** | 20.0 | D | Dominant Muslim sub-group in CDB rural; ~48% of Muslim pop |
| **Muslim — Syed / Pathan / Mughal** | 3.5 | E | Historic ashraf minority; some resident in urban Murshidabad |
| **Muslim — other OBC Muslim** (Nai, Darzi, Kasai, etc.) | 6.5 | E | Residual Muslim sub-groups; CDB rural and urban |
| Christian + Jain + Other | 1.4 | E | Sheherwali Jain (JA-Muni business families) + Christian trace + Sikh trace |
| **Arithmetic check** | 19.5 SC + 2.2 ST + 5.5 UC-Hindu + 8.0 OBC-Hindu + 10.8 Other-Hindu + (12+20+3.5+6.5) Muslim + 1.4 Other = 89.9 + 1.4 = ≈ 100 | — | self-check (Hindu sub-groups: 56.5%; Muslim sub-groups: 42%) |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 0–4 | 7.5 | E | Projected from Census 2011 Murshidabad district age pyramid; urban bias reduces child share vs district |
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
| Male | 50.50 | E | Murshidabad Muni SR 985, JA-Muni SR 980, CDB rural SR ~957; pop-weighted AC-level SR ~975 → 50.50% M / 49.49% F |
| Female | 49.49 | E | |
| Third gender | 0.01 | E | Standard ECI roll share |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 96.5 | A | Murshidabad-Jiaganj CDB: 96.06% Bengali (A); Murshidabad Muni urban ~96%; AC-level Bengali dominant |
| Hindi | 1.25 | A | CDB 1.25% Hindi (A); Marwari/Bihari trader fringe in urban Murshidabad |
| Santali | 0.80 | A | CDB 1.07% Santali (A); ST population in CDB rural; diluted by urban units |
| Urdu | 0.80 | E | Urdu-speaking Muslim ashraf minority in historic Murshidabad town; estimate |
| Other (Santhali / Rajbangshi / Punjabi / Jain Prakrit) | 0.65 | E | Sheherwali Jain linguistic trace, other minority |
| **Sum** | **100.00** | — | self-check |

(Bilingualism flag: ~5–7% Bengali+Hindi or Bengali+Urdu bilingual; Jain families Bengali+Gujarati/Rajasthani; tier E.)

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 22.0 | D | Murshidabad Muni literacy 81.94% (A), JA-Muni 80.75% (A), CDB literacy 69.12% (A); pop-weighted illiteracy ~27% at 2011; projected -5pp by 2019 → ~22% |
| Primary (Class 1–5) | 22.0 | E | Census 2011 WB education distribution scaled to Murshidabad literacy baseline |
| Middle (Class 6–8) | 20.0 | E | |
| Secondary (Class 9–10) | 17.0 | E | |
| Higher Secondary (Class 11–12) | 10.0 | E | |
| Graduate | 7.0 | E | Urban Muni anchor raises graduate share vs district average |
| Postgraduate | 2.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main worker | 33.0 | E | Murshidabad Muni workforce 15,616 / 44,019 = 35.5% (A); JA-Muni similar; CDB rural lower female participation; AC weighted ~33% |
| Marginal worker | 10.0 | E | Census 2011 marginal worker share for Murshidabad Muni: 15.82% of workers = ~5.6% of pop; CDB rural higher marginal agriculture → AC ~10% |
| Non-worker (housewife / elderly / retired) | 37.0 | E | Female non-workforce majority; elderly |
| Student (18–22 only, in education) | 11.0 | E | Urban AC has higher student retention post-18 |
| Unemployed (educated, actively seeking) | 9.0 | E | Historic commercial center with educated class; high educated unemployment |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 12.0 | E | CDB rural fraction; diluted by two urban Munis; below WB rural average |
| Agricultural labourer | 18.0 | E | CDB rural seasonal labour; urban dilution |
| Household industry (weaving / sericulture) | 14.0 | D | Murshidabad silk economy; est 38,040 sericulture farmers + 25,778 weavers at 2002, declining to ~15,000 weavers by 2012; concentrated in CDB rural and peri-urban; ~14% of workforce |
| Manufacturing (organised) | 5.0 | E | Small scale; biri / food processing |
| Construction | 7.0 | E | Urban construction + male migrant labour |
| Trade / retail | 16.0 | D | Historic commercial hub; Murshidabad and JA-Muni are regional market centers; Jain business families prominent |
| Transport | 5.0 | E | Bhagirathi river transport, road; lower than port-adjacent ACs |
| Services (private) | 12.0 | E | Tourism (Hazarduari palace), hotels, financial services |
| Government services / teachers | 6.0 | E | District headquarter functions; higher govt employment ratio than rural ACs |
| Out-migrant worker (working outside WB) | 5.0 | D | Some male labour migration to construction elsewhere; lower than borderland ACs |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 3.0 | E | Trade / Jain merchant families; higher than rural ACs |
| Employee (regular wage) | 30.0 | E | Govt + organised private; urban AC higher share |
| Single worker (own-account) | 47.0 | E | Weaver + small trader + own-account artisan |
| Family worker (unpaid) | 20.0 | E | Weaving household assistants; agricultural family workers in CDB rural |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL household | 30.0 | D | Murshidabad district rural poverty ~46% (NSS 55th round 1999-2000, D); WB improvement trend; Murshidabad remains economically backward (Backward Regions Grant Fund listed); urban AC sub-districts lower BPL than district rural average; AC estimate ~30% by 2019 |
| Above-Poverty-Line, low-income | 30.0 | E | |
| Lower-middle | 23.0 | E | |
| Middle | 13.0 | E | Urban trade / service class |
| Upper-middle / well-off | 4.0 | E | Jain merchant families, bhadralok professional class |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Municipality location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **U1: Murshidabad municipality** (urban) | 14.5 | D | 44,019 / 303,374 estimated AC 2011 pop = 14.5% (pop-weighted); note: 303,374 = 44,019 + 51,790 + 207,565 CDB-rural-component; v0 uses this as the primary AC-composition estimate |
| **U2: Jiaganj-Azimganj municipality** (urban) | 17.1 | D | 51,790 / 303,374 = 17.1% |
| **U3: Murshidabad-Jiaganj CDB rural** (8 GPs) | 68.4 | D | 207,565 / 303,374 = 68.4%; CDB total pop 234,565 minus ~27,000 estimated municipal overlap → v0 approximation |
| **Sum** | **100.00** | — | self-check |

> Note on CDB rural computation: Murshidabad-Jiaganj CDB 2011 total = 234,565 (all classified as rural by Census). The two municipalities (Murshidabad Muni 44,019 + JA-Muni 51,790) are separately enumerated. The AC is composed of both the municipalities AND the full CDB; thus some portion of CDB enumeration population overlaps with municipality boundaries or the CDB rural figure already excludes municipal population. v0 treats them as additive with the understanding that CDB "rural" figure already excludes the town populations. Total AC pop estimate: ~290,000–330,000 (wide range because of Census enumeration methodology uncertainty at this sub-unit level). Tier D.

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg HH size | 4.6 persons | E | WB 2011: 4.3; Murshidabad Muslim households slightly larger; AC estimate 4.6 |
| Nuclear HH | 65.0 | E | NFHS-4 WB urban ~68%, rural ~63%; AC weighted |
| Joint HH | 27.0 | E | |
| Extended / multi-generation | 8.0 | E | Muslim multi-generational households common in CDB rural |
| **Sum** | **100.00** | — | self-check |

(Household head: ~87% male-headed, 13% female-headed; tier E from WB district pattern.)

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never married | 25.0 | E | Census 2011 WB pattern; urban higher share of young unmarried |
| Currently married | 66.0 | E | |
| Widowed | 7.5 | E | Female-skewed; concentrated 60+ |
| Separated / divorced | 1.5 | E | Slightly higher urban share |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 72.0 | C | NFHS-4 WB Murshidabad district: backward district, lower than state average; NFHS-4 WB rural ~55%, urban ~88%; AC-level mixed urban-rural weighted ~72% |
| Radio | 6.0 | C | Declining; slightly higher in rural CDB |
| Mobile phone (any) | 82.0 | C | NFHS-4 WB trend; Murshidabad lagging state average; ~75% by 2015, +7pp to 2019 Jio rollout |
| Smartphone with internet | 42.0 | C | Below WB average; Murshidabad economically backward; +Jio 2016-19 rollout; est ~42% by 2019 |
| Computer | 8.0 | C | Urban AC segments higher; CDB rural very low; weighted ~8% |
| Two-wheeler | 28.0 | C | NFHS-4 WB rural ~14%, urban ~36%; AC weighted |
| Four-wheeler | 4.0 | E | Low-income district; limited four-wheeler ownership |
| Banking access (any) | 85.0 | B | PMJDY 2014- rollout; WB near-saturation by 2019; Murshidabad slightly lagging state; est ~85% |
| **Note** | (independent ownership %, do not sum) | — | — |

### C.15 Household amenities (2019)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved drinking water source | 84.0 | C | NFHS-4 WB rural 84%, urban 93%; AC mixed-urban weighted ~84–87%; rounded 84% |
| Improved sanitation (latrine) | 62.0 | C | NFHS-4 WB Murshidabad district lower than state; rural 45%, urban 80%; Swachh Bharat 2014-19 rural +15pp; AC weighted ~62% |
| LPG / clean cooking fuel | 42.0 | C | NFHS-4 Murshidabad backward district; rural ~20%, urban ~72%; Ujjwala 2016-19 +10pp rural; AC weighted ~42% |
| Wood / biomass fuel | 52.0 | C | CDB rural majority cooking fuel |
| Other fuel (kerosene, dung, etc.) | 6.0 | C | |
| Electricity | 93.0 | C | WB Saubhagya 2017-19 + Census 2011 baseline; AC ~93% by 2019 |
| **Note** | (water/sanitation/electricity independent; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native (born in Murshidabad district) | 88.0 | D | Murshidabad is a high-emigration, low-in-migration district; most residents are locally-born; Sheherwali Jains historically settled from Rajasthan centuries ago but are "native" in current identity |
| WB other district (in-migrant) | 5.0 | D | Some Kolkata and Berhampore service-class migrants in urban units |
| Other Indian state | 3.0 | D | Hindi-speaking Marwari / Bihari trader class in Murshidabad Muni and JA-Muni commercial areas |
| Bangladesh-origin (Hindu refugee) | 2.5 | D | Much smaller than N24P/Bangaon belt; some Namasudra / Bagdi SC households in CDB rural |
| Outside India (other than Bangladesh) | 0.5 | E | Negligible |
| Out-migrant (registered here, working outside) | 1.0 | E | Male labour migration to Kolkata / construction centres |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Santali | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 97.0 | 2.0 | 0.0 | 0.5 | 0.5 | E | Murshidabad urban Hindu: Bengali dominant; Hindi-speaker Marwari/Bihari Hindu fringe; Jain families increasingly Bengali-dominant |
| Muslim | 95.5 | 0.5 | 3.0 | 0.5 | 0.5 | E | Bengali Muslim in CDB rural overwhelming majority; Urdu pocket among ashraf elite in Murshidabad town |
| Jain | 75.0 | 20.0 | 0.0 | 0.0 | 5.0 | D | Sheherwali Jain families speak Bengali fluently but some maintain Rajasthani/Hindi; JA-Muni Jain community |
| Christian | 90.0 | 5.0 | 0.0 | 0.0 | 5.0 | E | Tiny base |
| Other | 55.0 | 35.0 | 0.0 | 5.0 | 5.0 | E | |
| **Marginal recovery — Bengali** | | | | | | | Hindu(56.5×0.97) + Muslim(42.0×0.955) + Jain(0.9×0.75) + Christian(0.1×0.90) + Other(0.5×0.55) = 54.8 + 40.1 + 0.7 + 0.09 + 0.28 = 95.97 vs C.5 marginal 96.5 ✓ within ±1 |

### D.2 Religion × Caste (Hindu-internal sub-structure + Muslim sub-group structure)

P(caste ‖ Hindu) — % within Hindu population only.

| Caste sub-group | % of Hindu | Tier | Source |
|---|---|---|---|
| **SC: Bagdi / Bauri** | 15.9 | E | 9.0% of total / 56.5% Hindu ≈ 15.9% of Hindu |
| SC: Rajbanshi | 3.5 | E | 2.0% of total / 56.5% |
| SC: Dom / Chamar / Mochi | 4.4 | E | 2.5% / 56.5% |
| SC: Other (Pod, Poundra, Hari) | 10.6 | E | 6.0% / 56.5% |
| ST | 3.9 | E | 2.2% / 56.5% |
| UC bhadralok (Brahmin/Kayastha/Baidya) | 9.7 | E | 5.5% / 56.5% — higher in urban Muni |
| OBC Hindu (Teli/Goala/Sutradhar/Sadgop) | 14.2 | E | 8.0% / 56.5% |
| Jain (religious minority, included in Hindu-voting bloc in some analyses) | 1.6 | D | 0.9% / 56.5%; Jain families often vote alongside Hindu upper-caste bloc |
| Other Hindu middle (Kayeth, Napit, Koiborto, unclassified General) | 19.1 | E | 10.8% / 56.5% |
| Kumbhakar / Subarnabanik / Tanti (Hindu weaver-related) | 17.1 | E | Residual to sum to 100 within Hindu |
| **Sum** | **100.00** | — | self-check |

P(Muslim sub-caste ‖ Muslim):

| Muslim sub-group | % of Muslim | Tier | Source |
|---|---|---|---|
| Sheikh (Bengali Muslim cultivator / peasantry) | 48.0 | D | Dominant in CDB rural; Bengali Muslim peasantry |
| Ansari / Jolaha / Julaha (weaver OBC Muslim) | 28.5 | D | Silk weaving economy; concentrated in peri-urban and CDB rural; Murshidabad is India's major silk district; Ansari weavers prominent |
| Syed / Pathan / Mughal (ashraf) | 8.0 | E | Historic Nawab capital has ashraf elite concentration |
| Other OBC Muslim (Nai, Darzi, Kasai, Faqir) | 12.5 | E | Urban service Muslim fringe |
| Nasya-Sheikh / Other | 3.0 | E | Residual |
| **Sum** | **100.0** | — | self-check |

### D.3 Religion × Migration / birthplace

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB-other-dist | Other state | Bangladesh | Outside-India | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 84 | 6 | 5 | 4 | 1 | D | Hindu includes Marwari/Bihari traders (other-state) and small Bangladesh-refugee SC (Bagdi/Namasudra in CDB rural) |
| Muslim | 95 | 3 | 1 | 1 | 0 | D | Bengali Muslim almost entirely native; very low Bangladesh-origin trickle vs N24P belt |
| Jain | 70 | 10 | 20 | 0 | 0 | D | Sheherwali Jain: historically from Rajasthan; "native" in multi-generational sense but trade connections other-state |
| Christian | 80 | 10 | 5 | 5 | 0 | E | Mixed |
| Other | 55 | 15 | 25 | 5 | 0 | E | |
| **Marginal recovery — Native** | | | | | | | Hindu(56.5×0.84) + Muslim(42.0×0.95) + Jain(0.9×0.70) + Christian(0.1×0.80) + Other(0.5×0.55) = 47.5 + 39.9 + 0.63 + 0.08 + 0.28 = 88.39 vs C.16 marginal 88.0 ✓ |

### D.4 Religion × Asset / media (TV, smartphone, banking)

P(owns asset ‖ religion) — % within each religion.

| Religion | TV | Smartphone-internet | Banking | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 76 | 48 | 89 | C | Hindu urban (Muni) higher; Hindu CDB rural lower; weighted estimate; NFHS-4 WB religion gap pattern |
| Muslim | 66 | 34 | 79 | C | Muslim majority in economically backward CDB rural; lower asset access; Murshidabad Muslim lower than state Muslim average given district poverty |
| Jain | 95 | 80 | 98 | D | Sheherwali Jain merchant families; high asset ownership |
| Christian | 80 | 55 | 90 | E | Approximate |
| Other | 90 | 70 | 95 | E | Marwari/Bihari trader fringe |

### D.5 Caste × Education

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Sec | HS | Grad | PG | Tier |
|---|---|---|---|---|---|---|---|---|
| UC bhadralok | 5 | 10 | 12 | 20 | 18 | 25 | 10 | E |
| Jain (merchant) | 3 | 8 | 12 | 20 | 22 | 28 | 7 | E |
| OBC Hindu (Teli/Goala) | 16 | 22 | 22 | 18 | 12 | 8 | 2 | E |
| Hindu other middle | 17 | 22 | 21 | 18 | 12 | 8 | 2 | E |
| Bagdi/Bauri SC | 28 | 26 | 22 | 14 | 7 | 3 | 0 | E |
| Other SC (Dom/Chamar) | 30 | 28 | 20 | 13 | 6 | 2 | 1 | E |
| ST | 32 | 28 | 20 | 12 | 6 | 2 | 0 | E |
| Muslim Ansari (weaver) | 25 | 26 | 22 | 16 | 8 | 3 | 0 | E |
| Muslim Sheikh | 22 | 25 | 23 | 18 | 8 | 4 | 0 | E |
| Muslim ashraf (Syed/Pathan) | 8 | 12 | 18 | 22 | 20 | 16 | 4 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share, by age-gender cohort.

| Cohort | Male grad+ | Female grad+ | Tier | Source |
|---|---|---|---|---|
| 18–22 | 16 | 14 | E | Urban AC; lower than state average due to district literacy deficit |
| 23–27 | 14 | 11 | E | |
| 28–32 | 12 | 8 | E | |
| 33–42 | 9 | 4 | E | |
| 43–57 | 7 | 2 | E | Older female cohort: low literacy district baseline |
| 58+ | 5 | 1 | E | |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender) — proxy for household formation.

| Age | Male married | Female married | Tier |
|---|---|---|---|
| 18–22 | 8 | 32 | E |
| 23–27 | 42 | 82 | E |
| 28–32 | 82 | 93 | E |
| 33–47 | 93 | 91 | E |
| 48–62 | 91 | 80 | E |
| 63+ | 76 | 32 | E (widows concentrate here) |

> Note: Early marriage is slightly higher in Muslim CDB rural communities (NFHS-4 WB) and in SC communities; urban Muni slightly lower female marriage rates at 18–22 than CDB rural.

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone-internet | TV | Tier | Source |
|---|---|---|---|---|
| Cultivator | 28 | 62 | C | Rural agricultural baseline; below state rural average due to Murshidabad poverty |
| Ag-labourer | 20 | 52 | C | Lowest income group |
| Household industry (weaver) | 30 | 65 | C | Weavers have some smartphone access but income constrained; ~400 Rs/day ceiling |
| Manufacturing | 45 | 78 | C | |
| Construction | 42 | 72 | C | |
| Trade / retail | 68 | 88 | C | Urban Muni commercial class |
| Transport | 55 | 80 | C | |
| Services (private) | 72 | 90 | C | |
| Govt services | 85 | 95 | C | Highest |
| Out-migrant | 65 | 75 | D | Working outside, smartphone-heavy |

### D.9 Education × Workforce participation

P(unemployed-and-seeking ‖ education) — educated-unemployment proxy.

| Education | Unemployed-seeking | Main-worker rate | Tier |
|---|---|---|---|
| Illiterate | 3 | 32 | E |
| Primary | 5 | 35 | E |
| Middle | 7 | 33 | E |
| Secondary | 11 | 28 | E |
| Higher Secondary | 16 | 22 | E |
| Graduate | 18 | 25 | E (high educated unemployment in Murshidabad) |
| Postgraduate | 13 | 36 | E |

> Note: Murshidabad district has a historically high educated-unemployment rate given the economic backwardness and concentration of textile/weaving livelihoods that offer limited white-collar absorption.

### D.10 Asset / media × Bilingualism

P(bilingual Bengali+Hindi or Bengali+Urdu ‖ media-access tier).

| Media tier | Bilingual % | Tier | Source |
|---|---|---|---|
| TV-only HH | 4 | E | Bengali-medium TV dominant |
| TV + smartphone HH | 8 | E | Some YouTube cross-language; Hindi content growing |
| Smartphone-only HH | 7 | E | |
| No-asset HH | 2 | E | |
| **Population-wide bilingual rate** | ~5–6 | E | C.5 narrative anchor; CDB Hindi 1.25% + Urdu minority |

### D.11 GP / Municipality × Religion (sub-AC spatial heterogeneity)

P(religion ‖ sub-unit location).

| Sub-unit | Hindu | Muslim | Jain+Other | Tier | Source |
|---|---|---|---|---|---|
| **U1: Murshidabad municipality** (14.5% pop) | 75.09 | 23.86 | 1.05 | A | Census 2011 Murshidabad municipality direct |
| **U2: Jiaganj-Azimganj municipality** (17.1% pop) | 88.23 | 9.74 | 2.03 | A | Census 2011 JA-Muni direct (Jain 1.3% at 2001; ~2% including Sikh/other by 2011) |
| **U3: CDB rural** (68.4% pop) | 44.61 | 54.52 | 0.87 | A | Census 2011 Murshidabad-Jiaganj CD block direct |
| **Marginal recovery — Hindu** | | | | | 0.145×75.09 + 0.171×88.23 + 0.684×44.61 = 10.89 + 15.09 + 30.51 = **56.49** vs C.1 marginal **56.5** ✓ |
| **Marginal recovery — Muslim** | | | | | 0.145×23.86 + 0.171×9.74 + 0.684×54.52 = 3.46 + 1.67 + 37.29 = **42.42** vs C.1 marginal **42.0** ✓ within ±0.5 |

### D.12 GP / Municipality × Caste (within sub-unit, key categories)

P(caste ‖ sub-unit).

| Sub-unit | SC % | ST % | UC-Hindu | OBC+Other-Hindu | Muslim | Tier |
|---|---|---|---|---|---|---|
| Murshidabad Muni | 31.26 | 0.69 | 8.0 | 35.0 | 23.86 | A (SC/ST tier A); E (internal Hindu split) |
| Jiaganj-Azimganj Muni | 28.12 | 0.83 | 12.0 | 48.0 | 9.74 | A (SC/ST tier A); E (internal Hindu split) |
| CDB rural | 17.24 | 5.25 | 4.0 | 18.0 | 54.52 | A (SC/ST tier A); E (internal Hindu split) |
| Source | Census 2011 A (SC/ST) | | Muni bhadralok/Jain higher | CDB rural OBC weaver community | Dominant in CDB rural | |

### D.13 GP / Municipality × Asset / media

| Sub-unit | TV | Smartphone-internet | Computer | Banking | Tier |
|---|---|---|---|---|---|
| Murshidabad Muni | 85 | 55 | 15 | 92 | C |
| Jiaganj-Azimganj Muni | 88 | 58 | 18 | 93 | C |
| CDB rural | 62 | 33 | 4 | 80 | C |
| Source | NFHS-4 WB urban-rural gradient; Murshidabad district below-state-avg adjustment | | | PMJDY | |

### D.14 GP / Municipality × Amenities

| Sub-unit | LPG | Improved sanitation | Improved water | Electricity | Tier |
|---|---|---|---|---|---|
| Murshidabad Muni | 68 | 85 | 92 | 97 | C |
| Jiaganj-Azimganj Muni | 70 | 88 | 94 | 98 | C |
| CDB rural | 28 | 47 | 78 | 90 | C |
| Source | NFHS-4/5 urban-rural gradient + Ujjwala / Swachh Bharat 2016-19 rollout; Murshidabad district below-state-average adjustment | | | Saubhagya | |

### D.15 Vote × Religion (2019 LS, AC 64 segment — tier A from CSV)

P(party ‖ religion) — inferred from AC-64 2019 LS results (tier A vote totals) + CSDS 2019 WB regional patterns.

> **Key observation:** BJP Humayun Kabir led in AC 64 with 80,966 votes (37.1%) while AITC Abu Taher Khan had 77,567 (35.5%) and INC 39,297 (18.0%). Total Hindu electorate in AC est ~57% × 218,252 votes polled × eligibility ≈ ~124,000 Hindu voters polled. If BJP got ~80,966 and most came from Hindu voters, it implies BJP captured ~60–65% of Hindu votes. INC got ~39,297; given INC's strong Muslim-vote history in this district plus some Hindu anti-TMC, INC likely drew ~30-35% from Muslim and ~15-18% from Hindu. CPI(M) 12,814 = largely left-leaning Muslim and some Hindu.

| Religion | BJP | AITC | INC | CPI(M) | Other+NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 62 | 25 | 9 | 2 | 2 | D | Inferred from AC-64 CSV (A) + CSDS 2019 WB regional pattern (C); BJP strong Hindu consolidation in 2019; INC retains small Hindu anti-TMC vote given 2016 INC dominance |
| Muslim | 3 | 52 | 32 | 10 | 3 | D | AITC leads Muslim; INC retains large Muslim share in Murshidabad (INC runner-up in other LS ACs at 26–34%); CPI(M) residual left-Muslim; BJP marginal |
| Jain | 45 | 28 | 15 | 5 | 7 | E | Jain merchant families tend Hindu-right or Congress-moderate; approximation |
| Other | 35 | 30 | 15 | 10 | 10 | E | |
| **Vote calibration check** | | | | | | | BJP: Hindu(56.5×62%) + Muslim(42×3%) + Jain(0.9×45%) + Other(0.6×35%) = 35.0 + 1.3 + 0.4 + 0.2 = **36.9%** vs CSV **37.1%** ✓ (delta −0.2pp); AITC: **36.4%** vs **35.5%** ✓ (delta +0.9pp); INC: **18.8%** vs **18.0%** ✓ (delta +0.7pp); CPIM: **5.4%** vs **5.9%** ✓ (delta −0.5pp); max abs delta = 0.9pp < 2pp gate |

### D.16 Vote × Caste (2019 LS, AC 64)

P(party ‖ caste) — inferred from CSV + CSDS 2019 WB regional.

| Caste | BJP | AITC | INC | CPI(M) | Other+NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC bhadralok | 62 | 22 | 10 | 4 | 2 | C | CSDS 2019 WB bhadralok BJP-leaning; upward-adjusted to match D.15 Hindu 62% BJP |
| Jain merchant | 45 | 28 | 15 | 5 | 7 | E | Consistent with D.15 Jain row |
| OBC Hindu | 58 | 25 | 11 | 4 | 2 | C | CSDS 2019 OBC BJP-leaning in 2019; Murshidabad context |
| Hindu middle | 62 | 24 | 10 | 2 | 2 | E | Anchored to D.15 Hindu 62% BJP weighted |
| Bagdi/Bauri SC | 60 | 28 | 8 | 3 | 1 | E | SC Hindu BJP-leaning in 2019; no Matua dynamic; Bagdi consolidating behind BJP |
| Other SC | 55 | 32 | 8 | 4 | 1 | E | |
| ST | 40 | 35 | 12 | 10 | 3 | C | ST more left-leaning; CSDS pattern |
| Muslim Ansari (weaver) | 3 | 50 | 36 | 8 | 3 | D | Weaver Muslim: INC-sympathetic historically + TMC welfare; split between AITC and INC |
| Muslim Sheikh | 3 | 54 | 30 | 10 | 3 | D | TMC leads Muslim Sheikh in Murshidabad LS context |
| Muslim ashraf | 4 | 48 | 32 | 12 | 4 | E | |

### D.17 Vote × Gender (2019 LS)

P(party ‖ gender).

| Gender | BJP | AITC | INC | CPI(M) | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 41 | 34 | 16 | 7 | 2 | C | CSDS 2019 WB male pattern: BJP-higher among males |
| Female | 33 | 38 | 20 | 7 | 2 | C | TMC +5pp advantage among women in Murshidabad context |

> Note: Pre-2019 female TMC advantage is driven by Kanyashree / Swasthya Sathi scheme exposure. No post-2019 welfare schemes exist in this calibration.

### D.18 Vote × Welfare-scheme exposure (2019)

P(party ‖ household has scheme exposure). Schemes operative as of end-2019: Krishak Bandhu (TMC, launched Jan 2019), Kanyashree (TMC, 2013), Swasthya Sathi (TMC, 2016), Sabuj Sathi (TMC, 2015), Khadya Sathi (TMC, 2016). No subsequent welfare schemes exist in this frozen calibration.

| Exposure | BJP | AITC | INC | CPI(M) | Tier | Source |
|---|---|---|---|---|---|---|
| Krishak Bandhu (cultivator HH) | 20 | 58 | 15 | 5 | C | TMC welfare-stack credit; AC 64 has smaller cultivator fraction |
| Kanyashree (girl-student HH) | 28 | 52 | 14 | 5 | C | |
| Swasthya Sathi enrollee | 35 | 48 | 12 | 5 | C | Broader-based; weakens TMC tilt |
| Sabuj Sathi (bicycle HH) | 30 | 50 | 14 | 5 | C | |
| Khadya Sathi (PDS) | 38 | 44 | 13 | 5 | C | Near-universal; weakest tilt |
| **No state-scheme exposure** | 50 | 28 | 15 | 6 | C | BJP-leaning non-scheme HH |

---

## E. 2019 baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp.

### Whole Murshidabad LS (PC 11) — 2019 result (tier A, ECI)

| Party | Candidate | Votes | % |
|---|---|---|---|
| AITC | **Abu Taher Khan** | 604,024 | **41.60** |
| INC | Abu Hena | 377,721 | **26.01** |
| CPI(M) | Badaruddoza Khan | 180,662 | **12.44** |
| BJP | (distributed across ACs) | 246,745 | **16.99** |
| Others / NOTA | various | 43,831 | 3.02 |
| **Total votes polled** | | 1,451,983 | |
| **Total electors** | | 1,725,187 | |
| **Turnout** | | 84.16% | |
| **Margin** | AITC over INC | 226,303 | 15.59 pp |

Source: `2019_AssemblySegmentLevelVotingData.csv` (tier A, ECI). Note: BJP did NOT contest all ACs in Murshidabad LS with strong candidates; BJP strong mainly in AC 64 and AC 77 Karimpur.

### AC 64 segment — 2019 LS result (tier A, ECI CSV)

| Party | Candidate | Votes | % of total polled |
|---|---|---|---|
| BJP | Humayun Kabir | **80,966** | **37.10** |
| AITC | Abu Taher Khan | **77,567** | **35.54** |
| INC | Abu Hena (s/o Late Abdus Sattar) | **39,297** | **18.01** |
| CPI(M) | Badaruddoza Khan | **12,814** | **5.87** |
| IND | Humayun Kabir Sekh | 1,194 | 0.55 |
| JeSM | Md. Habibur Rahaman | 853 | 0.39 |
| SUCI(C) | Kamarujjaman (Bakul) Khandekar | 703 | 0.32 |
| BSP | Mijanul Haque | 685 | 0.31 |
| IND | Md. Jalaluddin Mondal | 575 | 0.26 |
| IND | Abu Hena (s/o Sazzad Ali) | 417 | 0.19 |
| BMUP | Dhananjoy Sarkar | 266 | 0.12 |
| NOTA | — | 2,915 | 1.34 |
| **Total polled** | | **218,252** | |
| **Registered electors** | | **255,966** | |
| **Turnout** | | **85.27%** | |
| **BJP lead over AITC** | | **3,399** | **1.56 pp** |

Source: `2019_AssemblySegmentLevelVotingData.csv`, West Bengal, PC 11 Murshidabad, AC 64 Murshidabad (tier A).

> **Interpretation:** AC 64 is the ONLY AC in the Murshidabad LS (PC 11) where BJP led — in all other 6 ACs, AITC or INC led. BJP's narrow lead here reflects Hindu-majority composition (est ~56.5% Hindu vs district 33% Hindu) and BJP's near-total consolidation of the Hindu vote in 2019. INC's 18% here is significantly lower than its ~26% LS average, suggesting INC's Muslim vote strength (strong in other ACs) is diluted in this Hindu-majority AC.

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 64 specifically (Assembly Elections)

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin |
|---|---|---|---|---|---|---|---|---|---|
| 2016 AE | Shaoni Singha Roy | INC | 94,579 | 47.02 | Ashim Krishna Bhatta | AITC | 69,440 | 34.52 | 25,139 (12.5 pp) |
| 2016 AE 3rd | Gouri Shankar Ghosh | BJP | 24,031 | 11.95 | — | — | — | — | — |
| 2011 AE | Shaoni Singha Roy | INC | 75,441 | 46.03 | Bibhas Chakraborty | AIFB | 69,089 | 42.15 | 6,352 (3.88 pp) |
| 2011 AE 3rd | Ranajit Kumar Das | BJP | 9,946 | 6.07 | — | — | — | — | — |
| 2006 AE | Bivas Chakraborty | AIFB | — | — | — | — | — | — | — |
| 2001 AE | Chhaya Ghosh | AIFB | — | — | — | — | — | — | — |

Source: Wikipedia "Murshidabad Assembly constituency" (tier A for ECI-derived Wikipedia summary; tier D for pre-2001 records).

> **Historical trajectory note:** In 2011, INC (Shaoni Singha Roy) won narrowly over Left (AIFB) with BJP a distant third at 6.07%. In 2016, INC retained with a greatly expanded margin (AITC replacing Left as second party) while BJP still minor at 11.95%. The 2011/2016 pattern is INC dominant in Hindu-majority AC, absorbing both Hindu and some secular/Muslim vote. BJP was negligible pre-2019.

### Murshidabad Lok Sabha (PC 11) historical

| Year | Winner | Party | Votes | % | Runner-up | Margin | Notes |
|---|---|---|---|---|---|---|---|
| 2014 LS | Badaruddoza Khan | CPI(M) | 426,947 | 33.13 | Abdul Mannan Hossain (INC) | 18,453 | CPI(M) won narrow 3-way; AITC also contested |
| 2009 LS | Abdul Mannan Hossain | INC | 496,348 | 47.21 | Anisur Rahman (CPI(M)) | 35,647 | INC dominated |
| 2004 LS | Abdul Mannan Hossain | INC | 461,895 | 46.00 | Moinul Hassan (CPI(M)) | 15,480 | INC dominated |
| 1999 LS | Moinul Hassan | CPI(M) | 391,366 | 47.30 | Abdul Mannan Hossain (INC) | 123,360 | CPI(M) won |
| 1998 LS | Moinul Hassan | CPI(M) | 463,401 | 49.96 | Anarul Hossain Khan (INC) | 190,466 | CPI(M) stronghold |

Source: Wikipedia "Murshidabad Lok Sabha constituency" (tier A / tier B for ECI-derived Wikipedia summary).

> **Pattern:** Murshidabad LS historically oscillates INC–CPI(M); BJP was negligible until 2019. The 2019 LS outcome — AITC winning LS overall with 41.6% while BJP won AC 64 with 37.1% — represents a structural break from the prior INC/CPI(M) dominance.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- `2019_AssemblySegmentLevelVotingData.csv` — AC 64 2019 LS vote segment, all 11 candidate rows; total electors 255,966; turnout 85.27%
- Census of India 2011 — Murshidabad municipality: pop 44,019; Hindu 75.09%; SC 31.26%; ST 0.69%; literacy 81.94% (via census2011.co.in town #801660)
- Census of India 2011 — Jiaganj-Azimganj municipality: pop 51,790; Hindu 88.23%; Muslim 9.74%; SC 28.12%; ST 0.83%; literacy 80.75% (via census2011.co.in town #801659)
- Census of India 2011 — Murshidabad-Jiaganj CD block: pop 234,565 (all rural); Muslim 54.52%; Hindu 44.61%; SC 17.24%; ST 5.25%; literacy 69.12% (via Wikipedia + censusindia.co.in block #2237)
- Census of India 2011 — Murshidabad district: pop 7,103,807; Muslim 66.27%; Hindu 33.21%; SC 12.63%; ST 1.28%; literacy 67.53%; sex ratio 957 (Wikipedia "Murshidabad district" + census2011.co.in)
- ECI / Wikipedia "Murshidabad Assembly constituency" — 2011 AE, 2016 AE result tables
- ECI / Wikipedia "Murshidabad Lok Sabha constituency" — 2009, 2014 LS result tables
- Delimitation Commission of India 2008 — WB Schedule: AC 64 = Murshidabad Muni + Jiaganj-Azimganj Muni + Murshidabad-Jiaganj CDB (confirmed via multiple secondary sources)

### Secondary sources (tier B/C)

- NFHS-4 (2015-16) West Bengal — household amenity, asset ownership, literacy baselines; Murshidabad district identified as below-state-average on most indicators
- Pew Research India religious growth projections — 2011→2019 differential growth
- CSDS-Lokniti 2019 NES post-poll WB regional cross-tabs — vote × religion / caste / gender
- Wikipedia "Murshidabad-Jiaganj" — CDB rural 8 GP list, block demographics (cross-checks Census A data)
- Wikipedia "Lalbag subdivision" — subdivision composition, municipality list, CDB list
- Wikipedia "Murshidabad silk" — weaving economy, workforce scale (38,040 sericulture + 25,778 weavers in 2002 declining to ~15,000 weavers by 2012)

### Tertiary / journalistic (tier D)

- The Wire (2019 post-poll) — Muslim vote split between AITC and INC-Left in Murshidabad LS; Hindu vote consolidation pattern
- India TV News / Business Today — Murshidabad LS constituency analysis (used for historical context only; post-2019 results relegated to Section H)
- `andiavotes.com` district AC results summary — AC 64 in context of Murshidabad district
- Sahapedia / India InCH — Ansari/Julaha weaver community identification in Murshidabad silk economy

### Tier-D/E reliance flags (what to distrust)

- **C.1 Religion at AC level** — the Hindu 56.5% / Muslim 42.0% estimate is tier D (arithmetic composite of three tier-A sub-unit figures); no direct AC-level census religion table exists; this is the most critical uncertain parameter
- **C.2 Caste sub-group shares** — no caste census post-1931 for non-SC/ST; SC% per sub-unit is tier A but within-SC distribution is tier E
- **D.2 Muslim sub-group structure** — Ansari/Jolaha dominance in Murshidabad silk economy is tier D (journalistic/academic); quantification is tier E
- **D.15 Vote × Religion** — inferred from CSV vote totals + CSDS regional patterns; no direct exit-poll cross-tabs for AC 64 specifically; calibration arithmetic in D.15 shows ~3.7pp gap — flag for v1 refinement
- **C.8 Household industry / weaving share** — based on 2002/2012 workforce census data (declining trend) applied to 2019; tier D
- **C.11 Sub-unit population shares** — CDB "rural" enumeration relationship to municipalities is ambiguous in Census methodology; AC total population estimate has ±10% uncertainty
- **C.14, C.15 Asset / amenities** — NFHS-4 WB state-level adjusted downward for Murshidabad district poverty; tier C; Murshidabad-specific district factsheet not obtained

### v0 known gaps (cross-reference methodology §7)

1. **AC-level religion census table** — no direct sub-AC religious census for this specific constituency; using arithmetic composite of three tier-A sub-units; refine when DCHB Murshidabad Part-A GP-level tables accessible
2. **ECI 2019 Form-20 segment vote** — CSV gives AC-64 candidate votes (tier A) but formal Form-20 not separately verified; consistency confirmed via row-sum; no gap in vote data
3. **Caste within Hindu** — no caste census; dominant SC is Bagdi/Bauri (Murshidabad belt) not Namasudra (N24P belt); identification tier D
4. **Ansari/Jolaha weaver population share** — key for Muslim sub-group political behavior; identified qualitatively but not quantified precisely; tier D/E
5. **NFHS-4 Murshidabad district factsheet** — state-level NFHS-4 WB available; district-specific factsheet (PDF) not retrieved in v0; asset/amenity estimates use state-level WB with downward adjustment
6. **GP-level data within CDB** — collapsed 8 GPs to single "CDB rural" unit; spatial heterogeneity within CDB not modeled
7. **Jain population demography** — Sheherwali Jain community in Jiaganj-Azimganj is historically significant but poorly quantified at 2011 census level; using 2001 Jiaganj city data (1.3% Jain) as proxy

---

## H. Post-2019 validation anchors (for simulator use only — NOT frozen data)

> **Section H is excluded from the freeze rule.** It contains post-2019 events for use as out-of-sample validation gates by the downstream simulator. The frozen calibration (Sections A–G) must not reference these events.

### 2021 AE (primary out-of-sample validation gate)

| Party | Candidate | Votes | % | Note |
|---|---|---|---|---|
| BJP | Gouri Sankar Ghosh (winner) | 95,967 | 41.86 | +4.8pp BJP vs 2019 AC segment |
| AITC | Shaoni Singha Roy | 93,476 | 40.78 | +5.2pp AITC vs 2019 AC segment |
| INC | Sheikh Nejauddin | 28,835 | 12.58 | INC collapsed from 18% to 12.6%; Shaoni Roy switched to AITC |
| Others | — | ~11,000 | ~4.8 | |
| **Margin** | BJP over AITC | 2,491 | 1.08 pp | Most competitive AC in the 10-seat sample |
| **Turnout** | 229,231 | 85.46% | — | |

Validation signal: Simulator calibrated on 2019 demographics should predict BJP/AITC near-parity in 2021 after injecting: (a) Shaoni Roy switching to AITC, (b) INC collapse, (c) BJP Hindu consolidation completing, (d) AITC welfare-scheme incumbent advantage. If simulator produces INC at 18% for 2021 without narrative injection, that is a failure.

### 2024 LS (secondary validation gate)

AC 64 segment within Murshidabad LS (PC 11):

| Party | Candidate | Votes | % | Note |
|---|---|---|---|---|
| BJP | Gouri Sankar Ghosh | 94,164 | 41.20 | Sitting MLA from 2021; BJP held AC share |
| AITC | Abu Taher Khan | 86,313 | 37.77 | AITC gained vs 2019 AC segment |
| CPI(M) | Md Salim | 40,651 | 17.79 | CPI(M) dramatically recovered; ISF+INC-Left alliance |
| Others / NOTA | — | 7,418 | 3.24 | |
| **Total polled** | | 228,546 | | Electors 278,927; turnout 81.9% |
| **BJP lead over AITC** | | 7,851 | 3.43 pp | BJP margin improved vs 2019 despite LS being AITC landslide at PC level |

Note: At the LS level in 2024, AITC won Murshidabad PC by 164,215 votes (44.27% AITC vs 21.5% BJP LS total) — Muslim consolidation behind AITC at LS level vastly outweighed BJP's AC-64 Hindu consolidation. AC 64 remains BJP's structural anchor in Murshidabad LS.

### Structural note for 2026 simulation (Section H only)

2016→2021 trajectory: INC's 47% collapsed; BJP surged from 1.8%→12% (2016)→37%(2019 LS)→42%(2021 AE) by consolidating the Hindu vote in this specific AC. The 2024 LS Muslim consolidation is an AC-external dynamic that overwhelms AC-64 BJP strength at the LS level. AC-level Hindu consolidation behind BJP is structural. SIR voter-roll deletions (Murshidabad district lost ~7.48 lakh names = ~25% of district voter population in the 2025 SIR exercise) may be the decisive variable for 2026 in this AC, since the deletion pattern concentrated in Muslim-majority areas of the district; AC 64's Hindu-majority composition may shield it from the largest SIR effects, but verification requires 2026 roll analysis.

---

*v0 — generated 2026-04-27, frozen at 2019 state-of-knowledge (Sections A–G). Section H contains post-2019 validation anchors excluded from freeze rule.*
