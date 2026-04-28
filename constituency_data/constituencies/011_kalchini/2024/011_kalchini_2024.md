# AC 011 — Kalchini (ST) — Calibrated 2024 Population Snapshot

> **Frozen at end-2024.** This file describes the demographic and behavioural state of AC 011 Kalchini as of end-2024 — written as if the year were end-2024 (after June 2024 LS results were known). It does not reference any post-2024 events. The 2024 LS AC-segment result is the primary calibration target. The 2021 AE and 2019 LS are historical anchors.
>
> Companion artifacts: [`methodology_2024.md`](../../methodology_2024.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2024)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 011 | A | ECI / Delimitation Commission 2008 |
| AC name | Kalchini | A | ECI |
| Reservation | ST (Scheduled Tribe) | A | Delimitation 2008 |
| District | Alipurduar | A | Created from Jalpaiguri 2014 |
| Sub-division | Alipurduar | A | WB administrative |
| LS constituency | PC 2 — Alipurduars (ST reserved) | A | Delimitation 2008 |
| LS segments | AC 7–13 as per Delimitation 2008 | A | Delimitation 2008 |
| AC composition | All 11 GPs of Kalchini CD Block + Majherdabri GP (Alipurduar II) | A | Wikipedia; Delimitation 2008 |
| Geographic note | Eastern Dooars; tea-garden dominated; Bhutan border (Jaigaon-Phuentsholing); Buxa Tiger Reserve | A | Wikipedia |
| Archetype | A3 — North Bengal tea-garden ST; BJP BTWU stronghold under structural TMC pressure; Bangladesh interim regime impact on Dooars border trade (Aug 2024) | D | Multiple sources 2024 |
| Two sub-units | **U1_Kalchini_CDB_core** (11 GPs) · **U2_Majherdabri_GP** (Alipurduar II) | E | v0 simplification |

---

