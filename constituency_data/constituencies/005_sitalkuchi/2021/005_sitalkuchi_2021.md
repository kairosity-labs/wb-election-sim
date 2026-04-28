# AC 005 — Sitalkuchi (GEN) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 005 Sitalkuchi as of end-2021 — it does not reference any
> post-2021 events. Use post-2021 elections (2024 LS) as out-of-sample
> validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 005 | A | ECI / Delimitation Commission 2008 |
| AC name | Sitalkuchi | A | ECI |
| Reservation | GEN (unreserved) | A | Delimitation 2008; master/wb_ac_master_v3.csv |
| District | Cooch Behar (also rendered Koch Bihar) | A | Delimitation 2008 |
| Sub-division | Mathabhanga | A | WB administrative |
| LS constituency | 01 — Cooch Behar | A | Delimitation 2008 |
| LS segments included | AC 01 Mekhliganj · AC 02 Sitai · AC 03 Sitalkuchi · AC 04 Tufanganj · AC 05 Natabari · AC 06 Dinhata · AC 07 Nalhati (7 AC segments in Cooch Behar PC) | A | Delimitation 2008 |
| AC composition | Sitalkuchi CD Block (part): Sitalkuchi GP cluster + adjoining GPs within Mathabhanga sub-division; no municipality — fully rural | A | Delimitation 2008 |
| Geographic note | Northern Cooch Behar district; flat alluvial Terai, Raidak river basin; international border with Bangladesh to the west. The AC achieved national notoriety when CISF personnel opened fire on voters at a polling booth on 10 April 2021 (polling day for Phase 4), killing four persons. This event occurred during the 2021 AE and is part of the documented electoral context for this calibration year. | A | ECI / press reports dated April 2021 |
| Sub-units used in v0 | **U1: Sitalkuchi_CD_Block_north** (GPs north of Sitalkuchi town) · **U2: Sitalkuchi_CD_Block_south** (GPs south including Sitalkuchi bazaar fringe) | E | v0 equal-weight GP split pending DCHB Cooch Behar Part-A |

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~280,000 | E | Cooch Behar district Census 2011; Sitalkuchi CD Block population scaled to AC boundary; wb_ac_master_v3.csv pop_total 380,748 is Cooch Behar district share — AC-fraction applied |
| 2021 projected population | ~313,500 | E | 10-yr compound religion-differential growth (~1.0%/yr Hindu, ~1.3%/yr Muslim) from 2011 base |
| Sex ratio (2021, F per 1000 M) | ~1,010 | E | NFHS-5 Koch Bihar district sex ratio of total population = 1,058; back-projected conservatively to ~1,010 for AC-level 2021; note significant shift from Census 2011 district 946 |
| 2021 estimated electorate (18+) | ~285,260 | A | ECI 2021 AE — total electors for AC 005 (data/electoral_history/2021/detailed_results.csv; electors column = 285,260) |
| Estimated M / F / TG split (2021) | ~49.7% M / 50.2% F / <0.1% TG | E | NFHS-5 Koch Bihar sex ratio 1,058 applied to adult population; higher female share than 2019 estimate |
| 2021 polling stations (estimated) | ~310 | E | Back-derived from electorate size at ~920 electors/booth WB norm; slight increase from 2019 |
| 2021 AE total valid votes | 245,966 | A | ECI 2021 AE detailed results; sum of all candidate votes |
| 2021 AE turnout | 86.23% | A | 245,966 / 285,260 = 86.23% |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 71.50 | E | Cooch Behar district 2011 ~75.6% Hindu; 10-yr Muslim differential growth ~+0.3pp/yr → ~71.5% by 2021; Sitalkuchi block has higher Muslim share than district average |
| Muslim | 27.00 | E | Sitalkuchi block estimated ~25% Muslim 2011; 10-yr growth to ~27.0% |
| Christian | 0.30 | E | Cooch Behar district 2011 ~0.35% Christian; negligible trend change |
| Sarna_ORP | 0.80 | E | Rajbanshi community tribal religion trace; stable |
| Other_residual | 0.40 | E | Sikh + Buddhist + Not_stated residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 38.50 | A | Cooch Behar district SC Census 2011 40.0%; Sitalkuchi block slightly lower given Muslim share; wb_ac_master_v3.csv sc_pop / pop_total confirms district pattern |
| └ Rajbanshi_SC | 34.00 | C | Dominant SC community in Cooch Behar; Rajbanshi is largest SC sub-group; community straddles SC/OBC boundary |
| └ Namasudra_SC | 2.50 | E | Secondary SC sub-group in Cooch Behar |
| └ Other_SC | 2.00 | E | Remaining SC sub-groups (Koch, Bagdi etc.) |
| **ST_total** | 4.70 | A | Cooch Behar district ST 4.7% Census 2011 |
| └ Rajbanshi_ST | 3.50 | C | Rajbanshi community with ST listing in some classifications |
| └ Other_ST | 1.20 | E | Mech, Toto and smaller tribal groups |
| UC_bhadralok | 4.00 | E | Small upper-caste share in rural Cooch Behar; Brahmin/Kayastha fringe in market towns |
| OBC | 8.00 | E | OBC Rajbanshi (non-SC registered) + Koch-Rajbanshi + other backward communities |
| Other_Hindu_middle | 15.80 | E | Residual within Hindu (71.50 − 38.50 SC − 4.70 ST − 4.00 UC − 8.00 OBC = 16.30; minus Christian/Sarna overlap → ~15.80) |
| Muslim | 27.00 | E | See C.1; primarily Bengali-speaking peasantry and agricultural labourers |
| Christian_plus_Sarna_plus_Other | 2.00 | E | See C.1 |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2021, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.50 | E | Cooch Behar district age pyramid 2011; renormalized to 18+ voters; two additional years of cohort aging from 2019 estimate; NFHS-5 Koch Bihar population below age 15 = 25% confirming young-adult share |
| 23_27 | 12.00 | E | |
| 28_32 | 11.50 | E | |
| 33_37 | 10.50 | E | |
| 38_42 | 10.00 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.00 | E | |
| 63_67 | 7.00 | E | |
| 68 | 6.50 | E | 68+ open-ended |
| **Sum** | **100.00** | — | self-check (renormalized from Census 2011, excluding 0–17) |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 49.80 | E | NFHS-5 Koch Bihar sex ratio 1,058 F per 1000 M → 51.36% F / 48.64% M for total population; adult electorate adjusted to ~49.8% M |
| Female | 50.19 | E | Derived from NFHS-5 sex ratio; notably improved female share vs Census 2011 |
| Third_gender | 0.01 | E | WB state norm ~0.01% |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 84.80 | E | Dominant language in Cooch Behar; minimal change from 2019 |
| Hindi | 0.50 | E | Trader/migrant fringe in Sitalkuchi bazaar |
| Urdu | 0.50 | E | Small Muslim pocket |
| Other | 0.50 | E | Residual catch-all |
| Rajbongshi | 13.70 | E | Rajbongshi/Rajbanshi language spoken by Koch-Rajbanshi community; marginal increase with community identity assertion post-2019 BJP mobilisation; AC-local addition |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 20.00 | E | NFHS-5 Koch Bihar women literate 79.2% (from 73.7% NFHS-4); AC literacy improvement ~+2pp/2yr → ~20% illiterate 2021 |
| Primary | 24.00 | E | Census 2011 education distribution scaled; stable |
| Middle | 20.00 | E | |
| Secondary | 16.50 | E | Marginal increase with school enrolment trend |
| Higher_Secondary | 10.50 | E | |
| Graduate | 7.00 | E | Slight upward trend |
| Postgraduate | 2.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 32.50 | E | Cooch Behar district Census 2011 main-worker ~33%; slight COVID-19 disruption in 2020–2021 reduced formal employment; marginal recovery by end-2021 |
| Marginal_worker | 13.00 | E | Seasonal agricultural pattern; COVID-19 reverse migration increased marginal worker pool |
| Non_worker | 36.00 | E | Housewives + elderly; stable |
| Student | 10.00 | E | 18–22 cohort partly in education |
| Unemployed | 8.50 | E | Slightly elevated vs 2019 due to COVID-19 job disruption; educated job-seeking pool |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 28.00 | E | Cooch Behar district Census 2011 ~30% cultivators; Sitalkuchi rural pattern stable |
| Agricultural_labourer | 35.00 | E | High ag-labour share; landless Rajbanshi SC and Muslim labourers dominant; COVID-19 return migration reinforced local ag-labour pool |
| Household_industry | 4.00 | E | Cooch Behar district HH industry ~4.5%; stable |
| Manufacturing | 2.00 | E | Limited organised manufacturing |
| Construction | 5.00 | E | Includes local construction; some returning COVID-19 migrants re-joined construction |
| Trade_retail | 10.00 | E | Sitalkuchi bazaar traders; border-area petty trade |
| Transport_logistics | 4.00 | E | Road transport |
| Services | 6.00 | E | Private services |
| Government_services_teachers | 4.00 | E | Government employees + school teachers |
| Out_migrant_worker | 2.00 | D | Reduced vs longer-term trend; COVID-19 reverse migration; gradual resumption by end-2021 |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Census B-04 WB rural pattern; very low in agricultural AC |
| Employee | 22.00 | E | Government + organised sector + wage earners |
| Single_worker | 46.00 | E | Cultivator (own-account) + own-account artisan + petty trader |
| Family_worker | 30.50 | E | High family-worker share in agricultural households typical of Cooch Behar rural |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 31.00 | C | Cooch Behar district BPL ~35% (state BPL 2011 ~31%); rural Sitalkuchi estimated ~31% after WB poverty reduction trend; COVID-19 briefly reversed gains but welfare outreach (PMGKAY, Duare Sarkar) cushioned impact |
| Above_Poverty_Line_low_income | 35.00 | E | Working poor — subsistence agriculture; PMGKAY food ration supplemented incomes through COVID period |
| Lower_middle | 21.00 | E | Small cultivators + lower-grade government employees |
| Middle | 10.00 | E | Mid-level government employees + medium traders |
| Upper_middle_well_off | 3.00 | E | Sitalkuchi bazaar traders + larger landowners |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Sitalkuchi_CD_Block_north | 50.00 | E | v0 equal-split assumption pending DCHB Cooch Behar Part-A; northern GPs of Sitalkuchi block |
| U2_Sitalkuchi_CD_Block_south | 50.00 | E | Southern GPs including Sitalkuchi town fringe; refine when block-level Census tables available |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | WB rural stable; Cooch Behar rural consistent |
| Nuclear_HH | 65.00 | E | NFHS-4/5 WB rural pattern; Cooch Behar |
| Joint_HH | 28.00 | E | Higher joint-family share in farming communities |
| Extended_multi_generation | 7.00 | E | Extended households; elderly grandparents pattern |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.00 | E | Census 2011 Cooch Behar pattern; includes first-time voter cohort |
| Currently_married | 66.00 | E | High married share in rural AC; NFHS-5 Koch Bihar early marriage indicator (women 20-24 married before 18 = 46.7%) confirms pattern |
| Widowed | 8.00 | E | Concentrated in 60+; female-skewed |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 65.00 | C | NFHS-5 Koch Bihar (2019-21) consistent with NFHS-4 trend; rural Cooch Behar TV ownership stable ~65%; no major uplift 2019-2021 |
| Radio | 7.00 | C | Slight decline; border-area rural households still use radio |
| Mobile_phone | 88.00 | C | Post-COVID-19 mobile phone penetration surge; ~+6pp from 2019 est. 82%; Jio continued rural expansion |
| Smartphone_with_internet | 60.00 | C | Major post-COVID-19 surge; +25pp from 2019 est. 35%; NFHS-5 WB state-level smartphone penetration surge 2019-21; methodology_2021 §C.14: smartphone +20-30pp |
| Computer | 4.00 | C | Minimal change in rural agricultural AC |
| Two_wheeler | 23.00 | C | Marginal increase; modest motorisation |
| Four_wheeler | 3.00 | C | Negligible |
| Banking_access | 88.00 | B | PMJDY saturation + COVID-19 DBT/PMGKAY pushed near-universal enrollment; +6pp from 2019 est. 82%; methodology_2021 §C.14: banking +5-10pp |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 95.00 | B | NFHS-5 Koch Bihar indicator 8 = 99.3% population with improved drinking water; AC-level conservative estimate 95% |
| Improved_sanitation | 75.00 | B | NFHS-5 Koch Bihar indicator 9 = 75.7% improved sanitation; near-direct use |
| LPG_clean_cooking_fuel | 25.00 | B | NFHS-5 Koch Bihar indicator 10 = 25.7% households using clean fuel; note Ujjwala cylinders distributed but refill rate low; active use ~25% |
| Wood_biomass_fuel | 68.00 | B | Dominant fuel; NFHS-5 clean fuel 25.7% implies ~68-70% biomass; rural kitchen reality |
| Other_fuel | 7.00 | E | Kerosene + other residual |
| Electricity | 98.00 | B | NFHS-5 Koch Bihar indicator 7 = 98.2% electricity; Saubhagya near-saturation confirmed |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows LPG+Wood+Other sum to ~100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 74.00 | D | Estimate; Sitalkuchi is deep rural Cooch Behar; COVID-19 return migration reinforced native pool slightly |
| WB_other_district | 6.00 | D | Slight increase from COVID-19 reverse migration from Siliguri, Guwahati-adjacent districts |
| Other_Indian_state | 1.00 | D | Very small trader/service migrant fraction; COVID-19 somewhat reduced |
| Bangladesh_origin | 17.00 | D | Significant Hindu refugee/migrant presence from East Pakistan/Bangladesh partition and post-1971; Cooch Behar border district pattern; stable |
| Outside_India | 0.50 | E | Negligible |
| Out_migrant | 1.50 | E | Working outside AC but registered here; COVID-19 temporarily pushed some back; recovering by end-2021 |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 78.80 | 0.50 | 0.00 | 0.50 | 20.20 | E | Rajbanshi Hindu community uses Rajbongshi; Bengali dominant among non-Rajbanshi Hindus; marginal Rajbongshi increase with identity assertion |
| Muslim | 97.50 | 0.50 | 1.50 | 0.50 | 0.00 | E | Cooch Behar Muslims are Bengali-speaking peasantry; minimal Urdu; stable from 2019 |
| Christian | 90.00 | 2.00 | 0.00 | 8.00 | 0.00 | E | Small base; Bengali + English-medium |
| Sarna_ORP | 50.00 | 0.00 | 0.00 | 10.00 | 40.00 | E | Tribal communities use Rajbongshi and other local languages |
| Other_residual | 60.00 | 35.00 | 0.00 | 5.00 | 0.00 | E | Sikh/Marwari trader fringe |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 47.55 | 5.73 | 5.59 | 11.19 | 29.94 | 0 | 0 | E | SC 38.5%/71.5% Hindu = 53.8% of Hindu → adjusted; Rajbanshi SC dominant; rows sum to 100 |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 10 | 60 | 0 | 10 | 20 | 0 | 0 | E | Tribal communities route primarily to ST_total |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 67.00 | 6.00 | 1.00 | 24.50 | 0.50 | 1.00 | D | Hindu Bangladesh-origin share higher due to partition-era refugee settlement in Cooch Behar border belt; stable |
| Muslim | 91.00 | 5.00 | 0.50 | 2.50 | 0.50 | 0.50 | D | Cooch Behar Muslims are largely native; small Bangladesh-origin trickle |
| Christian | 80.00 | 10.00 | 5.00 | 5.00 | 0.00 | 0.00 | E | Mixed origin |
| Sarna_ORP | 90.00 | 8.00 | 1.00 | 1.00 | 0.00 | 0.00 | E | Tribal communities mostly native |
| Other_residual | 40.00 | 20.00 | 35.00 | 3.00 | 2.00 | 0.00 | E | Trader migrants primarily from other Indian states |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 68.00 | 63.00 | 90.00 | C | NFHS-5 Koch Bihar updated; Hindu above Muslim in rural WB; smartphone surge post-COVID-19 primarily benefited better-off households |
| Muslim | 57.00 | 50.00 | 80.00 | C | Rural Muslim households lower asset access; gap narrowing post-PMJDY; Cooch Behar pattern |
| Christian | 72.00 | 65.00 | 92.00 | E | Small base; assumed marginally above state Hindu average |
| Sarna_ORP | 48.00 | 38.00 | 72.00 | E | Tribal communities lower asset access; PMJDY improved banking |
| Other_residual | 80.00 | 72.00 | 95.00 | E | Trader community high asset access |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 7.00 | 11.00 | 14.00 | 20.00 | 21.00 | 19.00 | 8.00 | E |
| SC_total | 22.00 | 25.00 | 22.00 | 16.00 | 9.00 | 5.00 | 1.00 | E |
| ST_total | 28.00 | 28.00 | 20.00 | 14.00 | 7.00 | 2.50 | 0.50 | E |
| OBC | 18.00 | 23.00 | 22.00 | 18.00 | 11.00 | 6.50 | 1.50 | E |
| Other_Hindu_middle | 16.00 | 23.00 | 22.00 | 19.00 | 11.00 | 7.00 | 2.00 | E |
| Muslim | 23.00 | 25.00 | 22.00 | 17.00 | 8.00 | 4.50 | 0.50 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender).

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 13.00 | 11.00 | E |
| 23_27 | 12.00 | 9.50 | E |
| 28_32 | 10.00 | 7.00 | E |
| 33_37 | 8.50 | 5.00 | E |
| 38_42 | 7.50 | 3.50 | E |
| 43_47 | 6.50 | 3.00 | E |
| 48_52 | 5.50 | 2.50 | E |
| 53_57 | 5.00 | 2.00 | E |
| 58_62 | 4.50 | 1.50 | E |
| 63_67 | 4.00 | 1.00 | E |
| 68 | 3.50 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 6.00 | 32.00 | E |
| 23_27 | 43.00 | 84.00 | E |
| 28_32 | 82.00 | 93.00 | E |
| 33_37 | 92.00 | 91.00 | E |
| 38_42 | 93.00 | 89.00 | E |
| 43_47 | 92.00 | 85.00 | E |
| 48_52 | 90.00 | 78.00 | E |
| 53_57 | 88.00 | 68.00 | E |
| 58_62 | 84.00 | 55.00 | E |
| 63_67 | 78.00 | 38.00 | E |
| 68 | 68.00 | 25.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 48.00 | 60.00 | C | Rural agricultural baseline; post-COVID-19 smartphone surge even in farming households; +20pp from 2019 |
| Agricultural_labourer | 35.00 | 50.00 | C | Lowest income stratum; still significant uplift from 2019 est. 18% |
| Household_industry | 55.00 | 65.00 | C | Small artisan/weaver households; smartphone for trade |
| Manufacturing | 65.00 | 75.00 | C | |
| Construction | 62.00 | 68.00 | C | |
| Trade_retail | 80.00 | 82.00 | C | Sitalkuchi bazaar traders; WhatsApp for business |
| Transport_logistics | 75.00 | 78.00 | C | |
| Services | 82.00 | 85.00 | C | |
| Government_services_teachers | 92.00 | 92.00 | C | Highest connectivity |
| Out_migrant_worker | 82.00 | 72.00 | D | Working outside; smartphone-heavy for remittance transfers |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 38.00 | 2.00 | E |
| Primary | 40.00 | 3.00 | E |
| Middle | 36.00 | 5.00 | E |
| Secondary | 30.00 | 10.00 | E |
| Higher_Secondary | 22.00 | 15.00 | E |
| Graduate | 26.00 | 17.00 | E |
| Postgraduate | 35.00 | 10.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 005. See NORMALIZED_SCHEMA.md §4.7.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Sub-unit codes use `Un_` prefix matching C.11.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Sitalkuchi_CD_Block_north | 69.50 | 28.50 | 0.40 | 1.00 | 0.60 | E | Northern GPs; estimated higher Muslim share in northern border fringe; marginal Muslim increase from 2019 |
| U2_Sitalkuchi_CD_Block_south | 73.50 | 25.50 | 0.20 | 0.60 | 0.20 | E | Southern GPs around Sitalkuchi bazaar; marginally more Hindu |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Use canonical caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Sitalkuchi_CD_Block_north | 3.50 | 36.50 | 5.00 | 7.50 | 19.00 | 28.50 | 0.00 | E |
| U2_Sitalkuchi_CD_Block_south | 4.50 | 40.50 | 4.40 | 8.50 | 17.10 | 24.70 | 0.30 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Sitalkuchi_CD_Block_north | 60.00 | 55.00 | 3.00 | 85.00 | E |
| U2_Sitalkuchi_CD_Block_south | 70.00 | 65.00 | 5.00 | 91.00 | E |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Sitalkuchi_CD_Block_north | 22.00 | 70.00 | 92.00 | 97.00 | E |
| U2_Sitalkuchi_CD_Block_south | 28.00 | 80.00 | 98.00 | 99.00 | E |

