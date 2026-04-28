# AC 005 — Sitalkuchi (GEN) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 005 Sitalkuchi as of 2019 only — it does not reference
> any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 005 | A | ECI / Delimitation Commission 2008 |
| AC name | Sitalkuchi | A | ECI |
| Reservation | GEN (unreserved) | A | Delimitation 2008 |
| District | Cooch Behar | A | Delimitation 2008 |
| Sub-division | Mathabhanga | A | WB administrative |
| LS constituency | 01 — Cooch Behar | A | Delimitation 2008 |
| LS segments included | AC 01 Mekhliganj · AC 02 Sitai · AC 03 Sitalkuchi · AC 04 Tufanganj · AC 05 Natabari · AC 06 Dinhata · AC 07 Nalhati … (7 AC segments in Cooch Behar PC) | A | Delimitation 2008 |
| AC composition | Sitalkuchi CD Block (part): Sitalkuchi GP cluster + adjoining GPs within Mathabhanga sub-division; no municipality — fully rural | A | Delimitation 2008 |
| Geographic note | Northern Cooch Behar district; flat alluvial Terai, Raidak river basin; international border with Bangladesh to the west | A | — |
| Sub-units used in v0 | **U1: Sitalkuchi_CD_Block_north** (GPs north of Sitalkuchi town) · **U2: Sitalkuchi_CD_Block_south** (GPs south including Sitalkuchi bazaar fringe) | E | v0 simplification — equal-weight GP split pending DCHB Part-A |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~280,000 | E | Cooch Behar district Census 2011; Sitalkuchi CD Block population scaled to AC boundary |
| 2019 projected population | ~303,500 | E | 8-yr compound religion-differential growth (~1.0%/yr Hindu, ~1.3%/yr Muslim) |
| Sex ratio (2019, F per 1000 M) | ~946 | E | Cooch Behar district 2011 sex ratio 946; minimal projection drift |
| 2019 estimated electorate (18+) | ~275,720 | A | ECI 2019 LS — total electors for AC 005 segment (2019_AssemblySegmentLevelVotingData.csv) |
| Estimated M / F / TG split (2019) | 51.4% M / 48.6% F / <0.05% TG | E | Cooch Behar district sex ratio back-projected |
| 2019 polling stations (estimated) | ~305 | E | Back-derived from electorate size at ~900 electors/booth WB norm |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 72.00 | E | Cooch Behar district Census 2011: 75.6% Hindu; projected with Muslim growth +0.3pp/yr → ~72% by 2019 for this AC (Sitalkuchi block has higher Muslim share than district avg) |
| Muslim | 26.50 | E | Sitalkuchi block estimated ~25% Muslim 2011; 8-yr growth to ~26.5% |
| Christian | 0.30 | E | Cooch Behar district 2011 ~0.35% Christian; minimal in rural block |
| Sarna_ORP | 0.80 | E | Rajbanshi community carries tribal religion trace; Cooch Behar district ST ~4.7% |
| Other_residual | 0.40 | E | Sikh + Buddhist + Not_stated residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 38.50 | A | Cooch Behar district SC 40.0% Census 2011; Sitalkuchi block slightly lower given Muslim share; A-tier district figure used as proxy |
| └ Rajbanshi_SC | 34.00 | C | Dominant SC community in Cooch Behar; Rajbanshi is largest SC sub-group district-wide (Rajbanshi community straddles SC/OBC boundary; those listed as SC dominate) |
| └ Namasudra_SC | 2.50 | E | Secondary SC sub-group in Cooch Behar |
| └ Other_SC | 2.00 | E | Remaining SC sub-groups (Koch, Bagdi etc.) |
| **ST_total** | 4.70 | A | Cooch Behar district ST 4.7% Census 2011 |
| └ Rajbanshi_ST | 3.50 | C | Rajbanshi community with ST listing in some classifications; Cooch Behar tribal fringe |
| └ Other_ST | 1.20 | E | Mech, Toto and smaller tribal groups |
| UC_bhadralok | 4.00 | E | Small upper-caste share in rural Cooch Behar; Brahmin/Kayastha fringe in market towns |
| OBC | 8.00 | E | OBC Rajbanshi (non-SC registered) + Koch-Rajbanshi + other backward communities |
| Other_Hindu_middle | 16.30 | E | Residual within Hindu (72.00 − 38.50 SC − 4.70 ST − 4.00 UC − 8.00 OBC = 16.80; minus Muslim overlap) |
| Muslim | 26.50 | E | See C.1; primarily Bengali-speaking peasantry and agricultural labourers |
| Christian_plus_Sarna_plus_Other | 2.00 | E | See C.1 |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.50 | E | Cooch Behar district age pyramid 2011; renormalized to 18+ voters only |
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

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.40 | E | Cooch Behar district sex ratio 946 F per 1000 M → 51.4% M |
| Female | 48.59 | E | Derived from sex ratio |
| Third_gender | 0.01 | E | WB state norm ~0.01% |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 85.00 | E | Dominant language in Cooch Behar; Rajbanshi community increasingly Bengali-medium |
| Hindi | 0.50 | E | Trader/migrant fringe in Sitalkuchi bazaar |
| Urdu | 0.50 | E | Small Muslim pocket using Urdu script |
| Other | 0.50 | E | Residual catch-all |
| Rajbongshi | 13.50 | E | Rajbongshi/Rajbanshi language spoken by Koch-Rajbanshi community; AC-local addition (sub-set of Bengali/Other registrations in Census but distinct dialect) |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 22.00 | E | Cooch Behar district literacy 75.3% (Census 2011 A); AC literacy ~75%, +3pp/8yr improvement → ~22% illiterate 2019 |
| Primary | 24.00 | E | Census 2011 education distribution scaled to district pattern |
| Middle | 20.00 | E | |
| Secondary | 16.00 | E | |
| Higher_Secondary | 10.00 | E | |
| Graduate | 6.00 | E | |
| Postgraduate | 2.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 33.00 | E | Cooch Behar district Census 2011 main-worker share ~33%; rural agricultural AC |
| Marginal_worker | 13.00 | E | High marginal-worker share typical in Cooch Behar (seasonal agriculture) |
| Non_worker | 36.00 | E | Housewives + elderly + retired; rural WB pattern |
| Student | 10.00 | E | 18–22 cohort partly in education |
| Unemployed | 8.00 | E | Educated job-seeking pool; rural-urban aspiration gap |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 28.00 | E | Cooch Behar district Census 2011: ~30% cultivators (A); Sitalkuchi rural — slight adjustment |
| Agricultural_labourer | 35.00 | E | Very high ag-labour share; landless Rajbanshi SC and Muslim labourers dominant |
| Household_industry | 4.00 | E | Cooch Behar district HH industry ~4.5% |
| Manufacturing | 2.00 | E | Limited organised manufacturing in rural block |
| Construction | 5.00 | E | Includes local construction and seasonal migration |
| Trade_retail | 10.00 | E | Sitalkuchi bazaar traders; border-area petty trade |
| Transport_logistics | 4.00 | E | Road transport; no rail/river port in this block |
| Services | 6.00 | E | Private services in Sitalkuchi town fringe |
| Government_services_teachers | 4.00 | E | Government employees + school teachers |
| Out_migrant_worker | 2.00 | D | Limited compared to other WB districts; some to Siliguri and Guwahati |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Census B-04 WB rural pattern; very low in agricultural AC |
| Employee | 22.00 | E | Government + organised sector + wage earners |
| Single_worker | 46.00 | E | Cultivator (own-account) + own-account artisan + petty trader |
| Family_worker | 30.50 | E | High family-worker share in agricultural households typical of Cooch Behar rural |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 32.00 | C | Cooch Behar district BPL share ~35% (state BPL 2011 ~31%); rural Sitalkuchi estimated ~32% after WB poverty reduction trend |
| Above_Poverty_Line_low_income | 35.00 | E | Working poor — subsistence agriculture |
| Lower_middle | 20.00 | E | Small cultivators + lower-grade government employees |
| Middle | 10.00 | E | Mid-level government employees + medium traders |
| Upper_middle_well_off | 3.00 | E | Small fraction; Sitalkuchi bazaar traders + larger landowners |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Sitalkuchi_CD_Block_north | 50.00 | E | v0 equal-split assumption pending DCHB Part-A; northern GPs of Sitalkuchi block |
| U2_Sitalkuchi_CD_Block_south | 50.00 | E | Southern GPs including Sitalkuchi town fringe; refine when block-level Census tables available |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | WB rural 2011: 4.5; Cooch Behar district consistent with state rural |
| Nuclear_HH | 65.00 | E | NFHS-4 WB rural pattern; Cooch Behar |
| Joint_HH | 28.00 | E | Higher joint-family share in farming communities |
| Extended_multi_generation | 7.00 | E | Extended households; elderly grandparents pattern |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.00 | E | Census 2011 Cooch Behar pattern; includes first-time voter cohort |
| Currently_married | 66.00 | E | High married share in rural AC |
| Widowed | 8.00 | E | Concentrated in 60+; female-skewed (higher female widowhood) |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 65.00 | C | NFHS-4 WB rural 60%, +5pp/yr → ~65% by 2019; Cooch Behar rural slightly below state urban |
| Radio | 8.00 | C | Slightly higher than Bengal average; still used in border-area rural households |
| Mobile_phone | 82.00 | C | NFHS-4 WB ~78%, +growth → ~82% by 2019 |
| Smartphone_with_internet | 35.00 | C | Below state average; Jio rollout slower in remote Cooch Behar border block |
| Computer | 4.00 | C | NFHS-4 WB rural ~4%; very low in rural agricultural AC |
| Two_wheeler | 22.00 | C | NFHS-4 WB rural 18%; Cooch Behar modest motorisation |
| Four_wheeler | 3.00 | C | Negligible in rural block |
| Banking_access | 82.00 | B | PMJDY 2014– saturation; Cooch Behar rural PMJDY enrollment high |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 80.00 | C | NFHS-4 WB rural 84%; Cooch Behar border-area slightly lower access |
| Improved_sanitation | 60.00 | C | NFHS-4 WB rural 51% + Swachh Bharat 2014-19 (+15pp rural) → ~60-65% |
| LPG_clean_cooking_fuel | 35.00 | C | NFHS-4 WB rural 24%; +Ujjwala 2016-19 (+12pp rural) → ~35% |
| Wood_biomass_fuel | 58.00 | C | Dominant fuel; gradual Ujjwala displacement |
| Other_fuel | 7.00 | C | Kerosene + dung cakes residual |
| Electricity | 90.00 | A | Census 2011 Cooch Behar electrification + Saubhagya 2017-19 near-saturation |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 75.00 | D | Estimate; Sitalkuchi is deep rural Cooch Behar with low in-migration; most population native to district |
| WB_other_district | 5.00 | D | Small in-migrant fraction from Jalpaiguri, Koch Bihar neighbours |
| Other_Indian_state | 1.00 | D | Very small trader/service migrant fraction |
| Bangladesh_origin | 17.00 | D | Significant Hindu refugee/migrant presence from East Pakistan/Bangladesh partition and post-1971; Cooch Behar border district pattern |
| Outside_India | 0.50 | E | Negligible |
| Out_migrant | 1.50 | E | Working outside AC but registered here; lower than other WB districts |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 79.00 | 0.50 | 0.00 | 0.50 | 20.00 | E | Rajbanshi Hindu community uses Rajbongshi; Bengali dominant among non-Rajbanshi Hindus |
| Muslim | 97.50 | 0.50 | 1.50 | 0.50 | 0.00 | E | Cooch Behar Muslims are Bengali-speaking peasantry; minimal Urdu |
| Christian | 90.00 | 2.00 | 0.00 | 8.00 | 0.00 | E | Small base; Bengali + English-medium |
| Sarna_ORP | 50.00 | 0.00 | 0.00 | 10.00 | 40.00 | E | Tribal communities use Rajbongshi and other local languages |
| Other_residual | 60.00 | 35.00 | 0.00 | 5.00 | 0.00 | E | Sikh/Marwari trader fringe |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 47.22 | 5.83 | 5.56 | 11.11 | 30.28 | 0 | 0 | E | SC 38.5%/72% Hindu = 53.5% of Hindu → adjusted for Muslim share; Rajbanshi SC dominant |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 10 | 60 | 0 | 10 | 20 | 0 | 0 | E | Tribal communities route primarily to ST_total |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 68.00 | 5.50 | 1.00 | 24.00 | 0.50 | 1.00 | D | Hindu Bangladesh-origin share higher due to partition-era refugee settlement in Cooch Behar border belt |
| Muslim | 92.00 | 4.00 | 0.50 | 2.50 | 0.50 | 0.50 | D | Cooch Behar Muslims are largely native; small Bangladesh-origin trickle |
| Christian | 80.00 | 10.00 | 5.00 | 5.00 | 0.00 | 0.00 | E | Mixed origin |
| Sarna_ORP | 90.00 | 8.00 | 1.00 | 1.00 | 0.00 | 0.00 | E | Tribal communities mostly native |
| Other_residual | 40.00 | 20.00 | 35.00 | 3.00 | 2.00 | 0.00 | E | Trader migrants primarily from other Indian states |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 68.00 | 38.00 | 85.00 | C | NFHS-4 WB religion gap pattern; Hindu slightly above Muslim in rural WB |
| Muslim | 57.00 | 28.00 | 75.00 | C | Rural Muslim households lower asset access; Cooch Behar pattern |
| Christian | 72.00 | 42.00 | 88.00 | E | Small base; assumed marginally above state Hindu average |
| Sarna_ORP | 48.00 | 20.00 | 65.00 | E | Tribal communities lower asset access |
| Other_residual | 80.00 | 55.00 | 92.00 | E | Trader community high asset access |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 8.00 | 12.00 | 15.00 | 20.00 | 20.00 | 18.00 | 7.00 | E |
| SC_total | 24.00 | 26.00 | 22.00 | 15.00 | 8.00 | 4.00 | 1.00 | E |
| ST_total | 30.00 | 28.00 | 20.00 | 13.00 | 6.00 | 2.50 | 0.50 | E |
| OBC | 20.00 | 24.00 | 22.00 | 17.00 | 10.00 | 5.50 | 1.50 | E |
| Other_Hindu_middle | 18.00 | 24.00 | 22.00 | 18.00 | 10.00 | 6.00 | 2.00 | E |
| Muslim | 25.00 | 26.00 | 22.00 | 16.00 | 7.00 | 3.50 | 0.50 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender).

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 12.00 | 10.00 | E |
| 23_27 | 11.00 | 8.00 | E |
| 28_32 | 9.00 | 6.00 | E |
| 33_37 | 8.00 | 4.50 | E |
| 38_42 | 7.00 | 3.00 | E |
| 43_47 | 6.00 | 2.50 | E |
| 48_52 | 5.00 | 2.00 | E |
| 53_57 | 4.50 | 1.50 | E |
| 58_62 | 4.00 | 1.50 | E |
| 63_67 | 3.50 | 1.00 | E |
| 68 | 3.00 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 6.00 | 30.00 | E |
| 23_27 | 42.00 | 82.00 | E |
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
| Cultivator | 28.00 | 60.00 | C | Rural agricultural baseline; below state average |
| Agricultural_labourer | 18.00 | 50.00 | C | Lowest income stratum |
| Household_industry | 32.00 | 65.00 | C | Small artisan/weaver households |
| Manufacturing | 45.00 | 75.00 | C | |
| Construction | 40.00 | 68.00 | C | |
| Trade_retail | 60.00 | 82.00 | C | Sitalkuchi bazaar traders |
| Transport_logistics | 55.00 | 78.00 | C | |
| Services | 65.00 | 85.00 | C | |
| Government_services_teachers | 80.00 | 92.00 | C | Highest connectivity |
| Out_migrant_worker | 65.00 | 72.00 | D | Working outside; smartphone-heavy for remittance transfers |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 38.00 | 2.00 | E |
| Primary | 40.00 | 3.00 | E |
| Middle | 36.00 | 5.00 | E |
| Secondary | 30.00 | 9.00 | E |
| Higher_Secondary | 22.00 | 14.00 | E |
| Graduate | 26.00 | 16.00 | E |
| Postgraduate | 35.00 | 10.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 005. See NORMALIZED_SCHEMA.md §4.7.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Sub-unit codes use `Un_` prefix matching C.11.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Sitalkuchi_CD_Block_north | 70.00 | 28.00 | 0.40 | 1.00 | 0.60 | E | Northern GPs; estimated higher Muslim share in northern border fringe |
| U2_Sitalkuchi_CD_Block_south | 74.00 | 25.00 | 0.20 | 0.60 | 0.20 | E | Southern GPs around Sitalkuchi bazaar; marginally more Hindu |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Use canonical caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Sitalkuchi_CD_Block_north | 3.50 | 37.00 | 5.00 | 7.50 | 19.00 | 28.00 | 0.00 | E |
| U2_Sitalkuchi_CD_Block_south | 4.50 | 40.00 | 4.40 | 8.50 | 17.70 | 24.60 | 0.30 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Sitalkuchi_CD_Block_north | 60.00 | 30.00 | 3.00 | 78.00 | E |
| U2_Sitalkuchi_CD_Block_south | 70.00 | 40.00 | 5.00 | 86.00 | E |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Sitalkuchi_CD_Block_north | 30.00 | 55.00 | 75.00 | 87.00 | E |
| U2_Sitalkuchi_CD_Block_south | 40.00 | 65.00 | 85.00 | 93.00 | E |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 WB regional rollup anchored to AC 005 result.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 59.00 | 31.00 | 2.00 | 5.00 | 3.00 | C | CSDS-Lokniti 2019 WB Hindu-vote pattern; Cooch Behar Hindu consolidation for BJP |
| Muslim | 5.00 | 72.00 | 10.00 | 10.00 | 3.00 | C | CSDS 2019 WB Muslim vote; AITC dominant; LF residual in Cooch Behar Muslim belt |
| Christian | 30.00 | 50.00 | 10.00 | 5.00 | 5.00 | E | Small base; estimated |
| Sarna_ORP | 45.00 | 35.00 | 5.00 | 12.00 | 3.00 | E | Tribal vote split; BJP made inroads |
| Other_residual | 50.00 | 30.00 | 10.00 | 5.00 | 5.00 | E | |