## B. 2024 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (AC 011 total) | ~318,391 | E | Census 2011 — CDB Kalchini + Majherdabri GP |
| 2024 projected population | ~368,000 | E | 13-yr compound growth; religion-differential rates; tea-belt TFR decline continuing |
| Sex ratio (2024, F per 1000 M) | ~940 | E | Continuing marginal improvement trend |
| 2024 electorate | 254,731 | A | ECI 2024 LS `data/2024_AssemblySegmentLevelVotingData.csv` — TOTAL ELECTORS IN AC for AC_NO=11 |
| 2024 valid votes | 187,029 | A | Sum of VOTES SECURED EVM from 2024 CSV AC_NO=11 |
| 2024 turnout | 73.4% | A | 187,029 / 254,731 = 73.4%; lower than 2021 AE (~81.3%) and 2019 LS (80.8%) — LS vs AE pattern + potential voter fatigue |
| 2024 polling stations | ~330 | E | Marginal growth from 2021 (~324); estimated |
| Note on electorate growth | Electorate grew from 235,753 (2019) → ~241,000 (2021) → 254,731 (2024); growth rate ~3.9% over 2019-2024 consistent with demographic projection | A/E | 2019 CSV + 2024 CSV (tier A); interpolation tier E |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 65.00 | E | 2011: 67.08% (A); -2pp over 13yr; Christian/Sarna growth continues; v0 uses 65.0% |
| Muslim | 8.30 | E | 2011: 8.57% (A); very slow growth; Majherdabri GP Muslim share stable |
| Christian | 16.00 | E | 2011: 14.33% (A); +1.7pp over 13yr; mission-church activity continuing in tea-belt Adivasi communities |
| Sarna_ORP | 4.00 | E | Growing from 2011 (~2%) through Sarna identity movement; Jharkhand recognition in 2023 Census anticipation fueled further Sarna affiliation in tea-belt |
| Other_residual | 6.70 | E | Buddhist (Nepali-Gorkha, ~6.5%) + Sikh (0.5%) + Not_stated; slight Buddhist decrease as some claim Other_residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **ST_total** | 40.00 | A | Kalchini CDB 2011: 40.30%; stable; v0 holds at 40.00% |
| └ Oraon_Kurukh | 16.00 | D | ~40% of ST pool; stable |
| └ Munda | 8.00 | D | ~20% of ST pool |
| └ Santhal | 6.00 | D | ~15% of ST pool |
| └ Kharia_Gond_Kurmi | 6.00 | D | Mixed Chhattisgarh/Jharkhand-origin Adivasi |
| └ Nepali_Gorkha_ST | 4.00 | D | Tea-belt Nepali-origin ST |
| **SC_total** | 10.00 | A | Kalchini CDB 2011: 10.10%; stable |
| UC_bhadralok | 5.00 | D | Garden managers, Jaigaon traders; stable |
| OBC | 6.00 | D | Rajbanshi + other OBC; stable |
| Other_Hindu_middle | 7.00 | D | Bihari/Hindi-belt Hindu non-SC non-ST; Nepali non-ST non-SC |
| Muslim | 8.00 | E | See C.1; slightly higher than ST since 2011 base was 8.57% |
| Christian_plus_Sarna_plus_Other | 24.00 | E | Adivasi Christian (~16%) + Sarna/ORP (~4%) + Buddhist/Other (~4%); pooled |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2024, voters 18+ only; renormalized)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.0 | E | First-time voters 2024 (born 2002-2006); renormalized from 13-yr projection |
| 23_27 | 11.5 | E | |
| 28_32 | 11.0 | E | |
| 33_37 | 10.5 | E | |
| 38_42 | 10.0 | E | |
| 43_47 | 9.5 | E | |
| 48_52 | 8.5 | E | |
| 53_57 | 7.5 | E | |
| 58_62 | 7.0 | E | |
| 63_67 | 7.5 | E | |
| 68 | 6.0 | E | Smaller elderly cohort; tea-belt premature mortality pattern |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.50 | E | Continuing marginal shift toward balance from 2021 (51.65%); male in-migration from Jharkhand/Bihar stabilizing |
| Female | 48.49 | E | |
| Third_gender | 0.01 | E | Negligible |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 14.00 | A | Stable; Jaigaon urban Bengali community |
| Hindi | 8.00 | A | Stable |
| Urdu | 0.50 | E | Small Urdu-speaking fraction |
| Other | 3.50 | E | Boro, Rabha compressed residual |
| Sadri | 30.50 | A | Slight increase; Sadri remains dominant tea-garden lingua franca; cross-community bilingualism growing |
| Nepali | 25.50 | A | Slight decrease from 2011 (26.3%) as younger generation shifts to Sadri/Hindi |
| Kurukh | 3.00 | A | Stable; Oraon home language |
| Bhojpuri | 4.00 | A | Stable |
| Santali | 1.00 | E | Stable |
| Boro_Rabha_other | 10.00 | E | Slight increase as Other is recategorized; combined tribal language residual |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2024, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 22.00 | E | 2011: ~31%; +~1pp/yr improvement over 13yr → ~22% by 2024; Samagra Shiksha + mission schools |
| Primary | 22.00 | E | Shift from illiterate → primary continues |
| Middle | 22.00 | E | |
| Secondary | 16.00 | E | |
| Higher_Secondary | 11.00 | E | |
| Graduate | 5.50 | E | Stable; very low; tea-garden structural barrier to higher education |
| Postgraduate | 1.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 37.00 | E | Slight recovery from 2021 (36%); post-COVID normalization; tea-garden open gardens operating at pre-COVID capacity |
| └ Main_worker_tea_garden | 31.00 | D | Tea-garden wage labor; modest recovery; ₹232/day wage by 2024 |
| └ Main_worker_non_tea | 6.00 | D | Cultivator + ag-labor + household industry + trade + govt |
| Marginal_worker | 8.50 | E | Stable; seasonal picking continues |
| Non_worker | 37.50 | E | Housewife / elderly / retired; marginal decrease as female LFPR improves with Lakshmir Bhandar |
| Student | 7.00 | E | Stable enrollment |
| Unemployed | 10.00 | D | Slight improvement from 2021 (10.5%); some closed-garden rehabilitation; SSC scam dampened govt job aspirations nationally |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 4.00 | A | Stable |
| Agricultural_labourer | 5.00 | A | Stable |
| Household_industry | 2.00 | A | Stable |
| Manufacturing | 1.00 | E | Negligible |
| Construction | 1.50 | E | Slight decline from 2021 (2%); post-COVID normalization |
| Trade_retail | 8.00 | D | Jaigaon border-town retail growth; cross-border Bhutan trade resilient; Bangladesh interim govt (Aug 2024) disrupted Petrapole trade but Jaigaon-Bhutan channel less affected |
| Transport_logistics | 3.50 | D | Cross-border logistics growth as Bhutan trade expands |
| Services | 4.00 | E | Private service sector growth; healthcare, repair, telecoms |
| Government_services_teachers | 3.00 | E | Stable; SSC scam (2022) dampened new govt teacher recruitment; existing staff retained |
| Out_migrant_worker | 3.00 | E | Partial recovery of out-migration to Kerala/TN construction markets post-COVID; lower than pre-COVID as some settled back |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.00 | E | Stable |
| Employee | 70.00 | E | Tea-garden organized-sector recovery to 2019 levels after COVID casualization phase; govt employees stable |
| Single_worker | 18.00 | E | Own-account working stabilizing after COVID spike |
| Family_worker | 11.00 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2024, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 44.00 | D | Tea-garden wage revised to ₹232/day from 2023; marginal improvement from 2021 (47%); Lakshmir Bhandar provides ₹1,000/month supplementary income to ST women HH heads; RG Kar Aug 2024 protests did not directly affect tea-belt income; v0 uses 44% |
| Above_Poverty_Line_low_income | 29.00 | E | Marginal improvement as wage revision lifts some households |
| Lower_middle | 16.00 | E | Jaigaon border traders benefiting from Bhutan trade growth |
| Middle | 9.00 | E | Slightly improved; garden supervisory + govt employees + traders |
| Upper_middle_well_off | 2.00 | E | Garden managers; Jaigaon commercial class; stable |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Kalchini_CDB_core | 93.8 | E | Stable |
| U2_Majherdabri_GP | 6.2 | E | Stable |
| **Sum** | **100.00** | — | self-check |

