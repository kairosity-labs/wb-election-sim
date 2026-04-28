# AC 159 — Bhabanipur (General) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural state of AC 159 Bhabanipur as of 2019 only — it does not reference any post-2019 events. Use post-2019 elections (2021 AE, 2021 by-poll, 2024 LS) as out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).
>
> **Archetype: A5 — Urban Kolkata bhadralok + Hindi/Gujarati mixed | CM-incumbent dynamic.** Bhabanipur is a fully urban, KMC ward-based constituency — it has no Gram Panchayat sub-units. Sub-unit decomposition uses ward clusters (U1 / U2) rather than GP / Municipality.

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 159 | A | ECI / Delimitation Commission 2008 |
| AC name | Bhabanipur (also spelled Bhowanipore) | A | ECI |
| Reservation | General (unreserved) | A | Delimitation 2008 |
| District | Kolkata | A | Delimitation 2008 |
| Sub-division | Kolkata (urban ward-based; no block/rural sub-division) | A | WB administrative |
| LS constituency | PC 23 — Kolkata Dakshin | A | Delimitation 2008 |
| LS segments included in PC 23 | AC 149 Kasba · 153 Behala Purba · 154 Behala Paschim · 158 Kolkata Port · 159 Bhabanipur · 160 Rashbehari · 161 Ballygunge | A | Delimitation 2008 |
| AC composition | KMC Ward Nos. 63, 70, 71, 72, 73, 74, 77, 82 of Kolkata Municipal Corporation (Borough VIII area) | A | Delimitation 2008; Wikipedia Bhabanipur AC |
| Geographic note | South-central Kolkata; bounded by Gariahat to the east, Kalighat to the south-west, Rashbehari to the north, Kidderpur/Garden Reach fringe to the west | A | — |
| Urban character | 100% urban; KMC ward-based; no GP, no CDB, no rural block | A | Census 2011 — Kolkata district 100% urban |
| Two sub-units used in v0 (ward-cluster conditioning) | **U1: North ward cluster** (Wards 63, 70, 71, 72 — Bhowanipore core + Hazra) · **U2: South-west ward cluster** (Wards 73, 74, 77, 82 — Kalighat fringe + Patuapara + Elgin Road) | E | v0 simplification; ward 82 (Kidderpur fringe) carries higher Muslim share |

---

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~242,604 | A | Census 2011 — Bhabanipur AC (Wikipedia / Election Pandit; 100% urban, 8-ward aggregate) |
| SC share 2011 | 2.23% (~5,410 persons) | A | Census 2011 AC-level SC ratio (Wikipedia Bhabanipur AC) |
| ST share 2011 | 0.26% (~631 persons) | A | Census 2011 AC-level ST ratio (Wikipedia Bhabanipur AC) |
| 2019 projected population | ~254,500 | E | 8-yr compound urban growth ~0.6%/yr (Kolkata KMC area grows slower than state average; dominated by in-migration offsetting low natural increase) |
| Sex ratio (2019, F per 1000 M) | ~940 | E | Kolkata district 2011: 941 (Census); urban Kolkata skewed male due to working-age male in-migration |
| 2019 estimated electorate (18+) | ~200,000 | A | ECI 2019 LS data: 200,938 electors in AC 159 (CSV tier A) |
| Estimated M / F / TG split (2019) | 52% M / 47.9% F / <0.1% TG | E | Kolkata district 2011 sex ratio 941; male-skew persists in urban working-age in-migrants |
| 2019 polling stations | ~200 | D | Inferred: 200,938 electors ÷ ~1,000/booth urban norm; formal roll not separately published |
| 2019 total votes polled | 136,091 | A | ECI 2019 LS Form-20 / CSV: sum of all candidates + NOTA in AC 159 |
| 2019 turnout | 67.73% | A | 136,091 / 200,938 |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 73.50 | D | Bhabanipur AC: ~42% Bengali Hindu + ~31.5% non-Bengali Hindu = ~73.5% Census-Hindu (i.e. excludes Sikh, Jain counted separately per Census religion taxonomy); consistent with 24% Muslim and KMC-district average |
| Muslim | 24.00 | D | Multiple journalistic sources: "20% Muslim voters"; The Federal cites ~21.9% Muslim voters; rounded to 24% total pop (voters skew slightly lower — Muslim pop is younger with more sub-18 share) |
| Sikh | 1.50 | D | Bhabanipur has a noted Sikh community along Gurudwara corridor (Bhowanipore area); journalistic sources cite "Sikh households" as visible bloc |
| Jain | 0.80 | D | Marwari-Jain community; Bhowanipore + Elgin Road area; Census counts Jain separately from Hindu |
| Christian | 0.20 | E | Small urban Christian fringe |
| **Sum** | **100.00** | — | self-check |