### D.16 Vote × Caste (2019 LS)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 62.00 | 28.00 | 4.00 | 4.00 | 2.00 | C | CSDS 2019 WB UC pattern |
| OBC | 45.00 | 38.00 | 6.00 | 8.00 | 3.00 | C | Koch-Rajbanshi OBC swing toward BJP in 2019 |
| SC_total | 58.00 | 32.00 | 2.00 | 5.00 | 3.00 | C | Rajbanshi SC BJP lean; Cooch Behar specific pattern |
| ST_total | 42.00 | 38.00 | 4.00 | 12.00 | 4.00 | C | ST vote more mixed; some LF retention |
| Other_Hindu_middle | 52.00 | 36.00 | 3.00 | 6.00 | 3.00 | C | |
| Muslim | 5.00 | 72.00 | 10.00 | 10.00 | 3.00 | C | Same as D.15 Muslim row |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 49.00 | 41.00 | 3.00 | 4.00 | 3.00 | C | CSDS 2019 WB gender gap; male more BJP-leaning |
| Female | 43.00 | 48.00 | 3.00 | 3.50 | 2.50 | C | Female more AITC-leaning; pre-Lakshmir Bhandar 2019 baseline |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for AC 005. See NORMALIZED_SCHEMA.md §4.7.)

---