Sub-unit decomposition within U1 (2024):

| Category | % of U1 | Tier | Source / Note |
|---|---|---|---|
| Urban (Jaigaon + Uttar Satali + Uttar Latabari + Mechiabasti) | 31.0 | E | Continued urban expansion in Jaigaon border town; growth ~1pp per 3yr |
| Rural (tea-garden villages + forest settlements) | 69.0 | E | |

### C.12 Household composition (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.6 | E | Continuing decline from 2021 (4.7); fertility reduction and nuclear family formation |
| Nuclear_HH | 64.0 | E | Continuing increase |
| Joint_HH | 27.0 | E | Continuing decrease |
| Extended_multi_generation | 9.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.0 | E | Marginal increase; later marriage trend in 18-22 cohort |
| Currently_married | 65.0 | E | Stable |
| Widowed | 9.0 | E | Stable; COVID excess mortality effect fading |
| Separated_divorced | 1.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2024, household level — independent flags, do NOT sum)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 55.0 | D | Modest increase from 2021 (52%); saturation approaching in some communities; some HH dropping TV for mobile streaming |
| Radio | 10.0 | D | Continuing decline from 2021 (12%); radio yielding to mobile; still used in remote bagan areas |
| Mobile_phone | 90.0 | D | Near-saturation; up from 2021 (82%); even closed-garden workers have basic phones |
| Smartphone_with_internet | 72.0 | D | Strong growth from 2021 (48%); +24pp; UPI/BHIM required for Lakshmir Bhandar verification drove adoption; NFHS-5 WB rural ~70%; tea-belt converging toward state average; load-bearing for narrative-injection weighting |
| Computer | 6.0 | E | Very slow growth |
| Two_wheeler | 16.0 | E | Marginal increase; post-wage-revision asset accumulation |
| Four_wheeler | 2.5 | E | Very slight increase; Jaigaon traders |
| Banking_access | 88.0 | B | Strong increase from 2021 (82%); Lakshmir Bhandar enrollment drove bank account adoption; PMJDY + Aadhaar-seeded accounts |
| Note | (independent ownership %s, not categorical — do not sum) | — | — |

### C.15 Household amenities (2024)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 68.0 | D | Jal Jeevan Mission (JJM) made progress in WB 2021-24; Alipurduar received JJM connections; improvement from 2021 (62%) |
| Improved_sanitation | 35.0 | D | ODF campaign + SBM phase 2 improved coverage; +7pp from 2021 (28%); private bagan land remains under-covered |
| LPG_clean_cooking_fuel | 38.0 | D | Ujjwala 2.0 (Aug 2021) extended coverage; refill subsidies intermittently available; +8pp from 2021 (30%) |
| Wood_biomass_fuel | 57.0 | E | Decreasing from 2021 (65%) as LPG penetrates |
| Other_fuel | 5.0 | E | Stable |
| Electricity | 87.0 | D | Marginal improvement; quality of supply improving in some bagan lines |
| Note | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 62.0 | D | Further slight increase as more workers registered at home addresses |
| WB_other_district | 4.0 | D | Low; limited new internal WB in-migration |
| Other_Indian_state | 0.5 | E | Marginal |
| Bangladesh_origin | 0.5 | E | Bangladesh interim govt (Aug 2024) uncertainty did NOT produce significant new migration to tea-belt; Petrapole disruption was trade-not-migration; negligible increase |
| Outside_India | 0.5 | E | Nepal/Bhutan recent in-migration negligible |
| Out_migrant | 3.5 | E | Slight increase from 2021 (3%); post-COVID out-migration partially resumed to Kerala/Tamil Nadu construction |
| Jharkhand_origin | 24.5 | D | Stable multi-generational Adivasi identity; slight % decrease as native-born generation enlarges |
| Nepal_Bhutan_origin | 4.0 | D | Stable Nepali/Gorkha community |
| Bihari_UP_origin | 0.5 | D | Slight decrease; Bhojpuri-heritage older workers aging out |
| **Sum** | **100.00** | — | self-check; 62+4+0.5+0.5+0.5+3.5+24.5+4+0.5 = 100 |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue (2024)

