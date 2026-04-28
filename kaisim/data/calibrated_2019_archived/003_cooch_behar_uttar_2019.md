# AC 3 — Cooch Behar Uttar (SC) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural state of AC 3 Cooch Behar Uttar as of 2019 only — it does not reference any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 3 | A | ECI / Delimitation Commission 2008 |
| AC name | Cooch Behar Uttar | A | ECI |
| Reservation | SC | A | Delimitation 2008 |
| District | Cooch Behar (Koch Bihar) | A | Delimitation 2008 |
| Sub-division | Cooch Behar Sadar | A | WB administrative |
| LS constituency | PC 1 — Cooch Behar (SC reserved) | A | Delimitation 2008 |
| LS segments included with AC 3 | AC 1 Mathabhanga (SC) · AC 2 Cooch Behar Uttar · AC 3 Cooch Behar Dakshin · AC 4 Sitalkuchi (SC) · AC 5 Sitai · AC 6 Dinhata · AC 7 Natabari | A | Delimitation 2008; Wikipedia |
| AC composition | Cooch Behar II community development block (all 13 GPs + 5 census towns) | A | Delimitation 2008; Wikipedia Cooch Behar Uttar AC |
| Geographic note | North Bengal plains, Terai zone near Bhutan/Bangladesh border; Torsha and Tista river basin; Cooch Behar was a princely state until merger with India in 1949 | A | Historical record |
| Two sub-units used in v0 (GP-conditioning) | **U1: Census-towns cluster** (Khagrabari, Takagachh, Chakchaka, Baisguri, Baneswar — ~15.7% pop) · **U2: CDB-II-rural GPs** (13 GP rural remainder — ~84.3% pop) | E | Census 2011; v0 simplification — refine when DCHB Part-A available |

---

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | 343,901 (Cooch Behar II CDB: 289,917 rural + 53,984 urban census towns) | A | Census 2011 — Cooch Behar II CDB (Wikipedia / censusindia.co.in) |
| 2019 projected population | ~372,100 | E | 8-yr compound religion-differential growth (methodology §4): Hindu +1.0%/yr, Muslim +1.3%/yr |
| Sex ratio (2019, F per 1000 M) | ~921 | E | Cooch Behar II CDB 2011: 164,310 F / 179,591 M = 915; slight improvement projected; Cooch Behar district 942 |
| 2019 estimated electorate (18+) | ~272,057 | A | ECI 2019 LS roll — directly from 2019_AssemblySegmentLevelVotingData.csv (AC_NO=3) |
| Estimated M / F / TG split (2019) | 52.0% M / 48.0% F / <0.05% TG | E | CDB-II 2011: 52.2% M / 47.8% F; slight convergence trend to 2019 |
| 2019 polling stations (estimated) | ~290 | E | 2021 AE had ~300 for 263,078 electors; back-projection |
| 2019 total valid votes cast | 231,321 | A | 2019_AssemblySegmentLevelVotingData.csv (AC_NO=3, sum of all candidates + NOTA) |
| 2019 turnout | 85.03% | A | 231,321 / 272,057 (same CSV) |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 82.30 | E | CDB-II 2011: 81.85% (A); Muslim growth +1.3%/yr over 8yr → Hindu share dips ~0.45pp; projected 82.30% |
| Muslim | 17.20 | E | CDB-II 2011: 17.64%; Muslim share grows slightly relative to Hindu; after 8yr projection |
| Christian | 0.18 | E | CDB-II 2011: 0.18% (A); stable |
| Other (Sarna / Sikh / Jain / Buddhist) | 0.32 | E | CDB-II 2011: 0.34%; stable |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC total** | 45.20 | A | CDB-II 2011: SC 154,656 = 44.97% (A); minor growth in SC cohort by 2019 |
| └ **Rajbanshi / Koch-Rajbanshi** | 38.50 | C | Dominant SC sub-group in Cooch Behar — district SC majority (50.17% of total pop is SC); Rajbanshi ~85% of SC pool in Cooch Behar; Outlook India: ~40% of Cooch Behar LS electorate Rajbanshi |
| └ Namasudra / Poundra | 3.20 | E | ~7% of SC pool; secondary SC sub-group |
| └ Bagdi / Hari / Jhalo-Malo | 1.70 | E | ~3.8% of SC pool; fishing/agricultural labouring communities |
| └ Other SC (Rajbhar, Kahar, Dom etc.) | 1.80 | E | ~4% of SC pool; residual |
| **ST total** | 1.00 | A | CDB-II 2011: ST 3,429 = 1.00% (A); Mech, Rajbongshi tribal; stable |
| **UC bhadralok** (Brahmin / Kayastha / Baidya) | 4.50 | E | Lower in rural North Bengal vs. South Bengal; service class + professionals in census towns |
| **OBC** (Saha / Teli / Nai / Kurmi / Sutradhar) | 10.00 | E | Mixed artisan + service OBC; more prominent in Cooch Behar town area |
| **Other Hindu forward / middle** (Goala / Barman / Malo / unclassified) | 21.60 | E | Residual Hindu non-SC-non-ST-non-OBC; 82.30 − 45.20 SC − 1.00 ST − 4.50 UC − 10.00 OBC = 21.60 |
| **Muslim** (all sub-castes pooled) | 17.20 | E | See C.1; Bengali-Sheikh peasantry dominant sub-structure |
| Christian + Other | 0.50 | E | See C.1 |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 0–4 | 8.0 | E | Projected from Census 2011 Cooch Behar district age pyramid; rural North Bengal slightly higher fertility |
| 5–9 | 8.5 | E | |
| 10–14 | 8.5 | E | |
| 15–17 (pre-voter) | 5.5 | E | |
| 18–22 (first-time voters at 2019) | 9.0 | E | |
| 23–27 | 9.5 | E | |
| 28–32 | 9.5 | E | |
| 33–37 | 8.5 | E | |
| 38–42 | 7.5 | E | |
| 43–47 | 7.0 | E | |
| 48–52 | 5.5 | E | |
| 53–57 | 4.5 | E | |
| 58–62 | 3.5 | E | |
| 63–67 | 2.5 | E | |
| 68+ | 2.5 | E | |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 52.00 | E | CDB-II 2011: 52.19% M; slight convergence; Cooch Behar district sex ratio 942 (lower F share) |
| Female | 48.00 | E | |
| Third gender | <0.01 | E | Negligible; rounding not applied |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 93.49 | A | CDB-II 2011: 93.49% Bengali (A; Wikipedia Cooch Behar II) |
| **Rajbongshi / Rajbanshi** | 1.23 | A | CDB-II 2011: 1.23% Rajbongshi (A); distinct Koch-Rajbanshi language, closely related to but distinct from Bengali; language-identity marker for Kamatapur movement |
| Hindi | 1.85 | A | CDB-II 2011: 1.85% Hindi (A); Marwari/Bihari trader + migrant labour fringe in census towns |
| Urdu | 1.00 | E | Estimated Muslim Urdu-speaking pocket; Cooch Behar district 1.17% Hindi+Urdu per district data |
| Other (Mech / Koch / Nepali / Santhali) | 2.43 | E | Residual including tribal languages |
| **Sum** | **100.00** | — | self-check |

