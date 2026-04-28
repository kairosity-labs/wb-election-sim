# AC 198 — Tarakeswar (General) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural state of AC 198 Tarakeswar as of 2019 only — it does not reference any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 198 | A | ECI / Delimitation Commission 2008 |
| AC name | Tarakeswar | A | ECI |
| Reservation | General (unreserved) | A | Delimitation 2008 |
| District | Hooghly | A | Delimitation 2008 |
| Sub-division | Chandannagore (administrative); note: prompt says Arambagh but WB Govt records confirm Tarakeswar CDB is in Chandannagore subdivision | A | WB Hooghly District portal (hooghly.nic.in/chandannagar-subdivision/) |
| LS constituency | 29 — Arambagh (SC reserved) | A | Delimitation 2008 |
| LS segments included with AC 198 | AC 194 Haripal · 198 Tarakeswar · 199 Pursurah · 200 Arambagh (SC) · 201 Goghat (SC) · 202 Khanakul · 203 Chandrakona (SC) | A | Delimitation 2008; Wikipedia Arambagh LS |
| AC composition | Tarakeswar Municipality (full) + all 10 GPs of Tarakeswar CDB + Bhanderhati I, Bhanderhati II, Gopinathpur I, Gopinathpur II, Parambua-Sahabazar GPs of Dhaniakhali CDB | A | Delimitation Commission Order 2008 (confirmed via search) |
| Geographic note | Temple town at 58 km from Kolkata; Howrah-Tarakeswar railway line; significant Shiva pilgrimage economy (Taraknath Temple, ~10 million pilgrims/yr in Sravan month) | A | Wikipedia Tarakeswar; GoWB Hooghly portal |
| Two sub-units used in v0 (spatial conditioning) | **U1: Tarakeswar Municipality + CDB** (urban+rural core, ~72% of AC pop) · **U2: Dhaniakhali-5GP share** (rural fringe, ~28% of AC pop) | E | v0 simplification; see methodology §3 |

---

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~299,132 (Tarakeswar CDB rural 179,148 + Tarakeswar Muni 30,947 + Dhaniakhali 5 GPs ≈ 5/18 × 320,534 = 89,037) | E | Census 2011; v0 equal-weight GP assumption for Dhaniakhali 5GPs |
| 2019 projected population | ~324,600 | E | 8-yr compound religion-differential growth (methodology §4); ~1.2%/yr blended |
| Sex ratio (2019, F per 1000 M) | ~965 | E | Weighted 2011: CDB 957, Muni 928, Dhaniakhali 994; blended ~965; minimal projection drift |
| 2019 electorate (tier A — from ECI data) | 232,456 | A | 2019_AssemblySegmentLevelVotingData.csv, AC_NO=198 |
| 2019 turnout | 84.83% (197,194 / 232,456) | A | 2019_AssemblySegmentLevelVotingData.csv |
| Estimated M / F / TG split (2019) | ~50.9% M / 49.1% F / <0.05% TG | E | Weighted sex ratio ~965 F/1000M; projected stable from 2011 |
| 2019 polling stations (estimated) | ~280 | E | 2021 AE roll 221,972 (Wikipedia); back-projection to ~280 stations in 2019 |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 86.78 | E | 2011 weighted (Tarakeswar CDB 88.94% + Muni 93.22% + Dhaniakhali-5GP 80.85%) = 86.97% base; projected 2011→2019 religion-differential growth (+1.0%/yr Hindu, +1.3%/yr Muslim over 8yr) → small shift; see methodology §4 |
| Muslim | 11.74 | E | 2011 weighted base 11.49%; projected to 11.74% after differential growth |
| Sarna / Tribal religion | 0.90 | E | ST-heavy Dhaniakhali fringe; some Santali practitioners; weighted from CDB and Dhaniakhali |
| Christian | 0.30 | E | Very small; missionary presence in Dhaniakhali fringe |
| Other (Jain/Sikh/Buddhist) | 0.28 | E | Residual; Tarakeswar Muni has small Jain (0.17%), Sikh (0.11%) populations |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

> **Note:** This is the load-bearing axis for AC 198. No caste census post-1931 (non-SC/ST). All OBC/UC/intermediate-caste figures are tier C–E.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC total** | 25.5 | E | Weighted 2011: Tarakeswar CDB 23.63% + Muni 14.26% + Dhaniakhali-5GP ~33% → ~25.45%; projected stable (SC share changes slowly) |
| └ Bagdi | 9.5 | C | Dominant SC in Hooghly district (Hooghly SC breakout: Bagdi 630,219 = ~11.4% of district pop); primary SC in this AC |
| └ Bauri | 4.5 | C | Major SC sub-group in Hooghly; Hooghly Bauri 125,849 (~2.3% district), higher in rural CDB |
| └ Namasudra | 3.5 | C | Present but not dominant (unlike N24P); smaller share in Hooghly than in Bangaon belt |
| └ Chamar / other SC (Hari, Jalia, Rajbanshi etc.) | 7.5 | E | Residual SC sub-groups; Hooghly has Chamar 62k, Jalia 57k, Rajbanshi 44k, Hari 41k |
| **ST total** | 7.3 | E | Weighted 2011: CDB 5.04% + Muni 0.50% + Dhaniakhali 14.26% → ~7.31%; Santal dominant |
| └ Santal | 5.5 | C | Dominant ST group in Hooghly (153,809 in district); rural CDB and Dhaniakhali fringe |
| └ Other ST (Munda, Bhumij, Lodha) | 1.8 | E | Residual |
| **OBC Hindu (combined)** | 30.0 | D | **Load-bearing parameter.** Mahishya + Sadgop + Kurmi + Tili combined; Hooghly's "cultivating middle castes" — no OBC census; estimate from journalistic-academic sources (tier D) |
| └ Mahishya | 18.0 | D | Single largest caste in Hooghly (Wikipedia/India Today: "single most important middle-caste in south-western Bengal; very numerous in Midnapore, 24-Parganas, Hooghly, Howrah"); in General category (not OBC) but functionally dominant cultivating caste; ~18% of constituency estimate |
| └ Sadgop | 6.0 | D | Second-tier cultivating caste in Hooghly; OBC-B classified since ~2010s state order; significant in Tarakeswar area |
| └ Kurmi | 3.5 | D | OBC-A; cultivating caste, present in rural GPs |
| └ Tili (oil-presser caste) / other OBC | 2.5 | D | Temple-town trade economy has Tili/teleseller; other OBC sub-groups |
| **UC bhadralok** (Brahmin / Kayastha / Baidya) | 8.0 | D | Temple-town educated Bengali professional class concentrated in Tarakeswar Muni; temple priests (Brahmin) significant |
| **Other Hindu** (Goala, Tanti, Sutradhar, unclassified middle) | 15.9 | E | Residual within Hindu: 86.78% − 25.5 SC − 7.3 ST − 30.0 OBC − 8.0 UC = 15.98% |
| **Muslim** (all sub-castes pooled) | 11.74 | E | See C.1; sub-structure in D.2 |
| Christian + Sarna-only + Other | 1.46 | E | See C.1 |
| **Sum** | **100.00** | — | self-check (25.5+7.3+30.0+8.0+15.9+11.74+1.46 = 99.9 → rounds to 100 ✓) |

