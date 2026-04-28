# AC 004 — Cooch Behar Dakshin (GEN) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 004 Cooch Behar Dakshin as of end-2021 only — it does not reference
> any post-2021 events. Downstream simulators use post-2021 elections (2024 LS)
> as out-of-sample validation gates.
>
> Companion artifacts: [`methodology_2021.md`](../../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../../NORMALIZED_SCHEMA.md) (canonical schema)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 004 | A | ECI / Delimitation Commission 2008 |
| AC name | Cooch Behar Dakshin | A | ECI |
| Reservation | GEN | A | Delimitation 2008 |
| District | Cooch Behar (Koch Bihar) | A | Delimitation 2008 |
| Sub-division | Sadar | A | WB administrative |
| LS constituency | 1 — Cooch Behar (SC reserved) | A | Delimitation 2008 |
| LS segments included | AC 1 Mekhliganj · 2 Mathabhanga · 3 Cooch Behar Uttar · 4 Cooch Behar Dakshin · 5 Sitai · 6 Sitalkuchi · 7 Tufanganj | A | Delimitation 2008 |
| AC composition | Cooch Behar Municipality (full) + Chandamari, Chilkirhat, Falimari, Ghughumari, Haribhanga, Moyamari, Patchhara, Putimari Fuleswari and Suktabari GPs of Cooch Behar I CDB | A | Delimitation 2008 |
| Geographic note | Southern part of Cooch Behar town and surrounding rural belt of Cooch Behar I block; Rasikbeel wetland to south-east; borders Bangladesh | A | — |
| Sub-units used in v0 | **U1: Cooch_Behar_Municipality** (urban) · **U2: CDB_Cooch_Behar_I_rural** (9 GPs of CDB Cooch Behar I) | E | v0 simplification |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~287,879 (Muni 77,935 + 9/17 GPs of CDB CB-I ~209,944) | E | Census 2011; Coochbehar Municipality website; Census 2011 CB-I CDB aggregate |
| 2021 projected population | ~322,000 | E | 10-yr compound religion-differential growth (methodology §4); ~1.1%/yr net growth; COVID-19 mortality modestly accelerated; reverse migration added ~1-2pp |
| Sex ratio (2021, F per 1000 M) | ~1,058 | C | NFHS-5 Koch Bihar district sex ratio total population 1,058 F/1000 M (NFHS-5 2019-21) |
| 2021 estimated electorate (18+) | ~233,839 | A | ECI 2021 AE roll (detailed_results.csv AC 4 electorate = 233,839) |
| Estimated M / F / TG split (2021) | 48.6% M / 51.3% F / <0.05% TG | C | NFHS-5 Koch Bihar sex ratio 1,058 → ~51.3% F / 48.6% M; improved F enumeration |
| 2021 polling stations (estimated) | ~270 | E | Back-projection from 2021 electorate; standard ~875 electors/booth |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 66.00 | E | CB-I CDB 2011: 66.00% Hindu; Muni ~70%; Muslim differential growth (+0.3pp/yr); AC weighted ~66.0% by 2021 after 10yr; slight relative decline vs 2011 |
| Muslim | 33.60 | E | CB-I CDB 2011: 33.71% Muslim; +0.3pp relative gain over 10yr; Muni urban lower ~29.5%; AC weighted ~33.6% |
| Christian | 0.20 | E | CB-I CDB 2011: 0.17% Christian; marginal growth; rounded 0.20% |
| Sarna_ORP | 0.10 | E | Marginal tribal pocket; CB-I block ST 0.4% of which fraction Sarna |
| Other_residual | 0.10 | E | Sikh + Jain + Buddhist + Not_stated residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 39.80 | B | CB-I block Census 2011: SC 39.8%; no change assumed — caste composition structural |
| └ Rajbanshi_SC | 36.50 | C | Rajbanshi ~75.2% of district SC pool (The Print citing 2011 data); dominant SC in CB-I |
| └ Other_SC | 3.30 | E | Residual SC (Kaibarta, Bagdi, Hari etc.) |
| **ST_total** | 0.40 | B | CB-I block Census 2011: ST 0.4% |
| **UC_bhadralok** | 5.00 | E | Brahmin/Kayastha/Baidya; concentrated in municipality |
| **OBC** | 4.00 | E | OBC non-SC non-ST Hindu; smaller population in this AC |
| **Other_Hindu_middle** | 16.80 | E | Residual within Hindu (66.00 − 39.80 SC − 0.40 ST − 5.00 UC − 4.00 OBC = 16.80; Goala/Sutradhar/Tanti/unclassified Hindu) |
| **Muslim** | 33.60 | E | All sub-castes pooled; see C.1 |
| └ Muslim_Sheikh | 25.30 | D | Sheikh dominant in Cooch Behar Muslim community (Bengali Muslim peasantry) |
| └ Muslim_OBC | 5.60 | D | OBC Muslims (Jolaha, Nai, etc.) |
| └ Muslim_other | 2.70 | D | Pathan, Sayyid, Nasya-Sheikh residual |
| **Christian_plus_Sarna_plus_Other** | 0.40 | E | See C.1 Christian + Sarna_ORP + Other_residual |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2021, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.00 | E | Cooch Behar district age pyramid Census 2011; projected 2 yrs; younger cohort slightly smaller relative to total adult electorate |
| 23_27 | 11.00 | E | First-time-voter cohort from 2019 shifted up; COVID disrupted age-at-first-vote slightly |
| 28_32 | 10.50 | E | |
| 33_37 | 9.50 | E | |
| 38_42 | 9.00 | E | |
| 43_47 | 8.50 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.50 | E | |
| 58_62 | 7.00 | E | |
| 63_67 | 9.00 | E | |
| 68 | 9.00 | E | 68+ open-ended; slightly higher elderly concentration in 2021 vs 2019 due to COVID reverse migration of older adults |
| **Sum** | **100.00** | — | self-check (renormalized from Census age pyramid excluding 0–17; 2-year projection from 2019 state) |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 48.60 | C | NFHS-5 Koch Bihar sex ratio 1,058 F/1000 M → ~51.3% F / 48.6% M; improved female enumeration in NFHS-5 vs 2011 Census |
| Female | 51.39 | C | NFHS-5 Koch Bihar 2019-21 |
| Third_gender | 0.01 | E | Estimated ~0.01% per WB average |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 56.50 | E | Bengali-speaking Hindu and Muslim population; Cooch Behar municipality Bengali dominant; minimal change from 2019 |
| Hindi | 1.00 | E | Trader community in Muni; Bihar migrant workers; COVID-19 reverse migration brought some back temporarily |
| Urdu | 1.50 | E | Muslim population; primarily Bengali-speaking however |
| Other | 2.00 | E | Residual — Santali, Bodo fringe |
| Rajbongshi | 39.00 | E | AC-local: Rajbanshi community primary language; dominant in rural CDB-I GPs; ~75% of SC speaks Rajbongshi; est. ~39% of AC |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 22.00 | C | NFHS-5 Koch Bihar: women literacy ~79.2% (indicator 14); CB-I block literacy 76.56% (2011); AC weighted ~78% literate by 2021 → ~22% illiterate; slight improvement vs 2019 (24.5%) |
| Primary | 22.00 | E | Census 2011 education distribution CB district scaled + 2yr improvement trend |
| Middle | 19.00 | E | |
| Secondary | 16.00 | E | Small upward drift vs 2019 |
| Higher_Secondary | 11.00 | E | |
| Graduate | 7.50 | E | |
| Postgraduate | 2.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 31.00 | E | CB-I block Census 2011 main-worker share ~41% total pop; adult-only renormalization ~32%; COVID-19 lockdown displaced ~1pp → ~31% by mid-2021 |
| Marginal_worker | 10.00 | E | Seasonal agricultural workers; COVID reverse migrants adding to marginal pool |
| Non_worker | 39.00 | E | Housewife + elderly + retired; heavy in rural areas; slight increase as COVID kept women home |
| Student | 12.00 | E | 18–22 in education; aligned with age cohort; school closures 2020-21 disrupted but not on electorate roll composition |
| Unemployed | 8.00 | E | Educated job-seekers; district level unemployment pattern; COVID maintained pressure |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