(Bilingualism flag: ~8–10% of the population is Bengali+Rajbongshi bilingual, primarily among Rajbanshi SC community; tier E. Rajbongshi-mother-tongue speakers tend to also be functionally bilingual in Bengali.)

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 12.0 | E | CDB-II 2011: literacy 81.39% (A); projected improvement +0.5pp/yr over 8yr → ~85.5% literate; ~14.5% of age-7+ illiterate; adult-corrected ≈ 12% |
| Primary (Class 1–5) | 22.0 | E | Census 2011 education distribution, Cooch Behar district scaled |
| Middle (Class 6–8) | 22.0 | E | |
| Secondary (Class 9–10) | 19.0 | E | |
| Higher Secondary (Class 11–12) | 12.0 | E | |
| Graduate | 9.0 | E | |
| Postgraduate | 4.0 | E | UBKV (Uttar Banga Krishi Vishwavidyalaya) located near constituency; slightly elevated postgrad rate |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main worker | 32.0 | E | CDB-II 2011: total workers 37.31% of population; age-18+ adult worker share slightly higher; stable trend |
| Marginal worker | 12.0 | E | High marginal agricultural labour in rural GPs |
| Non-worker (housewife / elderly / retired) | 36.0 | E | Female non-worker share high in rural North Bengal |
| Student (18–22 only, in education) | 11.0 | E | |
| Unemployed (educated, actively seeking) | 9.0 | E | Educated unemployment salience in North Bengal towns |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 20.0 | E | CDB-II 2011: 21.35% cultivators; paddy, jute, potato — slight decline by 2019 |
| Agricultural labourer | 32.0 | E | CDB-II 2011: 33.77% ag-labour; dominant occupational category |
| Household industry | 4.0 | E | CDB-II 2011: 3.04%; hand-loom, tobacco processing |
| Manufacturing (organised) | 3.0 | E | Limited industrial base; some agro-processing |
| Construction | 6.0 | E | Includes out-migrants returning seasonally |
| Trade / retail | 12.0 | E | Census-town (Khagrabari, Takagachh) commercial hubs |
| Transport / logistics | 5.0 | E | Road transport; North Bengal highway connectivity |
| Services (private) | 10.0 | E | Including pisciculture workers (17,863 persons in CDB-II fisheries) |
| Government services / teachers | 5.0 | E | WB government employees; teachers; local administration |
| Out-migrant worker (working outside WB) | 3.0 | D | Smaller than South Bengal out-migration; some to Assam tea industry |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.0 | E | Census B-04 WB rural pattern |
| Employee (regular wage) | 25.0 | E | Govt + organised sector + retail employees |
| Single worker (own-account) | 48.0 | E | Cultivator + artisan + small trader |
| Family worker (unpaid) | 25.0 | E | Within agri-household; female family labour high in paddy harvest |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL household | 24.0 | C | Cooch Behar district: 48% SC majority + North Bengal poverty levels; WB overall BPL ~22% (2011 Tendulkar); Cooch Behar above-average poverty |
| Above-Poverty-Line, low-income | 36.0 | E | Ag-labourer + marginal cultivator households |
| Lower-middle | 24.0 | E | Small traders, petty services, census-town working class |
| Middle | 12.0 | E | Govt employees, established businesses |
| Upper-middle / well-off | 4.0 | E | Khagrabari census-town commercial class + Rajbanshi zamindari remnants |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Municipality location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **U1: Census-towns cluster** (Khagrabari 23,122 + Takagachh 12,414 + Chakchaka 8,582 + Baisguri 5,021 + Baneswar 4,841) | 15.70 | A | Census 2011: 53,984 urban / 343,901 total = 15.70%; held stable to 2019 |
| **U2: CDB-II rural GPs** (13 GPs: Ambari, Baneswar-GP, Bararangras, Chakchaka-GP, Dhandhingguri, Gopalpur, Khagrabari-GP, Khapaidanga, Madhupur, Marichbari Kholta, Patlakhawa, Pundibari, Takagachh Rajarhat) | 84.30 | A | Remainder: 289,917 / 343,901; v0 collapses 13 GPs into one rural cell — refine when DCHB Part-A accessible |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg HH size | 4.5 persons | E | WB rural North Bengal: Census 2011 ~4.4–4.6; Cooch Behar slightly higher fertility than state average |
| Nuclear HH | 65.0 | E | NFHS-4 WB rural pattern; slightly more joint HH in Rajbanshi agriculture communities |
| Joint HH | 28.0 | E | Agricultural joint households common in paddy-farming Rajbanshi families |
| Extended / multi-generation | 7.0 | E | |
| **Sum** | **100.00** | — | self-check |

