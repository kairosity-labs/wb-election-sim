# AC 012 — Alipurduars (GEN) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 012 Alipurduars as of end-2021 only — it must not reference
> any post-2021 events. Use post-2021 elections (2024 LS) as out-of-sample
> validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../../NORMALIZED_SCHEMA.md)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 012 | A | ECI / Delimitation Commission 2008 |
| AC name | Alipurduars | A | ECI |
| Reservation | GEN | A | Delimitation 2008 |
| District | Alipurduar | A | Delimitation 2008 (Alipurduar district carved from Jalpaiguri 2014) |
| Sub-division | Alipurduar | A | WB administrative |
| LS constituency | 2 — Alipurduars (ST reserved) | A | Delimitation 2008 |
| LS segments included | AC 9 Tufanganj · 10 Natabari · 11 Sitalkuchi · 12 Alipurduars · 13 Kalchini (ST) · 14 Kumargram (ST) · 15 Madarihat (ST) · 16 Dhupguri — see note | A | Delimitation 2008 |
| AC composition | Alipurduar Municipality (full) + Alipurduar Railway Junction census town + Banchukamari, Chakowakheti, Mathura, Parorpar, Patlakhawa, Shalkumar I, Shalkumar II, Tapsikhata, Vivekananda I, Vivekananda II GPs (Alipurduar I CDB) + Chaporerpar I, Chaporerpar II, Tatpara II GPs (Alipurduar II CDB) | A | Delimitation 2008 WB Schedule |
| Geographic note | District HQ town of Alipurduar district; Dooars foothills; tea garden and forest landscape; Buxa Tiger Reserve to the north | A | — |
| Sub-units used in v0 | **U1: Alipurduar_Municipality** (urban core) · **U2: CDB_rural_tea_garden** (GPs of Alipurduar I + II CDBs) | E | v0 simplification |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~180,000 (Muni 56,171 urban + Rly Junction town ~15,000 + GPs ~109,000) | E | Census 2011 Alipurduar I CDB; v0 rough apportionment as in 2019 file |
| 2021 projected population | ~199,500 | E | 10-yr compound growth ~1.05%/yr from 2011 (Dooars slower than state average; tea-belt outmigration holds growth below WB mean) |
| Sex ratio (2021, F per 1000 M) | ~952 | E | Alipurduar district NFHS-5 (2019-21) Jalpaiguri proxy: 1038 state-level shift; Dooars male-skew in tea pockets moderates; AC estimate |
| 2021 AE electorate | 260,652 | A | ECI 2021 WB AE official roll — from detailed_results.csv |
| Estimated M / F / TG split (2021) | 51.30% M / 48.60% F / 0.10% TG | E | District sex ratio projection; NFHS-5 Jalpaiguri sex ratio 969→1038 suggests modest improvement |
| 2021 polling stations | ~275 | E | Back-projection from 2021 AE; slight growth from 2019 estimate of ~270 |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 88.30 | E | 2019 baseline 88.50%; modest Muslim relative growth ~0.15pp over 2 yrs; Christian/Sarna stable in tea-belt; 2021 projected |
| Muslim | 6.30 | E | 2019: 6.20%; 2-yr differential growth ~+0.10pp |
| Christian | 3.50 | E | Stable; tea-garden Adivasi Christian share unchanged 2019→2021 |
| Sarna_ORP | 1.20 | E | Stable; Oraon/Munda Sarna practitioners |
| Other_residual | 0.70 | E | Buddhist/Sikh/Jain/Not_stated residual; marginal increase |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 40.00 | A | Unchanged from 2019 baseline; no new caste data; Census 2011 AC-weighted blend; municipality dilutes to ~40% |
| └ Rajbanshi_SC | 30.00 | C | Dominant SC sub-group in Dooars/Terai; Koch-Rajbongshi/Rajbanshi declared SC in WB |
| └ Other_SC | 10.00 | E | Smaller SC communities (Bagdi, Hari, Chamar fringe) |
| **ST_total** | 9.00 | E | Unchanged; GEN AC with lower ST concentration than AC 13/14; tea-garden Adivasi (Oraon, Munda, Ho, Santhali) |
| └ Oraon_ST | 4.50 | C | Largest ST group in Dooars tea gardens; Kurukh speakers |
| └ Munda_Santhali_ST | 3.00 | E | Second tier ST groups in tea gardens |
| └ Other_ST | 1.50 | E | Ho, Bhumij, Bhutia fringe |
| UC_bhadralok | 4.00 | E | Brahmin/Kayastha/Baidya; small in Dooars; service class in Alipurduar town |
| OBC | 5.00 | E | Koch-Rajbongshi OBC (those not classified SC), Mahishya fringe |
| Other_Hindu_middle | 28.00 | E | Unclassified Hindu middle + Rajbongshi community subsets; residual within Hindu non-SC/ST |
| Muslim | 6.30 | E | All sub-castes pooled; see C.1 2021 update |
| Christian_plus_Sarna_plus_Other | 7.70 | E | Christian (3.5%) + Sarna_ORP (1.2%) + Other_residual (0.7%) + remaining ST/others |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2021, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.50 | E | 2 yr cohort shift from 2019; 2019 first-timers now 20-24; slight reduction in youngest as birth-rate declines |
| 23_27 | 11.50 | E | Absorbs 2019 18-22 cohort + Jio-era young adults |
| 28_32 | 11.00 | E | Stable; slight shift |
| 33_37 | 10.00 | E | Unchanged from 2019 projection |
| 38_42 | 9.50 | E | Unchanged |
| 43_47 | 9.00 | E | Unchanged |
| 48_52 | 8.00 | E | Unchanged |
| 53_57 | 7.00 | E | Unchanged |
| 58_62 | 6.00 | E | Unchanged |
| 63_67 | 4.50 | E | Slight increase as 2011 older cohort ages in |
| 68 | 12.00 | E | 68+ open-ended; older cohort stable; renormalized to sum |
| **Sum** | **100.00** | — | self-check (18+ adults only; children excluded) |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.30 | E | NFHS-5 Jalpaiguri sex ratio 1038 F per 1000 M → ~49.1% F / 50.9% M; tea-garden slight male-skew in some pockets; AC estimate |
| Female | 48.60 | E | Marginal improvement from NFHS-5 trend |
| Third_gender | 0.10 | E | Small but non-negligible in town context |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 66.00 | A | CDB I 2011: 66.32% Bengali; stable; dominant in urban Alipurduar and bhadralok belt |
| Hindi | 5.00 | E | Bihari/UP migrant workers; stable |
| Urdu | 0.80 | E | Small Muslim pocket; stable |
| Other | 0.70 | E | Residual catch-all (Nepali fringe, Bhutia, etc.) |
| Sadri | 10.00 | A | CDB I 2011: 9.95% Sadri; tea-garden Adivasi lingua franca (Oraon, Munda workers); stable |
| Rajbongshi | 8.00 | A | CDB I 2011: 4.64% Rajbongshi (declared); AC includes Rajbanshi-belt GPs; est. ~8%; stable |
| Kurukh | 4.00 | A | CDB I 2011: 2.35% Kurukh; Oraon mother tongue; concentrated in tea-garden GPs |
| Boro | 2.50 | A | CDB I 2011: 1.52% Boro; Bodo community in Dooars foothill belt |
| Nepali | 1.50 | A | CDB I 2011: 1.15% Nepali; Gurkha/Gorkha community; Alipurduar town fringe |
| Mundari | 1.50 | A | CDB I 2011: 1.06% Mundari; Munda community in tea gardens |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 18.00 | E | 2019 baseline 20%; NFHS-5 Jalpaiguri women literate 73.6% vs NFHS-4 68.8% — ~+5pp improvement in literacy broadly; 2021 projection ~18% illiterate |
| Primary | 24.00 | E | Class 1–5; large share among tea-garden community; stable |
| Middle | 21.00 | E | Class 6–8; stable |
| Secondary | 18.00 | E | Class 9–10; slight +1pp as education expands |
| Higher_Secondary | 11.00 | E | Class 11–12; slight +1pp |
| Graduate | 6.00 | E | Urban professional class; stable |
| Postgraduate | 2.00 | E | Small but present in district HQ service sector |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 35.00 | E | Slight reduction from 2019 (36%) due to COVID-19 lockdown impact on informal workers; tea-garden permanent workers partially restored by late 2021 |
| └ Main_worker_tea_garden | 13.50 | E | Sub-row: slight COVID-impact reduction from 14% (is_subgroup=yes) |
| └ Main_worker_non_tea | 21.50 | E | Sub-row: non–tea-garden main workers (is_subgroup=yes) |
| Marginal_worker | 10.00 | E | Seasonal agricultural; stable; COVID disrupted some seasonal patterns |
| Non_worker | 35.00 | E | Increased slightly from 34% due to COVID workforce exit; Lakshmir Bhandar (Apr 2021) targets female non-workers |
| Student | 11.00 | E | Stable; some COVID disruption in 2020-21 academic year |
| Unemployed | 9.00 | E | Slight increase due to COVID economic disruption; educated job-seekers in district HQ |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 17.00 | A | CDB I 2011 cultivators 18.68%; Muni dilution; stable from 2019 |
| Agricultural_labourer | 28.00 | A | CDB I 2011: 34.39%; Muni dilution; tea-plucking; stable |
| Household_industry | 2.00 | A | CDB I 2011: 1.11%; stable |
| Manufacturing | 5.00 | E | Timber, minor processing; Alipurduar town; stable |
| Construction | 7.00 | E | District HQ construction; migrant workers; stable |
| Trade_retail | 10.00 | E | Alipurduar town trading hub; stable |
| Transport_logistics | 7.00 | E | Forest road, timber, NH27, Alipurduar RJN goods handling; stable |
| Services | 10.00 | E | Private services in district HQ; stable |
| Government_services_teachers | 8.00 | E | District headquarters with government offices; teachers; stable |
| Out_migrant_worker | 6.00 | D | Tea-belt Adivasi out-migration; COVID return then re-migration by late 2021 |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.00 | E | Census B-04 WB rural pattern; stable |
| Employee | 38.00 | E | Tea-garden permanent workers + govt + organised service; stable |
| Single_worker | 38.00 | E | Own-account cultivator + small trader + artisan; stable |
| Family_worker | 22.00 | E | Within agri-household; tea-plucking family labour; stable |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 29.00 | C | 2019 baseline 28%; COVID-19 pushed some near-poor households below poverty line; tea-belt districts higher BPL; ~29% by end-2021 |
| Above_Poverty_Line_low_income | 35.00 | E | Low-income daily-wage and tea-worker households; stable |
| Lower_middle | 22.00 | E | Small traders, lower-grade government employees |
| Middle | 11.00 | E | District HQ service class; slight reduction due to COVID job losses |
| Upper_middle_well_off | 3.00 | E | Small professional/business class in Alipurduar town; stable |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Alipurduar_Municipality | 32.00 | E | Electorate share estimated from 2021 AE roll; urban core; stable from 2019 |
| U2_CDB_rural_tea_garden | 68.00 | E | GPs of Alipurduar I and II CDBs; larger rural-and-tea-garden voter block |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | Slightly higher than WB average; tea-belt larger households; stable from 2019 |
| Nuclear_HH | 65.00 | E | NFHS-4/5 WB rural pattern; tea-garden worker households tend nuclear; stable |
| Joint_HH | 27.00 | E | Stable |
| Extended_multi_generation | 8.00 | E | Larger in Adivasi community households; stable |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 27.00 | E | Consistent with age pyramid; NFHS-5 Jalpaiguri women married before 18 dropped to 18.7% (from 34.5% NFHS-4) suggesting delayed marriage trend |
| Currently_married | 64.00 | E | High early-marriage rate in tea-belt communities; stable |
| Widowed | 7.50 | E | Slightly higher in female-dominated older cohort |
| Separated_divorced | 1.50 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 74.00 | C | 2019: 72%; TV growth slowing as smartphones replace; NFHS-5 WB improvement pattern; ~74% by 2021 |
| Radio | 7.00 | C | Slight decline from 8% (2019); radio still used in tea gardens but dropping |
| Mobile_phone | 90.00 | C | 2019: 85%; COVID-19 boosted mobile adoption for welfare payments, Duare Sarkar; ~90% by 2021 |
| Smartphone_with_internet | 65.00 | C | 2019: 42%; COVID-19 surge: +20pp+ post-lockdown (Jio, work-from-home, government welfare apps); Dooars lower than urban WB but significant jump; ~65% by end-2021 |
| Computer | 9.00 | C | Slight increase from 8%; stable |
| Two_wheeler | 28.00 | C | Stable from 2019; limited income growth in COVID period |
| Four_wheeler | 5.00 | C | Stable; limited to service-class |
| Banking_access | 92.00 | B | 2019: 85%; PMJDY + Lakshmir Bhandar bank-account requirement (Apr 2021) drove further adoption; tea-estate workers; ~92% by end-2021 |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 92.00 | C | NFHS-5 Jalpaiguri (proxy): 95.2%; 2019 baseline 88%; significant improvement; ~92% by 2021 for AC |
| Improved_sanitation | 70.00 | C | NFHS-5 Jalpaiguri (proxy): 73.2%; 2019 baseline 65%; Swachh Bharat continued; ~70% by 2021 |
| LPG_clean_cooking_fuel | 43.00 | C | NFHS-5 Jalpaiguri (proxy): 42.7%; 2019 baseline 40%; Ujjwala scheme continued; ~43% by 2021 |
| Wood_biomass_fuel | 49.00 | C | Declining as LPG rises from 52% (2019) |
| Other_fuel | 8.00 | C | Kerosene and coal residual; stable in tea garden worker quarters |
| Electricity | 97.00 | A | NFHS-5 Jalpaiguri (proxy): 97.4%; near-saturation confirmed; Saubhagya + Saubhagya II rollout |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 70.00 | D | Dooars deep-rooted Rajbanshi and tea-garden Adivasi communities; stable |
| WB_other_district | 8.00 | D | Jalpaiguri, Cooch Behar, plains Bengal in-migrants; stable |
| Other_Indian_state | 6.00 | D | Bihar/UP migrant workers; Assam-origin Adivasi; Jharkhand tea-belt origin workers; COVID return-migration then re-migration by late 2021 |
| Bangladesh_origin | 4.00 | D | Post-partition Hindu Bengali migrants; smaller than eastern border districts; stable |
| Outside_India | 0.50 | E | Negligible; Nepal/Bhutan origin in border fringe |
| Out_migrant | 4.00 | E | Tea-belt young men working in Assam, other states; COVID disrupted but largely restored by end-2021 |
| Jharkhand_origin | 7.50 | D | Tea-garden Adivasi (Oraon, Munda) multi-generational settlers from Jharkhand tribal belt |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Sadri | Rajbongshi | Kurukh | Boro | Nepali | Mundari | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 73.00 | 5.50 | 0.10 | 0.40 | 5.00 | 9.50 | 1.50 | 2.80 | 1.70 | 0.50 | E | Rajbanshi-Hindu concentration; Bengali urban Hindu; unchanged from 2019 |
| Muslim | 90.00 | 3.00 | 5.00 | 1.00 | 0.50 | 0.50 | 0.00 | 0.00 | 0.00 | 0.00 | E | Bengali-Muslim majority; stable |
| Christian | 15.00 | 3.00 | 0.00 | 2.00 | 40.00 | 2.00 | 25.00 | 3.00 | 5.00 | 5.00 | E | Tea-garden Adivasi Christians predominantly Sadri/Kurukh speakers; stable |
| Sarna_ORP | 10.00 | 2.00 | 0.00 | 1.00 | 50.00 | 3.00 | 25.00 | 2.00 | 2.00 | 5.00 | E | Sarna practitioners mostly Oraon/Munda; stable |
| Other_residual | 30.00 | 20.00 | 0.00 | 25.00 | 5.00 | 5.00 | 0.00 | 5.00 | 15.00 | 0.00 | E | Buddhist Bhutia/Nepali; Sikh; mixed residual |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. **2D canonical layout.**

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 43.50 | 3.50 | 4.52 | 5.65 | 42.83 | 0 | 0 | E | SC 40%/Hindu 88.3%×pop-weight; residual to Other_Hindu_middle; rows sum ~100; stable from 2019 |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident; tea-garden Christian mostly ST-background |
| Sarna_ORP | 0 | 92 | 0 | 5 | 3 | 0 | 0 | E | Sarna practitioners predominantly from ST communities |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Jharkhand_origin | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 72.00 | 8.00 | 4.00 | 5.50 | 0.50 | 4.00 | 6.00 | D | Hindu includes Rajbanshi natives + Bengali migrants; Bangladesh origin is Hindu-dominant; stable |
| Muslim | 82.00 | 8.00 | 3.00 | 5.00 | 0.00 | 2.00 | 0.00 | E | Mostly native Dooars Muslim; stable |
| Christian | 55.00 | 4.00 | 12.00 | 0.00 | 0.00 | 6.00 | 23.00 | E | Tea-garden Adivasi Christians; Jharkhand-origin heavily represented; stable |
| Sarna_ORP | 50.00 | 3.00 | 10.00 | 0.00 | 0.00 | 8.00 | 29.00 | E | Sarna practitioners have Jharkhand-origin heritage from tea-belt migration |
| Other_residual | 35.00 | 15.00 | 25.00 | 2.00 | 15.00 | 8.00 | 0.00 | E | Bhutia/Nepali/Sikh diverse migration pattern |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 78.00 | 70.00 | 95.00 | C | Higher urban Hindu access; Lakshmir Bhandar bank-account requirement boosted Hindu female banking; COVID smartphone surge |
| Muslim | 67.00 | 58.00 | 86.00 | C | NFHS-5 WB religion gap pattern; smartphone gap narrowing with Jio |
| Christian | 62.00 | 52.00 | 90.00 | C | Tea-garden estate banking access; COVID smartphone adoption among tea workers |
| Sarna_ORP | 57.00 | 45.00 | 84.00 | C | Lowest access but COVID pushed smartphone adoption even in remote areas |
| Other_residual | 82.00 | 72.00 | 95.00 | E | Smaller, largely urban/professional Bhutia/Sikh residual |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4.00 | 7.00 | 12.00 | 17.00 | 21.00 | 27.00 | 12.00 | E |
| SC_total | 17.00 | 25.00 | 22.00 | 18.00 | 10.00 | 7.00 | 1.00 | E |
| ST_total | 26.00 | 28.00 | 21.00 | 14.00 | 7.00 | 3.00 | 1.00 | E |
| OBC | 14.00 | 22.00 | 22.00 | 19.00 | 12.00 | 9.00 | 2.00 | E |
| Other_Hindu_middle | 15.00 | 23.00 | 22.00 | 19.00 | 12.00 | 7.00 | 2.00 | E |
| Muslim | 21.00 | 26.00 | 22.00 | 17.00 | 9.00 | 4.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender). **5-year cohorts.**

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 15.00 | 13.00 | E |
| 23_27 | 14.00 | 11.00 | E |
| 28_32 | 12.00 | 9.00 | E |
| 33_37 | 10.00 | 7.00 | E |
| 38_42 | 9.00 | 5.00 | E |
| 43_47 | 8.00 | 4.00 | E |
| 48_52 | 7.00 | 3.00 | E |
| 53_57 | 5.50 | 2.50 | E |
| 58_62 | 4.50 | 2.00 | E |
| 63_67 | 3.50 | 1.50 | E |
| 68 | 3.00 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender). **5-year cohorts.**

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8.00 | 28.00 | E |
| 23_27 | 42.00 | 80.00 | E |
| 28_32 | 82.00 | 92.00 | E |
| 33_37 | 93.00 | 90.00 | E |
| 38_42 | 94.00 | 88.00 | E |
| 43_47 | 93.00 | 84.00 | E |
| 48_52 | 91.00 | 78.00 | E |
| 53_57 | 89.00 | 70.00 | E |
| 58_62 | 87.00 | 60.00 | E |
| 63_67 | 82.00 | 45.00 | E |
| 68 | 75.00 | 30.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 48.00 | 68.00 | C | +18pp smartphone surge from COVID; rural ag lower baseline but significant jump |
| Agricultural_labourer | 38.00 | 58.00 | C | Tea-plucking labour; COVID-era welfare payment apps drove adoption |
| Household_industry | 55.00 | 70.00 | C | |
| Manufacturing | 62.00 | 77.00 | C | |
| Construction | 58.00 | 72.00 | C | |
| Trade_retail | 80.00 | 90.00 | C | Alipurduar town traders; near-saturation |
| Transport_logistics | 75.00 | 82.00 | C | |
| Services | 85.00 | 92.00 | C | |
| Government_services_teachers | 95.00 | 97.00 | C | Highest; near-saturation |
| Out_migrant_worker | 82.00 | 76.00 | D | Working outside; smartphone-dependent for remittances; COVID-era adoption |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 31.00 | 2.00 | E |
| Primary | 35.00 | 3.00 | E |
| Middle | 33.00 | 5.00 | E |
| Secondary | 27.00 | 11.00 | E |
| Higher_Secondary | 21.00 | 16.00 | E |
| Graduate | 25.00 | 19.00 | E |
| Postgraduate | 37.00 | 13.00 | E |

