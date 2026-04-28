# AC 123 — Sandeshkhali (ST) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural state of AC 123 Sandeshkhali as of 2019 only — it does not reference any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 123 | A | ECI / Delimitation Commission 2008 |
| AC name | Sandeshkhali | A | ECI |
| Reservation | ST | A | Delimitation 2008 |
| District | North 24 Parganas | A | Delimitation 2008 |
| Sub-division | Basirhat | A | WB administrative |
| LS constituency | 18 — Basirhat | A | Delimitation 2008 |
| LS segments included with AC 123 | AC 99 Baduria · 121 Haroa · 122 Minakhan (SC) · 123 Sandeshkhali (ST) · 124 Basirhat Dakshin · 125 Basirhat Uttar · 126 Hingalganj (SC) | A | Delimitation 2008 |
| AC composition | Sandeshkhali I CD Block (all 8 GPs: Bayermari I, Bayermari II, Kalinagar, Sarberia Agarhati, Nazat I, Nazat II, Sehera Radhanagar, Hatgachhi) + 7 of 8 GPs of Sandeshkhali II CD Block (Beramajur I, Beramajur II, Durgamandap, Jeliakhali, Korakati, Manipur, Sandeshkhali) — excludes Khulna GP of CDB-II | A | Delimitation 2008; Wikipedia Sandeshkhali Assembly constituency |
| Geographic note | Sundarbans fringe; river delta and partially tidal island terrain; Basirhat sub-division, North 24 Parganas; porous India-Bangladesh border corridor | A | Delimitation 2008; Basirhat LS Wikipedia |
| Two sub-units used in v0 (GP-conditioning) | **U1: CDB Sandeshkhali-I** (all 8 GPs, ~53.9% of AC pop) · **U2: CDB Sandeshkhali-II AC-share** (7 of 8 GPs, ~46.1% of AC pop) | E | v0 simplification — see methodology §3 |

---

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~305,319 (CDB-I 164,465 + 7/8 of CDB-II 160,976 = 140,854) | A/E | Census 2011 (CDB populations: A); 7/8 GP-equal-weight assumption: E |
| 2019 projected population | ~333,245 | E | 8-yr compound religion-differential growth (methodology §4); differential growth from Pew India 2021 |
| Sex ratio (2011, F per 1000 M) | ~962 (CDB-I: 960; CDB-II: 965; weighted) | A | Census 2011 via Department of Sundarbans Affairs WB |
| Sex ratio (2019, F per 1000 M) | ~963 | E | Minimal projection drift from 2011 baseline |
| 2019 electorate (ECI roll) | 229,369 | A | ECI 2019 LS voter roll; 2019 CSV AC-level field |
| Estimated M / F / TG split of electorate (2019) | ~51.0% M / 49.0% F / <0.05% TG | E | Derived from 2011 sex ratio 962 projected to 2019 |
| 2019 polling stations (estimated) | ~240–250 | E | Back-projection from 2024 LS (NOTA=735 votes, a round proxy); v0 unconfirmed |
| 2019 voter turnout | 86.10% | A | ECI 2019 LS: 197,486 valid votes / 229,369 electors |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu (incl. ST population census-classified as Hindu) | 72.42 | A/E | CDB-I 2011: 69.19% Hindu (A); CDB-II 2011: 77.17% Hindu (A); weighted to AC; projected 2011→2019 at +1.0%/yr differential |
| Muslim | 27.15 | A/E | CDB-I 2011: 30.42%; CDB-II 2011: 22.27%; weighted; projected +1.3%/yr differential |
| Christian | 0.25 | A | CDB-I: 0.21%; CDB-II: 0.43%; weighted — tiny base |
| Sarna / ORP | 0.10 | E | Census counts most ST practitioners under 'Hindu'; residual Sarna fraction estimated; CDB-I 'Other' 0.18%, CDB-II 0.11% — fraction attributable to Sarna/tribal religion |
| Other (Sikh / Jain / Buddhist) | 0.08 | E | Census 'Other/Not stated' residual |
| **Sum** | **100.00** | — | self-check |

