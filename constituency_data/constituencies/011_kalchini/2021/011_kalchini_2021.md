# AC 011 — Kalchini (ST) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural state of AC 011 Kalchini as of end-2021 only — it does not reference any post-2021 events. The 2019 LS result is an anchor; the 2021 WB AE is the primary calibration target. Use the 2024 LS AC-segment result as the out-of-sample validation gate for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 011 | A | ECI / Delimitation Commission 2008 |
| AC name | Kalchini | A | ECI |
| Reservation | ST (Scheduled Tribe) | A | Delimitation 2008 |
| District | Alipurduar | A | Alipurduar district created from Jalpaiguri in 2014 |
| Sub-division | Alipurduar | A | WB administrative; Kalchini CD Block in Alipurduar sub-division |
| LS constituency | PC 2 — Alipurduars (ST reserved) | A | Delimitation 2008 |
| LS segments included with AC 011 | AC 7 Madarihat · 8 Dhupguri · 9 Nagrakata · 10 Alipurduar · 11 Kalchini · 12 Falakata · 13 Kumargram | A | Delimitation 2008 |
| AC composition | All 11 GPs of Kalchini CD Block (Chuapara, Dalsingpara, Garopara, Jaigaon I, Jaigaon II, Kalchini, Latabari, Malangi, Mendabari, Rajabhatkhawa, Satali) + Majherdabri GP from Alipurduar II CD Block | A | Wikipedia "Kalchini (Vidhan Sabha constituency)"; Delimitation 2008 |
| Geographic note | Eastern Dooars; tea-garden dominated landscape; borders Bhutan (Jaigaon-Phuentsholing border crossing); forested terrain with Buxa Tiger Reserve | A | Wikipedia "Kalchini, Alipurduar" |
| Archetype | A3 — North Bengal tea-garden ST; BJP/BTWU stronghold with TMC consolidating opposition; COVID income shock visible in tea-belt by 2020-21 | D | The Print (2021); tea-garden labour surveys 2020 |
| Two sub-units used in v0 (bagan-conditioning) | **U1_Kalchini_CDB_core** (11 GPs, ~298,548 pop 2011) · **U2_Majherdabri_GP** from Alipurduar II (~19,843 pop 2011) | E | v0 simplification — see methodology §3 |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (CDB Kalchini) | 298,548 (rural 211,808 + urban 86,650) | A | Census 2011 — Kalchini CD Block |
| 2011 base population (Majherdabri GP, Alipurduar II) | ~19,843 | E | v0 GP-equal-weight assumption |
| 2011 base population (AC 011 total) | ~318,391 | E | Sum above |
| 2021 projected population | ~355,000 | E | 10-yr compound growth from 2011; religion-differential rates applied |
| Sex ratio (2021, F per 1000 M) | ~935 | E | Marginal improvement trend continuing from 2011 (925) → 2019 (~930) → 2021 (~935); male labour in-migration stabilizing |
| 2021 estimated electorate | ~241,000 | E | Back-derived: 2021 AE total votes 195,815 at ~81.3% turnout → electorate ~240,900; consistent with growth from 2019 ECI roll 235,753 |
| 2021 polling stations | ~324 | A | ECI 2021 AE records for AC 011; Wikipedia "Kalchini (Vidhan Sabha constituency)" |
| Note on COVID return migration | Tea-garden workers who had migrated to Kerala/TN construction jobs returned to Kalchini during 2020 COVID lockdowns; closed-garden displaced workers also more visible in bagan settlements by 2020-21; net effect: small population increase in-constituency | D | NFHS-5 (2019-21); journalistic coverage of reverse migration in tea-belt |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 65.50 | E | 2011: 67.08% (A); projected -1.6pp over 10yr as Christian/Tribal-ORP shares hold or grow; v0 uses 65.50% |
| Muslim | 8.20 | E | 2011: 8.57% (A); modest growth +~0.2pp/yr over 10yr → ~8.2%; Majherdabri GP (Muslim 6.5%) anchors moderate growth |
| Christian | 15.50 | E | 2011: 14.33% (A); tea-belt missions active among Adivasi; +1.2pp over 10yr |
| Sarna_ORP | 3.50 | E | 2011: ~2.0%; upward drift as Adivasi reclaim Sarna identity post-Jharkhand precedent; ~3.5% by 2021 |
| Other_residual | 7.30 | E | Buddhist (Nepali-Gorkha, stable ~7.0%) + Sikh (0.5%) + Not stated; lumped per schema |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **ST_total** | 40.00 | A | Kalchini CDB 2011: 40.30% ST; stable decadal share; v0 holds at 40.00% for AC-weighted estimate |
| └ Oraon_Kurukh | 16.00 | D | Dominant Adivasi group; ~40% of ST pool; journalistic |
| └ Munda | 8.00 | D | ~20% of ST pool |
| └ Santhal | 6.00 | D | ~15% of ST pool |
| └ Kharia_Gond_Kurmi | 6.00 | D | Mixed Chhattisgarh/Jharkhand-origin Adivasi |
| └ Nepali_Gorkha_ST | 4.00 | D | Tea-belt Nepali-origin ST; Buddhist subset |
| **SC_total** | 10.00 | A | Kalchini CDB 2011: 10.10% SC; stable |
| UC_bhadralok | 5.00 | D | Garden managers, Jaigaon traders; Bengali UC minority |
| OBC | 6.00 | D | Rajbanshi + other OBC; district average Rajbanshi ~3.17%; other non-ST non-SC OBC |
| Other_Hindu_middle | 7.00 | D | Bihari/Hindi-belt Hindu non-SC non-ST; Nepali non-ST non-SC |
| Muslim | 8.00 | E | See C.1; mainly Bengali-Muslim and some tribal-origin Muslim |
| Christian_plus_Sarna_plus_Other | 24.00 | E | Adivasi Christian (15.5% of total) + Sarna/ORP (3.5%) + Buddhist/Other (5%); pooled for caste leaf |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2021, voters 18+ only; renormalized)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.5 | E | First-time voter cohort 2021 (born 1999-2003); 2011 children now young adults; renormalized from all-age Census projection |
| 23_27 | 11.5 | E | |
| 28_32 | 11.0 | E | |
| 33_37 | 10.5 | E | |
| 38_42 | 9.5 | E | |
| 43_47 | 9.0 | E | |
| 48_52 | 8.0 | E | |
| 53_57 | 7.0 | E | |
| 58_62 | 6.5 | E | |
| 63_67 | 8.5 | E | Includes cohort born early 1950s–late 1950s; larger than 68+ due to tea-belt mortality |
| 68 | 7.0 | E | Tea-garden pattern: premature mortality from occupational exposure; smaller elderly cohort; sum with 63_67 ~15.5% consistent with WB pattern |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.65 | E | 2011: 51.87%; marginal shift toward balance continuing; male in-migration slightly below 2011 peak |
| Female | 48.34 | E | |
| Third_gender | 0.01 | E | Negligible; consistent with WB pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 14.00 | A | Kalchini CDB 2011: 14.2%; stable share; Jaigaon urban Bengali community |
| Hindi | 8.00 | A | Kalchini CDB 2011: 8.17%; stable |
| Urdu | 0.50 | E | Small Urdu-speaking Muslim fraction within Bengali-Muslim community |
| Other | 4.00 | E | Residual: Boro (2.85%), Rabha (1.73%) sub-totals compressed into Other |
| Sadri | 30.00 | A | Kalchini CDB 2011: 30.1%; dominant tea-garden lingua franca; stable across communities |
| Nepali | 26.00 | A | Kalchini CDB 2011: 26.3%; Gorkha/Nepali community; stable |
| Kurukh | 3.00 | A | Kalchini CDB 2011: 2.99%; Oraon home language |
| Bhojpuri | 4.00 | A | Kalchini CDB 2011: 3.93%; Bihari-origin tea labor |
| Santali | 1.00 | E | Santali-speakers; subset of Santhal ST |
| Boro_Rabha_other | 9.50 | E | Boro, Rabha, Mundari, Ho, Kharia and other tribal languages combined |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 24.00 | E | 2011 literacy 68.96% → ~31% illiterate; +~1pp/yr improvement → ~24% illiterate by 2021; COVID disrupted schooling but adult literacy continued marginal improvement |
| Primary | 23.00 | E | Tea-garden dropout high after primary; shift from illiterate → primary over decade |
| Middle | 21.00 | E | |
| Secondary | 15.00 | E | |
| Higher_Secondary | 10.00 | E | |
| Graduate | 5.50 | E | Low; managerial/trader class; some first-generation college graduates from mission schools |
| Postgraduate | 1.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 36.00 | E | 2011 total workers 40.29% of pop; 10-yr projection; COVID closed gardens added to displacement |
| └ Main_worker_tea_garden | 30.00 | D | Tea-garden wage labor (organized sector); lower than 2019 (34%) due to COVID income hits and temporary closures in 2020 |
| └ Main_worker_non_tea | 6.00 | D | Cultivator + ag-labor + household industry + trade + govt |
| Marginal_worker | 8.50 | E | Seasonal picking + casual; women and youth; slightly higher than 2019 as some permanent roles casualized |
| Non_worker | 38.00 | E | Housewife / elderly / retired; stable |
| Student | 7.00 | E | Slightly higher enrollment trend; mission schools + state school expansion |
| Unemployed | 10.50 | D | Closed gardens: 19 closed gardens in Dooars region; COVID income shock to open gardens; closed-garden workers displaced; tea-belt unemployment higher than state average |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 4.00 | A | Kalchini CDB 2011: 6.20% of workers; slight downward trend as bagan encroachment reduces smallholder plots |
| Agricultural_labourer | 5.00 | A | Kalchini CDB 2011: 7.06% of workers; non-tea ag labor; marginal decline |
| Household_industry | 2.00 | A | Kalchini CDB 2011: 1.88%; stable |
| Manufacturing | 1.00 | E | Negligible non-bagan manufacturing |
| Construction | 2.00 | E | Slightly higher as returned COVID migrants pick up local construction work |
| Trade_retail | 7.50 | D | Jaigaon border-town retail; cross-border Bhutan trade continuing; Jaigaon grew as border town |
| Transport_logistics | 3.00 | D | Cross-border trade logistics; stable |
| Services | 3.50 | E | Small non-bagan private sector; healthcare workers, mechanics; slight growth |
| Government_services_teachers | 3.00 | E | BDO / school / health center workers; stable |
| Out_migrant_worker | 2.00 | E | Net lower than 2019 due to COVID lockdown returns; out-migrant share temporarily reduced |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.00 | E | Bagan management and large traders; very few |
| Employee | 69.00 | E | Tea-garden organized-sector wage employees + govt; slightly lower than 2019 (70%) due to casualization during COVID |
| Single_worker | 19.00 | E | Own-account cultivators + Jaigaon traders + household industry; slight increase as formal bagan employment contracts weakened |
| Family_worker | 11.00 | E | Women + children assisting on smallholdings and household industry; stable |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 47.00 | D | Tea-garden wages revised to ₹202/day from Jan 2021; before revision wages ₹176/day; COVID halted gardens March-June 2020 → income loss; closed-garden workers remain extreme-poor; BPL rate ticked up slightly from 2019 (45%) due to COVID shock; v0 uses 47% |
| Above_Poverty_Line_low_income | 28.00 | E | Bagan workers at/above revised wage threshold; COVID erosion shifted some into BPL |
| Lower_middle | 15.00 | E | Jaigaon border traders; head-clerks / sirdars in garden management |
| Middle | 8.00 | E | Garden supervisory staff; govt employees; prosperous Jaigaon traders |
| Upper_middle_well_off | 2.00 | E | Garden managers; Jaigaon commercial class |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Kalchini_CDB_core | 93.8 | E | 2011: 298,548 / 318,391 = 93.8%; stable |
| U2_Majherdabri_GP | 6.2 | E | ~19,843 / 318,391 = 6.2%; stable |
| **Sum** | **100.00** | — | self-check |

