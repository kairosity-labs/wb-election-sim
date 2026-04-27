# AC 11 — Kalchini (ST) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural state of AC 11 Kalchini as of 2019 only — it does not reference any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 11 | A | ECI / Delimitation Commission 2008 |
| AC name | Kalchini | A | ECI |
| Reservation | ST (Scheduled Tribe) | A | Delimitation 2008 |
| District | Alipurduar | A | Alipurduar district created from Jalpaiguri in 2014; Delimitation 2008 lists Jalpaiguri as parent |
| Sub-division | Alipurduar | A | WB administrative; Kalchini CD Block is in Alipurduar sub-division |
| LS constituency | PC 2 — Alipurduars (ST reserved) | A | Delimitation 2008 |
| LS segments included with AC 11 | AC 7 Madarihat · 8 Dhupguri · 9 Nagrakata · 10 Alipurduar · 11 Kalchini · 12 Falakata · 13 Kumargram | A | Delimitation 2008 |
| AC composition | All 11 GPs of Kalchini CD Block (Chuapara, Dalsingpara, Garopara, Jaigaon I, Jaigaon II, Kalchini, Latabari, Malangi, Mendabari, Rajabhatkhawa, Satali) + Majherdabri GP from Alipurduar II CD Block | A | Wikipedia "Kalchini (Vidhan Sabha constituency)"; Delimitation 2008 |
| Geographic note | Eastern Dooars; tea-garden dominated landscape; borders Bhutan (Jaigaon-Phuentsholing border crossing); forested terrain with Buxa Tiger Reserve | A | Wikipedia "Kalchini, Alipurduar" |
| Archetype | A3 — North Bengal tea-garden ST; RSS-affiliated Bharatiya Tea Workers Union (BTWU) stronghold | D | The Print (2021); journalistic characterization |
| Two sub-units used in v0 (bagan-conditioning) | **U1: Kalchini CDB core** (11 GPs, ~298,548 pop 2011) · **U2: Majherdabri GP from Alipurduar II** (~19,843 pop 2011) | E | v0 simplification — see methodology §3 |

---

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (CDB Kalchini) | 298,548 (rural 211,808 + urban 86,650) | A | Census 2011 — Kalchini CD Block (Wikipedia summary of Census primary abstract) |
| 2011 base population (Majherdabri GP, Alipurduar II) | ~19,843 (1/11 of Alipurduar II CDB 218,272) | E | v0 equal-weight GP assumption; Alipurduar II CDB Census 2011 |
| 2011 base population (AC 11 total) | ~318,391 | E | Sum above; v0 GP-equal-weight assumption |
| 2019 projected population | ~345,000 | E | 8-yr compound growth; religion-differential rates (methodology §4) |
| Sex ratio (2011, F per 1000 M) | 925 | A | Kalchini CDB 2011: 143,269 F / 154,829 M = 925 (below WB average; labour-in-migration of male workers) |
| 2019 estimated sex ratio | ~930 | E | Marginal improvement trend; tea-garden male bias stable |
| 2019 estimated electorate (18+) | ~235,753 | A | ECI 2019 LS: 235,753 electors for AC 11 Kalchini (tier A, from `2019_AssemblySegmentLevelVotingData.csv`) |
| 2019 polling stations (estimated) | ~310 | E | 2021 AE had ~324; back-projection |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 66.00 | E | Kalchini CDB 2011: 67.08% (A); projected slight decline ~1pp over 8yr as Christian/Tribal-ORP shares hold or grow; v0 uses 66% |
| Christian | 15.00 | E | Kalchini CDB 2011: 14.33% (A); tea-belt missions active among Adivasi; +0.5pp projected |
| Buddhist | 7.00 | E | Kalchini CDB 2011: 7.28% (A); Nepali-Gorkha Buddhist community; stable |
| Muslim | 8.00 | E | Kalchini CDB 2011: 8.57% (A); projected +0.2pp/yr → ~9% by 2019; anchored to 8% with Majherdabri GP (Alipurduar II more Hindu-dominant) |
| Sarna / Tribal ORP | 3.00 | E | Kalchini CDB 2011: ~2.00%; small upward drift as some Adivasi reclaim Sarna identity; projected 3% by 2019 |
| Sikh | 0.50 | E | Kalchini CDB 2011: 0.50%; stable |
| Other / Not stated | 0.50 | E | Residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **ST total** | 40.00 | A | Kalchini CDB 2011: 120,282 ST = 40.30%; v0 rounds to 40.00% for AC-weighted estimate (Majherdabri is Alipurduar II which has lower ST ~18%) |
| └ Oraon (Kurukh-speaking) | 16.00 | D | Dominant Adivasi group in Kalchini tea gardens; Kurukh 2.99% of Kalchini CDB + the Oraon designation; journalistic sources; Oraon ~40% of ST pool |
| └ Munda | 8.00 | D | ~20% of ST pool; Kalchini Tea Garden majority Munda (journalistic) |
| └ Santhal | 6.00 | D | ~15% of ST pool; Jharkhand-origin labor in Dooars |
| └ Kharia / Gond / Kurmi (tea-belt Adivasi) | 6.00 | D | Remaining ST pool; mixed Chhattisgarh/Jharkhand origin |
| └ Nepali/Gorkha ST (Tamang, Rai etc.) | 4.00 | D | Tea-belt Nepali-origin ST; also part of Buddhist share |
| **SC total** | 10.00 | A | Kalchini CDB 2011: 30,157 SC = 10.10%; AC-11 weighted (Majherdabri is SC-heavy ~41% — see Alipurduar II) → AC-weighted estimate remains ~10% since Majherdabri is a small GP |
| **Nepali/Gorkha (non-ST, Hindu/Buddhist)** | 12.00 | D | Kalchini CDB: Nepali 26.3% mother-tongue speakers; significant non-tribal Nepali/Gorkha community in Dooars; not all Nepali-speakers are ST; overlap with Buddhist share |
| **Bengali (Hindu, upper/middle caste)** | 10.00 | D | Garden managers, small traders, Jaigaon town Bengali residents; minority but economically salient |
| **Bengali OBC / Rajbanshi** | 6.00 | D | Rajbanshi: 3.17% Alipurduar district average; other OBC; residual non-Adivasi non-bhadralok |
| **Muslim (all sub-castes pooled)** | 8.00 | E | See C.1; mainly Bengali-Muslim and some tribal-origin Muslim in peripheral GPs |
| **Christian (Adivasi-origin)** | 7.00 | E | Substantial share of ST converted to Christianity through 19th-20th century missions; sub-caste in C.2 D.2 joint |
| **Other / Sarna / Buddhist** | 7.00 | E | See C.1; Buddhist Nepali non-tribal; Sarna residual |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 0–4 | 8.5 | E | Kalchini CDB 2011: 34,627 age 0-6 = 11.6%; projected decline as fertility falls; 0-4 ≈ 8.5% by 2019 |
| 5–9 | 9.0 | E | |
| 10–14 | 9.0 | E | |
| 15–17 (pre-voter) | 5.5 | E | |
| 18–22 (first-time voters at 2019) | 8.5 | E | |
| 23–27 | 9.0 | E | |
| 28–32 | 9.0 | E | |
| 33–37 | 8.5 | E | |
| 38–42 | 7.5 | E | |
| 43–47 | 7.0 | E | |
| 48–52 | 6.0 | E | |
| 53–57 | 4.5 | E | |
| 58–62 | 3.5 | E | |
| 63–67 | 2.0 | E | |
| 68+ | 2.5 | E | Tea-garden pattern: premature mortality from occupational exposure; smaller elderly cohort |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.97 | E | Kalchini CDB 2011: 154,829 M / 298,548 = 51.87%; marginal shift toward balance by 2019 → ~51.97% (male labour in-migration stabilizes) |
| Female | 48.02 | E | |
| Third gender | 0.01 | E | Negligible; consistent with WB pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Sadri / Nagpuri (tea-belt lingua franca) | 30.00 | A | Kalchini CDB 2011: 30.1% Sadri — DOMINANT in tea gardens; lingua franca among Oraon, Munda, Kharia, Gond workers regardless of tribal origin; load-bearing for media-consumption modelling |
| Nepali | 26.00 | A | Kalchini CDB 2011: 26.3%; Gorkha/Nepali community in Dooars; second-largest language group |
| Bengali | 14.00 | A | Kalchini CDB 2011: 14.2%; Bengali-speakers concentrated in Jaigaon town and managerial/trader class |
| Hindi | 8.00 | A | Kalchini CDB 2011: 8.17%; Hindi-belt migrants + Hindi as second language for some Sadri-speakers |
| Kurukh (Oraon language) | 3.00 | A | Kalchini CDB 2011: 2.99%; Oraon home language alongside Sadri |
| Bhojpuri | 4.00 | A | Kalchini CDB 2011: 3.93%; Bihari-origin tea labor |
| Boro | 3.00 | A | Kalchini CDB 2011: 2.85%; Bodo community in eastern Dooars fringe |
| Rabha | 2.00 | A | Kalchini CDB 2011: 1.73%; Rabha tribal community |
| Santali | 1.00 | E | Santali-speakers; subset of Santhal ST |
| Other (Mundari, Ho, Kharia, etc.) | 9.00 | E | Residual tribal languages; many shift to Sadri for inter-community communication |
| **Sum** | **100.00** | — | self-check |