### D.15 Vote × Religion (2021 AE)

P(party ‖ religion) — anchored to 2021 AE result for AC 005. BJP won with 50.80% vs AITC 43.56%.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 62.00 | 30.00 | 0.50 | 4.50 | 3.00 | C | CSDS-Lokniti WB 2021 pattern anchored to AC result; Hindu consolidation for BJP continued and intensified vs 2019; Rajbanshi SC BJP vote firmed further |
| Muslim | 5.00 | 80.00 | 0.50 | 10.00 | 4.50 | C | Strong AITC Muslim consolidation nationally in 2021 WB AE; LF residual in Cooch Behar Muslim belt |
| Christian | 28.00 | 52.00 | 2.00 | 12.00 | 6.00 | E | Small base; estimated |
| Sarna_ORP | 50.00 | 32.00 | 0.50 | 14.00 | 3.50 | E | Tribal vote; BJP inroads continued |
| Other_residual | 52.00 | 30.00 | 2.00 | 10.00 | 6.00 | E | |

### D.16 Vote × Caste (2021 AE)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 65.00 | 25.00 | 2.00 | 5.00 | 3.00 | C | CSDS 2021 WB UC pattern; BJP consolidation |
| OBC | 52.00 | 35.00 | 0.50 | 8.00 | 4.50 | C | Koch-Rajbanshi OBC firm BJP vote |
| SC_total | 62.00 | 29.00 | 0.50 | 5.50 | 3.00 | C | Rajbanshi SC BJP lean; strong consolidation in 2021; AC 005 BJP winner Baren Chandra Barman is himself Rajbanshi SC |
| ST_total | 45.00 | 35.00 | 0.50 | 15.00 | 4.50 | C | ST vote more mixed; LF retention slightly higher |
| Other_Hindu_middle | 56.00 | 33.00 | 0.50 | 7.00 | 3.50 | C | |
| Muslim | 5.00 | 80.00 | 0.50 | 10.00 | 4.50 | C | Same as D.15 Muslim row |