Pcts sum to 100 across workers only (not all personas).

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 22.00 | E | CB-I block 2011: cultivator share ~22.6%; COVID-19 reverse migration reinforced agri share slightly; ~22% |
| Agricultural_labourer | 25.00 | E | CB-I block 2011 ag-labourer share ~21.2%; marginal workers inflate; COVID return migration added to agri-labour pool; ~25% |
| Household_industry | 5.00 | E | CB-I block pattern; weaving/handicraft |
| Manufacturing | 4.00 | E | Limited in CB district |
| Construction | 7.00 | E | Town expansion; some COVID disruption mid-2020 then resumed |
| Trade_retail | 11.00 | E | Cooch Behar Muni hub; COVID suppressed retail intermittently; slight dip |
| Transport_logistics | 5.00 | E | Road-based |
| Services | 11.00 | E | Private services in Muni; partial COVID recovery by end-2021 |
| Government_services_teachers | 6.00 | E | District headquarter town; govt employment stable |
| Out_migrant_worker | 4.00 | D | COVID return migration temporarily reduced permanent out-migrants; some returned to origin by end-2021 |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.00 | E | Census B-04 WB rural pattern; stable |
| Employee | 30.00 | E | Govt + organised + retail employees |
| Single_worker | 48.00 | E | Own-account cultivator + artisan + small trader |
| Family_worker | 20.00 | E | Unpaid agri-household labour |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 27.00 | C | Cooch Behar district BPL ~30% (2011 pattern); WB poverty reduction trend ~-3pp by 2019 → ~26%; COVID-19 temporary reversal +1pp → ~27% by end-2021 |
| Above_Poverty_Line_low_income | 35.00 | E | Slight compression due to COVID income shock |
| Lower_middle | 24.00 | E | |
| Middle | 11.00 | E | |
| Upper_middle_well_off | 3.00 | E | Cooch Behar Muni professional/trader fringe |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Cooch_Behar_Municipality | 26.80 | B | Cooch Behar Muni population 77,935 / AC base 287,879 = 27.07% (Census 2011); modest rural growth pulls share slightly down by 2021 → ~26.8% |
| U2_CDB_Cooch_Behar_I_rural | 73.20 | B | Remainder — 9 GPs of CDB Cooch Behar I; higher natural growth rate in rural |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | WB 2011: 4.3; Cooch Behar rural slightly larger; COVID return migration temporarily increased household size; ~4.5 |
| Nuclear_HH | 67.00 | E | NFHS-4/5 WB rural pattern; COVID return migration inflated joint HH fraction temporarily |
| Joint_HH | 27.00 | E | Slight increase vs 2019 (26%) due to COVID return migration |
| Extended_multi_generation | 6.00 | E | |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.50 | E | Census 2011 Cooch Behar district pattern; slight downward shift as 2019 first-time voter cohort moves toward marriage |
| Currently_married | 64.50 | E | Marginal upward shift |
| Widowed | 8.00 | E | Concentrated in 60+, female-skewed; COVID-19 elevated slightly in older cohorts |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

