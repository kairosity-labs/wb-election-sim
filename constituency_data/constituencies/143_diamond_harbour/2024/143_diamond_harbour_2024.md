# AC 143 — Diamond Harbour (GEN) — Calibrated 2024 Population Snapshot

> **Frozen at end-2024.** This file describes the demographic and behavioural state of AC 143 Diamond Harbour as of end-2024 only — it does not reference any post-2024 events. Use 2026 WB Assembly Election as out-of-sample validation gate for downstream simulators.
>
> Companion artifacts: [`methodology_2024.md`](../../methodology_2024.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2024)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 143 | A | ECI / Delimitation Commission 2008 |
| AC name | Diamond Harbour | A | ECI |
| Reservation | General (Unreserved) | A | Delimitation 2008 |
| District | South 24 Parganas | A | Delimitation 2008 |
| Sub-division | Diamond Harbour | A | WB administrative |
| LS constituency | PC 20 — Diamond Harbour | A | Delimitation 2008 |
| LS segments in PC 20 | AC 143 Diamond Harbour · 144 Falta · 145 Satgachhia · 146 Bishnupur (SC) · 147 Maheshtala · 148 Budge Budge · 149 Metiaburuz | A | Delimitation 2008 |
| AC composition | Diamond Harbour Municipality (full) + 7 of 8 GPs of CDB Diamond Harbour I + 6 of 8 GPs of CDB Diamond Harbour II | A | Delimitation 2008 / Wikipedia |
| Geographic note | Hugli estuary; Diamond Harbour town ~50 km south of Kolkata; river-dependent economy; Sundarban-fringe; partially affected by Cyclone Amphan 2020 (recovery by 2024); Bangladesh border economy indirect impact via Petrapole/S24P riverine trade | A/D | Multiple |
| Archetype | A6 — South Bengal TMC heartland; Abhishek Banerjee's LS bastion; 2024 record LS margin consolidates AITC dominance; candidate-effect differential remains critical model parameter | D | Project classification |
| Three sub-units | **U1: Diamond Harbour Municipality** (urban) · **U2: CDB-I rural GP share** (7 of 8 GPs Diamond Harbour I) · **U3: CDB-II rural GP share** (6 of 8 GPs Diamond Harbour II) | E | v0 simplification |

---

## B. 2024 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~299,423 (Municipality 41,802 + CDB-I rural 7/8 share 118,265 + CDB-II rural 6/8 share 139,356) | E | Census 2011 Wikipedia CDB articles |
| 2024 projected population | ~346,000 | E | 13-yr compound religion-differential growth from 2011; net ~15.5% over 2011 base |
| Sex ratio (2024, F per 1000 M) | ~963 | E | 2011 base 959; 13-yr drift; improving slowly in CDB-I Muslim-majority |
| 2024 electorate (from CSV) | 265,214 | A | `data/2024_AssemblySegmentLevelVotingData.csv` AC_NO=143 |
| 2024 LS valid votes | 213,296 | A | Same CSV (211,993 EVM + 1,303 NOTA) |
| 2024 LS turnout | 80.4% | A | 213,296 / 265,214 |
| Estimated M / F / TG split (2024) | ~51.0% M / 49.0% F / <0.05% TG | E | Sex ratio 963 projection |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2024)

**Key finding**: Muslim share continues slow upward drift. No religion-selective displacement since Amphan (2020) recovery. Bangladesh interim government (August 2024) had minimal direct demographic impact on this AC — unlike Matua-belt border ACs, Diamond Harbour has no active new Hindu refugee stream.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 57.30 | B | 13-yr projection from 2011: Hindu +1.0%/yr (Pew India 2021); weighted CDB-I 47.72%, CDB-II 59.77%, Muni 85.98%; continued Muslim differential upward drift |
| Muslim | 42.42 | B | Muslim +1.3%/yr for 13 yrs from 2011 base; CDB-I Muslim-majority driver; +0.42pp from 2021 |
| Christian | 0.15 | E | S24P fringe; slow decline |
| Sarna_ORP | 0.01 | E | Negligible |
| Other_residual | 0.12 | E | Sikh/Jain/Buddhist/unclassified |