### D.10 Asset × Bilingualism

| Asset_group | Bilingual_rate | Tier | Source |
|---|---|---|---|
| TV_only_HH | 5.00 | E | Bengali TV dominant; no change from 2019 |
| TV_and_smartphone_HH | 10.00 | E | YouTube cross-language; slight increase |
| Smartphone_only_HH | 9.00 | E | |
| No_asset_HH | 3.00 | E | Lowest exposure |

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Sub-unit codes use `Un_` prefix matching C.11.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Alipurduar_Municipality | 91.00 | 6.50 | 1.50 | 0.30 | 0.70 | E | Municipality census 2011: Hindu-dominant urban; lower Adivasi/Christian relative to rural GPs; stable |
| U2_CDB_rural_tea_garden | 87.30 | 6.20 | 4.30 | 1.60 | 0.60 | E | Rural GPs with tea gardens; higher Christian + Sarna_ORP from Adivasi workers; marginal religion-shift update |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Use canonical caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Alipurduar_Municipality | 8.00 | 18.00 | 1.00 | 6.00 | 58.50 | 6.50 | 2.00 | E |
| U2_CDB_rural_tea_garden | 2.00 | 49.00 | 12.00 | 4.50 | 15.00 | 6.20 | 11.30 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Alipurduar_Municipality | 91.00 | 82.00 | 20.00 | 97.00 | C |
| U2_CDB_rural_tea_garden | 65.00 | 57.00 | 5.00 | 90.00 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Alipurduar_Municipality | 74.00 | 89.00 | 96.00 | 99.00 | C |
| U2_CDB_rural_tea_garden | 28.00 | 59.00 | 90.00 | 96.00 | C |

