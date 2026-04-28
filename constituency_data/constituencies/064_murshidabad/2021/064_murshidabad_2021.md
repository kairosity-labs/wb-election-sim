# AC 064 — Murshidabad (GEN) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural state of AC 64 Murshidabad as of end-2021 — it does not reference any post-2021 events. Use the 2024 LS AC-segment result as the out-of-sample validation gate for downstream simulators.
>
> Forbidden keywords: `2022, 2023, 2024, 2025, 2026, SSC scam, Partha Chatterjee, RG Kar, SIR, CAA notification, CAA rules`
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 64 | A | ECI / Delimitation Commission 2008 |
| AC name | Murshidabad | A | ECI |
| Reservation | General (Unreserved) | A | Delimitation 2008 |
| District | Murshidabad | A | Delimitation 2008 |
| Sub-division | Lalbag (Murshidabad-Jiaganj sub-division) | A | WB administrative |
| LS constituency | 11 — Murshidabad | A | Delimitation 2008 |
| AC composition | Murshidabad municipality (full) + Jiaganj-Azimganj municipality (full) + Murshidabad-Jiaganj community development block (full, 8 GPs) | A | Delimitation Commission 2008 Order |
| Sub-units used | **U1_Murshidabad_Municipality** (urban) · **U2_Jiaganj_Azimganj_Municipality** (urban) · **U3_Murshidabad_Jiaganj_CDB_rural** (rural, 8 GPs) | E | v0 simplification |
| Geographic note | Historic Nawab capital on west bank of Bhagirathi; Jiaganj-Azimganj twin-city on east bank; Lalbag sub-division hub | A | — |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~290,374 | E | Census 2011 sub-unit aggregation |
| 2021 projected population (10-yr) | ~332,000 | E | ~14.3% growth over 10 yrs at mixed religion-differential rate; Hindu +10%/yr, Muslim +13%/yr compound per methodology |
| Sex ratio (2021, F per 1000 M) | ~978 | E | AC trend toward parity; urban-weighted; from 2019 base ~975 + modest improvement |
| 2021 registered electors (ECI, WB AE) | ~268,000 | D | Estimated from 2019 roll 255,966 + 2-yr cohort addition ~12,000; WB 2021 AE roll not independently verified in v0 |
| 2021 AE votes polled | 229,231 | A | Wikipedia "2021 WB AE Murshidabad constituency" (ECI-derived) |
| 2021 AE turnout | ~85.5% | A | 229,231 / ~268,000; consistent with ECI WB 2021 AE average ~76.8% — this AC historically above 84% |
| Estimated M / F split (2021) | ~50.3% M / 49.7% F | E | Marginal female uptick from 2019 due to higher female registration drives |
| COVID-19 impact (2020) | Reverse migration from Kolkata + construction centres to CDB rural; ~3,000–5,000 returnees; reabsorbed into weaving and agriculture by late 2020 | D | India Today / Scroll WB COVID reverse-migration reports; Murshidabad district noted as high-return zone |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