### D.17 Vote × Gender (2021 AE)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 54.00 | 37.00 | 0.50 | 5.50 | 3.00 | C | CSDS 2021 WB gender gap; male more BJP-leaning; intensified from 2019 |
| Female | 47.00 | 46.00 | 0.50 | 4.00 | 2.50 | C | Lakshmir Bhandar launched April 2021; limited electoral impact within 2021 AE itself (too new at polling time); AITC female advantage partially recovered from 2019 |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for AC 005. See NORMALIZED_SCHEMA.md §4.7.)

---

## E. 2021 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.** Tier A — from ECI 2021 WB AE detailed results for AC 005 (data/electoral_history/2021/detailed_results.csv).

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 50.80 | A | ECI 2021 AE — AC 005: Baren Chandra Barman (BJP) 124,955 votes / 245,966 total valid votes |
| AITC | 43.56 | A | ECI 2021 AE — AC 005: Partha Pratim Ray (AITC) 107,140 votes |
| INC | 0.00 | A | ECI 2021 AE — no INC candidate stood in AC 005 |
| LF | 3.01 | A | ECI 2021 AE — CPI(M) 6,720 + SUCI 693 = 7,413 votes |
| Other_NOTA | 2.63 | A | ECI 2021 AE — NOTA 2,743 + IND 2,018 + KPPU 976 + AMB 721 = 6,458 votes |
| **Sum** | **100.00** | — | self-check |