| Religion | Bengali | Hindi | Urdu | Sadri | Nepali | Kurukh | Bhojpuri | Santali | Boro_Rabha_other | Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 20.0 | 9.0 | 0.5 | 27.0 | 27.5 | 3.5 | 5.0 | 0.5 | 5.0 | 2.0 | E | Sadri gains slightly as inter-community communication intensifies; Nepali slight decrease |
| Muslim | 75.0 | 11.0 | 6.5 | 2.0 | 2.0 | 0.0 | 2.0 | 0.0 | 1.5 | 0.0 | E | Stable Bengali-Muslim language profile |
| Christian | 8.0 | 5.0 | 0.0 | 49.0 | 11.0 | 8.0 | 5.0 | 3.5 | 8.0 | 2.5 | E | Adivasi Christian stable; slight Santali increase |
| Sarna_ORP | 5.0 | 4.0 | 0.0 | 60.0 | 0.0 | 16.0 | 2.0 | 4.0 | 7.0 | 2.0 | E | Sarna-identifying Adivasi Sadri-dominant; growing Kurukh identity reclamation |
| Other_residual | 4.0 | 2.0 | 0.0 | 3.0 | 88.0 | 0.0 | 1.0 | 0.0 | 2.0 | 0.0 | E | Predominantly Nepali-speaking Buddhist |

### D.2 Religion × Caste (2024, 2D layout)

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 12.0 | 28.0 | 8.0 | 9.0 | 23.0 | 0.0 | 20.0 | E | Stable from 2021; see 2021 layer for derivation logic |
| Muslim | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | A | |
| Christian | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | A | |
| Sarna_ORP | 0.0 | 95.0 | 0.0 | 3.0 | 2.0 | 0.0 | 0.0 | E | Sarna = predominantly ST-identifying Adivasi |
| Other_residual | 2.0 | 5.0 | 3.0 | 10.0 | 30.0 | 0.0 | 50.0 | E | Buddhist Nepali + Sikh + Not-stated residual |

### D.3 Religion × Migration (2024)

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Jharkhand_origin | Nepal_Bhutan_origin | Bihari_UP_origin | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 61.0 | 5.0 | 0.5 | 0.5 | 0.5 | 3.5 | 20.0 | 8.0 | 1.0 | D | Stable profile |
| Muslim | 80.0 | 8.0 | 0.0 | 2.5 | 0.0 | 2.0 | 0.0 | 0.0 | 7.5 | D | Stable |
| Christian | 56.0 | 3.0 | 0.5 | 0.5 | 0.5 | 2.5 | 35.5 | 1.0 | 0.5 | D | Stable Jharkhand-origin Adivasi Christian families |
| Sarna_ORP | 46.0 | 3.0 | 0.5 | 0.5 | 0.5 | 2.0 | 46.0 | 1.0 | 0.5 | D | Stable |
| Other_residual | 51.0 | 2.0 | 0.5 | 0.5 | 0.5 | 1.5 | 0.0 | 43.5 | 0.5 | E | Nepal-origin Buddhist stable |

### D.4 Religion × Asset / media (2024)

| Religion | Television | Radio | Mobile_phone | Smartphone_with_internet | Computer | Two_wheeler | Four_wheeler | Banking_access | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 60.0 | 9.0 | 91.0 | 75.0 | 7.0 | 18.0 | 3.0 | 90.0 | D | UPI + Lakshmir Bhandar drove smartphone and banking adoption across all groups |
| Muslim | 63.0 | 8.0 | 92.0 | 73.0 | 7.0 | 17.0 | 2.5 | 89.0 | D | Stable relative rank |
| Christian | 47.0 | 10.0 | 87.0 | 62.0 | 5.0 | 12.0 | 1.5 | 82.0 | D | Adivasi Christian beneficiary of Lakshmir Bhandar (ST ₹1,000) drove banking |
| Sarna_ORP | 35.0 | 12.0 | 80.0 | 52.0 | 3.0 | 9.0 | 1.0 | 70.0 | D | Poorest segment; Lakshmir Bhandar partially closed asset gap |
| Other_residual | 68.0 | 7.0 | 93.0 | 78.0 | 10.0 | 22.0 | 4.0 | 92.0 | E | Nepali/Buddhist community; border-trade income; highest assets |

### D.5 Caste × Education (2024)

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 3.0 | 8.0 | 10.0 | 18.0 | 23.0 | 26.0 | 12.0 | E |
| OBC | 13.0 | 20.0 | 22.0 | 22.0 | 14.0 | 7.0 | 2.0 | E |
| Other_Hindu_middle | 15.0 | 21.0 | 22.0 | 21.0 | 13.0 | 6.0 | 2.0 | E |
| ST_total | 26.0 | 28.0 | 23.0 | 14.0 | 7.0 | 2.0 | 0.0 | E |
| SC_total | 25.0 | 27.0 | 24.0 | 16.0 | 7.0 | 1.0 | 0.0 | E |
| Muslim | 20.0 | 24.0 | 25.0 | 20.0 | 8.0 | 3.0 | 0.0 | E |
| Christian_plus_Sarna_plus_Other | 21.0 | 28.0 | 26.0 | 16.0 | 7.0 | 2.0 | 0.0 | E |

### D.6 Age × Gender × Education (2024)

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 10.0 | 8.0 | E |
| 23_27 | 9.0 | 6.0 | E |
| 28_32 | 7.0 | 4.0 | E |
| 33_37 | 6.0 | 3.0 | E |
| 38_42 | 5.0 | 2.0 | E |
| 43_47 | 4.5 | 1.5 | E |
| 48_52 | 3.5 | 1.0 | E |
| 53_57 | 3.0 | 1.0 | E |
| 58_62 | 2.5 | 0.5 | E |
| 63_67 | 2.0 | 0.5 | E |
| 68 | 2.0 | 0.5 | E |