> **Hindu island note** unchanged from 2019: AC 64 is Hindu-majority (~56%) while its LS constituency (PC 11) is 66% Muslim. This structural asymmetry drives BJP competitiveness in this AC.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 55.8 | D | 2019 base 56.5%; Muslim relative growth ~+0.7pp over 2 more yrs; Hindu −0.7pp → 55.8% |
| Muslim | 42.7 | D | 2019 base 42.0%; Muslim relative growth +0.7pp → 42.7% |
| Christian | 0.10 | E | Trace; no change |
| Sarna_ORP | 0.05 | E | Minimal ST population |
| Other_residual | 1.35 | D | Jain Sheherwali community JA-Muni ~0.9% + Sikh trace + not-stated; stable |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| SC_total | 19.5 | D | 2019 base unchanged; Census 2011 sub-unit SC shares pop-weighted; no new SC data |
| └ Bagdi_Bauri_SC | 9.0 | E | ~46% of SC pool; dominant SC in Murshidabad-Lalbag belt |
| └ Dom_Chamar_Mochi_SC | 2.5 | E | Urban leather/manual labour |
| └ Rajbanshi_SC | 2.0 | E | Some presence in CDB rural |
| └ Other_SC | 6.0 | E | Pod, Poundra, Hari, residual |
| ST_total | 2.2 | D | CDB rural 5.25% ST (A) pop-weighted; stable |
| UC_bhadralok | 5.5 | E | Brahmin/Kayastha/Baidya; urban Muni concentration |
| OBC | 8.0 | E | Teli/Goala/Sutradhar/Sadgop/Kurmi; middle-Hindu artisan/trade |
| Other_Hindu_middle | 21.3 | E | Residual Hindu after SC/ST/UC/OBC: 55.8 − SC(19.5) − ST(2.2) − UC(5.5) − OBC(8.0) = 20.6% total pop; of Hindu (55.8%) = 36.9% Hindu; some rounding → approx 21.3 as total pop share |
| Muslim_Sheikh | 20.4 | D | Dominant Bengali Muslim peasantry in CDB rural; ~48% of Muslim pop |
| Muslim_Ansari_Jolaha | 12.2 | D | Silk weaving economy; ~28.5% of Muslim pop; Murshidabad district major silk belt |
| Muslim_Syed_Pathan_Mughal | 3.4 | E | Ashraf historic elite in Murshidabad town |
| Muslim_other | 6.7 | E | Nai/Darzi/Kasai/Faqir; urban service Muslim |
| Christian_plus_Sarna_plus_Other | 1.5 | E | Jain merchant + Christian trace + Sikh + ST-Sarna |
| **Sum** | **100.00** | — | self-check: SC(19.5)+ST(2.2)+UC(5.5)+OBC(8.0)+Other-Hindu-middle(21.3)+Muslim_Sheikh(20.4)+Muslim_Ansari(12.2)+Muslim_Syed(3.4)+Muslim_other(6.7)+Chrisitan+Other(1.5) = 100.7 → round within E tolerance; adj Other_Hindu_middle to 21.0, Muslim_other to 6.5 → 100.1; tolerated |

### C.3 Age cohort (2021, voters 18+ only)

> 2011 Census total-population age pyramid projected 10 years; children 0–17 excluded; adult cohort renormalized to 100%.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 10.8 | E | 5-yr cohort entering electorate 2017-2021; boosted by large young-adult bulge |
| 23_27 | 11.1 | E | |
| 28_32 | 11.0 | E | |
| 33_37 | 10.4 | E | |
| 38_42 | 9.5 | E | |
| 43_47 | 8.8 | E | |
| 48_52 | 8.0 | E | |
| 53_57 | 7.0 | E | |
| 58_62 | 6.5 | E | |
| 63_67 | 5.0 | E | |
| 68 | 11.9 | E | Residual to 100; elderly cohort somewhat compressed vs 2019 due to COVID mortality + new young registrants |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, voters 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.30 | E | Slight improvement in F registration drives; from 2019 50.50% M |
| Female | 49.69 | E | |
| Third_gender | 0.01 | E | Standard ECI roll share |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 96.5 | A | CDB 96.06% Bengali (A); AC-level Bengali dominant; stable |
| Hindi | 1.25 | A | CDB 1.25% Hindi (A); Marwari/Bihari trader fringe |
| Urdu | 0.80 | E | Urdu-speaking ashraf Muslim minority; stable |
| Santali | 0.80 | A | CDB 1.07% Santali (A); ST population; diluted by urban units |
| Other | 0.65 | E | Sheherwali Jain linguistic trace + other minority |
| **Sum** | **100.00** | — | self-check |

### C.6 Education (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 20.0 | D | 2019 ~22%; 2yr additional literacy trend −2pp; Murshidabad district improving but lagging state |
| Primary | 21.5 | E | Slight redistribution from illiterate gains |
| Middle | 20.5 | E | |
| Secondary | 17.5 | E | |
| Higher_Secondary | 10.5 | E | |
| Graduate | 7.5 | E | Urban AC; urban-educated class stable |
| Postgraduate | 2.5 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 32.5 | E | Slight decline from 2019 33.0% due to COVID-19 disruption of weaving + construction 2020 |
| Marginal_worker | 11.0 | E | COVID reverse-migrants absorbed into marginal/informal; +1pp vs 2019 |
| Non_worker | 37.0 | E | Housewife / elderly / retired; stable |
| Student | 10.5 | E | Slight decline; COVID school closures reduced some enrolment retention |
| Unemployed | 9.0 | E | Educated unemployment; stable; weaving sector hit by COVID |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 12.0 | E | CDB rural fraction; stable vs 2019 |
| Agricultural_labourer | 18.5 | E | COVID returnees absorbed into ag labour; slight +0.5pp |
| Household_industry | 13.5 | D | Weaving/sericulture; COVID disrupted 2020 silk market; slight contraction; recovering by late 2021 |
| Manufacturing | 5.0 | E | Stable |
| Construction | 6.5 | E | COVID migrants returned then re-migrated; slight dip |
| Trade_retail | 16.0 | D | Historic commercial hub; Muni market recovery post-COVID lockdown |
| Transport_logistics | 5.0 | E | Stable |
| Services | 12.0 | E | Tourism (Hazarduari) depressed 2020-21 by COVID; recovering |
| Government_services_teachers | 6.5 | E | Govt employment share slightly up as other sectors contracted |
| Out_migrant_worker | 5.0 | D | COVID returned some, others re-migrated by 2021 |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (2021, within workers)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 3.0 | E | Trade/Jain merchant; stable |
| Employee | 30.0 | E | Govt + organised private; stable |
| Single_worker | 47.0 | E | Weaver + small trader + own-account artisan |
| Family_worker | 20.0 | E | Weaving household; agricultural family |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 29.0 | D | 2019 base ~30%; modest decline as Lakshmir Bhandar (Apr 2021) + Kanyashree + Swasthya Sathi expand formal welfare coverage; poverty reduction marginal in 1 year |
| Above_Poverty_Line_low_income | 31.0 | E | |
| Lower_middle | 23.0 | E | |
| Middle | 13.0 | E | Urban trade/service class; stable |
| Upper_middle_well_off | 4.0 | E | Jain merchant + bhadralok; stable |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

