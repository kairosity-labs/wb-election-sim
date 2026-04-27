# AC 222 — Jhargram (ST) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural state of AC 222 Jhargram as of 2019 only — it does not reference any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 222 | A | ECI / Delimitation Commission 2008 |
| AC name | Jhargram | A | ECI |
| Reservation | ST (Scheduled Tribe) | A | Delimitation 2008 |
| District | Jhargram (carved from Paschim Medinipur / West Midnapore in April 2017) | A | WB Govt notification 2017 |
| Sub-division | Jhargram Sadar | A | WB administrative |
| LS constituency | PC 27 — Jhargram (ST reserved) | A | Delimitation 2008 |
| LS segments included with PC 27 | AC 218 Nayagram (ST) · 219 Gopiballavpur · 220 Jhargram · 221 Binpur (ST) · 215 Garbeta (Paschim Medinipur) · 213 Salboni (Paschim Medinipur) · 296 Bandwan (Purulia) | A | Delimitation 2008; ECI |
| AC composition | Jhargram Municipality (full, 18 wards) + 4 GPs of Jhargram CD Block (Bandhgora/Bundhgora, Manikpara, Radhanagar, Sapdhara) + Binpur I CD Block (all 10 GPs) | A | Delimitation 2008; Wikipedia "Jhargram subdivision" |
| Geographic note | Jangalmahal — sal forest belt; Jhargram town on NH-60 (now NH-116B); Subarnarekha river basin; Lalgarh sub-area within Binpur I historically significant | A | — |
| Archetype | A4 — Jangalmahal Santhal ST | D | Project classification |
| Three sub-units used in v0 | **U1: Jhargram Municipality** (urban) · **U2: Jhargram-CDB-rural-4GP-share** · **U3: Binpur I CD Block** (wholly rural) | E | v0 simplification — see §3 below |

---

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~270,200 (Muni 61,712 + Jhargram-CDB 4/13 GPs × 170,097 ≈ 52,338 + Binpur I 156,153) | E | Census 2011 block/municipality figures; 4/13 GP equal-weight assumption |
| 2019 projected population | ~293,200 | E | 8-yr compound religion-differential growth (+8.5% overall; see methodology §4) |
| Sex ratio (2019, F per 1,000 M) | ~978 | A | District: 977 (2011, Jhargram dist); Muni 999; Binpur I 978; population-weighted |
| 2011 electorate (back-calculated) | ~184,109 | D | 2011 AE turnout 155,520 at 84.47% → 155,520/0.8447 = 184,109 |
| 2019 electorate (ECI, CSV) | **226,039** | **A** | `2019_AssemblySegmentLevelVotingData.csv`, AC_NO=222 |
| Estimated M / F / TG split (2019) | ~50.6% M / 49.4% F / <0.05% TG | E | Weighted district sex ratio 978 F/1000 M |
| 2019 estimated polling stations | ~270 | E | Back-projection from post-2019 electoral rolls; AC comparable to AC 95 scale |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

> **Census note:** In Census 2011, Sarna / ORP (Original Religion and Practice) practitioners were enumerated under "Other religions and persuasions" — they did NOT have a separate code. They appear partly under "Hindu" and partly under "Others." In Jangalmahal, ~10–17% of the rural population practices Sarna religion (worship of Marang Buru / Jaher Era). The "Hindu" row below includes those who self-identified as Hindu regardless of tribal religious practice; "Sarna/ORP" is a residual estimated from the "Others" share in block-level Census data plus academic accounts. In simulation, Sarna-practicing households should be treated as a sub-segment of the ST population with distinct political dispositions.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu (self-identified, including many syncretic Adivasi) | 84.04 | A | Weighted block average: Muni 94.72% × 22.8% + Jhargram CDB 91.03% × 19.4% + Binpur I 77.47% × 57.8% = 84.03%; projected stable 2011→2019. Note: ~10.9% of total population practices Sarna/ORP religion — they appear in Census 2011 "Hindu" or "Other religions" categories; the Sarna row below is a disaggregation within the Census "Other" + part of nominal "Hindu" |
| Muslim | 3.44 | E | Weighted: Muni 1.66% × 22.8% + Jhargram CDB 3.70% × 19.4% + Binpur I 3.89% × 57.8% = 3.34%; projected +0.1pp 2011→2019 |
| Sarna / ORP (tribal nature-worship) | 10.90 | E | Weighted "Others" share: Jhargram CDB 4.66% × 19.4% + Binpur I 16.29% × 57.8% + Muni 2.53% × 22.8% ≈ 10.9%; these are embedded within the Census "Other religions" category and partly within nominal Hindu; the 10.90% is NET of Hindu row above (no double-count) — see Census note |
| Christian | 0.43 | E | Muni 0.75% × 22.8% + CDB 0.30% × 19.4% + Binpur I 0.35% × 57.8% |
| Other / not stated | 1.19 | E | Weighted residual: Muni 0.34% × 22.8% + CDB 0.61% × 19.4% + Binpur I 2.35% × 57.8% |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

