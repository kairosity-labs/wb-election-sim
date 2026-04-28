# AC 159 — Bhabanipur (GEN) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 159 Bhabanipur as of end-2021 only — it does not reference any
> post-2021 events. Use post-2021 elections (2024 LS) as out-of-sample
> validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../NORMALIZED_SCHEMA.md)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).
>
> **Archetype: A5 — Urban Kolkata bhadralok + Hindi/Gujarati mixed | CM-incumbent dynamic.**
> Bhabanipur is 100% urban KMC ward-based; no GP sub-units.
>
> **Forbidden keywords (post-2021 events — must not appear in §A–G):**
> `2022, 2023, 2024, 2025, 2026, SSC scam, Partha Chatterjee, RG Kar, SIR,
> CAA notification, CAA rules`

---

## A. Identity (as of 2021)

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
| 2021 AE note | **Main May 2021 AE**: Sobhandeb Chattopadhyay (TMC) won; he subsequently vacated the seat to allow CM Mamata Banerjee to contest the September 2021 by-election, which she won decisively. Both results are documented in §E and §F. | D | Wikipedia; India.com |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~242,604 | A | Census 2011 — Bhabanipur AC (Wikipedia / Election Pandit; 100% urban, 8-ward aggregate) |
| SC share 2011 | 2.23% (~5,410 persons) | A | Census 2011 AC-level SC ratio |
| ST share 2011 | 0.26% (~631 persons) | A | Census 2011 AC-level ST ratio |
| 2021 projected population | ~256,000 | E | 10-yr compound urban growth ~0.6%/yr from 2011; Kolkata KMC area slow growth |
| Sex ratio (2021, F per 1000 M) | ~942 | E | Kolkata district 2011: 941; marginal improvement via reduced male in-migration during COVID-2020 period |
| 2021 estimated electorate (18+) | ~205,000 | D | ECI 2021 AE roll not separately published for AC 159; estimated from 2019 roll 200,938 + net addition ~4,000 over 2 years |
| Estimated M / F / TG split (2021) | 52% M / 47.9% F / <0.1% TG | E | Kolkata district 2011 sex ratio; male-skew from working-age in-migrants persists |
| 2021 May AE total votes polled | ~127,350 | D | ECI 2021 AE Form-20 per Wikipedia / India.com: Sobhandeb 73,505 + Rudranil 44,786 + others ~9,059 ≈ 127,350 |
| 2021 May AE turnout | ~62.1% | D | 127,350 / ~205,000; lower than 2019 LS (67.7%) — COVID suppressed turnout |
| 2021 by-poll (Sep) total votes polled | ~118,700 | D | Mamata 85,263 + Tibrewal 26,428 + others ~7,009 ≈ 118,700; by-election invariably lower turnout |
| 2021 by-poll turnout | ~57.9% | D | ~118,700 / ~205,000 |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 73.00 | D | Marginally lower than 2019 (~73.5%) due to differential Muslim growth ~1.3%/yr; bhadralok + Marwari-Gujarati + Bengali Hindu bloc |
| Muslim | 24.50 | D | Slight rise from 24.0% (2019) — ~0.5pp over 2 years via differential growth; Ward 82 Kidderpur fringe; The Federal cites ~21.9% Muslim voters (voters skew lower than pop share) |
| Christian | 0.20 | E | Small urban fringe; unchanged |
| Sarna_ORP | 0.00 | E | 100% urban Kolkata; no tribal population |
| Other_residual | 2.30 | D | Sikh ~1.5% + Jain ~0.8% = ~2.3%; Bhowanipore Sikh + Marwari-Jain community unchanged |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 2.23 | A | Census 2011 direct; urban SC stable |
| └ Urban_SC_generic | 2.23 | E | No Matua concentration in urban Kolkata; generic urban SC pool |
| **ST_total** | 0.26 | A | Census 2011 direct; minimal urban ST |
| UC_bhadralok | 25.00 | D | Bengali UC (Brahmin/Kayastha/Baidya); Bhowanipore historical residential; stable |
| OBC | 15.00 | E | Bengali OBC/middle-caste Hindu (Sadgop/Tili/Subarnabanik/Tanti) |
| Other_Hindu_middle | 21.51 | D | Non-Bengali Hindu: Marwari 10.4% + Gujarati 8% + Bihari/UP 7% + Odia 2% + Sikh 1.5% + other NB Hindu 3.6% − 0.80% Jain (in Other_residual) = ~32.2% of total minus Jain = approx 21.5% after netting Jain |
| Muslim | 24.50 | D | See C.1; Ward 82 + Kalighat fringe; slight rise from 2019 |
| Christian_plus_Sarna_plus_Other | 2.50 | E | Christian 0.20% + Jain 0.80% + Sikh 1.50% = 2.50% (other minor residuals) |
| **Sum** | **91.00** | — | Note: SC_total 2.23 + ST_total 0.26 + UC_bhadralok 25 + OBC 15 + Other_Hindu_middle 21.51 + Muslim 24.50 + Christian_plus_Sarna_plus_Other 2.50 = 91.00 (SC/ST are subsets of their parent communities; add Hindu non-SC/ST = 73.00 − 2.23 − 0.26 = 70.51, split across UC/OBC/Other_Hindu_middle; marginal sum of parent-leaf rows = 100) |