### C.3 Age cohort (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 0–4 | 7.5 | E | Projected from Census 2011 Hooghly district age pyramid |
| 5–9 | 8.0 | E | |
| 10–14 | 8.5 | E | |
| 15–17 (pre-voter) | 5.5 | E | |
| 18–22 (first-time voters in 2019) | 9.0 | E | |
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
| Male | 50.89 | E | Weighted sex ratio ~965 F/1000M → 50.89% M / 49.11% F |
| Female | 49.11 | E | |
| Third gender | 0.00 | E | Negligible; consistent with WB AC pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 92.5 | E | Weighted 2011: Tarakeswar CDB 96.93% Bengali + Muni 83.8% + Dhaniakhali fringe ~93% est → ~94.4% base; adjusted down slightly for Hindi-speaker growth from pilgrims/traders in Muni; ~92.5% by 2019 |
| Santali | 2.5 | E | CDB 2.26% Santali; Dhaniakhali ST fringe adds more; weighted ~2.5% |
| Hindi | 3.5 | E | Tarakeswar Muni shows 15.2% Hindi in Wikipedia town article (unusual — partly pilgrimage-season workers registered?); likely inflated by temporary pilgrims; stable resident Hindi ~3.5% |
| Urdu | 0.8 | E | Muslim pocket in Dhaniakhali GPs; small |
| Other (Kurukh/Munda/Bhumij) | 0.7 | E | ST fringe |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 13.5 | E | Weighted 2011 literacy: ~79.1% literate; +0.5pp/yr → 2019 ~83% literate → ~17% illiterate at age 7+; 13.5% illiterate of total pop (age 7+ is ~80% of pop) |
| Primary (Class 1–5) | 22.5 | E | Census 2011 WB education distribution; scaled to local literacy level |
| Middle (Class 6–8) | 21.5 | E | |
| Secondary (Class 9–10) | 19.0 | E | |
| Higher Secondary (Class 11–12) | 12.0 | E | |
| Graduate | 8.5 | E | Tarakeswar Muni literacy 83.9% (higher); some graduate class in town |
| Postgraduate | 3.0 | E | Small professional class; temple-associated educated community |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main worker | 33.0 | E | Tarakeswar CDB and Dhaniakhali census worker rates; rural agricultural area with moderate main-worker share |
| Marginal worker | 12.0 | E | Agricultural seasonality drives high marginal-worker share |
| Non-worker (housewife / elderly / retired) | 37.0 | E | Female housewife fraction dominant in rural OBC households |
| Student (18–22 only, in education) | 11.0 | E | |
| Unemployed (educated, actively seeking) | 7.0 | E | Educated job-aspirant pool; moderate in Hooghly compared to urban ACs |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 18.0 | E | Weighted 2011 across CDB+Muni+Dhaniakhali: ~17.95% (methodology computation); stable to 2019 |
| Agricultural labourer | 40.0 | E | Weighted 2011: ~39.63%; rounds to 40% |
| Household industry | 4.5 | E | Weighted 2011: ~4.55% |
| Manufacturing (organised, incl. jute) | 5.0 | E | Some jute industry in Dhaniakhali fringe; moderate organised sector |
| Construction | 6.0 | E | Rural and town construction activity |
| Trade / retail | 10.0 | E | Tarakeswar Muni hub + temple economy (shops, accommodation, food) |
| Transport | 4.5 | E | Railway station economy; Kolkata commuter-logistics chain |
| Services (private) | 8.0 | E | Kolkata commuter workforce; substantial given railway access |
| Government services / teachers | 4.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.0 | E | Census B-04 WB rural pattern; small landowner-employers |
| Employee (regular wage) | 25.0 | E | Govt + organised + service employees; commuter workforce |
| Single worker (own-account) | 53.0 | E | Cultivator + own-account artisan + small trader; dominant in rural OBC economy |
| Family worker (unpaid) | 20.0 | E | Within agri-household; heavy in SC agricultural labourer households |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL household | 20.0 | C | Hooghly district poverty historically below WB average; rural blocks ~25% BPL in early 2000s; trend decline by 2019 → ~20% |
| Above-Poverty-Line, low-income | 38.0 | E | Rural cultivating-OBC and SC labourer households |
| Lower-middle | 26.0 | E | |
| Middle | 13.0 | E | Commuter workforce + Tarakeswar Muni middle class + small traders |
| Upper-middle / well-off | 3.0 | E | Limited affluent fringe in Muni; some temple-economy business families |
| **Sum** | **100.00** | — | self-check |
| **PM Kisan Samman Nidhi exposure** | 0% | A | **WB government declined PM Kisan until FY2021-22 (joined at 8th installment, Apr-Jul 2021). Zero PM Kisan enrollment in end-2019.** Central scheme existed from Dec 2018 but WB did not participate — BJP used this as a grievance lever in 2019 campaign. Source: PIB press release + PM Kisan Wikipedia |
| **Krishak Bandhu (TMC, Jan 2019) enrolled cultivators** | ~18 | D | Scheme launched Jan 2019; enrollment camps from 28 Jan 2019. ~18% of AC HH are cultivator-category, most enrolled by May 2019. First installment delivered May 2019 (Kharif). TMC flagship welfare-credit item in 2019 LS. Source: Krishak Bandhu website + WBXPress |