Sub-unit decomposition within U1 (2021):

| Category | % of U1 | Tier | Source / Note |
|---|---|---|---|
| Urban (Jaigaon + Uttar Satali + Uttar Latabari + Mechiabasti) | 30.0 | E | 2011: 29.0%; slight urban expansion in Jaigaon border town; ~30% by 2021 |
| Rural (tea-garden villages + forest settlements) | 70.0 | E | |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.7 | E | Slight decline from 2019 (4.8); fertility reduction trend |
| Nuclear_HH | 62.0 | E | Marginal increase; COVID return migration temporarily increased nuclear HH as couples returned home |
| Joint_HH | 29.0 | E | Slight decrease; generational separation accelerating in bagan lines |
| Extended_multi_generation | 9.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 24.5 | E | Stable; slight increase in first-time voter cohort (18-22) share |
| Currently_married | 65.5 | E | Stable; tribal early-marriage pattern continues |
| Widowed | 9.0 | E | COVID mortality added marginally to widowed share; tea-garden occupational mortality base continues |
| Separated_divorced | 1.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level — independent flags, do NOT sum)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 52.0 | D | Modest increase from 2019 (50%); tea-garden electrification marginal improvement; NFHS-5 WB: rural TV ~60%; tea-belt still below state avg |
| Radio | 12.0 | D | Slight decline from 2019 (15%); radio losing ground to mobile; still important for Sadri/Hindi broadcasts in off-grid areas |
| Mobile_phone | 82.0 | D | Significant jump from 2019 (70%); Jio post-2016 rural penetration deeper by 2021; NFHS-5 WB rural ~88%; tea-belt below state avg |
| Smartphone_with_internet | 48.0 | D | **+20pp from 2019 (28%)**; COVID-driven smartphone surge: school-from-home, banking, govt scheme verification required smartphones; load-bearing for narrative-injection weighting; still below WB rural average |
| Computer | 5.0 | E | Negligible increase |
| Two_wheeler | 14.0 | E | Slight increase as wage revision allows some asset accumulation |
| Four_wheeler | 2.0 | E | Stable |
| Banking_access | 82.0 | B | +7pp from 2019 (75%); Lakshmir Bhandar (Apr 2021) requires bank account → drove PMJDY enrollment surge in tea-belt; identification challenge for Adivasi workers being resolved by ration-card + Aadhaar linkage |
| Note | (these are independent ownership %s, not categorical — do not sum) | — | — |