_Note on ST religion: The Santhal, Munda, Oraon, and Bhumij communities who form the ST population (~24.78%) are predominantly returned as 'Hindu' in Census 2011. A minority — estimated ~10–15% of ST pop — practice Sarna/ORP but are largely captured in the Hindu count. For simulation purposes the ST community is modelled as a caste sub-group within Hindu (C.2) with differentiated vote behaviour (D.16)._

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **ST total** | 24.78 | A | CDB-I: 42,674 (25.95%); CDB-II 7/8: ~33,234 (23.59%); weighted AC aggregate (Census 2011) |
| └ Santhal | 15.0 | D | Dominant ST group in Sundarbans/North 24 Parganas — Santhal, Munda, Oraon brought to reclaim delta land; Santhal largest sub-group |
| └ Munda | 5.0 | D | Second major group in Sundarbans fringe |
| └ Oraon / Bhumij / Other ST | 4.78 | E | Residual |
| **SC total** | 37.36 | A | CDB-I: 50,812 (30.90%); CDB-II 7/8: ~63,262 (44.91%); weighted (Census 2011) |
| └ Bagdi | 18.0 | D | Dominant SC community in delta; fishing/labouring caste |
| └ Namasudra | 10.0 | D | Present in both CDBs; lower share than in Bangaon belt |
| └ Halpati / Hari / Dom / other SC | 9.36 | E | Residual SC |
| **UC bhadralok** (Brahmin / Kayastha / Baidya) | 3.0 | E | Minimal presence in this rural delta AC |
| **OBC specific** (Mahishya / Sadgop / Teli / Kurmi) | 5.0 | E | Some Mahishya fishing-community presence |
| **Other Hindu middle castes** (Goala / Sutradhar / other unclassified) | 2.28 | E | Residual: 100 − 24.78 ST − 37.36 SC − 3.0 UC − 5.0 OBC − 27.15 Muslim − 0.43 non-Hindu non-Muslim = 2.28 |
| **Muslim** (all sub-castes pooled) | 27.15 | E | See C.1 |
| Christian + Sarna + Other | 0.43 | E | See C.1 residuals |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 0–4 | 7.5 | E | Projected from Census 2011 N24P age pyramid; under-6 share CDB-I 22,394/164,465 = 13.6%; similar CDB-II; adjusted for 5-yr cohort |
| 5–9 | 9.0 | E | |
| 10–14 | 8.5 | E | |
| 15–17 (pre-voter) | 5.0 | E | |
| 18–22 (first-time voters at 2019 LS) | 9.0 | E | |
| 23–27 | 9.5 | E | |
| 28–32 | 9.5 | E | |
| 33–37 | 8.5 | E | |
| 38–42 | 7.5 | E | |
| 43–47 | 7.0 | E | |
| 48–52 | 6.0 | E | |
| 53–57 | 5.0 | E | |
| 58–62 | 3.5 | E | |
| 63–67 | 2.5 | E | |
| 68+ | 2.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.96 | A/E | Sex ratio 962 (Census 2011 CDB-I 960, CDB-II 965; weighted); 1000/(1000+962) = 50.96% M; minimal projection drift to 2019 |
| Female | 49.03 | A/E | 962/(1000+962) = 49.03% F |
| Third gender | 0.01 | E | National pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 97.80 | A | CDB-I 2011: 97.64% Bengali (Census language data; A); CDB-II: ~99.64% Bengali (A); weighted AC ~98.5%; slight downward adjustment for tribal-language pockets |
| Sadri (Sadani / Sadri-Nagpuri) | 1.50 | A | CDB-I: 2.03% Sadri (Census 2011; A); spoken by Munda/Oraon communities; weighted down by CDB-II near-zero |
| Santali | 0.40 | E | Santhal community mother tongue; small fraction retains Santali — most code-switch to Bengali |
| Urdu | 0.20 | E | Small Muslim pocket; most WB rural Muslims speak Bengali |
| Other | 0.10 | E | Residual |
| **Sum** | **100.00** | — | self-check |

_(Bilingualism flag: ~4–5% of population is Bengali+Sadri or Bengali+Santali bilingual; tier E. Very few Bengali+Hindi bilinguals given no urban commercial hub in AC.)_

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 25.0 | E | CDB-I literacy 71.08% (2011; A), CDB-II 70.96% (A) → AC literacy ~71.02% in 2011; project +0.5pp/yr over 8yr → ~75.0% literate by 2019; illiterate ~25% |
| Primary (Class 1–5) | 25.0 | E | Rural delta pattern; Census 2011 WB education distribution scaled |
| Middle (Class 6–8) | 20.0 | E | |
| Secondary (Class 9–10) | 14.0 | E | |
| Higher Secondary (Class 11–12) | 9.0 | E | |
| Graduate | 5.5 | E | Low — limited tertiary infrastructure in delta blocks |
| Postgraduate | 1.5 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main worker | 28.0 | A/E | CDB-I main worker rate 40,131/164,465=24.4%; CDB-II: 34,118/160,976=21.2%; AC weighted ~22.8% of total pop; as % of 18+ (68.8% of pop) → ~33%; adjusted slightly for 2019 marginal expansion |
| Marginal worker | 14.0 | A/E | CDB-I marginal 20,874/164,465=12.7%; CDB-II marginal 27,631/160,976=17.2%; AC weighted ~14.8%; projected slightly down by 2019 as marginals convert to main |
| Non-worker (housewife / elderly / retired) | 42.0 | E | Includes high female housewife share typical of rural delta |
| Student (18–22, in education) | 10.0 | E | |
| Unemployed (educated, seeking) | 6.0 | E | Lower than urbanised ACs; educated youth migrate or remain underemployed in bheri/fishing economy |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 14.4 | A | CDB-I: 8,503/61,005=13.94% (A); CDB-II: 9,134/61,749=14.79% (A); weighted AC 14.37%; rounded |
| Agricultural labourer | 50.5 | A | CDB-I: 27,851/61,005=45.65% (A); CDB-II: 34,182/61,749=55.36% (A); weighted 50.49%; delta AC heavily ag-labourer dependent |
| Household industry | 3.5 | A | CDB-I: 2,392/61,005=3.92%; CDB-II: 1,863/61,749=3.02%; weighted 3.47% |
| Fishing / prawn / bheri (aquaculture) | 10.0 | D | Significant bheri (prawn pond) economy in Sandeshkhali; major livelihood not captured separately in Census classification (counted under 'Other worker'); D estimate from Dialogue Earth / Sundarbans Affairs data |
| Trade / retail (small) | 6.0 | E | Limited — no major commercial hub |
| Construction / building labour | 5.0 | E | Out-migration to construction sector in Kolkata / suburban areas |
| Transport | 3.0 | E | River/boat-based transport; limited road-based |
| Services (private / government) | 7.0 | E | Teachers, health workers, block-level staff |
| Other worker (unclassified) | 0.6 | E | Residual to 100 |
| **Sum** | **100.00** | — | self-check |