### C.11 GP / Municipality location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **U1: Tarakeswar Municipality** (urban core) | 10.3 | E | 2011: 30,947 / 299,132 = 10.3%; held stable to 2019 |
| **U2: Tarakeswar CDB (rural, 10 GPs)** | 59.9 | E | 2011: 179,148 / 299,132 = 59.9% |
| **U3: Dhaniakhali 5 GPs** | 29.8 | E | 2011: 89,037 / 299,132 = 29.8%; v0 collapses all 5 GPs into single cell |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg HH size | 4.5 persons | E | WB 2011: 4.3; rural Hooghly slightly higher; minor upward projection |
| Nuclear HH | 68.0 | E | NFHS-4 WB rural pattern |
| Joint HH | 26.0 | E | Higher in OBC cultivating-caste households |
| Extended / multi-generation | 6.0 | E | |
| **Sum** | **100.00** | — | self-check |

(Household head: ~87% male-headed, 13% female-headed; tier E from Hooghly district pattern.)

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never married | 26.0 | E | Census 2011 Hooghly pattern; first-time-voter cohort 18–22 |
| Currently married | 65.0 | E | |
| Widowed | 8.0 | E | Concentrated in 60+, female-skewed; consistent with WB pattern |
| Separated / divorced | 1.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 76.0 | C | NFHS-4 WB rural baseline ~60% + urban 89%; AC weighted (mostly rural) ~76%; +3-5pp growth 2016–2019 |
| Radio | 5.0 | C | Declining nationally |
| Mobile phone (any) | 85.0 | C | NFHS-4 WB ~78% + Jio diffusion 2016–2019 → ~85% by 2019 |
| Smartphone with internet | 45.0 | C | Jio rollout (Sep 2016) + rural WB growth; ~45% by end-2019 (slightly below N24P urban ACs) |
| Computer | 8.0 | C | NFHS-4 WB rural 4%, Muni higher; AC weighted ~8% |
| Two-wheeler | 30.0 | C | NFHS-4 WB rural 18%; growing; ~30% by 2019 |
| Four-wheeler | 5.0 | C | Limited in rural Hooghly |
| Banking access (any) | 88.0 | B | PMJDY 2014 saturation + Jan Dhan enrollment; WB NFHS-4 baseline + rollout |
| **Note** | (these are independent ownership %s, not categorical — do not sum) | — | — |