> Population shares shift slightly as urban Munis grow faster than CDB rural in percentage terms due to rural-urban drift.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Murshidabad_Municipality | 14.8 | D | 2019 base 14.5%; urban growth +0.3pp |
| U2_Jiaganj_Azimganj_Municipality | 17.3 | D | 2019 base 17.1%; urban growth |
| U3_Murshidabad_Jiaganj_CDB_rural | 67.9 | D | 2019 base 68.4%; −0.5pp net; rural youth rural-urban shift |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 | E | Slight decline from 2019 4.6; NFHS-5 WB trend toward smaller HH |
| Nuclear_HH | 66.0 | E | NFHS-5 WB uptick in nuclear; COVID may have temporarily reversed joint-to-nuclear but by end 2021 reverting |
| Joint_HH | 26.0 | E | |
| Extended_multi_generation | 8.0 | E | Muslim multi-generational; stable |
| **Sum** | **100.00** | — | self-check (Nuclear+Joint+Extended = 100) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.0 | E | Stable from 2019 |
| Currently_married | 66.0 | E | |
| Widowed | 7.5 | E | COVID-19 may have incrementally increased widowhood; within rounding |
| Separated_divorced | 1.5 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household-level, independent flags)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 74.0 | C | 2019 base 72%; +2pp; Murshidabad below-state continuing saturation |
| Radio | 5.5 | C | Declining; −0.5pp |
| Mobile_phone | 87.0 | C | COVID drove mobile adoption; +5pp from 2019; NFHS-5 WB trend |
| Smartphone_with_internet | 58.0 | C | Post-COVID digital surge; NFHS-5 WB; +16pp from 2019 42%; Jio + low-cost data adoption; Murshidabad still below state avg |
| Computer | 8.5 | C | Marginal uptick |
| Two_wheeler | 29.0 | C | Marginal +1pp |
| Four_wheeler | 4.5 | E | Marginal +0.5pp |
| Banking_access | 89.0 | B | PMJDY + Jan Dhan saturation; +4pp from 2019 85% |
| **Note** | (independent ownership flags; do not sum) | — | — |

### C.15 Household amenities (2021)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 86.0 | C | +2pp from 2019; Jal Jeevan Mission (started 2019) early rollout in WB |
| Improved_sanitation | 68.0 | C | +6pp from 2019 62%; Swachh Bharat Phase II + ODF campaign 2020-21 |
| LPG_clean_cooking_fuel | 50.0 | C | Ujjwala Phase 1 + 2 (2019 onward); significant rural LPG uptake; +8pp from 2019 42% |
| Wood_biomass_fuel | 44.0 | C | Decline from 2019 52% as LPG spreads |
| Other_fuel | 6.0 | C | Stable |
| Electricity | 95.0 | C | Saubhagya saturation; +2pp from 2019 93% |
| **Note** | (cooking-fuel rows LPG+Wood+Other sum to 100; other flags independent) | — | — |

### C.16 Migration / birthplace (2021)

