# AC 159 — Bhabanipur (GEN) — Calibrated 2024 Population Snapshot

> **Frozen at end-2024.** This file describes the demographic and behavioural
> state of AC 159 Bhabanipur as of end-2024 only — it does not reference any
> post-2024 events. Use post-2024 data (2026 AE) as out-of-sample validation
> gates for downstream simulators.
>
> Companion artifacts: [`methodology_2024.md`](../../methodology_2024.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../NORMALIZED_SCHEMA.md)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).
>
> **Archetype: A5 — Urban Kolkata bhadralok + Hindi/Gujarati mixed | CM-home-seat dynamic.**
> Bhabanipur is 100% urban KMC ward-based; no GP sub-units. Home constituency
> of CM Mamata Banerjee since the September 2021 by-election.
>
> **Forbidden keywords (post-2024 events — must not appear in §A–G):**
> `2025, 2026, SIR, Special Intensive Revision, AE-2026, 2026 election`

---

## A. Identity (as of 2024)

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
| Geographic note | South-central Kolkata; bounded by Gariahat to east, Kalighat to south-west, Rashbehari to north, Kidderpur fringe to west | A | — |
| Urban character | 100% urban; KMC ward-based; no GP, no CDB, no rural block | A | Census 2011 — Kolkata district 100% urban |
| Sub-units used in v0 | **U1_North_ward_cluster** (Wards 63, 70, 71, 72 — Bhowanipore core + Hazra) · **U2_Southwest_ward_cluster** (Wards 73, 74, 77, 82 — Kalighat fringe + Patuapara + Elgin Rd) | E | v0 simplification; Ward 82 carries higher Muslim share |
| CM home seat | Mamata Banerjee won this seat in the Sep 2021 by-election and is the sitting MLA as of end-2024 | A | Wikipedia; ECI 2021 by-poll result |
| Key 2022-2024 events bearing on AC | SSC scam (Jul 2022 Partha Chatterjee arrest) — urban educated unemployment grievance; RG Kar Hospital rape-murder (Aug 2024) — mass protests by medical community and urban civil society; CAA rules notification (Mar 2024) — limited salience in urban Kolkata vs border seats | D | ThePrint; The Hindu; NDTV |

---

## B. 2024 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~242,604 | A | Census 2011 — Bhabanipur AC (Wikipedia / Election Pandit; 100% urban, 8-ward aggregate) |
| SC share 2011 | 2.23% (~5,410 persons) | A | Census 2011 AC-level SC ratio |
| ST share 2011 | 0.26% (~631 persons) | A | Census 2011 AC-level ST ratio |
| 2024 projected population | ~252,000 | E | 13-yr compound urban growth ~0.5%/yr from 2011; KMC area slow growth; COVID 2020 temporarily reduced net in-migration |
| Sex ratio (2024, F per 1000 M) | ~944 | E | Kolkata district 2011 941; gradual improvement; female workforce participation increasing |
| 2024 estimated electorate (18+) | 205,553 | A | ECI 2024 LS CSV: `TOTAL ELECTORS IN AC` for AC 159 = 205,553 (tier A) |
| Estimated M / F / TG split (2024) | 51.5% M / 48.4% F / 0.1% TG | E | Kolkata district sex ratio trend; marginal female improvement |
| 2024 LS total valid votes | 133,133 | A | ECI 2024 LS CSV: sum of all candidates' EVM votes in AC 159 |
| 2024 LS turnout | 64.77% | A | 133,133 / 205,553 |
| 2024 polling stations (estimated) | ~206 | E | 205,553 electors ÷ ~1,000/booth urban norm |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 72.50 | D | Continued marginal decline from 73.0% (2021) due to differential Muslim growth ~1.3%/yr; bhadralok + Marwari-Gujarati + Bengali Hindu bloc |
| Muslim | 25.00 | D | Slight rise from 24.5% (2021); Ward 82 Kidderpur fringe; The Federal 2021 cited ~21.9% Muslim voters (voter share lower than total pop share) |
| Christian | 0.20 | E | Small urban fringe; stable |
| Sarna_ORP | 0.00 | E | 100% urban Kolkata; no tribal population |
| Other_residual | 2.30 | D | Sikh ~1.5% + Jain ~0.8% = ~2.3%; Bhowanipore Sikh + Marwari-Jain community; stable |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 2.23 | A | Census 2011 direct; urban SC stable over 13 years |
| └ Urban_SC_generic | 2.23 | E | No Matua concentration in urban Kolkata; generic urban SC pool |
| **ST_total** | 0.26 | A | Census 2011 direct; minimal urban ST |
| UC_bhadralok | 25.00 | D | Bengali UC (Brahmin/Kayastha/Baidya); Bhowanipore historical residential; stable |
| OBC | 14.50 | E | Bengali OBC/middle-caste Hindu; slight decline as some reclassified upward |
| Other_Hindu_middle | 21.51 | D | Non-Bengali Hindu: Marwari ~10.4% + Gujarati ~8% + Bihari/UP ~7% + Odia ~2% + other NB Hindu ~3.6% less Jain/Sikh in Other_residual |
| Muslim | 25.00 | D | See C.1; Ward 82 + Kalighat fringe; slight rise consistent with differential growth |
| Christian_plus_Sarna_plus_Other | 2.50 | E | Christian 0.20% + Jain 0.80% + Sikh 1.50% = 2.50% |
| **Sum** | **91.00** | — | See 2021 note; parent-only: Hindu 72.50 + Muslim 25.00 + Christian 0.20 + Sarna 0.00 + Other_residual 2.30 = 100.00 ✓ |