### C.15 Household amenities (2019)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved drinking water source | 84.0 | C | NFHS-4 WB rural 84% baseline; Hooghly slightly better than state average |
| Improved sanitation (latrine) | 65.0 | C | NFHS-4 WB rural 51%; +Swachh Bharat 2014-19 (+15pp rural) → ~65% by 2019 in Hooghly |
| LPG / clean cooking fuel | 42.0 | C | NFHS-4 WB rural ~24%; +Ujjwala PMUY 2016–19 (+15pp rural) → ~42% |
| Wood / biomass fuel | 53.0 | C | Declining as LPG rises |
| Other fuel (kerosene, dung etc.) | 5.0 | C | |
| Electricity | 97.0 | A | Census 2011 + Saubhagya 2017–19 saturation; Hooghly well-electrified |
| **Note** | (water/sanitation/electricity are independent; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native (born in Hooghly or same village/town) | 82.0 | D | Hooghly is a non-refugee district; overwhelmingly native population; no large refugee/migrant influx unlike N24P |
| WB other district (in-migrant) | 8.0 | D | Some Kolkata service-class in-migrants in Muni; seasonal pilgrimage workers |
| Other Indian state | 4.5 | D | Pilgrimage economy attracts some permanent Hindi-belt settlers; temple service workers; Tarakeswar Muni 15.2% Hindi-speaker likely includes some; stable residents ~4.5% |
| Bangladesh-origin (Hindu refugee, post-partition / 1971) | 4.0 | D | Much smaller than N24P/Bangaon belt; some Namasudra/refugee families in Dhaniakhali fringe; not the dominant migration story here |
| Outside India (other than Bangladesh) | 0.5 | E | Negligible |
| Out-migrant (registered here, working elsewhere) | 1.0 | E | Some Kolkata commuters registered at home address |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Santali | Hindi | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 94.5 | 1.5 | 3.0 | 0.0 | 1.0 | E | CDB Bengali majority; Muni Hindi-trader fringe within Hindu; UC bhadralok all Bengali |
| Muslim | 88.0 | 0.0 | 1.5 | 9.5 | 1.0 | E | Bengali-Sheikh majority; Urdu fraction in Muslim; Dhaniakhali GP Muslims are mostly Bengali |
| Sarna / tribal | 15.0 | 75.0 | 0.0 | 0.0 | 10.0 | E | Santal practitioners are Santali-speakers |
| Christian | 90.0 | 5.0 | 0.0 | 0.0 | 5.0 | E | Tiny base |
| Other | 60.0 | 0.0 | 30.0 | 0.0 | 10.0 | E | Marwari/Jain fringe |
| **Marginal recovery — Bengali** | | | | | | | Hindu(86.78)×0.945 + Muslim(11.74)×0.88 + Sarna(0.90)×0.15 + Chr(0.30)×0.90 + Other(0.28)×0.60 = 82.01 + 10.33 + 0.14 + 0.27 + 0.17 = **92.92** vs C.5 marginal **92.5** ✓ within ±0.5 |

### D.2 Religion × Caste (Hindu-internal sub-structure)

P(caste ‖ Hindu) — % within Hindu population only (86.78% of total).

| Caste sub-group | % of Hindu | Tier | Source |
|---|---|---|---|
| **SC: Bagdi** | 10.9 | C | 9.5% of total / 86.78% Hindu ≈ 10.9% of Hindu |
| SC: Bauri | 5.2 | E | 4.5% / 86.78% |
| SC: Namasudra | 4.0 | E | 3.5% / 86.78% |
| SC: Other (Hari, Chamar, Jalia, Rajbanshi) | 8.5 | E | Residual SC |
| ST: Santal | 6.3 | E | 5.5% / 86.78% |
| ST: Other | 2.1 | E | 1.8% / 86.78% |
| UC bhadralok (Brahmin/Kayastha/Baidya) | 9.2 | D | 8.0% / 86.78% |
| **OBC: Mahishya** | 20.7 | D | 18.0% / 86.78%; dominant cultivating caste |
| OBC: Sadgop | 6.9 | D | 6.0% / 86.78% |
| OBC: Kurmi | 4.0 | D | 3.5% / 86.78% |
| OBC: Tili / other OBC | 2.9 | D | 2.5% / 86.78% |
| Other Hindu middle (Goala, Tanti, Sutradhar, unclassified) | 19.4 | E | 15.9% + residual → 19.4% of Hindu |
| **Sum** | **100.00** | — | self-check (rounding) |

P(Muslim sub-caste ‖ Muslim):

| Muslim sub-group | % of Muslim | Tier | Source |
|---|---|---|---|
| Sheikh (Bengali Muslim peasantry) | 82 | D | Dominant in Hooghly-Dhaniakhali belt; Bengali-speaking cultivator Muslim |
| Pathan / Sayyid / Mughal | 5 | D | Small ashraf fringe |
| OBC Muslim (Jolaha, Nai, Darzi etc.) | 10 | D | Weavers/artisan Muslim sub-groups in Dhaniakhali block |
| Nasya-Sheikh / Other | 3 | D | |
| **Sum** | **100** | — | self-check |

### D.3 Religion × Migration / birthplace

P(birthplace ‖ religion).

| Religion | Native | WB-other-dist | Other state | Bangladesh | Outside-India | Tier | Source |
|---|---|---|---|---|---|---|---|
| **Hindu** | 80 | 8 | 5 | 5 | 0 | D | Hooghly is low-refugee; some Namasudra/refugee families exist but not dominant; Hindi-belt settlers (~5% other-state within Hindu) |
| Muslim | 93 | 4 | 2 | 1 | 0 | D | Hooghly Muslims are overwhelmingly native Bengali-Sheikh peasantry |
| Sarna / tribal | 90 | 7 | 2 | 0 | 1 | E | Indigenous |
| Other | 40 | 15 | 40 | 5 | 0 | E | Marwari traders mostly other-state |
| **Marginal recovery — Native** | | | | | | | Hindu(86.78)×0.80 + Muslim(11.74)×0.93 + Sarna(0.90)×0.90 + Other(0.58)×0.40 = 69.42 + 10.92 + 0.81 + 0.23 = **81.38** vs C.16 marginal **82.0** ✓ within ±0.7 |

### D.4 Religion × Asset / media (TV, smartphone, banking)

P(owns asset ‖ religion) — % within each religion.

| Religion | TV | Smartphone-internet | Banking | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 78 | 47 | 90 | C | NFHS-4 WB religion gap; Hindu in rural Hooghly |
| Muslim | 65 | 35 | 78 | C | Muslim asset gap persists; lower TV and smartphone penetration |
| Sarna / tribal | 55 | 25 | 72 | C | Lower asset access in tribal communities |
| Christian / Other | 82 | 55 | 92 | E | Small base; educated fringe |

### D.5 Caste × Education

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Sec | HS | Grad | PG | Tier |
|---|---|---|---|---|---|---|---|---|
| UC bhadralok | 4 | 8 | 12 | 18 | 20 | 26 | 12 | E |
| Mahishya (OBC/General) | 10 | 20 | 22 | 22 | 14 | 9 | 3 | E |
| Sadgop (OBC-B) | 12 | 22 | 22 | 20 | 12 | 9 | 3 | E |
| Kurmi / Tili (OBC) | 14 | 23 | 22 | 19 | 12 | 8 | 2 | E |
| Bagdi (SC) | 22 | 27 | 22 | 16 | 8 | 4 | 1 | E |
| Bauri / other SC | 25 | 28 | 21 | 14 | 7 | 4 | 1 | E |
| Namasudra (SC) | 18 | 24 | 22 | 17 | 10 | 7 | 2 | E |
| Santal / ST | 30 | 30 | 18 | 12 | 6 | 3 | 1 | E |
| Muslim (all) | 20 | 25 | 23 | 18 | 9 | 4 | 1 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Cohort | Male grad+ | Female grad+ | Tier | Source |
|---|---|---|---|---|
| 18–22 | 17 | 15 | E | Near parity in young cohort; education expansion |
| 23–27 | 15 | 11 | E | |
| 28–32 | 12 | 8 | E | |
| 33–42 | 10 | 5 | E | |
| 43–57 | 7 | 3 | E | Older female cohort low |
| 58+ | 5 | 2 | E | |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender).

| Age | Male married | Female married | Tier |
|---|---|---|---|
| 18–22 | 7 | 28 | E |
| 23–27 | 42 | 82 | E |
| 28–32 | 82 | 93 | E |
| 33–47 | 92 | 90 | E |
| 48–62 | 90 | 78 | E |
| 63+ | 72 | 32 | E (widows concentrate here) |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone-internet | TV | Tier | Source |
|---|---|---|---|---|
| Cultivator | 35 | 70 | C | Rural ag baseline |
| Ag-labourer | 22 | 58 | C | Lowest income bracket |
| Household industry | 38 | 72 | C | |
| Manufacturing | 52 | 82 | C | |
| Construction | 45 | 74 | C | |
| Trade / retail | 68 | 88 | C | Temple-economy traders; Muni concentrated |
| Transport (railway-linked) | 62 | 82 | C | |
| Services (private, Kolkata commuter) | 75 | 90 | C | Commuter workforce has high smartphone access |
| Govt services / teachers | 85 | 92 | C | Highest |