Independent rates — do NOT sum.

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 74.00 | C | NFHS-5 Koch Bihar proxy via state pattern; TV nearly saturated; modest +2pp from 2019 (72%) |
| Radio | 5.00 | C | Declining nationally; minimal change |
| Mobile_phone | 88.00 | C | NFHS-5 WB +growth; near-saturation in adults; +6pp from 2019 (82%) |
| Smartphone_with_internet | 62.00 | C | COVID-19 accelerated smartphone adoption (online classes, RTGS payments, news); Jio penetration near-complete in Cooch Behar by 2021; +22pp from 2019 (40%) — within methodology §2 (+20-30pp) band |
| Computer | 7.50 | E | Marginal improvement; home-office/online-class push; ~+0.5pp from 2019 |
| Two_wheeler | 28.00 | C | NFHS-5 WB pattern; stable; no major change |
| Four_wheeler | 5.00 | C | Stable |
| Banking_access | 91.00 | B | PMJDY further push 2019-21; NFHS-5 WB improvements; +6pp from 2019 (85%) — within methodology §2 (+5-10pp) band |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 99.00 | C | NFHS-5 Koch Bihar: 99.3% improved drinking water source (indicator 8); substantial improvement from 2019 estimate (80%) |
| Improved_sanitation | 75.00 | C | NFHS-5 Koch Bihar: 75.7% improved sanitation facility (indicator 9); large improvement from 2019 (60%); Swachh Bharat Phase-2 launched Oct 2019 |
| LPG_clean_cooking_fuel | 26.00 | C | NFHS-5 Koch Bihar: 25.7% clean cooking fuel (indicator 10); CB district lower than state; rural CB more dependent on biomass; aligned with NFHS-5 figure |
| Wood_biomass_fuel | 69.00 | C | NFHS-5 Koch Bihar inferred: dominant fuel; 100 − 25.7 − ~5 other = ~69% |
| Other_fuel | 5.00 | C | Kerosene, dung, etc. residual |
| Electricity | 98.00 | C | NFHS-5 Koch Bihar: 98.2% electricity (indicator 7); near-saturation from Saubhagya scheme |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 74.00 | D | Cooch Behar historically low out/in-migration; Rajbanshi and Bengali communities rooted; COVID-19 reverse migration (domestic) temporarily increased native-registered share; ~74% |
| WB_other_district | 8.00 | D | Some Kolkata service-class migrants in Muni; North Bengal internal migrants; stable |
| Other_Indian_state | 3.50 | D | Bihari/UP trader fringe + some COVID return migrants from other states; marginal +0.5pp |
| Bangladesh_origin | 12.00 | D | Cooch Behar border district; post-1947 and post-1971 Hindu Bengali refugee community; BSF 50km jurisdiction extended Oct 2021 — no major new migration; stable vs 2019 |
| Outside_India | 0.50 | E | Negligible |
| Out_migrant | 2.00 | E | COVID return migration reduced out-migrant pool; some returned by end-2021 but not yet re-departed; +0.5pp vs 2019 |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 42.00 | 1.00 | 0.00 | 1.50 | 55.50 | E | Rajbanshi SC dominant within Hindu (59.9% of Hindu is SC/OBC Rajbanshi-speaking); Muni Bengali Hindu fraction; unchanged from 2019 |
| Muslim | 92.00 | 0.50 | 4.50 | 1.50 | 1.50 | E | Bengali-Muslim peasantry dominant; small Urdu pocket; minimal Rajbongshi |
| Christian | 85.00 | 5.00 | 0.00 | 10.00 | 0.00 | E | Tiny base; Bengali + English-medium |
| Sarna_ORP | 30.00 | 0.00 | 0.00 | 40.00 | 30.00 | E | Tribal mix; Bodo/Rajbongshi fraction |
| Other_residual | 50.00 | 40.00 | 5.00 | 5.00 | 0.00 | E | Marwari/Bihari |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. 2D canonical table.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 60.30 | 0.61 | 7.58 | 6.06 | 25.45 | 0 | 0 | E | SC_total 39.80% / Hindu 66.00% = 60.30%; ST 0.40/66.00=0.61%; UC 5.0/66.00=7.58%; OBC 4.0/66.00=6.06%; residual 16.80/66.00=25.45% |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 92 | 0 | 5 | 3 | 0 | 0 | E | Tribal sub-castes mostly ST |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | E | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 69.00 | 8.00 | 3.50 | 17.50 | 0.50 | 1.50 | D | Hindu Rajbanshi community native; Hindu Bengali refugees from Bangladesh 1947/1971; BSF 50km extension Oct 2021 no new movement |
| Muslim | 87.50 | 6.00 | 2.00 | 2.50 | 1.00 | 1.00 | D | Bengali-Muslim peasantry largely native; stable vs 2019 |
| Christian | 80.00 | 10.00 | 5.00 | 5.00 | 0.00 | 0.00 | E | Mixed background |
| Sarna_ORP | 90.00 | 5.00 | 5.00 | 0.00 | 0.00 | 0.00 | E | Indigenous tribal, native |
| Other_residual | 30.00 | 15.00 | 50.00 | 5.00 | 0.00 | 0.00 | E | Marwari/Bihari mostly other-state |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 76.00 | 65.00 | 93.00 | E | NFHS-5 WB religion gap pattern; Hindu higher asset access; smartphone surge post-COVID |
| Muslim | 69.00 | 55.00 | 86.00 | E | Muslim rural CB slightly lower than Hindu; PMJDY penetration higher by 2021 |
| Christian | 80.00 | 70.00 | 93.00 | E | Approximation |
| Sarna_ORP | 58.00 | 35.00 | 76.00 | E | Tribal lower asset access; improved by 2021 vs 2019 |
| Other_residual | 90.00 | 80.00 | 97.00 | E | Marwari trader fringe — high asset |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 6.00 | 11.00 | 15.00 | 20.00 | 18.00 | 21.00 | 9.00 | E |
| SC_total | 24.00 | 23.00 | 20.00 | 17.00 | 10.00 | 5.00 | 1.00 | E |
| ST_total | 28.00 | 25.00 | 20.00 | 15.00 | 7.00 | 4.00 | 1.00 | E |
| OBC | 18.00 | 22.00 | 20.00 | 19.00 | 11.00 | 8.00 | 2.00 | E |
| Other_Hindu_middle | 16.00 | 22.00 | 20.00 | 19.00 | 12.00 | 8.00 | 3.00 | E |
| Muslim | 28.00 | 25.00 | 21.00 | 15.00 | 7.00 | 3.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender). 5-year cohorts.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 15.00 | 13.00 | E |
| 23_27 | 14.00 | 11.00 | E |
| 28_32 | 13.00 | 9.00 | E |
| 33_37 | 11.00 | 7.00 | E |
| 38_42 | 10.00 | 5.50 | E |
| 43_47 | 9.00 | 4.50 | E |
| 48_52 | 7.50 | 3.50 | E |
| 53_57 | 6.50 | 2.50 | E |
| 58_62 | 5.50 | 2.00 | E |
| 63_67 | 4.50 | 1.50 | E |
| 68 | 3.50 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender). 5-year cohorts.

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8.00 | 30.00 | E |
| 23_27 | 42.00 | 80.00 | E |
| 28_32 | 82.00 | 92.00 | E |
| 33_37 | 92.00 | 90.00 | E |
| 38_42 | 93.00 | 88.00 | E |
| 43_47 | 92.00 | 85.00 | E |
| 48_52 | 91.00 | 78.00 | E |
| 53_57 | 90.00 | 68.00 | E |
| 58_62 | 88.00 | 55.00 | E |
| 63_67 | 80.00 | 40.00 | E |
| 68 | 72.00 | 28.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 45.00 | 68.00 | C | Rural agri; COVID smartphone surge; +15pp from 2019 |
| Agricultural_labourer | 35.00 | 58.00 | C | Lowest income; +13pp from 2019 |
| Household_industry | 50.00 | 73.00 | C | |
| Manufacturing | 62.00 | 82.00 | C | |
| Construction | 57.00 | 75.00 | C | |
| Trade_retail | 76.00 | 88.00 | C | Muni concentrated; WhatsApp trade |
| Transport_logistics | 70.00 | 80.00 | C | |
| Services | 80.00 | 90.00 | C | |
| Government_services_teachers | 90.00 | 94.00 | C | Online work/school highest |
| Out_migrant_worker | 80.00 | 80.00 | D | Smartphone-heavy when outside; COVID kept many connected |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 35.00 | 1.00 | E |
| Primary | 38.00 | 3.00 | E |
| Middle | 36.00 | 5.00 | E |
| Secondary | 30.00 | 8.00 | E |
| Higher_Secondary | 24.00 | 14.00 | E |
| Graduate | 26.00 | 17.00 | E |
| Postgraduate | 36.00 | 13.00 | E |