_Note: Census 'Other worker' category (CDB-I: 36.49% of workers; CDB-II: 25.81%) includes bheri workers, traders, construction, services — the sub-breakdown above maps these into simulation-relevant occupation strata using D/E estimates._

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.0 | E | Rare in subsistence delta economy |
| Employee (regular wage — govt + organised) | 12.0 | E | Teachers, health, block office; smaller share than urbanised ACs |
| Single worker (own-account — cultivator, fisherman, bheri operator) | 52.0 | E | Dominant mode; own-account farming, fishing, small bheri |
| Family worker (unpaid — within ag / fishing HH) | 35.0 | E | High family-labour intensity in fishing + ag labourer HHs |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL household | 32.0 | D | North 24 Parganas Basirhat sub-division rural BPL estimated ~38% (2001); WB poverty headcount fell ~6pp over 2011-19 in rural areas → ~32%; higher than state average due to delta geography and low asset base |
| Above-Poverty-Line, low-income | 35.0 | E | |
| Lower-middle | 22.0 | E | |
| Middle | 9.0 | E | |
| Upper-middle / well-off | 2.0 | E | Very limited non-farming affluence in AC |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Municipality location (2019)

_No municipality in AC 123. AC is entirely rural, split across two CD Blocks._

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **U1: CDB Sandeshkhali-I** (all 8 GPs) | 53.9 | E | 2011: CDB-I 164,465 / AC-total 305,319 = 53.87%; held stable to 2019 |
| **U2: CDB Sandeshkhali-II AC-share** (7 of 8 GPs; excl. Khulna) | 46.1 | E | 2011: 140,854 / 305,319 = 46.13%; v0 collapses 7 GPs into one sub-unit |
| **Sum** | **100.00** | — | self-check |

_v0 sub-unit decomposition: 15 GPs collapsed into 2 CDB-level sub-units. Spatial refinement available when DCHB N24P Part-A accessible._

_Key GP names for record: CDB-I GPs: Bayermari I, Bayermari II, Kalinagar, Sarberia Agarhati, Nazat I, Nazat II, Sehera Radhanagar, Hatgachhi. CDB-II GPs in AC: Beramajur I, Beramajur II, Durgamandap, Jeliakhali, Korakati, Manipur, Sandeshkhali._

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg HH size | 4.1 persons | E | CDB-I: 164,465 pop / 37,344 families = 4.40; CDB-II: 160,976 / 37,771 = 4.26; weighted ~4.33; slight decline projected to 2019 |
| Nuclear HH | 72.0 | E | NFHS-4 WB rural pattern; delta poor HHs tend nuclear |
| Joint HH | 22.0 | E | |
| Extended / multi-generation | 6.0 | E | |
| **Sum** | **100.00** | — | self-check |

_(Household head: ~85% male-headed, ~15% female-headed; higher female-headed than state average due to male out-migration for fishing / construction labour; tier E from N24P pattern.)_

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never married | 26.0 | E | Census 2011 N24P rural pattern; first-time-voter cohort |
| Currently married | 65.0 | E | |
| Widowed | 8.0 | E | Slightly elevated vs state average; concentrated in 60+; sea/river fishing hazard, male mortality |
| Separated / divorced | 1.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 60.0 | C | NFHS-4 WB rural 60% (2015-16); delta geography limits grid power stability; lower than Bangaon belt; +2pp/yr → ~68% but offset by geography; conservative 60% |
| Radio | 8.0 | C | Higher than state average — radio more practical in flood-prone tidal areas with irregular electricity |
| Mobile phone (any) | 78.0 | C | NFHS-4 WB rural ~70%; +growth → ~78% by 2019; below state urban average |
| Smartphone with internet | 32.0 | C | NFHS-4 baseline + Jio rollout 2016-19; but lower penetration than mainland ACs due to connectivity and affordability constraints in delta |
| Computer | 4.0 | C | Very limited; Bangaon Muni analog was 12%; this is fully rural AC |
| Two-wheeler | 18.0 | C | Limited road infrastructure; boat transport common |
| Four-wheeler | 2.0 | E | Rare |
| Banking access (any) | 82.0 | B | PMJDY 2014- saturation; NFHS-4 WB baseline; slightly lower than mainland due to connectivity |
| **Note** | (these are independent ownership %s, not categorical — do not sum) | — | — |