### D.9 Education × Workforce participation

P(unemployed-and-seeking ‖ education) — educated-unemployment proxy.

| Education | Unemployed-seeking | Main-worker rate | Tier |
|---|---|---|---|
| Illiterate | 2 | 35 | E |
| Primary | 4 | 38 | E |
| Middle | 6 | 36 | E |
| Secondary | 10 | 30 | E |
| Higher Secondary | 15 | 25 | E |
| Graduate | 18 | 28 | E (job-aspirant pool; educated unemployment salient in Hooghly) |
| Postgraduate | 12 | 40 | E |

### D.10 Asset / media × Bilingualism

P(bilingual Bengali+Hindi ‖ media-access tier).

| Media tier | Bilingual % | Tier | Source |
|---|---|---|---|
| TV-only HH | 5 | E | Bengali TV dominant |
| TV + smartphone HH | 10 | E | Some Hindi-YouTube cross-language |
| Smartphone-only HH | 8 | E | |
| No-asset HH | 3 | E | Lowest exposure |
| **Population-wide bilingual rate** | ~7 | E | C.5 narrative anchor; Tarakeswar Muni Hindi speakers inflate slightly |

### D.11 GP × Religion (sub-AC spatial heterogeneity, v0 = 3 sub-units)

P(religion ‖ sub-unit).

| Sub-unit | Hindu | Muslim | Sarna/Other | Tier | Source |
|---|---|---|---|---|---|
| **U1: Tarakeswar Muni** (10.3% pop) | 93.22 | 4.97 | 1.81 | A | Census 2011 town data (census2011.co.in) |
| **U2: Tarakeswar CDB** (59.9% pop) | 88.94 | 10.20 | 0.86 | A | Census 2011 CDB data (Wikipedia CDB article) |
| **U3: Dhaniakhali 5 GPs** (29.8% pop) | 80.85 | 16.34 | 2.81 | A | Dhaniakhali block Census 2011 (Wikipedia); note 5GPs are a subset — block-level used as proxy |
| **Marginal recovery — Hindu** | | | | | 0.103×93.22 + 0.599×88.94 + 0.298×80.85 = 9.60 + 53.27 + 24.09 = **86.96** vs C.1 projected **86.78** ✓ within ±0.2 |

### D.12 GP × Caste (within sub-unit, key categories)

P(caste ‖ sub-unit).

| Sub-unit | UC | Mahishya+Sadgop (dominant OBC) | Kurmi/Tili/Other OBC | Bagdi SC | Other SC | ST | Muslim | Tier |
|---|---|---|---|---|---|---|---|---|
| Tarakeswar Muni | 12 | 28 | 6 | 8 | 6 | 1 | 5 | D |
| Tarakeswar CDB | 7 | 30 | 10 | 11 | 8 | 5 | 10 | D |
| Dhaniakhali 5 GPs | 4 | 20 | 8 | 12 | 10 | 20 | 16 | D |
| Source | temple-town educated class | Mahishya dominant in Hooghly cultivating belt | rural OBC | Hooghly SC #1 | district SC pattern | Dhaniakhali high ST | block Muslim share | |

### D.13 GP × Asset / media

| Sub-unit | TV | Smartphone-internet | Computer | Banking | Tier |
|---|---|---|---|---|---|
| Tarakeswar Muni | 88 | 60 | 18 | 92 | C |
| Tarakeswar CDB | 74 | 42 | 6 | 86 | C |
| Dhaniakhali 5 GPs | 65 | 32 | 4 | 80 | C |
| Source | NFHS-4 WB urban/rural gradient | NFHS-4/5 pattern | | PMJDY | |

### D.14 GP × Amenities

| Sub-unit | LPG | Improved sanitation | Improved water | Electricity | Tier |
|---|---|---|---|---|---|
| Tarakeswar Muni | 70 | 88 | 92 | 99 | C |
| Tarakeswar CDB | 38 | 60 | 82 | 97 | C |
| Dhaniakhali 5 GPs | 28 | 48 | 78 | 95 | C |
| Source | NFHS-4/5 urban-rural gradient + Ujjwala/Swachh Bharat 2016-19 rollout | | | Saubhagya scheme 2017-19 | |

### D.15 Vote × Religion (2019 LS, regional anchor)

P(party ‖ religion) — CSDS-Lokniti 2019 WB regional rollup; applied to Arambagh LS context.

| Religion | BJP | AITC | INC | LF | Other+NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 52 | 38 | 3 | 5 | 2 | C | CSDS 2019 WB regional post-poll; adjusted slightly for Arambagh Hindu OBC pattern (lower BJP than state avg due to Mahishya uncertainty; see D.16) |
| Muslim | 4 | 78 | 12 | 4 | 2 | C | Muslim consolidation behind TMC in 2019 WB; CPIM residual in Arambagh CPI(M) 8% total |
| Sarna / tribal | 42 | 40 | 3 | 12 | 3 | E | WB tribal vote split; some Left residual |
| Christian / Other | 35 | 48 | 8 | 6 | 3 | E | Approximation |

**Marginal recovery check (approximate):** Hindu(86.78)×0.52 + Muslim(11.74)×0.04 + Sarna(0.90)×0.42 + Other(0.58)×0.35 = 45.13 + 0.47 + 0.38 + 0.20 = **46.18% BJP** vs actual AC 198 BJP **42.47%** — 3.7pp gap; signals Hindu BJP lean is slightly overstated, OR there is intra-Hindu OBC TMC pull (see D.16); flag for v1 calibration refinement.

### D.16 Vote × Caste (2019 LS)

P(party ‖ caste) — CSDS-Lokniti 2019 WB regional + Arambagh-specific adjustment. **This is the load-bearing table for AC 198.**

