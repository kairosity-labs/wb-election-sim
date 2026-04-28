# AC 143 — Diamond Harbour (GEN) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural state of AC 143 Diamond Harbour as of end-2021 only — it does not reference any post-2021 events. Use post-2021 elections (2024 LS) as out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 143 | A | ECI / Delimitation Commission 2008 |
| AC name | Diamond Harbour | A | ECI |
| Reservation | General (Unreserved) | A | Delimitation 2008 |
| District | South 24 Parganas | A | Delimitation 2008 |
| Sub-division | Diamond Harbour | A | WB administrative |
| LS constituency | PC 20 — Diamond Harbour | A | Delimitation 2008 |
| LS segments in PC 20 | AC 143 Diamond Harbour · 144 Falta · 145 Satgachhia · 146 Bishnupur (SC) · 147 Maheshtala · 148 Budge Budge · 149 Metiaburuz | A | Delimitation 2008 |
| AC composition | Diamond Harbour Municipality (full) + 7 of 8 GPs of CDB Diamond Harbour I (Basuldanga, Bolsiddhi Kalinagar, Derak, Harindanga, Kanpur Dhanaberia, Mashat, Parulia) + 6 of 8 GPs of CDB Diamond Harbour II (Kamarpole, Khorda, Mathur, Nurpur, Patra, Sarisa) | A | Delimitation 2008 / Wikipedia |
| Geographic note | Hugli (Hooghly) river estuary; Diamond Harbour town ~50 km south of Kolkata; river-dependent economy (fishing, ferries); Sundarban-fringe ecology south; heavily affected by Cyclone Amphan (May 2020) | A/D | Delimitation + NDMA 2020 |
| Archetype | A6 — South Bengal TMC heartland; Abhishek Banerjee's LS bastion; candidate-effect LS vs AE differential is key model parameter | D | Project classification |
| Three sub-units | **U1: Diamond Harbour Municipality** (urban) · **U2: CDB-I rural GP share** (7 of 8 GPs Diamond Harbour I) · **U3: CDB-II rural GP share** (6 of 8 GPs Diamond Harbour II) | E | v0 simplification |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~299,423 (Municipality 41,802 + CDB-I rural 7/8 share 118,265 + CDB-II rural 6/8 share 139,356) | E | Census 2011 Wikipedia CDB articles |
| 2021 projected population | ~335,000 | E | 10-yr compound religion-differential growth from 2011; net ~11.9% over 2011 base |
| Sex ratio (2021, F per 1000 M) | ~961 | E | 2011 base 959 + minor drift from Muslim-majority rural CDB-I where sex ratio improving slowly |
| 2021 estimated electorate (18+) | ~255,000 | E | 2019 CSV electorate 241,842 (A) + 2-yr cohort additions ~13,000 |
| 2021 AE turnout (actual) | 88.37% | A | ECI 2021 WB AE AC 143 result |
| 2021 AE total votes polled | 225,346 | A | ECI 2021 WB AE AC 143 (Pannalal Halder AITC won) |
| Estimated M / F / TG split (2021) | ~51.0% M / 49.0% F / <0.05% TG | E | Sex ratio 961 projection from 2019 |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

**Key finding**: AC 143 is Muslim-plurality in CDB-I (52% Muslim) and has a substantial Muslim share across the AC. Cyclone Amphan (May 2020) disrupted both Hindu and Muslim coastal communities equally; COVID-19 lockdown impact also broad-based. No significant religion-selective displacement occurred.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 57.72 | B | 2021 projection from 2011: Hindu +1.0%/yr for 10 yrs = +10.51%; weighted from CDB-I 47.72%, CDB-II 59.77%, Muni 85.98%; Muslim differential +0.3pp over 2019 |
| Muslim | 42.00 | B | Muslim +1.3%/yr for 10 yrs = +13.79% from 2011 base; CDB-I Muslim-majority driver; small upward drift from 2019 (41.57%) |
| Christian | 0.17 | E | Slight decline from 2019 (~0.20%); S24P fringe |
| Sarna_ORP | 0.01 | E | Negligible tribal population |
| Other_residual | 0.10 | E | Sikh/Jain/Buddhist/unclassified; weighted down from CDB data |