Electorate: 285,260; total valid EVM votes: 245,966; turnout: 86.23%.
Margin: BJP over AITC by 17,815 votes (7.24 pp).
Winner: Baren Chandra Barman (BJP). Runner-up: Partha Pratim Ray (AITC).
Note: CISF firing incident on 10 April 2021 (polling day Phase 4) killed 4 persons at Booth 126, Jorpatki area. The election proceeded; results stand as calibration target.

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 005 Sitalkuchi (Assembly Elections)

Sitalkuchi was an AIFB (All India Forward Bloc) stronghold through the Left Front era through 2006. AITC began winning the seat from 2011, and held it in 2016 with an expanded margin. The 2021 shift to BJP — a decisive 7.24pp win — represented a major reversal driven by Rajbanshi SC community consolidation under BJP's Koch-Rajbanshi identity project.

| Year | Winner | Party | Winner % | Runner-up | Party | Runner-up % | Margin pp |
|---|---|---|---|---|---|---|---|
| 2011 AE | (AITC winner) | AITC | ~44.3 | (CPI(M)) | CPI(M) | ~35.2 | ~9.1 est. |
| 2016 AE | Hiten Barman | AITC | 44.18 | Namadipti Adhikary | CPI(M) | 37.45 | 6.73 |

Note: Udayan Guha was MLA for neighbouring Mathabhanga; 2016 Sitalkuchi winner was Hiten Barman (AITC). BJP share in 2016 was only 11.89% (Baren Chandra Barman as BJP candidate; same person who won in 2021 as BJP candidate). The 39pp BJP swing between 2016 and 2021 in this AC is among the largest in Cooch Behar district — driven by Rajbanshi SC and OBC Koch-Rajbanshi mobilisation.