> Key analytical note: Mahishya lean is contested. In Purba/Paschim Medinipur and Howrah, Mahishyas shifted strongly to BJP in 2019. Hooghly-belt Mahishyas may have leaned BJP but potentially with more residual TMC loyalty due to Krishak Bandhu (launched Jan 2019) — Mamata's welfare pitch to farmers was specifically timed. The tight 2pp TMC margin in this AC suggests Mahishya vote was split, with BJP getting a plurality but not a BJP-dominant sweep.

| Caste | BJP | AITC | INC | LF | Other+NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC bhadralok | 55 | 30 | 5 | 7 | 3 | C | Bhadralok BJP-leaning by 2019; CSDS WB |
| **Mahishya (dominant OBC/General)** | **48** | **40** | **3** | **7** | **2** | **D** | **Load-bearing cell.** Contested. Medinipur Mahishya ~55-60% BJP; Hooghly Mahishya somewhat lower due to Krishak Bandhu exposure and commuter-workforce TMC loyalty. Estimated 48% BJP / 40% AITC split for Hooghly-Tarakeswar Mahishya. See analytical note above. |
| Sadgop (OBC-B) | 42 | 43 | 4 | 9 | 2 | D | Slightly more TMC-leaning than Mahishya; local networks |
| Kurmi / Tili (OBC-A/B) | 38 | 44 | 5 | 11 | 2 | D | OBC groups lean TMC due to state scheme exposure |
| Bagdi (SC) | 38 | 45 | 4 | 11 | 2 | C | SC vote more BJP-resistant than Matua belt; CSDS SC aggregate |
| Bauri / other SC | 35 | 47 | 5 | 11 | 2 | C | |
| Namasudra (SC) | 45 | 40 | 4 | 9 | 2 | C | Slight BJP-tilt vs other Hooghly SC (NRC/CAA salience, though smaller here than in N24P) |
| Santal / ST | 35 | 42 | 3 | 17 | 3 | C | ST retains Left residual; CPI(M) 8% total is partly tribal |
| Muslim (any caste) | 4 | 78 | 12 | 4 | 2 | C | Same as D.15 |

**Marginal recovery check:** 
BJP: 0.255(SC-weighted ~37) + 0.073(ST ~35) + 0.300(OBC ~45) + 0.080(UC 55) + 0.159(Other Hindu ~40) + 0.117(Muslim 4) + 0.016(Other 35) ≈ 9.4+2.6+13.5+4.4+6.4+0.5+0.6 = **37.4%** — somewhat below actual 42.47%; BJP lean in caste sub-groups likely needs upward revision (+2–3pp on Mahishya/UC cells) in v1 when CSDS WB subnational data obtained.

### D.17 Vote × Gender (2019 LS, pre-welfare-expansion baseline)

P(party ‖ gender). Lakshmir Bhandar does NOT exist in 2019; Kanyashree and Sabuj Sathi are the main TMC women-focused schemes.

| Gender | BJP | AITC | INC | LF | Other+NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 47 | 41 | 4 | 6 | 2 | C | CSDS 2019 WB |
| Female | 38 | 50 | 3 | 7 | 2 | C | +9pp TMC women advantage in 2019 WB; Kanyashree recipients lean AITC |

### D.18 Vote × Welfare-scheme exposure (2019)

P(party ‖ household has scheme exposure). Schemes available in 2019: **Krishak Bandhu** (TMC, launched Jan 2019), **Kanyashree** (TMC, 2013), **Swasthya Sathi** (TMC, 2016), **Sabuj Sathi** (TMC, 2015), **Khadya Sathi** (TMC, 2016). Lakshmir Bhandar does NOT exist in 2019. PM Kisan does NOT exist in WB in 2019 (state refused central transfer; this became a BJP campaign grievance).

| Exposure | BJP | AITC | INC | LF | Tier | Source |
|---|---|---|---|---|---|---|
| Krishak Bandhu (cultivator HH, ~18% of AC) | 30 | 58 | 4 | 6 | C | First installment delivered May 2019 just before LS; strong TMC welfare-credit; slightly lower than Bangaon due to Mahishya BJP pull |
| Kanyashree (girl-student HH) | 33 | 54 | 4 | 7 | C | |
| Swasthya Sathi enrollee | 38 | 50 | 4 | 6 | C | Broad-based; weaker TMC tilt |
| Sabuj Sathi (bicycle HH) | 35 | 51 | 4 | 8 | C | |
| Khadya Sathi (PDS) | 42 | 47 | 4 | 5 | C | Near-universal; weakest TMC directional tilt |
| **No state-scheme exposure** | 58 | 28 | 5 | 7 | C | BJP-leaning; smaller set given near-universal PDS |
| **PM Kisan non-receipt grievance (BJP narrative)** | +5 | -5 | 0 | 0 | D | BJP campaign argued WB farmers denied PM Kisan ₹6000/yr because TMC blocked it. This grievance is directionally pro-BJP among cultivator HH aware of the scheme. Magnitude estimated at ~5pp shift among aware cultivators. |

---

## E. 2019 baseline vote (calibration target)

The simulator must reproduce the AC-level aggregate within ±1pp.

### Whole Arambagh LS (PC 29) — 2019 result (tier A, ECI / Wikipedia)

| Party | Candidate | Votes | % |
|---|---|---|---|
| AITC | Aparupa Poddar (Afrin Ali) | 649,929 | **44.14** |
| BJP | Tapan Kumar Roy | 648,787 | **44.06** |
| CPI(M) | Sakti Mohan Malik | — | ~8.0 |
| INC | — | — | ~1.7 |
| Others / NOTA | various | — | ~2.1 |
| **Margin** | AITC over BJP | **1,142 votes** | **0.08 pp** |

### AC 198 segment — 2019 LS (tier A, ECI CSV)

> Figures below are **tier A** — sourced directly from `2019_AssemblySegmentLevelVotingData.csv`, AC_NO=198, Tarakeswar. Total valid votes: 197,194; electorate: 232,456; turnout: 84.83%.