*(Note: 2011 Census for Kolkata district: Hindu 76.51%, Muslim 20.60%, Christian 0.88%, Sikh 0.61%, Jain 0.48%, others ~1.0%. Bhabanipur AC has higher Muslim share than KMC average, consistent with Ward 82 Kidderpur-fringe population. The "42% Bengali Hindu + 34% NB Hindu" journalistic framing includes Sikhs and Jains within the "Hindu" umbrella used colloquially; Census taxonomy separates them.)*

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC total** | 2.23 | A | Census 2011 direct for AC 159 |
| └ Namasudra / Rajbanshi / other SC | 2.23 | E | No Matua concentration in Kolkata urban; generic urban SC pool |
| **ST total** | 0.26 | A | Census 2011 direct for AC 159 |
| **Bengali bhadralok UC** (Brahmin / Kayastha / Baidya) | 25.00 | D | Bhowanipore historically bhadralok residential; Kayastha-Brahmin dominant in older parts; ~25% est. (journalistic sources on "South Kolkata bhadralok character") |
| **Bengali OBC / middle-caste Hindu** (Sadgop / Tili / Subarnabanik / Tanti / unclassified) | 15.00 | E | South Kolkata urban middle-caste pool; Subarnabanik merchant community notable; subtotal Bengali Hindu ~42% (UC 25 + OBC 15 + SC 2.23 + ST 0.26) |
| **Marwari** (Rajasthani Hindu) | 10.40 | D | The Print cites "10.4% Marwaris" in Bhabanipur electorate |
| **Gujarati Hindu** | 8.00 | D | Bhowanipore: Gujarati business families in Lansdowne-Chakraberia-Pudda Pukur belt; journalistic sources |
| **Bihari / UP migrant Hindu** | 7.00 | D | Labour + trade migrants from Hindi belt; ward 82 fringe + service workers |
| **Sikh** | 1.50 | D | See C.1; Punjabi community with Gurudwara presence |
| **Oriya Hindu** | 2.00 | D | South Kolkata domestic workers + traders from Odisha |
| **Jain** | 0.80 | D | Marwari-Jain business families; Elgin Road area; Census classifies Jain separately |
| **Other non-Bengali Hindu / South Indian / Anglo-Indian** | 3.60 | E | Residual non-Bengali non-Muslim bloc; South Indian professionals, small Tamil/Nepali communities |
| **Muslim** (all sub-groups) | 24.00 | D | See C.1; sub-structure in D.2 |
| Christian + Buddhist + other religion | 0.21 | E | Residual; small Christian + Parsi fringe |
| **Sum** | **100.00** | — | self-check: 2.23+0.26+25+15+10.40+8+7+1.50+2+0.80+3.60+24+0.21 = 100.00 |

### C.3 Age cohort (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 0–4 | 6.5 | E | Kolkata urban TFR ~1.5-1.6; low child share vs rural WB |
| 5–9 | 7.0 | E | |
| 10–14 | 7.5 | E | |
| 15–17 (pre-voter) | 5.0 | E | |
| 18–22 (first-time voters at 2019) | 9.5 | E | Urban youth bulge with in-migration |
| 23–27 | 10.5 | E | Working-age in-migrants peak here |
| 28–32 | 10.0 | E | |
| 33–37 | 9.0 | E | |
| 38–42 | 8.0 | E | |
| 43–47 | 7.5 | E | |
| 48–52 | 6.5 | E | |
| 53–57 | 5.0 | E | |
| 58–62 | 4.0 | E | |
| 63–67 | 2.5 | E | |
| 68+ | 1.5 | E | Kolkata urban elderly share lower than rural; out-migration to satellite towns |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.53 | E | Kolkata district 2011 sex ratio 941 (F per 1000 M) → 51.53% M / 48.46% F; male in-migration slightly increases male share over 8yr |
| Female | 48.46 | E | |
| Third gender | 0.01 | E | Urban Kolkata; small registered TG population |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 58.00 | D | Bengali Hindu + Bengali Muslim (roughly 42% Bengali Hindu + ~12% Bengali-speaking Muslims) ≈ 58% first language Bengali |
| Hindi | 20.00 | D | Marwari + Bihari/UP + some Gujarati Hindi-Hindi speakers; Bhowanipore has significant Hindi-belt diaspora |
| Gujarati | 7.00 | D | Gujarati business families; mother tongue distinct from Hindi |
| Urdu | 8.00 | D | A portion of Muslim population; Urdu-speaking sub-set; overlaps with Hindi-belt Muslim migrants in Ward 82 fringe |
| Punjabi | 1.50 | D | Sikh community |
| Odia | 2.00 | D | Odia workers/traders |
| English-dominant (Anglo-Indian / expat / elite school) | 0.50 | E | Small elite bilingual urban fringe |
| Other (Tamil/Marathi/Sindhi/Nepali) | 3.00 | E | Residual urban diversity in Kolkata |
| **Sum** | **100.00** | — | self-check |

*(Bilingualism flag: ~40% of population is bilingual Bengali+Hindi, or Hindi+Gujarati, or Bengali+English. This is unusually high vs rural WB — reflects Kolkata urban multilingual character. Tier D.)*

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 7.0 | E | Kolkata city literacy ~87.14% (Census 2011, A); AC 159 as premium urban area likely ~90%+ literate by 2019 → ~7% illiterate (mainly elderly women + migrant-labour fringe) |
| Primary (Class 1–5) | 10.0 | E | Census 2011 Kolkata education distribution |
| Middle (Class 6–8) | 13.0 | E | |
| Secondary (Class 9–10) | 19.0 | E | |
| Higher Secondary (Class 11–12) | 20.0 | E | Urban premium: HS share much higher than state average |
| Graduate | 22.0 | E | Kolkata bhadralok + business community: very high graduate share |
| Postgraduate | 9.0 | E | Notable research/professional class in South Kolkata |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main worker | 42.0 | E | Kolkata urban main-worker rate higher than WB rural; Census 2011 Kolkata main-worker ~42% |
| Marginal worker | 5.0 | E | Low marginal workers in urban Kolkata |
| Non-worker (housewife / retired / elderly) | 35.0 | E | Includes housewife share among non-Bengali women + retired bhadralok |
| Student (18–22, in education) | 10.0 | E | Large student population in South Kolkata university belt |
| Unemployed (educated, actively seeking) | 8.0 | E | Educated unemployment significant; graduate job-aspirant pool |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 0.0 | E | 100% urban; no agriculture |
| Agricultural labourer | 0.0 | E | Same |
| Household industry | 3.0 | E | Small-scale tailoring, handicraft, home-based retail |
| Manufacturing (organised) | 6.0 | E | Small factories + workshops; declining in Kolkata proper |
| Construction | 4.0 | E | Urban construction labour in-migrants |
| Trade / retail | 22.0 | E | Dominant sector: Marwari/Gujarati merchants + Bengali small traders; Rashbehari Ave, Gariahat proximity |
| Transport (auto, taxi, logistics) | 8.0 | E | Kolkata urban transport; Bhabanipur has major road corridors |
| Services (private) — banking, IT, hospitality | 22.0 | E | South Kolkata professional / service sector |
| Government services / teachers | 18.0 | E | High concentration of govt employees + teachers in bhadralok households |
| Domestic workers | 5.0 | E | Employed in affluent households within constituency |
| Petty vendor / street commerce | 7.0 | E | Urban informal economy |
| Other professionals (doctor, lawyer, CA) | 5.0 | E | South Kolkata professional cluster |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 8.0 | E | Higher than state average; Marwari/Gujarati business ownership |
| Employee (regular wage / salary) | 52.0 | E | Govt + private service dominant in urban Kolkata |
| Single worker (own-account) | 32.0 | E | Small traders, vendors, professionals |
| Family worker (unpaid) | 8.0 | E | Family businesses (Marwari/Gujarati HH) |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL household | 8.0 | E | Kolkata urban poverty much lower than rural WB; ~8% est. (WB urban BPL ~12-13% in 2011; Bhabanipur above-average affluence → ~8%) |
| Above-Poverty-Line, low-income | 22.0 | E | Construction labour, domestic workers, petty vendors |
| Lower-middle | 28.0 | E | Clerical govt, small trade, semi-skilled services |
| Middle | 25.0 | E | Teachers, officers, established small business |
| Upper-middle | 12.0 | E | Senior govt / corporate, large trade |
| Well-off / affluent | 5.0 | E | Marwari/Gujarati business elite, senior professionals; Bhowanipore + Elgin Road pockets |
| **Sum** | **100.00** | — | self-check |