(Bilingualism note: Sadri functions as a creole across tea-belt communities. ~70% of Adivasi workers are Sadri-bilingual regardless of home tribal language. Bengali bilingualism is ~25% of total population. Tier E.)

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 26.00 | E | Kalchini CDB 2011 literacy 68.96% → ~31% illiterate in 2011; projected improvement +0.7pp/yr → ~26% illiterate by 2019; female literacy 59.77% anchors high gender gap |
| Primary (Class 1–5) | 24.00 | E | Census 2011 age-education distribution; tea-garden children have high drop-out after primary |
| Middle (Class 6–8) | 20.00 | E | |
| Secondary (Class 9–10) | 14.00 | E | |
| Higher Secondary (Class 11–12) | 9.00 | E | |
| Graduate | 5.50 | E | Low; managerial/trader class; tea-garden worker families rarely reach graduate level |
| Postgraduate | 1.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main worker — tea-garden wage labor (organised sector) | 34.00 | A | Kalchini CDB 2011: total workers 120,238 = 40.29% of pop; "other workers" (overwhelmingly tea) = 84.86% of workers → ~34% of total pop are permanent/temporary tea wage workers; this is the dominant workforce category unlike any other WB AC |
| Main worker — non-tea (cultivator, ag-labor, trade, govt) | 6.00 | A | Kalchini CDB 2011: cultivators 6.20% + ag-laborers 7.06% + household industry 1.88% of workers = ~15% of workers = ~6% of total pop; small non-bagan sector |
| Marginal worker (seasonal / casual tea picking) | 8.00 | E | Tea-garden seasonal picking employs women and youth; marginal worker share above WB average for tea-belt |
| Non-worker (housewife / elderly / retired) | 38.00 | E | Kalchini CDB 2011: non-workers 178,220 = 59.71% of pop; tea-garden women often listed as non-worker even when active in picking; v0 projects 38% adult non-worker |
| Student (18–22 only, in education) | 6.00 | E | Low post-secondary enrollment in tea gardens |
| Unemployed (closed-garden / displaced) | 8.00 | D | Closed tea gardens (19 closed in broader Dooars-Jalpaiguri region); closed-garden workers neither employed nor formally unemployed; modeled as 8% (journalistic: ~60,000 workers displaced) |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Tea-garden plucking / processing (organized sector) | 72.00 | A | Computed: "other workers" = 84.86% of Kalchini CDB 2011 total workers; majority are bagan wage-earners; v0 uses 72% to allow for non-tea "other workers" |
| Cultivator (own-field, outside bagan) | 4.00 | A | Kalchini CDB 2011: 7,459 cultivators = 6.20% of workers; v0 adjusts to 4% to account for small landholding in tea-belt |
| Agricultural labourer (non-tea, seasonal) | 5.00 | A | Kalchini CDB 2011: 8,487 ag-laborers = 7.06% of workers |
| Household industry | 2.00 | A | Kalchini CDB 2011: 2,256 = 1.88% of workers |
| Trade / retail (Jaigaon border town) | 7.00 | D | Jaigaon is a busy India-Bhutan border trading town; retail/trade for border economy |
| Transport / border logistics (Jaigaon-Phuentsholing) | 3.00 | D | Cross-border trade logistics; small but economically distinct |
| Government services / teachers | 3.00 | E | BDO / school / health center workers |
| Services (private, non-bagan) | 3.00 | E | Small non-bagan private sector; healthcare workers, mechanics |
| Construction (out-migrant seasonal) | 1.00 | E | Low compared to other WB ACs; closed-garden displaced workers |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employee (regular wage / salary — bagan + govt) | 70.00 | E | Tea-garden is ORGANIZED SECTOR with nominal employment contracts; ~72% of workers are bagan wage-earners (=organized-sector employees); includes govt employees |
| Employer | 1.00 | E | Very few; bagan management and large traders in Jaigaon |
| Single worker (own-account — cultivator / trader) | 18.00 | E | Own-account cultivators + Jaigaon traders + household industry |
| Family worker (unpaid, within HH) | 11.00 | E | Women and children helping on small plots or in household industry |
| **Sum** | **100.00** | — | self-check |