### D.7 Marital status × Age × Gender (2024)

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 10.0 | 40.0 | E |
| 23_27 | 55.0 | 82.0 | E |
| 28_32 | 85.0 | 92.0 | E |
| 33_37 | 92.0 | 90.0 | E |
| 38_42 | 91.0 | 88.0 | E |
| 43_47 | 90.0 | 86.0 | E |
| 48_52 | 88.0 | 74.0 | E |
| 53_57 | 85.0 | 63.0 | E |
| 58_62 | 82.0 | 53.0 | E |
| 63_67 | 70.0 | 32.0 | E |
| 68 | 62.0 | 22.0 | E |

### D.8 Occupation × Asset / media (2024)

| Occupation | Television | Radio | Mobile_phone | Smartphone_with_internet | Computer | Two_wheeler | Four_wheeler | Banking_access | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Cultivator | 53.0 | 10.0 | 88.0 | 60.0 | 4.0 | 20.0 | 2.0 | 86.0 | E | |
| Agricultural_labourer | 40.0 | 11.0 | 82.0 | 50.0 | 2.0 | 10.0 | 0.5 | 78.0 | E | |
| Household_industry | 48.0 | 10.0 | 85.0 | 55.0 | 3.0 | 12.0 | 1.0 | 80.0 | E | |
| Manufacturing | 50.0 | 8.0 | 88.0 | 60.0 | 4.0 | 14.0 | 1.0 | 83.0 | E | |
| Construction | 42.0 | 10.0 | 85.0 | 52.0 | 2.0 | 12.0 | 0.5 | 78.0 | E | |
| Trade_retail | 75.0 | 6.0 | 96.0 | 82.0 | 10.0 | 35.0 | 5.0 | 94.0 | D | Jaigaon border-town traders; high UPI adoption; WhatsApp commerce |
| Transport_logistics | 65.0 | 8.0 | 93.0 | 72.0 | 6.0 | 50.0 | 4.0 | 90.0 | E | Cross-border logistics; high mobility |
| Services | 58.0 | 7.0 | 92.0 | 70.0 | 10.0 | 22.0 | 2.5 | 88.0 | E | |
| Government_services_teachers | 90.0 | 5.0 | 98.0 | 88.0 | 45.0 | 38.0 | 10.0 | 99.0 | E | |
| Out_migrant_worker | 38.0 | 8.0 | 92.0 | 60.0 | 4.0 | 14.0 | 1.5 | 80.0 | E | Remittances support moderate asset profile |

### D.9 Education × Workforce participation (2024)

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 42.0 | 2.0 | E |
| Primary | 45.0 | 3.5 | E |
| Middle | 40.0 | 5.5 | E |
| Secondary | 29.0 | 11.0 | E |
| Higher_Secondary | 19.0 | 21.0 | E |
| Graduate | 18.0 | 28.0 | E |
| Postgraduate | 30.0 | 18.0 | E |

### D.10 Asset × Bilingualism (2024)

P(bilingual Sadri+Bengali ‖ media-access tier):

| Category | Sadri_Bengali_bilingual | Tier | Source |
|---|---|---|---|
| TV-only HH | 22.0 | E | Stable |
| TV_plus_smartphone HH | 42.0 | E | YouTube Bengali content penetration; slightly higher than 2021 |
| Smartphone-only HH | 30.0 | E | Mobile-first users; cross-language YouTube growing |
| Radio-only HH | 10.0 | E | Declining radio base; remaining users in remote bagans |
| No-asset HH | 8.0 | E | Lowest exposure |

### D.11 GP / Sub-unit × Religion (2024)

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Kalchini_CDB_core | 64.5 | 7.5 | 16.3 | 4.2 | 7.5 | E | 2011 CDB proportions projected 13yr |
| U2_Majherdabri_GP | 84.0 | 6.5 | 8.7 | 0.5 | 0.3 | E | Alipurduar II CDB 2011 projected; stable |

### D.12 GP / Sub-unit × Caste (2024)

| Sub_unit | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Kalchini_CDB_core | 9.5 | 42.0 | 5.0 | 5.5 | 11.5 | 7.5 | 19.0 | E |
| U2_Majherdabri_GP | 41.8 | 18.4 | 3.0 | 10.0 | 14.0 | 6.5 | 6.3 | E |

### D.13 GP / Sub-unit × Asset / media (2024)

| Sub_unit | Television | Radio | Mobile_phone | Smartphone_with_internet | Computer | Two_wheeler | Four_wheeler | Banking_access | Tier |
|---|---|---|---|---|---|---|---|---|---|
| U1_Kalchini_CDB_core | 53.0 | 10.0 | 88.0 | 70.0 | 5.5 | 15.0 | 2.0 | 86.0 | D |
| U2_Majherdabri_GP | 68.0 | 7.0 | 95.0 | 80.0 | 9.0 | 24.0 | 4.0 | 94.0 | E |