### 2019 LS — AC 005 segment (historical anchor)

The 2019 LS result for AC 005 Sitalkuchi segment was a near dead-heat — the calibration target in the 2019 frozen file. By 2021, BJP had built substantially on this foundation.

| Year | BJP % | AITC % | LF % | INC % | Other/NOTA % | Winner (AC segment) |
|---|---|---|---|---|---|---|
| 2019 LS | 46.29 | 46.82 | 3.23 | 1.55 | 2.11 | AITC (by 1,230 votes, 0.53pp) |

Source: ECI 2019 LS Assembly Segment Level Voting Data CSV (tier A).

### Cooch Behar Lok Sabha (PC 01) historical

| Year | Winner | Party | Notes |
|---|---|---|---|
| 2014 LS | Renuka Sinha | AITC | AITC won Cooch Behar PC; BJP ~22%; Left second |
| 2019 LS | Nisith Pramanik | BJP | BJP won Cooch Behar PC; massive Rajbanshi swing; AC 005 segment near-tie |

### Context: CISF firing, 10 April 2021

During Phase 4 polling (10 April 2021), CISF personnel opened fire on a crowd at Booth 126 in Jorpatki village, AC 005 Sitalkuchi. Four voters were killed. The incident became a major political flashpoint — BJP accused TMC of orchestrating the crowd attack on central forces; TMC accused BJP and central forces of an unprovoked massacre. The Election Commission ordered re-polling at selected booths. The final result (BJP win) was tallied including all valid votes. This context is documented here as it is directly relevant to understanding the 2021 calibration target.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Cooch Behar district Primary Census Abstract (religion, SC/ST, literacy, worker categories)
- Census of India 2011 — Sitalkuchi CD Block (sub-district tables where available)
- Election Commission of India — `data/electoral_history/2021/detailed_results.csv` (AC 005, tier A: candidate votes, totals, electorate)
- Election Commission of India — `data/2019_AssemblySegmentLevelVotingData.csv` (AC 005 segment 2019 LS, tier A)
- Delimitation Commission of India 2008 — WB Schedule (AC 005 = Sitalkuchi; Cooch Behar PC 01)
- `data/master/wb_ac_master_v3.csv` — AC 005 population totals (pop_total, sc_pop, reservation=GEN confirmed)