### D.15 Vote × Religion (2021 AE anchor)

P(party ‖ religion) — anchored on 2021 WB Assembly Election AC 012 result (BJP 48.19%, AITC 41.00%, INC 7.03%); CSDS-Lokniti post-poll 2021 WB regional rollup.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 56.00 | 35.00 | 4.00 | 0.50 | 4.50 | C | BJP-lean maintained among Rajbanshi SC Hindu; Dooars Hindu BJP surge from 2019 slightly moderated; CSDS 2021 WB pattern |
| Muslim | 4.00 | 65.00 | 25.00 | 4.00 | 2.00 | C | Muslim consolidation behind AITC in 2021 AE; INC retained some Muslim vote in this seat (INC got 7% total); LF residual from RSP base now tiny |
| Christian | 30.00 | 48.00 | 8.00 | 0.50 | 13.50 | E | Tea-garden Christian: AITC-lean in 2021 AE; BJP also competing; John Barla (BJP Christian) effect; IND candidates got notable share |
| Sarna_ORP | 35.00 | 46.00 | 5.00 | 0.50 | 13.50 | E | Adivasi Sarna: AITC-lean in 2021 relative to 2019 LS; IND candidate share |
| Other_residual | 42.00 | 38.00 | 5.00 | 0.50 | 14.50 | E | Mixed residual |