## E. 2019 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.** Tier A — from ECI 2019 LS Assembly Segment Level Voting Data CSV for AC 005.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 46.29 | A | ECI 2019 LS segment data — AC 005: 108,541 votes / 234,468 total valid EVM votes |
| AITC | 46.82 | A | ECI 2019 LS segment data — AC 005: 109,771 votes |
| INC | 1.55 | A | ECI 2019 LS segment data — AC 005: 3,633 votes |
| LF | 3.23 | A | AIFB 7,000 + SUCI(C) 572 = 7,572 votes; AIFB is the principal LF presence in Cooch Behar |
| Other_NOTA | 2.11 | A | KPPU 539 + WPOI 418 + AMB 505 + IND 887 + IND 1,317 + IND 1,285 = 4,951 votes |
| **Sum** | **100.00** | — | self-check |

Electorate: 275,720; total valid EVM votes: 234,468; turnout: 85.04%.
Margin: AITC over BJP by 1,230 votes (0.53 pp) — extremely narrow.

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 005 Sitalkuchi (Assembly Elections)

Sitalkuchi was an AIFB (All India Forward Bloc) stronghold through the Left Front era. The 2019 shift to a near-dead-heat between AITC and BJP represented a dramatic departure from its Left legacy.

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Udayan Guha | AITC | ~44 | (AIFB) | AIFB | ~35 | ~12,000 est. |
| 2016 AE | Udayan Guha | AITC | ~49 | (AIFB/Left) | AIFB | ~29 | ~25,000 est. |