(Note: Kalchini's class-of-worker profile is the INVERSE of typical WB ACs. Regular-wage employees dominate, not own-account workers. This is the signature tea-garden occupational structure.)

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL household | 45.00 | D | Tea-garden wages ₹176/day (pre-2021 = 2015 revision baseline) × ~275 work-days = ~₹48,400/yr ≈ ₹4,000/month; below WB BPL threshold; journalistic: "majority of household income does not exceed ₹6,000/month"; v0 uses 45% BPL (much higher than WB state average ~20%) |
| Above-poverty-line, low-income | 30.00 | E | Bagan workers slightly above BPL threshold; regular wage but low |
| Lower-middle | 15.00 | E | Jaigaon border traders; head-clerks / sirdars in garden management |
| Middle | 8.00 | E | Garden supervisory staff; govt employees; prosperous Jaigaon traders |
| Upper-middle / well-off | 2.00 | E | Garden managers; Jaigaon commercial class |
| **Sum** | **100.00** | — | self-check |

### C.11 Bagan / GP location (2019)

Note: in Kalchini, the spatial sub-unit is the TEA GARDEN (bagan) rather than the GP, which is the standard unit for other WB ACs. Bagans are spatially discrete settlements with their own housing lines, management structures, and social fabric. For v0, we aggregate to two sub-units:

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **U1: Kalchini CDB core (all 11 GPs)** | 93.8 | E | 2011: 298,548 / 318,391 = 93.8% |
| **U2: Majherdabri GP (Alipurduar II)** | 6.2 | E | ~19,843 / 318,391 = 6.2%; more Bengali-dominant, higher SC, less tea-garden |
| **Sum** | **100.00** | — | self-check |

Sub-unit decomposition within U1 (Kalchini CDB core), for spatial-heterogeneity modelling:

| Category | % of U1 | Tier | Source / Note |
|---|---|---|---|
| Urban (4 census towns: Jaigaon + Uttar Satali + Uttar Latabari + Mechiabasti) | 29.0 | A | 2011: 86,650 urban / 298,548 = 29.0% (Jaigaon 42,254 dominant) |
| Rural (tea-garden villages + forest settlements) | 71.0 | A | 2011: 211,808 rural / 298,548 = 71.0% |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg HH size | 4.8 persons | E | Tea-garden "lines" housing: large family units in crowded bagan quarters; WB 2011 average 4.3; tea-belt higher |
| Nuclear HH | 60.0 | E | Bagan lines break extended family structures over generations; still more nuclear than joint |
| Joint HH | 30.0 | E | More joint HH than WB average; inter-generational bagan employment |
| Extended / multi-generation | 10.0 | E | |
| **Sum** | **100.00** | — | self-check |

(HH head: ~82% male-headed, 18% female-headed; higher female-headedness than WB average due to male out-migration from closed gardens; tier E.)

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never married | 24.0 | E | Younger first-voter cohort; tribal early marriage patterns |
| Currently married | 66.0 | E | Tribal communities: marriage earlier and near-universal |
| Widowed | 9.0 | E | Higher than WB average; premature male mortality from occupational diseases (silicosis, fluorosis) in tea areas; female-skewed widowhood |
| Separated / divorced | 1.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 50.0 | D | Tea-garden housing lines: significantly lower than WB rural average (~60% NFHS-4); sanitation survey (only 15.81% latrine access) signals general deprivation; The Bastion (2021) notes infrastructure deficits; v0 uses 50% |
| Radio | 15.0 | D | Higher than WB average; radio remains important in tea-garden areas with low TV penetration; used for Sadri/Hindi broadcasts |
| Mobile phone (any) | 70.0 | D | Growing post-Jio 2016 rollout; but tea-garden workers with low wages have lower penetration than WB rural average (~78% NFHS-4); v0 uses 70% |
| Smartphone with internet | 28.0 | D | Significantly below WB rural average (~50%); low disposable income + Sadri-language internet barrier; v0 uses 28% — **load-bearing for narrative-injection weighting** |
| Computer | 4.0 | E | Very low; bagan quarters have no computer culture |
| Two-wheeler | 12.0 | E | Below WB rural average; limited disposable income for capital assets |
| Four-wheeler | 2.0 | E | Only managers and Jaigaon traders |
| Banking access (any) | 75.0 | B | PMJDY 2014 rollout; lower than WB state average due to identification challenges for Adivasi tea workers (identity documents); v0 uses 75% |
| **Note** | (these are independent ownership %s, not categorical — do not sum) | — | — |

### C.15 Household amenities (2019)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved drinking water source | 60.0 | D | Tea-plantation sanitation survey (The Bastion): only 30.7% of plantation HH receive drinking water via tube wells in some studies; v0 uses 60% allowing for piped supply within bagan complex |
| Improved sanitation (latrine) | 25.0 | D | Tea-plantation survey: only 15.81% have latrines; majority defecate in open; Swachh Bharat had limited reach in tea-garden private land; v0 uses 25% as conservative improvement |
| LPG / clean cooking fuel | 25.0 | D | Below WB rural average; Ujjwala 2016-19 had limited penetration in tea-belt due to address/identity issues; bagan wood collection still dominant |
| Wood / biomass fuel | 70.0 | E | Dominant cooking fuel; bagan land provides access to firewood |
| Other fuel (kerosene, dung) | 5.0 | E | |
| Electricity | 80.0 | D | Lower than WB state average (Saubhagya 2017-19); bagan housing lines: older electrification but quality poor; journalistic sources note infrastructure gaps in closed gardens; v0 uses 80% |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native (born in Alipurduar / Jalpaiguri or same bagan) | 60.0 | D | 4th–5th generation descendants of original indentured labor; born in the bagan |
| WB other district (in-migrant) | 5.0 | D | Limited internal WB in-migration to tea belt |
| **Jharkhand / Chhattisgarh / Odisha origin (Adivasi, multi-generation)** | 25.0 | D | **Load-bearing**: Oraon, Munda, Santhal, Kharia, Gond forebears brought from Chhotanagpur plateau as indentured labor in 19th–early 20th century; 3rd–5th generation now "native" by birthplace but maintain Jharkhand-origin identity and tribal culture |
| Bihar / UP (Hindi-belt, Bhojpuri-speaking) | 5.0 | D | Bhojpuri 4% in CDB; some direct in-migration continued into 20th century |
| Nepal-origin (Gorkha/Nepali, multi-generation) | 4.0 | D | Nepali 26% speaker share implies substantial Nepal-heritage population in Dooars |
| Other Indian state | 0.5 | E | Marginal |
| Outside India | 0.5 | E | Negligible; some recent Nepal in-migration |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Sadri | Nepali | Bengali | Hindi/Bhojpuri | Kurukh | Boro/Rabha | Other tribal | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 25.0 | 28.0 | 20.0 | 11.0 | 3.5 | 4.0 | 8.5 | E | Hindu Nepali Gorkha + Bengali + Oraon Hindu; Sadri lower share within Hindu as Nepali/Bengali are non-Sadri |
| Christian | 48.0 | 12.0 | 8.0 | 6.0 | 8.0 | 4.0 | 14.0 | E | Adivasi Christian communities speak Sadri + Kurukh; mission schools promoted Bengali/Hindi literacy |
| Muslim | 2.0 | 2.0 | 75.0 | 14.0 | 0.0 | 3.0 | 4.0 | E | Muslims concentrated in Bengali/Hindi-speaking peripheral GPs; very few Sadri-Muslim |
| Buddhist | 3.0 | 90.0 | 4.0 | 2.0 | 0.0 | 1.0 | 0.0 | E | Buddhists almost entirely Nepali-speaking Gorkha community in Dooars |
| Sarna/ORP | 60.0 | 0.0 | 5.0 | 5.0 | 15.0 | 5.0 | 10.0 | E | Sarna adherents are Adivasi; Sadri-dominant + home tribal languages |
| **Marginal recovery — Sadri** | | | | | | | | | Hindu(66)×0.25 + Christian(15)×0.48 + Muslim(8)×0.02 + Buddhist(7)×0.03 + Sarna(3)×0.60 + Other(1)×0.20 = 16.5+7.2+0.16+0.21+1.8+0.2 = **26.07** vs C.5 **30.0** ⚠ off by 4pp — flag for v1 reconciliation (Sadri internal to Hindu sub-divided is conservative) |

### D.2 Religion × Caste (Hindu-internal sub-structure + inter-religion)

P(caste ‖ Hindu) — % within Hindu population only.

| Caste sub-group | % of Hindu | Tier | Source |
|---|---|---|---|
| **ST Adivasi (Hindu / Sarna-identifying)** | 28.0 | E | ~40% of total pop is ST; but ~35–40% of ST is Christian/Buddhist/Sarna → ~60-65% of ST in Hindu column → ST-Hindu ≈ 24–26% of total → % of Hindu (66%) ≈ ~28% |
| SC (various) | 15.0 | E | 10% of total / 66% Hindu = ~15% of Hindu |
| Nepali / Gorkha (non-ST, Hindu) | 18.0 | E | Large Nepali Hindu community; ~12% of total / 66% = ~18% of Hindu |
| Bengali bhadralok (UC Brahmin/Kayastha) | 8.0 | E | Small manager/trader class; ~5% of total / 66% = 8% of Hindu |
| Bengali OBC / Rajbanshi | 9.0 | E | ~6% of total / 66% = 9% of Hindu |
| Other Hindu middle (Bihari/Hindi-belt Hindu) | 22.0 | E | Bhojpuri/Hindi-belt non-SC non-ST; merged with Rajbanshi OBC fringe |
| **Sum** | **100.00** | — | self-check |

P(sub-community ‖ Christian) — % within Christian population:

| Sub-group | % of Christian | Tier | Source |
|---|---|---|---|
| Adivasi-origin (Oraon, Munda, Santhal convert) | 82.0 | D | Catholic and Protestant missions from 19th century overwhelmingly converted Adivasi workers |
| Bengali Christian | 10.0 | D | Old Catholic families in Jalpaiguri town tradition |
| Nepali Christian | 8.0 | D | Some Gorkha converts to Christianity |
| **Sum** | **100.0** | — | self-check |

### D.3 Religion × Migration / birthplace

P(birthplace ‖ religion):

| Religion | Native (WB) | WB-other-dist | Jharkhand/CG-origin | Bihar/UP | Nepal-origin | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 60 | 5 | 20 | 7 | 8 | D | Hindu Nepali and Adivasi-Hindu both present |
| Christian | 55 | 3 | 38 | 3 | 1 | D | Most Adivasi Christian families are Jharkhand-origin but 4th–5th generation |
| Muslim | 80 | 8 | 0 | 10 | 0 | D | Bengali Muslim and Bihari Muslim; not Adivasi |
| Buddhist | 50 | 2 | 0 | 0 | 48 | D | Nepali-origin Buddhist community |
| Sarna/ORP | 45 | 3 | 50 | 2 | 0 | D | Sarna-identifying Adivasi most closely tied to Jharkhand cultural origin |

### D.4 Religion × Asset / media (TV, smartphone, banking)

P(owns asset ‖ religion) — % within each religion.

| Religion | TV | Smartphone-internet | Banking |
|---|---|---|---|
| Hindu | 55 | 32 | 80 |
| Christian | 42 | 22 | 65 |
| Muslim | 58 | 30 | 72 |
| Buddhist | 62 | 35 | 80 |
| Sarna/ORP | 30 | 15 | 55 |
| Tier | D | D | C |
| Source | Tea-garden living conditions surveys (lower Christian/Sarna = poorest Adivasi segments) | Same | PMJDY + identification challenges |

### D.5 Caste × Education

P(education level ‖ caste group) — highest level achieved, age 18+.

| Caste | Illiterate | Primary | Middle | Sec | HS | Grad | PG | Tier |
|---|---|---|---|---|---|---|---|---|
| Bengali bhadralok (UC) | 5 | 10 | 12 | 20 | 20 | 23 | 10 | E |
| Bengali OBC / Rajbanshi | 15 | 22 | 22 | 20 | 12 | 7 | 2 | E |
| Nepali / Gorkha | 18 | 22 | 22 | 18 | 12 | 6 | 2 | E |
| **ST Adivasi (Hindu)** | **35** | **28** | **20** | **10** | **5** | **2** | **0** | **E** |
| **ST Adivasi (Christian)** | **20** | **30** | **25** | **15** | **7** | **3** | **0** | **E** |
| SC | 28 | 27 | 22 | 14 | 6 | 2 | 1 | E |
| Muslim | 22 | 26 | 24 | 18 | 7 | 3 | 0 | E |

(Note: Christian Adivasi show meaningfully better literacy than Hindu-or-Sarna Adivasi — mission school effect. This is load-bearing for vote × education modelling.)

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender):