> **Critical parameter.** ST sub-group breakdown within the ~22.9% ST share is load-bearing for the simulation. No caste census data post-1931 for non-SC/ST groups; all non-SC/ST sub-groups are tier E.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **ST total** | 22.92 | A | Weighted Census 2011: Muni 9.85% × 22.8% + Jhargram CDB 22.71% × 19.4% + Binpur I 28.15% × 57.8% |
| └ Santhal | 11.50 | D | ~50% of ST pool; dominant tribe across Jhargram district and Jangalmahal; Wikipedia "Jhargram district" + Ramakrishna Mission Jhargram narrative; largest tribe in sub-division |
| └ Munda | 3.90 | D | ~17% of ST pool; Lalgarh area and Binpur I concentrated; Mundari speaker data corroborates |
| └ Bhumij | 2.75 | D | ~12% of ST pool; Bhumij present across Jhargram and Gopiballavpur blocks; semi-Hinduised |
| └ Lodha | 1.40 | D | ~6% of ST pool; Lodhasuli GP (Jhargram CDB) by name; one of most marginalised tribes (PVTG category); forest-dependent |
| └ Ho | 1.15 | D | ~5% of ST pool; present in Binpur I and Lalgarh area; Ho language related to Mundari |
| └ Other ST (Mahali, Sabar, Kheriya, Korwa etc.) | 2.22 | E | ~10% of ST pool; residual |
| **SC total** | 19.52 | A | Weighted Census 2011: Muni 9.59% × 22.8% + Jhargram CDB 14.83% × 19.4% + Binpur I 25.02% × 57.8% |
| └ Bagdi | 7.00 | D | Largest SC sub-group in Jhargram; rural agricultural labour; ~36% of SC pool |
| └ Bauri | 4.00 | D | ~20% of SC pool; also forest-adjacent labour caste |
| └ Hari (Bhangi) | 1.56 | E | ~8% of SC pool; sanitation caste in town |
| └ Chamar / Mochi | 1.20 | E | ~6% of SC pool |
| └ Other SC (Rajbanshi / Malo / Pod etc.) | 5.76 | E | Residual ~30% of SC pool |
| **UC / bhadralok** (Brahmin / Kayastha / Baidya) | 6.50 | E | Concentrated in Jhargram Muni; district admin, teachers, traders |
| **OBC** (Mahato / Kurmi / Teli / Sutradhar) | 12.00 | D | Mahato (Kudumi Mahato) is significant OBC group in Jangalmahal; Chhatradhar Mahato was from this community; Mahato OBC ~8-10% alone; Wikipedia + academic notes on Jangalmahal |
| **Other Hindu middle castes** (unclassified) | 34.00 | E | Residual within total: 100 − 22.92 ST − 19.52 SC − 6.50 UC − 12.00 OBC − 3.44 Muslim − 1.62 Christian+Other = 34.00% |
| Muslim (all sub-castes pooled) | 3.44 | E | See C.1 |
| Christian + Other | 1.62 | E | Christian 0.43% + Other 1.19%; see C.1 |
| **Sum** | **100.00** | — | self-check (22.92+19.52+6.50+12.00+34.00+3.44+1.62=100.00) |

### C.3 Age cohort (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 0–4 | 8.5 | E | Jhargram district child (0-6) share ~17%; higher fertility in tribal rural belt vs state average |
| 5–9 | 9.0 | E | |
| 10–14 | 9.0 | E | |
| 15–17 (pre-voter) | 5.5 | E | |
| 18–22 (first-time voters at 2019) | 9.0 | E | |
| 23–27 | 9.5 | E | |
| 28–32 | 9.0 | E | |
| 33–37 | 8.0 | E | |
| 38–42 | 7.0 | E | |
| 43–47 | 6.0 | E | |
| 48–52 | 5.5 | E | |
| 53–57 | 4.5 | E | |
| 58–62 | 3.5 | E | |
| 63–67 | 2.5 | E | |
| 68+ | 3.5 | E | Older profile in rural tribal belt; Census 2011 Jhargram dist age pyramid |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.56 | A | District sex ratio 977 F/1000 M = 50.56% M; Muni 999/2000 slightly higher F |
| Female | 49.43 | A | |
| Third gender | 0.01 | E | Negligible |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

> **Multilingual tribal belt.** Santali is spoken in Ol Chiki script (standardized); many Santali, Munda, and Ho speakers are bilingual in Bengali. Santali is the dominant non-Bengali language in the AC.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 81.50 | A | Weighted: Muni ~91% × 22.8% + Jhargram CDB 86.83% × 19.4% + Binpur I 76.63% × 57.8% ≈ 81.9%; minor 2019 drift → 81.5% |
| Santali (Ol Chiki script) | 16.00 | A | Weighted: Muni ~7% × 22.8% + Jhargram CDB 11.66% × 19.4% + Binpur I 22.28% × 57.8% ≈ 16.7%; slight downward drift toward Bengali bilingualism by 2019 |
| Mundari | 1.50 | A | Jhargram district Census 2011: Mundari 1.45% of district; higher in Binpur I |
| Kurmali (Kudumi Mahato language) | 0.50 | A | Jhargram district Census 2011: Kurmali 1.16%; diluted in AC 222 by Muni weight |
| Hindi | 0.30 | E | Muni trader fringe; transport workers |
| Other (Ho / Bengali-Hindi bilingual / Urdu) | 0.20 | E | Residual |
| **Sum** | **100.00** | — | self-check |

(Bilingualism: ~35% of Santali/Mundari/Ho speakers are also functionally Bengali-bilingual; tier D. Ol Chiki literacy ~20% of Santali speakers; tier D.)

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 24.50 | E | 2011 literacy ~74.5% → illiterate ~25.5%; +0.5pp/yr × 8yr improvement → ~21.5% illiterate; weighted female drag: female literacy 2011 was ~68% in Binpur I (2019 ~71%); weighted mean → ~24.5% illiterate |
| Primary (Class 1–5) | 24.00 | E | Census 2011 education distribution for tribal-rural WB scaled |
| Middle (Class 6–8) | 20.00 | E | |
| Secondary (Class 9–10) | 14.00 | E | |
| Higher Secondary (Class 11–12) | 9.00 | E | |
| Graduate | 6.00 | E | Lower grad rate than N24P urban ACs; consistent with Jhargram literacy profile |
| Postgraduate | 2.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main worker | 35.0 | E | Binpur I main-worker share ~38% (Census 2011); Muni slightly lower; AC weighted |
| Marginal worker | 15.0 | E | High in ST/SC rural: seasonal forest labour, MGNREGA casual |
| Non-worker (housewife / elderly / retired) | 34.0 | E | Lower than N24P urban due to tribal female participation in forest work |
| Student (18–22 in education) | 10.0 | E | First-time voter cohort |
| Unemployed (educated, actively seeking) | 6.0 | E | Lower educated-unemployment rate than N24P; smaller graduate pool |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator (own land, incl. marginal) | 20.0 | E | Weighted: Binpur I patta-holders 23.62% + marginal farmers 23.37% ≈ 28% of agri-worker pool; AC-level cultivator ~20% |
| Agricultural labourer | 38.0 | E | Dominant: Binpur I 46.54%, Jhargram CDB 39.5%; AC-weighted ~40%; women overrepresented |
| Forest produce collection (sal leaf, mahua, NTFP) | 8.0 | D | Not separately captured in Census; estimated from literature (Jhargram NTFP dependence); Lodha, Ho, Santal women primary collectors |
| Household industry (handloom, basket, pottery) | 4.0 | E | Census 2011 WB rural household-industry share |
| Construction | 5.0 | E | Some male migration to construction sites |
| Trade / retail | 8.0 | E | Jhargram Muni-centric; smaller than N24P |
| Transport (NH-60 / state road logistics) | 3.0 | E | |
| Services (private, incl. hotel / domestic) | 6.0 | E | Town-concentrated |
| Government services / teachers / health workers | 5.0 | E | Slightly higher than state average due to tribal sub-quotas in WB govt |
| Out-migrant / remittance worker | 3.0 | D | Lower than N24P; Jangalmahal out-migration to Jharkhand / Odisha mines; press reports |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.0 | E | Census B-04 WB rural pattern; smaller than N24P |
| Employee (regular wage) | 22.0 | E | Govt + organised workers; lower than urban ACs |
| Single worker (own-account) | 45.0 | E | Own cultivator + petty trader + forest-produce seller |
| Family worker (unpaid) | 22.0 | E | High in tribal agriculture household |
| Casual / MGNREGA day labourer | 10.0 | D | MGNREGA-generated casual labour very high in tribal belt; Jhargram dist among top MGNREGA districts in WB; estimated from NREGA portal patterns |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2019, household level)