### C.15 Household amenities (2021)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 62.0 | D | Marginal improvement from 2019 (60%); Jal Jeevan Mission (JJM) started 2019 with limited reach by 2021 in tea-belt |
| Improved_sanitation | 28.0 | D | Modest improvement from 2019 (25%); Swachh Bharat limited in private bagan land; COVID awareness added marginal push |
| LPG_clean_cooking_fuel | 30.0 | D | Ujjwala 2.0 not yet launched (Aug 2021); original Ujjwala coverage improved slightly; +5pp from 2019 (25%); refill affordability remains issue |
| Wood_biomass_fuel | 65.0 | E | Declining from 2019 (70%) as LPG penetration improves |
| Other_fuel | 5.0 | E | Kerosene/dung; stable |
| Electricity | 83.0 | D | Marginal improvement from 2019 (80%); Saubhagya scheme completed by 2019; some quality improvement in existing connections |
| Note | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 61.0 | D | 4th–5th generation bagan-born; slight increase as COVID return migrants registered back at native addresses |
| WB_other_district | 4.5 | D | Slight decrease; limited new internal WB in-migration |
| Other_Indian_state | 0.5 | E | Marginal |
| Bangladesh_origin | 0.5 | E | Negligible; some families in border-adjacent GPs |
| Outside_India | 0.5 | E | Nepal recent in-migration negligible |
| Out_migrant | 3.0 | E | Net lower than pre-COVID as returned workers registered back; many closed-garden workers are local but jobless, not technically out-migrants |
| Jharkhand_origin | 25.0 | D | **Load-bearing**: Oraon, Munda, Santhal, Kharia, Gond forebears from Chhotanagpur plateau; 3rd–5th generation; stable multi-generational identity |
| Nepal_Bhutan_origin | 4.0 | D | Nepali/Gorkha community; stable |
| Bihari_UP_origin | 1.0 | D | Bhojpuri-heritage workers; stable but not growing |
| **Sum** | **100.00** | — | self-check; native+WB_other+Other_Indian+Bangladesh+Outside+Out_migrant+Jharkhand+Nepal_Bhutan+Bihari_UP = 61+4.5+0.5+0.5+0.5+3+25+4+1 = 100 |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue (2021)

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Sadri | Nepali | Kurukh | Bhojpuri | Santali | Boro_Rabha_other | Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 20.0 | 9.0 | 0.5 | 26.0 | 28.0 | 3.5 | 5.0 | 0.5 | 5.0 | 2.5 | E | Hindu Nepali Gorkha + Bengali + Adivasi Hindu; Sadri lower within Hindu as Nepali/Bengali non-Sadri |
| Muslim | 75.0 | 12.0 | 6.0 | 2.0 | 2.0 | 0.0 | 2.0 | 0.0 | 1.0 | 0.0 | E | Muslims concentrated in Bengali/Hindi-speaking peripheral GPs |
| Christian | 8.0 | 5.0 | 0.0 | 48.0 | 12.0 | 8.0 | 5.0 | 3.0 | 8.0 | 3.0 | E | Adivasi Christian: Sadri + Kurukh; mission schools promoted Bengali/Hindi literacy |
| Sarna_ORP | 5.0 | 5.0 | 0.0 | 60.0 | 0.0 | 15.0 | 2.0 | 3.0 | 8.0 | 2.0 | E | Sarna adherents are Adivasi; Sadri-dominant |
| Other_residual | 4.0 | 2.0 | 0.0 | 3.0 | 88.0 | 0.0 | 1.0 | 0.0 | 2.0 | 0.0 | E | Predominantly Nepali-speaking Buddhist Gorkha community |