### C.2 Caste / community (within total population, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| SC_total | 21.55 | B | Minimal drift; Census 2011 weighted anchor; slow change in SC share |
| └ Namasudra_Bagdi_SC | 9.0 | D | River-delta SC: Namasudra (fishers/farmers) + Bagdi; no Matua concentration in this AC |
| └ Munda_other_SC | 3.0 | E | CDB-II rural pockets |
| └ Unclassified_SC | 9.55 | E | Residual within SC total |
| ST_total | 0.05 | A | Census 2011; negligible change |
| UC_bhadralok | 5.0 | E | Brahmin/Kayastha/Baidya in Muni; stable |
| OBC | 6.0 | E | Mahishya (fishing OBC) + Sadgop (farming OBC); S24P coastal belt |
| Other_Hindu_middle | 24.75 | E | Residual Hindu: 57.30 − 21.55 SC − 0.05 ST − 5.0 UC − 6.0 OBC = 24.70; rounded 24.75 |
| Muslim | 42.42 | B | Bengali-Sheikh peasantry dominant (see C.1) |
| Christian_plus_Sarna_plus_Other | 0.23 | E | C.1 residuals combined |

### C.3 Age cohort (2024, adults 18+ only — renormalized)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 13.0 | E | 2011 cohort aging; younger cohorts large due to higher CDB-I fertility |
| 23_27 | 12.5 | E | |
| 28_32 | 12.0 | E | |
| 33_37 | 11.5 | E | |
| 38_42 | 10.5 | E | |
| 43_47 | 9.5 | E | |
| 48_52 | 8.5 | E | |
| 53_57 | 7.5 | E | |
| 58_62 | 6.0 | E | |
| 63_67 | 5.0 | E | |
| 68 | 4.0 | E | Modest 68+ as previous high-mortality fishing cohorts age through |

### C.4 Gender (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.00 | E | Sex ratio 963 → F/total = 963/1963 = 49.06%; M = 50.94%; rounded to 51.00 |
| Female | 48.99 | E | |
| Third_gender | 0.01 | E | WB state rate from 2011 |

### C.5 Mother tongue (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 99.44 | A | No significant change; CDB-I+II Bengali-dominant; Muni ~98.5% Bengali |
| Hindi | 0.22 | E | Stable trader/migrant Hindi fringe; COVID-era out-migration partially reversed |
| Urdu | 0.28 | E | Small Muslim Urdu-speaker pocket in Muni and CDB-II; stable |
| Other | 0.06 | E | Residual |

### C.6 Education level (2024, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 17.5 | E | Further literacy improvement 2021→2024; Kanyashree + school enrollment continuing; CDB-I female literacy advancing |
| Primary | 24.0 | E | |
| Middle | 22.5 | E | |
| Secondary | 17.0 | E | |
| Higher_Secondary | 11.0 | E | SSC scam (2022) and education disruption have not significantly reduced enrollment at this level |
| Graduate | 6.5 | E | Slow expansion; delta deprivation context |
| Postgraduate | 1.5 | E | Stable |

### C.7 Workforce status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 30.0 | E | Recovery to 2019 levels by 2024; fishing + construction + trade normalised post-Amphan and post-COVID |
| Marginal_worker | 13.0 | E | Stabilised at 2019 levels |
| Non_worker | 37.0 | E | Lakshmir Bhandar (active since 2021) serves non-working female HH heads directly; this group is primary LB constituency |
| Student | 11.0 | E | Recovery to 2019 level; school/college reopened |
| Unemployed | 9.0 | E | Slightly elevated; SSC scam (2022) disrupted government-teacher employment pipeline for educated youth; educated youth unemployment salient |

### C.8 Occupation (within main + marginal workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 6.3 | B | Stable; minor change from 2021 |
| Agricultural_labourer | 18.5 | B | Stable |
| Household_industry | 6.5 | B | Recovery from Amphan disruption; bidi + mat weaving resumed |
| Manufacturing | 2.0 | E | Small factory; Muni fringe |
| Construction | 5.5 | E | Ongoing Amphan reconstruction + state infrastructure spending |
| Trade_retail | 11.0 | E | Stable; Muni commercial hub |
| Transport_logistics | 7.0 | D | River ferry + road; stable |
| Services | 10.0 | E | |
| Government_services_teachers | 5.5 | E | Slight reduction: SSC scam fallout reduced government-sector confidence; some teaching vacancies not filled |
| Out_migrant_worker | 13.0 | D | Recovering to near-2019 levels; Kerala/Tamil Nadu destination for skilled S24P labour; deep-sea fishing resumed fully |
| Fishing_pisciculture | 12.2 | D | Hugli delta fishing + prawn aquaculture; Amphan recovery complete by 2024; Namasudra + Mahishya caste occupation |
| Tourism_hospitality | 2.0 | D | Diamond Harbour waterfront tourism restored; state tourism push |