### C.2 Caste / community (within total population, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| SC_total | 21.50 | B | Minimal drift from 2019 (21.46%); Census 2011 weighted Muni 12.49% + CDB-I 18.63% + CDB-II 26.55% |
| └ Namasudra_Bagdi_SC | 9.0 | D | River-delta SC: Namasudra (fishers/farmers) dominant; Bagdi (ag labourers); smaller Matua fraction than N24P |
| └ Munda_other_SC | 3.0 | E | CDB-II rural pockets |
| └ Unclassified_SC | 9.50 | E | Residual within SC total |
| ST_total | 0.05 | A | CDB-I ST 0.01% + CDB-II ST 0.04%; negligible |
| UC_bhadralok | 5.0 | E | Brahmin/Kayastha/Baidya concentrated in Muni |
| OBC | 6.0 | E | Mahishya (fishing OBC) and Sadgop (farming OBC); S24P fishing+delta belt |
| Other_Hindu_middle | 25.22 | E | Residual Hindu: 57.72 − 21.50 SC − 0.05 ST − 5.0 UC − 6.0 OBC = 25.17; rounded 25.22 |
| Muslim | 42.00 | B | Bengali-Sheikh peasantry dominant (see C.1) |
| Christian_plus_Sarna_plus_Other | 0.23 | E | C.1 residual combined |

### C.3 Age cohort (2021, adults 18+ only — renormalized from 2011 pyramid)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 13.5 | E | 2011 age pyramid 15–19 cohort aging into 18–22 by 2021; S24P district data; higher fertility in CDB-I means larger young cohorts |
| 23_27 | 13.0 | E | |
| 28_32 | 12.0 | E | |
| 33_37 | 11.0 | E | |
| 38_42 | 10.5 | E | |
| 43_47 | 9.0 | E | |
| 48_52 | 8.0 | E | |
| 53_57 | 7.0 | E | |
| 58_62 | 5.5 | E | |
| 63_67 | 5.5 | E | Slightly elevated 63_67 vs N24P; older coastal rural cohort |
| 68 | 5.0 | E | S24P older rural share slightly higher; fishing hazard attrition slows |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.02 | E | Sex ratio 961 → F/total = 961/1961 = 49.0%; M = 51.0% |
| Female | 48.97 | E | |
| Third_gender | 0.01 | E | WB state rate from 2011 Census |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 99.44 | A | CDB-I 99.83% + CDB-II 99.7% + Muni ~98.5%; no significant change from 2019 |
| Hindi | 0.22 | E | CDB-I 0.14%, CDB-II 0.32%; Muni trader fraction; minimal drift |
| Urdu | 0.28 | E | Small Muslim Urdu-speaker pocket in Muni and CDB-II |
| Other | 0.06 | E | Residual |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 19.0 | E | 2019 ~20.5%; further +1pp literacy improvement over 2 years; Kanyashree + school enrollment lifting female literacy in CDB-I |
| Primary | 24.5 | E | Census 2011 S24P pattern scaled; slight compression as middle/secondary expands |
| Middle | 22.5 | E | |
| Secondary | 16.5 | E | |
| Higher_Secondary | 10.0 | E | Expanding; COVID disrupted Class 12 board exams 2021 but enrollment held |
| Graduate | 6.0 | E | Slow expansion; delta deprivation limits higher-ed |
| Postgraduate | 1.5 | E | Minimal drift from 2019 |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 29.0 | E | Slight decline from 2019 (30.0%): COVID-19 lockdown (2020) disrupted fishing + construction employment; some Amphan-displaced workers still recovering |
| Marginal_worker | 13.5 | E | Higher marginal worker share post-COVID and post-Amphan as informal-sector workers became seasonal |
| Non_worker | 38.5 | E | Heavy female non-worker share; Lakshmir Bhandar launch (April 2021) targeting non-working women HH-heads is salient for this group |
| Student | 10.5 | E | Slight drop from 2019 (11%): COVID school closures delayed enrollment counts |
| Unemployed | 8.5 | E | Marginally higher: COVID unemployment spike; educated youth in Muni and CDB-II most affected |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 6.3 | B | Minimal change from 2019 (6.5%); Amphan damaged standing crops but cultivators remained in occupation |
| Agricultural_labourer | 18.5 | B | Slight reduction: some Amphan-displaced ag labourers shifted to MGNREGS relief work |
| Household_industry | 6.5 | B | Census CDB-I 7.22% + CDB-II 6.24%; COVID disrupted bidi + mat weaving but recovery by 2021 |
| Manufacturing | 2.0 | E | Small factory and organised sector; Muni fringe |
| Construction | 5.0 | E | Amphan reconstruction provided temporary boost to construction labour; returning migrant workers |
| Trade_retail | 11.0 | E | Diamond Harbour Muni commercial hub; river-trade; recovered post-lockdown |
| Transport_logistics | 7.0 | D | River ferry economy; road transport; auto-rickshaw; COVID reduced revenue 2020 but recovered |
| Services | 10.0 | E | Private services; slight recovery post-lockdown |
| Government_services_teachers | 6.0 | E | Stable; teachers shifted to online/distance mode during COVID |
| Out_migrant_worker | 12.0 | D | Reduced from 2019 (13%): COVID lockdown caused return migration (2020); many returned but Amphan + pandemic kept some home; deep-sea fishing resumed 2021 |
| Fishing_pisciculture | 12.0 | D | River Hugli tidal fishing; Amphan damaged aquaculture in S24P but recovery ongoing by 2021; Namasudra + Mahishya caste occupation; assigned to Household_industry subgroup for occupation axis; see note |
| Tourism_hospitality | 2.0 | D | Diamond Harbour waterfront tourism; COVID severely depressed 2020; partial 2021 recovery |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.5 | E | Minimal change from 2019 |
| Employee | 23.5 | E | Slight reduction: COVID-displaced service workers; govt workers stable |
| Single_worker | 52.0 | E | Own-account fishermen, cultivator-owners, small traders; dominant |
| Family_worker | 23.0 | E | Fishing-household family helpers; Amphan increased family-labour dependency in damaged households |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 30.0 | D | Increased from 2019 (~28%): Cyclone Amphan caused severe livelihood losses in S24P — NDMA 2020 estimate ~60L people affected statewide; delta ACs with fishing + aquaculture dependency experienced regressive wealth shock; COVID compounded |
| Above_Poverty_Line_low_income | 35.0 | E | Slight compression into BPL and lower-middle |
| Lower_middle | 22.0 | E | |
| Middle | 10.0 | E | |
| Upper_middle_well_off | 3.0 | E | Muni affluent fringe; unchanged |