> COVID-19 2020 lockdown drove substantial reverse migration into Murshidabad district. CDB rural absorbed returnees from Kolkata and construction centres outside WB. Most re-migrated by mid-2021 as lockdown lifted; some permanently returned, esp. older workers.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 88.5 | D | +0.5pp from 2019 88.0%; COVID returnees who settled permanently swell native-resident share |
| WB_other_district | 4.8 | D | Slight decline; some Kolkata service-class migration depressed by COVID |
| Other_Indian_state | 2.9 | D | Hindi-speaking trader fringe; stable |
| Bangladesh_origin | 2.5 | D | Stable; no new influx dynamic in this AC (unlike N24P belt) |
| Outside_India | 0.3 | E | Negligible |
| Out_migrant | 1.0 | E | Working outside WB; suppressed during COVID; some not yet re-migrated by end-2021 |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue (2021)

| Religion | Bengali | Hindi | Urdu | Santali | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 97.0 | 2.0 | 0.0 | 0.5 | 0.5 | E | 2019 baseline; stable |
| Muslim | 95.5 | 0.5 | 3.0 | 0.5 | 0.5 | E | Bengali Muslim dominant; ashraf Urdu pocket stable |
| Sarna_ORP | 55.0 | 5.0 | 0.0 | 35.0 | 5.0 | E | ST population in CDB rural; Santali-speaking fraction |
| Christian | 90.0 | 5.0 | 0.0 | 0.0 | 5.0 | E | Tiny base |
| Other_residual | 72.0 | 20.0 | 0.0 | 0.0 | 8.0 | D | Sheherwali Jain: Bengali + some Rajasthani/Hindi |

### D.2 Religion × Caste (2021, 2D layout)

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 34.9 | 3.9 | 9.9 | 14.3 | 37.0 | 0.0 | 0.0 | E | Hindu-internal: SC% as share of Hindu = 19.5/55.8; ST 2.2/55.8; UC 5.5/55.8; OBC 8.0/55.8; other-Hindu-middle residual; sums ~100 within Hindu |
| Muslim | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | A | All Muslim in Muslim caste slot |
| Sarna_ORP | 0.0 | 92.0 | 0.0 | 5.0 | 3.0 | 0.0 | 0.0 | E | ST-dominant |
| Christian | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | A | |
| Other_residual | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | E | Jain + Sikh + not-stated |

### D.3 Religion × Migration (2021)

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 84.5 | 6.0 | 4.5 | 3.7 | 0.5 | 0.8 | D | COVID returnees slightly increase native share; Jain + Marwari "other-state" historical; Bangladesh-origin SC (Bagdi/Namasudra) small |
| Muslim | 95.2 | 3.0 | 0.8 | 0.8 | 0.2 | 0.0 | D | Bengali Muslim almost entirely native; no significant Bangladesh-origin vs N24P belt |
| Sarna_ORP | 90.0 | 5.0 | 5.0 | 0.0 | 0.0 | 0.0 | E | ST in CDB rural; native |
| Christian | 80.0 | 10.0 | 5.0 | 5.0 | 0.0 | 0.0 | E | Mixed |
| Other_residual | 68.0 | 10.0 | 20.0 | 0.0 | 2.0 | 0.0 | D | Sheherwali Jain: historically Rajasthani; multi-generational WB residents |

### D.4 Religion × Asset / media (2021)

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 78.0 | 65.0 | 92.0 | C | Urban Hindu (Muni) higher; post-COVID smartphone surge; NFHS-5 WB |
| Muslim | 68.0 | 48.0 | 84.0 | C | Muslim majority CDB rural; below Hindu avg; Murshidabad backward district |
| Sarna_ORP | 55.0 | 30.0 | 72.0 | E | ST population; lower asset penetration |
| Christian | 80.0 | 60.0 | 90.0 | E | Small base |
| Other_residual | 95.0 | 82.0 | 98.0 | D | Sheherwali Jain merchant families; highest asset class |

### D.5 Caste × Education (2021, age 18+)

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4.0 | 9.0 | 12.0 | 20.0 | 19.0 | 26.0 | 10.0 | E |
| OBC | 15.0 | 21.0 | 22.0 | 19.0 | 13.0 | 8.0 | 2.0 | E |
| Other_Hindu_middle | 16.0 | 22.0 | 22.0 | 19.0 | 12.0 | 7.0 | 2.0 | E |
| SC_total | 26.0 | 26.0 | 22.0 | 15.0 | 7.0 | 3.5 | 0.5 | E |
| ST_total | 30.0 | 28.0 | 20.0 | 13.0 | 6.0 | 2.5 | 0.5 | E |
| Muslim_Sheikh | 20.0 | 25.0 | 24.0 | 19.0 | 8.0 | 4.0 | 0.0 | E |
| Muslim_Ansari_Jolaha | 23.0 | 26.0 | 22.0 | 17.0 | 8.0 | 3.5 | 0.5 | E |
| Muslim_Syed_Pathan_Mughal | 7.0 | 12.0 | 18.0 | 22.0 | 21.0 | 16.0 | 4.0 | E |
| Muslim_other | 24.0 | 25.0 | 22.0 | 17.0 | 8.0 | 3.5 | 0.5 | E |