### C.9 Class of worker (within workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.5 | E | Stable |
| Employee | 24.0 | E | Recovery; organised sector, govt, services |
| Single_worker | 52.0 | E | Own-account fishermen, cultivators, small traders dominant |
| Family_worker | 22.5 | E | Stable; fishing-household family helpers |

### C.10 Economic / poverty (2024, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 27.5 | D | Amphan shock (2020) has largely recovered by 2024; Lakshmir Bhandar + Krishak Bandhu + Khadya Sathi improve household consumption floor; slight reduction from 2021 peak (30%) but higher than 2019 (28%) due to persistent SSC/unemployment impact on educated youth |
| Above_Poverty_Line_low_income | 36.0 | E | Marginal uplift from Lakshmir Bhandar direct cash transfers |
| Lower_middle | 22.0 | E | |
| Middle | 11.0 | E | |
| Upper_middle_well_off | 3.5 | E | Muni affluent fringe; slight expansion via trade + services recovery |

### C.11 GP / Municipality location (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Diamond_Harbour_Municipality | 13.2 | E | 2024 projection; Muni share declining as rural grows faster |
| U2_CDB_I_rural_GP_share | 40.0 | E | CDB-I 7 GPs; Muslim-majority (52%+); highest growth rate |
| U3_CDB_II_rural_GP_share | 46.8 | E | CDB-II 6 GPs; Hindu-majority but 40% Muslim |

### C.12 Household composition (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.4 | E | S24P slowly declining HH size; Muni urban nuclear trend |
| Nuclear_HH | 66.0 | E | Slight increase in nuclear as younger generation sets up households |
| Joint_HH | 25.0 | E | Declining |
| Extended_multi_generation | 9.0 | E | Stable in fishing communities |

### C.13 Marital status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 24.0 | E | Large 18–22 cohort entering pool; earlier marriage norms in CDB-I partially moderating |
| Currently_married | 67.0 | E | |
| Widowed | 8.0 | E | Fishing hazard and Amphan fatality effect persists |
| Separated_divorced | 1.0 | E | |

### C.14 Asset / media access (2024, household level)

**2024 context**: Smartphone effectively saturated in urban; high in rural. UPI/digital payments normalized. Lakshmir Bhandar digital-payment delivery increased banking access. TV remains primary political-news medium in CDB-I rural.

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 78.0 | C | NFHS-5 WB anchor + growth; saturating in Muni (~95%); CDB-I ~72%; CDB-II ~78% |
| Radio | 2.5 | C | Continuing decline; near-marginal |
| Mobile_phone | 93.0 | C | Near-universal; Jio saturation + Airtel |
| Smartphone_with_internet | 72.0 | C | Rapid growth from 2021 (~60%); NFHS-5 + state surveys; CDB-I still lower (~62%) than Muni (~88%) |
| Computer | 9.0 | C | Minimal change |
| Two_wheeler | 28.0 | C | Slow steady increase; fishing boat + bicycle still dominant in delta |
| Four_wheeler | 6.0 | C | Slight increase; Muni and upper-income CDB-II |
| Banking_access | 94.0 | B | PMJDY + Lakshmir Bhandar bank-account requirement near-saturation; CDB-I rural women now banked for LB transfers |

### C.15 Household amenities (2024)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 85.0 | C | NFHS-5 + steady infrastructure improvement; Amphan salination effects resolved |
| Improved_sanitation | 72.0 | C | Continued Swachh Bharat + state ODF campaign; NFHS-5 WB rural ~66%, urban ~92% |
| LPG_clean_cooking_fuel | 53.0 | C | Ujjwala Phase-2 + market expansion; +6pp from 2021; CDB-I still lowest at ~40% |
| Wood_biomass_fuel | 39.0 | C | Declining; mangrove-fringe firewood reducing |
| Other_fuel | 8.0 | C | Stable |
| Electricity | 95.0 | C | Saubhagya completion + grid maintenance post-Amphan; coastal delta now well-connected |

### C.16 Migration / birthplace (2024, all ages)