(Household head: ~87% male-headed, 13% female-headed; tier E from Cooch Behar district pattern.)

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never married | 27.0 | E | Census 2011 Cooch Behar district pattern; young voter cohort |
| Currently married | 64.0 | E | |
| Widowed | 8.0 | E | Slightly elevated vs. state average; concentrated in 60+, female-skewed |
| Separated / divorced | 1.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 74.0 | C | NFHS-4 WB rural ~60%, urban ~89%; North Bengal rural lower than state; CDB-II 84% rural → weighted ~70–74% by 2019 |
| Radio | 4.0 | C | Declining nationally; rural North Bengal slightly higher than state |
| Mobile phone (any) | 84.0 | C | NFHS-4 WB ~78%; +Jio rollout 2016–19; rural AC → ~84% |
| Smartphone with internet | 40.0 | C | NFHS-4 WB rural ~30–35%; Jio-driven growth; lower than South Bengal urban; ~40% by 2019 |
| Computer | 6.0 | C | NFHS-4 WB rural 4%; urban 15%; CDB-II 84% rural → ~6% |
| Two-wheeler | 30.0 | C | NFHS-4 WB rural 18%; growth; North Bengal ~25–30% |
| Four-wheeler | 5.0 | C | Limited in predominantly rural AC |
| Banking access (any) | 88.0 | B | PMJDY 2014– saturation in WB; Cooch Behar district PMJDY enrollment high |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved drinking water source | 85.0 | C | NFHS-4 WB rural ~82%; +minor improvement; North Bengal surface water dominance |
| Improved sanitation (latrine) | 68.0 | C | NFHS-4 WB rural ~51%; +Swachh Bharat 2014–19 (+15pp rural); North Bengal lower baseline than South Bengal |
| LPG / clean cooking fuel | 38.0 | C | NFHS-4 WB rural ~24%; +Ujjwala 2016–19 (+12pp rural); North Bengal rural Ujjwala rollout significant but wood-fuel habits persist |
| Wood / biomass fuel | 57.0 | C | Dominant; declines as LPG rises |
| Other fuel (kerosene / dung) | 5.0 | C | |
| Electricity | 94.0 | C | Census 2011 Cooch Behar CDB-II electrification lower than state average; +Saubhagya 2017–19 |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native (born in Cooch Behar district or same village/town) | 84.0 | D | Cooch Behar was a princely state with closed borders until 1949; low historical out-migration/in-migration; predominantly local-born population |
| WB other district (in-migrant) | 6.0 | D | Some service class from Jalpaiguri / Siliguri corridor; Kolkata-connected traders |
| Other Indian state | 4.0 | D | Marwari/Bihari traders (Hindi-speaking fringe) in Khagrabari/Takagachh census towns |
| Bangladesh-origin (refugee / border community) | 4.0 | D | Unlike South Bengal, Cooch Behar Rajbanshi community is largely locally settled (pre-partition); some border-area Muslim families with Bangladesh connections; smaller refugee footprint than Matua belt |
| Nepal / Bhutan-origin | 1.0 | E | North Bengal proximity; tea-garden linked population fringe |
| Out-migrant (registered here but working outside) | 1.0 | E | Census reverse; mostly seasonal |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Rajbongshi | Hindi | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 90.0 | 1.5 | 2.0 | 0.0 | 6.5 | E | CDB-II: 93.49% Bengali, 1.23% Rajbongshi overall; Rajbongshi concentrated within Hindu SC; Hindi-trader fringe within Hindu |
| Muslim | 96.0 | 0.0 | 0.5 | 3.0 | 0.5 | E | Bengali-Sheikh dominant Muslim; small Urdu pocket; no Rajbongshi-speaking Muslim |
| Christian | 90.0 | 0.0 | 5.0 | 0.0 | 5.0 | E | Tiny base |
| Other | 50.0 | 10.0 | 30.0 | 0.0 | 10.0 | E | Marwari/tribal mix |
| **Marginal recovery — Bengali** | | | | | | | Hindu(82.30)×0.90 + Muslim(17.20)×0.96 + Chrisitan(0.18)×0.90 + Other(0.32)×0.50 = 74.07 + 16.51 + 0.16 + 0.16 = **90.90** vs C.5 **93.49** ⚠ off by 2.6pp — v1 gap: Hindi-/Rajbongshi-speaker distribution within Hindu needs refinement |