### D.16 Vote × Caste (2021 AE)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 58.00 | 30.00 | 5.00 | 0.50 | 6.50 | C | CSDS 2021 WB bhadralok BJP-lean; marginally less than 2019 |
| OBC | 50.00 | 38.00 | 5.00 | 0.50 | 6.50 | C | Rajbongshi OBC BJP-leaning; stable |
| SC_total | 55.00 | 36.00 | 3.00 | 0.50 | 5.50 | C | Rajbanshi SC BJP swing maintained in 2021 AE; CSDS pattern |
| ST_total | 40.00 | 40.00 | 8.00 | 0.50 | 11.50 | C | Tea-garden ST divided; BJP-AITC split; IND candidates drew some ST vote |
| Other_Hindu_middle | 52.00 | 39.00 | 3.50 | 0.50 | 5.00 | E | Dooars Hindu middle-caste BJP lean; slightly moderated from 2019 |
| Muslim | 4.00 | 65.00 | 25.00 | 4.00 | 2.00 | C | Same as D.15 |

### D.17 Vote × Gender (2021 AE, post-Lakshmir Bhandar launch)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 53.00 | 37.00 | 5.00 | 0.50 | 4.50 | C | CSDS 2021 WB; male BJP-lean; slightly moderated from 2019 |
| Female | 44.00 | 45.00 | 9.00 | 0.50 | 1.50 | C | CSDS 2021; Lakshmir Bhandar launched Apr 2021 (₹500/month GEN, ₹1000 SC/ST) boosted female AITC vote; INC also benefited from female vote in this Dooars seat |