### C.15 Household amenities (2019)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved drinking water source | 76.0 | C | NFHS-4 WB rural 84%; delta salinity and flooding reduces access; conservative 76% for Sundarbans fringe; Aila 2009 damaged water infrastructure — partial restoration by 2019 |
| Improved sanitation (latrine) | 55.0 | C | NFHS-4 WB rural 51%; +Swachh Bharat 2014-19 (+10pp rural in delta); tidal geography limits pucca latrine construction → lower than mainland |
| LPG / clean cooking fuel | 35.0 | C | NFHS-4 WB rural 24%; +Ujjwala 2016-19 (+10pp rural delta); lower than mainland due to access constraints |
| Wood / biomass fuel | 58.0 | C | Dominant fuel — mangrove wood / paddy straw; higher than state average |
| Other fuel (kerosene / dung / other) | 7.0 | C | |
| Electricity | 88.0 | B | Census 2011 + Saubhagya 2017-19; CDB-I 100% villages electrified per Sundarbans Affairs; but HH-level connection lower due to household connectivity gaps and tidal flooding risks |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native (born in Sandeshkhali / N24P or same village) | 78.0 | D | Estimate: delta population is historically settled; low in-migration; predominantly native Santhal/Bagdi/Muslim peasantry |
| WB other district (in-migrant) | 8.0 | D | Some Kolkata periphery linkages; returning migrants |
| Other Indian state | 1.0 | E | Very small — no commercial/industrial node to attract inter-state migrants |
| **Cyclone Aila displacement (2009) — internal displacement anchor** | — | D | Cyclone Aila (May 2009) severely affected both Sandeshkhali-I and II blocks; households displaced temporarily to embankments and relief camps; a fraction (~5–8% of HHs) migrated semi-permanently to Kolkata periphery; those who remained are counted as native |
| Bangladesh-origin (long-term Hindu/Muslim settlers) | 10.0 | D | Lower than Bangaon belt; some older Hindu SC/ST settlement traceable to pre-1971 migration; Muslim fishing community with Bangladesh tidal border ties |
| Outside India (other than Bangladesh) | 0.0 | E | Negligible |
| Out-migrant (registered here, working outside) | 3.0 | D | Male out-migration for construction / fishing labour in Kolkata / suburban WB; registered voters in AC |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Sadri | Santali | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu (non-ST) | 99.0 | 0.5 | 0.0 | 0.0 | 0.5 | E | Bengali-dominant Hindu peasantry in delta |
| Hindu (ST sub-group, ~34% of Hindu pop) | 85.0 | 7.0 | 6.0 | 0.0 | 2.0 | E | Santhal/Munda households: Bengali is primary, Sadri/Santali spoken at home |
| Muslim | 99.5 | 0.0 | 0.0 | 0.4 | 0.1 | E | WB rural Muslim overwhelmingly Bengali-speaking; tiny Urdu pocket |
| Christian | 90.0 | 5.0 | 0.0 | 0.0 | 5.0 | E | Small base; Bengali + tribal-language |
| Other (Sarna) | 60.0 | 15.0 | 20.0 | 0.0 | 5.0 | E | Sarna practitioners retain tribal languages more |
| **Marginal recovery — Bengali** | | | | | | | 0.7242×(0.66×0.99+0.34×0.85) + 0.2715×0.995 + 0.0043×0.93 ≈ 0.7242×0.941 + 0.2702 + 0.004 = 0.681+0.270+0.004 = **0.955** vs C.5 **97.8%** — slight gap absorbed by rounding in tribal-language estimation; within ±2pp |

### D.2 Religion × Caste (Hindu-internal sub-structure)

P(caste ‖ Hindu) — % within Hindu population (72.42%) only.

| Caste sub-group | % of Hindu | Tier | Source |
|---|---|---|---|
| **ST total** (Santhal / Munda / Oraon / Bhumij) | 34.2 | A/E | 24.78% of AC / 72.42% Hindu = 34.2% of Hindu population (A numerator, E denominator) |
| └ Santhal | 20.7 | D | Largest ST sub-group in Sundarbans fringe |
| └ Munda | 6.9 | D | |
| └ Oraon / Bhumij / Other ST | 6.6 | E | |
| **SC total** (Bagdi / Namasudra / other) | 51.6 | A/E | 37.36% of AC / 72.42% Hindu = 51.6% of Hindu pop |
| └ Bagdi | 24.9 | D | Dominant fishing SC in delta; ~48% of SC pool within AC |
| └ Namasudra | 13.8 | D | Present but lower density than Bangaon belt; ~27% of SC pool |
| └ Halpati / Hari / Dom / other SC | 12.9 | E | Residual |
| UC bhadralok (Brahmin / Kayastha / Baidya) | 4.1 | E | 3% of AC / 72.42% = 4.1% of Hindu |
| OBC specific (Mahishya / Teli / Sadgop) | 6.9 | E | 5% of AC / 72.42% = 6.9% of Hindu |
| Other Hindu middle castes | 3.2 | E | Residual within Hindu |
| **Sum** | **100.00** | — | self-check |

P(Muslim sub-caste ‖ Muslim):

| Muslim sub-group | % of Muslim | Tier | Source |
|---|---|---|---|
| Sheikh (Bengali Muslim peasantry / fishermen) | 85 | D | Dominant in North 24 Parganas delta Muslim community |
| Jolaha / Weaver OBC Muslim | 8 | D | Some presence in block-level data |
| Pathan / Sayyid | 3 | D | Minimal |
| Other Muslim sub-castes | 4 | D | |
| **Sum** | **100** | — | self-check |

### D.3 Religion × Migration / birthplace

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB-other-dist | Other-state | Bangladesh-origin | Out-migrant-registered | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 76 | 8 | 1 | 12 | 3 | D | Some Hindu SC/ST settler origin pre-1971; majority long-settled native |
| Muslim | 82 | 7 | 0 | 8 | 3 | D | Bengali Muslim fishing community with cross-border family ties; majority native |
| Christian + Other | 85 | 10 | 5 | 0 | 0 | E | Mixed |
| **Marginal recovery — native** | | | | | | | 0.7242×0.76 + 0.2715×0.82 + 0.0043×0.85 = 0.550 + 0.223 + 0.004 = **0.777** vs C.16 **78.0%** ✓ within ±0.3pp |

### D.4 Religion × Asset / media (TV, smartphone, banking)

P(owns asset ‖ religion) — % within each religion.

| Religion | TV | Smartphone-internet | Banking | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 62 | 33 | 83 | C | NFHS-4 WB religion gap; Hindu slight advantage in asset access |
| Muslim | 55 | 29 | 78 | C | WB Muslim-Hindu gap pattern; rural fishing economy |
| Christian / Other | 65 | 38 | 85 | E | Small base; slight uplift from Christian mission-school exposure |