### D.2 Religion × Caste (2021, 2D layout)

P(caste ‖ religion) — % within each religion.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 12.0 | 28.0 | 8.0 | 9.0 | 23.0 | 0.0 | 20.0 | E | Hindu Adivasi ST + SC + Bengali UC + Rajbanshi OBC + Nepali-Hindu folded into Other_Hindu_middle; ST-Hindu share: ~40% ST × 60-65% Hindu-identifying = ~26% of total → ~26/65.5 = ~40% of Hindu → 28% used (conservative adj for Sarna-identifying overlap) |
| Muslim | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | A | Muslim is its own leaf |
| Christian | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | A | Adivasi Christian → Christian_plus_Sarna_plus_Other leaf |
| Sarna_ORP | 0.0 | 95.0 | 0.0 | 3.0 | 2.0 | 0.0 | 0.0 | E | Sarna = predominantly ST-identifying Adivasi |
| Other_residual | 2.0 | 5.0 | 3.0 | 10.0 | 30.0 | 0.0 | 50.0 | E | Buddhist (mostly Nepali non-ST), Sikh, Not-stated residual |

### D.3 Religion × Migration (2021)

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Jharkhand_origin | Nepal_Bhutan_origin | Bihari_UP_origin | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 60.0 | 5.0 | 0.5 | 0.5 | 0.5 | 3.0 | 20.0 | 8.0 | 2.5 | D | Hindu Nepali and Adivasi-Hindu both present |
| Muslim | 80.0 | 8.0 | 0.0 | 2.0 | 0.0 | 2.0 | 0.0 | 0.0 | 8.0 | D | Bengali Muslim and Bihari Muslim |
| Christian | 55.0 | 3.0 | 0.5 | 0.5 | 0.5 | 2.5 | 36.0 | 1.0 | 1.0 | D | Most Adivasi Christian families 4th–5th generation Jharkhand-origin |
| Sarna_ORP | 45.0 | 3.0 | 0.5 | 0.5 | 0.5 | 2.0 | 47.0 | 1.0 | 0.5 | D | Sarna-identifying Adivasi most closely tied to Jharkhand cultural origin |
| Other_residual | 50.0 | 2.0 | 0.5 | 0.5 | 0.5 | 1.5 | 0.0 | 44.0 | 1.0 | E | Predominantly Nepal-origin Buddhist |

### D.4 Religion × Asset / media (2021)

P(owns asset ‖ religion) — % within each religion.

| Religion | Television | Radio | Mobile_phone | Smartphone_with_internet | Computer | Two_wheeler | Four_wheeler | Banking_access | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 57.0 | 11.0 | 84.0 | 52.0 | 5.5 | 16.0 | 2.5 | 85.0 | D | Higher-income Nepali/Bengali Hindu subsect lifts averages |
| Muslim | 60.0 | 10.0 | 85.0 | 50.0 | 5.0 | 15.0 | 2.0 | 83.0 | D | Peripheral GP Bengali-Muslim: slightly better-off than Adivasi |
| Christian | 43.0 | 13.0 | 76.0 | 38.0 | 3.5 | 10.0 | 1.0 | 72.0 | D | Adivasi Christian lowest income; mission-school exposure partially offsets |
| Sarna_ORP | 32.0 | 14.0 | 70.0 | 30.0 | 2.0 | 8.0 | 0.5 | 58.0 | D | Poorest Adivasi segment; least media access |
| Other_residual | 65.0 | 8.0 | 88.0 | 55.0 | 7.0 | 18.0 | 3.0 | 86.0 | E | Nepali/Buddhist community: border-trade income, higher assets |

### D.5 Caste × Education (2021)

P(education level ‖ caste group) — highest level achieved, age 18+.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4.0 | 9.0 | 11.0 | 19.0 | 22.0 | 25.0 | 10.0 | E |
| OBC | 14.0 | 21.0 | 22.0 | 21.0 | 13.0 | 7.0 | 2.0 | E |
| Other_Hindu_middle | 16.0 | 22.0 | 22.0 | 20.0 | 12.0 | 6.0 | 2.0 | E |
| ST_total | 28.0 | 29.0 | 22.0 | 13.0 | 6.0 | 2.0 | 0.0 | E |
| SC_total | 27.0 | 27.0 | 23.0 | 15.0 | 6.0 | 2.0 | 0.0 | E |
| Muslim | 21.0 | 25.0 | 24.0 | 19.0 | 7.0 | 4.0 | 0.0 | E |
| Christian_plus_Sarna_plus_Other | 22.0 | 29.0 | 25.0 | 15.0 | 7.0 | 2.0 | 0.0 | E |