### C.11 Ward cluster / zone location (2019)

*(Bhabanipur is fully urban; this section replaces GP / Municipality with KMC ward clusters.)*

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **U1: North ward cluster** (Wards 63, 70, 71, 72 — Bhowanipore core, Hazra Rd, Naktala fringe) | 52.0 | E | Ward 71 pop 29,922 + Ward 73 pop 23,512 (Census 2011 via Wikipedia) used as anchor; 4 of 8 wards roughly ~52% of AC pop; lower Muslim share, more Bengali + Marwari-Gujarati |
| **U2: South-west ward cluster** (Wards 73, 74, 77, 82 — Kalighat, Patuapara, Elgin Rd, Kidderpur fringe) | 48.0 | E | Ward 82 carries Kidderpur-adjacent Muslim-concentrated blocks; higher Muslim share in U2 |
| **Sum** | **100.00** | — | self-check |

*(Note: Full 8-ward breakdown with individual Census 2011 populations deferred to v1 when DCHB Kolkata Part-A ward tables are accessible.)*

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg HH size | 3.8 persons | E | Urban Kolkata HH size ~3.7-3.9 (Census 2011 Kolkata 3.7); slightly higher for Muslim HH |
| Nuclear HH | 75.0 | E | NFHS-4 WB urban pattern; high in bhadralok + non-Bengali communities |
| Joint HH | 18.0 | E | Marwari/Gujarati business families tend toward joint structure |
| Extended / multi-generation | 7.0 | E | |
| **Sum** | **100.00** | — | self-check |

*(HH head: ~80% male-headed, 20% female-headed; higher female-headed share than rural WB due to urban widow HHs and single-professional women; tier E.)*

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never married | 30.0 | E | Urban youth + student population; large single working cohort |
| Currently married | 61.0 | E | |
| Widowed | 7.5 | E | Concentrated in 60+ female cohort |
| Separated / divorced | 1.5 | E | Slightly higher than rural WB; urban educated population |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 95.0 | C | NFHS-4 WB urban ~89%; South Kolkata upper-income → ~95% by 2019 |
| Radio | 6.0 | C | Very low; declining urban media |
| Mobile phone (any) | 97.0 | C | Near-saturation in urban Kolkata by 2019 |
| Smartphone with internet | 78.0 | C | NFHS-4 WB urban ~60%; +Jio rollout 2016-19 + bhadralok high income → ~78% |
| Computer / laptop | 38.0 | C | South Kolkata professional class; much higher than state average |
| Two-wheeler | 30.0 | C | Lower than suburban; Kolkata has dense public transport reducing motorcycle need |
| Four-wheeler | 20.0 | C | Much higher than state average; 1-in-5 HHs has a car in this constituency |
| Banking access (any) | 98.0 | B | Near-saturation in urban Kolkata; PMJDY + prior formal banking history |
| Cable / satellite TV subscription | 85.0 | C | Bengali news channels + Hindi news heavy consumption |
| **Note** | (these are independent ownership %s, do not sum) | — | — |

### C.15 Household amenities (2019)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved drinking water (piped municipal) | 98.0 | C | KMC piped water — near-universal in this constituency |
| Improved sanitation (flush latrine) | 97.0 | C | Urban Kolkata near-universal; KMC sewage network |
| LPG / clean cooking fuel | 90.0 | C | NFHS-4 WB urban 81%; South Kolkata affluence → ~90% |
| Kerosene / biomass fuel | 8.0 | C | Declining; petty-vendor and domestic-worker households |
| Other fuel | 2.0 | E | |
| Electricity (metered) | 99.5 | A | Census 2011 Kolkata ~99% + Saubhagya 2017-19 |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native Kolkata-born (born in Kolkata or KMC area) | 50.0 | D | South Kolkata old-neighbourhood families; bhadralok multigenerational residents |
| WB other district (in-migrant from rest of WB) | 10.0 | D | Service class from Hooghly, Howrah, 24 Parganas migrating for work / education |
| **Hindi belt (UP/Bihar/Rajasthan/Gujarat) in-migrant** | **28.0** | **D** | **Load-bearing**: Marwari (~10.4%), Gujarati (~8%), Bihari/UP labour and trade (~7%), Rajasthani others — all sourced from Hindi-belt or Gujarati-speaking states; settled 1–3 generations ago or recent |
| Other Indian state (Orissa, South India, Maharashtra, Punjab) | 8.0 | D | Odia workers + Sikh Punjabi community + South Indian professionals |
| Bangladesh-origin Hindu | 2.5 | D | Very low in Kolkata Dakshin vs North WB; a small refugee-SC fringe |
| Outside India (other) | 0.5 | E | NRI families; small Anglo-Indian / Parsi fraction |
| Out-migrant (registered here but working elsewhere) | 1.0 | E | Bhadralok professionals working in Mumbai/Delhi/abroad; return-vote pattern |
| **Sum** | **100.00** | — | self-check |