### D.18 Vote × Welfare-scheme exposure (2021)

> AC 012 does not have a declared welfare_exposure marginal axis in v0. Section omitted per NORMALIZED_SCHEMA §4.7.

---

## E. 2021 baseline vote (calibration target)

**2021 WB Assembly Election — AC 012 Alipurduars. Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 48.19 | A | ECI 2021 AE: Suman Kanjilal 107,333 / 222,732 valid votes; data/electoral_history/2021/detailed_results.csv |
| AITC | 41.00 | A | ECI 2021 AE: Sourav Chakraborty (Ghutis) 91,326 / 222,732 |
| INC | 7.03 | A | ECI 2021 AE: Deba Prasad Roy 15,651 / 222,732 |
| LF | 0.50 | A | ECI 2021 AE: SUCI(C) Pijush Kanti Sarma 1,111 / 222,732; no RSP/CPI(M) candidate stood |
| Other_NOTA | 3.28 | A | ECI 2021 AE: IND (2,351+1,393+696+620+270) + NOTA (1,981) = 7,311 / 222,732 |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 012 Alipurduars (Assembly Elections)

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin |
|---|---|---|---|---|---|---|---|---|---|
| 1977 AE | Nani Bhattacharya | RSP | — | — | — | — | — | — | RSP began 30-yr run |
| 1987 AE | Nani Bhattacharya | RSP | — | — | — | — | — | — | RSP 3rd consecutive win |
| 1991 AE | Nirmal Das | RSP | — | — | — | — | — | — | RSP continued dominance |
| 2006 AE | Nirmal Das | RSP | — | — | — | — | — | — | RSP 4th consecutive Nirmal Das win; Left Front fortress |
| 2011 AE | Debaprasad Roy (Mithu) | INC | ~79,605 | — | Kshiti Goswami | RSP | ~72,822 | — | 6,783; INC broke RSP after 34 yrs; anti-Left wave |
| 2016 AE | Sourav Chakraborty | AITC | 89,695 | — | Biswa Ranjan Sarkar | INC | 77,737 | — | ~11,958; TMC swept Dooars |

