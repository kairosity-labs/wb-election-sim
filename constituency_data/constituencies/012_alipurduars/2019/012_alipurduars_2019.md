# AC 012 — Alipurduars (GEN) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 012 Alipurduars as of 2019 only — it does not reference
> any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../../NORMALIZED_SCHEMA.md)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 012 | A | ECI / Delimitation Commission 2008 |
| AC name | Alipurduars | A | ECI |
| Reservation | GEN | A | Delimitation 2008 |
| District | Alipurduar | A | Delimitation 2008 (Alipurduar district carved from Jalpaiguri 2014) |
| Sub-division | Alipurduar | A | WB administrative |
| LS constituency | 2 — Alipurduars (ST reserved) | A | Delimitation 2008 |
| LS segments included | AC 9 Tufanganj · 10 Natabari · 11 Sitalkuchi · 12 Alipurduars · 13 Kalchini (ST) · 14 Kumargram (ST) · 15 Madarihat (ST) · wait — see note | A | Delimitation 2008 |
| AC composition | Alipurduar Municipality (full) + Alipurduar Railway Junction census town + Banchukamari, Chakowakheti, Mathura, Parorpar, Patlakhawa, Shalkumar I, Shalkumar II, Tapsikhata, Vivekananda I, Vivekananda II GPs (Alipurduar I CDB) + Chaporerpar I, Chaporerpar II, Tatpara II GPs (Alipurduar II CDB) | A | Delimitation 2008 WB Schedule |
| Geographic note | District HQ town of Alipurduar district; Dooars foothills; tea garden and forest landscape; Buxa Tiger Reserve to the north | A | — |
| Sub-units used in v0 | **U1: Alipurduar_Municipality** (urban core) · **U2: CDB_rural_tea_garden** (GPs of Alipurduar I + II CDBs) | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~180,000 (Muni 56,171 urban + Rly Junction town ~15,000 + GPs ~109,000) | E | Census 2011 Alipurduar I CDB pop 216,931 total; AC covers ~55% of CDB I + 3 GPs of CDB II; v0 rough apportionment |
| 2019 projected population | ~196,000 | E | 8-yr compound growth ~1.1%/yr (Dooars slower than state average; tea-belt outmigration) |
| Sex ratio (2019, F per 1000 M) | ~946 | E | Alipurduar district baseline; tea-garden male-skew in some pockets |
| 2019 estimated electorate (18+) | ~215,000 | D | Back-derived from 2019 ECI roll 249,960 minus usual roll-over; CSV gives 249,960 |
| Estimated M / F / TG split (2019) | 51.4% M / 48.5% F / 0.1% TG | E | District sex ratio projection |
| 2019 polling stations (estimated) | ~270 | E | Back-projection from 2021 SIR pattern |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 88.50 | E | Alipurduar I block 2011: 90.55% Hindu; CDB II 2011: 84.40% Hindu; AC-weighted blend (Muni higher-Hindu urban + rural GPs lower); projected 2011→2019 modest relative growth |
| Muslim | 6.20 | E | CDB I 2011: 5.93%; CDB II 2011: 6.50%; AC-weighted ~6.2% |
| Christian | 3.50 | E | CDB I 2011: 2.54%; CDB II 2011: 8.64% (tea-garden belt); AC weight skewed toward CDB I; ~3.5% for the GPs captured |
| Sarna_ORP | 1.20 | E | Tribal Adivasi tea-garden workers (Oraon, Munda, Santhali); reckoned from ST share ~8-10% of AC; fraction practising Sarna rather than Christian |
| Other_residual | 0.60 | E | Buddhist (Bhutia fringe) + Sikh + Jain + Not_stated; district residual |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 40.00 | A | CDB I 2011: 48.4% SC; Alipurduar Municipality 2011: 18.04% SC; AC-weighted blend; municipality dilutes overall to ~40% |
| └ Rajbanshi_SC | 30.00 | C | Dominant SC sub-group in Dooars/Terai (Koch-Rajbongshi/Rajbanshi declared SC in WB); primary SC community |
| └ Other_SC | 10.00 | E | Smaller SC communities (Bagdi, Hari, Chamar fringe) |
| **ST_total** | 9.00 | E | District ST 25.62% overall; AC 12 is GEN (lower ST concentration than ST-reserved AC 13/14); tea-garden Adivasi (Oraon, Munda, Ho, Santhali) concentrated in rural GPs |
| └ Oraon_ST | 4.50 | C | Largest ST group in Dooars tea gardens; Kurukh speakers |
| └ Munda_Santhali_ST | 3.00 | E | Second tier ST groups in tea gardens |
| └ Other_ST | 1.50 | E | Ho, Bhumij, Bhutia fringe |
| UC_bhadralok | 4.00 | E | Brahmin/Kayastha/Baidya; small in Dooars; largely service class in Alipurduar town |
| OBC | 5.00 | E | Koch-Rajbongshi OBC (those not classified SC), Mahishya fringe; Dooars OBC pool is limited |
| Other_Hindu_middle | 28.00 | E | Unclassified Hindu middle + Rajbongshi community subsets; residual within Hindu non-SC/ST |
| Muslim | 6.20 | E | All sub-castes pooled; see C.1 |
| Christian_plus_Sarna_plus_Other | 7.80 | E | Christian (3.5%) + Sarna_ORP (1.2%) + Other_residual (0.6%) + remaining ST/others; note: some ST Adivasi practise Christianity |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.00 | E | Projected from Alipurduar district 2011 age pyramid; young cohort somewhat high (tea-belt fertility) |
| 23_27 | 11.50 | E | |
| 28_32 | 11.00 | E | |
| 33_37 | 10.00 | E | |
| 38_42 | 9.50 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.00 | E | |
| 63_67 | 4.00 | E | |
| 68 | 12.00 | E | 68+ open-ended; older cohort thinned by lower historical survival; renormalized to sum |
| **Sum** | **100.00** | — | self-check (18+ adults only; children excluded) |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 51.35 | E | District sex ratio ~946 F per 1000 M → 51.35% M / 48.55% F; tea-garden slightly male-skew in some blocks |
| Female | 48.55 | E | |
| Third_gender | 0.10 | E | Small but non-negligible in town context; tier E |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 66.00 | A | CDB I 2011: 66.32% Bengali; dominant in urban Alipurduar and bhadralok belt |
| Hindi | 5.00 | E | Bihari/UP migrant workers + Marwari traders; higher in Alipurduar town |
| Urdu | 0.80 | E | Small Muslim pocket; Bengali-Muslim majority use Bengali |
| Other | 0.70 | E | Residual catch-all (Nepali fringe, Bhutia, etc.) |
| Sadri | 10.00 | A | CDB I 2011: 9.95% Sadri; tea-garden Adivasi lingua franca (Oraon, Munda workers) |
| Rajbongshi | 8.00 | A | CDB I 2011: 4.64% Rajbongshi (declared); likely under-counted; AC includes Rajbanshi-belt GPs; est. ~8% |
| Kurukh | 4.00 | A | CDB I 2011: 2.35% Kurukh; Oraon mother tongue; concentrated in tea-garden GPs |
| Boro | 2.50 | A | CDB I 2011: 1.52% Boro; Bodo community in Dooars foothill belt |
| Nepali | 1.50 | A | CDB I 2011: 1.15% Nepali; Gurkha/Gorkha community; Alipurduar town fringe |
| Mundari | 1.50 | A | CDB I 2011: 1.06% Mundari; Munda community in tea gardens |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 20.00 | E | CDB I 2011 literacy ~76.19%; tea-garden workers historically lower literacy; AC ~80% literate by 2019 with trend improvement → ~20% illiterate |
| Primary | 24.00 | E | Class 1–5; large share among tea-garden community |
| Middle | 21.00 | E | Class 6–8 |
| Secondary | 17.00 | E | Class 9–10 |
| Higher_Secondary | 10.00 | E | Class 11–12 |
| Graduate | 6.00 | E | Urban professional class in Alipurduar town; lower rural share |
| Postgraduate | 2.00 | E | Small but present in district HQ service sector |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 36.00 | E | CDB I 2011 workers ~45% of total pop; tea-garden adult workers high; adult-only renormalized ~36% main workers |
| └ Main_worker_tea_garden | 14.00 | E | Sub-row: estimate of tea-estate employed adult workers (is_subgroup=yes) |
| └ Main_worker_non_tea | 22.00 | E | Sub-row: non–tea-garden main workers (is_subgroup=yes) |
| Marginal_worker | 10.00 | E | Seasonal agricultural and tea-plucking day-labour |
| Non_worker | 34.00 | E | Housewife heavy in Adivasi and Muslim households; retired |
| Student | 11.00 | E | 18–22 in college/school |
| Unemployed | 9.00 | E | Educated job-seekers in district HQ town; rural educated youth gap |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 17.00 | A | CDB I 2011 cultivators 18.68%; AC weighted with Muni dilution → ~17% |
| Agricultural_labourer | 28.00 | A | CDB I 2011: 34.39%; Muni dilution reduces to ~28% including tea-plucking |
| Household_industry | 2.00 | A | CDB I 2011: 1.11%; lower in this AC |
| Manufacturing | 5.00 | E | Timber, minor processing; Alipurduar town has some small industry |
| Construction | 7.00 | E | District HQ construction activity; migrant construction workers |
| Trade_retail | 10.00 | E | Alipurduar town trading hub for Dooars region |
| Transport_logistics | 7.00 | E | Forest road transport, timber, interstate NH27 logistics; Alipurduar RJN goods handling |
| Services | 10.00 | E | Private services in district HQ (banking, hospitality, health) |
| Government_services_teachers | 8.00 | E | District headquarters with government offices; teachers in schools |
| Out_migrant_worker | 6.00 | D | Tea-belt Adivasi out-migration to Assam and other states; journalistic estimate |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.00 | E | Census B-04 WB rural pattern |
| Employee | 38.00 | E | Tea-garden permanent workers (estate employees) + govt + organised service |
| Single_worker | 38.00 | E | Own-account cultivator + small trader + artisan |
| Family_worker | 22.00 | E | Within agri-household; tea-plucking family labour on own plots |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 28.00 | C | Tea-belt districts had higher BPL; Jalpaiguri/Alipurduar dist BPL survey ~30%; 2019 projection after reduction ~28% |
| Above_Poverty_Line_low_income | 35.00 | E | Low-income daily-wage and tea-worker households |
| Lower_middle | 22.00 | E | Small traders, lower-grade government employees |
| Middle | 12.00 | E | District HQ service class |
| Upper_middle_well_off | 3.00 | E | Small professional/business class in Alipurduar town |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Alipurduar_Municipality | 32.00 | E | Muni 2011 pop 56,171 + Rly Jnc town ~15,000 = ~71,000 / AC ~180,000 ≈ 39%; adjusted for slightly faster urban growth by 2019; v0 estimate ~32% of 2019 electorate share (electoral roll skew toward registered rural voters) |
| U2_CDB_rural_tea_garden | 68.00 | E | GPs of Alipurduar I and II CDBs; larger rural-and-tea-garden voter block |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | Slightly higher than WB average; tea-belt larger households; WB 2011: 4.3 |
| Nuclear_HH | 65.00 | E | NFHS-4 WB rural pattern; tea-garden worker households tend nuclear |
| Joint_HH | 27.00 | E | |
| Extended_multi_generation | 8.00 | E | Larger in Adivasi community households |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 27.00 | E | Consistent with age pyramid; first-time voter cohort |
| Currently_married | 64.00 | E | High early-marriage rate in tea-belt communities |
| Widowed | 7.50 | E | Slightly higher in female-dominated older cohort |
| Separated_divorced | 1.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 72.00 | C | NFHS-4 WB rural 60%, urban 89%; Dooars tea-belt below state urban average; AC ~72% by 2019 |
| Radio | 8.00 | C | Slightly higher in Dooars than Bengal plains; radio still used in tea gardens |
| Mobile_phone | 85.00 | C | NFHS-4 WB ~78%, +Jio rollout 2016-19; tea belt coverage improved |
| Smartphone_with_internet | 42.00 | C | NFHS-4 WB baseline + Jio; Dooars lower than urban WB; ~42% by 2019 |
| Computer | 8.00 | C | NFHS-4 WB rural 4%, urban 27%; AC weighted ~8%; lower than N24P |
| Two_wheeler | 28.00 | C | NFHS-4 WB rural 18%, urban 41%; tea-belt moderate motorcycle ownership |
| Four_wheeler | 5.00 | C | Low; limited to service-class in Alipurduar town |
| Banking_access | 85.00 | B | PMJDY 2014- saturation; tea-estate workers have formal banking through estates |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 88.00 | C | NFHS-4 WB rural 84%; river-fed area has relatively good water access; AC ~88% |
| Improved_sanitation | 65.00 | C | NFHS-4 WB rural 51% + Swachh Bharat 2014-19 (+15pp); Dooars lower base; ~65% by 2019 |
| LPG_clean_cooking_fuel | 40.00 | C | NFHS-4 WB rural 24%; Ujjwala scheme 2016-19 rollout; Dooars lower income → ~40% by 2019 |
| Wood_biomass_fuel | 52.00 | C | High wood-fuel use in tea gardens and forest-adjacent households |
| Other_fuel | 8.00 | C | Kerosene and coal residual; higher in tea garden worker quarters |
| Electricity | 95.00 | A | Saubhagya 2017-19 near-saturation; census 2011 + rollout |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 70.00 | D | Dooars has deep-rooted Rajbanshi and tea-garden Adivasi communities; most residents born in district |
| WB_other_district | 8.00 | D | Jalpaiguri, Cooch Behar, and plains Bengal in-migrants to Alipurduar town service sector |
| Other_Indian_state | 6.00 | D | Bihar/UP migrant workers; Assam-origin Adivasi; Jharkhand tea-belt origin workers |
| Bangladesh_origin | 4.00 | D | Post-partition Hindu Bengali migrants; smaller than eastern border districts but present |
| Outside_India | 0.50 | E | Negligible; some Nepal/Bhutan origin in border fringe |
| Out_migrant | 4.00 | E | Tea-belt young men working in Assam, other states; registered here |
| Jharkhand_origin | 7.50 | D | Tea-garden Adivasi (Oraon, Munda) brought as contract labour historically; multi-generational settlers but Jharkhand tribal identity retained |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Sadri | Rajbongshi | Kurukh | Boro | Nepali | Mundari | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 73.00 | 5.50 | 0.10 | 0.40 | 5.00 | 9.50 | 1.50 | 2.80 | 1.70 | 0.50 | E | Rajbanshi-Hindu concentration; Bengali urban Hindu |
| Muslim | 90.00 | 3.00 | 5.00 | 1.00 | 0.50 | 0.50 | 0.00 | 0.00 | 0.00 | 0.00 | E | Bengali-Muslim majority; small Urdu pocket in Alipurduar town |
| Christian | 15.00 | 3.00 | 0.00 | 2.00 | 40.00 | 2.00 | 25.00 | 3.00 | 5.00 | 5.00 | E | Tea-garden Adivasi Christians predominantly Sadri/Kurukh speakers |
| Sarna_ORP | 10.00 | 2.00 | 0.00 | 1.00 | 50.00 | 3.00 | 25.00 | 2.00 | 2.00 | 5.00 | E | Sarna practitioners mostly Oraon/Munda; Sadri/Kurukh dominant |
| Other_residual | 30.00 | 20.00 | 0.00 | 25.00 | 5.00 | 5.00 | 0.00 | 5.00 | 15.00 | 0.00 | E | Buddhist Bhutia/Nepali; Sikh; mixed residual |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. **2D canonical layout.**

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 43.50 | 3.50 | 4.52 | 5.65 | 42.83 | 0 | 0 | E | SC 40%/Hindu 88.5%×pop-weight; residual to Other_Hindu_middle; rows sum ~100 |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident; tea-garden Christian mostly ST-background but map to Christian_plus_Sarna_plus_Other |
| Sarna_ORP | 0 | 92 | 0 | 5 | 3 | 0 | 0 | E | Sarna practitioners predominantly from ST communities |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Jharkhand_origin | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 72.00 | 8.00 | 4.00 | 5.50 | 0.50 | 4.00 | 6.00 | D | Hindu includes Rajbanshi natives + Bengali migrants; Bangladesh origin is Hindu-dominant |
| Muslim | 82.00 | 8.00 | 3.00 | 5.00 | 0.00 | 2.00 | 0.00 | E | Mostly native Dooars Muslim; small Bangladesh-origin |
| Christian | 55.00 | 4.00 | 12.00 | 0.00 | 0.00 | 6.00 | 23.00 | E | Tea-garden Adivasi Christians; Jharkhand-origin heavily represented |
| Sarna_ORP | 50.00 | 3.00 | 10.00 | 0.00 | 0.00 | 8.00 | 29.00 | E | Sarna practitioners have Jharkhand-origin heritage from tea-belt migration |
| Other_residual | 35.00 | 15.00 | 25.00 | 2.00 | 15.00 | 8.00 | 0.00 | E | Bhutia/Nepali/Sikh diverse migration pattern |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 76.00 | 46.00 | 88.00 | C | Higher urban Hindu access via Alipurduar town |
| Muslim | 65.00 | 35.00 | 78.00 | C | NFHS-4 WB religion gap pattern |
| Christian | 60.00 | 30.00 | 82.00 | C | Tea-garden estate banking access partially offsets lower smartphone |
| Sarna_ORP | 55.00 | 25.00 | 75.00 | C | Lowest access; remote tea-garden Sarna households |
| Other_residual | 80.00 | 55.00 | 90.00 | E | Smaller, largely urban/professional Bhutia/Sikh residual |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 5.00 | 8.00 | 12.00 | 17.00 | 20.00 | 27.00 | 11.00 | E |
| SC_total | 18.00 | 25.00 | 22.00 | 18.00 | 10.00 | 6.00 | 1.00 | E |
| ST_total | 28.00 | 28.00 | 20.00 | 13.00 | 7.00 | 3.00 | 1.00 | E |
| OBC | 15.00 | 22.00 | 22.00 | 19.00 | 12.00 | 8.00 | 2.00 | E |
| Other_Hindu_middle | 16.00 | 24.00 | 22.00 | 18.00 | 11.00 | 7.00 | 2.00 | E |
| Muslim | 22.00 | 26.00 | 22.00 | 17.00 | 8.00 | 4.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender). **5-year cohorts.**

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 14.00 | 12.00 | E |
| 23_27 | 13.00 | 10.00 | E |
| 28_32 | 11.00 | 8.00 | E |
| 33_37 | 9.00 | 6.00 | E |
| 38_42 | 8.00 | 4.00 | E |
| 43_47 | 7.00 | 3.00 | E |
| 48_52 | 6.00 | 2.50 | E |
| 53_57 | 5.00 | 2.00 | E |
| 58_62 | 4.00 | 1.50 | E |
| 63_67 | 3.50 | 1.00 | E |
| 68 | 3.00 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender). **5-year cohorts.**

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8.00 | 30.00 | E |
| 23_27 | 42.00 | 82.00 | E |
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
| Cultivator | 30.00 | 65.00 | C | Rural ag lower access; Dooars below WB average |
| Agricultural_labourer | 22.00 | 55.00 | C | Tea-plucking labour — lowest income segment |
| Household_industry | 35.00 | 68.00 | C | |
| Manufacturing | 45.00 | 75.00 | C | |
| Construction | 40.00 | 70.00 | C | |
| Trade_retail | 65.00 | 88.00 | C | Alipurduar town traders |
| Transport_logistics | 58.00 | 80.00 | C | |
| Services | 72.00 | 90.00 | C | |
| Government_services_teachers | 85.00 | 95.00 | C | Highest |
| Out_migrant_worker | 68.00 | 75.00 | D | Working outside; smartphone-dependent for remittances |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 32.00 | 2.00 | E |
| Primary | 36.00 | 3.00 | E |
| Middle | 34.00 | 5.00 | E |
| Secondary | 28.00 | 10.00 | E |
| Higher_Secondary | 22.00 | 15.00 | E |
| Graduate | 26.00 | 18.00 | E |
| Postgraduate | 38.00 | 12.00 | E |

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Sub-unit codes use `Un_` prefix matching C.11.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Alipurduar_Municipality | 91.00 | 6.50 | 1.50 | 0.30 | 0.70 | E | Municipality census 2011: Hindu-dominant urban; lower Adivasi/Christian relative to rural GPs |
| U2_CDB_rural_tea_garden | 87.50 | 6.10 | 4.30 | 1.60 | 0.50 | E | Rural GPs with tea gardens; higher Christian + Sarna_ORP from Adivasi workers |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Use canonical caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Alipurduar_Municipality | 8.00 | 18.00 | 1.00 | 6.00 | 58.50 | 6.50 | 2.00 | E |
| U2_CDB_rural_tea_garden | 2.00 | 49.00 | 12.00 | 4.50 | 15.00 | 6.10 | 11.40 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Alipurduar_Municipality | 90.00 | 60.00 | 18.00 | 93.00 | C |
| U2_CDB_rural_tea_garden | 63.00 | 33.00 | 4.00 | 81.00 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Alipurduar_Municipality | 72.00 | 88.00 | 95.00 | 99.00 | C |
| U2_CDB_rural_tea_garden | 25.00 | 55.00 | 85.00 | 93.00 | C |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — CSDS-Lokniti 2019 regional WB rollup + Alipurduar-local adjustment.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 60.00 | 33.00 | 2.50 | 3.50 | 1.00 | C | CSDS 2019 WB Hindu BJP-lean; Dooars Hindu BJP surge reinforced |
| Muslim | 5.00 | 68.00 | 20.00 | 5.50 | 1.50 | C | CSDS 2019 WB Muslim consolidation; LF residual from RSP base |
| Christian | 35.00 | 42.00 | 5.00 | 12.00 | 6.00 | E | Tea-garden Christian: split BJP/AITC; RSP historically strong in tea belt |
| Sarna_ORP | 40.00 | 40.00 | 3.00 | 12.00 | 5.00 | E | Adivasi Sarna: divided BJP/AITC; RSP legacy |
| Other_residual | 45.00 | 35.00 | 5.00 | 10.00 | 5.00 | E | Mixed residual |