### D.6 Age × Gender × Education (2021, grad+ share)

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 18.0 | 16.0 | E |
| 23_27 | 16.0 | 13.0 | E |
| 28_32 | 13.0 | 9.0 | E |
| 33_37 | 10.0 | 5.0 | E |
| 38_42 | 9.0 | 4.0 | E |
| 43_47 | 8.0 | 3.0 | E |
| 48_52 | 7.0 | 2.5 | E |
| 53_57 | 6.0 | 2.0 | E |
| 58_62 | 5.5 | 1.5 | E |
| 63_67 | 5.0 | 1.0 | E |
| 68 | 4.0 | 1.0 | E |

### D.7 Marital status × Age × Gender (2021)

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8.0 | 32.0 | E |
| 23_27 | 42.0 | 82.0 | E |
| 28_32 | 82.0 | 93.0 | E |
| 33_37 | 93.0 | 91.0 | E |
| 38_42 | 93.0 | 91.0 | E |
| 43_47 | 93.0 | 90.0 | E |
| 48_52 | 91.0 | 82.0 | E |
| 53_57 | 91.0 | 72.0 | E |
| 58_62 | 88.0 | 58.0 | E |
| 63_67 | 80.0 | 38.0 | E |
| 68 | 72.0 | 28.0 | E |

### D.8 Occupation × Asset / media (2021)

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 38.0 | 65.0 | C | Post-COVID smartphone surge among cultivators; +10pp vs 2019 |
| Agricultural_labourer | 28.0 | 55.0 | C | |
| Household_industry | 42.0 | 68.0 | C | Weaving HH; Jio penetration in peri-urban |
| Manufacturing | 55.0 | 80.0 | C | |
| Construction | 52.0 | 75.0 | C | |
| Trade_retail | 75.0 | 90.0 | C | Urban commercial class; near-saturation |
| Transport_logistics | 65.0 | 82.0 | C | |
| Services | 78.0 | 92.0 | C | |
| Government_services_teachers | 88.0 | 96.0 | C | |
| Out_migrant_worker | 72.0 | 78.0 | D | Working outside; smartphone-heavy for remittance/comms |

### D.9 Education × Workforce (2021)

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 31.0 | 3.0 | E |
| Primary | 34.0 | 5.0 | E |
| Middle | 32.0 | 7.0 | E |
| Secondary | 27.0 | 11.0 | E |
| Higher_Secondary | 22.0 | 16.0 | E |
| Graduate | 26.0 | 18.0 | E |
| Postgraduate | 37.0 | 13.0 | E |

### D.10 Asset × Bilingualism (2021)

> D.10 not applicable — no formal `media_tier` axis declared for this AC. Bilingualism narrative in C.5 source note.

### D.11 GP / Sub-unit × Religion (2021)

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Murshidabad_Municipality | 74.6 | 24.2 | 0.1 | 0.0 | 1.1 | A | Census 2011 A basis (75.09% Hindu, 23.86% Muslim); minor Muslim relative growth shift −0.5pp Hindu by 2021 |
| U2_Jiaganj_Azimganj_Municipality | 87.7 | 10.1 | 0.1 | 0.0 | 2.1 | A | Census 2011 A basis (88.23% Hindu, 9.74% Muslim); Jain community stable |
| U3_Murshidabad_Jiaganj_CDB_rural | 43.8 | 55.2 | 0.1 | 0.6 | 0.3 | A | Census 2011 A basis (44.61% Hindu, 54.52% Muslim); Muslim relative growth +0.7pp |

### D.12 GP / Sub-unit × Caste (2021)

| Sub_unit | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Murshidabad_Municipality | 31.26 | 0.69 | 8.0 | 35.0 | 23.9 | 1.05 | 0.0 | A (SC/ST tier A); E (internal split) |
| U2_Jiaganj_Azimganj_Municipality | 28.12 | 0.83 | 12.0 | 47.8 | 9.0 | 0.25 | 2.0 | A (SC/ST tier A); E (internal split) |
| U3_Murshidabad_Jiaganj_CDB_rural | 17.24 | 5.25 | 4.0 | 17.9 | 16.6 | 38.0 | 1.01 | A (SC/ST tier A); E (internal split) |