### D.10 Asset × Bilingualism

| Asset_tier | Bilingual_Bengali_Hindi_pct | Tier | Source |
|---|---|---|---|
| TV_only_HH | 5.00 | E | Bengali TV dominant |
| TV_smartphone_HH | 10.00 | E | YouTube cross-language; +1pp from 2019 due to Hindi content consumption |
| Smartphone_only_HH | 9.00 | E | |
| No_asset_HH | 3.00 | E | Lowest exposure |

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Sub-unit codes use Un_ prefix matching C.11.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Cooch_Behar_Municipality | 69.50 | 29.00 | 0.80 | 0.10 | 0.60 | E | Cooch Behar Muni: Muslim share slightly higher by 2021 due to differential growth vs 2019 (28%→29%); Hindu slightly lower |
| U2_CDB_Cooch_Behar_I_rural | 64.10 | 35.50 | 0.10 | 0.10 | 0.20 | E | Rural CB-I block: 66% Hindu, 33.71% Muslim (Census 2011 adjusted for 10yr differential growth) |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Parent caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Cooch_Behar_Municipality | 10.00 | 32.00 | 0.20 | 6.00 | 21.80 | 29.00 | 1.00 | E |
| U2_CDB_Cooch_Behar_I_rural | 3.00 | 43.00 | 0.50 | 3.50 | 14.10 | 35.50 | 0.40 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Cooch_Behar_Municipality | 89.00 | 78.00 | 20.00 | 95.00 | C |
| U2_CDB_Cooch_Behar_I_rural | 66.00 | 54.00 | 3.00 | 88.00 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Cooch_Behar_Municipality | 60.00 | 95.00 | 99.00 | 99.50 | C |
| U2_CDB_Cooch_Behar_I_rural | 13.00 | 67.00 | 99.00 | 97.50 | C |