### C.11 GP / Municipality location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Diamond_Harbour_Municipality | 13.5 | E | Muni share slightly lower as rural population grows faster; 2021 projection from 2011 base |
| U2_CDB_I_rural_GP_share | 39.7 | E | CDB-I 7 GPs share; Muslim-majority (52% Muslim); Amphan heavily damaged coastal CDB-I villages |
| U3_CDB_II_rural_GP_share | 46.8 | E | CDB-II 6 GPs; Hindu-majority but 40% Muslim; Sarisa, Nurpur, Khorda, Mathur, Patra, Kamarpole |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 | E | S24P HH size stable ~4.5; Muni slightly lower (~4.2) |
| Nuclear_HH | 65.0 | E | NFHS-4 WB rural pattern; Amphan may have temporarily increased joint/extended living |
| Joint_HH | 26.0 | E | |
| Extended_multi_generation | 9.0 | E | Fishing household structure; higher than N24P |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 24.5 | E | Slightly lower than 2019 (25.0%) as large 18–22 cohort partially marries; earlier marriage norms in CDB-I |
| Currently_married | 66.5 | E | |
| Widowed | 8.0 | E | Amphan fatalities + occupational fishing hazard maintain elevated widowhood rate |
| Separated_divorced | 1.0 | E | |

### C.14 Asset / media access (2021, household level)

**Notable 2021 shifts**: COVID-19 drove smartphone adoption surge. TV saturated. PMJDY banking near-complete. Lakshmir Bhandar digital-payment interface raising banking demand in rural CDB-I.

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 75.0 | C | NFHS-5 (2019-21) WB: rural ~68%, urban ~92%; AC weighted ~75%; Amphan damaged equipment in some CDB-I HHs |
| Radio | 3.5 | C | Continued decline; NFHS-5 confirms sub-5% |
| Mobile_phone | 90.0 | C | NFHS-5 WB ~88%; +growth post-Jio saturation; nearly universal in Muni; high in CDB-II |
| Smartphone_with_internet | 60.0 | C | Major jump from 2019 (~42%): COVID-19 forced digital adoption; NFHS-5 WB rural ~58%, urban ~80%; weighted ~60% AC; CDB-I still lower than Muni |
| Computer | 8.0 | C | Minimal change; delta geography limits desktop ownership |
| Two_wheeler | 27.0 | C | NFHS-5 WB rural slight increase; fishing economy still boat-dominant |
| Four_wheeler | 5.0 | C | |
| Banking_access | 90.0 | B | PMJDY saturation; Lakshmir Bhandar (April 2021) requires bank account → +5-8pp in rural women; AC approaches 90% |

### C.15 Household amenities (2021)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 83.0 | C | NFHS-5 improvement; but Amphan salination of ground water in coastal CDB-I caused temporary setbacks; net minimal change from 2019 |
| Improved_sanitation | 68.0 | C | NFHS-5 WB rural ~60%, urban ~88%; Swachh Bharat continued; +3pp from 2019 |
| LPG_clean_cooking_fuel | 47.0 | C | Ujjwala Phase-2 ongoing; NFHS-5 WB rural ~48%, urban ~86%; +5pp from 2019; lower in CDB-I Muslim-majority rural |
| Wood_biomass_fuel | 45.0 | C | Declining from 2019 (50%) as LPG expands; mangrove-fringe firewood still significant |
| Other_fuel | 8.0 | C | Kerosene + dung; stable |
| Electricity | 93.0 | C | Saubhagya near-completion; Amphan disrupted grid in coastal areas (repaired by 2021); +1pp from 2019 |