### D.2 Religion × Caste (Hindu-internal sub-structure)

P(caste ‖ Hindu) — % within Hindu population only.

| Caste sub-group | % of Hindu | Tier | Source |
|---|---|---|---|
| **SC: Rajbanshi / Koch-Rajbanshi** | 46.8 | C | 38.50% of total / 82.30% Hindu = 46.8% of Hindu; dominant SC in Cooch Behar |
| SC: Namasudra / Poundra | 3.9 | E | 3.20% total / 82.30% Hindu |
| SC: Bagdi / Hari / Jhalo-Malo | 2.1 | E | 1.70% total / 82.30% Hindu |
| SC: Other | 2.2 | E | 1.80% total / 82.30% Hindu |
| ST | 1.2 | E | 1.00% total / 82.30% Hindu |
| UC bhadralok | 5.5 | E | 4.50% total / 82.30% Hindu |
| OBC | 12.1 | E | 10.00% total / 82.30% Hindu |
| Other Hindu middle | 26.2 | E | 21.60% total / 82.30% Hindu = 26.2%; Barman, Malo, Goala, unclassified |
| **Sum** | **100.0** | — | self-check |

P(Muslim sub-caste ‖ Muslim):

| Muslim sub-group | % of Muslim | Tier | Source |
|---|---|---|---|
| Sheikh (Bengali Muslim peasantry) | 75 | D | Dominant in Cooch Behar; North Bengal border Muslim peasantry |
| Pathan / Sayyid / Mughal | 5 | D | Small ashraf fraction in Cooch Behar town |
| OBC Muslim (Jolaha / Nai / Darzi etc.) | 14 | D | |
| Nasya-Sheikh / Other | 6 | D | |
| **Sum** | **100** | — | self-check |

### D.3 Religion × Migration / birthplace

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB-other-dist | Other state | Bangladesh-origin | Nepal/Bhutan | Out-migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 84 | 6 | 5 | 3 | 1 | 1 | D | Rajbanshi are largely native; small Bangladesh-origin refugee fringe; Marwari traders = other-state |
| Muslim | 82 | 8 | 1 | 8 | 0 | 1 | D | Border-area Muslim community has higher Bangladesh-heritage share; North Bengal Muslim border overlap |
| Christian | 80 | 10 | 5 | 5 | 0 | 0 | E | Mixed |
| Other | 50 | 15 | 30 | 5 | 0 | 0 | E | Marwari/Bihari traders = other state dominant |
| **Marginal recovery — Bangladesh** | | | | | | | Hindu(82.30)×0.03 + Muslim(17.20)×0.08 + Others(0.50)×0.04 = 2.47 + 1.38 + 0.02 = **3.87%** vs C.16 **4.0%** ✓ |

### D.4 Religion × Asset / media (TV, smartphone, banking)

P(owns asset ‖ religion) — % within each religion.

| Religion | TV | Smartphone-internet | Banking | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 76 | 43 | 90 | C | NFHS-4 WB religion gap pattern; Hindu higher in rural CDB-II |
| Muslim | 65 | 29 | 78 | C | Muslim asset gap: NFHS-4 WB pattern; lower rural Muslim asset base |
| Christian | 78 | 45 | 92 | E | Approximation |
| Other | 82 | 52 | 90 | E | Trader/Marwari community higher assets |

### D.5 Caste × Education

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Sec | HS | Grad | PG | Tier |
|---|---|---|---|---|---|---|---|---|
| UC bhadralok | 4 | 9 | 13 | 18 | 20 | 24 | 12 | E |
| **Rajbanshi-SC** | 14 | 22 | 22 | 19 | 12 | 8 | 3 | E |
| Other SC (Namasudra/Bagdi) | 20 | 26 | 22 | 16 | 9 | 5 | 2 | E |
| ST | 22 | 28 | 22 | 16 | 7 | 4 | 1 | E |
| OBC | 12 | 21 | 22 | 19 | 13 | 10 | 3 | E |
| Other Hindu middle | 12 | 22 | 22 | 19 | 13 | 9 | 3 | E |
| Muslim (all) | 18 | 24 | 23 | 18 | 10 | 6 | 1 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Cohort | Male grad+ | Female grad+ | Tier | Source |
|---|---|---|---|---|
| 18–22 | 16 | 15 | E | Near parity in youngest cohort; education expansion in North Bengal |
| 23–27 | 15 | 12 | E | |
| 28–32 | 13 | 8 | E | |
| 33–42 | 10 | 5 | E | |
| 43–57 | 7 | 2 | E | Older female cohort: very low; CDB-II female literacy 75.85% |
| 58+ | 5 | 2 | E | |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender) — proxy for household formation.