### D.5 Caste × Education

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Sec | HS | Grad | PG | Tier |
|---|---|---|---|---|---|---|---|---|
| UC bhadralok | 8 | 12 | 15 | 18 | 18 | 20 | 9 | E |
| Bagdi (SC) | 28 | 27 | 20 | 12 | 7 | 5 | 1 | E |
| Namasudra (SC) | 22 | 26 | 22 | 15 | 9 | 5 | 1 | E |
| Other SC | 30 | 28 | 20 | 12 | 6 | 3 | 1 | E |
| **ST (Santhal / Munda / Oraon)** | **38** | **30** | **17** | **10** | **4** | **1** | **0** | E |
| OBC specific | 18 | 24 | 22 | 18 | 10 | 6 | 2 | E |
| Other Hindu middle | 22 | 26 | 22 | 17 | 8 | 4 | 1 | E |
| Muslim | 28 | 27 | 22 | 14 | 6 | 3 | 0 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share (%).

| Cohort | Male grad+ | Female grad+ | Tier | Source |
|---|---|---|---|---|
| 18–22 | 10 | 9 | E | Low — limited college access in delta; students commute to Basirhat town |
| 23–27 | 9 | 6 | E | |
| 28–32 | 7 | 4 | E | |
| 33–42 | 6 | 2 | E | Older female cohort very low — limited historical schooling |
| 43–57 | 5 | 1 | E | |
| 58+ | 4 | 1 | E | |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender).

| Age | Male married | Female married | Tier |
|---|---|---|---|
| 18–22 | 8 | 35 | E |
| 23–27 | 42 | 82 | E |
| 28–32 | 82 | 93 | E |
| 33–47 | 92 | 90 | E |
| 48–62 | 88 | 75 | E |
| 63+ | 72 | 30 | E (widows concentrate here) |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone-internet | TV | Tier | Source |
|---|---|---|---|---|
| Cultivator | 25 | 55 | C | Rural ag baseline; delta geography — lower than mainland |
| Ag labourer | 18 | 45 | C | Lowest income, poorest connectivity |
| Fisher / bheri worker | 22 | 50 | C | Seasonal, low income; similar to ag labourer |
| Household industry | 28 | 58 | C | |
| Construction | 38 | 65 | C | Workers often have smartphone for urban contacts |
| Trade / retail | 55 | 75 | C | |
| Transport (boat / road) | 40 | 65 | C | |
| Services (private) | 60 | 78 | C | |
| Govt services / teachers | 78 | 88 | C | Highest in AC |
| Out-migrant (registered, working outside) | 65 | 72 | D | Smartphone for remittance / family contact |

### D.9 Education × Workforce participation

P(unemployed-and-seeking ‖ education) and main-worker rate.

| Education | Unemployed-seeking | Main-worker rate | Tier |
|---|---|---|---|
| Illiterate | 1 | 40 | E |
| Primary | 3 | 42 | E |
| Middle | 5 | 38 | E |
| Secondary | 7 | 30 | E |
| Higher Secondary | 12 | 22 | E |
| Graduate | 20 | 20 | E (educated unemployment severe; bheri/fishing economy offers few graduate jobs) |
| Postgraduate | 15 | 28 | E |

### D.10 Asset / media × Bilingualism

P(bilingual Bengali+tribal-language ‖ media-access tier) — ST community bilingualism proxy.

| Media tier | Bengali+Sadri/Santali bilingual | Tier | Source |
|---|---|---|---|
| TV-only HH | 8 | E | Low tribal-language media content on TV |
| TV + smartphone HH | 10 | E | YouTube tribal content slightly increases bilingualism |
| Smartphone-only HH | 9 | E | |
| No-asset HH | 12 | E | Tribal HHs overrepresented in no-asset; retain language |
| **Population-wide bilingual rate** | ~5 | E | C.5 narrative anchor (Sadri 1.5% + Santali 0.4%) |

### D.11 GP × Religion (sub-AC spatial heterogeneity, v0 = 2 sub-units)

P(religion ‖ sub-unit location).

| Sub-unit | Hindu | Muslim | Other | Tier | Source |
|---|---|---|---|---|---|
| **U1: CDB Sandeshkhali-I** (53.9% pop) | 69.19 | 30.42 | 0.39 | A | Census 2011 CDB-I religion data |
| **U2: CDB Sandeshkhali-II AC-share** (46.1% pop) | 77.17 | 22.27 | 0.56 | A | Census 2011 CDB-II religion data |
| **Marginal recovery — Hindu** | | | | | 0.539×69.19 + 0.461×77.17 = 37.29 + 35.58 = **72.87** vs C.1 2011 base **72.87** ✓; 2019 proj ~72.42 within rounding |
| **Marginal recovery — Muslim** | | | | | 0.539×30.42 + 0.461×22.27 = 16.40 + 10.27 = **26.67** vs C.1 2011 base **26.66** ✓ |

### D.12 GP × Caste (within sub-unit, key categories)

P(caste ‖ sub-unit).

| Sub-unit | UC | SC (Bagdi+Namasudra+other) | ST | OBC+Other Hindu | Muslim | Tier |
|---|---|---|---|---|---|---|
| CDB-I | 2 | 30.9 | 25.95 | 10.35 | 30.42 | A/E |
| CDB-II AC-share | 4 | 44.91 | 23.42 | 4.84 | 22.27 | A/E |
| Source | E-estimated | Census 2011 SC% (A) | Census 2011 ST% (A) | E-residual | Census 2011 Muslim% (A) | |