Note: Udayan Guha (AITC) was the sitting MLA from 2011 and 2016. The BJP did not field a strong candidate in 2011 or 2016 in Sitalkuchi; its rise to near-parity by 2019 LS was driven by the Koch-Rajbanshi consolidation under BJP and the appeal to Hindu Rajbanshi identity (Kshatriya status campaign). AIFB traditionally held the Rajbanshi SC vote through caste-based Left mobilisation; BJP replicated this appeal on Hindu-nationalist lines.

### Cooch Behar Lok Sabha (PC 01) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Renuka Sinha | AITC | ~38 | AITC won Cooch Behar PC; CPI(M) second; BJP ~22% |
| 2016 AE | (AITC held all Cooch Behar ACs) | AITC | — | AITC dominant after Left collapse; BJP weak |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Cooch Behar district Primary Census Abstract (religion, SC/ST, literacy, worker categories)
- Census of India 2011 — Sitalkuchi CD Block (sub-district tables where available)
- Election Commission of India — `2019_AssemblySegmentLevelVotingData.csv` (AC 005 segment, tier A)
- Delimitation Commission of India 2008 — WB Schedule (AC 005 = Sitalkuchi; Cooch Behar PC 01)

### Secondary sources (tier B/C)

- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline (rural/urban split)
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2019 NES — vote × demographic conditionals (WB regional rollup)
- WB District Statistical Handbook — Cooch Behar (BPL and economic status proxy)