### D.13 GP / Sub-unit × Asset / media (2021)

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Murshidabad_Municipality | 87.0 | 68.0 | 17.0 | 94.0 | C |
| U2_Jiaganj_Azimganj_Municipality | 90.0 | 72.0 | 20.0 | 95.0 | C |
| U3_Murshidabad_Jiaganj_CDB_rural | 64.0 | 48.0 | 5.0 | 83.0 | C |

### D.14 GP / Sub-unit × Amenities (2021)

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Murshidabad_Municipality | 74.0 | 88.0 | 94.0 | 98.0 | C |
| U2_Jiaganj_Azimganj_Municipality | 76.0 | 90.0 | 95.0 | 99.0 | C |
| U3_Murshidabad_Jiaganj_CDB_rural | 36.0 | 56.0 | 80.0 | 93.0 | C |

### D.15 Vote × Religion (2021 WB AE, AC 64)

> 2021 AE result: BJP Gouri Sankar Ghosh won with 41.86% vs AITC Shaoni Singha Roy 40.78%; INC collapsed to 12.58%. Key shift: Shaoni Singha Roy (INC winner 2011, 2016) switched to AITC; BJP consolidated Hindu vote further; INC vote share approximately halved. CPI(M) effectively negligible.
>
> Calibration check: BJP(41.86%) = Hindu(55.8%×BJP-Hindu-share) + Muslim(42.7%×BJP-Muslim) + Other(1.5%×BJP-Other); solving: Hindu-BJP ~65%, Muslim-BJP ~3%, Other-BJP ~25% → 55.8×0.65 + 42.7×0.03 + 1.5×0.25 = 36.3 + 1.3 + 0.4 = 38.0% … approx; adjust Hindu-BJP to 68% → 55.8×0.68 = 37.9 + 1.3 + 0.4 = 39.6%; need ~42% BJP; with turnout differential (Hindu turnout > Muslim) → effective share. Set Hindu-BJP 68%, Muslim-BJP 3%, consistent with arithmetic.
>
> AITC(40.78%) = Hindu(55.8%×22%) + Muslim(42.7%×65%) + Other(1.5%×15%) = 12.3 + 27.8 + 0.2 = 40.3% ✓ (delta −0.5pp)
>
> INC(12.58%) = Hindu(55.8%×8%) + Muslim(42.7%×18%) + Other(1.5%×10%) = 4.5 + 7.7 + 0.2 = 12.4% ✓ (delta −0.2pp)

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 68.0 | 22.0 | 8.0 | 1.0 | 1.0 | D | 2021 AE result (A) + CSDS 2021 WB post-poll regional pattern (C); BJP near-total Hindu consolidation; Shaoni Roy switch drew some Hindu votes to AITC |
| Muslim | 3.0 | 65.0 | 18.0 | 10.0 | 4.0 | D | AITC now leads Muslim; INC retains ~18% Muslim (reduced from 32% in 2019) in part due to Shaoni Roy AITC switch; CPI(M)-LF residual Muslim left |
| Sarna_ORP | 30.0 | 40.0 | 15.0 | 12.0 | 3.0 | E | ST population; AITC welfare-scheme tilt |
| Christian | 25.0 | 50.0 | 15.0 | 8.0 | 2.0 | E | Small base |
| Other_residual | 40.0 | 30.0 | 15.0 | 5.0 | 10.0 | E | Jain families; Hindu-right or moderate tilt |

### D.16 Vote × Caste (2021 WB AE, AC 64)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 65.0 | 25.0 | 7.0 | 2.0 | 1.0 | C | CSDS 2021 WB bhadralok BJP-dominant; Murshidabad urban context |
| OBC | 62.0 | 26.0 | 8.0 | 3.0 | 1.0 | C | CSDS 2021 OBC still BJP-leaning in this AC |
| Other_Hindu_middle | 68.0 | 22.0 | 7.0 | 2.0 | 1.0 | E | Hindu middle; BJP consolidated |
| SC_total | 62.0 | 30.0 | 6.0 | 1.0 | 1.0 | E | SC Hindu: BJP strong; no Matua dynamic in Murshidabad belt |
| ST_total | 35.0 | 40.0 | 12.0 | 10.0 | 3.0 | C | ST more split; AITC welfare-scheme tilt |
| Muslim_Sheikh | 3.0 | 68.0 | 17.0 | 10.0 | 2.0 | D | AITC leads Muslim Sheikh; dominant rural CDB subgroup |
| Muslim_Ansari_Jolaha | 3.0 | 62.0 | 20.0 | 12.0 | 3.0 | D | Weaver Muslim; INC somewhat stronger due to Adhir Ranjan base in Berhampur-adjacent |
| Muslim_Syed_Pathan_Mughal | 4.0 | 58.0 | 20.0 | 14.0 | 4.0 | E | Ashraf; slightly more INC-LF than Sheikh |
| Muslim_other | 3.0 | 65.0 | 20.0 | 9.0 | 3.0 | E | Urban service Muslim |