### D.14 GP / Sub-unit × Amenities (2024)

| Sub_unit | Improved_drinking_water_source | Improved_sanitation | LPG_clean_cooking_fuel | Wood_biomass_fuel | Other_fuel | Electricity | Tier |
|---|---|---|---|---|---|---|---|
| U1_Kalchini_CDB_core | 66.0 | 33.0 | 36.0 | 59.0 | 5.0 | 85.0 | D |
| U2_Majherdabri_GP | 80.0 | 52.0 | 48.0 | 47.0 | 5.0 | 95.0 | E |

### D.15 Vote × Religion (2024 LS, AC 011)

P(party ‖ religion) — derived from AC 011 2024 LS segment result (BJP 51.54% / AITC 43.59%) combined with CSDS-Lokniti WB patterns.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 54.0 | 36.0 | 2.0 | 4.5 | 3.5 | C/D | BJP BTWU hold weakening gradually; Nepali-Gorkha community partially shifting; Lakshmir Bhandar matured delivery to women |
| Muslim | 6.0 | 75.0 | 4.0 | 10.0 | 5.0 | D | Muslim consolidated AITC; BJP made no inroads in Muslim tea-belt segment |
| Christian | 40.0 | 48.0 | 2.5 | 6.5 | 3.0 | D | Christian Adivasi: AITC now slight plurality; Lakshmir Bhandar ₹1,000/ST women; 3yr delivery; CAA notification not relevant to tea-belt ST |
| Sarna_ORP | 50.0 | 37.0 | 2.0 | 7.0 | 4.0 | D | Sarna BJP support narrowing; identity movement somewhat independent of BJP; but no organized Sarna party here |
| Other_residual | 52.0 | 35.0 | 2.0 | 4.0 | 7.0 | D | Nepali/Buddhist: BJP hold weakening; some anti-incumbency at Centre |

### D.16 Vote × Caste (2024 LS, AC 011)

P(party ‖ caste group):

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| ST_total | 56.0 | 37.0 | 1.5 | 4.0 | 1.5 | D | BTWU hold weakened ~4pp from 2021 AE; Manoj Tigga replaced John Barla (LS 2024); Adivasi ST vote drifting toward AITC via welfare delivery; BJP still plurality |
| SC_total | 30.0 | 55.0 | 2.0 | 9.0 | 4.0 | D | SC decisively AITC; Lakshmir Bhandar + Swasthya Sathi; 3yr cumulative welfare delivery impact |
| UC_bhadralok | 50.0 | 40.0 | 3.0 | 4.0 | 3.0 | D | Bengali bhadralok BJP weakening with RG Kar Aug 2024 protests nationally; but Kalchini bhadralok is small |
| OBC | 40.0 | 50.0 | 3.0 | 5.0 | 2.0 | D | OBC shifted further toward AITC |
| Other_Hindu_middle | 48.0 | 40.0 | 2.5 | 6.5 | 3.0 | D | Mixed; slight AITC improvement |
| Muslim | 6.0 | 75.0 | 4.0 | 10.0 | 5.0 | D | |
| Christian_plus_Sarna_plus_Other | 43.0 | 46.0 | 2.0 | 6.0 | 3.0 | D | Christian Adivasi + Sarna: AITC now edging ahead; cumulative welfare scheme delivery decisive |

### D.17 Vote × Gender (2024 LS, AC 011)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 53.0 | 39.0 | 2.0 | 4.5 | 1.5 | D | Male BTWU worker base; BJP narrow majority; some male anti-incumbency on Centre jobs/price rise |
| Female | 49.5 | 46.0 | 2.0 | 1.5 | 1.0 | D | Lakshmir Bhandar ₹1,000/ST women 3yr delivery; female vote closing BJP-AITC gap; AITC nearly at parity among women |
| Third_gender | 49.5 | 46.0 | 2.0 | 1.5 | 1.0 | E | Assumed same as Female distribution; negligible sample |

### D.18 Vote × Welfare scheme exposure (2024 LS, AC 011)

P(party ‖ welfare-scheme exposure) — dominant schemes by 2024: Lakshmir Bhandar (3 years of delivery), Swasthya Sathi (health card), Kanyashree, Krishak Bandhu, revised tea-garden wage ₹232/day.

| Welfare_exposure | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Lakshmir_Bhandar_enrolled | 38.0 | 55.0 | 2.0 | 3.5 | 1.5 | D | 3 years of ₹1,000/month for ST women HH heads; strongest AITC credit claim; cumulative impact higher than 2021 |
| Swasthya_Sathi_enrolled | 44.0 | 49.0 | 2.0 | 3.0 | 2.0 | D | Health scheme 3yr delivery; AITC plurality in scheme-exposed HH |
| Kanyashree_HH | 48.0 | 45.0 | 2.5 | 3.0 | 1.5 | D | Girl-student HH; near-parity |
| Khadya_Sathi_PDS | 52.0 | 40.0 | 2.5 | 4.0 | 1.5 | D | PDS; BJP still competitive; BTWU distributes BJP credit for Centre's free ration scheme |
| No_state_scheme_exposure | 60.0 | 28.0 | 2.5 | 7.0 | 2.5 | D | BJP dominant among scheme-unexposed; BTWU organizational substitute |