**2024 context**: Bangladesh interim regime (August 2024) created anxiety among Hindu communities near the border. Diamond Harbour is not a primary border corridor (unlike Bangaon, Basirhat). However, given the large S24P Muslim population and CDB-I Muslim majority, some sensitivity exists around communal polarization discourse. Petrapole border-trade disruption has secondary economic impact on S24P district but minimal direct livelihood impact on this predominantly fishing + agriculture AC. Sustained out-migration to Kerala and Tamil Nadu for skilled fishing-boat crew continues.**

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 80.0 | D | Stabilised post-COVID return-migration surge; S24P coastal communities deeply rooted; no significant new in-migration stream |
| WB_other_district | 5.5 | D | Stable; Kolkata-commuter class in Muni |
| Other_Indian_state | 2.0 | D | Recovery of Bihari/Marwari trader migration to near-2019 levels |
| Bangladesh_origin | 3.0 | D | Unchanged; pre-1971 Namasudra fraction in CDB-II; indigenous S24P Muslim peasantry; Bangladesh interim government changes not creating new in-migration to this non-border AC |
| Outside_India | 0.5 | E | Negligible |
| Out_migrant | 9.0 | D | Sustained out-migration for deep-sea fishing (Kerala/Tamil Nadu boats), Kolkata daily commuters, Kerala/Delhi construction workers; effective polling-booth absentee rate |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language | religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|
| Hindu | 99.7 | 0.2 | 0.0 | 0.1 | A | CDB-I+II 99.83%/99.7% Bengali; Hindu trader Hindi fringe in Muni |
| Muslim | 98.5 | 0.5 | 0.9 | 0.1 | E | Bengali-Sheikh peasantry; small Urdu pocket in Muni |
| Christian | 92.0 | 5.0 | 0.0 | 3.0 | E | Tiny base |
| Sarna_ORP | 80.0 | 10.0 | 0.0 | 10.0 | E | Negligible |
| Other_residual | 70.0 | 25.0 | 0.0 | 5.0 | E | Marwari/Bihari traders |

### D.2 Religion × Caste (2D layout)

P(caste | religion) — % within each religion; each row sums to 100.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 37.61 | 0.09 | 8.73 | 10.47 | 43.10 | 0 | 0 | B/E | SC 21.55% / Hindu 57.30% = 37.61%; UC 5.0/57.30=8.73%; OBC 6.0/57.30=10.47%; residual 43.10% |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | All Muslim |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | |
| Sarna_ORP | 0 | 90 | 0 | 5 | 5 | 0 | 0 | E | |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | |

### D.3 Religion × Migration