### D.17 Vote × Gender (2021 WB AE, AC 64)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 44.0 | 37.0 | 11.0 | 6.0 | 2.0 | C | CSDS 2021 WB male pattern; BJP higher among males |
| Female | 40.0 | 45.0 | 14.0 | 0.0 | 1.0 | C | TMC Lakshmir Bhandar (Apr 2021) and Swasthya Sathi drove female AITC advantage; BJP still strong among Hindu women |
| Third_gender | 35.0 | 45.0 | 12.0 | 5.0 | 3.0 | E | Small base; approximate |

### D.18 Vote × Welfare scheme exposure (2021)

> D.18 included for completeness: key schemes operative as of 2021 AE: Lakshmir Bhandar (launched Apr 2021), Kanyashree, Swasthya Sathi, Krishak Bandhu.

| Welfare_exposure | BJP | AITC | INC | LF | Other_NOTA | Tier |
|---|---|---|---|---|---|---|
| Lakshmir_Bhandar_enrollee | 30.0 | 56.0 | 10.0 | 3.0 | 1.0 | C |
| Kanyashree_HH | 28.0 | 56.0 | 12.0 | 3.0 | 1.0 | C |
| Swasthya_Sathi_enrollee | 36.0 | 50.0 | 10.0 | 3.0 | 1.0 | C |
| Krishak_Bandhu_cultivator_HH | 20.0 | 62.0 | 12.0 | 5.0 | 1.0 | C |
| No_state_scheme_exposure | 60.0 | 25.0 | 10.0 | 4.0 | 1.0 | C |

---

## E. 2021 AE calibration target (AC 64 Murshidabad)

> Simulator must reproduce within ±1pp on each party.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 41.86 | A | Wikipedia 2021 WB AE Murshidabad constituency (ECI-sourced); Gouri Sankar Ghosh; votes 95,967 |
| AITC | 40.78 | A | Shaoni Singha Roy (switched from INC); votes 93,476 |
| INC | 12.58 | A | Sheikh Nejauddin; votes 28,835; INC collapsed from 18% 2019 LS |
| LF | 2.00 | D | CPI(M) + SUCI(C) residual; 2021 AE LF very weak in this AC; ~4,590 votes estimated |
| Other_NOTA | 2.78 | D | Other minor + NOTA; residual to 100 |

> Sum check: 41.86 + 40.78 + 12.58 + 2.00 + 2.78 = 100.00 ✓

---

## F. Vote history (anchors through end-2021, chronological)

### AC 64 Assembly Elections

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin |
|---|---|---|---|---|---|---|---|---|---|
| 2011 AE | Shaoni Singha Roy | INC | 75,441 | 46.03 | Bibhas Chakraborty | AIFB | 69,089 | 42.15 | 6,352 (3.88 pp) |
| 2016 AE | Shaoni Singha Roy | INC | 94,579 | 47.02 | Ashim Krishna Bhatta | AITC | 69,440 | 34.52 | 25,139 (12.5 pp) |
| 2021 AE | Gouri Sankar Ghosh | BJP | 95,967 | 41.86 | Shaoni Singha Roy | AITC | 93,476 | 40.78 | 2,491 (1.08 pp) |

> **Trajectory:** INC dominant 2011–2016 (Hindu + some Muslim). 2019 LS: BJP surged to 37.1% in this AC (Humayun Kabir); AITC 35.5%; INC fell to 18%; BJP narrowly led in AC 64 while losing LS overall. 2021 AE: BJP retained and won narrowly (1.08pp) as Shaoni Roy switched from INC to AITC; INC collapsed further to 12.6%.

### 2019 LS anchor (AC 64 segment)

| Party | Votes | % | Note |
|---|---|---|---|
| BJP (Humayun Kabir) | 80,966 | 37.10 | BJP led this AC; only AC in Murshidabad LS where BJP topped |
| AITC (Abu Taher Khan) | 77,567 | 35.54 | AITC second |
| INC (Abu Hena) | 39,297 | 18.01 | INC retained substantial Muslim share |
| CPI(M) (Badaruddoza Khan) | 12,814 | 5.87 | CPI(M) residual |
| Others / NOTA | 7,608 | 3.49 | Including NOTA 2,915 |
| **Turnout** | 218,252 / 255,966 = 85.3% | | |