| Cohort | Male grad+ | Female grad+ | Tier | Source |
|---|---|---|---|---|
| 18–22 | 8 | 6 | E | Very low grad-attainment in tea belt; some first-generation college |
| 23–27 | 7 | 4 | E | |
| 28–32 | 5 | 2 | E | |
| 33–42 | 4 | 1 | E | Old cohort nearly all bagan-labor |
| 43–57 | 3 | 1 | E | |
| 58+ | 2 | 0.5 | E | |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender):

| Age | Male married | Female married | Tier |
|---|---|---|---|
| 18–22 | 10 | 45 | E |
| 23–27 | 55 | 85 | E |
| 28–32 | 85 | 93 | E |
| 33–47 | 92 | 90 | E |
| 48–62 | 88 | 75 | E |
| 63+ | 72 | 30 | E (high widowhood: occupational male premature mortality) |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation):

| Occupation | Smartphone-internet | TV | Tier | Source |
|---|---|---|---|---|
| Tea-garden permanent worker | 22 | 45 | D | Daily wage ₹176 leaves very limited surplus; bagan housing has TV but smartphone less common |
| Tea-garden seasonal / marginal | 15 | 35 | D | Lowest income; least media access |
| Cultivator (non-bagan) | 25 | 50 | E | Slightly more asset-holding than bagan |
| Trade / retail (Jaigaon) | 65 | 85 | D | Border-town traders have high smartphone penetration |
| Govt services / teachers | 80 | 90 | E | |
| Transport / logistics | 55 | 75 | E | |
| Closed-garden displaced worker | 10 | 30 | D | Extreme poverty; least media access |