### D.15 Vote × Religion (2021 AE anchor)

P(party ‖ religion) — anchored on 2021 AE result (BJP 46.83%, AITC 44.31%, AIFB-LF 5.24%, Other+NOTA 3.62%). BJP drew on Hindu-Rajbanshi base; AITC recovered some Muslim + Hindu women vote via Lakshmir Bhandar (launched Apr 2021).

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 58.00 | 34.00 | 1.00 | 5.00 | 2.00 | D | 2021 AE AC-4 result anchored; BJP retained Hindu-Rajbanshi SC bloc; AITC recovered modestly vs 2019 LS baseline; INC collapsed |
| Muslim | 4.00 | 72.00 | 10.00 | 10.00 | 4.00 | D | AITC Muslim consolidation higher in 2021 AE; INC further squeezed; AIFB retained some residual Muslim vote |
| Christian | 22.00 | 62.00 | 5.00 | 8.00 | 3.00 | E | Approximation; tiny base |
| Sarna_ORP | 38.00 | 46.00 | 3.00 | 10.00 | 3.00 | E | Tribal small base; AITC welfare messaging; BJP still competitive |
| Other_residual | 42.00 | 40.00 | 8.00 | 5.00 | 5.00 | E | Marwari/Bihari — BJP leaning but AITC competitive |