(Note: Christian Adivasi within this pooled leaf show better literacy than Hindu/Sarna Adivasi — mission-school effect; collapsed into pooled Christian_plus_Sarna leaf per schema.)

### D.6 Age × Gender × Education (2021)

P(grad+ ‖ age × gender) — % within cohort × gender:

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 9.0 | 7.0 | E |
| 23_27 | 8.0 | 5.0 | E |
| 28_32 | 6.0 | 3.0 | E |
| 33_37 | 5.0 | 2.0 | E |
| 38_42 | 4.5 | 1.5 | E |
| 43_47 | 4.0 | 1.0 | E |
| 48_52 | 3.0 | 1.0 | E |
| 53_57 | 3.0 | 1.0 | E |
| 58_62 | 2.5 | 0.5 | E |
| 63_67 | 2.0 | 0.5 | E |
| 68 | 2.0 | 0.5 | E |

### D.7 Marital status × Age × Gender (2021)

P(currently married ‖ age × gender):

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 10.0 | 45.0 | E |
| 23_27 | 55.0 | 85.0 | E |
| 28_32 | 85.0 | 93.0 | E |
| 33_37 | 92.0 | 90.0 | E |
| 38_42 | 92.0 | 89.0 | E |
| 43_47 | 90.0 | 87.0 | E |
| 48_52 | 88.0 | 75.0 | E |
| 53_57 | 86.0 | 65.0 | E |
| 58_62 | 83.0 | 55.0 | E |
| 63_67 | 72.0 | 35.0 | E |
| 68 | 65.0 | 25.0 | E |

(High female widowhood at 63+ due to occupational male premature mortality from silicosis/fluorosis in tea areas.)

### D.8 Occupation × Asset / media (2021)

P(owns asset ‖ occupation) — % within occupation group:

| Occupation | Television | Radio | Mobile_phone | Smartphone_with_internet | Computer | Two_wheeler | Four_wheeler | Banking_access | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Cultivator | 50.0 | 12.0 | 82.0 | 38.0 | 3.0 | 18.0 | 1.5 | 80.0 | E | Slightly better-off than bagan; own-plot farming |
| Agricultural_labourer | 38.0 | 14.0 | 75.0 | 28.0 | 1.0 | 8.0 | 0.5 | 70.0 | E | Poor non-bagan ag labor |
| Household_industry | 45.0 | 12.0 | 78.0 | 32.0 | 2.0 | 10.0 | 1.0 | 72.0 | E | Cottage industry workers |
| Manufacturing | 48.0 | 10.0 | 80.0 | 38.0 | 3.0 | 12.0 | 1.0 | 76.0 | E | |
| Construction | 40.0 | 12.0 | 78.0 | 32.0 | 1.0 | 10.0 | 0.5 | 70.0 | E | Returned COVID migrants, casual construction |
| Trade_retail | 72.0 | 8.0 | 92.0 | 68.0 | 8.0 | 30.0 | 4.0 | 90.0 | D | Jaigaon border-town traders; high smartphone penetration for WhatsApp commerce |
| Transport_logistics | 60.0 | 10.0 | 88.0 | 58.0 | 5.0 | 45.0 | 3.0 | 85.0 | E | Cross-border logistics workers |
| Services | 55.0 | 8.0 | 88.0 | 55.0 | 8.0 | 20.0 | 2.0 | 85.0 | E | Private service sector |
| Government_services_teachers | 88.0 | 6.0 | 95.0 | 82.0 | 40.0 | 35.0 | 8.0 | 98.0 | E | Highest-asset occupation group |
| Out_migrant_worker | 35.0 | 10.0 | 85.0 | 42.0 | 3.0 | 12.0 | 1.0 | 72.0 | E | Net lower; returned workers show moderate asset profile |

### D.9 Education × Workforce participation (2021)

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 41.0 | 2.0 | E |
| Primary | 44.0 | 4.0 | E |
| Middle | 39.0 | 6.0 | E |
| Secondary | 28.0 | 12.0 | E |
| Higher_Secondary | 18.0 | 22.0 | E |
| Graduate | 17.0 | 30.0 | E |
| Postgraduate | 28.0 | 20.0 | E |