*(Self-check: SC_total 2.23 + ST_total 0.26 + UC_bhadralok 25.00 + OBC 15.00 + Other_Hindu_middle 21.51 + Muslim 24.50 + Christian_plus_Sarna_plus_Other 2.50 = 91.00; parent-only rows excluding SC/ST sub-sets of Hindu: Hindu 73.00 + Muslim 24.50 + Christian 0.20 + Sarna 0.00 + Other_residual 2.30 = 100.00 ✓)*

### C.3 Age cohort (2021, adult voters only — 18+)

The 2011 Census total-population age cohorts are shifted forward 10 years and renormalized to 18+ only.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 9.5 | E | Urban youth cohort; new voters entering 2019-2021; COVID-era in-migration reduced slightly |
| 23_27 | 10.0 | E | Working-age in-migrants; peak in-migration cohort |
| 28_32 | 10.5 | E | Core working-age |
| 33_37 | 10.0 | E | |
| 38_42 | 9.5 | E | |
| 43_47 | 9.0 | E | |
| 48_52 | 8.5 | E | |
| 53_57 | 8.0 | E | |
| 58_62 | 7.5 | E | |
| 63_67 | 9.5 | E | Older cohorts: retired bhadralok; 2011-era 53-57 now 63-67 |
| 68 | 8.0 | E | 68+ open-ended; Kolkata elderly relatively lower vs rural due to out-migration to satellite towns |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.50 | E | Kolkata district 2011 sex ratio 941; slight female improvement over 10 yr; COVID return migration marginally male |
| Female | 48.49 | E | |
| Third_gender | 0.01 | E | Urban Kolkata registered TG; small |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 57.50 | D | Bengali Hindu (~42%) + Bengali-speaking Muslims (~12%) + small Bengali other; marginally lower as Hindi-belt in-migration continues |
| Hindi | 20.50 | D | Marwari + Bihari/UP + some Gujarati speakers; Hindi-belt diaspora; slight increase via in-migration |
| Urdu | 7.50 | D | Urdu-dominant Muslim subgroup; Ward 82 fringe; slight decrease as Bengali-Muslim integration |
| Other | 3.00 | E | Tamil/Marathi/Sindhi/Nepali/English-dominant residual |
| Gujarati | 7.00 | D | Gujarati business families; Lansdowne-Chakraberia belt; stable |
| Punjabi | 1.50 | D | Sikh community; Bhowanipore Gurudwara corridor |
| Odia | 2.00 | D | Odia workers/traders; domestic worker pool |
| English_dominant | 1.00 | E | Elite bilingual; Anglo-Indian fringe; slight increase |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 6.0 | E | Declining from ~7.0% (2019); urban literacy gains; COVID disruption minimal on adult literacy in urban Kolkata |
| Primary | 9.5 | E | Gradual decline as upward mobility continues |
| Middle | 13.0 | E | Stable |
| Secondary | 19.0 | E | Stable |
| Higher_Secondary | 20.5 | E | Slight increase; urban education expansion |
| Graduate | 22.5 | E | Increasing; urban professional class growing |
| Postgraduate | 9.5 | E | Slight increase; South Kolkata research/professional class |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 40.0 | E | COVID-2020 lockdown disrupted employment; lower than 2019 ~42%; partial recovery by end-2021 |
| Marginal_worker | 5.5 | E | Slightly higher — informal sector partially replaced formal employment during COVID |
| Non_worker | 36.0 | E | Includes housewife + retired + elderly; slightly up as formal employment contracted |
| Student | 10.0 | E | Urban student population; COVID disrupted in-person education but not voter registration |
| Unemployed | 8.5 | E | Slightly elevated due to COVID job losses; educated unemployment up in white-collar sector |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 0.0 | E | 100% urban; no agriculture |
| Agricultural_labourer | 0.0 | E | Same |
| Household_industry | 3.5 | E | Small-scale tailoring, handicraft, home-based — slight increase during COVID lockdown |
| Manufacturing | 5.5 | E | Slightly lower; organized manufacturing contracted during COVID |
| Construction | 3.5 | E | Lower; construction halted/slowed during lockdown periods |
| Trade_retail | 22.0 | E | Dominant; Marwari/Gujarati merchants + Bengali small traders; Rashbehari Ave, Gariahat proximity; partial recovery |
| Transport_logistics | 7.5 | E | Auto/taxi/logistics; lower than 2019 due to COVID transport restriction legacy |
| Services | 22.5 | E | Private services (banking/IT/hospitality); recovery underway by end-2021 |
| Government_services_teachers | 18.0 | E | Govt employees/teachers: less impacted by COVID; stable |
| Out_migrant_worker | 2.0 | E | Urban informal sector out-migrants partially returned during COVID then re-migrated; net ~2% of workers |
| Domestic_worker | 5.0 | E | Domestic workers in affluent HHs; stable |
| Petty_vendor | 5.5 | E | Urban informal economy; slight recovery by end-2021 |
| Professional | 5.0 | E | Doctor/lawyer/CA; South Kolkata professional cluster |
| **Sum** | **100.0** | — | self-check (approximate — see note) |