### D.9 Education × Workforce participation

P(unemployed-and-seeking ‖ education):

| Education | Unemployed-seeking | Main-worker rate | Tier |
|---|---|---|---|
| Illiterate | 1 | 42 | E |
| Primary | 3 | 45 | E |
| Middle | 5 | 40 | E |
| Secondary | 10 | 30 | E |
| Higher Secondary | 20 | 20 | E |
| Graduate | 28 | 18 | E |
| Postgraduate | 18 | 30 | E |

(Tea-garden economy: illiterate/primary workers are absorbed as permanent bagan labor; educated youth face structural unemployment as bagan management jobs are capped.)

### D.10 Asset / media × Bilingualism

P(bilingual Sadri+Bengali ‖ media-access tier):

| Media tier | Sadri+Bengali bilingual | Tier | Source |
|---|---|---|---|
| TV-only HH | 20 | E | Bengali TV channels; Sadri-speaking workers pick up Bengali |
| TV + smartphone HH | 35 | E | YouTube cross-language; higher exposure to Bengali content |
| Smartphone-only HH | 25 | E | |
| Radio-only HH | 12 | E | Radio uses Hindi/Sadri more than Bengali |
| No-asset HH | 8 | E | Lowest exposure to Bengali |
| **Population-wide Sadri–Bengali bilingual rate** | ~22 | E | C.5 anchor: Bengali 14% primary + ~22% bilingual population |

### D.11 Bagan / Sub-unit × Religion

P(religion ‖ spatial sub-unit):

| Sub-unit | Hindu | Christian | Muslim | Buddhist | Sarna/ORP | Tier | Source |
|---|---|---|---|---|---|---|---|
| **U1: Kalchini CDB core** (93.8% pop) | 65.5 | 15.5 | 7.5 | 7.5 | 3.5 | E | Directly from CDB 2011 census proportions (A) projected to 2019 |
| **U2: Majherdabri GP (Alipurduar II)** (6.2% pop) | 84.4 | 8.6 | 6.5 | 0.0 | 0.5 | E | Alipurduar II CDB 2011: Hindu 84.40%, Christian 8.64%, Muslim 6.50%; no significant Buddhist |
| **Marginal recovery — Hindu** | | | | | | | 0.938×65.5 + 0.062×84.4 = 61.44 + 5.23 = **66.67** vs C.1 **66.00** ✓ within ±1pp |

### D.12 Bagan / Sub-unit × Caste

P(caste ‖ sub-unit):

| Sub-unit | ST % | SC % | Nepali/Gorkha | Bengali UC/OBC | Muslim | Tier |
|---|---|---|---|---|---|---|
| U1: Kalchini CDB core | 42.0 | 10.0 | 14.0 | 15.0 | 8.0 | E |
| U2: Majherdabri GP | 18.4 | 41.8 | 3.0 | 25.0 | 6.5 | E |
| Source | CDB 2011 ST=40.30% (A) | CDB 2011 SC=10.10% (A) | Nepali language proxy | Bengali mgmt/trade | CDB 2011 religion proxy | |

### D.13 Bagan / Sub-unit × Asset / media

| Sub-unit | TV | Smartphone-internet | Banking | Tier |
|---|---|---|---|---|
| U1: Kalchini CDB core (tea-garden dominated) | 48 | 26 | 73 | D |
| U2: Majherdabri GP (more agrarian, SC-heavy) | 62 | 38 | 82 | E |
| Source | Tea-garden deprivation (The Bastion) | Same | PMJDY differential | |