| Age | Male married | Female married | Tier |
|---|---|---|---|
| 18–22 | 5 | 30 | E |
| 23–27 | 40 | 80 | E |
| 28–32 | 82 | 93 | E |
| 33–47 | 93 | 90 | E |
| 48–62 | 90 | 78 | E |
| 63+ | 75 | 33 | E (widows concentrate here) |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone-internet | TV | Tier | Source |
|---|---|---|---|---|
| Cultivator | 30 | 68 | C | Rural ag baseline — North Bengal lower than state avg |
| Ag-labourer | 22 | 58 | C | Lowest income; low asset base |
| Household industry | 35 | 70 | C | Tobacco / handloom workers |
| Manufacturing | 48 | 78 | C | |
| Construction | 42 | 72 | C | |
| Trade / retail | 62 | 88 | C | Census-town commercial cluster |
| Transport | 56 | 80 | C | Road transport workers |
| Services (private) | 65 | 85 | C | |
| Govt services | 80 | 92 | C | Highest; teachers + administrators |
| Out-migrant | 65 | 75 | D | Seasonal migrants, smartphone-heavy |
| Pisciculture / fisheries | 28 | 64 | E | CDB-II has 17,863 fisheries workers; below-median asset base |

### D.9 Education × Workforce participation

P(unemployed-and-seeking ‖ education) — educated-unemployment proxy.

| Education | Unemployed-seeking | Main-worker rate | Tier |
|---|---|---|---|
| Illiterate | 2 | 36 | E |
| Primary | 4 | 38 | E |
| Middle | 6 | 35 | E |
| Secondary | 9 | 30 | E |
| Higher Secondary | 15 | 24 | E |
| Graduate | 18 | 27 | E (job-aspirant pool in North Bengal towns) |
| Postgraduate | 12 | 38 | E |

### D.10 Asset / media × Bilingualism

P(bilingual Bengali + Rajbongshi ‖ media-access tier).

| Media tier | Bilingual Beng+Rajbongshi % | Tier | Source |
|---|---|---|---|
| TV-only HH | 6 | E | Rajbongshi-identity households watch Bengali TV but maintain language |
| TV + smartphone HH | 8 | E | YouTube vernacular content consumption |
| Smartphone-only HH | 7 | E | |
| No-asset HH | 5 | E | Rural Rajbanshi households with low media access maintain language |
| **Population-wide Rajbongshi bilingual rate** | ~7 | E | C.5 narrative anchor |

### D.11 GP × Religion (sub-AC spatial heterogeneity, v0 = 2 sub-units)

P(religion ‖ GP/Census-town location).

| Sub-unit | Hindu | Muslim | Other | Tier | Source |
|---|---|---|---|---|---|
| **U1: Census-towns cluster** (15.7% pop) | 90.0 | 9.0 | 1.0 | E | Khagrabari and Takagachh census towns: higher Hindu proportion; traders and service class dominant |
| **U2: CDB-II rural GPs** (84.3% pop) | 81.0 | 18.5 | 0.5 | E | Rural GPs closer to CDB-II block average; Muslim peasantry concentrated in rural GPs |
| **Marginal recovery — Hindu** | | | | | 0.157×90.0 + 0.843×81.0 = 14.13 + 68.28 = **82.41** vs C.1 **82.30** ✓ within ±0.5 |
| **Marginal recovery — Muslim** | | | | | 0.157×9.0 + 0.843×18.5 = 1.41 + 15.60 = **17.01** vs C.1 **17.20** ✓ within ±0.5 |

### D.12 GP × Caste (within sub-unit, key categories)

P(caste ‖ GP).

| Sub-unit | UC | Rajbanshi-SC | Other SC | ST | OBC + Other Hindu | Muslim | Tier |
|---|---|---|---|---|---|---|---|
| Census-towns cluster | 8 | 32 | 5 | 0.5 | 45 | 9 | E |
| CDB-II rural GPs | 3 | 40 | 7 | 1.2 | 30 | 18.5 | E |
| Source | Town service class | Rajbanshi dominant in rural; slightly lower in towns | SC residual | Minimal ST | Mixed artisan/cultivator | Rural border Muslim | |

### D.13 GP × Asset / media

| Sub-unit | TV | Smartphone-internet | Computer | Banking | Tier |
|---|---|---|---|---|---|
| Census-towns cluster | 88 | 58 | 12 | 94 | C |
| CDB-II rural GPs | 70 | 36 | 4 | 86 | C |
| Source | NFHS-4 WB urban/rural gradient | NFHS-4/5 WB rural + Jio rollout | | PMJDY enrolment pattern | |

### D.14 GP × Amenities