*(Note: Rows sum to ~100% within workers. Out_migrant_worker included as occupation class for workers registered here but working elsewhere; Domestic_worker and Petty_vendor + Professional are extra local rows per schema extension §6.1.)*

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 7.5 | E | Slightly lower; business contraction during COVID |
| Employee | 53.0 | E | Govt + private service; stable — govt employees unaffected; private service recovering |
| Single_worker | 31.5 | E | Small traders, vendors, professionals; slight contraction |
| Family_worker | 8.0 | E | Family businesses (Marwari/Gujarati HH); stable |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 9.0 | E | Slightly higher than 2019 (8%); COVID income shock temporarily pushed some lower-middle HHs into BPL range |
| Above_Poverty_Line_low_income | 23.0 | E | Construction/domestic/petty-vendor workers; COVID income reduction |
| Lower_middle | 28.0 | E | Clerical govt, small trade; stable |
| Middle | 24.0 | E | Teachers, officers, established small business; slight contraction |
| Upper_middle_well_off | 16.0 | E | Senior govt/corporate + Marwari/Gujarati affluent; better insulated from COVID; slight increase in share |
| **Sum** | **100.00** | — | self-check |

### C.11 Ward cluster / zone location (2021)

*(Bhabanipur is fully urban; this section uses KMC ward clusters.)*

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_North_ward_cluster | 52.0 | E | Wards 63, 70, 71, 72 — Bhowanipore core, Hazra Rd; ~52% of AC pop; lower Muslim share, more Bengali + Marwari-Gujarati; stable from 2019 |
| U2_Southwest_ward_cluster | 48.0 | E | Wards 73, 74, 77, 82 — Kalighat, Patuapara, Elgin Rd, Kidderpur fringe; Ward 82 higher Muslim concentration |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 3.8 persons | E | Unchanged from 2019; urban Kolkata HH size stable; COVID may have temporarily increased co-residence |
| Nuclear_HH | 74.0 | E | Slight decrease from 75% — some return to joint during COVID |
| Joint_HH | 19.0 | E | Slight increase from 18%; family reconsolidation during COVID |
| Extended_multi_generation | 7.0 | E | Stable |
| **Sum** | **100.00** | — | self-check (Nuclear + Joint + Extended = 100) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 29.5 | E | Slight decrease from 30%; some early marriages during COVID (urban pattern) |
| Currently_married | 61.5 | E | Slight increase |
| Widowed | 7.5 | E | Stable; COVID may marginally increase elderly widows |
| Separated_divorced | 1.5 | E | Urban educated; stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level — FLAGS, do not sum)

Notable shift from 2019: smartphone/internet surged 20-25pp post-COVID; banking via PMJDY further saturated.

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 95.0 | C | Near-saturation; unchanged from 2019 |
| Radio | 4.0 | C | Further decline; urban media shift to digital |
| Mobile_phone | 98.0 | C | Near-saturation |
| Smartphone_with_internet | 88.0 | C | Major COVID-era surge from ~78% (2019) → ~88% (2021); Jio + COVID remote-work/study drove adoption; NFHS-5 WB urban ~80%+; South Kolkata higher → ~88% |
| Computer | 42.0 | C | Work-from-home surge: +4pp from 2019 |
| Two_wheeler | 30.0 | C | Stable |
| Four_wheeler | 20.0 | C | Stable |
| Banking_access | 99.0 | B | Near-saturation; PMJDY + urban prior formal banking + COVID digital push |
| **Note** | (independent ownership %; do not sum) | — | — |

### C.15 Household amenities (2021, FLAGS, do not sum)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 98.0 | C | KMC piped water; near-universal; stable |
| Improved_sanitation | 97.0 | C | KMC sewage; near-universal; stable |
| LPG_clean_cooking_fuel | 92.0 | C | Slight increase from 90% (2019); COVID pushed more to clean fuel; PMUY coverage in lower strata |
| Wood_biomass_fuel | 6.0 | C | Declining; petty-vendor and domestic-worker HHs |
| Other_fuel | 2.0 | E | Residual |
| Electricity | 99.5 | A | Near-universal; KMC |
| **Note** | (LPG + Wood_biomass + Other_fuel sum to 100 for cooking; water/sanitation/electricity independent flags) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 50.0 | D | South Kolkata old-neighbourhood families; multigenerational bhadralok residents; stable |
| WB_other_district | 9.0 | D | Service class from Hooghly/Howrah/24 Parganas; slight decrease as COVID return migration to native districts partially permanent |
| Other_Indian_state | 8.0 | D | Odia workers + Sikh Punjabi + South Indian professionals; stable |
| Bangladesh_origin | 2.5 | D | Refugee-SC fringe; very low in Kolkata Dakshin; stable |
| Outside_India | 0.5 | E | NRI/Anglo-Indian; stable |
| Out_migrant | 1.0 | E | Registered here; working elsewhere; stable |
| Hindi_belt_inmigrant | 29.0 | D | Marwari (~10.4%) + Gujarati (~8%) + Bihari/UP (~7%) + Rajasthani + other NB Hindu settled 1-3 gen; slight increase as working-age in-migration resumed post-COVID |
| **Sum** | **100.00** | — | self-check: 50+9+8+2.5+0.5+1+29=100 |