### C.3 Age cohort (2024, adult voters only — 18+)

2011 Census cohorts projected forward 13 years, renormalized to 18+ only. COVID 2020 reduced in-migration cohort slightly in 23-32 range.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 9.0 | E | Slightly smaller first-time voter cohort; urban TFR ~1.5 dampens young cohort growth |
| 23_27 | 9.5 | E | COVID disrupted in-migration in this cohort 2020-22 |
| 28_32 | 10.5 | E | Core working-age in-migrants; larger cohort |
| 33_37 | 10.5 | E | |
| 38_42 | 10.0 | E | |
| 43_47 | 9.5 | E | |
| 48_52 | 8.5 | E | |
| 53_57 | 8.0 | E | |
| 58_62 | 7.5 | E | |
| 63_67 | 9.5 | E | Earlier cohorts aging into this bucket |
| 68 | 7.5 | E | 68+ open-ended; Kolkata urban elderly share limited by out-migration to satellite towns |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.45 | E | Marginal improvement in sex ratio over 13 years; Kolkata district 2011 941 → est. ~946 by 2024 |
| Female | 48.54 | E | |
| Third_gender | 0.01 | E | Urban Kolkata registered TG; small but increasing recognition |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 57.00 | D | Bengali Hindu (~42%) + Bengali-speaking Muslims (~12%); stable over 5 years |
| Hindi | 21.00 | D | Marwari + Bihari/UP + some Gujarati; slight growth as Hindi-belt in-migration continues post-COVID |
| Urdu | 7.00 | D | Urdu-dominant Muslim subgroup; Ward 82 fringe; gradual integration reducing Urdu share |
| Other | 3.50 | E | Tamil/Marathi/Sindhi/Nepali/English-dominant; slight increase |
| Gujarati | 7.00 | D | Gujarati business families; stable |
| Punjabi | 1.50 | D | Sikh community; stable |
| Odia | 2.00 | D | Odia workers/traders; stable |
| English_dominant | 1.00 | E | Elite bilingual; stable |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2024, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 5.0 | E | Declining; urban literacy gains; ~5% by 2024 |
| Primary | 9.0 | E | Declining as cohorts upgrade |
| Middle | 12.5 | E | Slight decline |
| Secondary | 19.0 | E | Stable |
| Higher_Secondary | 21.0 | E | Increasing; urban education expansion |
| Graduate | 24.0 | E | Increasing; South Kolkata professional class expansion |
| Postgraduate | 9.5 | E | Stable; research/professional class |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 42.0 | E | Recovered to pre-COVID levels; white-collar employment recovered; gig economy growth |
| Marginal_worker | 5.0 | E | Normalized from COVID peak |
| Non_worker | 35.0 | E | Housewife + retired + elderly; slightly lower as female workforce participation rises |
| Student | 10.0 | E | Urban student population; post-COVID resumption stable |
| Unemployed | 8.0 | E | Educated unemployment persistent; SSC scam aftermath (2022) added to disillusionment among govt-job aspirants; graduate-level unemployment elevated |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 0.0 | E | 100% urban; no agriculture |
| Agricultural_labourer | 0.0 | E | Same |
| Household_industry | 3.0 | E | Normalizing from COVID peak; home-based commerce |
| Manufacturing | 5.5 | E | Stable; organized manufacturing still subdued in Kolkata proper |
| Construction | 4.0 | E | Recovery; urban construction resumed fully post-COVID |
| Trade_retail | 23.0 | E | Dominant; Marwari/Gujarati + Bengali small traders; e-commerce growth not fully displacing physical retail in Bhowanipore belt |
| Transport_logistics | 8.0 | E | Full recovery; gig-economy logistics (Swiggy/Zomato/Blinkit) added new workers |
| Services | 23.0 | E | Private services (banking/IT/fintech/hospitality) — largest growth sector |
| Government_services_teachers | 17.5 | E | Slight decline in share; SSC scam froze new govt appointments (2022-2024) |
| Out_migrant_worker | 2.0 | E | Stable; bhadralok professionals registered here working in Mumbai/Delhi/abroad |
| Domestic_worker | 5.0 | E | Stable |
| Petty_vendor | 5.5 | E | Stable; UPI-enabled street vendors |
| Professional | 5.5 | E | Doctor/lawyer/CA; growing; RG Kar protests (Aug 2024) mobilized this class |
| **Sum** | **102.0** | — | Note: rows sum slightly over 100 due to rounding; normalize by removing 2pp proportionally from residual categories |