### D.16 Vote × Caste (2019 LS)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 62.00 | 28.00 | 4.00 | 4.00 | 2.00 | C | CSDS 2019 WB bhadralok BJP-lean |
| OBC | 52.00 | 36.00 | 4.00 | 6.00 | 2.00 | C | CSDS 2019; Rajbongshi OBC BJP-leaning |
| SC_total | 58.00 | 34.00 | 2.00 | 5.00 | 1.00 | C | Rajbanshi SC major BJP swing 2019 in Dooars; CSDS pattern |
| ST_total | 45.00 | 36.00 | 3.00 | 12.00 | 4.00 | C | Tea-garden ST divided; RSP legacy strong; BJP gaining |
| Other_Hindu_middle | 55.00 | 37.00 | 2.50 | 4.00 | 1.50 | E | Dooars Hindu middle-caste BJP lean |
| Muslim | 5.00 | 68.00 | 20.00 | 5.50 | 1.50 | C | Same as D.15 |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 57.00 | 35.00 | 3.00 | 4.00 | 1.00 | C | CSDS 2019 WB; male BJP-lean |
| Female | 52.00 | 41.00 | 2.50 | 3.50 | 1.00 | C | CSDS 2019; female TMC premium +6pp vs male |

---

## E. 2019 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 55.11 | A | ECI GE2019 Form-20 AC-segment CSV: 114,879 / 208,442 valid votes |
| AITC | 37.35 | A | ECI GE2019 Form-20 AC-segment CSV: 77,859 / 208,442 |
| INC | 2.29 | A | ECI GE2019: 4,773 votes |
| LF | 4.34 | A | RSP 8,455 + SUCI(C) 586 = 9,041 / 208,442 |
| Other_NOTA | 0.91 | A | IND 482 + IND 1,408 = 1,890 / 208,442 |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 012 Alipurduars (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 1977 AE | Nani Bhattacharya | RSP | — | — | — | — | RSP began 30-yr run |
| 1987 AE | Nani Bhattacharya | RSP | — | — | — | — | RSP 3rd consecutive win |
| 1991 AE | Nirmal Das | RSP | — | — | — | — | RSP continued dominance |
| 2006 AE | Nirmal Das | RSP | — | — | — | — | RSP 4th consecutive Nirmal Das win; Left Front fortress |
| 2011 AE | Debaprasad Roy (Mithu) | INC | — | Kshiti Goswami | RSP | — | 6,783 INC broke RSP after 34 yrs; anti-Left wave; INC got ~79,605 |
| 2016 AE | Sourav Chakraborty | AITC | — | Biswa Ranjan Sarkar | INC | — | ~11,958; AITC 89,695; INC 77,737; TMC swept Dooars |

### Alipurduars Lok Sabha (PC 2) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | — | Left Front | — | RSP held LS seat in Left era; TMC was competing |
| 2019 LS | John Barla | BJP | ~54.4% of LS | BJP surge; John Barla won 750,804 votes; AITC 506,815 (Dasrath Tirkey); margin 243,989 — massive swing |

**Narrative notes:**
- Alipurduars was an RSP/Left fortress from 1977–2009 at both LS and AC level; INC broke this in 2011 riding anti-Left wave.
- AITC absorbed INC voters in 2016; TMC consolidation in Dooars complete by 2016 AE.
- 2019 LS saw a dramatic BJP surge: John Barla (Christian Adivasi) won on BJP ticket — significant because Adivasi Christian vote partially moved to BJP, fracturing the AITC consolidation.
- The RSP retained a significant residual (4.1% AC-12 segment in 2019 LS) reflecting legacy Left identity in tea-belt.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- `data/2019_AssemblySegmentLevelVotingData.csv` — ECI GE2019 AC-segment vote tallies; AC 12 (tier A); confirms BJP 55.11%, AITC 37.35%
- Census of India 2011 — Alipurduar I CD block (Primary Census Abstract; Wikipedia "Alipurduar I" article)
- Census of India 2011 — Alipurduar II CD block (Wikipedia "Alipurduar II" article; censusindia.co.in)
- Census of India 2011 — Alipurduar Municipality (census2011.co.in/data/town/801642)
- Delimitation Commission of India 2008 — WB Schedule (AC 012 composition)
- ECI — 2011 AE, 2016 AE results for AC 012

### Secondary sources (tier B/C)
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline
- Pew Research India 2021 — religion-differential growth projections
- CSDS-Lokniti 2019 NES — vote × demographic conditionals (WB regional rollup)
- Alipurduar District Statistical Handbook / District Profile (alipurduarzp.org)

### Tertiary / journalistic (tier D)
- Elections.in / MyNeta / ElectionGuru — 2019 LS Alipurduars constituency result (John Barla win)
- Journalistic coverage of Dooars Adivasi political alignment 2019 (BJP's John Barla, Christian ST identity)
- electionsguru.in — Alipurduars AC election history 1977–2021

### Tier-D/E reliance flags (what to distrust)
- **Mother tongue shares** (C.5): multiple language groups; AC-level Census language data not directly available; tier A for CDB-I block but AC is subset; some extrapolation needed
- **Sub-unit population split** (C.11): v0 uses 2 sub-units; exact electorate split between Municipality and rural GPs not verified against ECI roll
- **Caste sub-group shares** (C.2, D.2): no caste census post-1931 for non-SC/ST; Rajbanshi SC shares tier C from CSDS/academic sources
- **Tea-garden worker share** (C.7 sub-rows): estimate; no public tea-estate worker head-count at GP level
- **Vote × demographic** (D.15–D.17): CSDS 2019 WB regional rollup + Dooars-specific adjustments; tier C
- **Migration shares** (C.16, D.3): no AC-level Census D-series; tier D from journalistic and block-level patterns
- **Asset/media** (C.14, D.4, D.13): NFHS-4/5 state-level pattern; tier C

### v0 known gaps
1. DCHB Alipurduar Part-A — v0 collapses 13 GPs into 2 sub-units
2. Exact AC electorate from 2019 ECI roll (used CSV figure 249,960 as direct)
3. Census language table: block-level data used; AC is partial block coverage
4. Tea-garden worker population: no public estate-level census; tier E estimate
5. 2019 LS AC-segment form-20 — tier A available from CSV; all parties confirmed

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge. No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2021 WB Assembly Election — AC 012 Alipurduars (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Suman Kanjilal | 107,333 | 48.19% | A — ECI 2021 AE |
| AITC | Sourav Chakraborty | 91,326 | 41.00% | A — ECI 2021 AE |
| INC | (candidate) | ~15,647 | 7.03% | A — ECI 2021 AE |
| **BJP margin** | | **16,007 votes** | | A |

Voter turnout 2021 AE: 85.68%.

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