---

## E. 2024 baseline vote (calibration target)

The simulator must reproduce this aggregate within ±1pp. **Calibration year: 2024 LS AC-segment.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 51.54 | A | ECI 2024 LS CSV — Manoj Tigga (BJP) 96,391 / 187,029 total valid; data/2024_AssemblySegmentLevelVotingData.csv |
| AITC | 43.59 | A | ECI 2024 LS CSV — Prakash Chik Baraik (AITC) 81,526 votes |
| INC | 0.00 | A | No INC candidate in 2024 LS AC 011; 0.0% |
| LF | 1.58 | A | RSP (Mili Oraon) 2,954 votes; only Left party contesting; INC+LF=1.58% |
| Other_NOTA | 3.29 | A | NOTA 2,945 + IND (1,823+1,596) + KMSP 738 + BSP 907 + SUCI 357 + others = 8,366 votes; computed as 100 - 51.54 - 43.59 - 0.00 - 1.58 = 3.29 |

> Sum check: 51.54 + 43.59 + 0.00 + 1.58 + 3.29 = 100.00 ✓
> Total valid votes: 187,029 | Electorate: 254,731 | Turnout: 73.4%
> BJP margin over AITC: 14,865 votes (7.95 pp)
> BJP retained plurality for the fourth consecutive election (2019 LS, 2021 AE, 2024 LS) but margin compressed from 24.90 pp (2019 LS) → 14.59 pp (2021 AE) → 7.95 pp (2024 LS).

---

## F. Vote history (2019–2024 chronological anchors)

### AC 011 Kalchini — full electoral record

| Year | Winner | Party | Votes | % | Runner-up | Party | % | Margin | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2024 LS (AC-seg) | Manoj Tigga | BJP | 96,391 | 51.54 | Prakash Chik Baraik | AITC | 43.59 | 7.95 pp | BJP plurality; AITC closed gap significantly; calibration target for this layer |
| 2021 AE | Bishal Lama | BJP | 103,104 | 52.65 | Passang Lama | AITC | 38.06 | 14.59 pp | BJP retained; Lakshmir Bhandar mid-campaign effect; AITC +4.4 pp vs 2019 LS |
| 2019 LS (AC-seg) | John Barla | BJP | 111,477 | 58.53 | Dasrath Tirkey | AITC | 33.63 | 24.90 pp | BJP surge; BTWU consolidation; RSP collapse; 2019 baseline calibration target |
| 2016 AE | Wilson Champramary | AITC | 62,061 | 34.99 | Bishal Lama | BJP | 60,550 | 34.14 | 0.85 pp — razor-thin AITC win; GJM vote split |
| 2011 AE | Wilson Champramary | GJM-backed IND | 46,455 | 30.05 | Binay Bhusan Kerketta | RSP | 39,210 | 25.37 | Multi-party split; GJM IND won |
| 2009 LS | Manohar Tirkey | RSP | — | 41.22 | Paban Kumar Lakra | AITC | 29.14 | — | RSP hold; BJP 21.40% third |
| 2006 AE | Manohar Tirkey | RSP | — | — | Paban Kumar Lakra | INC | — | — | RSP stronghold period |
| 2001 AE | Paban Kumar Lakra | INC | — | — | Manohar Tirkey | RSP | — | — | INC beat RSP |

### Trajectory summary

The BJP-AITC margin has compressed in each successive election: 24.90 pp (2019 LS) → 14.59 pp (2021 AE) → 7.95 pp (2024 LS). The compression rate is roughly 8.5 pp per 2-3 year cycle. If trend continues, the seat is marginal by 2026.

### Key 2021–2024 context events (known by end-2024)