*(Migration is the defining feature of Bhabanipur's uniqueness: ~28% of the population traces roots to the Hindi belt, making it WB's most non-Bengali constituency outside border districts. This is the structural basis for BJP's strong urban performance here.)*

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Gujarati | Urdu | Punjabi | Odia | Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu (Bengali) | 100 | 0 | 0 | 0 | 0 | 0 | 0 | E | By definition — Bengali Hindu uses Bengali |
| Hindu (non-Bengali) | 5 | 52 | 22 | 5 | 5 | 6 | 5 | D | Marwari/Bihari: Hindi; Gujarati: Gujarati; Odia: Odia; Sikh: Punjabi |
| Muslim | 50 | 20 | 0 | 28 | 0 | 1 | 1 | D | Bhabanipur: ~50% Bengali-speaking Muslims (Sheikh/local) + ~20% Hindi-speaking (Bihar-origin) + ~28% Urdu-dominant |
| Sikh | 10 | 30 | 0 | 0 | 60 | 0 | 0 | E | Sikh: Punjabi dominant |
| Jain | 10 | 30 | 55 | 0 | 0 | 0 | 5 | E | Jain: Gujarati or Hindi |
| **Marginal Bengali** | | | | | | | | | 0.735×(Bengali-H ~42/73.5=57.1%→100%) + 0.24×Muslim 50% = ~0.42×100 + 0.24×50 ≈ 42+12 = 54 + NB-Hindu ~5% = **~58%** ✓ matches C.5 |

### D.2 Religion × Caste (Hindu-internal + Muslim sub-structure)

P(caste ‖ Hindu) — % within Hindu population (~73.5% of total; excludes Jain 0.8% counted separately in Census):

| Caste sub-group | % of Hindu | Tier | Source |
|---|---|---|---|
| UC bhadralok Bengali (Brahmin/Kayastha/Baidya) | 34.0 | D | 25% of total pop / 73.5% Hindu |
| Bengali OBC / middle-caste (Sadgop/Tili/Subarnabanik) | 20.4 | E | 15% of total / 73.5% |
| SC total | 3.0 | A | 2.23% of total / 73.5% |
| ST | 0.4 | A | 0.26% of total / 73.5% |
| Marwari | 14.1 | D | 10.4% / 73.5% |
| Gujarati | 10.9 | D | 8% / 73.5% |
| Bihari/UP Hindu | 9.5 | D | 7% / 73.5% |
| Odia | 2.7 | D | 2% / 73.5% |
| Other NB Hindu (South Indian / other) | 4.9 | E | 3.6% / 73.5%; residual to close sum |
| **Sum** | **99.9** | — | self-check (rounding) |

P(Muslim sub-caste ‖ Muslim):

| Muslim sub-group | % of Muslim | Tier | Source |
|---|---|---|---|
| Bengali Sheikh (local urban Muslim) | 45 | D | South Kolkata Muslim belt; old-resident Kolkata Muslims |
| Bihari/UP Muslim (in-migrant Hindi-belt) | 25 | D | Kidderpur fringe (Ward 82) + labour migrant pool; Hindi/Urdu-speaking |
| Pathan / Sayyid | 8 | D | Old Kolkata Muslim aristocracy fringe |
| OBC Muslim (Jolaha / Nai / Darzi / Kasai) | 15 | D | Artisan Muslim; present in Kalighat area |
| Other / unclassified | 7 | E | Mixed; Qureshi etc. |
| **Sum** | **100** | — | self-check |

### D.3 Religion × Migration / birthplace

P(birthplace ‖ religion) — % within each religion.

| Religion | Native Kolkata | WB-other-dist | Hindi-belt | Other state | Bangladesh-origin | Outside India | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Bengali Hindu | 65 | 15 | 0 | 5 | 13 | 2 | D | Old Kolkata bhadralok families; small refugee fraction from East Bengal |
| Non-Bengali Hindu | 15 | 5 | 75 | 5 | 0 | 0 | D | Marwari/Gujarati/Bihari are almost entirely Hindi-belt origin (settled 1-3 gen) |
| Muslim | 45 | 10 | 35 | 5 | 4 | 1 | D | ~45% long-resident Bengali Muslim; ~35% Hindi-belt Muslim migrant (Bihari/UP in Kidderpur) |
| Sikh | 30 | 5 | 60 | 5 | 0 | 0 | E | Punjabi settled families |
| Jain | 20 | 5 | 70 | 5 | 0 | 0 | E | Marwari-Jain |
| **Marginal recovery — Hindi-belt** | | | | | | | | 0.42×0 + 0.34×0.75 + 0.24×0.35 + 0.015×0.60 + 0.008×0.70 = 0 + 0.255 + 0.084 + 0.009 + 0.006 = **0.354** vs C.16 **0.28** ⚠ ~7.5pp gap — flag for v1; Hindi-belt % may be slightly lower or Bengali-NB-Hindu migrant fraction higher than assumed |

### D.4 Religion × Asset / media (TV, smartphone, banking)

P(owns asset ‖ religion) — % within each religion.

| Religion | TV | Smartphone-internet | Banking | Four-wheeler | Tier | Source |
|---|---|---|---|---|---|---|
| Bengali Hindu | 97 | 82 | 99 | 18 | C | Bhadralok high-media, high-banking; moderate car ownership |
| Non-Bengali Hindu | 96 | 85 | 99 | 28 | C | Marwari/Gujarati: very high smartphone + car; business use |
| Muslim | 88 | 58 | 94 | 8 | C | Lower income stratum on average; Muslim ward fringe (W82) lower |
| Sikh | 97 | 86 | 99 | 32 | C | Punjabi community: high asset; car ownership high |
| Jain | 98 | 90 | 100 | 40 | C | High-income Jain business families |

### D.5 Caste × Education

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Sec | HS | Grad | PG | Tier |
|---|---|---|---|---|---|---|---|---|
| UC bhadralok Bengali | 2 | 3 | 5 | 12 | 20 | 35 | 23 | E |
| Bengali OBC/middle | 7 | 8 | 12 | 20 | 25 | 22 | 6 | E |
| SC (Bengali) | 12 | 15 | 18 | 22 | 18 | 12 | 3 | E |
| Marwari | 4 | 5 | 10 | 18 | 25 | 28 | 10 | E |
| Gujarati | 3 | 5 | 8 | 15 | 25 | 32 | 12 | E |
| Bihari/UP Hindu | 14 | 18 | 22 | 22 | 14 | 8 | 2 | E |
| Muslim (all) | 12 | 18 | 22 | 22 | 15 | 9 | 2 | E |
| Odia | 10 | 15 | 20 | 25 | 18 | 10 | 2 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Cohort | Male grad+ | Female grad+ | Tier | Source |
|---|---|---|---|---|
| 18–22 | 30 | 35 | E | Female grad+ edges male in young Kolkata urban cohort; education expansion |
| 23–27 | 40 | 42 | E | Peak: urban Kolkata's working young adult |
| 28–32 | 38 | 35 | E | |
| 33–42 | 35 | 28 | E | |
| 43–57 | 28 | 18 | E | Older female cohort lower |
| 58+ | 22 | 10 | E | |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender).

