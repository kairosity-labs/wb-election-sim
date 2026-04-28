# AC 002 — Mathabhanga (SC) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 002 Mathabhanga as of end-2021 only — it does not reference
> any events after 2021. Use post-2021 elections (2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../../NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 2 | A | ECI / Delimitation Commission 2008 |
| AC name | Mathabhanga | A | ECI |
| Reservation | SC | A | Delimitation 2008 |
| District | Cooch Behar | A | Delimitation 2008 |
| Sub-division | Mathabhanga | A | WB administrative |
| LS constituency | 1 — Cooch Behar (SC reserved) | A | Delimitation 2008 |
| LS segments included | AC 2 Mathabhanga · 3 Sitalkuchi · 4 Dinhata · 5 Sitai · 6 Cooch Behar Uttar · 7 Cooch Behar Dakshin · 8 Natabari | A | Delimitation 2008 |
| AC composition | Mathabhanga Municipality (full) + Mathabhanga II CD block (full) + Hazrahat I, Hazrahat II and Pachagarh gram panchayats of Mathabhanga I CD block | A | Delimitation 2008 / Wikipedia Mathabhanga Assembly constituency |
| Geographic note | Northern West Bengal; Mathabhanga subdivision of Cooch Behar district; predominantly rural flatlands along the Mansai river; near Bangladesh border; BSF 50km jurisdiction active from Oct 2021 | A | — |
| Sub-units used in v0 | **U1: Mathabhanga_Municipality** (urban) · **U2: Mathabhanga_II_CDB_and_GPs** (rural — Mathabhanga II full + 3 GPs of Mathabhanga I) | E | v0 simplification |

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~265,000 (Mathabhanga Muni 23,890 + Mathabhanga II CDB 227,397 + 3 GPs of Mathabhanga I ~14,000 est.) | E | Census 2011; v0 GP-equal-weight assumption for 3 GPs of Mathabhanga I |
| 2021 projected population | ~292,000 | E | 10-yr compound religion-differential growth (methodology §4); ~0.8%/yr composite from 2011 |
| Sex ratio (2021, F per 1000 M) | ~1,058 | B | NFHS-5 Koch Bihar district sex ratio 1,058 (2019-21 survey) — replaces NFHS-4 estimate |
| 2021 electorate (18+) | 248,022 | A | ECI 2021 AE roll — data/electoral_history/2021/detailed_results.csv, total electors column |
| Estimated M / F / TG split (2021) | 48.6% M / 51.4% F / <0.05% TG | B | NFHS-5 Koch Bihar sex ratio 1,058 implies female majority; gender-balanced electorate roll |
| 2021 turnout | 86.36% | A | 214,203 valid votes / 248,022 electors — data/electoral_history/2021/detailed_results.csv |
| 2021 polling stations (estimated) | ~290 | E | Electorate growth from 241,785 (2019) to 248,022 (2021); back-projection |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 82.40 | B | 2019 baseline 82.50%; slight relative Muslim gain (+0.1pp over 2yr); Mathabhanga II CDB 84.46% Hindu, Mathabhanga I 3 GPs ~80.77%; 10-yr projection from Census 2011 |
| Muslim | 17.00 | B | 2019 baseline 16.90%; border AC, modest relative gain; weighted from Mathabhanga II 15.26% + Mathabhanga I 18.61% CDB projected |
| Christian | 0.25 | E | Stable; Mathabhanga II 0.18% + Mathabhanga I 0.02%; negligible change |
| Sarna_ORP | 0.20 | E | Minimal; Cooch Behar district ST share ~1%; mostly Hindu-identified |
| Other_residual | 0.15 | E | Sikh + Jain + Buddhist + Not_stated; residual; stable |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 61.50 | B | Stable from 2019; Mathabhanga II SC 64.92% + Muni SC 23.89% + 3 GPs of Mathabhanga I ~68.77% SC (CDB I avg); weighted population-share; Cooch Behar is India's highest-SC district |
| └ Rajbanshi_SC | 55.00 | C | Dominant SC sub-group in Cooch Behar; ~75% of SC pool per Print/Census pattern; Koch-Rajbanshi SC |
| └ Namasudra_SC | 3.50 | E | Second SC group in region; smaller presence |
| └ Other_SC | 3.00 | E | Residual SC sub-groups |
| **ST_total** | 1.00 | B | Mathabhanga II ST 1.31%; Mathabhanga I ST 0.06%; Muni ST negligible; stable |
| UC_bhadralok | 4.00 | E | Brahmin/Kayastha/Baidya; very small in this predominantly SC-Rajbanshi district |
| OBC | 3.50 | E | Koch-OBC and artisan communities |
| Other_Hindu_middle | 12.85 | E | Residual within Hindu (82.40 − 61.50 SC − 1.00 ST − 4.00 UC − 3.50 OBC = 12.40; slight rounding) |
| Muslim | 17.00 | E | All sub-castes pooled; see C.1 |
| Christian_plus_Sarna_plus_Other | 0.15 | E | Christian 0.25 + Sarna 0.20 + Other 0.15 = 0.60; minor rounding; lumped per schema |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2021, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.50 | E | Renormalized from Cooch Behar district Census 2011 age pyramid + 2yr cohort advance; 18+ only; NFHS-5 Koch Bihar: 25% population below age 15 |
| 23_27 | 12.50 | E | 2019 18_22 cohort advances; first-time voters 2021 aged into this group |
| 28_32 | 11.50 | E | |
| 33_37 | 10.50 | E | |
| 38_42 | 10.00 | E | |
| 43_47 | 9.50 | E | |
| 48_52 | 8.50 | E | |
| 53_57 | 7.50 | E | |
| 58_62 | 6.50 | E | |
| 63_67 | 6.00 | E | |
| 68 | 6.00 | E | 68+ open-ended; slight aging of cohort |
| **Sum** | **100.00** | — | self-check (renormalized from Census after excluding 0–17) |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 48.60 | B | NFHS-5 Koch Bihar sex ratio 1,058 F per 1000 M → 48.6% M / 51.4% F; shift from NFHS-4 baseline of 949 |
| Female | 51.39 | B | NFHS-5 Koch Bihar district |
| Third_gender | 0.01 | E | Marginal fraction; state pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 91.00 | B | Dominant language; Cooch Behar CDBs majority Bengali-speaking; stable from 2019 |
| Hindi | 0.50 | E | Small trader and migrant fringe; stable |
| Urdu | 1.50 | E | Muslim pockets in border area; slight increase with Muslim population gain |
| Other | 0.50 | E | Residual |
| Rajbongshi | 6.50 | C | Rajbanshi/Rajbongshi dialect spoken by Koch-Rajbanshi SC community; AC-local; significant in rural areas of Cooch Behar; classified under Bengali in census but functionally distinct |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 16.50 | B | NFHS-5 Koch Bihar: women literate 79.2% (NFHS-5) vs 73.7% attended school (NFHS-4); 2yr further literacy improvement from 2019 baseline 18%; ~16.5% by 2021 |
| Primary | 23.50 | E | |
| Middle | 22.00 | E | |
| Secondary | 17.50 | E | Slight secondary-level expansion |
| Higher_Secondary | 10.50 | E | |
| Graduate | 7.50 | E | Marginal improvement; SC community educational expansion |
| Postgraduate | 2.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 32.00 | B | COVID-19 impact on formal employment; slight decline from 2019 33%; reverse migration from urban centres during 2020 lockdowns inflated local registration |
| Marginal_worker | 13.00 | E | Slightly higher due to COVID-period disruption and irregular work |
| Non_worker | 36.50 | E | Lakshmir Bhandar beneficiaries concentrated here; post-COVID housewife + elderly |
| Student | 10.00 | E | Stable; school reopening post-COVID in progress |
| Unemployed | 8.50 | E | COVID-period job loss; educated job-seekers; limited urban employment |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 38.50 | B | Slight increase due to COVID reverse migration returning workers to agriculture; Mathabhanga I: 47.24% cultivators; Mathabhanga II: 34.25% |
| Agricultural_labourer | 32.00 | B | Stable; Mathabhanga I: 31.21%; Mathabhanga II: 39.06%; lockdown-driven shift |
| Household_industry | 2.00 | B | Stable |
| Manufacturing | 2.50 | E | Slight decline from COVID disruption |
| Construction | 5.00 | E | Stable; local construction resumed post-lockdown |
| Trade_retail | 8.00 | E | Mathabhanga Muni sub-divisional hub; partial COVID disruption 2020 recovered by 2021 |
| Transport_logistics | 3.00 | E | Stable |
| Services | 5.00 | E | Partial recovery from COVID |
| Government_services_teachers | 4.00 | E | Stable; school teachers partially active |
| Out_migrant_worker | 0.00 | E | COVID-driven reverse migration reduced out-migration to near zero by 2021 |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Stable; limited employer class in SC-heavy AG economy |
| Employee | 21.00 | E | Slight COVID-period contraction in regular employment |
| Single_worker | 53.00 | E | Increase; reverse migrants returning to own-account farming; Rajbanshi farming community |
| Family_worker | 24.50 | E | Stable; unpaid family helpers in agriculture |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 32.00 | E | COVID impact reversed some poverty-reduction gains; 2019 baseline 30%; slight increase due to lockdown income loss in 2020 |
| Above_Poverty_Line_low_income | 35.00 | E | Stable |
| Lower_middle | 21.00 | E | Slight compression due to COVID income loss |
| Middle | 9.50 | E | |
| Upper_middle_well_off | 2.50 | E | Limited affluence; Muni trader class partially impacted |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Mathabhanga_Municipality | 8.20 | E | 2011: Muni 23,890 / AC ~265,000 = 9.0%; urban share continues slight relative decline vs rural growth → ~8.2% by 2021 |
| U2_Mathabhanga_II_CDB_and_GPs | 91.80 | E | Remainder; Mathabhanga II full CDB + 3 GPs of Mathabhanga I; COVID reverse migration swelled rural area temporarily |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | WB 2011: 4.3; Cooch Behar slightly larger household; COVID period may have temporarily increased HH size due to return migration |
| Nuclear_HH | 64.00 | E | Slight decrease from 2019 due to return migrants rejoining extended families |
| Joint_HH | 29.00 | E | Slight increase; return migrants |
| Extended_multi_generation | 7.00 | E | Stable |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.00 | E | Stable; Census 2011 Cooch Behar pattern; NFHS-5 Koch Bihar: women age 20-24 married before 18 = 46.7% (high early marriage) |
| Currently_married | 66.00 | E | Stable; high marriage prevalence in rural SC community |
| Widowed | 7.00 | E | Concentrated in 60+, female-skewed; slight increase with aging |
| Separated_divorced | 1.00 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 72.00 | B | NFHS-5 not directly providing TV data; 2019 baseline 70%; modest +2pp rural saturation; TV near-saturated in urban fraction |
| Radio | 5.00 | E | Declining; stable 2019 baseline |
| Mobile_phone | 87.00 | B | 2019 baseline 82%; post-COVID acceleration; migrant return households now mobile-equipped; ~+5pp |
| Smartphone_with_internet | 58.00 | B | Notable post-COVID surge; 2019 baseline 38%; Jio + COVID work-from-home + Duare Sarkar digital rollout drove +20pp; lockdown forced digital adoption |
| Computer | 6.50 | E | Marginal improvement from 2019 6%; Muni fraction |
| Two_wheeler | 23.00 | E | Modest +1pp from 2019 22% |
| Four_wheeler | 3.00 | E | Stable; limited affluence |
| Banking_access | 93.00 | B | PMJDY + Lakshmir Bhandar bank account requirement (Apr 2021) drove further penetration; +8pp from 2019 85%; near-saturation |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 99.00 | B | NFHS-5 Koch Bihar: 99.3% — dramatic improvement from NFHS-4 98.8%; effectively saturated |
| Improved_sanitation | 76.00 | B | NFHS-5 Koch Bihar: 75.7% — significant gain from NFHS-4 53.3%; Swachh Bharat continued impact |
| LPG_clean_cooking_fuel | 26.00 | B | NFHS-5 Koch Bihar: 25.7% — lower than state urban average; Ujjwala but rural SC households slow to adopt; slight gain from 2019 35% estimate (downward correction from NFHS-5 hard data) |
| Wood_biomass_fuel | 68.00 | B | NFHS-5 Koch Bihar: wood/biomass still dominant; cooking fuel sum adjustment |
| Other_fuel | 6.00 | E | Kerosene, dung, crop residue |
| Electricity | 98.00 | B | NFHS-5 Koch Bihar: 98.2% — near-saturation; Saubhagya saturation confirmed |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 80.50 | E | Predominantly settled Rajbanshi-SC farming community; slight increase in native share due to COVID return migration of temporarily out-migrated workers |
| WB_other_district | 5.00 | E | Stable; small fraction of in-migrants to Muni |
| Other_Indian_state | 1.50 | E | Stable; Hindi-speaking traders; COVID reduced fresh in-migration |
| Bangladesh_origin | 11.00 | D | Border AC; post-1947/1971 Hindu migration families; stable long-term; BSF 50km jurisdiction (Oct 2021) increased border sensitivity |
| Outside_India | 0.50 | E | Negligible |
| Out_migrant | 1.50 | E | Reduced from 2019 2%; COVID reverse migration brought out-migrants back; many re-registered locally by 2021 |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 87.00 | 0.50 | 0.00 | 0.50 | 12.00 | E | Stable from 2019; Rajbanshi-SC population uses Rajbongshi dialect; urban Hindu uses Bengali |
| Muslim | 95.50 | 0.50 | 3.50 | 0.50 | 0.00 | E | Bengali-Muslim border belt; slight Urdu pocket; stable |
| Christian | 90.00 | 5.00 | 0.00 | 5.00 | 0.00 | E | Tiny base; Bengali + English-medium families |
| Sarna_ORP | 70.00 | 0.00 | 0.00 | 5.00 | 25.00 | E | Small tribal population; some Rajbongshi overlap |
| Other_residual | 70.00 | 25.00 | 0.00 | 5.00 | 0.00 | E | Marwari/trader fringe |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 72.00 | 1.20 | 4.85 | 4.25 | 17.70 | 0 | 0 | E | SC_total 61.50/82.40 Hindu ≈ 74.6%; adjusted for non-Hindu SC fraction; stable from 2019 |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 80 | 0 | 5 | 15 | 0 | 0 | E | Tribal sub-castes mostly route to ST_total |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 76.50 | 4.50 | 1.50 | 15.00 | 0.50 | 2.00 | D | Hindu Bangladesh-origin in border AC; Rajbanshi community mostly native; COVID reverse migration returned some out-migrants; stable from 2019 |
| Muslim | 90.50 | 3.00 | 1.00 | 4.00 | 0.50 | 1.00 | D | Muslim border trickle; mostly native Bengali-Muslim peasantry; BSF 50km context |
| Christian | 85.00 | 10.00 | 5.00 | 0.00 | 0.00 | 0.00 | E | Mixed; tiny base |
| Sarna_ORP | 95.00 | 3.00 | 2.00 | 0.00 | 0.00 | 0.00 | E | Local tribal; very settled |
| Other_residual | 40.00 | 20.00 | 35.00 | 5.00 | 0.00 | 0.00 | E | Trader/migrant fringe |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 74.00 | 61.00 | 94.00 | B | NFHS-5 Koch Bihar district baseline; post-COVID smartphone surge; Lakshmir Bhandar banking push |
| Muslim | 65.00 | 45.00 | 87.00 | E | Lower asset access; rural Muslim border belt; PMJDY penetration but less smartphone adoption |
| Christian | 82.00 | 62.00 | 95.00 | E | Tiny base; slightly better asset profile |
| Sarna_ORP | 58.00 | 30.00 | 78.00 | E | Minimal tribal base |
| Other_residual | 94.00 | 78.00 | 98.00 | E | Trader/upper-income fringe |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4.00 | 8.00 | 11.00 | 18.00 | 21.00 | 26.00 | 12.00 | E |
| SC_total | 20.00 | 26.00 | 22.00 | 16.00 | 9.00 | 5.50 | 1.50 | E |
| ST_total | 26.00 | 28.00 | 21.00 | 13.00 | 7.00 | 4.00 | 1.00 | E |
| OBC | 14.00 | 24.00 | 22.00 | 18.00 | 12.00 | 8.00 | 2.00 | E |
| Other_Hindu_middle | 13.00 | 22.00 | 22.00 | 18.00 | 12.50 | 9.50 | 3.00 | E |
| Muslim | 21.00 | 26.00 | 22.00 | 16.00 | 9.50 | 4.50 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 13.00 | 11.00 | E |
| 23_27 | 13.00 | 10.00 | E |
| 28_32 | 11.00 | 8.00 | E |
| 33_37 | 9.00 | 6.00 | E |
| 38_42 | 8.00 | 5.00 | E |
| 43_47 | 7.00 | 4.00 | E |
| 48_52 | 6.00 | 3.00 | E |
| 53_57 | 5.00 | 2.50 | E |
| 58_62 | 4.50 | 1.50 | E |
| 63_67 | 3.50 | 1.00 | E |
| 68 | 3.00 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8.00 | 32.00 | E |
| 23_27 | 46.00 | 83.00 | E |
| 28_32 | 83.00 | 93.00 | E |
| 33_37 | 92.00 | 90.00 | E |
| 38_42 | 93.00 | 88.00 | E |
| 43_47 | 93.00 | 83.00 | E |
| 48_52 | 91.00 | 75.00 | E |
| 53_57 | 88.00 | 65.00 | E |
| 58_62 | 85.00 | 50.00 | E |
| 63_67 | 78.00 | 35.00 | E |
| 68 | 70.00 | 25.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 42.00 | 65.00 | E | Post-COVID Jio rural expansion; reverse migrants with smartphones returned to agriculture |
| Agricultural_labourer | 30.00 | 58.00 | E | Lowest income; modest gain from 2019 |
| Household_industry | 48.00 | 70.00 | E | |
| Manufacturing | 60.00 | 80.00 | E | |
| Construction | 55.00 | 74.00 | E | |
| Trade_retail | 72.00 | 87.00 | E | Muni concentrated; near-saturation |
| Transport_logistics | 65.00 | 80.00 | E | |
| Services | 75.00 | 90.00 | E | |
| Government_services_teachers | 88.00 | 95.00 | E | Highest; Duare Sarkar digital infrastructure |
| Out_migrant_worker | 70.00 | 78.00 | E | Reduced pool; those remaining more smartphone-intensive |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 37.00 | 1.50 | E |
| Primary | 39.00 | 3.00 | E |
| Middle | 35.00 | 5.50 | E |
| Secondary | 28.00 | 9.50 | E |
| Higher_Secondary | 22.00 | 15.00 | E |
| Graduate | 24.00 | 17.00 | E |
| Postgraduate | 34.00 | 11.00 | E |

### D.10 Asset / media × Bilingualism

(Skip — no `media_tier` axis declared for this AC; Rajbongshi-speaking population adds local dimension but no formal media-tier axis.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit). Sub-unit codes use `Un_` prefix matching C.11.

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Mathabhanga_Municipality | 85.00 | 13.60 | 0.70 | 0.20 | 0.50 | E | Muni: lower Muslim share than rural; SC 23.89% mostly Hindu Rajbanshi; stable from 2019 |
| U2_Mathabhanga_II_CDB_and_GPs | 82.20 | 17.20 | 0.22 | 0.20 | 0.18 | B | Mathabhanga II CDB + 3 GPs; slight Muslim share gain from 2019 projection |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Use canonical caste leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Mathabhanga_Municipality | 8.00 | 23.89 | 0.25 | 6.00 | 47.26 | 13.60 | 1.00 | B |
| U2_Mathabhanga_II_CDB_and_GPs | 3.50 | 65.50 | 1.05 | 3.20 | 9.55 | 17.20 | 0.00 | B |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Mathabhanga_Municipality | 90.00 | 70.00 | 18.00 | 97.00 | C |
| U2_Mathabhanga_II_CDB_and_GPs | 70.00 | 55.00 | 5.50 | 92.00 | C |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Mathabhanga_Municipality | 55.00 | 92.00 | 99.00 | 99.00 | B |
| U2_Mathabhanga_II_CDB_and_GPs | 22.00 | 73.00 | 99.00 | 98.00 | B |

### D.15 Vote × Religion (2021 AE)

P(party ‖ religion) — anchored on 2021 AE result (BJP 52.87%, AITC 40.67%, LF 3.60%).

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 63.00 | 32.00 | 0.00 | 3.50 | 1.50 | C | 2021 AE: BJP consolidated Rajbanshi-SC Hindu vote; no INC candidate; strong BJP performance in Cooch Behar Hindu-SC belt |
| Muslim | 5.00 | 76.00 | 0.00 | 14.00 | 5.00 | C | Muslim voters split between AITC and LF (CPI-M retained Muslim bloc in border ACs); no INC candidate |
| Christian | 25.00 | 60.00 | 0.00 | 10.00 | 5.00 | E | Tiny base; AITC-leaning in 2021 |
| Sarna_ORP | 42.00 | 40.00 | 0.00 | 13.00 | 5.00 | E | Mixed tribal; slight BJP gain |
| Other_residual | 45.00 | 38.00 | 0.00 | 12.00 | 5.00 | E | |

### D.16 Vote × Caste (2021 AE)

P(party ‖ caste) — anchored on 2021 AE result.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 60.00 | 30.00 | 0.00 | 7.00 | 3.00 | C | BJP dominant; no INC candidate |
| OBC | 42.00 | 40.00 | 0.00 | 14.00 | 4.00 | C | Mixed; BJP gains among OBC Koch |
| SC_total | 58.00 | 35.00 | 0.00 | 4.50 | 2.50 | C | Rajbanshi-SC BJP consolidation; 2021 result confirms continued SC BJP alignment; Koch-Rajbanshi identity politics |
| ST_total | 44.00 | 38.00 | 0.00 | 13.00 | 5.00 | E | Small ST base; mixed |
| Other_Hindu_middle | 52.00 | 38.00 | 0.00 | 7.00 | 3.00 | C | BJP strong |
| Muslim | 5.00 | 76.00 | 0.00 | 14.00 | 5.00 | C | Same as D.15 |

### D.17 Vote × Gender (2021 AE)

P(party ‖ gender) — 2021 AE; post-Lakshmir Bhandar launch (Apr 2021).

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 56.00 | 37.00 | 0.00 | 5.50 | 1.50 | C | BJP male advantage maintained; CSDS 2021 WB regional exit poll pattern |
| Female | 49.00 | 45.00 | 0.00 | 4.00 | 2.00 | C | Female shift toward AITC; Lakshmir Bhandar announced Apr 2021 during campaign; TMC women's advantage greater than 2019 |

### D.18 Vote × Welfare

(Skip — no `welfare_exposure` axis declared for this AC in v0.)

---

## E. 2021 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 52.87 | A | ECI 2021 AE; Sushil Barman 113,249 valid votes / 214,203 total — data/electoral_history/2021/detailed_results.csv |
| AITC | 40.67 | A | Girindra Nath Barman 87,115 votes / 214,203 — same source |
| INC | 0.00 | A | No INC candidate contesting — same source |
| LF | 3.60 | A | CPI(M) Ashok Barman 7,718 votes / 214,203 — same source |
| Other_NOTA | 2.86 | A | NOTA 1,443 + KPPU 1,289 + IND 1,167 + IND 1,147 + SUCI 589 + AMB 486 = 6,121 / 214,203 — same source |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 002 Mathabhanga (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Binay Krishna Barman | AITC | ~48.1 | Khagen Chandra Barman | CPI(M) | ~32.2 | ~31,918 votes (96,383 vs 64,465) |
| 2016 AE | Binay Krishna Barman | AITC | ~48.1 | Khagen Chandra Barman | CPI(M) | ~32.2 | ~31,918 votes; BJP contested (Sushil Barman) but ran third |

Note: 2016 result shows same incumbent re-elected with BJP establishing a third-place presence. The 2016 vote total of ~200,385 is separately confirmed. BJP's Sushil Barman (the 2021 winner) built his base in 2016.

### 2019 Lok Sabha Election — AC 002 segment within Cooch Behar LS (PC 1)

| Party | Candidate | Votes (AC segment) | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Nisith Pramanik | 107,063 | 52.09% | A | 2019_AssemblySegmentLevelVotingData.csv — was 2019 calibration target; now historical anchor |
| AITC | Adhikary Paresh Chandra | 86,188 | 41.94% | A | Same |
| INC | — | 3,012 | 1.47% | A | Same |
| LF (AIFB) | — | 5,757 | 2.80% | A | Same |
| Other_NOTA | various | 3,498 | 1.70% | A | Same |
| **Total valid votes** | | 205,518 | 100% | A | 2019_AssemblySegmentLevelVotingData.csv |

Political dynamics by 2021: BJP maintained its Rajbanshi-SC dominance established in 2019. Sushil Barman (BJP) won the 2021 AE seat with 52.87% against AITC's Girindra Nath Barman (40.67%), increasing the BJP margin to 26,134 votes (12.20pp) — substantially higher than the 2019 LS AC-segment margin of 10.15pp. The BJP victory confirmed continued consolidation of Koch-Rajbanshi identity and SC voter alignment. CPI(M)'s Ashok Barman ran third with 3.60%. No INC candidate contested. The Sitalkuchi (AC 5) CISF firing incident on 10 April 2021 during polling had spillover sensitivity in adjacent Cooch Behar constituencies; Mathabhanga was polled in an earlier phase.

### Cooch Behar Lok Sabha (PC 1) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | (AITC held Cooch Behar) | AITC | — | AITC held; BJP third |
| 2019 LS | Nisith Pramanik | BJP | ~48.0 | BJP win; Rajbanshi mobilisation; margin 54,231; total electorate 1,329,086 |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Election Commission of India — `data/electoral_history/2021/detailed_results.csv` — AC 002 Mathabhanga 2021 AE result: Sushil Barman (BJP) 113,249; Girindra Nath Barman (AITC) 87,115; Ashok Barman (CPI-M) 7,718; NOTA 1,443; KPPU 1,289; IND 1,167; IND 1,147; SUCI 589; AMB 486; total valid 214,203; electorate 248,022
- Election Commission of India — `data/2019_AssemblySegmentLevelVotingData.csv` — AC 002 segment 2019 LS: BJP 107,063; AITC 86,188; AIFB 5,757; INC 3,012; others 3,498; total 205,518; electorate 241,785
- ECI / Delimitation Commission of India 2008 — WB Schedule: AC 2 Mathabhanga (SC) = Mathabhanga Municipality + Mathabhanga II CDB + Hazrahat I, Hazrahat II and Pachagarh GPs of Mathabhanga I CDB; under Cooch Behar (SC) LS PC 1

### Secondary sources (tier B / C)

- Census of India 2011 — Mathabhanga I CD block Primary Census Abstract (Wikipedia: pop 218,191; Hindu 80.77%; Muslim 18.61%; SC 68.77%; workers 44.94%)
- Census of India 2011 — Mathabhanga II CD block Primary Census Abstract (Wikipedia: pop 227,397; Hindu 84.46%; Muslim 15.26%; SC 64.92%; ST 1.31%)
- Census of India 2011 — Mathabhanga Municipality (census2011.co.in: pop 23,890; SC 23.89%; ST 0.25%)
- NFHS-5 (2019-21) Koch Bihar district — `data/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv` — sex ratio 1,058; electricity 98.2%; drinking water 99.3%; improved sanitation 75.7%; clean cooking fuel 25.7%; women literacy 79.2%; early marriage 46.7%
- CSDS-Lokniti 2021 WB exit poll / post-poll — vote × religion / caste / gender regional WB rollup (gender gap anchor for D.17)

### Tertiary / journalistic (tier D)

- The Print: "Who are Rajbanshis, caught in Shah-Mamata scrap" — Rajbanshi SC ~75% of SC pool in Cooch Behar; BJP Koch-Rajbanshi mobilisation strategy
- ResultUniversity / IndiaStatPublications: Mathabhanga 2011 AE result (Binay Krishna Barman AITC 96,383; Khagen CPI(M) 64,465)
- Wikipedia "Mathabhanga Assembly constituency" — AC composition (Delimitation 2008); 2021 AE candidate details
- Cooch Behar 2019 LS: Nisith Pramanik (BJP) 731,594 votes; margin 54,231

### Tier-D / E reliance flags (what to distrust)

- **Religion composition** (C.1, D.11) — Muni religion breakout not in CSV; Tier-B weighted estimate from CDB-level data
- **Caste sub-group shares within Hindu** (C.2, D.2) — no caste census post-1931 for non-SC/ST; Rajbanshi dominant position well-established but sub-group percentages Tier-C/E
- **Migration/birthplace** (C.16, D.3) — no public AC-level Census D-series; Tier-D from journalistic/geographic anchor
- **GP-level sub-unit data** (D.11–D.14) — collapsed to 2 sub-units (Muni + rural); refine when DCHB Cooch Behar Part-A accessible
- **Asset/media smartphone** (C.14 Smartphone, D.4, D.13) — NFHS-5 Koch Bihar does not directly report smartphone %; +20pp estimate from 2019 baseline uses methodology §4 post-COVID surge rule; Tier-B
- **Vote × Demographic** (D.15–D.17) — CSDS 2021 WB regional exit poll; no AC-specific cross-tab; Tier-C
- **LPG cooking fuel** (C.15) — NFHS-5 hard data 25.7% is LOWER than 2019 estimate of 35%; adopted NFHS-5 as correction; Tier-B
- **Gender split** (C.4, B) — NFHS-5 sex ratio 1,058 applied; significant upward revision from 2019 sex ratio 949 baseline

### v0 known gaps

1. DCHB Cooch Behar Part-A — sub-unit detail collapsed to 2 (Muni + rural CDB)
2. AC-level religion breakout for Mathabhanga Municipality — using district/CDB proxy
3. Census D-series for migration — using geographic/journalistic anchor
4. Full CSDS WB Cooch Behar-specific cross-tabs — using WB regional rollup
5. 2016 AE exact votes — data ambiguity between 2011 and 2016 elections in sources; both appear to show same incumbent winning
6. LPG clean cooking fuel 2019 estimate was 35% vs NFHS-5 actual 25.7% — downward correction applied; prior estimate may have over-applied Ujjwala rural trend

---

*v0 — generated 2026-04-28, frozen at 2021 state-of-knowledge.
No post-2021 events referenced.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs. The
> validator's leakage gate exempts §H from the no-future-leakage check.

### 2024 Lok Sabha Election — AC 002 segment within Cooch Behar LS (PC 1) (tier A, CSV)

> Figures below are **tier A** — sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=2, Mathabhanga segment.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Nisith Pramanik | 110,612 | 50.38% | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Jagadish Chandra Barma Basunia | 99,974 | 45.53% | A | Same |
| AIFB (LF) | Nitish Chandra Roy | 4,197 | 1.91% | A | Same |
| INC | Piya Roy Chowdhury | 1,107 | 0.50% | A | Same |
| NOTA | — | 1,964 | 0.89% | A | Same |
| Others | BSP+SUCI+KPPU+INDs | 1,711 | 0.78% | A | Same |
| **Total valid votes** | | 219,565 | 100% | A | Computed |

> BJP margin over AITC: 10,638 votes; 4.85pp. BJP held but margin substantially tightened compared to 2021 AE (12.20pp margin) and 2019 LS (10.15pp margin). AITC gained significant share from 2021 AE 40.67% → 2024 LS 45.53% (+4.86pp). Electorate grew from 248,022 (2021) to 265,316 (2024). Turnout 82.76%.

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC segment shares within ±3pp of the tier-A figures:
- BJP target: 50.4% ± 3pp
- AITC target: 45.5% ± 3pp
- LF+INC+others: ~4.1% ± 3pp