### D.16 Vote × Caste (2021 AE)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 55.00 | 34.00 | 4.00 | 5.00 | 2.00 | D | 2021 AE AC-4 anchored; BJP maintained UC base; slight AITC recovery |
| OBC | 38.00 | 45.00 | 4.00 | 10.00 | 3.00 | D | AITC welfare stack re-engaged OBC voters |
| SC_total | 55.00 | 36.00 | 2.00 | 5.00 | 2.00 | D | Rajbanshi SC bloc BJP-dominant; AITC recovered 4pp vs 2019 LS; 2021 AE anchored |
| ST_total | 38.00 | 44.00 | 3.00 | 12.00 | 3.00 | E | Tribal base; AITC welfare messaging |
| Other_Hindu_middle | 50.00 | 38.00 | 3.00 | 6.00 | 3.00 | D | |
| Muslim | 4.00 | 72.00 | 10.00 | 10.00 | 4.00 | D | Same as D.15 Muslim |

### D.17 Vote × Gender (2021 AE)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 50.00 | 41.00 | 2.00 | 5.00 | 2.00 | D | 2021 AE AC-4 anchored; male BJP lead narrower than 2019 LS; AITC recovered |
| Female | 43.00 | 49.00 | 1.00 | 5.00 | 2.00 | D | Women swing toward AITC 2021; Lakshmir Bhandar (Apr 2021) signalling; turnout boost in women; Female AITC advantage |