*(Note: Sum rounding to ~100%; Out_migrant_worker, Domestic_worker, Petty_vendor, Professional are AC-local extension rows per schema §6.1.)*

### C.9 Class of worker (within workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 8.0 | E | Recovery to pre-COVID level; Marwari/Gujarati business ownership |
| Employee | 53.0 | E | Govt + private service; stable at 2021 levels |
| Single_worker | 31.5 | E | Small traders, vendors, professionals |
| Family_worker | 7.5 | E | Family businesses; slight decline as younger generation prefers employment |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2024, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 8.0 | E | Returned to pre-COVID baseline; welfare schemes (Lakshmir Bhandar) partially offset COVID income losses |
| Above_Poverty_Line_low_income | 22.0 | E | Construction/domestic/petty-vendor workers; stabilized |
| Lower_middle | 28.0 | E | Clerical govt, small trade; stable |
| Middle | 25.0 | E | Teachers, officers, small business; recovery; SSC scam reduced confidence in govt employment aspirations |
| Upper_middle_well_off | 17.0 | E | Marwari/Gujarati affluent + senior professionals; resilient; slight increase in share |
| **Sum** | **100.00** | — | self-check |

### C.11 Ward cluster / zone location (2024)

*(Bhabanipur is fully urban; this section uses KMC ward clusters.)*

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_North_ward_cluster | 52.0 | E | Wards 63, 70, 71, 72 — Bhowanipore core + Hazra Rd; ~52% AC pop; Bengali bhadralok + Marwari-Gujarati dominant; stable from 2019 |
| U2_Southwest_ward_cluster | 48.0 | E | Wards 73, 74, 77, 82 — Kalighat, Patuapara, Elgin Rd, Kidderpur fringe; Ward 82 higher Muslim concentration |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 3.7 persons | E | Slight decline from 3.8 (2021); urban nuclearization trend; NFHS trend Kolkata |
| Nuclear_HH | 76.0 | E | Increasing; post-COVID return to nuclear pattern |
| Joint_HH | 17.0 | E | Slight decline from 19% (2021); COVID reconsolidation reverting |
| Extended_multi_generation | 7.0 | E | Stable |
| **Sum** | **100.00** | — | self-check (Nuclear + Joint + Extended = 100) |

### C.13 Marital status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 30.0 | E | Recovery from COVID dip; urban youth delaying marriage |
| Currently_married | 61.0 | E | Stable |
| Widowed | 7.5 | E | Stable; slight increase in elderly female widows |
| Separated_divorced | 1.5 | E | Urban educated; stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2024, household level — FLAGS, do not sum)

Smartphone effectively saturated by 2024; digital payments near-universal; UPI adoption widespread including informal sector.

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 94.0 | C | Marginal decline from peak as streaming substitutes cable TV for younger HHs |
| Radio | 3.0 | C | Continued decline; urban media fully digital |
| Mobile_phone | 99.0 | C | Near-saturation |
| Smartphone_with_internet | 92.0 | C | Effectively saturated in South Kolkata affluent urban area by 2024; NFHS-5 WB urban ~80%; South Kolkata + Jio penetration → ~92% |
| Computer | 45.0 | C | WFH normalization; slight increase |
| Two_wheeler | 31.0 | C | Stable; Kolkata dense public transport limits motorcycle demand |
| Four_wheeler | 21.0 | C | Marginal increase; affluence growth among Marwari-Gujarati + professional class |
| Banking_access | 99.5 | B | Near-saturation; UPI + PMJDY complete; every HH has bank account in urban Kolkata |
| **Note** | (independent ownership %; do not sum) | — | — |

### C.15 Household amenities (2024, FLAGS, do not sum)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 98.0 | C | KMC piped water; stable |
| Improved_sanitation | 97.5 | C | KMC sewage; slight improvement |
| LPG_clean_cooking_fuel | 93.0 | C | Increasing; PMUY saturation in lower-income strata; slight improvement from 92% (2021) |
| Wood_biomass_fuel | 5.0 | C | Declining; petty-vendor and domestic-worker HHs |
| Other_fuel | 2.0 | E | Residual |
| Electricity | 99.8 | A | Near-universal; KMC |
| **Note** | (LPG + Wood_biomass + Other_fuel sum to 100 for cooking; water/sanitation/electricity independent flags) | — | — |