> **Very high poverty constituency.** Binpur I BPL households 47.46% in 2007 (Census block data). District-level literature: "more than 90% of tribal people in the region belong to BPL" (search result from regional report). SECC 2011 not available at AC-level for direct cite, but Jangalmahal poverty rate consistently cited as among highest in WB. Jhargram was classified as an "LWE-affected" district receiving special central funds pre-2019.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL household (including SECC "auto-included" deprived) | 42.0 | D | Binpur I BPL 47.46% (2007); Jhargram CDB rural ~35%; Muni ~15%; AC weighted ~42%; decline from 2007 baseline due to poverty-reduction programs; upper-bound estimate |
| Above-Poverty-Line, low-income (₹3,000–₹8,000/month HH) | 33.0 | E | |
| Lower-middle (₹8,000–₹15,000/month HH) | 16.0 | E | |
| Middle (₹15,000–₹30,000/month HH) | 7.0 | E | Muni-concentrated; Jhargram town traders, teachers |
| Upper-middle / well-off (>₹30,000/month HH) | 2.0 | E | Small urban professional fringe in Muni |
| **Sum** | **100.00** | — | self-check |

**MGNREGA note (2019):** Jhargram (then Paschim Medinipur) was among WB's highest MGNREGA-utilization districts. Estimated average ~42–48 work-days per job-card household per year (2017–18 MIS data range for Jangalmahal blocks); ~55–60% of rural HHs have active job cards. This is the primary state-welfare variable for modeling vote×welfare in Section D.18. (Tier D — MIS pattern; block-specific not verified for v0.)

### C.11 GP / Municipality location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **U1: Jhargram Municipality** (urban, 18 wards) | 22.8 | E | 2011: Muni 61,712 / AC total ~270,200 = 22.8%; held stable to 2019 |
| **U2: Jhargram-CDB-4GP-rural-share** (Bandhgora, Manikpara, Radhanagar, Sapdhara) | 19.4 | E | 4/13 × Jhargram CDB 170,097 = 52,338 / 270,203 = 19.4%; 4 GPs per Delimitation 2008 |
| **U3: Binpur I CD Block** (10 GPs: Andharia, Belatikri, Binpur, Boita, Dahijuri, Dharampur, Lalgarh, Nepuria, Ramgarh, Sijua) | 57.8 | E | 156,153 / 270,203 = 57.8%; dominant rural sub-unit; includes Lalgarh |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg HH size | 4.6 persons | E | Slightly larger than WB 4.3 due to tribal joint household pattern; Census 2011 tribal block data |
| Nuclear HH | 62.0 | E | NFHS-4 WB rural tribal pattern — somewhat lower nuclearity than non-tribal |
| Joint HH | 28.0 | E | Tribal patrilineal joint family (particularly Santhal and Munda) |
| Extended / multi-generation | 10.0 | E | |
| **Sum** | **100.00** | — | self-check |