### D.13 GP × Asset / media

| Sub-unit | TV | Smartphone-internet | Banking | Tier |
|---|---|---|---|---|
| CDB-I | 58 | 30 | 80 | C |
| CDB-II AC-share | 62 | 34 | 84 | C |
| Source | NFHS-4 WB rural adjusted for delta geography | NFHS-4/5 rural | PMJDY | |

_Note: Both sub-units are fully rural, so urban-rural gradient is minimal. CDB-II slightly higher assets per Sunda rbans Affairs connectivity data._

### D.14 GP × Amenities

| Sub-unit | LPG | Improved sanitation | Improved water | Electricity | Tier |
|---|---|---|---|---|---|
| CDB-I | 32 | 50 | 72 | 88 | C |
| CDB-II AC-share | 38 | 60 | 80 | 88 | C |
| Source | NFHS-4/5 rural + Ujjwala/Swachh Bharat rollout; Aila 2009 water-infra damage (pre-2019 partially restored) | | | | |

### D.15 Vote × Religion (2019 LS AC 123 segment, tier A vote target)

P(party ‖ religion) — calibrated to AC 123 segment result (52.46% AITC / 38.83% BJP from ECI 2019 CSV).

| Religion | BJP | AITC | CPI | INC | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 51.5 | 41.0 | 3.0 | 1.0 | 3.5 | C/E | Back-calculated to recover AC aggregate; CSDS-Lokniti 2019 WB regional anchors adjusted for ST-heavy AC |
| Muslim | 5.0 | 83.0 | 2.0 | 2.5 | 7.5 | C | CSDS WB pattern; TMC dominant Muslim vote in Basirhat; INC residual stronger here than Bangaon due to Quazi INC base |
| Other (ST / Sarna / Christian) | 20.0 | 55.0 | 5.0 | 5.0 | 15.0 | E | ST typically TMC-leaning but BJP made inroads 2019; 15% other captures SUCI etc. |

**Recovery check:** AITC = 0.7242×0.41 + 0.2715×0.83 + 0.0043×0.55 = 0.297 + 0.225 + 0.002 = **52.4%** ✓ (target 52.46%); BJP = 0.7242×0.515 + 0.2715×0.05 + 0.0043×0.20 = 0.373 + 0.014 + 0.001 = **38.8%** ✓ (target 38.83%)

### D.16 Vote × Caste (2019 LS, AC 123 segment)

P(party ‖ caste) — within-Hindu differentiation; Muslim as single block.

| Caste | BJP | AITC | CPI | INC | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC bhadralok | 55 | 30 | 5 | 5 | 5 | C | WB 2019 UC BJP-leaning |
| OBC (Mahishya / Teli) | 42 | 38 | 8 | 5 | 7 | C | Mixed |
| Bagdi (SC) | 50 | 38 | 6 | 3 | 3 | C/E | SC BJP inroads 2019 but TMC welfare-base |
| Namasudra (SC) | 48 | 40 | 6 | 3 | 3 | E | |
| Other SC | 52 | 36 | 6 | 3 | 3 | E | |
| **ST (Santhal / Munda / Oraon)** | **35** | **52** | **5** | **5** | **3** | **C/E** | **TMC stronger with ST welfare in delta; BJP lower than state-wide SC average in ST-reservation AC** |
| Muslim (any caste) | 5 | 83 | 2 | 2.5 | 7.5 | C | See D.15 |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

P(party ‖ gender). Note: Lakshmir Bhandar does NOT exist in 2019.

| Gender | BJP | AITC | CPI | INC | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 43 | 48 | 3 | 2 | 4 | C | Swarajya/CSDS 2019 WB; male BJP share higher in state |
| Female | 35 | 57 | 2 | 1 | 5 | C | Female TMC advantage in 2019; welfare-scheme recipients disproportionately female |

### D.18 Vote × Welfare-scheme exposure (2019)

P(party ‖ household has scheme exposure). Schemes available by 2019: Krishak Bandhu (TMC, Jan 2019), Kanyashree (TMC, 2013), Swasthya Sathi (TMC, 2016), Sabuj Sathi (TMC, 2015), Khadya Sathi (TMC, 2016). **Lakshmir Bhandar does NOT exist in 2019.** Bhumi-Prapta (land pattas to ST/SC) relevant for ST community.

| Exposure | BJP | AITC | CPI | INC | Tier | Source |
|---|---|---|---|---|---|---|
| Krishak Bandhu (cultivator HH) | 30 | 58 | 5 | 5 | C | TMC welfare credit; bheri/farming HHs enrolled |
| Kanyashree (girl-student HH) | 28 | 60 | 5 | 5 | C | Significant uptake in delta blocks |
| Swasthya Sathi enrollee | 35 | 52 | 5 | 5 | C | Broad-based; weaker TMC tilt |
| Sabuj Sathi (bicycle HH) | 32 | 55 | 5 | 6 | C | |
| Khadya Sathi (PDS) | 40 | 48 | 5 | 5 | C | Near-universal coverage; weakest tilt |
| Bhumi-Prapta / ST patta (ST HH) | 22 | 62 | 5 | 8 | D | Land patta scheme targeted at ST community; strong TMC credit among ST beneficiaries |
| **No state-scheme exposure** | 58 | 28 | 6 | 5 | C | BJP-leaning |

---

## E. 2019 baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp.

### Whole Basirhat LS (PC 18) — 2019 result (tier A, ECI)