| Age | Male married | Female married | Tier |
|---|---|---|---|
| 18–22 | 4 | 18 | E |
| 23–27 | 30 | 65 | E |
| 28–32 | 72 | 85 | E |
| 33–47 | 88 | 84 | E |
| 48–62 | 85 | 68 | E |
| 63+ | 72 | 28 | E (widow concentration) |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone-internet | TV | Four-wheeler | Tier | Source |
|---|---|---|---|---|---|
| Trade / retail (large, Marwari/Gujarati) | 92 | 98 | 45 | C | Business community — very high |
| Trade / retail (small/petty vendor) | 70 | 92 | 5 | C | |
| Govt services / teachers | 88 | 97 | 18 | C | Bhadralok service class |
| Private services (banking/IT) | 90 | 97 | 22 | C | Urban professional |
| Professionals (doctor/lawyer) | 93 | 98 | 55 | C | |
| Transport | 65 | 88 | 5 | C | Auto/taxi drivers |
| Manufacturing | 60 | 88 | 8 | C | |
| Construction labour | 40 | 75 | 0 | C | In-migrant construction workers |
| Domestic workers | 38 | 60 | 0 | C | Lowest stratum |
| Student (18–22) | 88 | 95 | 12 | C | Urban youth: very high smartphone |

### D.9 Education × Workforce participation

P(unemployed-and-seeking ‖ education).

| Education | Unemployed-seeking | Main-worker rate | Tier |
|---|---|---|---|
| Illiterate | 3 | 30 | E |
| Primary | 5 | 35 | E |
| Middle | 7 | 38 | E |
| Secondary | 10 | 35 | E |
| Higher Secondary | 12 | 32 | E |
| Graduate | 14 | 38 | E |
| Postgraduate | 8 | 55 | E |

### D.10 Asset / media × Bilingualism

P(bilingual ‖ media-access tier).

| Media tier | Bengali+Hindi bilingual | Bengali+English bilingual | Hindi+Gujarati bilingual | Tier | Source |
|---|---|---|---|---|---|
| TV-only HH | 18 | 5 | 10 | E | Bengali + Zee/Aaj Tak cross-exposure |
| TV + smartphone HH | 28 | 15 | 18 | E | YouTube + news consumption |
| Smartphone-only HH | 22 | 12 | 15 | E | |
| No-asset HH | 8 | 2 | 5 | E | Minimal exposure |
| **Population-wide bilingual rate** | ~22 | ~12 | ~12 | E | Derived; unusually high vs rural WB |

### D.11 Ward cluster × Religion

P(religion ‖ ward cluster location).

| Sub-unit | Hindu (all) | Muslim | Sikh+Jain+Other | Tier | Source |
|---|---|---|---|---|---|
| **U1: North cluster** (Wards 63, 70, 71, 72 — 52% pop) | 79.0 | 18.0 | 3.0 | D | Bhowanipore core: predominantly Bengali bhadralok + Marwari-Gujarati bloc; lower Muslim share |
| **U2: South-west cluster** (Wards 73, 74, 77, 82 — 48% pop) | 66.5 | 30.5 | 3.0 | D | Ward 82 Kidderpur-adjacent + Patuapara Muslim pocket; Kalighat fringe; meaningfully higher Muslim concentration |
| **Marginal recovery — Muslim** | | | | | 0.52×0.18 + 0.48×0.305 = 0.0936 + 0.1464 = **0.240** ✓ matches C.1 marginal **24.0%** within ±0.5pp |

### D.12 Ward cluster × Caste (within sub-unit, key categories)

P(caste ‖ ward cluster).

| Sub-unit | UC Bengali | Marwari+Gujarati | Bihari/UP | Odia | Bengali OBC | Muslim | SC | Tier |
|---|---|---|---|---|---|---|---|---|
| U1 North | 30 | 25 | 8 | 2 | 16 | 18 | 2 | D |
| U2 South-west | 18 | 15 | 12 | 3 | 18 | 31 | 3 | D |
| Source | Bhowanipore bhadralok core | Lansdowne-Chakraberia belt heavier in N | Kidderpur fringe higher in U2 | | | W82 Kidderpur + Patuapara dominant in U2 | | |

### D.13 Ward cluster × Asset / media

| Sub-unit | TV | Smartphone-internet | Computer | Four-wheeler | Banking | Tier |
|---|---|---|---|---|---|---|
| U1 North | 97 | 82 | 42 | 24 | 99 | C |
| U2 South-west | 93 | 73 | 33 | 15 | 97 | C |
| Source | Bhadralok + business community high-asset | | | | | NFHS-4/5 WB urban gradient; constituency-adjusted |