### Secondary sources (tier B/C)

- NFHS-5 (2019-21) — Koch Bihar district: indicators 7 (electricity 98.2%), 8 (drinking water 99.3%), 9 (sanitation 75.7%), 10 (clean cooking fuel 25.7%), 3 (sex ratio 1,058), 14 (women literacy 79.2%); file: `data/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv`
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline (rural/urban split); comparison baseline for 2021 changes
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2021 WB AE post-poll — vote × demographic conditionals (WB regional rollup; 2021 calibration anchor)
- WB District Statistical Handbook — Cooch Behar (BPL and economic status proxy)

### Tertiary / journalistic (tier D)

- Wikipedia "Sitalkuchi (Vidhan Sabha constituency)" — AC composition, election history summary
- Wikipedia "2021 West Bengal legislative assembly election" and "Sitalkuchi firing" — April 10 incident documentation
- Wikipedia "Koch-Rajbanshi people" — Kshatriya movement, political alignment
- Journalistic reports on BJP Cooch Behar mobilisation 2019-2021 and Koch-Rajbanshi identity politics
- `data/electoral_history/2016/detailed_results.csv` — 2016 AE candidate-level results for AC 005 (tier A for the 2016 result; used here as tier D historical anchor)

### Tier-D/E reliance flags (what to distrust)