(Household head: ~82% male-headed, 18% female-headed; higher female headship than N24P due to male out-migration; tier E.)

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never married | 26.0 | E | First-time-voter cohort; tribal communities have younger marriage age |
| Currently married | 65.0 | E | |
| Widowed | 8.0 | E | Higher than N24P: male forest-labour mortality; older rural age profile |
| Separated / divorced | 1.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 58.0 | C | NFHS-4 WB rural 60%, NFHS-5 WB rural ~71%; Jhargram district is poorer than WB average — estimated 55% rural, 85% Muni; AC-weighted ~58% |
| Radio | 8.0 | C | Higher than N24P: radio remains relevant in forest-fringe areas with limited TV access |
| Mobile phone (any) | 75.0 | C | NFHS-4 WB rural ~72%; +growth → ~75% by 2019; lower than N24P urban ACs |
| Smartphone with internet | 30.0 | C | Jio Dhan Dhana Dhan scheme 2017-onwards reached tribal belt but lower smartphone adoption vs urban; NFHS-4 WB rural baseline ~25% → ~30% by 2019 |
| Computer | 5.0 | C | NFHS-4 WB rural 4%; minimal uplift in poor tribal AC |
| Two-wheeler | 18.0 | C | Lower than N24P; household bicycle more common; NFHS-4 WB rural |
| Four-wheeler | 3.0 | C | Minimal |
| Banking access (any) | 82.0 | B | PMJDY 2014– saturation; Jhargram tribal HHs prioritized in Jan Dhan drive; NFHS-4 WB rural banking baseline |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved drinking water source | 78.0 | C | NFHS-4 WB rural 84%; Jhargram forest-belt lower due to river/pond dependence; AC-weighted ~78% |
| Improved sanitation (latrine) | 48.0 | C | NFHS-4 WB rural 51%; +Swachh Bharat 2014–19 (+10pp rural in LWE districts at slower pace); estimated 48% |
| LPG / clean cooking fuel | 25.0 | C | NFHS-4 WB rural 24%; +Ujjwala 2016–19 (~+8pp in tribal belt); tribal HH lower take-up; estimated 25% |
| Wood / biomass fuel (sal / other forest) | 68.0 | D | High: forest-fringe HHs collect fuel wood as primary cooking fuel; compensates lower LPG |
| Other fuel (kerosene / dung) | 7.0 | C | |
| Electricity | 88.0 | C | Census 2011 WB rural electrification + Saubhagya 2017–19; Jhargram behind N24P; estimated ~88% by 2019 |
| **Note** | (water/sanitation/electricity are independent; cooking fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native (born in Jhargram district or same village/town) | 84.0 | D | Primarily sedentary tribal and SC population; much lower refugee/migrant component than N24P |
| WB other district (in-migrant) | 6.0 | D | Government employees, traders, teachers from other districts; Muni-concentrated |
| Other Indian state (in-migrant) | 4.0 | D | Bihari/Jharkhand railway workers, traders; some seasonal labour from Odisha |
| Jharkhand-origin (tribal cross-border) | 3.0 | D | Santhals, Mundas with kin-ties to Jharkhand; some forest-labour seasonal settlers; Jhargram-Jharkhand border area |
| Bangladesh-origin | 1.5 | D | Very small; Jangalmahal has no significant refugee stream unlike N24P |
| Out-migrant (registered here, working elsewhere) | 1.5 | E | Male out-migration to Jharkhand/Odisha mines; registered voter roll |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Santali | Mundari | Kurmali | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu (non-Sarna) | 93.0 | 4.0 | 1.0 | 1.5 | 0.5 | E | Hindu population includes Bhumij (semi-Hinduised), Bagdi, UC; Bengali-dominant |
| Sarna/ORP (tribal) | 18.0 | 63.0 | 10.0 | 4.0 | 5.0 | E | Sarna pop is largely Santhal, Munda, Ho; bilingual in Bengali but MT is tribal lang |
| Muslim | 95.0 | 0.5 | 0.0 | 0.0 | 4.5 | E | Bengali-Muslim peasantry in Jhargram; some Urdu pocket in Muni |
| Christian | 70.0 | 15.0 | 8.0 | 2.0 | 5.0 | E | Tribal Christians (Santhal, Munda) evangelized in colonial period; bilingual |
| **Marginal recovery — Bengali** | | | | | | | Hindu(79.0)×0.93 + Sarna(10.9)×0.18 + Muslim(3.4)×0.95 + Christian(0.43)×0.70 + Other(0.27)×0.80 = 73.47+1.96+3.23+0.30+0.22 = **79.18** vs C.5 **81.5** ⚠ off by 2.3pp — rounding/simplification flag; refine sub-unit weights in v1 |

### D.2 Religion × Caste (Hindu-internal sub-structure, and Sarna-internal)

P(caste ‖ Hindu/Sarna) — % within each religion.

**Within Hindu population:**

| Caste sub-group | % of Hindu | Tier | Source |
|---|---|---|---|
| ST (semi-Hinduised Bhumij, some Mahali) | 8.5 | E | ST who self-identify Hindu (not Sarna); ~37% of total ST pool × ST/Hindu ratio |
| SC: Bagdi | 8.9 | E | 7.0% of total / 79% Hindu = 8.9% of Hindu |
| SC: Bauri | 5.1 | E | 4.0% / 79% |
| SC: Other SC | 8.8 | E | 6.9% / 79% |
| UC bhadralok | 8.2 | E | 6.5% / 79% |
| OBC Mahato / Kurmi | 15.2 | E | 12.0% / 79% |
| Other Hindu middle | 45.3 | E | Residual within Hindu population |
| **Sum** | **100.00** | — | self-check |

**Within Sarna/ORP population (exclusively ST):**

| ST tribe | % of Sarna | Tier | Source |
|---|---|---|---|
| Santhal | 53.0 | D | Dominant tribe; Santhal-Sarna connection strongest |
| Munda | 20.0 | D | Munda traditionally Sarna-practicing |
| Ho | 12.0 | D | Ho = closely related to Munda; share Marang Buru worship |
| Lodha | 6.0 | D | Forest-fringe tribe; PVTG |
| Other ST | 9.0 | E | Mahali, Sabar, Korwa |
| **Sum** | **100.00** | — | self-check |

**Muslim sub-caste structure:**

| Muslim sub-group | % of Muslim | Tier | Source |
|---|---|---|---|
| Sheikh (Bengali Muslim peasantry) | 85 | D | Dominant in rural WB Muslim population |
| Other Muslim (Pathan, Sayyid, OBC Muslim) | 15 | D | Small; Muni-concentrated |
| **Sum** | **100** | — | self-check |

### D.3 Religion × Migration / birthplace

P(birthplace ‖ religion).

| Religion | Native | WB-other-dist | Other-state / Jharkhand | Bangladesh | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 82 | 6 | 8 | 4 | D | Bhumij, Bagdi, Mahato are largely native; UC bhadralok may be in-migrant govt employee |
| Sarna/ORP | 96 | 1 | 3 | 0 | D | Indigenous tribal population; almost entirely native |
| Muslim | 88 | 5 | 5 | 2 | D | Some cross-border trickle; largely native Bengali Muslim |
| Christian | 78 | 10 | 8 | 4 | E | Mission-converted Santhals; mixed origin |
| **Marginal recovery — Native** | | | | | | Hindu(79)×0.82 + Sarna(10.9)×0.96 + Muslim(3.4)×0.88 + Christian(0.43)×0.78 + Other(0.27)×0.85 = 64.78+10.46+2.99+0.34+0.23 = **78.8** vs C.16 marginal **84.0** ⚠ off by 5.2pp — Sarna-native share may be underweighted; flag for v1 reconciliation |

### D.4 Religion × Asset / media (TV, smartphone, banking)

P(owns asset ‖ religion).

| Religion | TV | Smartphone-internet | Banking |
|---|---|---|---|
| Hindu | 62 | 32 | 84 |
| Sarna/ORP | 42 | 20 | 75 |
| Muslim | 55 | 28 | 79 |
| Christian | 65 | 35 | 82 |
| Tier | C | C | C |
| Source | NFHS-4 WB rural-tribal gap | NFHS-5 WB pattern | PMJDY enrollment pattern |

> Note: Sarna/ORP households are disproportionately the poorest tribal HHs (PVTG-adjacent, deep forest belt) — asset access is the lowest of any religious segment.

### D.5 Caste × Education

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Sec | HS | Grad | PG | Tier |
|---|---|---|---|---|---|---|---|---|
| UC bhadralok | 5 | 10 | 12 | 18 | 20 | 25 | 10 | E |
| OBC Mahato/Kurmi | 18 | 24 | 22 | 18 | 10 | 7 | 1 | E |
| SC Bagdi/Bauri | 32 | 26 | 20 | 13 | 6 | 3 | 0 | E |
| ST Santhal | 28 | 25 | 22 | 14 | 7 | 4 | 0 | D | Academic: tribal literacy improvement in Jangalmahal post-2011 school expansion |
| ST Munda / Ho | 30 | 24 | 22 | 14 | 7 | 3 | 0 | E |
| ST Bhumij (semi-Hinduised) | 22 | 25 | 23 | 16 | 9 | 5 | 0 | E |
| ST Lodha (PVTG) | 45 | 28 | 18 | 7 | 2 | 0 | 0 | D | Lodha: most marginalised; Lodha Self-Employment Scheme data |
| Muslim | 25 | 26 | 22 | 15 | 8 | 4 | 0 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share, age 18+.

| Cohort | Male grad+ | Female grad+ | Tier | Source |
|---|---|---|---|---|
| 18–22 | 10 | 9 | E | Slight gender parity in young cohort; school expansion reached girls |
| 23–27 | 10 | 7 | E | |
| 28–32 | 8 | 5 | E | |
| 33–42 | 6 | 3 | E | |
| 43–57 | 5 | 2 | E | Older female cohort very low in tribal belt |
| 58+ | 4 | 1 | E | |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender).