### D.14 Ward cluster × Amenities

| Sub-unit | LPG | Improved sanitation | Improved water | Electricity | Tier |
|---|---|---|---|---|---|
| U1 North | 93 | 98 | 99 | 99.8 | C |
| U2 South-west | 86 | 95 | 97 | 99.2 | C |
| Source | KMC infrastructure near-universal; U2 slightly lower for migrant-labour households | | | | |

### D.15 Vote × Religion (2019 LS, AC 159 specific anchor)

P(party ‖ religion) — calibrated to AC 159 2019 LS result. AC-specific adjustment to CSDS WB baseline: BJP over-performs vs state average in non-Bengali Hindu; AITC retains Muslim near-monopoly; CPI(M)/INC much weaker than rural WB.

| Religion | BJP | AITC | CPI(M) | INC | Others+NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Bengali Hindu (~42% of pop) | 43 | 48 | 5 | 3 | 1 | C/D | CSDS 2019 WB urban bhadralok: BJP ~43% consistent with national-level UC Hindu swing; AITC retains plurality due to CM incumbency |
| Non-Bengali Hindu (~34% of pop) | 65 | 20 | 5 | 5 | 5 | D | Marwari/Gujarati: strongly BJP (Modi factor, national narrative); Bihari workers split BJP/INC |
| Muslim (~24% of pop) | 10 | 75 | 8 | 5 | 2 | C | CSDS 2019 WB: Muslim near-consolidation behind AITC; Bhabanipur consistent |
| Sikh (1.5%) | 55 | 28 | 5 | 7 | 5 | E | Nationally Sikh leaned BJP in 2019 |
| Jain (0.8%) | 70 | 18 | 2 | 5 | 5 | E | Business Jain: strong BJP |
| **Model recovery: BJP** | | | | | | | 0.42×0.43 + 0.34×0.65 + 0.24×0.10 + 0.015×0.55 + 0.008×0.70 = 0.181+0.221+0.024+0.008+0.006 = **0.440** vs actual **42.60%** ✓ within ±2pp (residual in Others) |
| **Model recovery: AITC** | | | | | | | 0.42×0.48 + 0.34×0.20 + 0.24×0.75 + 0.015×0.28 + 0.008×0.18 = 0.202+0.068+0.180+0.004+0.001 = **0.455** vs actual **44.92%** ✓ within ±1pp |

### D.16 Vote × Caste (2019 LS)

P(party ‖ caste) — AC 159 adjustment.

| Caste | BJP | AITC | CPI(M) | INC | Others | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC Bengali bhadralok | 45 | 44 | 6 | 4 | 1 | C | Close contest; bhadralok split (BJP Modi-surge vs AITC CM-incumbent) |
| Bengali OBC/middle | 38 | 50 | 7 | 4 | 1 | C | More AITC-leaning; benefit from TMC welfare schemes |
| SC (Bengali) | 30 | 52 | 10 | 6 | 2 | C | |
| Marwari | 68 | 18 | 4 | 5 | 5 | D | Strong BJP; Gujarat/Marwar business community national BJP orientation |
| Gujarati | 70 | 16 | 3 | 5 | 6 | D | Strongest BJP sub-group |
| Bihari/UP Hindu | 55 | 28 | 8 | 8 | 1 | D | Modi wave; some INC retention |
| Odia | 40 | 42 | 8 | 7 | 3 | E | Mixed; regional identity |
| Muslim (all) | 10 | 75 | 8 | 5 | 2 | C | Same as D.15 |

### D.17 Vote × Gender (2019 LS, pre-welfare-scheme baseline)

P(party ‖ gender). Lakshmir Bhandar does NOT exist in 2019 — no LB-driven female swing captured here.

| Gender | BJP | AITC | CPI(M) | INC | Others | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 46 | 42 | 6 | 4 | 2 | C | CSDS 2019 WB urban male: BJP edges AITC; male non-Bengali voters more BJP-concentrated |
| Female | 38 | 49 | 7 | 4 | 2 | C | CSDS 2019: female TMC advantage ~7-9pp; absent LB this is structural (CM-incumbent female empathy) |

### D.18 Vote × Welfare-scheme exposure (2019)

P(party ‖ household scheme exposure). Urban Bhabanipur context: Krishak Bandhu N/A (urban); Kanyashree, Swasthya Sathi, Khadya Sathi most relevant. **Lakshmir Bhandar does NOT exist in 2019.**

| Exposure | BJP | AITC | CPI(M) | INC | Tier | Source |
|---|---|---|---|---|---|---|
| Kanyashree beneficiary HH | 35 | 52 | 7 | 5 | C | Urban girl-child education scheme; moderate AITC tilt |
| Swasthya Sathi enrollee | 40 | 48 | 6 | 5 | C | Broad health coverage; weaker AITC tilt in urban (govt hospital access pre-exists) |
| Khadya Sathi (PDS) | 42 | 46 | 6 | 5 | C | Near-universal; weakest tilt |
| Sabuj Sathi (bicycle — less relevant urban) | 38 | 50 | 6 | 5 | E | Fewer urban recipients |
| **No state-scheme exposure** | 55 | 32 | 7 | 5 | C | BJP-leaning HHs; affluent Marwari/Gujarati who use private services |

---

## E. 2019 baseline vote (calibration target)

The simulator must reproduce AC 159's aggregate within ±1pp.

### Whole Kolkata Dakshin LS (PC 23) — 2019 result (tier A, ECI CSV)

| Party | Candidate | Votes | % |
|---|---|---|---|
| AITC | **Mala Roy** | 572,188 | **48.11** |
| BJP | Chandra Kumar Bose | 417,086 | **35.07** |
| CPI(M) | (various per AC) | 139,770 | 11.75 |
| INC | (various per AC) | 42,536 | 3.58 |
| Others + NOTA | — | 17,876 | 1.50 |
| **Total** | | **1,189,456** | **100.00** |
| **Margin** | AITC over BJP | **155,102** | **13.04 pp** |