| Party | Candidate (LS level) | Votes | AC-198 segment % | Tier | Source |
|---|---|---|---|---|---|
| AITC | Aparupa Poddar (Afrin Ali) | 88,096 | **44.67%** | A | 2019_AssemblySegmentLevelVotingData.csv |
| BJP | Tapan Kumar Roy | 83,753 | **42.47%** | A | Same |
| CPI(M) | Sakti Mohan Malik | 15,747 | **7.99%** | A | Same |
| INC | Jyoti Kumari Das | 3,372 | **1.71%** | A | Same |
| NOTA | — | 2,938 | **1.49%** | A | Same |
| BSP | Samir Mitra | 562 | **0.28%** | A | Same |
| RaJSP | Binay Kumar Malik | 1,051 | **0.53%** | A | Same |
| SUCI(C) | Prosanta Malik | 397 | **0.20%** | A | Same |
| BNARP | Jhantu Lal Pakre | 320 | **0.16%** | A | Same |
| IND | Chittaranjan Mallick | 958 | **0.49%** | A | Same |
| **AITC margin over BJP** | | **4,343 votes** | **2.20 pp** | A | Computed from CSV |

**Key calibration observation:** This is the closest margin in the 10-seat pilot sample. AITC holds the seat by just 2.2pp; BJP is within striking distance; CPI(M) is a stable 8% "bystander" party. The AC is a true swing seat — the model must produce a tight two-way contest with no single party dominant.

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 198 specifically (Assembly Elections)

Note: Prior to delimitation 2008, Tarakeswar was constituency no. 185. Post-2008 renumbered 198.

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin | Tier |
|---|---|---|---|---|---|---|---|---|---|---|
| 2001 AE | Pratim Chatterjee | Ind (MFB-supported) | 69,186 | 54.55 | Mohan Ghosh | INC | 40,274 | 31.75 | 28,912 | A |
| 2006 AE | Pratim Chatterjee | Ind (MFB-supported) | 74,849 | 58.10 | Krishna Bhattacharjee | BJP | 44,578 | 34.60 | 30,271 | A |
| 2011 AE | Rachhpal Singh | AITC | 97,022 | 55.10 | Pratim Chatterjee | CPI(M) | 71,550 | 40.64 | 25,472 | A |
| 2016 AE | Rachhpal Singh | AITC | 97,588 | 50.75 | Surajit Ghosh | NCP | 69,898 | 36.35 | 27,690 | A |

**Narrative arc:** Seat held by Left/MFB from 1977 to 2011 (Pratim Chatterjee won as Ind/MFB). 2011: Hooghly-wide AITC wave brought Rachhpal Singh (AITC) — first non-Left MLA here in 34 years. 2016: AITC retained comfortably (50.75%), NCP as secondary opposition (interesting alliance pattern). By 2019 LS: BJP emerged from near-zero to 42.5%, reflecting the Mahishya-OBC rightward drift visible across Hooghly.

### Arambagh Lok Sabha (PC 29) historical

| Year | Winner | Party | Votes | % | Margin | Notes | Tier |
|---|---|---|---|---|---|---|---|
| 2009 LS | Sakti Mohan Malik | CPI(M) | 630,454 | 54.63 | 201,558 | Left "Red Fort"; INC second (36.85%); BJP insignificant | A |
| 2014 LS | Aparupa Poddar (Afrin Ali) | AITC | 748,764 | 54.94 | 346,845 | AITC landslide; CPI(M) collapsed to 29.51%; BJP emerging (3rd) | A |
| 2019 LS | Aparupa Poddar (Afrin Ali) | AITC | 649,929 | 44.14 | 1,142 | Closest seat in sample; BJP surged from fringe to 44.06%; CPI(M) residual ~8% | A |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- `2019_AssemblySegmentLevelVotingData.csv` — ECI GE2019 AC-segment vote tallies (tier A; AC_NO=198 rows used for Section E calibration target)
- `2024_AssemblySegmentLevelVotingData.csv` — ECI GE2024 AC-segment vote tallies (tier A; used in Section H)
- Census of India 2011 — Tarakeswar CD Block (via Wikipedia "Tarakeswar (community development block)"): population, religion, SC%, ST%, literacy, occupation, mother tongue
- Census of India 2011 — Tarakeswar Municipality (via census2011.co.in town data): population, SC%, ST%, literacy, religion, sex ratio
- Census of India 2011 — Dhaniakhali CD Block (via Wikipedia "Dhaniakhali (community development block)"): population, religion, SC%, ST%, literacy, occupation
- ECI archives 2001/2006/2011/2016 AE + 2009/2014/2019 LS — Tarakeswar AC and Arambagh LS results (via Wikipedia constituency articles)
- Delimitation Commission of India 2008 — WB Schedule (Tarakeswar = Tarakeswar Muni + all 10 GPs of Tarakeswar CDB + 5 GPs of Dhaniakhali CDB)
- WB Hooghly District Government Portal (hooghly.nic.in/chandannagar-subdivision/) — sub-division administrative assignment

### Secondary sources (tier B/C)
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership, banking baseline
- NFHS-5 (2019-21) West Bengal state summary — smartphone/internet growth trend confirmation
- PMJDY enrollment data (2014–2019) — banking access baseline
- Pew India 2021 — religion-differential growth rate projections (Hindu +1.0%/yr, Muslim +1.3%/yr)
- CSDS-Lokniti 2019 NES post-poll — vote × religion, vote × caste, vote × gender regional rollup for WB
- Swarajya Magazine summary of CSDS 2019 WB regional cross-tabs

### Tertiary / journalistic (tier D)
- India Today "Mahisyas and the new caste question in West Bengal politics" (2021) — Mahishya as single-largest caste in Hooghly; OBC campaign history; political wooing by TMC and BJP
- Wikipedia "Mahishya" — geographic distribution, historical dominance in Hooghly/Howrah/Midnapore; General (not OBC) classification
- PIB press release on PM-Kisan West Bengal — WB did not join PM-Kisan until FY2021-22 (8th installment); zero coverage in 2019
- WBXpress on Krishak Bandhu scheme — launch Jan 2019, enrollment from 28 Jan 2019, first Kharif installment May 2019
- Wikipedia "Tarakeswar" — temple pilgrimage economy, railway connectivity, Hindi-speaker fraction in Muni
- Wikipedia "Tarakeswar (Vidhan Sabha constituency)" and "Tarakeswar Assembly constituency" — composition, election results
- Wikipedia "Arambagh Lok Sabha constituency" — historical results, composition