**Narrative notes 2019–2021:**
- 2019 LS John Barla (BJP, Christian Adivasi) won Alipurduars PC with a massive margin; AC 012 BJP segment 55.11% — a striking anti-incumbency swing away from the prior AITC consolidation.
- 2021 AE: BJP retained Alipurduars AC with Suman Kanjilal defeating AITC's Sourav Chakraborty (who had held the seat in 2016); margin 16,007 votes. INC's Deba Prasad Roy — the 2011 INC winner — came third with 7.03%, suggesting INC retained a Dooars-specific legacy vote distinct from the state pattern.
- COVID-19 lockdown (Mar 2020): tea-garden closures hurt Adivasi worker livelihoods; reverse migration from Assam/other states; government relief vis-a-vis AITC "Duare Sarkar" camps.
- Lakshmir Bhandar (Apr 2021): ₹500/month for GEN women HH heads, ₹1000 SC/ST — a late-campaign welfare promise that reached female voters before the May 2021 count.
- BSF 50km jurisdiction extension (Oct 2021): post-AE; known by end-2021 but no electoral effect yet.

### Alipurduars Lok Sabha (PC 2) historical

| Year | Winner | Party | Votes | % | Notes |
|---|---|---|---|---|---|
| 2014 LS | Dasrath Tirkey | AITC | — | ~36% | AITC won; Left weakened; BJP nascent |
| 2019 LS | John Barla | BJP | 750,804 | ~54.4% of LS | BJP surge; AITC Dasrath Tirkey 506,815; margin 243,989 — massive swing; John Barla is Christian Adivasi from tea-belt |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- `data/electoral_history/2021/detailed_results.csv` — ECI 2021 WB AE candidate-level results; AC 12 complete: BJP 107,333 / AITC 91,326 / INC 15,651 / SUCI 1,111 / NOTA 1,981; electorate 260,652
- Census of India 2011 — Alipurduar I CD block (Primary Census Abstract; Wikipedia "Alipurduar I" article)
- Census of India 2011 — Alipurduar II CD block (Wikipedia "Alipurduar II" article)
- Census of India 2011 — Alipurduar Municipality (census2011.co.in/data/town/801642)
- Delimitation Commission of India 2008 — WB Schedule (AC 012 composition)
- ECI — 2011 AE, 2016 AE results for AC 012