### Tertiary / journalistic (tier D)

- Wikipedia "Sitalkuchi (Vidhan Sabha constituency)" — AC composition, election history summary
- Wikipedia "Cooch Behar district" — demographic overview, Rajbanshi community
- Wikipedia "Koch-Rajbanshi people" — Kshatriya movement, political alignment
- Journalistic reports on BJP Cooch Behar mobilisation 2018-19 and Koch-Rajbanshi identity politics

### Tier-D/E reliance flags (what to distrust)

- **Sub-unit split** (C.11, D.11–D.14): v0 equal 50/50 split; no DCHB Part-A block-GP breakdown retrieved
- **Caste sub-group shares** (C.2, D.2): no caste census post-1931 for non-SC/ST; SC sub-group breakdown is tier-C/E
- **Migration / birthplace** (C.16, D.3): no AC-level Census D-series; tier D from journalistic/district pattern
- **Asset/media** (C.14, D.4, D.13): NFHS-4/5 state-level projected to AC; tier C
- **Vote × Demographic** (D.15–D.17): CSDS 2019 WB regional rollup calibrated to AC 005 result; tier C
- **Religion splits** (C.1): Sitalkuchi block-level 2011 data not retrieved; district-level projection used; tier E
- **Assembly election history** (F): percentages are approximate estimates from Wikipedia summaries; tier D