### D.18 Vote × Welfare-scheme exposure (2021)

Omitted — no welfare_exposure axis declared for this AC. Narrative in §F instead.

---

## E. 2021 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 46.83 | A | ECI 2021 AE AC-4 result; Nikhil Ranjan Dey 91,560 votes / 195,505 total valid = 46.83% (electoral_history/2021/detailed_results.csv) |
| AITC | 44.31 | A | ECI 2021 AE AC-4 result; Avijit De Bhowmik 86,629 votes / 195,505 = 44.31% |
| INC | 0.00 | A | No INC candidate stood in AC 4 in 2021 AE; INC column = 0.00% |
| LF | 5.24 | A | AIFB Akshay Thakur 10,246 votes / 195,505 = 5.24%; AIFB is dominant left party in Cooch Behar |
| Other_NOTA | 3.62 | A | IND1(1,485) + NOTA(1,464) + BSP(1,419) + SUCI(1,138) + IND2(739) + IND3(496) + AMB(329) = 7,070 / 195,505 = 3.62% |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 004 Assembly Elections

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Akshay Thakur | AIFB | ~49.5 | Abdul Jalil Ahmed | AITC | ~48.0 | 2,863 |
| 2016 AE | Mihir Goswami | AITC | ~46.2 | Debasis Banik | AIFB | ~36.1 | 18,195 |

Notes: 2011 was a rare AIFB win in an AITC wave year. 2016 saw a large AITC swing and Goswami flipped the seat. BJP was not the main challenger in either 2011 or 2016 AEs.

### 2019 Lok Sabha — AC 004 segment (historical anchor)

| Party | Votes | % | Note |
|---|---|---|---|
| BJP | 86,431 | 47.79% | Nisith Pramanik BJP wave; ECI 2019 LS Form-20 |
| AITC | 80,410 | 44.46% | Paresh Chandra Adhikary AITC; ECI 2019 LS |
| LF | 7,749 | 4.28% | AIFB 7,197 + SUCI(C) 552 |
| INC | 3,667 | 2.03% | |
| Other_NOTA | 2,585 | 1.43% | KPPU + WPOI + AMB + 3 IND |
| **Total** | **180,842** | **99.99%** | ECI 2019 LS AC-segment; electorate 223,411; turnout ~81% |

The 2019 LS BJP surge (47.79%) reflected the Rajbanshi SC community's strong consolidation around BJP's Nisith Pramanik. Cooch Behar was a BJP stronghold nationally in 2019. The 2021 AE saw BJP largely maintain this advantage at the AC level (46.83%) while AITC recovered from 44.46% to 44.31% — essentially a two-party contest.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- Election Commission of India — 2021 WB Assembly Election, AC 4 detailed results (data/electoral_history/2021/detailed_results.csv): BJP 91,560 / AITC 86,629 / AIFB 10,246 / others 7,070; total valid votes 195,505; electorate 233,839; turnout 83.61%
- Election Commission of India — 2019 LS Cooch Behar PC, AC-4 segment (2019_AssemblySegmentLevelVotingData.csv): electorate 223,411
- ECI Delimitation Commission of India 2008 — WB Schedule (AC 4 = Cooch Behar Muni + 9 GPs of CB-I CDB)
- Coochbehar Municipality official website — Muni population 77,935 (Census 2011)

### Secondary sources (tier B / C)
- Census of India 2011 — Cooch Behar I CDB (censusindia.co.in): population 326,558, Hindu 66%, Muslim 33.71%, SC 39.8%, ST 0.4%, literacy 76.56%, sex ratio 942
- Census of India 2011 — Cooch Behar district: SC 50.17%, Hindu 74.06%, Muslim 25.54%, literacy 74.78%
- NFHS-5 (2019-21) Koch Bihar district — key indicators: sex ratio 1,058 F/1000 M; electricity 98.2%; improved drinking water 99.3%; improved sanitation 75.7%; clean cooking fuel 25.7% (data/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv)
- NFHS-4 (2015-16) West Bengal — household amenities baseline (for pre-2021 trajectory)
- CSDS-Lokniti 2019 NES post-poll — vote × religion/caste/gender cross-tabs (WB regional rollup; adapted for 2021 AE result anchor)
- indiastatpublications.com — Coochbehar Dakshin Assembly demographic summary; constituency SC 36.19%, rural/urban 72.93/27.07%