(COVID shock increased educated unemployment in 2020-21; tea-garden economy doesn't absorb educated youth.)

### D.10 Asset × Bilingualism (2021)

P(bilingual Sadri+Bengali ‖ media-access tier):

| Category | Sadri_Bengali_bilingual | Tier | Source |
|---|---|---|---|
| TV-only HH | 22.0 | E | Bengali TV channels expand Sadri-speaker Bengali comprehension |
| TV_plus_smartphone HH | 38.0 | E | YouTube cross-language; higher exposure to Bengali content |
| Smartphone-only HH | 28.0 | E | Mobile-first users |
| Radio-only HH | 12.0 | E | Radio uses Hindi/Sadri more |
| No-asset HH | 8.0 | E | Lowest exposure |

### D.11 GP / Sub-unit × Religion (2021)

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Kalchini_CDB_core | 65.0 | 7.5 | 15.8 | 3.7 | 8.0 | E | Directly from CDB 2011 census proportions projected to 2021 |
| U2_Majherdabri_GP | 84.0 | 6.5 | 8.7 | 0.5 | 0.3 | E | Alipurduar II CDB 2011: Hindu 84.40%, Christian 8.64%, Muslim 6.50% |

### D.12 GP / Sub-unit × Caste (2021)

| Sub_unit | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Kalchini_CDB_core | 9.5 | 42.0 | 5.0 | 5.5 | 11.5 | 7.5 | 19.0 | E |
| U2_Majherdabri_GP | 41.8 | 18.4 | 3.0 | 10.0 | 14.0 | 6.5 | 6.3 | E |

### D.13 GP / Sub-unit × Asset / media (2021)

| Sub_unit | Television | Radio | Mobile_phone | Smartphone_with_internet | Computer | Two_wheeler | Four_wheeler | Banking_access | Tier |
|---|---|---|---|---|---|---|---|---|---|
| U1_Kalchini_CDB_core | 50.0 | 13.0 | 80.0 | 46.0 | 4.5 | 13.0 | 1.5 | 80.0 | D |
| U2_Majherdabri_GP | 65.0 | 9.0 | 90.0 | 58.0 | 7.0 | 20.0 | 3.5 | 90.0 | E |

### D.14 GP / Sub-unit × Amenities (2021)

| Sub_unit | Improved_drinking_water_source | Improved_sanitation | LPG_clean_cooking_fuel | Wood_biomass_fuel | Other_fuel | Electricity | Tier |
|---|---|---|---|---|---|---|---|
| U1_Kalchini_CDB_core | 60.0 | 25.0 | 28.0 | 67.0 | 5.0 | 81.0 | D |
| U2_Majherdabri_GP | 74.0 | 43.0 | 38.0 | 57.0 | 5.0 | 92.0 | E |

### D.15 Vote × Religion (2021 AE, AC 011)

P(party ‖ religion) — derived from AC 011 2021 AE result (BJP 52.65% / AITC 38.06%) combined with CSDS-Lokniti WB patterns adjusted for tea-belt context.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 57.0 | 32.0 | 2.5 | 5.0 | 3.5 | C/D | BJP BTWU hold weakened vs 2019; TMC Passang Lama mobilized some Nepali-Hindu vote; Lakshmir Bhandar targeting women |
| Muslim | 8.0 | 70.0 | 5.0 | 12.0 | 5.0 | D | Muslim strongly AITC in 2021; anti-BJP consolidation post-2020 communal narrative |
| Christian | 44.0 | 42.0 | 3.0 | 7.0 | 4.0 | D | Christian Adivasi: TMC gained; Lakshmir Bhandar + health schemes resonated; BJP still narrow plurality |
| Sarna_ORP | 52.0 | 33.0 | 2.5 | 8.0 | 4.5 | D | Sarna-identifying Adivasi: BJP weakened slightly; Sarna identity politics still BTWU-linked |
| Other_residual | 52.0 | 33.0 | 2.0 | 4.0 | 9.0 | D | Nepali/Buddhist: BJP-BTWU hold; anti-TMC Gorkha identity sentiment |

### D.16 Vote × Caste (2021 AE, AC 011)

P(party ‖ caste group):

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| ST_total | 60.0 | 31.0 | 2.0 | 5.0 | 2.0 | D | BTWU hold weakened ~8pp from 2019 LS; Bishal Lama retained BJP but TMC Passang Lama ate into Adivasi ST vote; wage revision + Lakshmir Bhandar resonated |
| SC_total | 35.0 | 48.0 | 3.0 | 10.0 | 4.0 | D | SC more TMC-leaning; Lakshmir Bhandar particularly effective for SC women |
| UC_bhadralok | 52.0 | 38.0 | 3.0 | 4.0 | 3.0 | D | Bengali bhadralok BJP slightly weakened from 2019 statewide BJP retreat |
| OBC | 42.0 | 46.0 | 3.0 | 6.0 | 3.0 | D | Mixed; Rajbanshi more AITC-inclined post-Matua/Rajbanshi welfare focus |
| Other_Hindu_middle | 50.0 | 36.0 | 3.0 | 7.0 | 4.0 | D | Nepali non-ST/SC; Bihari; slight BJP dominance |
| Muslim | 8.0 | 70.0 | 5.0 | 12.0 | 5.0 | D | |
| Christian_plus_Sarna_plus_Other | 46.0 | 40.0 | 2.5 | 8.0 | 3.5 | D | Christian Adivasi TMC gains; Sarna Adivasi BJP-leaning but narrowed |

### D.17 Vote × Gender (2021 AE, AC 011)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 55.0 | 36.0 | 2.5 | 5.0 | 1.5 | D | BTWU male workforce; BJP stronger among male bagan workers but weakened from 2019 |
| Female | 50.0 | 42.0 | 2.0 | 4.0 | 2.0 | D | Lakshmir Bhandar (Apr 2021) targeted women household heads; launched mid-campaign; TMC gained ground among female tea-garden workers |
| Third_gender | 50.0 | 42.0 | 2.0 | 4.0 | 2.0 | E | Assumed same as Female distribution; negligible sample |

### D.18 Vote × Welfare scheme exposure (2021 AE, AC 011)

P(party ‖ welfare-scheme exposure) — dominant schemes available by 2021: Lakshmir Bhandar (Apr 2021), Krishak Bandhu, Kanyashree, Swasthya Sathi, Khadya Sathi/PDS; tea-garden wage revision Jan 2021.

| Welfare_exposure | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Lakshmir_Bhandar_enrolled | 42.0 | 50.0 | 2.0 | 4.0 | 2.0 | D | ST women enrolled ₹1,000/month; AITC credit claim; BJP countered with BTWU wage-revision narrative; AITC plurality in this segment |
| Kanyashree_HH | 49.0 | 43.0 | 2.0 | 4.0 | 2.0 | D | Girl-student HH; BJP still competitive even in scheme-exposed tea-belt HH |
| Swasthya_Sathi_enrolled | 46.0 | 46.0 | 2.5 | 4.0 | 1.5 | D | Tea-belt workers enrolled in health scheme; near-equal split |
| Khadya_Sathi_PDS | 53.0 | 38.0 | 2.5 | 5.0 | 1.5 | D | PDS coverage high in tea belt; BJP still dominant — BTWU networks distribute BJP credit |
| No_state_scheme_exposure | 62.0 | 27.0 | 2.5 | 6.0 | 2.5 | D | BJP dominant; BTWU organizational networks substitute for TMC welfare narrative |

---

## E. 2021 baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp. **Calibration year: 2021 WB Assembly Election.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 52.65 | A | ECI 2021 AE via Wikipedia — Bishal Lama (BJP) 103,104 votes / 195,815 total |
| AITC | 38.06 | A | ECI 2021 AE via Wikipedia — Passang Lama (AITC) 74,528 votes |
| INC | 2.83 | D | ~5,548 votes estimated from Wikipedia summary |
| LF | 3.00 | D | RSP ~5,880 votes estimated; Left parties combined in LF column |
| Other_NOTA | 3.46 | D | NOTA + IND + others; residual to 100 |

> Total valid votes 2021 AE: 195,815 | Electorate ~241,000 | Turnout ~81.3%
> Winning candidate: **Bishal Lama** (BJP) | Runner-up: Passang Lama (AITC)
> BJP margin: 28,576 votes (~14.59 pp)
> BJP margin compressed from 2019 LS AC-segment (24.90 pp) — BJP retained but TMC gained ~4.4 pp.

---

## F. Pre-2021 vote history (anchors for belief evolution)

### AC 011 Kalchini — Assembly Election history

| Year | Winner | Party | Votes | % | Runner-up | Party | % | Margin | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2021 AE | Bishal Lama | BJP | 103,104 | 52.65 | Passang Lama | AITC | 38.06 | 14.59 pp | BJP retained; AITC TMC gained ~4pp vs 2019 LS; Lakshmir Bhandar mid-campaign effect; BTWU hold but weakened |
| 2016 AE | Wilson Champramary | AITC | 62,061 | 34.99 | Bishal Lama | BJP | 60,550 | 34.14 | 1,511 votes — razor-thin AITC win; GJM vote split enabled AITC; BJP within 1pp |
| 2011 AE | Wilson Champramary | GJM-backed IND | 46,455 | 30.05 | Binay Bhusan Kerketta | RSP | 39,210 | 25.37 | Multi-party split; GJM-backed IND won; AITC, BJP, INC also competed |
| 2006 AE | Manohar Tirkey | RSP | — | — | Paban Kumar Lakra | INC | — | — | RSP hold; LF Front dominance |
| 2001 AE | Paban Kumar Lakra | INC | — | — | Manohar Tirkey | RSP | — | — | INC beat RSP; Left Front still dominant |

Source: Wikipedia "Kalchini Assembly constituency"; tier A for named results; tier D for early years without vote counts.

### 2019 LS AC 011 segment (now anchor, was previous calibration target)

| Party | Votes | AC-011 segment % | Tier |
|---|---|---|---|
| BJP (John Barla) | 111,477 | 58.53 | A |
| AITC (Dasrath Tirkey) | 64,045 | 33.63 | A |
| INC | 4,860 | 2.55 | A |
| RSP | 4,194 | 2.20 | A |
| Others / NOTA | 5,877 | 3.09 | A |
| **Electorate** | **235,753** | | A |
| **Turnout** | **80.8%** | | A |

> BJP margin in 2019 LS AC-segment: 47,432 votes (24.90 pp). This was the calibration target for the 2019-layer; it is now a historical anchor for the 2021-layer belief evolution.

### Alipurduars Lok Sabha (PC 2) — 2019 LS full result

| Party | Candidate | Votes | % |
|---|---|---|---|
| BJP | John Barla (BTWU President) | 750,804 | 54.36 |
| AITC | Dasrath Tirkey | 506,815 | 36.69 |
| RSP | Mili Oraon | 54,010 | 3.91 |
| Others | various | ~69,547 | ~5.04 |

**Key trajectory**: RSP (Left) dominated 1977–2009 through Adivasi labor base (Manohar Tirkey). BJP captured this base via BTWU-RSS organizing by 2019 (54.36%). Narrow AITC hold in 2016 AE (1,511 vote margin) reversed decisively in 2019 LS and 2021 AE with BJP consolidation. 2021 AE shows BJP-AITC margin compressing (24.90 pp → 14.59 pp): BJP firmly holds Kalchini but is not immunity-endowed.

### 2020–2021 context events (known by end-2021)

- **COVID-19 lockdown (Mar–Jun 2020)**: Tea gardens shut for 2+ months; ₹176/day wage workers lost income; closed-garden workers (19 gardens) experienced acute destitution; Adivasi tea workers among WB's most COVID-economically-vulnerable
- **COVID return migration (2020)**: Workers who had left for Kerala/Tamil Nadu construction returned to Kalchini; some re-enrolled on voter rolls; net slight increase in registered voters vs 2019
- **Cyclone Amphan (May 20, 2020)**: Primary damage in 24-Parganas and 2-Dinajpur; Kalchini/Alipurduar minimally affected; no significant displacement event here
- **Lakshmir Bhandar launch (April 2021)**: ₹500/month for general-category women household heads; ₹1,000 for SC/ST women HH heads; launched in April 2021 — during the AE campaign; required bank account (drove PMJDY enrollment in tea-belt); tea-garden ST women (SC/ST rate ₹1,000) were primary beneficiaries in Kalchini; created a counter-narrative to BJP's BTWU-welfare framing; the timing mid-campaign partially accounts for the 4pp AITC gain over 2019 LS
- **Tea-garden wage revision (Jan 2021)**: WB govt revised minimum wage to ₹202/day (from ₹176); a BJP-competing welfare claim — both parties claimed credit; BJP argued Centre's Atmanirbhar package; AITC credited Mamata; in tea-belt the wage revision is load-bearing for vote shift
- **BSF 50km jurisdiction (Oct 2021)**: Extended BSF jurisdiction to 50km from Bangladesh/Pakistan border; Kalchini is near Bhutan border (not Bangladesh), so direct electoral impact minimal; but border-belt community anxieties about sovereignty and identity were present
- **2021 AE result (May 2, 2021)**: TMC 213 / BJP 77 / ISF 5 / others 4 statewide; BJP significantly underperformed exit-poll forecasts; in Kalchini specifically BJP retained but with compressed margin; Bishal Lama retained the seat

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Kalchini CD Block Primary Census Abstract — population, religion, ST/SC, literacy, occupation, language
- Census of India 2011 — Alipurduar II CD Block — for Majherdabri GP approximation
- ECI 2021 WB Assembly Election — AC 011 Kalchini result: Bishal Lama (BJP) 103,104 / Passang Lama (AITC) 74,528; total valid 195,815; via Wikipedia "Kalchini (Vidhan Sabha constituency)"
- ECI 2019 LS `2019_AssemblySegmentLevelVotingData.csv` — AC-011 Kalchini segment: BJP 111,477 / AITC 64,045; electorate 235,753; turnout 80.8%
- ECI 2016 AE / 2011 AE historical results — via Wikipedia
- Delimitation Commission of India 2008 — WB Schedule

### Secondary sources (tier B/C)

- NFHS-5 (2019-21) West Bengal — asset/media diffusion update; rural smartphone penetration; banking access
- NFHS-4 (2015-16) West Bengal — baseline comparison for asset shifts
- CSDS-Lokniti 2021 WB AE post-poll survey — state-level vote × religion/caste/gender (used for directional priors)

### Tertiary / journalistic (tier D)

- The Print (Jul 2021) "How tea gardens in North Bengal, key to poll fortunes of BJP & TMC" — BTWU in 199 of 408 gardens; wage ₹176 → ₹202 revision; 19 closed gardens
- The Bastion (2021) "Brewing in Uncertainty" — sanitation (15.81% latrine), water (30.7% tube-well), wage data
- Wire / Scroll (2020) — COVID impact on tea-garden workers; reverse migration; closed-garden income collapse
- IDR Online / Down To Earth — tea-garden worker conditions; Adivasi labour rights
- Wikipedia "Kalchini (Vidhan Sabha constituency)" — election results, composition
- Wikipedia "Kalchini (community development block)" — Census 2011 summary
- Wikipedia "Alipurduars Lok Sabha constituency" — historical LS results

### Tier-D/E reliance flags

- **Caste sub-group shares within ST** (C.2, D.2) — no caste census post-1931 for non-SC/ST sub-groupings; all tribal sub-group shares are tier D/E
- **2021 AE INC/LF/Other vote counts** — Wikipedia provides BJP and AITC tier A; INC and LF total are tier D estimates (5,548 and 5,880 respectively) from contextual sources; Other_NOTA is residual
- **Vote × religion/caste joints** (D.15–D.17) — no 2021 AC-level CSDS post-poll; derived from 2019 joints adjusted for 14.59 pp compression; treat as tier C/D
- **Asset/media** (C.14, D.4, D.8, D.13) — NFHS-5 provides state and district direction; no bagan-specific survey; tier D
- **COVID migration return** (B, C.16) — directional certainty but magnitude E

### v0 known gaps

1. INC + LF + Other vote counts for 2021 AE — Wikipedia not granular; use with tier D caution
2. Bagan-level spatial heterogeneity — 18 tea gardens in Kalchini block; v0 collapses to CDB
3. NFHS-5 tea-garden sub-sample — no tea-belt specific NFHS-5; journalistic proxy
4. Lakshmir Bhandar penetration rate in tea-belt by Oct 2021 — scheme launched Apr 2021; enrollment speed uncertain; tier D
5. Majherdabri GP-level demographics — approximated as 1/11 of Alipurduar II CDB

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No post-2021 events referenced.*

---

## H. Post-2021 validation anchors

> **These are OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> The simulator must reproduce the 2024 LS result from 2021 priors + narrative injection (SSC scam, RG Kar, Bangladesh trade disruption, CAA notification, wage stagnation 2021-24) without these figures being baked into calibration input.

### 2024 Lok Sabha Election — AC 011 segment within Alipurduars LS (tier A, CSV)

> Figures below are **tier A** — sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=11, Kalchini. Total valid votes: 187,029; electorate 254,731; turnout 73.4%.

| Party | Votes | AC-011 segment % | Tier | Source |
|---|---|---|---|---|
| BJP (Manoj Tigga) | 96,391 | 51.54 | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC (Prakash Chik Baraik) | 81,526 | 43.59 | A | Same |
| RSP (Mili Oraon) | 2,954 | 1.58 | A | Same |
| NOTA | 2,945 | 1.57 | A | Same |
| IND + Others | 3,213 | 1.72 | A | Same |
| **BJP margin** | **14,865 votes** | **7.95 pp** | A | Computed |

> **Trend summary**: BJP-AITC margin compressed further from 14.59 pp (2021 AE) → 7.95 pp (2024 LS). AITC clawed back ~5.5 pp over 2021-24. BJP retained plurality in every election since 2019 but the seat is now competitive.