### Secondary sources (tier B/C)
- NFHS-5 (2019-21) West Bengal — `data/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv`; Jalpaiguri district used as proxy for Alipurduar (Alipurduar not separately tabulated); key: electricity 97.4%, improved water 95.2%, sanitation 73.2%, LPG 42.7%
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership 2019 baseline
- CSDS-Lokniti 2021 WB post-poll — vote × demographic conditionals (WB regional rollup applied to Dooars)
- PMJDY dashboard — banking access post-Lakshmir Bhandar (Apr 2021) bank-account requirement

### Tertiary / journalistic (tier D)
- Elections.in / MyNeta — 2021 AE Alipurduars constituency result confirmation
- Journalistic coverage of Dooars Adivasi political alignment 2021 AE; John Barla BJP Christian effect
- ECI 2019 LS AC-segment form-20 data (2019 calibration file confirms tier A: BJP 55.11%, AITC 37.35%)
- electionsguru.in — Alipurduars AC election history 1977–2021

### Tier-D/E reliance flags (what to distrust)
- **Smartphone penetration** (C.14): +23pp jump from 2019 to 2021 — large modeled change; relies on COVID-era adoption narrative; could be +20pp or +25pp; tier C with high uncertainty
- **Banking access** (C.14): +7pp from 2019 to 2021; Lakshmir Bhandar bank-account requirement is a credible driver but exact AC-level penetration not measured; tier B
- **Mother tongue shares** (C.5): multiple language groups; AC-level Census language data not directly available; sub-extrapolation needed
- **Sub-unit population split** (C.11): v0 uses 2 sub-units; exact electorate split between Municipality and rural GPs not verified against 2021 ECI roll breakdown
- **Caste sub-group shares** (C.2, D.2): no caste census post-1931 for non-SC/ST; Rajbanshi SC shares tier C from CSDS/academic sources
- **Vote × demographic** (D.15–D.17): CSDS 2021 WB regional rollup + Dooars-specific adjustments; tier C; row×column marginal-recovery not independently verified for this AC
- **Migration shares** (C.16, D.3): no AC-level Census D-series; tier D from journalistic and block-level patterns