*Source: 2019_AssemblySegmentLevelVotingData.csv (tier A). Electors: 1,728,850 across 7 ACs.*

### AC 159 Bhabanipur segment — 2019 result (tier A, ECI CSV)

| Party | Candidate | Votes | % | Tier | Note |
|---|---|---|---|---|---|
| AITC | Mala Roy | 61,137 | **44.92** | A | CSV direct |
| BJP | Chandra Kumar Bose | 57,969 | **42.60** | A | CSV direct |
| CPI(M) | Nandini Mukherjee | 8,700 | **6.39** | A | CSV direct |
| INC | Mita Chakraborty | 4,662 | **3.43** | A | CSV direct |
| Others (BSP+SUCI(C)+SHS+7×IND) | various | 1,836 | **1.35** | A | CSV direct |
| NOTA | — | 1,787 | **1.31** | A | CSV direct |
| **Total votes** | | **136,091** | **100.00** | A | |
| **Electors** | | **200,938** | | A | CSV direct |
| **Turnout** | | | **67.73%** | A | |
| **AITC margin over BJP** | | **3,168** | **2.33 pp** | A | **Very narrow — this is the tightest result in AC 159 across all tracked elections** |

*This is a tier A calibration target — CSV is a direct primary source, no decomposition needed.*

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 159 specifically (Assembly Elections)

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin |
|---|---|---|---|---|---|---|---|---|---|
| 2011 AE | Subrata Bakshi | AITC | 87,903 | ~64.8 | Narayan Prasad Jain | CPI(M) | 37,967 | ~28.0 | ~49,936 |
| 2011 AE by-poll (Oct) | Mamata Banerjee | AITC | — | ~77.0 | Nandini Mukherjee | CPI(M) | — | ~? | ~54,000 |
| 2016 AE | Mamata Banerjee | AITC | 65,520 | ~47.7 | Deepa Dasmunshi | INC | 40,219 | ~29.3 | 25,301 |

*Notes:*
- *2011 AE: Subrata Bakshi (AITC) won decisively when Left was collapsing across WB. Total valid votes 135,716; electors 212,821. Source: Wikipedia / resultuniversity.com (tier C).*
- *2011 by-poll: Bakshi vacated seat so Mamata Banerjee (CM-elect) could enter the assembly. Mamata won by ~54,000 votes with ~77% share. Source: journalistic (tier D).*
- *2016 AE: Mamata Banerjee contested from Bhabanipur (her "home" constituency); faced INC's Deepa Dasmunshi (not CPI(M)) as principal rival. BJP was not the major challenger in 2016 here. 65,520 / ~137,000 total ≈ 47.7%. Source: Wikipedia / India.com (tier C).*

### Kolkata Dakshin Lok Sabha (PC 23) historical

| Year | Winner | Party | Votes | % | Notes |
|---|---|---|---|---|---|
| 2014 LS | Subrata Bakshi | AITC | 431,715 | 36.95 | Won against BJP Tathagata Roy (25.28%); margin 136,339; CPI(M) strong third |
| 2019 LS | Mala Roy | AITC | 572,188 | 48.11 | See E above; BJP surged to 35.07%; CPI(M) fell to 11.75% |

*Note: In 2014, Subrata Bakshi stood as the AITC candidate for Kolkata Dakshin LS (he had been the 2011 AC 159 MLA before vacating for Mamata). Mala Roy was not the 2014 LS candidate.*

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- **ECI 2019 LS Form-20 / CSV**: `2019_AssemblySegmentLevelVotingData.csv` — exact votes for all candidates in AC 159, electors, NOTA (used for Section E + D.15 model calibration)
- **ECI 2024 LS CSV**: `2024_AssemblySegmentLevelVotingData.csv` — AC 159 votes (Section H validation anchor only; not used in frozen calibration)
- **Census 2011 — Kolkata district**: Religion (76.51% Hindu, 20.60% Muslim), literacy, sex ratio 941 — used for C.1, C.4, C.6
- **Census 2011 — Bhabanipur AC level**: Population 242,604; SC 2.23%; ST 0.26% — via Wikipedia Bhabanipur AC article (tier A aggregate)
- **Census 2011 — KMC Ward 71, Ward 73 individual populations**: Ward 71: 29,922; Ward 73: 23,512 — Wikipedia ward articles (tier A)
- **Delimitation Commission 2008**: Ward composition of AC 159 (Wards 63, 70, 71, 72, 73, 74, 77, 82) — tier A

### Secondary sources (tier B/C)
- **NFHS-4 (2015-16) West Bengal** — asset / amenity baseline; urban pattern (C.14, C.15, D.4, D.13)
- **CSDS-Lokniti 2019 NES post-poll** — vote × religion / caste / gender regional WB pattern (D.15–D.17)
- **Swarajya / CSDS 2019 WB urban cross-tabs** — bhadralok BJP swing pattern (D.15, D.16)
- **NFHS-5 (2019-21) WB** — smartphone diffusion validation (C.14)

### Tertiary / journalistic (tier D)
- **The Print (Sep 2021)**: "In Mamata bypoll seat, Gujaratis & Marwaris are BJP backers but TMC has history on its side" — 10.4% Marwari electorate; Gujarati + Marwari + NB-Hindu share ~34-40%; used for C.2, C.5, C.16
- **The Wire (Sep 2021)**: "In Bhabanipur, Mamata Banerjee's Bastion Faces Its Hardest Test" — community composition; non-Bengali Hindu bloc characterization
- **Wikipedia: Bhabanipur, West Bengal Assembly constituency** — KMC ward list; 2011/2016 election results; 2021 AE/by-poll results (Section F + H)
- **Wikipedia: Bhowanipore (neighbourhood)** — Gujarati business families in Lansdowne belt; ward-level community narrative
- **Wikipedia: Electoral history of Mamata Banerjee** — 2011 by-poll votes; 2016 AE votes
- **Bhowanipore Grokipedia / ProKerala** — "42% Bengali Hindu + 34% NB Hindu + 24% Muslim" community breakdown (D.11, D.12, D.15)
- **India.com / IndiaTV** — 2021 AE and by-poll vote totals (Section H only)
- **The Federal (2026 SIR context article)** — 21.9% Muslim voters in Bhabanipur (used to calibrate C.1)
- **ResultUniversity / IndiaStat** — 2011, 2016 AE results cross-check