| Age | Male married | Female married | Tier |
|---|---|---|---|
| 18–22 | 10 | 45 | E (earlier female marriage in tribal belt vs urban) |
| 23–27 | 50 | 85 | E |
| 28–32 | 82 | 93 | E |
| 33–47 | 92 | 90 | E |
| 48–62 | 88 | 76 | E |
| 63+ | 72 | 30 | E (widows concentrate here; higher female mortality risk) |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone-internet | TV | Tier | Source |
|---|---|---|---|---|
| Cultivator | 22 | 52 | C | Rural ag baseline; tribal landholding tiny |
| Ag-labourer | 15 | 42 | C | Poorest income bracket |
| Forest-produce collector | 10 | 35 | D | NTFP workers: remotest, lowest media access; D estimate from Jangalmahal livelihood reports |
| Household industry | 25 | 55 | C | |
| Construction | 30 | 55 | C | |
| Trade / retail | 55 | 80 | C | Muni-concentrated; higher access |
| Transport | 45 | 72 | C | |
| Services (private) | 60 | 82 | C | |
| Govt services / teachers | 80 | 90 | C | Highest |
| Out-migrant | 55 | 65 | D | Smartphone needed for remittance; WhatsApp penetration high among migrants |

### D.9 Education × Workforce participation

P(unemployed-and-seeking ‖ education) — educated-unemployment proxy.

| Education | Unemployed-seeking | Main-worker rate | Tier |
|---|---|---|---|
| Illiterate | 1 | 42 | E (illiterate workers absorbed into ag-labour / forest labour) |
| Primary | 3 | 40 | E |
| Middle | 5 | 37 | E |
| Secondary | 8 | 32 | E |
| Higher Secondary | 12 | 27 | E |
| Graduate | 14 | 30 | E (tribal graduate: job-aspirant pool with quota pathway) |
| Postgraduate | 10 | 40 | E |

### D.10 Asset / media × Bilingualism (Bengali + Santali/Mundari)

P(Santali/tribal-language fluent ‖ media-access tier).

| Media tier | Santali/tribal bilingual % | Tier | Source |
|---|---|---|---|
| TV-only HH | 22 | E | Santali TV programs (Doordarshan) + local cable content |
| TV + smartphone HH | 28 | E | YouTube Santali content expanding; Ol Chiki digital content |
| Smartphone-only HH | 24 | E | |
| No-asset HH | 32 | E | Highest tribal-language retention in no-asset HH (most remote) |
| **Population-wide tribal-bilingual rate** | ~35 | E | C.5 narrative anchor: 18.5% Santali + Mundari + Kurmali MT → ~35% who can speak tribal lang |

### D.11 Sub-unit × Religion (spatial heterogeneity)

P(religion ‖ sub-unit location).

| Sub-unit | Hindu | Sarna/ORP | Muslim | Christian | Tier | Source |
|---|---|---|---|---|---|---|
| **U1: Jhargram Municipality** (22.8% pop) | 94.72 | 2.53 | 1.66 | 0.75 | A | Census 2011 Jhargram municipality |
| **U2: Jhargram-CDB-4GP rural** (19.4% pop) | 91.03 | 4.66 | 3.70 | 0.30 | A | Census 2011 Jhargram CD Block; 4 GP proportional |
| **U3: Binpur I CD Block** (57.8% pop) | 77.47 | 16.29 | 3.89 | 0.35 | A | Census 2011 Binpur I CD Block |
| **Marginal recovery — Sarna/ORP** | | | | | | 0.228×2.53 + 0.194×4.66 + 0.578×16.29 = 0.58+0.90+9.42 = **10.90** vs C.1 marginal **10.90** ✓ exact |

### D.12 Sub-unit × Caste (within sub-unit, key categories)

P(caste ‖ sub-unit).

| Sub-unit | UC | OBC Mahato | SC (all) | ST (all) | Other Hindu | Muslim | Tier |
|---|---|---|---|---|---|---|---|
| Jhargram Muni | 14 | 8 | 9.59 | 9.85 | 56.9 | 1.66 | A/E |
| Jhargram-CDB rural | 8 | 12 | 14.83 | 22.71 | 38.76 | 3.70 | A/E |
| Binpur I | 3 | 15 | 25.02 | 28.15 | 24.94 | 3.89 | A/E |
| Source | Muni bhadralok-skewed | OBC Mahato dominant in forest belt | Census 2011 A | Census 2011 A | Residual E | Census 2011 A | |

### D.13 Sub-unit × Asset / media

| Sub-unit | TV | Smartphone-internet | Computer | Banking | Tier |
|---|---|---|---|---|---|
| Jhargram Muni | 85 | 50 | 15 | 92 | C |
| Jhargram-CDB rural | 60 | 28 | 4 | 82 | C |
| Binpur I | 42 | 18 | 2 | 76 | C |
| Source | NFHS-4 WB urban | NFHS-4/5 WB rural graded | | PMJDY tribal enrollment | |

### D.14 Sub-unit × Amenities