### D.14 Bagan / Sub-unit × Amenities

| Sub-unit | LPG | Improved sanitation | Improved water | Electricity | Tier |
|---|---|---|---|---|---|
| U1: Kalchini CDB core | 22 | 22 | 58 | 78 | D |
| U2: Majherdabri GP | 35 | 40 | 72 | 88 | E |
| Source | The Bastion (2021): only 15.81% latrine in plantation | Same | 30.7% tube-well water in plantation | Journalistic: bagan electricity partial | |

### D.15 Vote × Religion (2019 LS, AC 11 segment)

P(party ‖ religion) — derived from AC 11 2019 result (BJP 58.53% / AITC 33.63%) combined with CSDS-Lokniti WB patterns adjusted for tea-belt context.

| Religion | BJP | AITC | RSP | INC | Other/NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| **Hindu (Adivasi + Nepali + Bengali)** | 60 | 30 | 3 | 3 | 4 | C/D | BJP's BTWU hold on Adivasi Hindu; Nepali community leaning BJP via BTWU + Gorkha identity; Bengali managerial class BJP |
| Christian (Adivasi) | 48 | 36 | 5 | 6 | 5 | D | Christian Adivasi: BJPs BTWU organizing effective but slightly weaker among Christian converts; RSP residual |
| Muslim | 10 | 65 | 5 | 15 | 5 | D | Muslim minority strongly TMC; weaker in tea-belt where Muslim share is low |
| Buddhist (Nepali-Gorkha) | 55 | 28 | 3 | 4 | 10 | D | Gorkha community leaning BJP/GJM-allied parties; some GJM-endorsed vote in 2011 |
| Sarna/ORP | 55 | 30 | 5 | 3 | 7 | D | Sarna Adivasi: BTWU organizing + BJP identity politics |
| **Marginal recovery — BJP** | | | | | | | Hindu(66)×0.60 + Christian(15)×0.48 + Muslim(8)×0.10 + Buddhist(7)×0.55 + Sarna(3)×0.55 + Other(1)×0.40 = 39.6+7.2+0.8+3.85+1.65+0.4 = **53.5** vs AC 11 tier-A **58.53%** ⚠ off by ~5pp — BTWU organizational bonus not fully captured; flag for v1 calibration of Hindu Adivasi BJP share |

### D.16 Vote × Caste (2019 LS, AC 11)

P(party ‖ caste group):

| Caste | BJP | AITC | RSP | INC | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| **ST Adivasi (Hindu/Sarna)** | **68** | **22** | **4** | **3** | **3** | **D** | **BTWU hold; RSS outreach; John Barla Adivasi identity resonance** |
| ST Adivasi (Christian) | 52 | 32 | 6 | 6 | 4 | D | Slightly weaker BJP; mission-school educated more independent |
| SC | 38 | 45 | 5 | 8 | 4 | D | SC more TMC-leaning than Adivasi ST in tea belt |
| Nepali / Gorkha | 58 | 25 | 3 | 3 | 11 | D | BJP + residual GJM-sympathy; anti-TMC due to Gorkhaland demand history |
| Bengali bhadralok (UC) | 55 | 35 | 3 | 4 | 3 | D | Bhadralok BJP swing 2019 WB |
| Bengali OBC / Rajbanshi | 45 | 40 | 5 | 6 | 4 | D | Mixed; Rajbanshi more AITC-inclined in some areas |
| Muslim | 10 | 65 | 5 | 15 | 5 | D | |

### D.17 Vote × Gender (2019 LS, AC 11)

P(party ‖ gender). No Lakshmir Bhandar in 2019.

| Gender | BJP | AITC | RSP | INC | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 60 | 30 | 3 | 3 | 4 | D | BTWU-heavy male workforce in tea gardens; BJP stronger among male Adivasi workers |
| Female | 56 | 38 | 2 | 2 | 2 | D | Tea-garden female workers also BTWU-organized but slightly more TMC; WB female TMC bias partially holds |

### D.18 Vote × Welfare-scheme exposure (2019)

Available schemes as of 2019: Krishak Bandhu (TMC, Jan 2019), Kanyashree (TMC, 2013), Swasthya Sathi (TMC, 2016), Sabuj Sathi (TMC, 2015), Khadya Sathi (TMC, 2016). **Lakshmir Bhandar does NOT exist in 2019.** Note: tea-garden workers have limited access to some TMC schemes tied to agricultural/municipal identity; bagan workers often excluded from Krishak Bandhu (not cultivators).

| Scheme exposure | BJP | AITC | RSP | INC | Tier | Source |
|---|---|---|---|---|---|---|
| Krishak Bandhu (cultivator HH — minority in tea belt) | 25 | 62 | 5 | 6 | C | TMC welfare credit for farmers; few tea-bagan workers qualify |
| Kanyashree (girl-student HH) | 50 | 42 | 3 | 3 | D | BTWU counters TMC narrative; BJP still dominant even in scheme-exposed HH in tea belt |
| Swasthya Sathi enrollee | 48 | 44 | 3 | 3 | D | Tea-belt workers enrolled; BJP still competitive |
| Khadya Sathi / PDS | 55 | 36 | 4 | 3 | D | PDS coverage high in tea belt; BJP still dominant |
| **No state-scheme exposure** | 65 | 25 | 5 | 3 | D | BJP dominant; BTWU organizational networks substitute for TMC welfare narrative |

---

## E. 2019 baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp.

### Whole Alipurduars LS (PC 2) — 2019 result (tier A, ECI)

| Party | Candidate | Votes | % |
|---|---|---|---|
| BJP | **John Barla** (BTWU President, Adivasi leader) | 750,804 | **54.36** |
| AITC | Dasrath Tirkey | 506,815 | **36.69** |
| RSP | Mili Oraon | 54,010 | **3.91** |
| INC | (candidates) | (residual) | ~2.0 |
| Others / NOTA | various | ~69,547 | ~3.04 |
| **Margin** | BJP over AITC | **243,989** | **17.67 pp** |

Source: `2019_AssemblySegmentLevelVotingData.csv` aggregated; Wikipedia "Alipurduars Lok Sabha constituency"; tier A.

### AC 11 segment — 2019 LS (tier A, CSV)