| Sub-unit | LPG | Improved sanitation | Improved water | Electricity | Tier |
|---|---|---|---|---|---|
| Census-towns cluster | 68 | 88 | 96 | 99 | C |
| CDB-II rural GPs | 32 | 62 | 83 | 92 | C |
| Source | NFHS-4/5 urban-rural gradient + Ujjwala/Swachh Bharat rollout; Saubhagya electrification 2017–19 | | | | |

### D.15 Vote × Religion (2019 LS, AC 3 segment)

P(party ‖ religion) — calibrated to AC 3 segment 2019 result (BJP 51.27%, AITC 39.50%, AIFB 4.28%, INC 2.45%).

| Religion | BJP | AITC | AIFB | INC | Other/NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| **Hindu** | **61.4** | **32.5** | **4.6** | **1.2** | **0.3** | C | Solved from AC 3 segment result; consistent with Quint/Outlook: Rajbanshi-led Hindu bloc heavily BJP in 2019; AIFB share collapsed from 2016 AE stronghold |
| Muslim | 5.0 | 72.0 | 3.0 | 8.0 | 12.0 | C | CSDS-Lokniti 2019 WB; Muslim plurality strongly AITC; higher AITC Muslim share in North Bengal vs. South (less Congress competition) |
| Christian | 25.0 | 52.0 | 8.0 | 8.0 | 7.0 | E | Approximation; small population |
| Other | 45.0 | 30.0 | 5.0 | 5.0 | 15.0 | E | |
| **Marginal recovery — BJP** | | | | | | | Hindu(82.30)×0.614 + Muslim(17.20)×0.05 + Other(0.50)×0.35 = 50.53 + 0.86 + 0.18 = **51.57** vs target **51.27** ✓ within ±0.5 |
| **Marginal recovery — AITC** | | | | | | | Hindu(82.30)×0.325 + Muslim(17.20)×0.72 + Other(0.50)×0.40 = 26.75 + 12.38 + 0.20 = **39.33** vs target **39.50** ✓ within ±0.5 |

### D.16 Vote × Caste (2019 LS, AC 3 segment)

P(party ‖ caste) — calibrated to Cooch Behar LS result; adjusted for Rajbanshi BJP swing.

| Caste | BJP | AITC | AIFB | INC | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC bhadralok | 55 | 30 | 5 | 5 | 5 | C | CSDS 2019 WB; UC BJP-leaning |
| OBC | 42 | 34 | 8 | 10 | 6 | C | Mixed; AIFB retained some OBC base |
| **Rajbanshi-SC** | **65** | **27** | **5** | **1** | **2** | **C** | **Load-bearing**: Rajbanshi ~40% of electorate; BJP consolidated Rajbanshi SC vote in 2019 via Nisith Pramanik candidacy + Greater Cooch Behar movement alliance (Ananta Rai-BJP axis). All 5 WB seats with >15% Rajbanshi went BJP in 2019. |
| Other SC | 52 | 33 | 8 | 4 | 3 | C | |
| ST | 40 | 35 | 10 | 8 | 7 | C | |
| Muslim (any caste) | 5 | 72 | 3 | 8 | 12 | C | Same as D.15 |

### D.17 Vote × Gender (2019 LS, AC 3 segment)

P(party ‖ gender). Pre-2019 baseline — no Lakshmir Bhandar in 2019.

| Gender | BJP | AITC | AIFB | INC | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 54 | 37 | 4 | 3 | 2 | C | Swarajya/CSDS 2019 WB; Rajbanshi male vote heavily BJP |
| Female | 49 | 42 | 5 | 2 | 2 | C | Smaller BJP gender gap in Rajbanshi SC seats than state average; AITC welfare scheme retention |

### D.18 Vote × Welfare-scheme exposure (2019)

P(party ‖ household has scheme exposure). 2019-available TMC schemes: Krishak Bandhu (Jan 2019), Kanyashree (2013), Swasthya Sathi (2016), Sabuj Sathi (2015), Khadya Sathi (2016). **Lakshmir Bhandar does NOT exist in 2019.**

| Exposure | BJP | AITC | AIFB | INC | Tier | Source |
|---|---|---|---|---|---|---|
| Krishak Bandhu (cultivator HH) | 32 | 54 | 8 | 4 | C | TMC welfare-stack credit in ag-dependent AC; AIFB retains farm-peasant loyalty |
| Kanyashree (girl-student HH) | 35 | 50 | 9 | 4 | C | |
| Swasthya Sathi enrollee | 40 | 46 | 8 | 4 | C | Broad-based; weakest TMC tilt |
| Sabuj Sathi (bicycle HH) | 36 | 50 | 8 | 4 | C | |
| Khadya Sathi (PDS) | 42 | 45 | 7 | 4 | C | Universal; weakest tilt |
| **No state-scheme exposure** | 58 | 28 | 6 | 4 | C | BJP-leaning; unattached voter pool |

---

## E. 2019 baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp on each major party.

### Whole Cooch Behar LS (PC 1) — 2019 result (tier A, ECI)

| Party | Candidate | Votes | % |
|---|---|---|---|
| BJP | **Nisith Pramanik** | 732,594 | **47.98** |
| AITC | Paresh Chandra Adhikary | 677,363 | **44.43** |
| AIFB | (Forward Bloc candidate) | — | — |
| **Margin** | BJP over AITC | **54,231** | **3.55 pp** |