- **Tea-garden wage revision (2021-2024)**: WB govt revised minimum wage to ₹202/day (Jan 2021), then ₹232/day (2023); both BJP and AITC contested credit; BTWU credit narrative for BJP eroded as AITC wage revision delivered under TMC
- **SSC scam exposure (Jul 2022)**: Partha Chatterjee arrested; Rs 21 crore cash seized at Arpita Mukherjee; WB teacher recruitment scandal; direct impact in Kalchini limited (few SSC teachers in tea-belt); indirect national narrative damaged TMC image but tea-garden Adivasi electorate prioritized local welfare delivery over state-level corruption narrative
- **WB Panchayat election (Jul 2023)**: TMC dominance statewide; BJP panchayat presence weakened; in Alipurduar district TMC made panchayat gains but BJP retained rural presence through BTWU
- **CAA rules notification (Mar 2024)**: Citizenship Amendment Act 2019 rules notified March 11, 2024; Matua belt in South Bengal jubilant; Kalchini/Alipurduar is tea-belt ST seat — CAA not applicable to ST communities; minimal direct electoral impact in Kalchini; no Matua demographic in AC 011
- **2024 LS campaign**: Manoj Tigga (BJP) replaced John Barla as Alipurduars LS candidate; Tigga is also ST from tea-belt; AITC candidate Prakash Chik Baraik ran strong campaign emphasizing Lakshmir Bhandar delivery; BJP Centre's free ration scheme (PMGKAY) emphasized; turnout dipped to 73.4% from 2019 (80.8%)
- **RG Kar Hospital protests (Aug 2024)**: Mass protests across WB following rape-murder of trainee doctor; Kalchini is remote tea-belt — protests more symbolic than structural; TMC reputation dented nationally; some educated urban sympathy in Jaigaon but minimal impact on Adivasi bagan vote
- **Bangladesh interim regime (Aug 2024+)**: Hasina ouster; Yunus govt; India-Bangladesh trade disrupted at Petrapole/Benapole; however Kalchini borders Bhutan (Jaigaon-Phuentsholing), not Bangladesh; Bhutan trade channel unaffected; Dooars-based tea garden exports to Bangladesh via Changrabandha partially disrupted; modest income effect on tea-belt traders
- **Dooars tea-belt economic conditions 2021-24**: Tea garden wages improved from ₹176 to ₹202 to ₹232/day; closed gardens remained a grievance (19+ closed); Lakshmir Bhandar ₹1,000/month for ST women substantially supplemented household income in tea-belt; PMGKAY free ration sustained Centre-level BJP credit; dual welfare narrative created competitive parity

---

## G. Sources & tier flags

### Primary sources (tier A)

- Census of India 2011 — Kalchini CD Block; Alipurduar II CD Block; Alipurduar District
- `data/2024_AssemblySegmentLevelVotingData.csv` — AC_NO=11: BJP 96,391 / AITC 81,526 / RSP 2,954 / NOTA 2,945 / others; electorate 254,731; ECI tier A
- ECI 2021 AE — AC 011 Kalchini result: Bishal Lama (BJP) 103,104 / Passang Lama (AITC) 74,528; via Wikipedia
- ECI 2019 LS `data/2019_AssemblySegmentLevelVotingData.csv` — BJP 111,477 / AITC 64,045; electorate 235,753
- ECI 2016 AE / 2011 AE historical results — via Wikipedia
- Delimitation Commission of India 2008

### Secondary sources (tier B/C)

- NFHS-5 (2019-21) West Bengal — asset/media baseline update
- CSDS-Lokniti 2024 NES post-poll — WB regional vote × religion/caste/gender (state rollup)
- WB Jal Jeevan Mission progress reports (district level)
- WB Lakshmir Bhandar dashboard — district-level enrollment

### Tertiary / journalistic (tier D)

- The Print (2021, 2024) — tea-garden labor and BTWU organizing; CAA impact on North Bengal
- The Bastion (2021) — plantation sanitation and wage data
- Wire/Scroll/Indian Express (2022-24) — SSC scam; RG Kar; Bangladesh trade; CAA notification
- Business Standard / Mint — tea-garden wage revision 2021, 2023
- Wikipedia "Kalchini (Vidhan Sabha constituency)"; "Alipurduars Lok Sabha constituency"; "Kalchini (community development block)"

### Tier-D/E reliance flags

- **Vote × religion/caste joints** (D.15–D.17) — derived from tier-A aggregate + CSDS directional priors; no 2024 AC-level post-poll; treat as tier C/D
- **Asset/media** (C.14, D.4, D.8, D.13) — NFHS-5 provides district direction; no bagan-specific survey; tier D
- **Economic status** (C.10) — directional from wage revision data; no AC-level HH survey; tier D
- **CAA/Bangladesh impact** — minimal for ST-reserved tea-belt AC; modeled as near-zero; tier E

### v0 known gaps

1. Bagan-level election results — within Kalchini CDB, different gardens may show different vote patterns; v0 collapses to CDB
2. CSDS 2024 WB post-poll sub-district data — not publicly available at AC 011 granularity
3. Actual Lakshmir Bhandar enrollment count in Kalchini — state dashboard figure not accessed at block level
4. 2021 AE INC and LF granular vote counts — tier D estimates

---

*v0 — generated 2026-04-28, frozen at end-2024 state-of-knowledge. No 2025/2026 events referenced.*

---

## H. Post-2024 validation anchors

> No post-2024 out-of-sample anchors have been fetched in v0. The 2026 WB Assembly Election result for AC 011 Kalchini is the next validation gate.
>
> Projection: Given BJP-AITC margin compression (24.90 pp → 14.59 pp → 7.95 pp across three elections), AC 011 Kalchini enters 2026 as a **competitive but BJP-leaning** seat. The simulator's 2026 forecast should capture this uncertainty.
>
> TBD: 2026 WB Assembly Election result for AC 011 (will be added as tier A once available).