> Figures below are **tier A** — sourced directly from `/home/ubuntu/wb-election-sim/2019_AssemblySegmentLevelVotingData.csv`, AC_NO=11, Kalchini. Total valid votes: 190,453; electorate 235,753; turnout 80.8%.

| Party | Candidate | Votes | AC-11 segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | John Barla | 111,477 | **58.53%** | A | 2019_AssemblySegmentLevelVotingData.csv |
| AITC | Dasrath Tirkey | 64,045 | **33.63%** | A | Same |
| INC | Mohanlal Basumata | 4,860 | **2.55%** | A | Same |
| RSP | Mili Oraon | 4,194 | **2.20%** | A | Same |
| IND | Prasen Jayant Kindo | 1,603 | **0.84%** | A | Same |
| NOTA | — | 3,034 | **1.59%** | A | Same |
| SUCI(C) | — | 668 | **0.35%** | A | Same |
| IND | Gergory Trikey | 572 | **0.30%** | A | Same |
| **BJP margin over AITC** | | **47,432 votes** | **24.90 pp** | A | Computed |

> AC 11 Kalchini segment BJP vote (58.53%) is **significantly higher** than the whole-LS BJP average (54.36%), confirming Kalchini as a BJP stronghold within the Alipurduars LS. The BJP-AITC margin at AC level (24.90 pp) is tighter than the LS overall (17.67 pp is LS-wide). Use these CSV-derived AC-level figures as authoritative calibration target.

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 11 Kalchini specifically (Assembly Elections)

| Year | Winner | Party | Votes | % | Runner-up | Party | % | Margin | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2016 AE | Wilson Champramary | AITC | 62,061 | 34.99 | Bishal Lama | BJP | 60,550 | 34.14 | 1,511 — razor-thin AITC win; GJM vote split enabled AITC |
| 2011 AE | Wilson Champramary | GJM-backed Independent | 46,455 | 30.05 | Binay Bhusan Kerketta | RSP | 39,210 | 25.37 | Multi-party split; GJM-backed IND won; AITC, BJP, Congress also competed |
| 2009 by-election | Wilson Champramary | Independent (GJM-backed) | — | — | Sandip Ekka | Adivasi Vikas Parishad | — | — | Held after Manohar Tirkey elected to LS (2009 LS) |
| 2006 AE | Manohar Tirkey | RSP | — | — | Paban Kumar Lakra | INC | — | — | RSP hold; LF Front dominance |
| 2001 AE | Paban Kumar Lakra | INC | — | — | Manohar Tirkey | RSP | — | — | INC beat RSP; Left Front still dominant |
| 1996 AE | Manohar Tirkey | RSP | — | — | — | INC | — | — | RSP stronghold period |
| 1991 AE | Manohar Tirkey | RSP | — | — | — | INC | — | — | |
| 1987 AE | (INC) | INC | — | — | Manohar Tirkey | RSP | — | — | INC interlude |
| 1982 AE | Manohar Tirkey | RSP | — | — | — | — | — | — | RSP control |

Source: Wikipedia "Kalchini Assembly constituency"; tier A for named results; tier D for early years without vote counts.

### Alipurduars Lok Sabha (PC 2) historical

| Year | Winner | Party | % | Runner-up | Party | % | Notes |
|---|---|---|---|---|---|---|---|
| 2009 LS | Manohar Tirkey | RSP | 41.22 | Paban Kumar Lakra | AITC | 29.14 | RSP hold; BJP 21.40% third — LF era |
| 2014 LS | Dasrath Tirkey | AITC | 29.46 | Manohar Tirkey | RSP | 27.72 | AITC flip; BJP 27.30% close third — three-way split |
| 2019 LS | John Barla (BTWU) | BJP | 54.36 | Dasrath Tirkey | AITC | 36.69 | BJP surge; RSP 3.91% collapse |

Source: Wikipedia "Alipurduars Lok Sabha constituency"; tier A.

**Key pattern**: The RSP (Left) dominated 1977–2009. The Adivasi vote was the RSP's constituency (Manohar Tirkey was an Adivasi RSP stalwart). The BJP, through BTWU-RSS organizing in the tea gardens from the mid-2000s onward, captured this vote base by 2019. The transition went via a GJM-backed Independent phase in 2009–2011 (Gorkhaland agitation spillover) and a narrow AITC hold in 2016, before the BJP consolidated in 2019.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Kalchini CD Block Primary Census Abstract (via Wikipedia "Kalchini (community development block)") — population, religion, ST/SC, literacy, occupation, language
- Census of India 2011 — Alipurduar II CD Block — population, religion, ST/SC, literacy, occupation, language for Majherdabri GP approximation
- Census of India 2011 — Alipurduar District — religion, ST/SC, sex ratio, literacy, language (district level)
- ECI 2019 LS `2019_AssemblySegmentLevelVotingData.csv` — AC-11 Kalchini segment votes: BJP 111,477 / AITC 64,045 / INC 4,860 / RSP 4,194 / others / NOTA 3,034; electorate 235,753; turnout 80.8%
- ECI 2011 AE / 2016 AE / 2009 by-election / 2006 AE / 2001 AE results — via Wikipedia "Kalchini Assembly constituency"
- ECI 2009/2014/2019 LS Alipurduars — via Wikipedia "Alipurduars Lok Sabha constituency"
- Delimitation Commission of India 2008 — WB Schedule (Kalchini = all 11 GPs of Kalchini CDB + Majherdabri GP of Alipurduar II)

### Secondary sources (tier B/C)

- NFHS-4 (2015-16) West Bengal — household amenity and asset baseline; used for state-level proxy where block data unavailable
- The Print (Jul 2021) "How tea gardens in North Bengal, key to poll fortunes of BJP & TMC" — BTWU presence in 199 of 408 tea gardens; daily wage ₹176 pre-2021; 19 closed gardens; "voted en masse for BJP in 2019"
- The Bastion (2021) "Brewing in Uncertainty" — daily wage ₹176/₹202; sanitation: 15.81% latrine access; drinking water: 30.7% tube-well; housing conditions
- CSDS-Lokniti 2019 NES post-poll — WB regional vote × religion/caste/gender (state rollup, not AC-level)

### Tertiary / journalistic (tier D)