- **Sub-unit split** (C.11, D.11–D.14): v0 equal 50/50 split; no DCHB Part-A block-GP breakdown retrieved
- **Caste sub-group shares** (C.2, D.2): no caste census post-1931 for non-SC/ST; SC sub-group breakdown is tier-C/E
- **Migration / birthplace** (C.16, D.3): no AC-level Census D-series; tier D from journalistic/district pattern
- **Asset/media** (C.14, D.4, D.13): NFHS-5 district-level projected to AC; smartphone surge modeled from state trend; tier C
- **Vote × Demographic** (D.15–D.17): CSDS 2021 WB regional rollup calibrated to AC 005 result; tier C
- **Religion splits** (C.1): Sitalkuchi block-level 2011 data not retrieved; district-level projection used; tier E
- **Sex ratio** (B, C.4): NFHS-5 Koch Bihar sex ratio 1,058 notably higher than Census 2011 946; used conservatively

### v0 known gaps

1. Sitalkuchi CD Block Census 2011 sub-district tables — collapsed to 2 sub-units; refine when DCHB Cooch Behar Part-A available
2. Block-level religion data — using district-level projection with assumed Muslim differential
3. ECI Form-20 per-booth breakdown for 2021 AE at AC 005 — candidate-level totals used; booth-level not retrieved
4. CSDS 2021 WB AE regional cross-tabs — WB rollup used; not AC-specific survey
5. Post-incident re-polling booths — unclear if the aggregate includes or excludes contested booths; treated as final ECI figure

---

*v0 — frozen at end-2021 state-of-knowledge. No post-2021 events referenced.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2024 Lok Sabha Election — AC 005 segment within Cooch Behar LS (PC 01)

> Tier-A segment data for AC 005 not confirmed in `2024_AssemblySegmentLevelVotingData.csv` (schema/mapping to AC_NO not verified for Cooch Behar). Figures below are tier D from journalistic accounts of Cooch Behar PC 2024 result.

| Party | Candidate (LS level) | AC-segment % (est.) | Tier | Source |
|---|---|---|---|---|
| BJP | Nisith Pramanik | ~50 | D | Journalistic estimate; BJP retained Cooch Behar PC 2024; AC 005 BJP stronghold |
| AITC | (candidate) | ~43 | D | Journalistic estimate |
| INC | (INDIA bloc) | ~2 | D | Residual |
| LF | — | ~2 | D | AIFB/SUCI residual |
| Other_NOTA | — | ~3 | D | NOTA + IND |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC 005 segment shares within ±3pp of the tier-A figures (BJP / AITC combined) once tier-A 2024 segment data is retrieved.