Note: Nisith Pramanik is himself a Rajbanshi leader; his candidacy was central to Rajbanshi community consolidation behind BJP in 2019. BJP backed the Ananta Rai faction of the Greater Cooch Behar People's Association (a Kamatapur-adjacent Rajbanshi statehood party) ahead of this election.

### AC 3 segment — 2019 LS (tier A, ECI CSV)

> All figures are **tier A** — sourced directly from `2019_AssemblySegmentLevelVotingData.csv`, State=West Bengal, AC_NO=3, COOCHBEHAR UTTAR. Total electors: 272,057. Total votes: 231,321. Turnout: 85.03%.

| Party | Candidate | Votes | % | Tier |
|---|---|---|---|---|
| BJP | Nisith Pramanik | 118,606 | **51.27** | A |
| AITC | Paresh Chandra Adhikary | 91,380 | **39.50** | A |
| AIFB | Gobinda Chandra Roy | 9,910 | **4.28** | A |
| INC | Piya Roy Chowdhury | 5,664 | **2.45** | A |
| NOTA | — | 2,087 | **0.90** | A |
| IND (3) | Nirmal Kr. Roy + Harekrishna Sarkar + Naresh C. Roy | 2,329 | **1.01** | A |
| Others (SUCI+KPPU+AMB+WPOI) | various | 1,345 | **0.58** | A |
| **BJP margin over AITC** | | **27,226** | **11.77 pp** | A |

**Calibration note:** AC 3 outperformed the whole-PC BJP average (51.27% vs 47.98%) — confirming this sub-segment is a BJP stronghold within Cooch Behar LS. AITC underperformed the whole-PC average (39.50% vs 44.43%) — the Muslim-heavy neighbouring ACs (Mathabhanga, Natabari) account for most AITC's PC-level upside.

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 3 Cooch Behar Uttar specifically (Assembly Elections)

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin |
|---|---|---|---|---|---|---|---|---|---|
| 2011 AE | Nagendra Nath Roy | **AIFB** | 84,825 | 45.11 | Prasenjit Barman | AITC | 82,628 | 43.94 | 2,197 (very close) |
| 2016 AE | Nagendra Nath Roy | **AIFB** | 97,629 | 43.63 | Parimal Barman | AITC | 85,336 | 38.14 | 12,293 |

**History note:** Cooch Behar Uttar was an AIFB / Left-aligned stronghold through 2011–2016 Assembly elections. The Forward Bloc retained this seat even in the 2011 anti-Left wave that swept most of WB. The 2019 LS swing to BJP (~51%) was a dramatic reversal of the local Left legacy, driven by Rajbanshi community consolidation behind Nisith Pramanik. In 2016 AE, BJP received only ~7% of the vote (mostly absorbed in the "Others 18.24%" bucket); by 2019 LS they captured 51%.

### Cooch Behar Lok Sabha (PC 1) historical

| Year | Winner | Party | Votes | % | Runner-up | Party | % | Margin | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2009 LS | Nripendra Nath Roy | **AIFB** | 508,677 | 44.66 | Arghya Roy Pradhan | AITC | 41.65 | 41,749 | Left held in 2009 anti-LF wave attenuation |
| 2014 LS | Renuka Sinha | **AITC** | 526,499 | 39.51 | Dipak Kumar Roy | AIFB | 32.98 | 87,107 | AITC won as Left collapsed nationally |
| 2019 LS | Nisith Pramanik | **BJP** | 732,594 | 47.98 | Paresh C. Adhikary | AITC | 44.43 | 54,231 | BJP swept North Bengal; Rajbanshi bloc consolidation |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- Census of India 2011 — Cooch Behar II Community Development Block Primary Census Abstract (via Wikipedia "Cooch Behar II (community development block)") — population, religion, SC, literacy, mother tongue, occupation
- Census of India 2011 — Cooch Behar district (via Wikipedia "Cooch Behar district") — district-level cross-checks, SC majority, language shares
- `2019_AssemblySegmentLevelVotingData.csv` — ECI GE2019 AC-segment vote tallies, AC_NO=3 (tier A; Section E calibration target)
- Delimitation Commission of India 2008 — WB Schedule (Cooch Behar Uttar AC 3 = Cooch Behar II CDB entire)
- Wikipedia "Cooch Behar Uttar Assembly constituency" — 2011 and 2016 AE results (tier A via ECI)
- Wikipedia "Cooch Behar Lok Sabha constituency" — 2009, 2014, 2019 LS results (tier A via ECI)

### Secondary sources (tier B/C)
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership, media-access baselines
- NFHS-5 (2019-21) West Bengal state report — smartphone/banking cross-check
- CSDS-Lokniti 2019 NES post-poll — vote × religion / caste / gender (WB regional pattern)
- Swarajya Magazine summary of CSDS 2019 WB cross-tabs — WB Hindu/Muslim/caste vote shares
- Pew Research India 2021 — religion-differential growth projections 2011→2019
- Outlook India "Stained Floodplains" — Rajbanshi electoral analysis, Cooch Behar LS (~40% Rajbanshi electorate)
- `2024_AssemblySegmentLevelVotingData.csv` — used only in Section H (post-2019 gate)