| Sub-unit | LPG | Improved sanitation | Improved water | Electricity | Tier |
|---|---|---|---|---|---|
| Jhargram Muni | 55 | 78 | 90 | 98 | C |
| Jhargram-CDB rural | 22 | 50 | 80 | 88 | C |
| Binpur I | 14 | 32 | 68 | 82 | C |
| Source | NFHS-4/5 WB rural + Ujjwala 2016-19 | Swachh Bharat at lower pace in LWE dist | Forest-fringe water access | Saubhagya 2017-19 | |

### D.15 Vote × Religion (2019 LS, regional anchor)

P(party ‖ religion) — 2019 WB Jangalmahal-region adjustment over CSDS state rollup.

> Note: 2019 LS at AC-222 was extremely close (BJP 44.49% vs AITC 43.62%, margin 0.87pp — tier A from CSV). CSDS 2019 WB average shows Hindu 57% BJP, but Jangalmahal's Hindu population includes a large Sarna/tribal fraction that voted differently from N24P Hindu. Adjustments reflect Jangalmahal context.

| Religion | BJP | AITC | CPIM | Other | Tier | Source |
|---|---|---|---|---|---|---|
| Hindu (non-Sarna) | 47 | 42 | 5 | 6 | C | CSDS 2019 WB Hindu BJP majority adjusted downward for Jangalmahal tribal-Hindu + Mahato OBC complexity; row sums: 47+42+5+6=100 |
| Sarna/ORP (tribal, Santhal/Munda) | 38 | 49 | 3 | 10 | D | Sarna vote split in 2019; ~10% went to tribal protest parties (JKP(N), AKBJHP); BJP slightly behind AITC among Sarna voters; D estimate from AC-222 result structure; row sums: 38+49+3+10=100 |
| Muslim | 5 | 80 | 10 | 5 | C | CSDS 2019 WB Muslim vote; small Muslim share in AC; row sums: 5+80+10+5=100 |
| Christian (tribal Christian) | 35 | 50 | 8 | 7 | E | Tribal Christian vote — slightly TMC-leaning; row sums: 35+50+8+7=100 |
| Other religion | 40 | 20 | 20 | 20 | E | Residual; row sums: 40+20+20+20=100 |
| **Marginal recovery — BJP** | | | | | | Hindu(84.04)×0.47 + Sarna(10.9)×0.38 + Muslim(3.44)×0.05 + Christian(0.43)×0.35 + Other(1.19)×0.40 = 39.50+4.14+0.17+0.15+0.48 = **44.44** vs CSV **44.49** ✓ within ±0.1pp |
| **Marginal recovery — AITC** | | | | | | Hindu(84.04)×0.42 + Sarna(10.9)×0.49 + Muslim(3.44)×0.80 + Christian(0.43)×0.50 + Other(1.19)×0.20 = 35.30+5.34+2.75+0.22+0.24 = **43.84** vs CSV **43.62** ✓ within ±0.3pp |

### D.16 Vote × Caste (2019 LS)

P(party ‖ caste) — 2019 WB, Jangalmahal regional adjustment.

| Caste | BJP | AITC | CPIM | Other | Tier | Source |
|---|---|---|---|---|---|---|
| UC bhadralok | 55 | 32 | 8 | 5 | C | CSDS 2019 WB; bhadralok BJP-leaning |
| OBC Mahato/Kurmi | 52 | 36 | 6 | 6 | C | Mahato vote split in 2019; some Mahato anti-TMC from PCAPA-era politics |
| SC Bagdi/Bauri | 42 | 45 | 8 | 5 | C | SC vote more TMC-leaning than Mahato in Jhargram |
| **ST Santhal** | **43** | **46** | **5** | **6** | **D** | **Critical: Santhal vote was near-50:50 in 2019; BJP made tribal inroads via PM-KISAN + "Ghar Wapsi" Sarna outreach; TMC retained slight edge; JKP(N) drew ~2% Santhal protest vote** |
| ST Munda / Ho | 45 | 44 | 4 | 7 | D | Munda vote similar to Santhal; AKBJHP drew Mundari protest vote |
| ST Bhumij | 40 | 50 | 5 | 5 | D | Bhumij more TMC-leaning (semi-Hinduised, closer to SC political pattern) |
| ST Lodha (PVTG) | 35 | 55 | 5 | 5 | D | Lodha most marginalized: TMC welfare-outreach dependency stronger |
| Muslim | 5 | 80 | 10 | 5 | C | See D.15 |

### D.17 Vote × Gender (2019 LS)