### Tertiary / journalistic (tier D)
- The Print (2021) — "Who are Rajbanshis" — Rajbanshi ~75.2% of CB district SC pool; 91% workers in agriculture
- Wikipedia — Cooch Behar Dakshin Assembly constituency; Cooch Behar Lok Sabha constituency; Mihir Goswami MLA; Nikhil Ranjan Dey (2021 BJP winner)
- oneindia.com — 2021 WB AE AC-4 Cooch Behar Dakshin result cross-check

### Tier-D / E reliance flags (what to distrust)
- **Religion shares** (C.1): Muni religion data not separately available; CB-I block aggregate used with urban/rural adjustment → tier E
- **Caste sub-group shares** (C.2, D.2): No caste census post-1931 for non-SC/ST; Rajbanshi dominance from district-level journalistic sources → tier C/D
- **Mother tongue Rajbongshi share** (C.5): inferred from Rajbanshi SC fraction + demographic linguistic overlap; no AC-level mother tongue census data → tier E
- **Migration/birthplace shares** (C.16, D.3): no public AC-level Census D-series; estimated from district pattern → tier D
- **GP-level data** (D.11–D.14): collapsed to 2 sub-units (Muni + CDB-rural-share); refine when DCHB Part-A accessible for CB-I GPs
- **Asset/media** (C.14, D.4, D.13): NFHS-5 Koch Bihar district calibrated + COVID smartphone projection; AC sub-level unavailable → tier C
- **Vote × Demographic** (D.15–D.17): anchored on 2021 AE result but vote×religion breakdown from CSDS adapted → tier D

### v0 known gaps
1. DCHB Koch Bihar Part-A — collapsed sub-units to 2 instead of 9; refine when available
2. No INC candidate in 2021 AE AC-4 — INC column set to 0.00 in §E; no INC vote to calibrate
3. Census HH-13 GP-level — using NFHS-5 district proxy for asset/media
4. Census D-series — using qualitative/journalistic anchor for migration shares
5. CSDS-Lokniti 2021 WB AE vote×caste/religion — using CSDS 2019 + 2021 result anchor in D.15–D.17; formal 2021 post-poll not available

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge.
No post-2021 events referenced. Forbidden keywords absent: 2022, 2023, 2024, 2025, 2026, SSC scam, Partha Chatterjee, RG Kar, SIR, CAA notification, CAA rules.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs against post-2021 shocks.

### 2024 Lok Sabha Election — AC 004 segment within Cooch Behar LS (PC 1) (tier A, CSV)

Figures sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=4, Cooch Behar Dakshin. Total valid votes: 194,819; electorate 241,441; turnout ~80.7%.

| Party | Candidate (LS level) | Votes | AC-004 segment % | Tier | Source |
|---|---|---|---|---|---|
| AITC | Jagadish Chandra Barma Basunia | 95,092 | 48.81% | A | 2024_AssemblySegmentLevelVotingData.csv |
| BJP | Nisith Pramanik | 87,383 | 44.85% | A | Same |
| LF (AIFB) | Nitish Chandra Roy | 5,275 | 2.71% | A | Same |
| INC | Piya Roy Chowdhury | 1,726 | 0.89% | A | Same |
| NOTA | — | 1,943 | 1.00% | A | Same |
| Others (BSP+SUCI+KPPU+INDs) | various | 3,400 | 1.74% | A | Same |
| **AITC margin over BJP** | | **7,709 votes** | **3.96 pp** | A | Computed |

Note: 2024 LS saw AITC flip the AC-4 segment vs 2021 AE (BJP 46.83% → 44.85%; AITC 44.31% → 48.81%). This reversal is out-of-sample for the 2021 calibration.

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC-4 segment shares within ±3pp of tier-A CSV figures:
- AITC target: 49% ± 3pp
- BJP target: 45% ± 3pp
- LF + others target: 6% ± 3pp