| Party | Candidate | Votes | % |
|---|---|---|---|
| AITC | **Nusrat Jahan Ruhi** | 781,920 | **54.93** |
| BJP | Sayantan Basu | 431,105 | **30.29** |
| INC | Quazi Abdur Rahim | 104,137 | **7.32** |
| CPI | Pallab Sengupta | 68,278 | **4.80** |
| Others / IND | various | 38,934 | **2.66** |
| **Total valid votes** | | **1,424,374** | |
| **Margin** | AITC over BJP | **350,815** | 24.64 pp |

_Source: ECI 2019 LS voter data CSV (processed from 2019_AssemblySegmentLevelVotingData.csv); tier A._

### AC 123 segment — 2019 LS result (tier A, ECI form-20 equivalent from CSV)

| Party | Candidate | Votes | % |
|---|---|---|---|
| AITC | Nusrat Jahan Ruhi | 103,600 | **52.46** |
| BJP | Sayantan Basu | 76,688 | **38.83** |
| CPI | Pallab Sengupta | 5,545 | **2.81** |
| INC | Quazi Abdur Rahim | 2,822 | **1.43** |
| Others (SUCI+BSP+IND+NOTA) | various | 8,831 | **4.47** |
| **Total valid votes** | | **197,486** | |
| **Electors** | | **229,369** | |
| **Turnout** | | | **86.10%** |
| **Margin** | AITC over BJP | **26,912** | 13.63 pp |

_Source: ECI 2019 LS voter-data CSV, AC 123 rows filtered directly; tier A. This is the calibration target._

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 123 Sandeshkhali specifically (Assembly Elections)

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin |
|---|---|---|---|---|---|---|---|---|---|
| 2016 AE | Sukumar Mahata | AITC | 96,566 | 51.49 | Nirapada Sardar | CPI(M) | 58,366 | 31.13 | ~38,200 |
| 2011 AE | Nirapada Sardar | CPI(M) | 66,815 | 43.21 | Padma Mahato | AITC | 62,583 | 40.47 | ~4,232 |
| 2006 AE | Abani Roy | CPI(M) | — | — | Gita Mondal | AITC | — | — | CPI(M) retained |
| 2001 and earlier | CPI(M) dominant under Kanti Biswas / Kumud Ranjan Biswas | CPI(M) | — | — | — | — | — | — | Left Front stronghold 1977–2011 |

_Sources: Wikipedia "Sandeshkhali Assembly constituency"; tier A for 2011 and 2016._

_Note on 2016 seat change: TMC won Sandeshkhali in 2016 (Sukumar Mahata unseated long-term CPI(M) MLA Nirapada Sardar) in the broader anti-Left wave. TMC held it against BJP in 2019 LS with AITC dominant in this AC._

### Basirhat Lok Sabha (PC 18) historical

| Year | Winner | Party | Votes | % | Runner-up | Party | % | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2014 LS | Idris Ali | AITC | 492,326 | 38.65 | Nurul Sekh | CPI | 382,667 | 30.04 | TMC won; BJP 18.36% (Samik Bhattacharya); AITC margin ~109,659 |
| 2009 LS | Idris Ali | AITC | — | — | CPI | — | — | TMC won; Cyclone Aila year |
| 2004 LS and earlier | Predominantly Left (CPI / CPI(M)) | Left | — | — | — | — | — | Basirhat was a Left stronghold for most of 1977-2009 |

_Note on 2014: Basirhat LS had a high INC vote (~7-8% via left-liberal bloc tied to minority-community politics in some segments). AC 123's Muslim-heavy profile (CDB-I 30% Muslim) made the INC base non-trivial in 2014._

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Sandeshkhali I CD Block Primary Census Abstract (religion, SC/ST, literacy, occupation, language, sex ratio) via Wikipedia "Sandeshkhali I" and Department of Sundarbans Affairs WB
- Census of India 2011 — Sandeshkhali II CD Block Primary Census Abstract via Wikipedia "Sandeshkhali II" and Department of Sundarbans Affairs WB
- Election Commission of India — 2019 LS General Election, AC 123 segment vote data (direct CSV: 2019_AssemblySegmentLevelVotingData.csv, rows filtered for West Bengal, AC NO=123)
- Election Commission of India — 2019 LS Basirhat constituency total result (same CSV, PC NAME=Basirhat aggregation)
- Election Commission of India — 2011 AE and 2016 AE results for AC 123 (via Wikipedia "Sandeshkhali Assembly constituency"; tier A)
- Delimitation Commission of India 2008 — WB Schedule (AC 123 = CDB Sandeshkhali-I + 7 GPs of CDB Sandeshkhali-II)

### Secondary sources (tier B/C)

- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership, cooking fuel baseline
- Department of Sundarbans Affairs, Government of West Bengal — block-level demographic tables (population, religion, SC/ST, literacy, sex ratio) for Sandeshkhali-I and Sandeshkhali-II
- CSDS-Lokniti 2019 NES post-poll (national rollup); Swarajya Magazine summary of CSDS 2019 WB regional cross-tabs (vote × religion / caste / gender)
- Pew Research India 2021 — religion-differential growth projections used for 2011→2019 projection
- WB District Statistical Handbook — N24P (BPL baseline, occupation distribution patterns)
- Dialogue Earth / ICSF (2024) — "Sandeshkhali and the exploitative aquaculture of the Bengal Delta" — bheri economy scale, ecological context (pre-2019 data sections only)

### Tertiary / journalistic (tier D)