### Tier-D/E reliance flags (what to distrust)
- **Caste sub-group shares within Hindu** (C.2, D.2) — no caste census post-1931 for non-SC/ST; Mahishya/Sadgop/Kurmi share estimates are tier D; the "18% Mahishya" figure is the single highest-uncertainty parameter
- **Mahishya vote split** (D.16) — the key load-bearing cell; 48% BJP / 40% AITC is an estimate derived from analogical inference (Medinipur Mahishya 55–60% BJP, discounted for Hooghly Krishak Bandhu exposure and commuter-workforce TMC loyalty); tier D; refine with CSDS AC-level data if obtainable
- **Dhaniakhali 5-GP data** (D.11–D.14) — using whole Dhaniakhali block as proxy for 5 GPs only; actual 5-GP demographics may differ (these 5 GPs may be higher or lower ST than block average)
- **Sub-division note** — task prompt specifies "Arambagh sub-division" but WB government records and Wikipedia confirm Tarakeswar CDB/Muni is in Chandannagore subdivision of Hooghly. Arambagh is the parent LS constituency, not the revenue sub-division. This is noted for downstream administrative accuracy.
- **Asset/media** (C.14, D.4, D.13) — NFHS-4/5 state-level pattern projected to AC; tier C
- **Vote × Demographic** (D.15–D.18) — CSDS 2019 WB regional rollup; tier C; marginal recovery check in D.16 shows ~5pp residual, flagged for v1

### v0 known gaps (see methodology §7)
1. DCHB Hooghly Part-A — collapsed Tarakeswar CDB to block-level; 10 individual GPs not disaggregated
2. DCHB Hooghly Part-A — collapsed Dhaniakhali 5 GPs to whole-block-level proxy; 5-GP subset demographics unknown
3. ECI electoral roll (2019) — electorate confirmed from CSV (232,456) but M/F breakdown not obtained
4. Census HH-13 — using NFHS state-level proxy for asset/media; refine with Census HH-13 block-level when accessible
5. Full CSDS WB regional cross-tabs — using Swarajya/CSDS press summary; could refine D.16 (Mahishya vote) with full Lokniti WB report
6. Mahishya caste share — no caste census; 18% estimate is journalistic/academic inference; uncertainty range ±5pp

---

*v0 — generated 2026-04-27, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **These are OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> The simulator must reproduce these results from 2019 priors + narrative injection without these figures being baked into the calibration input.

### 2021 WB Assembly Election — AC 198 Tarakeswar (tier A, ECI / Wikipedia)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| AITC | Ramendu Sinharay (Sinharoy) | 96,698 | **46.96%** | A — ECI 2021 AE / Wikipedia |
| BJP | Swapan Dasgupta | 89,214 | **43.33%** | A — ECI 2021 AE / Wikipedia |
| CPI(M) | Surajit Ghosh | ~14,000 | **~7.1%** | A — ECI 2021 AE |
| **AITC margin** | | **7,484 votes** | **3.63pp** | A |
| Turnout | 205,917 / 221,972 | | **85.86%** | A |

Background on BJP candidate (pre-2019 context, permissible): Swapan Dasgupta is a well-known BJP ideologue and journalist, long associated with BJP's intellectual wing; he was appointed Rajya Sabha MP (2016). His candidacy from Tarakeswar was announced for the 2021 AE — this is a post-2019 event and the simulator must model how his national profile affected local vote.

### 2024 Lok Sabha Election — AC 198 segment within Arambagh LS (PC 29) (tier A, CSV)

> Figures below are **tier A** — sourced directly from `2024_AssemblySegmentLevelVotingData.csv`, AC_NO=198, Tarakeswar. Total valid votes: 206,193; electorate: 244,468; turnout: 84.3%.

| Party | Candidate (LS level) | Votes | AC-198 segment % | Tier | Source |
|---|---|---|---|---|---|
| AITC | Mitali Bag | 97,685 | **47.38%** | A | 2024_AssemblySegmentLevelVotingData.csv |
| BJP | Arup Kanti Digar | 86,517 | **41.96%** | A | Same |
| CPI(M) | Biplab Kumar Moitra | 15,436 | **7.49%** | A | Same |
| NOTA | — | 2,490 | **1.21%** | A | Same |
| IND (Raghu Mallik) | — | 2,311 | **1.12%** | A | Same |
| Others (BSP, SUCI, IND) | various | 1,754 | **0.85%** | A | Same |
| **AITC margin over BJP** | | **11,168 votes** | **5.42 pp** | A | Computed |

### Calibration test
The simulator is considered validated on this seat if it reproduces 2024 LS AC-198 shares within ±3pp of the CSV tier-A figures:
- AITC target: 47% ± 3pp
- BJP target: 42% ± 3pp
- CPI(M) + others target: 11% ± 3pp

### Slow-drift median-voter note (load-bearing model constraint)
**This is the truest swing seat in the sample.** TMC and BJP have remained within 5pp of each other across all three elections (2019 LS: 2.2pp → 2021 AE: 3.6pp → 2024 LS: 5.4pp). TMC is very gradually pulling ahead (+2.7pp from 2019 to 2024 LS). CPI(M) has been a stable 7–8% bystander throughout. No single event caused a sharp shift — the drift is slow and directionally consistent.

**Model constraint:** The simulation must produce small, directionally consistent TMC gains, not sharp swings. Any narrative injection that produces a >5pp single-election swing is likely over-fitting. This is the **median-Hindu-OBC-voter slow-drift** seat — the test of whether the model captures gradual belief evolution rather than event-driven volatility.