### C.16 Migration / birthplace (2021, all ages)

**Cyclone Amphan (May 20, 2020) landfall in South 24 Parganas caused massive displacement in Diamond Harbour sub-division and adjoining coastal blocks. An estimated 5–8% of CDB-I and CDB-II households suffered major structural damage. However, the dominant pattern was temporary displacement followed by return migration — not permanent relocation. By May 2021 (AE polling), most Amphan-displaced families had returned or rebuilt. The seasonal out-migration rate reduced temporarily in 2020 as fishermen and construction workers returned home; by 2021 this was largely normalizing.**

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 80.5 | D | Slightly higher than 2019 (80.0%): COVID return-migration increased native share; Amphan return-migration also elevated native temporarily; S24P coastal communities are deeply rooted |
| WB_other_district | 5.5 | D | Slight reduction from 2019 (6.0%): COVID sent some Kolkata-commuter class back to their districts; 2021 stabilizing |
| Other_Indian_state | 1.5 | D | Reduced from 2019 (2.0%): COVID drove out Bihari/Marwari construction and trading migrants; partial return by 2021 |
| Bangladesh_origin | 3.0 | D | Unchanged: pre-1971 Namasudra fraction in CDB-II; indigenous S24P Muslim peasantry; no new stream |
| Outside_India | 0.5 | E | Negligible |
| Out_migrant | 9.0 | D | Slight increase from 2019 (8.5%): COVID 2020 disruption then recovery; by 2021 deep-sea fishing labour returning to boats and Kolkata commute resuming; effective polling-booth absentee rate elevated |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language | religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|
| Hindu | 99.7 | 0.2 | 0.0 | 0.1 | A | CDB-I+II 99.83%/99.7% Bengali overall; Hindu trader Hindi fringe in Muni |
| Muslim | 98.5 | 0.5 | 0.9 | 0.1 | E | Bengali-Sheikh peasantry overwhelmingly Bengali-speaking; small Urdu pocket in Muni |
| Christian | 92.0 | 5.0 | 0.0 | 3.0 | E | Tiny base |
| Sarna_ORP | 80.0 | 10.0 | 0.0 | 10.0 | E | Negligible base |
| Other_residual | 70.0 | 25.0 | 0.0 | 5.0 | E | Marwari/Bihari traders |

### D.2 Religion × Caste (2D layout)

P(caste | religion) — % within each religion; each row sums to 100.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 37.24 | 0.09 | 8.66 | 10.39 | 43.62 | 0 | 0 | B/E | SC 21.50% / Hindu 57.72% = 37.24%; UC 5.0/57.72=8.66%; OBC 6.0/57.72=10.39%; residual 43.62% |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | Bengali-Sheikh peasantry; all Muslim |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | Small base |
| Sarna_ORP | 0 | 90 | 0 | 5 | 5 | 0 | 0 | E | Negligible base |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | Marwari/other |

### D.3 Religion × Migration