### v0 known gaps
1. DCHB Alipurduar Part-A — v0 collapses 13 GPs into 2 sub-units; refine when DCHB available
2. NFHS-5 Alipurduar district not separately tabulated; Jalpaiguri used as proxy; some indicator drift possible
3. Smartphone/banking 2021 exact penetration: COVID-era surge modeled; no sub-AC survey available
4. Tea-garden worker population: no public estate-level census; tier E estimate unchanged
5. CSDS 2021 WB AE post-poll detailed cross-tabs: using summary pattern; full cross-tabs not available in data/

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No post-2021 events referenced.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2024 Lok Sabha Election — AC 012 segment within Alipurduars LS (PC 2) (tier A, CSV)

> Figures below are tier A — sourced from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=12, Alipurduars. Total candidate votes: 214,114; electorate 268,670; turnout ~79.7%.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Manoj Tigga | 114,821 | 53.63% | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Prakash Chik Baraik | 86,257 | 40.29% | A | Same |
| RSP | Mili Oraon | 7,266 | 3.39% | A | Same |
| SUCI | Chandan Oraon | 430 | 0.20% | A | Same |
| Others (BSP, KPPU, KMSP, GNASURKP, NBNGPLPP, IND×2) | various | 5,340 | 2.49% | A | Same |
| **BJP margin over AITC** | | **28,564 votes** | **13.34 pp** | A | Computed |

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC segment shares within ±3pp:
- BJP target: 53.6% ± 3pp
- AITC target: 40.3% ± 3pp
- LF (RSP+SUCI) target: 3.6% ± 2pp