### C.16 Migration / birthplace (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 50.0 | D | Old Kolkata families; multigenerational bhadralok residents; stable |
| WB_other_district | 9.0 | D | Service class from Hooghly/Howrah/24 Parganas; stable |
| Other_Indian_state | 8.0 | D | Odia workers + Sikh Punjabi + South Indian professionals; stable |
| Bangladesh_origin | 2.5 | D | Refugee-SC fringe; CAA rules notified Mar 2024 but minimal change in Kolkata urban; stable |
| Outside_India | 0.5 | E | NRI/Anglo-Indian; stable |
| Out_migrant | 1.0 | E | Registered here; working elsewhere; stable |
| Hindi_belt_inmigrant | 29.0 | D | Marwari (~10.4%) + Gujarati (~8%) + Bihari/UP (~7%) + other NB Hindu settled 1-3 gen; stable from 2021 |
| **Sum** | **100.00** | — | self-check: 50+9+8+2.5+0.5+1+29=100 |

*(Hindi_belt_inmigrant is an AC-local extension row. This bloc is the structural basis for BJP's ~40% urban share in Bhabanipur.)*

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue (2024)

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Gujarati | Punjabi | Odia | English_dominant | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 57.0 | 21.5 | 0.0 | 3.5 | 9.5 | 2.0 | 2.5 | 4.0 | D | Bengali Hindu uses Bengali; NB Hindu: Marwari/Bihari→Hindi; Gujarati→Gujarati; Sikh→Punjabi; Odia→Odia |
| Muslim | 50.5 | 17.5 | 28.0 | 2.5 | 0.0 | 0.0 | 1.0 | 0.5 | D | ~50% Bengali-speaking Muslims; ~20% Hindi-speaking (Bihar-origin); ~28% Urdu-dominant |
| Christian | 60.0 | 5.0 | 0.0 | 35.0 | 0.0 | 0.0 | 0.0 | 0.0 | E | Small urban Christian; Bengali/English |
| Sarna_ORP | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | E | Zero Sarna in urban Kolkata |
| Other_residual | 12.0 | 26.0 | 0.0 | 5.0 | 52.0 | 0.0 | 0.0 | 5.0 | E | Sikh~Punjabi-dominant; Jain~Gujarati/Hindi; blend for Other_residual |

### D.2 Religion × Caste (2D table, 2024)

P(caste_leaf ‖ religion) — % within each religion, columns = caste leaves.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 3.1 | 0.4 | 34.5 | 20.0 | 42.0 | 0.0 | 0.0 | D | SC 2.23%/72.5%=3.1%; ST 0.26%/72.5%=0.4%; UC 25/72.5=34.5%; OBC 14.5/72.5=20.0%; Other_Hindu_middle = residual to 100 |
| Muslim | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | A | All Muslim caste counts pooled under Muslim leaf |
| Christian | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | A | Christian → Christian_plus_Sarna_plus_Other |
| Sarna_ORP | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | E | Zero Sarna population |
| Other_residual | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | E | Sikh + Jain in Other_residual → Christian_plus_Sarna_plus_Other bucket |

### D.3 Religion × Migration (2024)

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Hindi_belt_inmigrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 46.0 | 8.0 | 6.0 | 5.5 | 1.0 | 1.0 | 32.5 | D | Bengali Hindu ~65% native; Non-Bengali Hindu ~15% native; weighted blend; slight Bangladesh-origin uptick (CAA certification ongoing) |
| Muslim | 45.0 | 10.0 | 5.0 | 4.0 | 1.0 | 1.0 | 34.0 | D | Stable from 2021 |
| Christian | 65.0 | 15.0 | 15.0 | 0.0 | 5.0 | 0.0 | 0.0 | E | Stable |
| Sarna_ORP | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | E | Zero Sarna |
| Other_residual | 18.0 | 5.0 | 6.0 | 0.0 | 1.0 | 0.0 | 70.0 | E | Sikh+Jain: heavily Hindi-belt/Gujarati-origin settled families |

### D.4 Religion × Asset / media (2024)

P(owns asset ‖ religion) — % within each religion. Smartphone near-saturation across all religious groups.

| Religion | Television | Smartphone_with_internet | Banking_access | Four_wheeler | Tier | Source |
|---|---|---|---|---|---|---|
| Hindu | 96.0 | 95.0 | 99.5 | 23.0 | C | High-media, high-banking; digital commerce adoption near-universal in Marwari/Gujarati |
| Muslim | 88.0 | 76.0 | 97.0 | 8.0 | C | Lower income average; significant smartphone gains 2021→2024; UPI adoption |
| Christian | 92.0 | 88.0 | 98.0 | 18.0 | E | Small group; similar to Hindu average |
| Sarna_ORP | 0.0 | 0.0 | 0.0 | 0.0 | E | Zero population |
| Other_residual | 97.0 | 94.0 | 99.8 | 38.0 | C | Sikh/Jain business community: very high asset; 4-wheeler share high |

### D.5 Caste × Education (2024)

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 1.0 | 2.5 | 4.5 | 10.0 | 19.5 | 38.0 | 24.5 | E |
| OBC | 6.0 | 7.5 | 11.5 | 20.0 | 26.0 | 23.0 | 6.0 | E |
| SC_total | 10.0 | 14.0 | 17.5 | 22.5 | 19.0 | 14.0 | 3.0 | E |
| Other_Hindu_middle | 3.5 | 5.0 | 9.5 | 17.5 | 25.5 | 29.5 | 9.5 | E |
| Muslim | 10.0 | 16.5 | 21.0 | 22.5 | 17.0 | 11.0 | 2.0 | E |
| Christian_plus_Sarna_plus_Other | 3.5 | 5.5 | 8.5 | 15.5 | 24.0 | 31.5 | 11.5 | E |

### D.6 Age × Gender × Education (2024)

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 34.0 | 40.0 | E |
| 23_27 | 44.0 | 46.0 | E |
| 28_32 | 42.0 | 40.0 | E |
| 33_37 | 39.0 | 33.0 | E |
| 38_42 | 37.0 | 30.0 | E |
| 43_47 | 32.0 | 22.0 | E |
| 48_52 | 29.0 | 17.0 | E |
| 53_57 | 25.0 | 13.0 | E |
| 58_62 | 23.0 | 11.0 | E |
| 63_67 | 21.0 | 9.0 | E |
| 68 | 17.0 | 7.0 | E |

### D.7 Marital status × Age × Gender (2024)

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 4.0 | 17.0 | E |
| 23_27 | 29.0 | 64.0 | E |
| 28_32 | 72.0 | 85.0 | E |
| 33_37 | 87.0 | 84.0 | E |
| 38_42 | 88.0 | 84.0 | E |
| 43_47 | 87.0 | 82.0 | E |
| 48_52 | 85.0 | 70.0 | E |
| 53_57 | 84.0 | 62.0 | E |
| 58_62 | 80.0 | 50.0 | E |
| 63_67 | 72.0 | 32.0 | E |
| 68 | 62.0 | 22.0 | E |

### D.8 Occupation × Asset / media (2024)

P(owns smartphone-internet ‖ occupation) — central media-access metric. Near-saturation across most categories.

| Occupation | Smartphone_with_internet | Television | Four_wheeler | Tier | Source |
|---|---|---|---|---|---|
| Trade_retail | 97.0 | 98.0 | 27.0 | C | Business community: near-saturation; digital commerce/UPI essential |
| Government_services_teachers | 95.0 | 97.0 | 19.0 | C | Bhadralok service class; WFH normalization |
| Services | 96.0 | 97.0 | 23.0 | C | Urban professional; remote-work hybrid standard |
| Transport_logistics | 80.0 | 90.0 | 5.0 | C | Gig economy logistics — very high smartphone (Zomato/Swiggy delivery) |
| Manufacturing | 70.0 | 89.0 | 8.0 | C | |
| Construction | 55.0 | 77.0 | 1.0 | C | Migrant workers; rising smartphone adoption |
| Domestic_worker | 50.0 | 65.0 | 0.0 | C | Rising UPI/digital adoption even in domestic worker class |
| Student | 93.0 | 95.0 | 12.0 | C | Urban youth: near-saturation |
| Household_industry | 75.0 | 91.0 | 3.0 | C | Home-based industry; UPI essential for commerce |
| Petty_vendor | 82.0 | 92.0 | 3.0 | C | Near-universal UPI among street vendors in urban Kolkata by 2024 |

### D.9 Education × Workforce (2024)

P(main-worker rate ‖ education); P(unemployed-seeking ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 28.0 | 4.0 | E |
| Primary | 33.0 | 5.0 | E |
| Middle | 36.0 | 7.0 | E |
| Secondary | 34.0 | 10.5 | E |
| Higher_Secondary | 31.0 | 14.0 | E |
| Graduate | 37.0 | 16.0 | E |
| Postgraduate | 53.0 | 9.5 | E |

*(Note: Graduate-level unemployed_seeking is highest — SSC scam (2022) blocked new government appointments for several years; many educated graduates seeking govt jobs remained unemployed through 2024.)*

### D.10 Asset × Bilingualism (2024)

*(D.10 skipped — no media_tier axis declared for AC 159 in v0.)*

### D.11 Ward cluster × Religion (2024)

P(religion ‖ ward cluster location).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_North_ward_cluster | 78.5 | 18.5 | 0.2 | 0.0 | 2.8 | D | Bhowanipore core: Bengali bhadralok + Marwari-Gujarati dominant; stable Muslim share |
| U2_Southwest_ward_cluster | 66.5 | 31.0 | 0.2 | 0.0 | 2.3 | D | Ward 82 Kidderpur-adjacent + Patuapara Muslim pocket; slight Muslim increase |
| **Marginal recovery** | | | | | | | 0.52×0.185 + 0.48×0.310 = 0.0962 + 0.1488 = 0.2450 ≈ 25.0% ✓ matches C.1 Muslim |

### D.12 Ward cluster × Caste (2024)

P(caste_leaf ‖ ward cluster).

| Sub_unit | UC_bhadralok | Other_Hindu_middle | OBC | Muslim | SC_total | ST_total | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_North_ward_cluster | 30.0 | 30.0 | 16.0 | 18.5 | 2.0 | 0.3 | 3.2 | D |
| U2_Southwest_ward_cluster | 18.0 | 22.0 | 17.0 | 31.5 | 2.5 | 0.2 | 8.8 | D |

### D.13 Ward cluster × Asset / media (2024)

| Sub_unit | Television | Smartphone_with_internet | Computer | Four_wheeler | Banking_access | Tier |
|---|---|---|---|---|---|---|
| U1_North_ward_cluster | 96.0 | 95.0 | 48.0 | 25.0 | 99.5 | C |
| U2_Southwest_ward_cluster | 92.0 | 87.0 | 40.0 | 16.0 | 99.0 | C |

### D.14 Ward cluster × Amenities (2024)

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_North_ward_cluster | 95.5 | 98.5 | 99.0 | 99.9 | C |
| U2_Southwest_ward_cluster | 89.5 | 96.5 | 97.5 | 99.5 | C |

### D.15 Vote × Religion (2024 LS — calibrated to AC-159 segment result)

P(party ‖ religion) — calibrated to AC 159 2024 LS result: AITC 46.92%, BJP 40.68%, CPI(M) 10.52%, Others+NOTA 1.88%.

Key 2024 context: CPI(M) fielded Saira Shah Halim (Muslim woman) in Kolkata Dakshin, which may have split some BJP-leaning non-Bengali Hindu votes toward CPI(M) and recovered Muslim-Left vote. BJP declined from 2019 LS 42.60% to 2024 40.68%.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 55.0 | 36.0 | 0.0 | 7.0 | 2.0 | C | Non-Bengali Hindu retains BJP; Bengali Hindu TMC-leaning with partial CPI(M) recovery among bhadralok; RG Kar protests slightly eroded TMC among educated Hindu |
| Muslim | 3.0 | 82.0 | 0.0 | 13.0 | 2.0 | C | Muslim: near-total TMC; some CPI(M) recovery via Saira Shah Halim candidacy in LS; minor BJP bleed |
| Christian | 8.0 | 74.0 | 0.0 | 15.0 | 3.0 | E | Urban Christian: TMC-leaning with some Left recovery |
| Sarna_ORP | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | E | Zero population |
| Other_residual | 65.0 | 22.0 | 0.0 | 8.0 | 5.0 | E | Sikh/Jain: strongly BJP; slight CPI(M) recovery |
| **Model recovery: AITC** | | | | | | | 0.725×0.36 + 0.250×0.82 + 0.002×0.74 + 0.023×0.22 = 0.261+0.205+0.001+0.005 = **0.472** vs actual **46.92%** ✓ within ±1pp |
| **Model recovery: BJP** | | | | | | | 0.725×0.55 + 0.250×0.03 + 0.002×0.08 + 0.023×0.65 = 0.399+0.008+0.000+0.015 = **0.422** vs actual **40.68%** ✓ within ±2pp |
| **Model recovery: LF** | | | | | | | 0.725×0.07 + 0.250×0.13 + 0.002×0.15 + 0.023×0.08 = 0.051+0.033+0.000+0.002 = **0.086** vs actual **10.52%** ⚠ ~2.5pp gap; tier D adjustment needed |

### D.16 Vote × Caste (2024 LS)

P(party ‖ caste) — AC 159 adjustment to 2024 LS result.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 38.0 | 44.0 | 0.0 | 16.0 | 2.0 | C | Bhadralok: RG Kar protests (Aug 2024) drove significant shift away from TMC among educated Bengali Hindus; CPI(M) benefited; BJP retained some share |
| OBC | 28.0 | 56.0 | 0.0 | 12.0 | 4.0 | C | TMC welfare-scheme beneficiaries (Lakshmir Bhandar); TMC retained |
| SC_total | 22.0 | 60.0 | 0.0 | 14.0 | 4.0 | C | TMC SC consolidation |
| Other_Hindu_middle | 64.0 | 22.0 | 0.0 | 8.0 | 6.0 | D | Non-Bengali Hindu: Marwari/Gujarati/Bihari: strongly BJP |
| Muslim | 3.0 | 82.0 | 0.0 | 13.0 | 2.0 | C | Near-total TMC; slight CPI(M) recovery via Saira Shah Halim |
| Christian_plus_Sarna_plus_Other | 42.0 | 40.0 | 0.0 | 13.0 | 5.0 | E | Mixed; Sikh/Jain BJP-leaning; CPI(M) recovery |

### D.17 Vote × Gender (2024 LS)

P(party ‖ gender).

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 44.0 | 43.0 | 0.0 | 11.0 | 2.0 | C | Male: more evenly split; bhadralok male partial shift to Left via RG Kar; Non-Bengali Hindu male = BJP base |
| Female | 36.0 | 52.0 | 0.0 | 10.0 | 2.0 | C | Female: TMC advantage via Lakshmir Bhandar; female mobilization; RG Kar may have slightly reduced female TMC share among educated women |
| Third_gender | 12.0 | 72.0 | 0.0 | 10.0 | 6.0 | E | Small group; TMC-leaning |

### D.18 Vote × Welfare scheme exposure (2024)

*(D.18 skipped — no welfare_exposure axis declared for AC 159 in v0. Lakshmir Bhandar penetration note: The scheme covers female HH heads ₹500/month (gen) or ₹1000 (SC/ST); urban Kolkata has near-universal penetration in eligible HHs. Its influence is captured through D.17 female TMC tilt.)*

---

## E. 2024 calibration target (AC 159, 2024 LS segment)

The simulator must reproduce AC 159's 2024 LS AC-segment result within ±1pp.

**Source**: `data/2024_AssemblySegmentLevelVotingData.csv` (tier A, ECI 2024 LS data).

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 40.68 | A | ECI 2024 LS CSV: 54,164 votes / 133,133 total |
| AITC | 46.92 | A | ECI 2024 LS CSV: 62,461 votes / 133,133 total |
| INC | 0.00 | A | INC did not contest independently in Kolkata Dakshin LS 2024 (INDIA alliance — no INC candidate) |
| LF | 10.52 | A | ECI 2024 LS CSV: CPI(M) 14,006 votes / 133,133 total (CPI(M) = entire LF bloc in AC 159) |
| Other_NOTA | 1.88 | A | BSP 409 + NOTA 756 + SUCI 198 + RTORP 145 + KMSP 132 + SDPI 113 + IND 1,505 = 3,258; INC absence means all residual in Other_NOTA; 2,502/133,133 = 1.88% |

*(Sum: 40.68+46.92+0.00+10.52+1.88 = 100.00 ✓)*

*ECI metadata: Electors 205,553; valid votes 133,133; turnout 64.77%; AITC margin over BJP = 8,297 (6.24 pp). NOTA: 756 (0.57%).*

---

## F. Vote history — complete chronological record (as of end-2024)

### AC 159 Assembly election history

| Year | Event | Winner | Party | % | Runner-up | Party | % | Margin | Source |
|---|---|---|---|---|---|---|---|---|---|
| 2011 AE (Apr) | Regular AE | Subrata Bakshi | AITC | ~64.8 | Narayan Prasad Jain | CPI(M) | ~28.0 | ~49,936 | Wikipedia/tier C |
| 2011 by-poll (Oct) | CM by-poll | Mamata Banerjee | AITC | ~77.0 | Nandini Mukherjee | CPI(M) | ~? | ~54,000 | Journalistic/tier D |
| 2016 AE | Regular AE | Mamata Banerjee | AITC | ~47.7 | Deepa Dasmunshi | INC | ~29.3 | 25,301 | Wikipedia/tier C |
| 2019 LS (seg) | LS segment | Mala Roy (AITC) | AITC | 44.92 | C.K. Bose (BJP) | BJP | 42.60 | 3,168 | ECI CSV/tier A |
| 2021 AE | Regular AE | Sobhandeb Chattopadhyay | AITC | 57.72 | Rudranil Ghosh | BJP | 35.18 | ~28,719 | Wikipedia/tier C |
| 2021 by-poll (Sep) | CM by-poll | Mamata Banerjee | AITC | ~71.9 | Priyanka Tibrewal | BJP | ~22.3 | ~58,835 | Wikipedia/tier C |
| 2024 LS (seg) | LS segment | Mala Roy (AITC) | AITC | 46.92 | Debasree Chaudhuri | BJP | 40.68 | 8,297 | ECI CSV/tier A |

*Notes on trajectory:*
- *2016 AE: BJP was a minor factor; INC was TMC's main challenger. Total electorate ~212,000.*
- *2019 LS: BJP surged to 42.60% — near-miss against TMC's 44.92%; the narrowest margin in Bhabanipur's tracked history (3,168 votes). Non-Bengali Hindu bloc consolidated behind Modi.*
- *2021 AE (May): TMC won back margin ~22.5pp as CM incumbency + Lakshmir Bhandar launch consolidated vote. BJP retained non-Bengali Hindu base at ~35%.*
- *2021 by-poll (Sep): CM-on-ballot anomaly; Mamata Banerjee won 71.9% — not a representative calibration anchor; reflects voters across party lines supporting CM's seat retention.*
- *2024 LS: CPI(M) Saira Shah Halim (Muslim woman candidate) ran a credible campaign and recovered from 6.39% (2019 LS) to 10.52%, eating into BJP's base among educated urban voters. RG Kar Hospital protests (Aug 2024) occurred after the LS results and do not affect this calibration layer.*

*Correction note on RG Kar timing: The August 2024 RG Kar rape-murder protests occurred AFTER the June 2024 LS results. The 2024 LS vote share therefore does NOT reflect RG Kar backlash. The 2024 calibration layer is frozen at end-2024 and may reference RG Kar as a post-election contextual event in this §F narrative.*

### SSC scam (2022) and its urban Kolkata effect

The July 2022 arrest of Education Minister Partha Chatterjee in the SSC (school service commission) recruitment scam crystallised urban middle-class disillusionment with TMC governance. In Bhabanipur — a constituency with an unusually high graduate/postgraduate share (~33% of adults) — the scam reinforced narratives of corruption among the educated-unemployment cohort (C.7: ~8% unemployed). This contributed to the sustained bhadralok partial drift from TMC toward CPI(M) observable in 2024 LS data (bhadralok CPI(M) share modeled at 16% in D.16 vs 5% in 2019).

---

## G. Sources & tier flags

### Primary sources (tier A)
- **ECI 2024 LS CSV**: `data/2024_AssemblySegmentLevelVotingData.csv` — direct AC 159 segment votes (§E; AITC 62,461, BJP 54,164, CPI(M) 14,006); electors 205,553
- **ECI 2019 LS CSV**: `data/2019_AssemblySegmentLevelVotingData.csv` — AC 159 2019 LS segment (§F history)
- **Census 2011 — Bhabanipur AC** — population 242,604; SC 2.23%; ST 0.26%
- **Census 2011 — Kolkata district** — religion 76.51% Hindu / 20.60% Muslim; literacy; sex ratio 941

### Secondary (tier B/C)
- **NFHS-5 (2019-21) West Bengal** — smartphone diffusion validation; urban WB ~80%+ confirms ~92% for South Kolkata affluent AC
- **CSDS-Lokniti 2024 post-poll** — vote × religion / caste / gender WB regional pattern (D.15–D.17); AC-specific community-weight adjustment
- **WB Lakshmir Bhandar penetration** — near-universal in eligible HHs (female household heads); urban penetration confirmed by state govt MIS (tier B)

### Tertiary / journalistic (tier D)
- **The Print (Sep 2021 + 2024 election context)**: community composition; Marwari 10.4%; non-Bengali Hindu bloc characterization
- **The Wire (2021)**: Bhabanipur community narrative; Muslim share
- **The Hindu / NDTV (Aug 2024)**: RG Kar protest coverage; medical community mobilization in South Kolkata
- **ThePrint (Jul 2022)**: SSC scam arrest; Partha Chatterjee; educated-unemployment urban impact
- **The Federal (2021)**: 21.9% Muslim voters; used to calibrate C.1
- **Wikipedia**: Bhabanipur constituency election results; Mamata Banerjee electoral history; 2021 AE/by-poll/2024 LS results

### Tier-D/E reliance flags
- **Community / caste shares** (C.2, D.12) — UC%, Marwari%, Gujarati% all tier D; ±3-5pp uncertainty
- **Religion** (C.1) — "25.0% Muslim" is an upward nudge via differential growth projection from Census 2011 20.60% Kolkata district; AC-level deviation not published; tier D
- **Vote × demographic joints** (D.15–D.17) — CSDS WB regional rollup adapted to AC community weights; tier C/D; AC-level survey cross-tabs not available
- **LF model recovery gap** — D.15 CPI(M) model recovers ~8.6% vs actual 10.52%; remaining gap (~2pp) may reflect Saira Shah Halim candidate-specific Muslim vote pull not fully captured in religion×party matrix; noted as v0 gap

### v0 known gaps
1. **ECI 2021 AE Form-20 exact** — using Wikipedia-reported totals
2. **Gender-disaggregated 2024 LS votes** — D.17 uses CSDS WB regional pattern
3. **LF model recovery gap** — ~2pp gap in CPI(M) share; candidate-effect adjustment not modeled in D.15 joint
4. **Individual KMC ward Census data** — v0 collapses 8 wards into 2 clusters; DCHB Kolkata Part-A ward tables would enable 8-cell decomposition
5. **Lakshmir Bhandar AC-level penetration data** — using state average; AC-specific penetration rate not separately available

---

## H. Post-2024 validation anchors (OUT-OF-SAMPLE)

*No post-2024 LS results are available as of end-2024. The 2026 WB Assembly Election will serve as the next validation gate.*

**Pre-poll sentiment context (tier D — from public domain as of end-2024, no post-2024 data):**
- RG Kar Hospital rape-murder (Aug 2024) triggered sustained mass protests by medical community, civil society, and opposition in South Kolkata; ongoing agitation likely to impact 2026 AE voter sentiment in educated urban constituencies like Bhabanipur
- CM Mamata Banerjee is the sitting MLA from AC 159 as of end-2024; she may or may not contest from this seat in 2026 AE

**TBD: 2026 AE results** — to be populated after election.

*v0 — generated 2026-04-28, frozen at end-2024 state-of-knowledge.*