- Wikipedia "Sandeshkhali Assembly constituency" — election history, composition
- Wikipedia "Basirhat Lok Sabha constituency" — 2014 LS result, LS composition
- UNDMT Cyclone Aila situation reports (May 2009) — displacement and agriculture impact in Sandeshkhali-I and II blocks
- Organiser.org / Sundarbans demography summaries — ST community identity (Santhal/Munda/Oraon) in Sundarbans fringe (pre-2019 sections only)
- Springer/Sage tribal migrant labour in Sundarbans — ST occupation patterns

### Tier-D/E reliance flags (what to distrust)

- **Caste sub-group shares within ST and SC** (D.2) — no caste census post-1931 for non-SC/ST; named sub-groups (Santhal, Munda, Bagdi, Namasudra) are D-level estimates from journalistic/academic anchors
- **Bheri / fishing occupation sub-share** (C.8) — Census doesn't separate fisheries from 'Other worker'; D estimate from Sundarbans Affairs data
- **GP-level data** (D.11–D.14) — collapsed to 2 sub-units (CDB-I + CDB-II-AC-share); spatial heterogeneity within CDB suppressed; refine when DCHB N24P Part-A accessible
- **Migration / birthplace** (C.16, D.3) — no AC-level Census D-series; D estimate; Aila displacement anchor is qualitative
- **Asset / media** (C.14, D.4, D.13) — NFHS-4/5 state-level pattern projected to AC with delta-geography discount; tier C
- **Vote × Demographic** (D.15–D.18) — CSDS 2019 WB regional rollup adjusted for AC-specific caste/religion profile; tier C
- **Khulna GP share in CDB-II** — assumed 1/8 of CDB-II population; no sub-GP census breakdown available

### v0 known gaps (cross-reference methodology §7)

1. DCHB N24P Part-A — collapsed 15 GPs to 2 CDB sub-units; refine when accessible
2. Census HH-13 block-level — using NFHS state-level proxy for asset/media; refine with Census HH-13 when accessible
3. GP-equal-weight assumption for Khulna exclusion — Khulna GP share in CDB-II assumed 1/8; actual population unknown
4. Occupation bheri/fishing sub-split — Census 'Other worker' category doesn't separate pisciculture; D-level estimate
5. Full CSDS WB regional cross-tabs — using state-summary numbers; could refine with full Lokniti WB report
6. ECI Form-20 AC segment for 2016 and earlier AEs — Wikipedia vote totals used (tier A via ECI indirect); 2019 LS segment is tier A from CSV
7. Sarna religion count — census-classified as 'Other' (tiny 0.18-0.39%); actual Sarna-practising fraction of ST community higher but captured under Hindu; imprecise for agent-level religious behaviour modelling

---

## H. Post-2019 validation anchors (OUT-OF-SAMPLE — do NOT use in calibration)

_These results are listed here for simulator validation only. They were unknown at end-2019 and must not inform Sections A–G._

### 2021 WB Assembly Election — AC 123 Sandeshkhali (tier A)

| Party | Candidate | Votes | % |
|---|---|---|---|
| AITC | Sukumar Mahata | 112,450 | 54.64 |
| BJP | Bhaskar Sardar | 72,765 | 35.36 |
| Others | various | ~20,605 | ~10.00 |
| **Margin** | AITC over BJP | **39,685** | 19.28 pp |

_Source: Wikipedia "Sandeshkhali Assembly constituency"; tier A._

### 2024 LS — AC 123 segment (tier A, ECI CSV)

| Party | Candidate | Votes | % |
|---|---|---|---|
| BJP | Rekha Patra | 95,862 | 47.46 |
| AITC | Sk Nurul Islam | 87,475 | 43.31 |
| AISF | Akhtar Rahaman Biswas | 7,566 | 3.75 |
| CPI(M) | Nirapada Sardar | 3,825 | 1.89 |
| Others / NOTA | various | 7,238 | 3.58 |
| **Total valid votes** | | **201,966** | |
| **Electors** | | **245,817** | |
| **Turnout** | | | **82.16%** |
| **Margin** | BJP over AITC | **8,387** | 4.15 pp |

_Source: ECI 2024 LS voter data CSV, AC 123 rows filtered; tier A._

### 2024 LS — Whole Basirhat LS (PC 18) (tier A)

| Party | Votes | % |
|---|---|---|
| AITC (Haji Nurul Islam) | 801,542 | 52.95 |
| BJP (Rekha Patra) | 468,593 | 30.95 |
| AISF | 123,432 | 8.15 |
| CPI(M) | 77,611 | 5.13 |
| Others / IND | 42,721 | 2.82 |
| **Margin** | AITC over BJP | **332,949** | 22.0 pp |

_Source: ECI 2024 LS voter data CSV; tier A._

### Critical validation signal

The Sandeshkhali violence episode (January–February 2024) and Rekha Patra's BJP candidacy generated significant national media coverage. Yet at the AC 123 segment level in the 2024 LS result, TMC retained 43.31% vs BJP's 47.46% — a swing of only ~9pp from 2019 toward BJP in the AC segment (from 38.83% BJP in 2019 to 47.46% in 2024), while at the whole-Basirhat LS level TMC maintained a 23pp margin. **This is a critical signal: national narrative shocks, even those with a strong local origin in the precise AC under study, do not automatically translate to proportional local AC vote shifts — the Basirhat LS-level TMC dominance was virtually unchanged from 2019 to 2024.**

---

*v0 — generated 2026-04-27, frozen at 2019 state-of-knowledge. No post-2019 events referenced in Sections A–G.*