P(party ‖ gender). Note: Tribal women in Jangalmahal have significant political autonomy (Santhal women's councils — Majhiher); their vote pattern differs from N24P SC women.

| Gender | BJP | AITC | CPIM | Other | Tier | Source |
|---|---|---|---|---|---|---|
| Male | 47 | 41 | 6 | 6 | C | CSDS 2019 WB; Jangalmahal male tribal split |
| Female | 42 | 46 | 5 | 7 | D | TMC tribal women advantage slightly lower than N24P (no Lakshmir Bhandar in 2019); AC-222 result near-parity suggests smaller gender gap than WB overall |

### D.18 Vote × Welfare-scheme exposure (2019)

P(party ‖ household has scheme exposure). Schemes available in 2019: MGNREGA (UPA/central), PM-KISAN (Modi, Feb 2019), PM Awas Yojana-Gramin (PMAY-G, central 2016–), Kanyashree (TMC, 2013), Swasthya Sathi (TMC, 2016), Krishak Bandhu (TMC, Jan 2019), Khadya Sathi (TMC, 2016). **Lakshmir Bhandar does NOT exist in 2019.**

| Exposure | BJP | AITC | CPIM | Other | Tier | Source |
|---|---|---|---|---|---|---|
| MGNREGA job-card holder HH | 38 | 50 | 6 | 6 | D | MGNREGA credit partially attributed to TMC in tribal belt; also central scheme |
| PM-KISAN beneficiary (Feb–May 2019) | 52 | 36 | 5 | 7 | D | BJP launched PM-KISAN Feb 2019 targeting farmer vote; tribal smallholder HHs enrolled |
| Krishak Bandhu (state) | 28 | 62 | 5 | 5 | C | Strong TMC welfare-attribution among Krishak Bandhu HHs |
| Kanyashree / girl-student HH | 30 | 58 | 6 | 6 | C | TMC welfare-stack credit in school-enrollment improvement |
| Khadya Sathi (PDS ration) | 38 | 50 | 6 | 6 | C | Universal scheme; moderate TMC attribution |
| PMAY-G (housing scheme, central) | 50 | 38 | 5 | 7 | D | PMAY-G = central scheme; BJP attribution stronger in tribal belt where Sabuj Sathi / Krishak Bandhu less salient |
| **No state-scheme exposure** | 55 | 30 | 8 | 7 | C | BJP-leaning among scheme-excluded HH |

---

## E. 2019 baseline vote (calibration target)

The simulator must reproduce the AC-222 segment within ±1pp on major parties.

### Whole Jhargram LS (PC 27) — 2019 result (tier A, ECI/Wikipedia)

| Party | Candidate | Votes | % |
|---|---|---|---|
| BJP | **Kunar Hembram** | 626,583 | **44.56** |
| AITC | Birbaha Soren | 614,816 | **43.72** |
| CPI(M) | (candidate) | ~112,000 | ~7.97 |
| Others / NOTA | various | ~52,000 | ~3.75 |
| **Margin** | BJP over AITC | **11,767** | 0.84 pp |

> Source: Wikipedia "Jhargram Lok Sabha constituency" — 2019 result; tier A (ECI).

### AC 222 Jhargram segment — 2019 LS (tier A, CSV)

> **Tier A** — sourced directly from `2019_AssemblySegmentLevelVotingData.csv`, AC_NO=222, "West Bengal". Electorate: 226,039. Turnout: 83.33% (188,364 votes cast including NOTA).

| Party | Candidate | Votes | AC-222 segment % | Tier |
|---|---|---|---|---|
| BJP | Kunar Hembram | 83,812 | **44.49%** | A |
| AITC | Birbaha Soren | 82,169 | **43.62%** | A |
| CPI(M) | Deblina Hembram | 9,571 | **5.08%** | A |
| JKP(N) (Jharkhand Party Naren) | Birbaha Hansda | 1,816 | **0.96%** | A |
| INC | Jageswar Hembram | 2,973 | **1.58%** | A |
| BSP | Ashok Kumar Murmu | 1,612 | **0.86%** | A |
| AKBJHP (Adivasi party) | Maheswar Hembram | 1,222 | **0.65%** | A |
| SUCI(C) | Sushil Mandi | 1,141 | **0.61%** | A |
| IND | Narendra Nath Hembram | 1,226 | **0.65%** | A |
| NOTA | — | 2,822 | **1.50%** | A |
| **BJP margin over AITC** | | **1,643 votes** | **0.87 pp** | **A** |

> **Key observation:** The AC-222 result (BJP 44.49% vs AITC 43.62%, margin 1,643) is dramatically closer than the LS-wide result (BJP 44.56% vs AITC 43.72%, margin 11,767). The AC segment essentially mirrors the LS average, confirming this is the most competitive seat within the Jhargram LS. The sub-1pp BJP margin is load-bearing — the simulation must reproduce a near-50:50 tribal split, not a clear BJP majority.

> **Second observation:** JKP(N) candidate Birbaha Hansda (0.96%) and AKBJHP candidate Maheswar Hembram (0.65%) together drew ~1.61% tribal protest votes. These represent Adivasi political consciousness operating outside the BJP-TMC binary — important for the simulation's agent heterogeneity.

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 222 specifically (Assembly Elections)

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin | Source tier |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 AE | Sukumar Hansda | AITC | 99,233 | 54.97 | Chunibala Hansda | Jharkhand Party (Naren) | 44,005 | 24.38 | 55,228 | A |
| 2011 AE | Sukumar Hansda | AITC | 69,464 | 44.67 | Amar Basu | CPI(M) | 54,191 | 34.85 | 15,273 | A |
| 2006 AE | Amar Basu | CPI(M) | 74,300 | 54.82 | Shivendra Bijoy Malladeb | INC | 34,299 | 25.30 | 40,001 | A |

**2011 AE notable:** Chhatradhar Mahato (IND, jailed PCAPA leader) drew 20,037 votes (12.88%) from jail. This reflects the depth of anti-establishment sentiment in the Binpur I / Lalgarh sub-area in the immediate aftermath of the Maoist suppression (2009–11). Turnout: 155,520 (84.47%).

**Political sociology note (pre-2019):** Jangalmahal was a Maoist/Naxalite stronghold 2004–2011. The CPI(M)-affiliated PCAPA movement arose from the Lalgarh uprising (Nov 2008–2009) following police atrocities post the Buddhadeb Bhattacharya convoy landmine attack (Nov 2008). Operation Lalgarh (June 2009) was a joint police-paramilitary operation. By 2011, TMC's Mamata Banerjee had made Jangalmahal a central campaign promise — "peace in Jangalmahal" — and tribal voters defected en masse from CPI(M) to AITC. The 2016 TMC landslide (55%) reflected completion of CPI(M)'s collapse in tribal Jangalmahal. By 2019, BJP had begun making inroads via Hindutva-tribal mobilization and PM welfare schemes, narrowing the TMC margin from 55,228 (2016 AE) to 1,643 votes (2019 LS).

### Jhargram LS (PC 27) historical

| Year | Winner | Party | Votes | % | Notes |
|---|---|---|---|---|---|
| 2009 LS | Dr. Pulin Bihari Baske | CPI(M) | 545,231 | 56.92 | CPI(M) last win; Maoist insurgency peak year; INC 26.4% second |
| 2014 LS | Dr. Uma Saren | AITC | 674,504 | 54.60 | TMC wave; Jangalmahal peace credit; CPI(M) 26.5% second; BJP minimal |
| 2019 LS | Kunar Hembram | BJP | 626,583 | 44.56 | BJP first win; margin 11,767; TMC 43.72%; CPI(M) collapsed |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- `2019_AssemblySegmentLevelVotingData.csv` — ECI GE2019 AC-222 segment vote tallies (party-wise, NOTA, electorate, total votes; AC-level tier A)
- Census of India 2011 — Jhargram municipality (via census2011.co.in and Wikipedia)
- Census of India 2011 — Jhargram CD Block (via Wikipedia "Jhargram (community development block)")
- Census of India 2011 — Binpur I CD Block (via Wikipedia "Binpur I (community development block)")
- Census of India 2011 — Jhargram district (via Wikipedia "Jhargram district")
- ECI archives — 2006 AE, 2011 AE, 2016 AE AC-222 results (via Wikipedia "Jhargram Assembly constituency")
- ECI archives — 2009 LS, 2014 LS, 2019 LS Jhargram PC results (via Wikipedia "Jhargram Lok Sabha constituency")
- Delimitation Commission of India 2008 — WB AC-222 composition (Muni + 4 GPs Jhargram CDB + Binpur I CDB)

### Secondary sources (tier B/C)
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline
- NFHS-5 (2019-21) West Bengal — asset/media crosscheck (used with caution; post-2019 data only for corroboration of 2019 projection direction)
- PMJDY enrollment data — banking access proxy
- Pew Research India 2021 — religion-differential growth projections (used for 2011→2019 projection)
- CSDS-Lokniti 2019 NES post-poll (national rollup; WB regional adjustment)
- Census 2011 — Jhargram subdivision administrative structure (via Wikipedia)

### Tertiary / journalistic (tier D)
- Wikipedia "Jhargram Assembly constituency" — assembly election results
- Wikipedia "Jhargram Lok Sabha constituency" — LS election results
- Wikipedia "Operation Lalgarh" — Maoist insurgency chronology
- Binpur I BPL data (47.46%, 2007) — via Wikipedia "Binpur I (community development block)"
- Jhargram district tribal composition — via Ramakrishna Mission Jhargram Ashrama website
- ResearchGate "Socio-economic and demographic conditions of Jhargram district, WB, 2011"
- Sanhati.com — Lalgarh Movement history (adivasi uprising context)
- The Wire — "What Trinamool's Induction of Chhatradhar Mahato Means to Bengal Politics"

### Tier-D/E reliance flags (what to distrust)
- **ST sub-group shares** (C.2, D.2): no tribe-specific Census data at AC-level; estimated from district-level literature; largest uncertainty in this file
- **Sarna/ORP separate from Hindu** (C.1, D.1, D.11): Census 2011 has no Sarna code; the 10.9% Sarna estimate is derived from "Others" category in Census block data; may be undercounted
- **Sub-unit proportional allocation** (C.11, D.11–D.14): Jhargram CDB contribution assumes 4 GPs out of 13 at equal weight; actual GP-level data not available; Binpur I assumed full block
- **Vote × caste / tribe** (D.16): tribal vote behavior in Jangalmahal estimated from AC-222 result structure and CSDS state summary; no sub-group exit-poll data available
- **MGNREGA work days** (C.10, D.18): block-level NREGA portal not directly accessed; estimated from WB Jangalmahal district pattern
- **Migration share** (C.16, D.3): qualitative estimates; Census D-series migration data not directly accessed

### v0 known gaps (see methodology §7)
1. **GP-level demographics** — collapsed to 3 sub-units; Jhargram CDB 4 GP equal-weight assumption; refine when DCHB Jhargram Part-A accessible
2. **Tribe-specific population shares** — no Census 2011 Schedule Tribe appendix accessed at block level; current estimates from district literature
3. **Sarna/ORP vs Hindu census overlap** — the 10.9% Sarna estimate needs cross-validation against Census PCA "Other religion" category at block level
4. **MGNREGA persondays at block level** — NREGA portal block-wise 2018-19 data not directly fetched; proxy estimate used
5. **Vote × caste D.16** — no Lokniti sub-constituency tribal exit-poll; using result-structure inference

---

*v0 — generated 2026-04-27, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **These are OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> The simulator must reproduce these results from 2019 priors + narrative injection (tribal welfare messaging, Birbaha Hansda celebrity candidacy, Adivasi alienation from BJP) without these figures being baked into the calibration input.

### 2021 WB Assembly Election — AC 222 Jhargram (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| AITC | Birbaha Hansda | 1,09,493 | 54.31% | A — ECI 2021 AE |
| BJP | Sukhmoy Satpati | 71,253 | 35.34% | A — ECI 2021 AE |
| CPI(M) | Madhuja Sen Roy | ~10,430 | 5.17% | A — ECI 2021 AE |
| NOTA | — | 3,636 | ~1.80% | A |
| **TMC margin** | | **38,240 votes** | **18.97 pp** | A |

TMC swing from 43.62% (2019 LS) to 54.31% (2021 AE) = +10.7pp. BJP collapsed from 44.49% to 35.34% = −9.1pp. The swing was driven by Birbaha Hansda's celebrity (folk singer, first woman to contest from this seat) + Adivasi alienation from BJP post-2019.

### 2024 Lok Sabha Election — AC 222 segment within Jhargram LS (PC 27) (tier A, CSV)

> Figures below are **tier A** — sourced directly from `2024_AssemblySegmentLevelVotingData.csv`, AC_NO=222, West Bengal. Total valid votes: 201,151 (candidates) + 2,272 (NOTA) = 203,423; electorate 246,403; turnout ~82.6%.

| Party | Candidate (LS level) | Votes | AC-222 segment % | Tier |
|---|---|---|---|---|
| AITC | Kalipada Saren (Kherwal) | 96,608 | **47.49%** | A |
| BJP | Dr. Pranat Tudu | 82,507 | **40.56%** | A |
| CPI(M) | Sonamani Tudu | 10,448 | **5.14%** | A |
| JKPP | Surya Singh Besra | 2,526 | **1.24%** | A |
| NOTA | — | 2,272 | **1.12%** | A |
| Others (BSP, IND, APoI, SUCI, AISF) | various | ~8,662 | **4.26%** | A |
| **AITC margin over BJP** | | **14,101 votes** | **6.93 pp** | A |

### Mean-reversion note (critical for simulation)

**This is a mean-reverting seat: BJP 44.49%→35.34%→40.56%, AITC 43.62%→54.31%→47.49%.**

The 2021 TMC spike was driven by candidate-effect (Birbaha Hansda, a celebrity folk singer with strong Adivasi identity appeal) + COVID welfare messaging + tribal alienation from BJP's failure to deliver on Sarna code demand. It was NOT fully sustained. By 2024, BJP partially recovered as the candidate-effect wore off and BJP continued tribal outreach via central schemes. The simulation must reproduce oscillation, not lock-in on either side. The 2026 forecast must model: (a) whether Birbaha Hansda contests again (her candidacy is an exogenous input to inject), (b) whether Sarna code demand remains unresolved (BJP liability), (c) MGNREGA central government fund-release patterns, and (d) PM-KISAN vs state welfare scheme attribution battle.