- Wikipedia "Kalchini (Vidhan Sabha constituency)" — constituency composition, election results
- Wikipedia "Kalchini (community development block)" — Census 2011 demographic summary
- Wikipedia "Kalchini, Alipurduar" — geographic, economic, tea-garden overview
- Wikipedia "Alipurduars Lok Sabha constituency" — historical LS results
- Wikipedia "Alipurduar district" — district-level Census 2011 data
- Wikipedia "Alipurduar II (community development block)" — Majherdabri GP context
- The Print (2021) — BTWU organizational reach and John Barla's role
- Down To Earth (2019) — tea garden survey; Adivasi worker conditions
- Scroll.in — "In dying tea gardens of North Bengal, Adivasi workers struggle to make a living wage"
- IDR Online — "The sick tea gardens: Workers seek alternative livelihoods"

### Tier-D/E reliance flags (what to distrust)

- **Caste sub-group shares within ST** (C.2, D.2) — no caste census post-1931 for non-SC/ST sub-groupings; all tribal sub-group shares are tier D/E from journalistic and academic proxies
- **Mother-tongue marginal recovery** (D.1) — Sadri marginal recovers to ~26% vs C.5 anchor 30%; off by ~4pp — Sadri speakers who register as "Hindu" likely underweight in the joint table; flag for v1
- **Vote × religion marginal recovery** (D.15) — BJP marginal recovers to ~53.5% vs tier-A calibration target 58.53%; off by ~5pp — BTWU organizational effect and tribal-cultural BJP mobilization not fully captured in religion-based cross-tabs alone; flag for v1 — the gap is intentional: vote × caste (D.16) should be used as primary simulator input, not vote × religion
- **Asset/media** (C.14, D.4, D.8, D.13) — tea-garden specific data from journalistic sources (tier D); no NFHS sub-district data available for tea-belt specifically
- **Bagan-level spatial heterogeneity** (D.11–D.14) — collapsed to 2 sub-units (Kalchini CDB core + Majherdabri GP); individual bagan-level data not accessible
- **Pre-2006 vote history** (F) — vote count totals not retrieved; only winner/runner-up known from Wikipedia; tier D for those rows

### v0 known gaps (cross-reference methodology §7)

1. Bagan-level demographic data — 18 tea gardens in Kalchini block have distinct social structures; v0 collapses to CDB level; when DCHB Alipurduar Part-A accessible, refine to bagan sub-units
2. ECI 2009 by-election + 2006/2001 AE vote counts — names retrieved from Wikipedia but vote totals not scraped; refine for accurate pre-2019 anchor slopes
3. NFHS-4/5 tea-garden sub-sample — no NFHS sub-block data for tea-belt specifically; using journalistic proxy (tier D) for asset/amenity; refine if IIM Calcutta or TERI plantation surveys become accessible
4. Tribal language sub-group shares (Mundari vs Ho vs Kurukh within "tribal" bucket) — not disaggregated from Census 2011 at block level; using district-level proxy
5. BTWU garden-level membership data — 199 of 408 gardens organized (whole-North-Bengal figure); Kalchini-specific BTWU penetration estimate not available; assumed higher than average given AC-11 BJP margin
6. Majherdabri GP-level demographics — approximated as 1/11 of Alipurduar II CDB; actual GP data not retrieved; refine when DCHB accessible

---

*v0 — generated 2026-04-27, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **These are OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> The simulator must reproduce these results from 2019 priors + narrative injection (BJP governance in Centre, tea-garden wage revision cycle, Gorkha land political developments) without these figures being baked into the calibration input.

### 2021 WB Assembly Election — AC 11 Kalchini (tier A, Wikipedia + ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Bishal Lama | 103,104 | **52.65%** | A — ECI 2021 AE via Wikipedia |
| AITC | Passang Lama | 74,528 | **38.06%** | A — ECI 2021 AE via Wikipedia |
| INC | — | ~5,548 | **~2.83%** | D — Wikipedia (from prompt) |
| RSP | — | ~5,880 | **~3.00%** | D — Wikipedia (from prompt) |
| **BJP margin** | | **28,576 votes** | **~14.59 pp** | A |
| **Total votes** | | 195,815 | | A |

> BJP retained Kalchini in 2021 but with a reduced margin vs 2019 LS (24.90 pp → 14.59 pp). TMC gained ~4.4 pp (33.63% → 38.06%) between 2019 LS and 2021 AE. This is a BJP-locked seat but not BJP-immune.

### 2024 Lok Sabha Election — AC 11 segment within Alipurduars LS (tier A, CSV)

> Figures below are **tier A** — sourced directly from `/home/ubuntu/wb-election-sim/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=11, Kalchini. Total valid votes: 189,974; electorate 254,731; turnout 74.6%.

| Party | Candidate (LS level) | Votes | AC-11 segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Manoj Tigga | 96,391 | **50.74%** | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Prakash Chik Baraik | 81,526 | **42.91%** | A | Same |
| RSP | Mili Oraon | 2,954 | **1.55%** | A | Same |
| NOTA | — | 2,945 | **1.55%** | A | Same |
| IND | Arjun Indwar | 1,823 | **0.96%** | A | Same |
| IND | Parimal Oraon | 1,596 | **0.84%** | A | Same |
| KMSP | Rahul Marak | 738 | **0.39%** | A | Same |
| BSP | — | 907 | **0.48%** | A | Same |
| Others | various | 1,094 | **0.58%** | A | Same |
| **BJP margin over AITC** | | **14,865 votes** | **7.83 pp** | A | Computed |

> **Trend summary for simulation calibration**: Tea-garden seats are BJP-locked but not BJP-immune. TMC clawed back ~9 pp (33.63% in 2019 LS → 42.91% in 2024 LS at AC level), while BJP shed ~8 pp (58.53% → 50.74%) over the same period. The BJP margin compressed from 24.90 pp (2019 LS) to 7.83 pp (2024 LS). The model must capture slow directional drift — not a flip — with the BJP remaining the plurality winner throughout but the AITC closing the gap via gradual welfare-scheme penetration and wage narrative. RSP has collapsed (2.20% → 1.55%), having lost its former Left base entirely to BJP.

### Calibration test

The simulator is considered validated on AC 11 Kalchini if it reproduces 2024 LS AC-11 shares within ±3pp of the CSV tier-A figures:

- BJP target: 51% ± 3pp
- TMC target: 43% ± 3pp
- RSP + others target: 6% ± 3pp