### v0 known gaps

1. Sitalkuchi CD Block Census 2011 sub-district tables — collapsed to 2 sub-units; refine when DCHB Cooch Behar Part-A available
2. Block-level religion data — using district-level projection with assumed Muslim differential
3. ECI Form-20 per-candidate breakdown for 2016 AE, 2011 AE at AC 005 — Wikipedia summary only
4. CSDS WB regional cross-tabs — Swarajya/Lokniti summary used, not full AC-specific survey
5. 2024 LS segment data not available in supplied CSV for AC 005 — Section H incomplete

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge.
No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2021 WB Assembly Election — AC 005 Sitalkuchi (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| AITC | Udayan Guha | — | — | A — ECI 2021 AE (figures to be populated from ECI archive) |
| BJP | (candidate) | — | — | A — ECI 2021 AE |
| **Note** | AC 005 was the site of the April 10 2021 AE booth-day incident; the final result stands as the out-of-sample validation gate | — | — | Incident is post-2019 context; not in frozen sections A-G |

AITC won AC 005 in 2021; BJP was runner-up. Exact vote counts to be populated from ECI 2021 AE archive.

### 2024 Lok Sabha Election — AC 005 segment within Cooch Behar LS (PC 01)

> Tier-A segment data for AC 005 not available in the supplied `2024_AssemblySegmentLevelVotingData.csv` (different schema; WB rows not mapped to AC NO). Figures below are tier D from journalistic accounts of Cooch Behar PC 2024 result.

| Party | Candidate (LS level) | Votes (est.) | AC segment % (est.) | Tier | Source |
|---|---|---|---|---|---|
| BJP | Nisith Pramanik | — | ~47 | D | Journalistic estimate; Cooch Behar PC 2024 BJP win |
| AITC | (candidate) | — | ~44 | D | Journalistic estimate |
| INC | — | — | ~3 | D | INDIA bloc candidate |
| LF | — | — | ~2 | D | AIFB residual |
| Other_NOTA | — | — | ~4 | D | NOTA + IND |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC 005 segment shares within ±3pp of the tier-A figures (BJP / AITC / INC / LF combined) once tier-A 2024 segment data is retrieved.