### Tertiary / journalistic (tier D)
- The Quint — "BJP's Rise in North Bengal Reversed?" — BJP Rajbanshi vote share patterns
- The Print — "BJP Anant Maharaj as RS candidate" — Greater Cooch Behar / BJP alignment pre-2019
- Scroll.in — "BJP stokes statehood demands in Cooch Behar" — Kamatapur movement BJP connection
- Wikipedia "Cooch Behar Lok Sabha constituency" / "Cooch Behar Uttar Assembly constituency" — electoral history

### Tier-D/E reliance flags (what to distrust)
- **Rajbanshi sub-group share within SC** (C.2, D.2) — no post-1931 caste census for non-SC/ST nationally; SC composition from journalistic anchor (~85% of SC pool = Rajbanshi) using Outlook India; tier C
- **Caste-level vote shares** (D.16) — calibrated from AC result + CSDS WB regional; Rajbanshi-specific BJP share (65%) derived from narrative anchors, not direct survey; tier C
- **Migrant/birthplace shares** (C.16, D.3) — no public AC-level Census D-series; tier D from Cooch Behar princely-state history + border analysis
- **GP-level data** (D.11–D.14) — collapsed to 2 sub-units; DCHB Cooch Behar Part-A not accessible in v0; refine when available
- **Asset/media** (C.14, D.4, D.13) — NFHS-4/5 WB rural/urban averages proxied to AC; tier C; North Bengal below-state-average adjustment applied
- **Vote × Welfare** (D.18) — CSDS WB pattern; no AC-level welfare-scheme enrollment data; tier C

### v0 known gaps (see methodology §7)
1. DCHB Cooch Behar Part-A — collapsed 13 GPs + 5 census towns into 2 sub-units; refine when accessible
2. GP-level census data — individual GP populations not available; equal-weight approximation applied within rural sub-unit
3. Census HH-13 asset/media — using NFHS WB rural/urban averages; block-level not fetched
4. Census D-series migration — using qualitative anchor (princely-state low-migration history); no AC-level D-series
5. CSDS WB regional caste cross-tabs for Rajbanshi specifically — using Quint/Outlook narrative synthesis; full Lokniti North Bengal report not accessed
6. Cooch Behar municipality (77,935 pop) confirmed outside AC 3 (falls in AC 4 Cooch Behar Dakshin via Cooch Behar I CDB); no municipal population correction needed

---

*v0 — generated 2026-04-27, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **These are OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> The simulator must reproduce these results from 2019 priors + narrative injection without these figures being baked into the calibration input.

### 2021 WB Assembly Election — AC 3 Cooch Behar Uttar (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Sukumar Roy | 120,483 | **49.40** | A — ECI 2021 AE |
| AITC | Binay Krishna Barman | 105,868 | **43.40** | A — ECI 2021 AE |
| AIFB | Nagendra Nath Roy | ~11,600 | **4.70** | A — ECI 2021 AE |
| **BJP margin** | | **14,615 votes** | **5.99 pp** | A |
| Total valid votes | 243,916 | Turnout: 263,078 electors | ~92.7% | A — Wikipedia |

### 2024 Lok Sabha Election — AC 3 segment within Cooch Behar LS (PC 1) (tier A, CSV)

> All figures are **tier A** — sourced directly from `2024_AssemblySegmentLevelVotingData.csv`, AC_NO=3. Total electors: 292,443; total votes: 244,811; turnout: 83.71%.

| Party | Candidate (LS level) | Votes | AC-3 segment % | Tier |
|---|---|---|---|---|
| BJP | Nisith Pramanik | 123,859 | **50.59** | A |
| AITC | Jagadish Chandra Barma Basunia | 105,870 | **43.25** | A |
| AIFB | Nitish Chandra Roy | 6,251 | **2.55** | A |
| INC | Piya Roy Chowdhury | 2,191 | **0.89** | A |
| NOTA | — | 2,110 | **0.86** | A |
| Others | various | 4,530 | **1.85** | A |
| **BJP margin over AITC** | | **17,989 votes** | **7.35 pp** | A |

### AC-level structural stability note (for simulator)

**AC-level share was remarkably static across all 3 elections (BJP ~50–51%, AITC ~39–43%).** The Cooch Behar LS seat flipped AITC in 2024 because Muslim-heavy ACs elsewhere in the LS (Mathabhanga, Natabari, Sitai, Dinhata) shifted back toward TMC. Cooch Behar Uttar AC 3 is **structurally BJP-Rajbanshi**: the BJP's 2019 majority has held across both the 2021 AE and 2024 LS segment. Key simulation constraint: any model that de-stabilizes AC 3 away from 50% BJP is almost certainly mis-calibrated on the Rajbanshi identity vote.

### Calibration test
The simulator is considered validated on this seat if it reproduces 2024 LS AC-3 shares within ±3pp of the CSV tier-A figures:
- BJP target: 51% ± 3pp
- AITC target: 43% ± 3pp
- AIFB + others target: 6% ± 3pp