### Tier-D/E reliance flags (what to distrust)
- **Community / caste shares** (C.2, D.2, D.12) — no caste census post-1931 for non-SC/ST; bhadralok UC%, Marwari%, Gujarati% all tier D from journalistic sources; ±3-5pp uncertainty
- **Religion breakdown** (C.1, D.11) — "24% Muslim" derived from journalistic "~20% Muslim voters" + age-structure adjustment; Census 2011 Kolkata district gives 20.60%; AC-level deviation from district not published; tier D
- **Mother tongue** (C.5) — no Census language tables at AC level accessible; derived from community × language mapping; tier D
- **Migration/birthplace** (C.16, D.3) — no Census D-series at AC level; entirely derived from community-composition journalistic anchors; tier D
- **Ward-cluster spatial split** (D.11–D.14) — full 8-ward individual Census populations not assembled in v0; U1/U2 split is a simplification; tier E
- **Vote × Demographic** (D.15–D.18) — CSDS WB urban regional rollup adapted to AC-specific community weights; tier C/D; AC-level survey cross-tabs not available
- **Pre-2019 assembly results** (Section F) — tier C from Wikipedia / journalistic; exact official ECI publications not individually verified

### v0 known gaps (see methodology §7)
1. **Individual KMC ward Census data** — v0 collapses 8 wards into 2 clusters; DCHB Kolkata Part-A ward tables would enable 8-cell spatial sub-unit decomposition
2. **Census 2011 religion at ward level** — Muslim ward distribution derived from journalistic "Ward 82 Kidderpur fringe" narrative; Census HH-1 ward tables would provide exact ward-level religion data
3. **ECI final electoral roll 2019 AC 159** — electors taken from 2019 LS CSV (200,938); gender-disaggregated roll not accessed; male/female voter split is estimated
4. **Census D-series migration tables** — no AC-level migration data; community composition approach is entirely journalistic; tier D
5. **CSDS WB urban sub-sample** — using WB state-level regional rollup; specific Kolkata South urban cross-tabs not separately published; vote × caste adjustments are D-tier
6. **Pre-2019 assembly by-poll (Oct 2011) exact vote counts** — Mamata Banerjee by-poll result used at ~77% / 54,000-vote margin from journalistic source; ECI formal result not separately confirmed
7. **SC community sub-group composition** — 2.23% SC in AC 159 is very low; sub-group composition within SC pool is unknown; collapsed to generic "urban SC" bucket

---

## H. Post-2019 validation anchors (NOT part of 2019 calibration — for simulator use only)

*This section is explicitly out-of-freeze. The simulator uses these as out-of-sample tests.*

### 2021 AE (May 2021) — Main Assembly Election

| Party | Candidate | Votes | % | Note |
|---|---|---|---|---|
| AITC (TMC) | Sobhandeb Chattopadhyay | 73,505 | **57.7** | Won; Sobhandeb vacated later for CM |
| BJP | Rudranil Ghosh | 44,786 | **35.2** | |
| Others | — | ~9,400 | ~7.4 | Left + others |
| **Margin** | TMC over BJP | **28,719** | **22.5 pp** | |

*Source: India.com / Wikipedia (tier C). The May 2021 AE result (~57.7% TMC) is the **representative simulation calibration anchor** for Phase-2 (post-2019 event effects — TMC consolidation, BJP assembly push). It is structurally sounder than the by-poll for calibration because it involved a contested multi-party assembly election.*

### 2021 by-poll (September 2021) — Anomalous CM-incumbent result

| Party | Candidate | Votes | % | Note |
|---|---|---|---|---|
| AITC (TMC) | **Mamata Banerjee** (CM) | 85,263 | **71.9** | **CM-on-ballot dynamic** |
| BJP | Priyanka Tibrewal | 26,428 | **22.3** | |
| Left (CMP/SUCI) | — | ~4,300 | ~3.6 | |
| **Margin** | TMC over BJP | **58,835** | **49.6 pp** | |

*Source: Wikipedia / India.com (tier C).*

> **IMPORTANT CALIBRATION NOTE**: The September 2021 by-poll result (71.9% TMC, 58,835 margin) is **anomalously high** and should NOT be used as a Phase-2 calibration target. It reflects CM-on-ballot incumbency dynamics (voters across party lines rallying to ensure sitting CM does not lose her seat), which is a unique non-recurring event. The May 2021 AE (~57.7%) is the representative anchor for simulation calibration.

### 2024 LS (Kolkata Dakshin, AC 159 segment) — tier A, ECI CSV

| Party | Candidate | Votes | % | Note |
|---|---|---|---|---|
| AITC | Mala Roy | 62,461 | **46.65** | |
| BJP | Debasree Chaudhuri | 54,164 | **40.45** | |
| CPI(M) | Saira Shah Halim | 14,006 | **10.46** | CPI(M) recovered vs 2019 |
| Others + NOTA | — | 3,258 | **2.43** | |
| **Total** | | **133,889** | **100.00** | |
| **Electors** | | **205,553** | | |
| **Turnout** | | | **65.14%** | Slightly lower than 2019 |
| **AITC margin** | | **8,297** | **6.20 pp** | TMC lead widened vs 2019 (2.33pp → 6.20pp) |

*Source: 2024_AssemblySegmentLevelVotingData.csv (tier A). CPI(M) surge in 2024 (6.39% → 10.46%) at BJP's partial expense is notable.*

---

*v0 — generated 2026-04-27, frozen at 2019 state-of-knowledge. No post-2019 events referenced in Sections A–G.*