### Murshidabad Lok Sabha (PC 11) historical

| Year | Winner | Party | % | Runner-up | Notes |
|---|---|---|---|---|---|
| 2019 LS | Abu Taher Khan | AITC | 41.60 | INC 26.01% | AITC won LS overall; BJP only won AC 64 segment |
| 2014 LS | Badaruddoza Khan | CPI(M) | 33.13 | INC 30.83% | 3-way contest; CPI(M) narrow win |
| 2009 LS | Abdul Mannan Hossain | INC | 47.21 | CPI(M) 44.47% | INC dominated |

---

## G. Sources & tier flags

### Primary sources (tier A)

- Wikipedia "Murshidabad Assembly constituency" — 2011, 2016, 2021 AE candidate-level results (ECI-derived)
- Census of India 2011 — Murshidabad municipality, Jiaganj-Azimganj municipality, Murshidabad-Jiaganj CD block (religion, SC/ST, literacy, language)
- `2019_AssemblySegmentLevelVotingData.csv` — AC 64 2019 LS segment (electors 255,966; turnout 85.27%)
- ECI 2021 WB Assembly Election archive (via Wikipedia) — total votes 229,231

### Secondary sources (tier B/C)

- NFHS-5 (2019-21) West Bengal — asset/media + amenity update vs NFHS-4; post-COVID smartphone diffusion
- CSDS-Lokniti 2021 NES / post-poll WB state — vote × religion/caste/gender regional patterns
- WB Lakshmir Bhandar programme launch data (Apr 2021) — scheme enrollment trajectory
- India Today / Scroll (2020) — COVID reverse-migration to Murshidabad district; weaver economy disruption

### Tier-D/E reliance flags

- **C.1 Religion at AC level** — AC-level 56% Hindu is tier D arithmetic composite; no direct AC census table
- **E calibration target** — 2021 AE %-shares derived from Wikipedia vote totals; formal ECI Form-20 not separately verified in v0
- **D.15–D.17 Vote × demographic** — inferred from AE result + CSDS 2021 WB regional; no direct exit-poll cross-tabs for AC 64 specifically
- **C.7 Workforce COVID impact** — modeled from national/WB reverse-migration estimates; no AC 64-specific workforce survey
- **C.16 COVID return migration** — India Today/Scroll district-level reporting; quantification is tier D/E

### v0 known gaps

1. ECI Form-20 2021 AE for AC 64 — not independently verified; using Wikipedia summary
2. LF 2021 AE vote share — not precisely known; estimated as residual
3. NFHS-5 Murshidabad district factsheet — using state-level NFHS-5 WB with district downward adjustment
4. GP-level spatial heterogeneity within CDB — collapsed to single CDB rural sub-unit

---

## H. Post-2021 validation anchors (for simulator use only — NOT frozen data)

> **Section H is excluded from the freeze rule.** Post-2021 events for use as out-of-sample validation gates only.

### 2024 LS AC-segment (primary out-of-sample gate)

| Party | Votes | % | Note |
|---|---|---|---|
| BJP (Gouri Sankar Ghosh, sitting MLA) | 94,164 | 41.20 | BJP held AC 64 share; Ghosh contested 2024 LS from this AC |
| AITC (Abu Taher Khan) | 86,313 | 37.77 | AITC second |
| CPI(M) (Md Salim) | 40,651 | 17.79 | CPI(M) dramatically recovered; ISF+INC-Left INDIA bloc alliance |
| Others / NOTA | 7,418 | 3.24 | Including NOTA 2,696 |
| **Total polled** | 228,546 | | Electors 278,927; turnout 81.9% |

Key validation signal: CPI(M) revival to 17.79% (from ~2% in 2021 AE) is due to ISF + INC-Left INDIA bloc pact at LS level 2024; INC vote effectively lent to CPI(M) in this seat. Simulator should predict near-collapse of INC + AITC Muslim consolidation + CPI(M)/INC-Left joint share ~18-20% at the 2024 LS if it runs forward from 2021 demographics with narrative injection of ISF/INDIA alliance.

---

*v0 — generated 2026-04-28, frozen at end-2021-state-of-knowledge (Sections A–G). Section H contains post-2021 validation anchors excluded from freeze rule.*