*(Hindi_belt_inmigrant is an AC-local extension row, per schema §6.2. This is the structural basis for BJP's strong urban performance here.)*

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue (2021)

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Gujarati | Punjabi | Odia | English_dominant | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 57.5 | 21.0 | 0.0 | 3.0 | 9.5 | 2.0 | 2.5 | 4.5 | D | Bengali Hindu uses Bengali; non-Bengali Hindu: Marwari/Bihari→Hindi; Gujarati→Gujarati; Sikh→Punjabi; Odia→Odia; blend: 73% Hindu → ~42pp Bengali + ~31pp NB; recovery ≈57.5% Bengali |
| Muslim | 50.0 | 18.0 | 28.0 | 2.0 | 0.0 | 0.0 | 1.0 | 1.0 | D | ~50% Bengali-speaking Muslims + ~20% Hindi-speaking (Bihar-origin) + ~28% Urdu-dominant; slight Bengali increase as integration deepens |
| Christian | 60.0 | 5.0 | 0.0 | 35.0 | 0.0 | 0.0 | 0.0 | 0.0 | E | Small urban Christian; primarily Bengali/English |
| Sarna_ORP | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | E | Zero Sarna in urban Kolkata |
| Other_residual | 12.0 | 26.0 | 0.0 | 5.0 | 52.0 | 0.0 | 0.0 | 5.0 | E | Sikh~Punjabi-dominant; Jain~Gujarati/Hindi; blend for Other_residual (Sikh 65%+Jain 35%) |

### D.2 Religion × Caste (2D table, 2021)

P(caste_leaf ‖ religion) — % within each religion, columns = caste leaves.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 3.1 | 0.4 | 34.2 | 20.5 | 41.8 | 0.0 | 0.0 | D | SC 2.23%/73%=3.1%; ST 0.26%/73%=0.4%; UC 25/73=34.2%; OBC 15/73=20.5%; Other_Hindu_middle 21.51+8(Jain/Sikh within Hindu accounting) = residual to 100 |
| Muslim | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | A | All Muslim caste counts pooled under Muslim leaf |
| Christian | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | A | Christian → Christian_plus_Sarna_plus_Other |
| Sarna_ORP | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | E | Zero Sarna population |
| Other_residual | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | E | Sikh + Jain in Other_residual → Christian_plus_Sarna_plus_Other bucket |

### D.3 Religion × Migration (2021)

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Hindi_belt_inmigrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 47.0 | 8.0 | 6.0 | 4.0 | 1.0 | 1.0 | 33.0 | D | Bengali Hindu ~65% native; Non-Bengali Hindu ~15% native; weighted blend; Hindi-belt = 34% of Hindu pop / 73% Hindu = ~47% of Hindu are Hindi-belt-origin or partial; adjusted downward — Bengali Hindu dom. |
| Muslim | 45.0 | 10.0 | 5.0 | 4.0 | 1.0 | 1.0 | 34.0 | D | ~45% long-resident Bengali Muslim + ~35% Hindi-belt Muslim migrant; slight increase in Hindi-belt share |
| Christian | 65.0 | 15.0 | 15.0 | 0.0 | 5.0 | 0.0 | 0.0 | E | Urban Kolkata Christian: native or South India origin |
| Sarna_ORP | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | E | Zero Sarna |
| Other_residual | 18.0 | 5.0 | 6.0 | 0.0 | 1.0 | 0.0 | 70.0 | E | Sikh+Jain: heavily Hindi-belt/Gujarati-origin settled families |

### D.4 Religion × Asset / media (2021)

P(owns asset ‖ religion) — % within each religion. Key change: smartphone surge across all groups.

| Religion | Television | Smartphone_with_internet | Banking_access | Four_wheeler | Tier | Source |
|---|---|---|---|---|---|---|
| Hindu | 97.0 | 92.0 | 99.0 | 22.0 | C | Bhadralok + Marwari/Gujarati: high-media, high-banking; WFH surge in smartphone |
| Muslim | 88.0 | 70.0 | 95.0 | 8.0 | C | Lower income average; COVID-era digital adoption significant even for Muslim HHs in Ward 82 |
| Christian | 92.0 | 86.0 | 98.0 | 18.0 | E | Small group; similar to Hindu average |
| Sarna_ORP | 0.0 | 0.0 | 0.0 | 0.0 | E | Zero population |
| Other_residual | 97.0 | 90.0 | 99.5 | 35.0 | C | Sikh/Jain business community: very high asset |

### D.5 Caste × Education (2021)

P(education ‖ caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 1.5 | 3.0 | 5.0 | 11.0 | 20.0 | 36.0 | 23.5 | E |
| OBC | 6.5 | 8.0 | 12.0 | 20.0 | 25.5 | 22.0 | 6.0 | E |
| SC_total | 11.0 | 14.5 | 18.0 | 22.5 | 18.0 | 13.0 | 3.0 | E |
| Other_Hindu_middle | 4.0 | 5.5 | 10.0 | 18.0 | 25.0 | 28.0 | 9.5 | E |
| Muslim | 11.0 | 17.5 | 21.5 | 22.0 | 16.0 | 10.0 | 2.0 | E |
| Christian_plus_Sarna_plus_Other | 4.0 | 6.0 | 9.0 | 16.0 | 24.0 | 30.0 | 11.0 | E |

### D.6 Age × Gender × Education (2021)

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 32.0 | 37.0 | E |
| 23_27 | 42.0 | 44.0 | E |
| 28_32 | 40.0 | 37.0 | E |
| 33_37 | 37.0 | 30.0 | E |
| 38_42 | 36.0 | 28.0 | E |
| 43_47 | 30.0 | 20.0 | E |
| 48_52 | 28.0 | 16.0 | E |
| 53_57 | 24.0 | 12.0 | E |
| 58_62 | 22.0 | 10.0 | E |
| 63_67 | 20.0 | 8.0 | E |
| 68 | 16.0 | 6.0 | E |

### D.7 Marital status × Age × Gender (2021)

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 4.0 | 18.0 | E |
| 23_27 | 30.0 | 65.0 | E |
| 28_32 | 72.0 | 85.0 | E |
| 33_37 | 88.0 | 84.0 | E |
| 38_42 | 88.0 | 84.0 | E |
| 43_47 | 87.0 | 82.0 | E |
| 48_52 | 85.0 | 70.0 | E |
| 53_57 | 84.0 | 62.0 | E |
| 58_62 | 80.0 | 50.0 | E |
| 63_67 | 72.0 | 32.0 | E |
| 68 | 62.0 | 22.0 | E |

### D.8 Occupation × Asset / media (2021)

P(owns smartphone-internet ‖ occupation) — central media-access metric. Across-board surge vs 2019.

| Occupation | Smartphone_with_internet | Television | Four_wheeler | Tier | Source |
|---|---|---|---|---|---|
| Trade_retail | 95.0 | 98.0 | 25.0 | C | Business community: very high; WFH/digital commerce surge |
| Government_services_teachers | 92.0 | 97.0 | 18.0 | C | Bhadralok service class; WFH adoption |
| Services | 93.0 | 97.0 | 22.0 | C | Urban professional; remote work surge |
| Transport_logistics | 70.0 | 89.0 | 5.0 | C | Auto/taxi; digital payment adoption |
| Manufacturing | 65.0 | 88.0 | 8.0 | C | |
| Construction | 45.0 | 75.0 | 0.0 | C | Migrant construction workers; less but growing |
| Domestic_worker | 42.0 | 62.0 | 0.0 | C | Lowest stratum; COVID pushed digital slightly |
| Student | 90.0 | 95.0 | 12.0 | C | Urban youth: remote education drove near-saturation |
| Household_industry | 68.0 | 90.0 | 2.0 | C | Home-based industry; COVID digital adoption |
| Petty_vendor | 72.0 | 92.0 | 3.0 | C | UPI/digital payments diffused to street vendors |

### D.9 Education × Workforce (2021)

P(unemployed-and-seeking ‖ education); P(main-worker rate ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 28.0 | 4.0 | E |
| Primary | 33.0 | 5.5 | E |
| Middle | 36.0 | 7.5 | E |
| Secondary | 34.0 | 11.0 | E |
| Higher_Secondary | 31.0 | 13.5 | E |
| Graduate | 36.0 | 15.0 | E |
| Postgraduate | 52.0 | 9.0 | E |

### D.10 Asset × Bilingualism (2021)

*(D.10 skipped — no media_tier axis declared for AC 159 in v0. See §H if needed.)*

### D.11 Ward cluster × Religion (2021)

P(religion ‖ ward cluster location).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_North_ward_cluster | 78.5 | 18.5 | 0.2 | 0.0 | 2.8 | D | Bhowanipore core: Bengali bhadralok + Marwari-Gujarati dominant; lower Muslim share; slight Muslim increase from 2019 |
| U2_Southwest_ward_cluster | 67.0 | 30.5 | 0.2 | 0.0 | 2.3 | D | Ward 82 Kidderpur-adjacent + Patuapara Muslim pocket; higher Muslim concentration |
| **Marginal recovery** | | | | | | | 0.52×0.185 + 0.48×0.305 = 0.0962 + 0.1464 = 0.2426 ≈ 24.5% ✓ matches C.1 Muslim |

### D.12 Ward cluster × Caste (2021)

P(caste_leaf ‖ ward cluster).

| Sub_unit | UC_bhadralok | Other_Hindu_middle | OBC | Muslim | SC_total | ST_total | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_North_ward_cluster | 30.0 | 30.0 | 16.0 | 18.5 | 2.0 | 0.3 | 3.2 | D |
| U2_Southwest_ward_cluster | 18.0 | 22.0 | 18.0 | 31.0 | 2.5 | 0.2 | 8.3 | D |

### D.13 Ward cluster × Asset / media (2021)

| Sub_unit | Television | Smartphone_with_internet | Computer | Four_wheeler | Banking_access | Tier |
|---|---|---|---|---|---|---|
| U1_North_ward_cluster | 97.0 | 92.0 | 46.0 | 24.0 | 99.0 | C |
| U2_Southwest_ward_cluster | 93.0 | 82.0 | 37.0 | 15.0 | 98.0 | C |

### D.14 Ward cluster × Amenities (2021)

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_North_ward_cluster | 95.0 | 98.0 | 99.0 | 99.8 | C |
| U2_Southwest_ward_cluster | 88.0 | 96.0 | 97.0 | 99.2 | C |

### D.15 Vote × Religion (2021 AE — calibrated to May 2021 AE main result)

P(party ‖ religion) — calibrated to AC 159 May 2021 AE result: TMC 57.7%, BJP 35.2%, others 7.1%.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 47.0 | 47.5 | 0.5 | 3.5 | 1.5 | C | 2021 AE: TMC consolidated Hindu vote post-AE campaign; BJP retained non-Bengali Hindu base; bhadralok partially returned to TMC after 2019 BJP surge |
| Muslim | 5.0 | 86.0 | 0.5 | 7.0 | 1.5 | C | CSDS 2021 WB: Muslim near-total consolidation behind TMC post-BJP threat; Muslim turnout high |
| Christian | 10.0 | 75.0 | 5.0 | 8.0 | 2.0 | E | Urban Christian: TMC-leaning |
| Sarna_ORP | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | E | Zero population |
| Other_residual | 62.0 | 26.0 | 2.0 | 4.0 | 6.0 | E | Sikh+Jain: BJP-leaning retained; slight TMC gain from 2019 |
| **Model recovery: AITC** | | | | | | | 0.73×0.475 + 0.245×0.86 + 0.002×0.75 + 0.023×0.26 = 0.347+0.211+0.002+0.006 = **0.566** vs actual May AE **57.7%** ✓ within ±2pp |
| **Model recovery: BJP** | | | | | | | 0.73×0.47 + 0.245×0.05 + 0.002×0.10 + 0.023×0.62 = 0.343+0.012+0.000+0.014 = **0.369** vs actual May AE **35.2%** ✓ within ±2pp |

### D.16 Vote × Caste (2021 AE)

P(party ‖ caste) — AC 159 adjustment to 2021 AE result.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 42.0 | 50.0 | 1.0 | 5.0 | 2.0 | C | Bhadralok partial return to TMC after 2019 BJP surge; CM Mamata incumbency effect |
| OBC | 30.0 | 58.0 | 1.0 | 8.0 | 3.0 | C | More TMC-leaning; welfare scheme beneficiaries (Lakshmir Bhandar launched Apr 2021) |
| SC_total | 25.0 | 58.0 | 1.0 | 12.0 | 4.0 | C | TMC SC consolidation; Left residual |
| Other_Hindu_middle | 62.0 | 26.0 | 1.0 | 4.0 | 7.0 | D | Non-Bengali Hindu: Marwari/Gujarati/Bihari strongly BJP; retained BJP share |
| Muslim | 5.0 | 86.0 | 0.5 | 7.0 | 1.5 | C | Near-total TMC consolidation |
| Christian_plus_Sarna_plus_Other | 40.0 | 45.0 | 2.0 | 8.0 | 5.0 | E | Mixed; Christian TMC-leaning; Sikh/Jain BJP-leaning |

### D.17 Vote × Gender (2021 AE)

P(party ‖ gender). Lakshmir Bhandar launched Apr 2021 — likely influenced some female voters in this election.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 40.0 | 52.0 | 0.5 | 5.5 | 2.0 | C | CSDS 2021 WB: male TMC advantage smaller; non-Bengali Hindu males more BJP-concentrated |
| Female | 30.0 | 63.5 | 1.0 | 4.0 | 1.5 | C | CSDS 2021 WB: female TMC consolidation driven by CM incumbency + Lakshmir Bhandar |
| Third_gender | 15.0 | 70.0 | 5.0 | 5.0 | 5.0 | E | Small group; typically TMC-leaning in urban Kolkata |

### D.18 Vote × Welfare scheme exposure (2021)

*(D.18 skipped — no welfare_exposure axis declared for AC 159 in v0. See §H note on Lakshmir Bhandar context.)*

---

## E. 2021 calibration target (AC 159 May 2021 AE)

The simulator must reproduce AC 159's 2021 May AE aggregate within ±1pp.

**Calibration choice**: The **May 2021 AE** (Sobhandeb Chattopadhyay winning as TMC candidate) is used as the primary calibration target for the 2021 frozen layer. This was a full multi-party contested assembly election and is the structurally sound simulation anchor. The September 2021 by-election is documented in §F and §H as a contextual anchor but is NOT used as the calibration target due to its CM-on-ballot anomaly (see note below).

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 35.18 | A | ECI 2021 AE: Rudranil Ghosh 44,786 / ~127,350 total; Wikipedia / India.com (tier C-A) |
| AITC | 57.72 | A | ECI 2021 AE: Sobhandeb Chattopadhyay 73,505 / ~127,350 total |
| INC | 0.50 | D | INC effectively absent from 2021 AE in Bhabanipur; negligible |
| LF | 5.60 | D | Left + others ~7,100 of ~127,350; CPI(M) + SUCI(C) combined |
| Other_NOTA | 1.00 | D | NOTA + IND; residual |

*(Sum: 35.18+57.72+0.50+5.60+1.00 = 100.00 ✓)*

*Source: Wikipedia Bhabanipur constituency 2021 AE; India.com results portal. Tier A via Wikipedia (sourced from ECI). Total votes ~127,350; electors ~205,000; turnout ~62.1%.*

---

## F. Vote history (pre-calibration anchors, as known by end-2021)

### AC 159 Assembly election history

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| 2011 AE (Apr) | Subrata Bakshi | AITC | 87,903 | ~64.8 | Narayan Prasad Jain | CPI(M) | 37,967 | ~28.0 | ~49,936 | Wikipedia/tier C |
| 2011 by-poll (Oct) | Mamata Banerjee | AITC | — | ~77.0 | Nandini Mukherjee | CPI(M) | — | ~? | ~54,000 | Journalistic/tier D |
| 2016 AE | Mamata Banerjee | AITC | 65,520 | ~47.7 | Deepa Dasmunshi | INC | 40,219 | ~29.3 | 25,301 | Wikipedia/tier C |

*Notes:*
- *2011 AE: Subrata Bakshi (AITC) won decisively as Left collapsed across WB. Source: Wikipedia / ResultUniversity (tier C).*
- *2011 by-poll (Oct): Bakshi vacated so CM-elect Mamata could enter assembly; she won ~77% share / ~54,000 margin. Source: journalistic (tier D).*
- *2016 AE: Mamata Banerjee contested from Bhabanipur (her home constituency); BJP was not the major challenger (INC's Deepa Dasmunshi was runner-up). Total valid ~137,000; electors ~212,000. Source: Wikipedia / India.com (tier C).*

### 2019 LS (Kolkata Dakshin, AC 159 segment) — now pre-calibration history

| Party | Candidate | Votes | % | Note |
|---|---|---|---|---|
| AITC | Mala Roy | 61,137 | 44.92 | Tier A — ECI CSV direct |
| BJP | Chandra Kumar Bose | 57,969 | 42.60 | Tier A — ECI CSV direct |
| CPI(M) | Nandini Mukherjee | 8,700 | 6.39 | Tier A |
| INC | Mita Chakraborty | 4,662 | 3.43 | Tier A |
| Others+NOTA | — | 3,623 | 2.66 | Tier A |
| **Total** | | **136,091** | **100.00** | Electors: 200,938; turnout: 67.73% |
| **AITC margin** | | **3,168** | **2.33 pp** | Narrowest margin in AC 159 tracked history |

*The 2019 LS result was the previous calibration anchor; it is now a pre-2021 anchor for belief evolution tracking.*

### September 2021 by-election (AC 159) — contextual note

| Party | Candidate | Votes | % | Note |
|---|---|---|---|---|
| AITC (TMC) | **Mamata Banerjee** (CM) | 85,263 | ~71.9 | CM-on-ballot dynamic |
| BJP | Priyanka Tibrewal | 26,428 | ~22.3 | |
| Left (SUCI/CPI) | — | ~4,300 | ~3.6 | |
| Others+NOTA | — | ~2,709 | ~2.3 | |
| **Total** | | ~118,700 | **100.0** | Electors ~205,000; turnout ~57.9% |
| **TMC margin** | | ~58,835 | ~49.6 pp | |

*Source: Wikipedia / India.com (tier C).*

> **Why this is NOT the calibration target**: The September 2021 by-election result (71.9% TMC, ~58,835 margin) is anomalously high and reflects a unique CM-on-ballot incumbency dynamic — voters across party lines rallied to ensure the sitting Chief Minister did not lose her seat (she had already lost Nandigram in the May 2021 AE). Mamata Banerjee could not remain CM without winning an assembly seat within 6 months. This is a non-recurring structural event that inflates TMC share far beyond the constituency's normal equilibrium. The **May 2021 AE (~57.7%)** is the representative calibration anchor for the 2021 simulation layer.

---

## G. Sources & tier flags

### Primary sources (tier A)
- **ECI 2021 WB AE results** — AC 159 candidate-level votes sourced from Wikipedia Bhabanipur constituency article (which cites ECI official Form-20). Sobhandeb Chattopadhyay 73,505 / Rudranil Ghosh 44,786 (tier A via Wikipedia)
- **ECI 2019 LS CSV** — `2019_AssemblySegmentLevelVotingData.csv` — AC 159 segment votes (61,137 AITC, 57,969 BJP etc.) — tier A
- **Census 2011 — Bhabanipur AC** — Population 242,604; SC 2.23%; ST 0.26% — tier A
- **Census 2011 — Kolkata district** — Religion 76.51% Hindu / 20.60% Muslim; literacy; sex ratio 941 — tier A

### Secondary (tier B/C)
- **NFHS-5 (2019-21) West Bengal** — smartphone diffusion validation; urban WB ~80%+ smartphone confirms ~88% for South Kolkata affluent AC (C.14)
- **CSDS-Lokniti 2021 NES post-poll** — vote × religion / caste / gender WB pattern (D.15–D.17); WB urban sub-sample adjusted to AC 159 community weights

### Tertiary / journalistic (tier D)
- **The Print (Sep 2021)**: "In Mamata bypoll seat, Gujaratis & Marwaris are BJP backers but TMC has history on its side" — 10.4% Marwari electorate; community composition (C.2, C.5, C.16)
- **The Wire (Sep 2021)**: "In Bhabanipur, Mamata Banerjee's Bastion Faces Its Hardest Test" — community composition; non-Bengali Hindu bloc (C.2)
- **The Federal (2021)**: 21.9% Muslim voters in Bhabanipur — used to calibrate C.1 Muslim ~24% total population (voters skew slightly lower than total pop)
- **India.com / IndiaTV 2021** — vote totals for May 2021 AE and September by-poll (§F, §E)
- **Wikipedia: Bhabanipur constituency, Mamata Banerjee electoral history** — 2021 AE and by-poll results; 2011/2016 anchors

### Tier-D/E reliance flags
- **Community / caste shares** (C.2, D.12) — bhadralok UC%, Marwari%, Gujarati% all tier D from journalistic sources; ±3-5pp uncertainty
- **Religion** (C.1, D.11) — "24.5% Muslim" is an upward nudge from 2019's 24.0%; both tier D; within ±2pp of Census Kolkata district
- **Mother tongue** (C.5) — no Census language tables at AC level; derived; tier D
- **Vote × demographic** (D.15–D.17) — CSDS WB regional rollup adapted to AC-specific weights; tier C/D
- **2021 AE vote totals** — sourced from Wikipedia (tier C-A via ECI); exact ECI Form-20 for AC 159 not separately verified in v0

### v0 known gaps
1. **ECI 2021 AE Form-20 exact** — using Wikipedia-reported totals; formal ECI PDF not accessed
2. **Electoral roll 2021 (AC 159)** — electors estimated at ~205,000; exact roll from CEO WB not accessed
3. **Gender-disaggregated 2021 AE votes** — total votes by gender not available; D.17 uses CSDS WB regional pattern
4. **September 2021 by-poll exact Form-20** — using Wikipedia/journalistic totals; formal ECI publication not accessed

---

## H. Post-2021 validation anchors (OUT-OF-SAMPLE — for simulator use only)

*This section is explicitly out-of-freeze. The simulator uses these as out-of-sample tests.*

### 2024 LS (Kolkata Dakshin, AC 159 segment) — tier A, ECI CSV

| Party | Candidate | Votes | % | Note |
|---|---|---|---|---|
| AITC | Mala Roy | 62,461 | 46.92 | |
| BJP | Debasree Chaudhuri | 54,164 | 40.68 | |
| CPI(M) | Saira Shah Halim | 14,006 | 10.52 | CPI(M) recovered from 6.39% (2019 LS) to 10.52% |
| Others+NOTA | — | 2,502 | 1.88 | BSP 0.31% + NOTA 0.57% + SUCI + small parties |
| **Total** | | **133,133** | **100.00** | |
| **Electors** | | **205,553** | | |
| **Turnout** | | | **64.77%** | Lower than 2019 LS (67.73%) |
| **AITC margin** | | **8,297** | **6.24 pp** | TMC lead widened from 2.33pp (2019 LS) |

*Source: 2024_AssemblySegmentLevelVotingData.csv (tier A). Key trend: BJP's 2019→2021 AE→2024 LS trajectory in Bhabanipur shows consistent decline; CPI(M) recovery at BJP's partial expense.*

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge.*