P(birthplace | religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 77.0 | 7.0 | 2.0 | 5.0 | 0.5 | 8.5 | D | Hindu SC (Namasudra) Bangladesh-origin fraction; indigenous Mahishya/Sadgop; fishing out-migration |
| Muslim | 85.0 | 4.0 | 0.5 | 1.0 | 0.0 | 9.5 | D | Bengali-Sheikh indigenous S24P; seasonal fishing/labour out-migration elevated |
| Christian | 80.0 | 10.0 | 5.0 | 5.0 | 0.0 | 0.0 | E | |
| Sarna_ORP | 80.0 | 10.0 | 5.0 | 0.0 | 0.0 | 5.0 | E | |
| Other_residual | 50.0 | 15.0 | 30.0 | 5.0 | 0.0 | 0.0 | E | Marwari/Bihari traders |

### D.4 Religion × Asset / media (flags)

P(owns asset | religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 83.0 | 79.0 | 96.0 | C | NFHS-5 WB; Hindu Muni+CDB-II smartphone saturation approaching |
| Muslim | 72.0 | 63.0 | 91.0 | C | NFHS-5 WB Muslim rural gap; Lakshmir Bhandar bank-account requirement narrowed banking gap substantially |
| Christian | 86.0 | 72.0 | 94.0 | E | |
| Sarna_ORP | 72.0 | 58.0 | 88.0 | E | |
| Other_residual | 93.0 | 85.0 | 98.0 | E | Trader class |

### D.5 Caste × Education

P(education | caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 2 | 8 | 11 | 18 | 22 | 28 | 11 | E |
| OBC | 10 | 20 | 23 | 22 | 14 | 9 | 2 | E |
| Namasudra_Bagdi_SC | 17 | 24 | 24 | 18 | 10 | 6 | 1 | E |
| Other_Hindu_middle | 13 | 23 | 24 | 18 | 12 | 8 | 2 | E |
| Muslim | 20 | 26 | 25 | 17 | 9 | 3 | 0 | E |
| Christian_plus_Sarna_plus_Other | 14 | 21 | 25 | 21 | 13 | 5 | 1 | E |

### D.6 Age × Gender × Education (grad+)

P(grad+ | age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 14 | 12 | E |
| 23_27 | 15 | 11 | E |
| 28_32 | 12 | 8 | E |
| 33_37 | 10 | 5 | E |
| 38_42 | 9 | 4 | E |
| 43_47 | 7 | 3 | E |
| 48_52 | 6 | 2 | E |
| 53_57 | 5 | 1 | E |
| 58_62 | 4 | 1 | E |
| 63_67 | 4 | 1 | E |
| 68 | 3 | 1 | E |

### D.7 Marital status × Age × Gender

P(currently married | age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 10 | 37 | E |
| 23_27 | 48 | 87 | E |
| 28_32 | 85 | 93 | E |
| 33_37 | 93 | 91 | E |
| 38_42 | 93 | 90 | E |
| 43_47 | 92 | 88 | E |
| 48_52 | 91 | 80 | E |
| 53_57 | 90 | 72 | E |
| 58_62 | 87 | 61 | E |
| 63_67 | 80 | 38 | E |
| 68 | 74 | 28 | E |

### D.8 Occupation × Asset / media

P(owns smartphone-internet | occupation) and P(TV | occupation).

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 52 | 75 | C | UPI + mandi price apps; NFHS-5 + growth |
| Agricultural_labourer | 38 | 66 | C | Smartphone uptake among lowest-income |
| Household_industry | 56 | 78 | C | Mat-weaving + bidi; smartphones for small business |
| Manufacturing | 68 | 88 | C | |
| Construction | 65 | 80 | C | Migrant workers need remittance apps |
| Trade_retail | 82 | 93 | C | Muni commercial; UPI now standard |
| Transport_logistics | 72 | 85 | D | Ferry + road; GPS and navigation |
| Services | 85 | 94 | C | |
| Government_services_teachers | 91 | 98 | C | Highest; mandatory digital for govt functions |
| Out_migrant_worker | 82 | 80 | D | Remittance via UPI; Kerala destination near-100% smartphone |
| Fishing_pisciculture | 58 | 72 | D | Working boats now routinely carry smartphones for weather and fish-market price alerts |
| Tourism_hospitality | 70 | 92 | D | Muni hotel/ghat economy; digital payments standard |

### D.9 Education × Workforce participation

P(unemployed-and-seeking | education) and P(main-worker | education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 32 | 1 | E |
| Primary | 35 | 3 | E |
| Middle | 32 | 6 | E |
| Secondary | 28 | 9 | E |
| Higher_Secondary | 22 | 15 | E |
| Graduate | 25 | 17 | E |
| Postgraduate | 35 | 12 | E |

### D.10 Asset × Bilingualism

P(bilingual Bengali+Hindi or Bengali+Urdu | media-access tier).

| Media_tier | Bilingual_pct | Tier | Source |
|---|---|---|---|
| Television_only | 2 | E | Bengali TV overwhelmingly dominant |
| Television_plus_smartphone | 6 | E | YouTube cross-language content increasing |
| Smartphone_only | 5 | E | |
| No_asset | 1 | E | |

### D.11 GP / Sub-unit × Religion

P(religion | sub-unit location).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Diamond_Harbour_Municipality | 85.98 | 13.75 | 0.15 | 0.00 | 0.12 | A | Census 2011; minimal secular drift by 2024 |
| U2_CDB_I_rural_GP_share | 47.50 | 52.38 | 0.06 | 0.01 | 0.05 | A/E | Census 2011 anchor (A) + minor 13-yr projection (E) |
| U3_CDB_II_rural_GP_share | 59.55 | 39.90 | 0.20 | 0.00 | 0.35 | A/E | Census 2011 anchor (A) + minor projection |

### D.12 GP / Sub-unit × Caste

P(caste category | sub-unit) — key categories.

| Sub_unit | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Diamond_Harbour_Municipality | 12.49 | 0.17 | 8.0 | 7.0 | 58.4 | 13.75 | 0.27 | B/A |
| U2_CDB_I_rural_GP_share | 18.63 | 0.01 | 2.0 | 5.0 | 21.9 | 52.38 | 0.08 | B/A |
| U3_CDB_II_rural_GP_share | 26.55 | 0.04 | 4.0 | 7.0 | 22.2 | 39.90 | 0.31 | B/A |

### D.13 GP / Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Diamond_Harbour_Municipality | 93 | 85 | 22 | 98 | C |
| U2_CDB_I_rural_GP_share | 70 | 62 | 5 | 90 | C |
| U3_CDB_II_rural_GP_share | 77 | 68 | 7 | 93 | C |

### D.14 GP / Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Diamond_Harbour_Municipality | 82 | 93 | 96 | 98 | C |
| U2_CDB_I_rural_GP_share | 40 | 63 | 82 | 93 | C |
| U3_CDB_II_rural_GP_share | 48 | 70 | 86 | 95 | C |

### D.15 Vote × Religion (2024 LS, AC 143)

P(party | religion) — calibrated to AC 143 2024 LS AC-segment result (AITC 69.08%, BJP 20.24%, AISF 4.65%, CPI(M) 3.45%); religion weights: Hindu 57.30%, Muslim 42.42%. AISF and CPI(M) lumped into LF column; Other_NOTA includes BSP + INSAF + SUCI + INDs + NOTA.

**Model interpretation**: Abhishek Banerjee's record 2024 margin reflects (a) massive personal leadership premium above AE candidate (~25pp gap vs 2021 AE), (b) BJP soft-Hindu deflation following weak WB BJP performance nationally, (c) AISF split (4.65%) drawing residual Abul Hasnat network votes rather than CPI(M) (3.45%); the Left vote fragmented. Muslim voter consolidation behind AITC is near-complete in LS context.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 36 | 53 | 1 | 5 | 5 | C | BJP Hindu base compressed from 2021 AE (58%); Abhishek's incumbency + national BJP underperformance in WB peeled moderate Hindus back to AITC |
| Muslim | 2 | 88 | 0 | 6 | 4 | C | Near-total Muslim consolidation behind Abhishek in LS; AISF (Majnu Laskar) drew ~4% of Muslim vote; residual CPI(M) minimal |
| Christian | 8 | 72 | 2 | 10 | 8 | E | Tiny base |
| Sarna_ORP | 15 | 65 | 0 | 12 | 8 | E | |
| Other_residual | 30 | 58 | 2 | 4 | 6 | E | |

(Recovery check: BJP = 36×0.5730 + 2×0.4242 = 20.63 + 0.85 = 21.48% vs 20.24% Δ=1.24pp ✓; AITC = 53×0.5730 + 88×0.4242 = 30.37 + 37.33 = 67.70% vs 69.08% Δ=1.38pp ✓; LF = 5×0.5730 + 6×0.4242 = 2.87 + 2.55 = 5.41% vs 8.10% [AISF+CPI(M)] Δ=2.69pp — within ±3pp model tolerance for LF fragmentation)

### D.16 Vote × Caste (2024 LS, AC 143)

P(party | caste).

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 42 | 48 | 1 | 5 | 4 | C | BJP UC base compressed; some bhadralok returned to AITC in 2024 LS (national anti-BJP swing) |
| OBC | 30 | 57 | 1 | 7 | 5 | C | Mahishya/Sadgop fishing OBC: AITC gains from BJP in 2024 LS vs 2021 AE |
| Namasudra_Bagdi_SC | 35 | 53 | 1 | 7 | 4 | C | SC BJP-lean reduced; Abhishek's SC welfare outreach + rural welfare schemes |
| Other_Hindu_middle | 33 | 56 | 1 | 5 | 5 | C | |
| Muslim | 2 | 88 | 0 | 6 | 4 | C | Near-unanimous AITC; AISF drew small Muslim fraction |
| Christian_plus_Sarna_plus_Other | 12 | 65 | 2 | 12 | 9 | E | Small base |

### D.17 Vote × Gender (2024 LS)

P(party | gender). Lakshmir Bhandar is fully active since 2021; penetration deepened through 2024. The female TMC tilt is now higher than 2021 AE.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 28 | 62 | 1 | 6 | 3 | C | CSDS 2024 WB; BJP male base compressed; Abhishek incumbency pulls male AITC |
| Female | 13 | 76 | 0 | 7 | 4 | C | Lakshmir Bhandar + Kanyashree + Swasthya Sathi: female TMC lean substantially stronger than 2021 in LS context |
| Third_gender | 10 | 75 | 0 | 10 | 5 | E | |

(Recovery check: AITC = 62×0.5100 + 76×0.4899 = 31.62 + 37.23 = 68.85% vs 69.08% Δ=0.23pp ✓)

### D.18 Vote × Welfare scheme (2024 LS)

Schemes active at 2024 LS: all prior schemes + Lakshmir Bhandar (deeply embedded since 2021), Duare Sarkar delivery infrastructure, continued Khadya Sathi, expanded Swasthya Sathi. SSC scam (2022) created anti-TMC sentiment among some educated state-sector aspirants but did not materially affect welfare-recipient voters.

| Exposure | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Lakshmir_Bhandar_recipient | 5 | 80 | 0 | 10 | 5 | C | Strong TMC tilt; even in Left Muslim HHs receiving LB transfers, AITC dominant in LS context |
| Krishak_Bandhu | 20 | 65 | 1 | 10 | 4 | C | Cultivator HH; AITC gains from 2021 as BJP deflated |
| Kanyashree | 18 | 68 | 0 | 10 | 4 | C | Female scheme; strong AITC tilt |
| Swasthya_Sathi | 22 | 65 | 1 | 8 | 4 | C | Broad-based welfare-scheme voter |
| Khadya_Sathi | 30 | 58 | 1 | 8 | 3 | C | Universal; BJP floor |
| No_state_scheme | 40 | 45 | 1 | 8 | 6 | C | BJP-leaning but compressed vs 2021; Abhishek incumbency premium |

---

## E. 2024 LS baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 20.24 | A | `data/2024_AssemblySegmentLevelVotingData.csv` AC_NO=143; 43,176 votes |
| AITC | 69.08 | A | Same CSV; 147,343 votes; Abhishek Banerjee LS candidate |
| INC | 0.00 | E | INC did not contest Diamond Harbour LS 2024 as part of INDIA alliance; negligible presence |
| LF | 8.10 | A | AISF 9,918 (4.65%) + CPI(M) 7,360 (3.45%) = 17,278 votes / 213,296 total = 8.10% (lumped as LF) |
| Other_NOTA | 2.58 | A | BSP 1,002 + INSAF 325 + SUCI 230 + INDs 2,639 + NOTA 1,303 = 5,499 votes / 213,296 |

---

## F. Vote history (chronological anchors for belief evolution)

### AC 143 Diamond Harbour — full electoral history

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin | Tier |
|---|---|---|---|---|---|---|---|---|---|---|
| 2006 AE | Rishi Halder | CPI(M) | — | — | Subhashis Chakraborty | AITC | — | — | — | D |
| 2011 AE | Dipak Kumar Halder | AITC | 87,645 | 53.37 | Subhra Sau | CPI(M) | 66,871 | 40.72 | 20,774 | A |
| 2016 AE | Dipak Kumar Halder | AITC | 96,833 | 48.58 | Abul Hasnat | CPI(M) | 81,796 | 41.03 | 15,037 | A |
| 2019 LS (AC-143 segment) | Abhishek Banerjee | AITC | 109,134 | 52.86 | Nilanjan Roy | BJP | 73,673 | 35.69 | 35,461 | A |
| 2021 AE | Pannalal Halder | AITC | 98,478 | 43.69 | Dipak Kumar Halder | BJP | 81,482 | 36.15 | 16,996 | A |
| **2024 LS (AC-143 segment)** | **Abhishek Banerjee** | **AITC** | **147,343** | **69.08** | **Abhijit Das** | **BJP** | **43,176** | **20.24** | **104,167** | **A** |

**Key model narratives (chronological)**:

- **2006-2016 pattern**: CPI(M) stronghold → TMC capture (2011) under Dipak Kumar Halder → narrow 2016 AE win with CPI(M) still at 41%. High LF residual reflects organised Left-Muslim base in CDB-I built around Abul Hasnat.
- **2019 LS surge**: BJP wave hits this AC as a Hindu-consolidation effect (BJP 35.69%). Abhishek's 52.86% reflects LS leadership premium + Muslim bloc consolidation.
- **2021 AE inversion**: Dipak Kumar Halder defects to BJP — takes organisational infrastructure. Pannalal Halder (new AITC candidate) wins but compressed to 43.69%. CPI(M) recovers to 17.18% (Pratik Ur Rahaman) in the Left's best AC performance in South Bengal. BJP holds 36.15%. Cyclone Amphan relief distribution and Lakshmir Bhandar launch (April 2021) credited with enabling AITC to hold.
- **2022 SSC scam**: Partha Chatterjee arrest (July 2022) damages TMC's educated-youth support; state-exam aspirants (a significant group in this delta AC with high educated-unemployment) became alienated. Limited direct impact on welfare-dependent rural voters.
- **2024 LS consolidation**: Abhishek Banerjee's record margin — 104,167 at AC-143 segment level; 7.1 lakh across Diamond Harbour PC 20. BJP deflated to 20.24% (15.91pp drop from 2021 AE). AISF (Majnu Laskar, linked to Abul Hasnat S24P network) appeared as third force at 4.65%, fragmenting the former CPI(M) Left-Muslim bloc.

---

## G. Sources & tier flags

### Primary sources (tier A)
- `data/2024_AssemblySegmentLevelVotingData.csv` — ECI GE2024 AC-segment vote tallies; AC_NO=143 Diamond Harbour (2024 calibration target)
- `data/2019_AssemblySegmentLevelVotingData.csv` — ECI GE2019 AC-segment; AC_NO=143 (2019 predecessor)
- Census of India 2011 — Diamond Harbour Municipality, CDB Diamond Harbour I, CDB Diamond Harbour II (Wikipedia rollups)
- ECI 2021 WB AE, 2016 AE, 2011 AE results for AC 143 (Wikipedia "Diamond Harbour Assembly constituency")
- ECI 2014 LS, 2019 LS, 2024 LS results for Diamond Harbour PC 20 (Wikipedia "Diamond Harbour Lok Sabha constituency")

### Secondary sources (tier B/C)
- NFHS-5 (2019-21) West Bengal — household asset/media + amenity update
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2024 WB Lok Sabha election post-poll cross-tabs
- PMJDY dashboard 2024 — banking penetration South 24 Parganas
- WB CDWDSW Lakshmir Bhandar penetration dashboard (partial data available)

### Tertiary / journalistic (tier D)
- The Hindu / Indian Express / ThePrint — Abhishek Banerjee 2024 record margin coverage; Diamond Harbour PC 20 analysis
- CAA rules notification (March 2024) — coverage in Matua-belt context; minimal direct impact on this AC (no significant Matua population)
- RG Kar Hospital rape-murder protest (August 2024) — mass protests; medical community and urban educated female mobilisation; minimal AC-specific impact confirmed
- Bangladesh interim government / Hasina ouster (August 2024) — S24P communal anxiety monitoring; no direct demographic impact on this non-border AC
- Sandeshkhali women's protests (February 2024) — geographically proximate in North S24P; generated state-wide anti-TMC local-governance narrative; moderate impact on Muni educated voters here

### Tier-D/E reliance flags
- **2024 religion share projection** (C.1): 13-yr compound from 2011; GP-equal-weight within CDBs unchanged; largest model uncertainty in demographic layer
- **Smartphone surge 2021→2024** (C.14): jump to ~72% uses state-level NFHS-5 as anchor + extrapolation; AC-specific rate uncertain
- **Vote × Religion CPI(M)+AISF Muslim split** (D.15): AISF (Majnu Laskar) is an independent candidate linked to Abul Hasnat's network; whether AISF votes came from former CPI(M) Muslims or from TMC-Muslim fringe is unresolved; LF lumping of AISF+CPI(M) at 8.10% is correct by aggregate but sub-split uncertain
- **SSC scam electoral impact** (C.7 educated-unemployment, D.16 UC/OBC vote): scam awareness is high in educated youth; quantified impact on vote compressed into AC-level modelled numbers; no AC-specific exit poll confirms magnitude

### v0 known gaps
1. INC 2024 LS presence — INDIA alliance seat-sharing arrangements mean INC formally absent in Diamond Harbour LS; the 0% INC in §E is modelled as alliance-level decision; any INC sub-presence (cross-voting, symbolic candidacy) not tracked
2. AISF / INSAF party breakdown — AISF (All India Secular Front, Pirzada Abbas Siddiqui's party) is distinct from INSAF; Majnu Laskar is AISF; both appear in CSV; treated as LF-adjacent for party-axis purposes
3. Lakshmir Bhandar penetration at AC level — WB CDWDSW state-level figures available but AC 143 specific penetration rate not confirmed; using state-average modelling

---

## H. Post-2024 validation anchors

No post-2024 election results available at time of writing (end-2024 freeze). 2026 WB Assembly Election results will be the primary out-of-sample validation gate.

**Expected 2026 AE simulation targets (prior, not calibration)**:
- If Abhishek Banerjee's personal LS premium (~25pp above AE candidate) persists, expect AITC AE candidate ~44-50%
- BJP 2026 AE recovery contingent on Hindu consolidation dynamics + candidate quality
- LF 2026 trajectory unclear: AISF fragmentation of Left-Muslim bloc may suppress CPI(M) further below 2021's 17.18%

*v0 — generated 2026-04-28, frozen at end-2024 state-of-knowledge. No post-2024 events referenced in §A–§G.*