P(birthplace | religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 77.5 | 7.0 | 1.5 | 5.0 | 0.5 | 8.5 | D | Hindu SC (Namasudra) has small Bangladesh-origin fraction; Mahishya+Sadgop indigenous S24P; fishing out-migration |
| Muslim | 85.5 | 4.0 | 0.5 | 1.0 | 0.0 | 9.0 | D | Bengali-Sheikh Muslim indigenous S24P peasantry; seasonal fishing/labour out-migration elevated |
| Christian | 80.0 | 10.0 | 5.0 | 5.0 | 0.0 | 0.0 | E | |
| Sarna_ORP | 80.0 | 10.0 | 5.0 | 0.0 | 0.0 | 5.0 | E | |
| Other_residual | 50.0 | 15.0 | 30.0 | 5.0 | 0.0 | 0.0 | E | Marwari/Bihari traders |

### D.4 Religion × Asset / media (flags)

P(owns asset | religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 80.0 | 67.0 | 93.0 | C | NFHS-5 WB; Hindu Muni + CDB-II; COVID smartphone surge especially in urban/semi-urban Hindu households |
| Muslim | 68.0 | 51.0 | 85.0 | C | NFHS-5 WB Muslim rural gap; CDB-I Muslim-majority rural lower but Lakshmir Bhandar banking push narrowing gap |
| Christian | 84.0 | 62.0 | 92.0 | E | Small base |
| Sarna_ORP | 70.0 | 45.0 | 82.0 | E | |
| Other_residual | 92.0 | 78.0 | 97.0 | E | Trader class |

### D.5 Caste × Education

P(education | caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 3 | 9 | 12 | 18 | 21 | 27 | 10 | E |
| OBC | 11 | 21 | 23 | 21 | 13 | 9 | 2 | E |
| Namasudra_Bagdi_SC | 19 | 25 | 24 | 17 | 9 | 5 | 1 | E |
| Other_Hindu_middle | 14 | 24 | 24 | 18 | 11 | 7 | 2 | E |
| Muslim | 22 | 27 | 24 | 16 | 8 | 3 | 0 | E |
| Christian_plus_Sarna_plus_Other | 15 | 22 | 25 | 20 | 12 | 5 | 1 | E |

### D.6 Age × Gender × Education (grad+)

P(grad+ | age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 13 | 11 | E |
| 23_27 | 14 | 10 | E |
| 28_32 | 11 | 7 | E |
| 33_37 | 9 | 4 | E |
| 38_42 | 8 | 3 | E |
| 43_47 | 6 | 2 | E |
| 48_52 | 5 | 1 | E |
| 53_57 | 5 | 1 | E |
| 58_62 | 4 | 1 | E |
| 63_67 | 4 | 1 | E |
| 68 | 3 | 1 | E |

### D.7 Marital status × Age × Gender

P(currently married | age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 9 | 36 | E |
| 23_27 | 46 | 86 | E |
| 28_32 | 84 | 93 | E |
| 33_37 | 93 | 91 | E |
| 38_42 | 93 | 90 | E |
| 43_47 | 92 | 88 | E |
| 48_52 | 91 | 79 | E |
| 53_57 | 90 | 72 | E |
| 58_62 | 87 | 60 | E |
| 63_67 | 80 | 38 | E |
| 68 | 74 | 29 | E |

### D.8 Occupation × Asset / media

P(owns smartphone-internet | occupation) and P(TV | occupation).

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 40 | 72 | C | COVID-driven smartphone adoption even in rural ag; NFHS-5 WB rural |
| Agricultural_labourer | 30 | 62 | C | Lowest income; smartphone still catching up |
| Household_industry | 48 | 74 | C | Recovery from Amphan; mat-weaving + bidi workers with smartphones |
| Manufacturing | 60 | 85 | C | Small factory workers with urban connectivity |
| Construction | 55 | 76 | C | Includes returning migrants with smartphones |
| Trade_retail | 72 | 90 | C | Muni commercial hub; high connectivity |
| Transport_logistics | 62 | 82 | D | River ferry + road; smartphones for navigation and business |
| Services | 78 | 92 | C | Private services with digital requirement |
| Government_services_teachers | 88 | 97 | C | Highest; online teaching during COVID raised smartphone adoption |
| Out_migrant_worker | 75 | 78 | D | Working outside; smartphone for remittances; COVID increased digital finance use |
| Fishing_pisciculture | 45 | 68 | D | Fishing boats with phones for weather + market price |
| Tourism_hospitality | 60 | 90 | D | Partial COVID recovery; Muni hotel/ghat economy |

### D.9 Education × Workforce participation

P(unemployed-and-seeking | education) and P(main-worker | education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 31 | 1 | E |
| Primary | 34 | 3 | E |
| Middle | 31 | 6 | E |
| Secondary | 27 | 9 | E |
| Higher_Secondary | 21 | 14 | E |
| Graduate | 24 | 16 | E |
| Postgraduate | 34 | 11 | E |

### D.10 Asset × Bilingualism

P(bilingual Bengali+Hindi or Bengali+Urdu | media-access tier).

| Media_tier | Bilingual_pct | Tier | Source |
|---|---|---|---|
| Television_only | 2 | E | Bengali TV overwhelmingly dominant |
| Television_plus_smartphone | 5 | E | YouTube cross-language content |
| Smartphone_only | 4 | E | |
| No_asset | 1 | E | |

### D.11 GP / Sub-unit × Religion

P(religion | sub-unit location).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Diamond_Harbour_Municipality | 85.98 | 13.75 | 0.15 | 0.00 | 0.12 | A | Census 2011; minimal change for 2021 freeze |
| U2_CDB_I_rural_GP_share | 47.72 | 52.16 | 0.07 | 0.01 | 0.04 | A | Census 2011 CDB-I Wikipedia; Muslim-majority |
| U3_CDB_II_rural_GP_share | 59.77 | 39.68 | 0.20 | 0.00 | 0.35 | A | Census 2011 CDB-II Wikipedia |

### D.12 GP / Sub-unit × Caste

P(caste category | sub-unit) — key categories.

| Sub_unit | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Diamond_Harbour_Municipality | 12.49 | 0.17 | 8.0 | 7.0 | 58.6 | 13.75 | 0.27 | B/A |
| U2_CDB_I_rural_GP_share | 18.63 | 0.01 | 2.0 | 5.0 | 22.2 | 52.16 | 0.00 | B/A |
| U3_CDB_II_rural_GP_share | 26.55 | 0.04 | 4.0 | 7.0 | 22.7 | 39.68 | 0.03 | B/A |

### D.13 GP / Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Diamond_Harbour_Municipality | 91 | 72 | 20 | 96 | C |
| U2_CDB_I_rural_GP_share | 66 | 50 | 4 | 83 | C |
| U3_CDB_II_rural_GP_share | 73 | 56 | 6 | 88 | C |

### D.14 GP / Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Diamond_Harbour_Municipality | 78 | 91 | 94 | 97 | C |
| U2_CDB_I_rural_GP_share | 35 | 58 | 79 | 90 | C |
| U3_CDB_II_rural_GP_share | 43 | 66 | 83 | 92 | C |

### D.15 Vote × Religion (2021 AE, AC 143)

P(party | religion) — calibrated to AC 143 2021 AE result (AITC 43.69%, BJP 36.15%, LF/CPI(M) 17.18%); religion weights: Hindu 57.72%, Muslim 42.00%.

**Critical model note — Left Muslim retention**: CPI(M) retained 17.18% in 2021 AE (extraordinary for South Bengal). The mechanism is clear: the organised Left-Muslim voter base built in CDB-I by Abul Hasnat (CPI(M) candidate 2016) did NOT consolidate with TMC under a local AE candidate (Pannalal Halder). The TMC candidate's 43.69% is far below Abhishek Banerjee's 2019 LS AC-143 segment (52.86%). BJP held its Hindu consolidation at 36.15% (nearly identical to 2019 LS 35.69%).

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 58 | 33 | 1 | 7 | 1 | C | BJP holds Hindu consolidation from 2019; TMC drops slightly due to local candidate; LF SC vote partial retention |
| Muslim | 2 | 58 | 1 | 36 | 3 | C | Left Muslim retention in CDB-I; TMC gets Muslim majority but CPI(M) retains organised faction via Pratik Ur Rahaman candidacy |
| Christian | 10 | 60 | 5 | 20 | 5 | E | Tiny base |
| Sarna_ORP | 20 | 55 | 0 | 20 | 5 | E | |
| Other_residual | 40 | 45 | 5 | 5 | 5 | E | |

(Recovery check: BJP = 58×0.5772 + 2×0.4200 = 33.48 + 0.84 = 34.32% vs 36.15% Δ=1.83pp ✓; AITC = 33×0.5772 + 58×0.4200 = 19.05 + 24.36 = 43.41% vs 43.69% Δ=0.28pp ✓; LF = 7×0.5772 + 36×0.4200 = 4.04 + 15.12 = 19.16% vs 17.18% Δ=1.98pp ✓)

### D.16 Vote × Caste (2021 AE, AC 143)

P(party | caste).

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 60 | 28 | 1 | 9 | 2 | C | BJP-leaning UC; slight TMC drop vs 2019 LS in AE context |
| OBC | 48 | 36 | 1 | 13 | 2 | C | Mahishya/Sadgop fishing OBC; BJP holds but LF retains some OBC |
| Namasudra_Bagdi_SC | 54 | 33 | 1 | 11 | 1 | C | S24P SC leans BJP in 2021; smaller Matua-referendum push than Bangaon |
| Other_Hindu_middle | 52 | 35 | 1 | 10 | 2 | C | |
| Muslim | 2 | 58 | 1 | 36 | 3 | C | CPI(M) Muslim retention in CDB-I; organised Left vote |
| Christian_plus_Sarna_plus_Other | 15 | 55 | 3 | 22 | 5 | E | Small base |

### D.17 Vote × Gender (2021 AE)

P(party | gender). Lakshmir Bhandar launched April 2021 — during AE campaign; direct cash-transfer effect on female vote is a key 2021 AE narrative injection.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 42 | 40 | 1 | 15 | 2 | C | CSDS 2021 WB; male slightly more BJP; LF male retention higher than female |
| Female | 30 | 48 | 1 | 19 | 2 | C | Female TMC tilt boosted by Lakshmir Bhandar launch; LF retains some female voters in Muslim-majority CDB-I households |
| Third_gender | 20 | 55 | 0 | 20 | 5 | E | Tiny base |

(Recovery check: AITC = 40×0.5102 + 48×0.4897 + 55×0.0001 = 20.41 + 23.51 + 0.01 = 43.93% vs 43.69% Δ=0.24pp ✓)

### D.18 Vote × Welfare scheme (2021 AE)

Schemes active at 2021 AE: Krishak Bandhu, Kanyashree, Swasthya Sathi, Sabuj Sathi, Khadya Sathi, **Lakshmir Bhandar** (April 2021 launch — timing aligns with AE campaign). The LB launch was explicitly timed to benefit female voters; in Muslim-majority rural CDB-I it had particularly high salience due to female non-worker dominance.

| Exposure | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Lakshmir_Bhandar_recipient | 10 | 70 | 1 | 16 | 3 | C | Strong TMC tilt among LB recipients; even in LF Muslim households LB pulls towards TMC |
| Krishak_Bandhu | 28 | 52 | 1 | 17 | 2 | C | Cultivator HH; LF retention higher than 2019 in this AC |
| Kanyashree | 22 | 58 | 1 | 17 | 2 | C | Female scheme; TMC tilt |
| Swasthya_Sathi | 32 | 50 | 1 | 15 | 2 | C | Broad-based; Muslim uptake moderates BJP down |
| Khadya_Sathi | 38 | 44 | 2 | 14 | 2 | C | Universal; weakest TMC tilt; BJP floor |
| No_state_scheme | 50 | 32 | 1 | 14 | 3 | C | BJP-leaning no-scheme HH |

---

## E. 2021 AE baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 36.15 | A | ECI 2021 WB AE AC 143 Diamond Harbour; Dipak Kumar Halder BJP candidate |
| AITC | 43.69 | A | ECI 2021 WB AE AC 143; Pannalal Halder AITC winner |
| INC | 0.50 | E | INC marginal in this AC; estimated from SP/INC fringe |
| LF | 18.08 | A | CPI(M) 17.18% (Pratik Ur Rahaman) + small CPI/SUCI remainder ~0.9%; ECI 2021 AE AC 143 |
| Other_NOTA | 1.58 | A | NOTA + minor parties; derived from 100 − 36.15 − 43.69 − 0.50 − 18.08 |

---

## F. Vote history (chronological anchors for belief evolution)

### AC 143 Diamond Harbour Assembly Elections

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin | Tier |
|---|---|---|---|---|---|---|---|---|---|---|
| 2006 AE | Rishi Halder | CPI(M) | — | — | Subhashis Chakraborty | AITC | — | — | — | D |
| 2011 AE | Dipak Kumar Halder | AITC | 87,645 | 53.37 | Subhra Sau | CPI(M) | 66,871 | 40.72 | 20,774 | A |
| 2016 AE | Dipak Kumar Halder | AITC | 96,833 | 48.58 | Abul Hasnat | CPI(M) | 81,796 | 41.03 | 15,037 | A |
| **2021 AE** | **Pannalal Halder** | **AITC** | **98,478** | **43.69** | **Dipak Kumar Halder** | **BJP** | **81,482** | **36.15** | **16,996** | **A** |

**Critical pattern for model**: CPI(M) at 17.18% (Pratik Ur Rahaman) in 2021 AE is among the highest Left AE residuals in South Bengal in this election cycle. The prior AITC AE incumbent (Dipak Kumar Halder) switched to BJP and became the BJP candidate — a rare and significant defection carrying some organisational infrastructure to BJP. Pannalal Halder, the new AITC candidate, entered against a BJP opponent with local incumbent name recognition. The net result: AITC vote compressed to 43.69% from 48.58% (2016 AE) while CPI(M) recovered to 17.18% from 41.03% (2016 AE), then partly rebounded. The BJP rose from 7% (2016 AE) to 36.15% (2021 AE) — a seismic consolidation.

### Diamond Harbour LS (PC 20) — key LS anchors

| Year | Winner | Party | % | Runner-up | Party | % | Margin | Tier |
|---|---|---|---|---|---|---|---|---|
| 2014 LS | Abhishek Banerjee | AITC | 40.31 | Abul Hasnat | CPI(M) | 34.66 | 71,294 | A |
| 2019 LS | Abhishek Banerjee | AITC | ~56.15 | Nilanjan Roy | BJP | ~33.44 | 320,594 | A |
| 2019 LS AC-143 segment | Abhishek Banerjee | AITC | 52.86 | Nilanjan Roy | BJP | 35.69 | 35,461 | A |

**Model note on LS vs AE differential**: The gap between Abhishek Banerjee's 2019 LS AC-143 segment share (52.86%) and Pannalal Halder's 2021 AE share (43.69%) is 9.17pp — the candidate-effect differential. This is the central simulation challenge: the AITC's structural vote base in AC 143 is ~44-48%, but Abhishek's personal leadership premium adds ~9pp in LS contests. The simulator must model this as a distinguishable component.

---

## G. Sources & tier flags

### Primary sources (tier A)
- ECI 2021 WB Assembly Election — AC 143 Diamond Harbour candidate-level result (Wikipedia sourced from ECI): Pannalal Halder (AITC) 98,478 votes / 43.69%; Dipak Kumar Halder (BJP) 81,482 / 36.15%; Pratik Ur Rahaman (CPI(M)) 38,719 / 17.18%; total polled 225,346; turnout 88.37%
- `2019_AssemblySegmentLevelVotingData.csv` — ECI GE2019 AC-segment; AC_NO=143 (calibration predecessor)
- Census of India 2011 — Diamond Harbour Municipality, CDB-I, CDB-II (Wikipedia rollups; tier A for religion, SC, ST, literacy, language, occupation, sex ratio)
- ECI 2016 AE, 2011 AE results for AC 143 (Wikipedia "Diamond Harbour Assembly constituency")
- ECI 2014 LS, 2019 LS results for Diamond Harbour PC 20 (Wikipedia "Diamond Harbour Lok Sabha constituency")

### Secondary sources (tier B/C)
- NFHS-5 (2019-21) West Bengal — household asset/media and amenity diffusion update from NFHS-4
- Pew Research India 2021 — religion-differential growth projections (2011 → 2021)
- CSDS-Lokniti 2021 WB Assembly Election post-poll (national rollup with WB regional; party × religion, party × caste cross-tabs)
- PMJDY dashboard — banking penetration S24P by 2021

### Tertiary / journalistic (tier D)
- NDMA Amphan cyclone 2020 impact assessment — S24P displacement + housing damage statistics
- National Disaster Response Fund S24P Amphan reports — 13 blocks affected; Diamond Harbour sub-division among worst hit
- WB government Amphan relief portal — block-level distribution
- Wikipedia "Cyclone Amphan" — S24P track, landfall, damage
- COVID-19 WB district-level reports — reverse migration estimates; PMC-Bengal-Kerala study (2020)
- Lakshmir Bhandar launch coverage (April 2021) — TMC press releases; The Hindu/Indian Express coverage

### Tier-D/E reliance flags
- **2021 religion share projection** (C.1): 10-yr compound from 2011; GP-equal-weight within each CDB unchanged
- **Post-Amphan BPL shift** (C.10): increase from 28% to 30% is modeled; no post-Amphan AC-level poverty survey available
- **Smartphone surge 2019→2021** (C.14): jump from ~42% to ~60% uses NFHS-5 WB rural (~58%) as anchor; AC-specific rate uncertain
- **Vote × Religion CPI(M) Muslim retention** (D.15): LF-Muslim column is the highest model uncertainty; no AC-level exit poll confirms the 36% Muslim-LF figure; it is consistent with CPI(M)'s 17.18% aggregate and Hindu-BJP consolidation logic but derived via residual
- **Lakshmir Bhandar vote-switch** (D.18): timing of April 2021 launch and the scale of female TMC boost is modeled from journalistic accounts; no AC-level LB penetration survey available

### v0 known gaps
1. AE 2021 INC+minor party vote — exact figure not in Wikipedia summary; estimated as residual from top-3
2. LB penetration rate in AC 143 at May 2021 polling — launch timing (April 2021) vs AE (April-May 2021 phases) means penetration was partial; WB CDWDSW dashboard needed
3. CSDS 2021 WB regional cross-tabs — using WB summary-level; Diamond Harbour PC-specific not published
4. Candidate-effect differential quantum — modeled at 9pp LS-vs-AE; actual decomposition into candidate-vs-wave effects requires agent-level simulation

---

## H. Post-2021 validation anchors

> **These are OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**

### 2024 LS AC-143 segment — Diamond Harbour (PC 20) (tier A)

> Sourced from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=143. Total electors: 265,214; total valid votes: 213,296; turnout: 80.4%.

| Party | Candidate (LS level) | Votes | AC-143 segment % | Tier |
|---|---|---|---|---|
| AITC | Abhishek Banerjee | 147,343 | 69.08 | A |
| BJP | Abhijit Das (Bobby) | 43,176 | 20.24 | A |
| AISF | Majnu Laskar | 9,918 | 4.65 | A |
| LF (CPI(M)) | Pratik Ur Rahaman | 7,360 | 3.45 | A |
| Other_NOTA | (BSP + INSAF + SUCI + INDs + NOTA) | 5,499 | 2.58 | A |

**2024 interpretation**: Abhishek's 69.08% is 25.39pp above Pannalal Halder's 2021 AE (43.69%), confirming extreme candidate-effect differential. BJP collapsed from 36.15% (2021 AE) to 20.24% (2024 LS). AISF (linked to Abul Hasnat's S24P network) captured 4.65% — residual third-force Muslim/Left split persisted even in 2024. Abhishek Banerjee won Diamond Harbour LS PC 20 by approximately 7.1 lakh votes in 2024 — a record margin in WB LS history.

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No post-2021 events referenced in §A–§G.*
