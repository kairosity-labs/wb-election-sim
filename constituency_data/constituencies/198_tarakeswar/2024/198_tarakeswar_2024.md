# AC 198 — Tarakeswar (GEN) — Calibrated 2024 Population Snapshot

> **Frozen at end-2024.** This file describes the demographic and behavioural state of AC 198 Tarakeswar as of end-2024 only. It does not reference any post-2024 events. Section H contains a thin forward-looking placeholder for 2026 AE.
>
> Events known by end-2024 and freely referenced here: 2019 LS, 2020 COVID-19 lockdown, 2020 Cyclone Amphan, 2021 WB AE, Lakshmir Bhandar (Apr 2021), BSF 50km jurisdiction (Oct 2021), SSC scam exposure (Jul 2022), 2023 WB Panchayat elections, CAA rules notification (Mar 2024), 2024 LS campaign and result (Jun 2024), RG Kar Hospital protests (Aug 2024), Bangladesh interim regime (Aug 2024).
>
> **Forbidden keywords (auto-checked):** `2025, 2026, SIR, Special Intensive Revision, AE-2026, 2026 election`
>
> Companion artifacts: [`methodology_2024.md`](../../methodology_2024.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2024)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 198 | A | ECI / Delimitation Commission 2008 |
| AC name | Tarakeswar | A | ECI |
| Reservation | General (unreserved) | A | Delimitation 2008 |
| District | Hooghly | A | Delimitation 2008 |
| Sub-division | Chandannagore (Hooghly district administrative); Tarakeswar CDB/Muni is in Chandannagore subdivision | A | WB Hooghly District portal |
| LS constituency | 29 — Arambagh (SC reserved) | A | Delimitation 2008 |
| AC composition | Tarakeswar Municipality (full) + all 10 GPs of Tarakeswar CDB + Bhanderhati I, Bhanderhati II, Gopinathpur I, Gopinathpur II, Parambua-Sahabazar GPs of Dhaniakhali CDB | A | Delimitation Commission Order 2008 |
| Geographic note | Temple town at 58 km from Kolkata; Howrah-Tarakeswar railway line; Taraknath Shiva Temple ~10 million pilgrims per year in Sravan month; pilgrim economy (accommodation, food, trade, transport) supplements agrarian base; commuter workforce to Kolkata significant | A | Wikipedia Tarakeswar; GoWB Hooghly portal |
| Two sub-units used in v0 | **U1_Tarakeswar_Muni_CDB** (urban+rural core, ~72% of AC pop) · **U2_Dhaniakhali_5GP** (rural fringe, ~28%) | E | v0 simplification |
| Pilgrim economy note (2020-2024) | Sravan pilgrimage collapsed in 2020 (zero pilgrims, COVID lockdown); partial 2021; full recovery by 2022 Sravan season (~10M pilgrims). By 2024 the pilgrim economy has fully rebounded; temple-related trade, accommodation, and micro-hospitality are back at pre-COVID levels. | D | Press reports; Wikipedia Tarakeswar temple |
| Political context 2022-2024 | SSC scam (Jul 2022 Partha Chatterjee arrest) created anti-TMC educated-youth sentiment across WB including Hooghly. RG Kar Hospital rape-murder (Aug 2024) generated large-scale protests. CAA rules notified (Mar 2024) — less salient in Hooghly than in N24P/Matua belt but BJP used it in campaign. | D | Indian Express; ThePrint; Wikipedia |

---

## B. 2024 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~299,132 | E | Census 2011; v0 GP proxy |
| 2024 projected population | ~340,800 | E | 13-yr compound religion-differential growth from 2011 (~1.2%/yr blended); methodology §4 |
| Sex ratio (2024, F per 1000 M) | ~968 | E | 2011 base ~965; gradual female-favourable drift; rural WB pattern |
| 2024 electorate (tier A — ECI 2024 LS CSV) | 244,468 | A | 2024_AssemblySegmentLevelVotingData.csv, AC_NO=198 |
| 2024 turnout (2024 LS) | 84.34% (206,193 / 244,468) | A | 2024_AssemblySegmentLevelVotingData.csv |
| Estimated M / F / TG split (2024) | ~50.8% M / 49.2% F / <0.05% TG | E | Sex ratio ~968 F/1000M; near-stable from 2021 |
| 2024 polling stations (estimated) | ~295 | E | Slight growth from 2021 (~285) with voter-roll expansion |
| Note on electorate change | 2021 roll 221,972 → 2024 electorate 244,468 (+22,496). This reflects voter-roll expansion (new additions, 18-22 cohort additions, roll correction) between 2021 AE and 2024 LS. Both tier A. | A | ECI 2021 AE roll + 2024 CSV |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 86.40 | E | 2021 base 86.61%; 3 more years of religion-differential growth (Muslim +1.3%/yr, Hindu +1.0%/yr) → Hindu dips ~0.21pp additional; 86.40% by end-2024 |
| Muslim | 12.20 | E | 2021 base 11.98%; +0.22pp over 3 more years differential growth |
| Christian | 0.30 | E | Held stable |
| Sarna_ORP | 0.83 | E | Slight continued decline |
| Other_residual | 0.27 | E | Residual; Jain/Sikh/Buddhist in Muni |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| SC_total | 25.3 | E | Near-stable from 2021 base 25.4% |
| └ Bagdi_SC | 9.4 | C | Dominant SC; near-stable |
| └ Bauri_SC | 4.4 | E | |
| └ Namasudra_SC | 3.5 | E | |
| └ Other_SC | 8.0 | E | Hari, Chamar, Jalia, Rajbanshi residual |
| ST_total | 7.1 | E | Near-stable from 2021 base 7.2% |
| └ Santal_ST | 5.4 | C | Dominant ST in Hooghly |
| └ Other_ST | 1.7 | E | Munda, Bhumij, Lodha |
| UC_bhadralok | 8.0 | D | Temple-town educated class; Brahmin priests significant; stable |
| OBC | 30.3 | D | Mahishya + Sadgop + Kurmi + Tili; marginal growth |
| └ Mahishya | 18.1 | D | Single largest caste in Hooghly; dominant cultivating caste |
| └ Sadgop | 6.0 | D | OBC-B; second-tier cultivating caste |
| └ Kurmi | 3.5 | D | OBC-A; rural CDB cultivator |
| └ Tili_other_OBC | 2.7 | D | Temple-economy trade + residual OBC |
| Other_Hindu_middle | 15.8 | E | Goala, Tanti, Sutradhar, unclassified middle |
| Muslim | 12.20 | E | See C.1; Bengali-Sheikh peasantry dominant |
| Christian_plus_Sarna_plus_Other | 1.40 | E | See C.1 |
| **Sum** | **100.00** | — | self-check (25.3+7.1+8.0+30.3+15.8+12.20+1.40 ≈ 100.1 → rounds to 100 with ±0.1 tolerance ✓) |

### C.3 Age cohort (2024, voters 18+ only)

> Renormalized to voter-eligible population (18+); three more years of new entrants into the electorate.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.8 | E | 2024 voter cohort (born 2002-2006); first-time voter 2024 LS cohort |
| 23_27 | 12.5 | E | |
| 28_32 | 12.8 | E | |
| 33_37 | 12.0 | E | |
| 38_42 | 11.0 | E | |
| 43_47 | 9.8 | E | |
| 48_52 | 8.5 | E | |
| 53_57 | 7.3 | E | |
| 58_62 | 5.8 | E | |
| 63_67 | 4.5 | E | |
| 68 | 4.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.82 | E | Sex ratio ~968 F/1000M → 50.82% M / 49.18% F |
| Female | 49.18 | E | |
| Third_gender | 0.00 | E | Negligible |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 92.1 | E | 2021 base 92.3%; slight further decline |
| Santali | 2.5 | E | ST fringe; stable |
| Hindi | 3.7 | E | Tarakeswar Muni Hindi-speaker fringe; stable |
| Urdu | 1.0 | E | Muslim pocket in Dhaniakhali GPs; slight growth |
| Other | 0.7 | E | Kurukh/Munda/Bhumij ST fringe |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2024, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 11.5 | E | 2021 base 12.5%; continued +0.5pp/yr literacy improvement |
| Primary | 21.0 | E | |
| Middle | 21.0 | E | |
| Secondary | 20.0 | E | SSC expansion continues |
| Higher_Secondary | 13.0 | E | |
| Graduate | 10.0 | E | Modest growth; college expansion |
| Postgraduate | 3.5 | E | Small professional class; slight growth |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 32.5 | E | 2021 base 31.5%; post-COVID recovery to near 2019 levels; pilgrim economy and railway-linked services restored |
| Marginal_worker | 12.5 | E | Slight decline as recovered main-worker share absorbs marginal workers |
| Non_worker | 37.5 | E | Female housewife fraction; stable with Lakshmir Bhandar expanding female economic engagement marginally |
| Student | 10.5 | E | Slight decline from 2021; educated cohort entering job market |
| Unemployed | 7.0 | E | SSC scam exposure (Jul 2022) heightened educated-youth unemployment anxiety; held at 7% but with qualitatively higher frustration |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 17.5 | E | 2021 base 18.5%; slight decline as farm-to-services mobility resumes post-COVID |
| Agricultural_labourer | 39.5 | E | Slight decline from 2021 (40.5%) |
| Household_industry | 4.5 | E | Stable |
| Manufacturing | 5.0 | E | Recovery to 2019 level |
| Construction | 6.0 | E | Recovery to 2019 level; Kolkata commuter construction workers returned |
| Trade_retail | 10.5 | E | Pilgrim economy fully recovered by 2022-2024 Sravan season; above 2021 depressed level |
| Transport_logistics | 4.5 | E | Railway fully operational; Kolkata commuter logistics stable |
| Services | 8.5 | E | Kolkata commuter workforce; slight growth from service-sector expansion |
| Government_services_teachers | 4.0 | E | Stable; SSC scam created uncertainty about new government appointments in education sector |
| Out_migrant_worker | 0.0 | E | Very small; negligible |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.0 | E | Recovery from COVID disruption; small business revival in Muni |
| Employee | 25.0 | E | Near 2019 levels |
| Single_worker | 53.0 | E | Own-account agriculture + artisan; stable |
| Family_worker | 20.0 | E | Near 2019 levels |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2024, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 19.5 | C | 2021 base 21.0%; declining trend resumed post-COVID recovery; Hooghly below WB average poverty rate; Lakshmir Bhandar and other welfare schemes providing income floor |
| Above_Poverty_Line_low_income | 37.5 | E | Rural cultivating-OBC and SC labourer households |
| Lower_middle | 26.5 | E | Modest growth from welfare and service-sector expansion |
| Middle | 13.0 | E | Recovery to near 2019 level |
| Upper_middle_well_off | 3.5 | E | Slight growth from temple-economy business revival |
| **Sum** | **100.00** | — | self-check |
| **Lakshmir Bhandar saturation** | ~65% of eligible women HH heads | D | From ~35% enrollment end-2021 to ~65% by end-2024; scheme became central welfare anchor for TMC women base across WB including Hooghly; ₹500/month general + ₹1000 SC/ST. Source: WB CDWDSW; press estimates |
| **PM Kisan exposure** | ~18% of cultivator HH | D | WB joined at 8th installment (Apr-Jul 2021); now 3 years of receipt by end-2024; ~₹6000/yr per cultivator HH; bipartisan benefit (BJP takes credit for central scheme; TMC for state joining) |
| **SSC scam sentiment** | — | D | Partha Chatterjee arrest (Jul 2022), money seizure at Arpita Mukherjee; significant corruption scandal damage to TMC's educated-class image statewide. Sentiment salient among graduate+ job-aspirants in Tarakeswar. |

### C.11 GP / Municipality location (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Tarakeswar_Muni_CDB | 70.5 | E | Near-stable from 2021 (70.3%); slight Muni growth |
| U2_Dhaniakhali_5GP | 29.5 | E | Near-stable from 2021 (29.7%) |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2024)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.3 | E | Declining from 2021 (4.4); continued nuclear-family trend; post-COVID extended-household arrangement partially dissolved |
| Nuclear_HH | 69.5 | E | Near-stable trend |
| Joint_HH | 24.5 | E | Continued mild decline |
| Extended_multi_generation | 6.0 | E | |
| **Sum** | **100.00** | — | self-check (Nuclear+Joint+Extended = 100 ✓) |

### C.13 Marital status (2024, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.0 | E | Stable |
| Currently_married | 66.0 | E | Slight increase as large 23-32 cohort in peak marriage years |
| Widowed | 8.0 | E | Stable |
| Separated_divorced | 1.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2024, household level)

> Smartphone effectively saturated; UPI/digital payments near-universal among smartphone holders; banking at peak penetration

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 80.0 | C | 2021 base 78.0%; near-saturation; slight growth |
| Radio | 3.5 | C | Continuing decline |
| Mobile_phone | 94.0 | C | Near-saturation; further growth mainly in 68+ cohort and BPL HH |
| Smartphone_with_internet | 80.0 | C | 2021 base 62.0%; **+18pp further surge** 2021-2024; NFHS-5 WB rural ~58% in 2019-21 survey period; by 2024 rural Hooghly ~80% consistent with national 80%+ smartphone ownership trend; Jio 5G rollout in Hooghly 2023 |
| Computer | 10.0 | C | Modest growth; WFH adoption |
| Two_wheeler | 35.0 | C | Continued growth; aspiration and commuter utility |
| Four_wheeler | 6.5 | C | Gradual growth from pilgrim-economy business class |
| Banking_access | 95.0 | B | PMJDY saturation + Lakshmir Bhandar bank-account requirement; near-total penetration |
| **Note** | (these are independent ownership %s, not categorical — do not sum) | — | — |

### C.15 Household amenities (2024)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 88.0 | C | 2021 base 85.5%; Jal Jeevan Mission (2019+) continuing; Hooghly piped water improvement |
| Improved_sanitation | 78.0 | C | 2021 base 71.0%; ODF Plus drive; Swachh Bharat Phase 2 targets; Hooghly above WB average |
| LPG_clean_cooking_fuel | 60.0 | C | 2021 base 52.0%; Ujjwala 2.0 + continued PMUY + PMGKY free-cylinder end but refill subsidy; significant increase; wood-fuel substitution accelerating |
| Wood_biomass_fuel | 35.0 | C | Declining as LPG rises |
| Other_fuel | 5.0 | C | Kerosene, dung; stable |
| Electricity | 99.0 | A | Full saturation; Hooghly well-electrified |
| **Note** | (LPG + Wood_biomass + Other_fuel sum to 100; water/sanitation/electricity are independent flags) | — | — |

### C.16 Migration / birthplace (2024, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 82.5 | D | Stable from 2021; post-COVID reverse migration of some workers consolidated in home village |
| WB_other_district | 7.5 | D | Stable |
| Other_Indian_state | 4.5 | D | Hindi-belt pilgrim-economy traders; stable |
| Bangladesh_origin | 4.0 | D | Hooghly is non-refugee district; Bangladesh-origin families; Bangladesh August 2024 regime change not materially affecting cross-border migration to this AC (inland Hooghly, no border) |
| Outside_India | 0.5 | E | Negligible |
| Out_migrant | 1.0 | E | Kolkata commuters; stable |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue (2024)

P(language | religion) — % within each religion's population.

| Religion | Bengali | Santali | Hindi | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 94.2 | 1.5 | 3.3 | 0.0 | 1.0 | E | Near-stable from 2021 |
| Muslim | 87.0 | 0.0 | 1.5 | 10.5 | 1.0 | E | Bengali-Sheikh majority; Urdu fraction slight growth |
| Sarna_ORP | 15.0 | 74.0 | 0.0 | 0.0 | 11.0 | E | Santal practitioners |
| Christian | 90.0 | 5.0 | 0.0 | 0.0 | 5.0 | E | Tiny base |
| Other_residual | 58.0 | 0.0 | 32.0 | 0.0 | 10.0 | E | Marwari/Jain fringe |

### D.2 Religion × Caste (2D layout per normalized schema)

P(caste | religion) — % within each religion. Rows sum to 100.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 29.3 | 8.2 | 9.3 | 35.1 | 18.1 | 0.0 | 0.0 | D | (SC_total 25.3 + ST_total 7.1 + UC 8.0 + OBC 30.3 + Other_Hindu 15.8) / Hindu 86.40%; aggregated sub-castes into parent leaves |
| Muslim | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | A | |
| Sarna_ORP | 0.0 | 92.0 | 0.0 | 5.0 | 3.0 | 0.0 | 0.0 | E | |
| Christian | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | A | |
| Other_residual | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | E | |

### D.3 Religion × Migration (2024)

P(birthplace | religion).

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 80.5 | 7.5 | 5.5 | 5.0 | 0.0 | 1.5 | D | Stable from 2021 |
| Muslim | 93.5 | 3.5 | 2.0 | 1.0 | 0.0 | 0.0 | D | |
| Sarna_ORP | 90.0 | 7.0 | 2.0 | 0.0 | 1.0 | 0.0 | E | |
| Christian | 85.0 | 10.0 | 5.0 | 0.0 | 0.0 | 0.0 | E | |
| Other_residual | 40.0 | 15.0 | 40.0 | 5.0 | 0.0 | 0.0 | E | |

### D.4 Religion × Asset / media (2024)

P(owns asset | religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 82.0 | 83.0 | 96.0 | C | NFHS-5 direction + 2024 trend; near-saturation for Hindu in Hooghly |
| Muslim | 70.0 | 65.0 | 88.0 | C | Muslim asset gap narrowing; Lakshmir Bhandar + PMJDY banking drives |
| Sarna_ORP | 62.0 | 52.0 | 82.0 | C | Improvement from 2021; welfare digital enrollment |
| Christian | 85.0 | 72.0 | 95.0 | E | |
| Other_residual | 88.0 | 85.0 | 96.0 | E | Marwari business class |

### D.5 Caste × Education (2024)

P(education | caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 3 | 6 | 10 | 17 | 20 | 30 | 14 | E |
| Mahishya | 8 | 18 | 21 | 24 | 16 | 10 | 3 | E |
| Sadgop | 9 | 20 | 21 | 22 | 14 | 11 | 3 | E |
| Kurmi | 12 | 22 | 22 | 21 | 13 | 8 | 2 | E |
| Tili_other_OBC | 12 | 21 | 21 | 21 | 13 | 9 | 3 | E |
| Bagdi_SC | 18 | 25 | 22 | 18 | 11 | 5 | 1 | E |
| Bauri_SC | 21 | 26 | 21 | 16 | 9 | 6 | 1 | E |
| Namasudra_SC | 14 | 22 | 22 | 19 | 12 | 9 | 2 | E |
| Santal_ST | 25 | 28 | 20 | 15 | 8 | 3 | 1 | E |
| Other_ST | 28 | 27 | 19 | 14 | 7 | 4 | 1 | E |
| Muslim | 16 | 23 | 23 | 20 | 11 | 6 | 1 | E |

### D.6 Age × Gender × Education (2024)

P(grad+ | age × gender) — graduate-or-higher share. Education recovery post-COVID; 2024 cohorts show near-normal attainment.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 20 | 18 | E |
| 23_27 | 18 | 14 | E |
| 28_32 | 15 | 10 | E |
| 33_37 | 13 | 7 | E |
| 38_42 | 11 | 6 | E |
| 43_47 | 9 | 4 | E |
| 48_52 | 7 | 3 | E |
| 53_57 | 6 | 2 | E |
| 58_62 | 5 | 2 | E |
| 63_67 | 4 | 1 | E |
| 68 | 3 | 1 | E |

### D.7 Marital status × Age × Gender (2024)

P(currently married | age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 7 | 30 | E |
| 23_27 | 45 | 84 | E |
| 28_32 | 84 | 95 | E |
| 33_37 | 93 | 92 | E |
| 38_42 | 93 | 91 | E |
| 43_47 | 92 | 88 | E |
| 48_52 | 91 | 80 | E |
| 53_57 | 90 | 73 | E |
| 58_62 | 88 | 63 | E |
| 63_67 | 76 | 40 | E |
| 68 | 72 | 30 | E |

### D.8 Occupation × Asset / media (2024)

P(owns asset | occupation) — smartphone-internet and TV ownership rates by occupation.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 65.0 | 78.0 | C | 2024: Krishak Bandhu online + PM Kisan app; significant smartphone adoption |
| Agricultural_labourer | 50.0 | 68.0 | C | 2024: WhatsApp groups for daily labor markets; significant adoption vs 2021 |
| Household_industry | 65.0 | 78.0 | C | |
| Manufacturing | 75.0 | 87.0 | C | |
| Construction | 72.0 | 82.0 | C | |
| Trade_retail | 88.0 | 93.0 | C | Temple-economy traders; near-saturation |
| Transport_logistics | 82.0 | 87.0 | C | |
| Services | 92.0 | 95.0 | C | Kolkata commuter; near-saturation |
| Government_services_teachers | 95.0 | 97.0 | C | |
| Out_migrant_worker | 92.0 | 90.0 | C | |

### D.9 Education × Workforce participation (2024)

P(unemployed-and-seeking | education) — educated-unemployment proxy. SSC scam (2022) elevated frustration among Secondary/HS/Graduate cohort seeking government jobs.

| Education | Unemployed_seeking | Main_worker_rate | Tier |
|---|---|---|---|
| Illiterate | 2 | 35 | E |
| Primary | 4 | 37 | E |
| Middle | 7 | 35 | E |
| Secondary | 14 | 27 | E |
| Higher_Secondary | 20 | 21 | E |
| Graduate | 24 | 24 | E |
| Postgraduate | 14 | 40 | E |

### D.10 Asset × Bilingualism (2024)

| Asset_tier | Bilingual_Bengali_Hindi | Tier | Source |
|---|---|---|---|
| TV_only_HH | 5 | E | Bengali TV dominant |
| TV_plus_smartphone_HH | 15 | E | Hindi-YouTube + Jio content; increasing from 2021 (12%) |
| Smartphone_only_HH | 10 | E | |
| No_asset_HH | 3 | E | Lowest exposure |
| Population_wide_bilingual | 10 | E | Increase from 2021 (~8%) from digital Hindi content consumption; Tarakeswar Muni Hindi-trader presence |

### D.11 GP × Religion (2024)

P(religion | sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Tarakeswar_Muni_CDB | 89.8 | 8.4 | 0.3 | 1.2 | 0.3 | E | Weighted 2011 projected: Muni + CDB weighted composite; slight Muslim share growth from differential growth |
| U2_Dhaniakhali_5GP | 80.2 | 16.8 | 0.3 | 2.5 | 0.2 | A | Dhaniakhali block Census 2011; 5-GP subset uses block proxy; slight Muslim growth |

### D.12 GP × Caste (2024)

P(caste | sub-unit).

| Sub_unit | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Tarakeswar_Muni_CDB | 22.0 | 4.0 | 10.0 | 36.0 | 19.6 | 8.4 | 0.0 | D |
| U2_Dhaniakhali_5GP | 22.0 | 18.0 | 4.0 | 20.0 | 14.5 | 18.5 | 3.0 | D |

### D.13 GP × Asset / media (2024)

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Tarakeswar_Muni_CDB | 93.0 | 86.0 | 24.0 | 97.0 | C |
| U2_Dhaniakhali_5GP | 72.0 | 62.0 | 6.0 | 90.0 | C |

### D.14 GP × Amenities (2024)

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Tarakeswar_Muni_CDB | 82.0 | 88.0 | 92.0 | 99.5 | C |
| U2_Dhaniakhali_5GP | 42.0 | 62.0 | 82.0 | 97.0 | C |

### D.15 Vote × Religion (2024 LS anchor)

P(party | religion) — anchored on 2024 LS AC-198 segment result (AITC 47.38% / BJP 41.96% / CPI(M) 7.49%). Hooghly PC (Arambagh) stayed TMC. Rachna Banerjee (TMC) won adjacent Hooghly PC; Arambagh PC also TMC. RG Kar protests (Aug 2024) occurred after June 2024 LS result — not reflected.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 48.5 | 42.0 | 0.5 | 6.5 | 2.5 | C | CSDS/ABP Ananda 2024 WB post-poll; Hindu BJP lean moderated vs 2021 peak; Mahishya and Sadgop partial return to TMC for LS |
| Muslim | 2.5 | 86.0 | 1.5 | 8.0 | 2.0 | C | Muslim consolidation behind AITC deepened; BJP further reduced among Muslim voters |
| Sarna_ORP | 38.0 | 44.0 | 0.5 | 14.0 | 3.5 | E | ST vote: AITC ahead; Left residual persists |
| Christian | 28.0 | 57.0 | 5.0 | 7.0 | 3.0 | E | Approximation |
| Other_residual | 38.0 | 48.0 | 2.0 | 5.0 | 7.0 | E | |

### D.16 Vote × Caste (2024 LS anchor)

P(party | caste) — 2024 LS calibration. BJP retreated from 2021 AE peak; TMC welfare consolidation held via Lakshmir Bhandar + PM Kisan (now available). SSC scam created some anti-TMC educated-caste sentiment but did not translate to BJP gain in this AC.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 52.0 | 32.0 | 3.0 | 8.0 | 5.0 | C | UC BJP lean persists but somewhat moderated from 2021 peak; SSC scam frustrated educated class but BJP not the primary beneficiary |
| OBC | 46.0 | 42.0 | 1.0 | 8.0 | 3.0 | D | OBC BJP moderation from 2021; PM Kisan now in TMC's column (WB joined); Lakshmir Bhandar holds Mahishya women |
| └ Mahishya | 48.0 | 40.0 | 1.0 | 8.0 | 3.0 | D | Load-bearing cell; slight BJP retreat from 2021 peak (52%); Hooghly Mahishya BJP plurality maintained but TMC welfare schemes effective |
| └ Sadgop | 42.0 | 46.0 | 1.5 | 8.0 | 2.5 | D | More TMC-leaning; Lakshmir Bhandar holds Sadgop women |
| └ Kurmi | 38.0 | 48.0 | 2.0 | 9.0 | 3.0 | D | OBC welfare loyal; TMC |
| └ Tili_other_OBC | 36.0 | 50.0 | 2.0 | 9.0 | 3.0 | D | Temple-economy traders |
| SC_total | 37.0 | 49.0 | 2.0 | 9.5 | 2.5 | C | SC BJP vote slightly retreating from 2021; TMC welfare and Lakshmir Bhandar for SC women |
| └ Bagdi_SC | 37.0 | 50.0 | 2.0 | 9.0 | 2.0 | C | |
| └ Bauri_SC | 34.0 | 52.0 | 2.0 | 9.5 | 2.5 | C | |
| └ Namasudra_SC | 44.0 | 41.0 | 2.0 | 9.5 | 3.5 | C | Namasudra BJP lean persists; CAA now notified (Mar 2024) but actual citizenship grants minimal; tempered enthusiasm |
| ST_total | 34.0 | 45.0 | 1.0 | 16.5 | 3.5 | C | ST retains Left residual; slight AITC improvement |
| Muslim | 2.5 | 86.0 | 1.5 | 8.0 | 2.0 | C | Same as D.15 |

### D.17 Vote × Gender (2024 LS anchor)

P(party | gender). Lakshmir Bhandar mature penetration (~65% eligible women enrolled by 2024) strongly anchors AITC women's vote. Gender gap wider than any previous election in this AC.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 48.5 | 40.0 | 1.5 | 7.5 | 2.5 | C | CSDS/ABP Ananda 2024 WB post-poll |
| Female | 35.0 | 55.5 | 1.0 | 6.0 | 2.5 | C | Lakshmir Bhandar + Kanyashree + Swasthya Sathi + Krishak Bandhu combination; strongest female TMC lean yet |
| Third_gender | 38.0 | 45.0 | 2.0 | 8.0 | 7.0 | E | Approximation |

---

## E. 2024 LS calibration target (AC 198 Tarakeswar segment)

> **Tier A** — direct extraction from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=198 (`West Bengal`). Electorate: 244,468. Total valid votes: 206,193. Turnout: 84.34%.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| AITC | 47.38 | A | Mitali Bag (Arambagh LS candidate); 97,685 votes; 2024_AssemblySegmentLevelVotingData.csv |
| BJP | 41.96 | A | Arup Kanti Digar (Arambagh LS candidate); 86,517 votes; same CSV |
| LF | 7.49 | A | CPI(M) Biplab Kumar Moitra; 15,436 votes; same CSV |
| INC | 0.00 | A | INC not present in 2024 Arambagh LS for this segment; 0 votes |
| Other_NOTA | 3.18 | A | BSP 469 + SUCI 200 + IND (4 candidates) 3,396 + NOTA 2,490 = 6,555 votes; computed |

> **AITC margin: 11,168 votes (5.42pp)**. TMC gaining. Trend: 2019 LS 2.20pp → 2021 AE 3.63pp → 2024 LS 5.42pp. Slow directional drift; no sharp swings.

---

## F. Vote history (chronological, all elections)

### AC 198 Assembly Election history

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin | Tier |
|---|---|---|---|---|---|---|---|---|---|---|
| 2001 AE | Pratim Chatterjee | Ind (MFB-supported) | 69,186 | 54.55 | Mohan Ghosh | INC | 40,274 | 31.75 | 28,912 | A |
| 2006 AE | Pratim Chatterjee | Ind (MFB-supported) | 74,849 | 58.10 | Krishna Bhattacharjee | BJP | 44,578 | 34.60 | 30,271 | A |
| 2011 AE | Rachhpal Singh | AITC | 97,022 | 55.10 | Pratim Chatterjee | CPI(M) | 71,550 | 40.64 | 25,472 | A |
| 2016 AE | Rachhpal Singh | AITC | 97,588 | 50.75 | Surajit Ghosh | NCP | 69,898 | 36.35 | 27,690 | A |
| 2021 AE | Ramendu Sinharay | AITC | 96,698 | 46.96 | Swapan Dasgupta | BJP | 89,214 | 43.33 | 7,484 | A |

### AC 198 LS segment history

| Year | LS Winner | Party | AC-198 segment % | AC-198 margin (pp) | Tier |
|---|---|---|---|---|---|
| 2019 LS | Aparupa Poddar (Afrin Ali) | AITC | 44.67% AITC / 42.47% BJP | 2.20pp AITC | A |
| 2021 AE | Ramendu Sinharay | AITC | 46.96% AITC / 43.33% BJP | 3.63pp AITC | A |
| **2024 LS** | **Mitali Bag** | **AITC** | **47.38% AITC / 41.96% BJP** | **5.42pp AITC** | **A** |

### Arambagh Lok Sabha (PC 29) history

| Year | Winner | Party | % | Margin | Notes | Tier |
|---|---|---|---|---|---|---|
| 2009 LS | Sakti Mohan Malik | CPI(M) | 54.63 | 201,558 | Left "Red Fort" | A |
| 2014 LS | Aparupa Poddar (Afrin Ali) | AITC | 54.94 | 346,845 | AITC landslide; CPI(M) collapsed | A |
| 2019 LS | Aparupa Poddar (Afrin Ali) | AITC | 44.14 | 1,142 | Closest WB seat; BJP 44.06%; razor margin | A |
| 2024 LS | Mitali Bag | AITC | — | — | TMC held Arambagh; BJP retreated | A |

### Narrative arc (2019-2024)

2019 LS: Razor-margin TMC win (2.20pp AC-198 segment); BJP's Mahishya + UC + Namasudra bloc nearly flipped the seat. 2021 AE: BJP fielded Swapan Dasgupta (national BJP intellectual/Rajya Sabha MP) — gamble on name-recognition failed; AITC's Ramendu Sinharay won by 7,484 votes (3.63pp); Lakshmir Bhandar campaign announcement during election galvanized women voters. 2023-2024: SSC scam (2022) damaged TMC's educated-class image; but RG Kar protests (Aug 2024) occurred after LS election and are post-calibration. 2024 LS: AITC further widened margin to 5.42pp; BJP's 2021 AE peak (43.33%) did not convert to LS victory; Lakshmir Bhandar at ~65% women enrollment matured as structural TMC anchor.

**Model constraint:** This is the truest swing seat in the pilot sample. TMC and BJP within 6pp across all three calibrated elections. No single event caused a sharp swing — the drift is slow, directionally consistent, and driven by structural factors (welfare enrollment, women's vote, Mahishya gradual re-evaluation). The simulation must reproduce small directional shifts, not event-driven volatility.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- `2024_AssemblySegmentLevelVotingData.csv` — ECI GE2024 AC-segment vote tallies (tier A; AC_NO=198 rows used for Section E calibration target)
- ECI 2021 WB Assembly Election archive — AC 198 result (Ramendu Sinharay AITC; Wikipedia Tarakeswar constituency article)
- ECI 2019 LS `2019_AssemblySegmentLevelVotingData.csv` — historical anchor
- Census of India 2011 — Tarakeswar CD Block, Tarakeswar Municipality, Dhaniakhali CD Block
- ECI AE archives 2001/2006/2011/2016/2021 — AC 198 results (via Wikipedia)
- ECI LS archives 2009/2014/2019/2024 — Arambagh PC results (via Wikipedia)

### Secondary sources (tier B/C)
- NFHS-5 (2019-21) WB — asset/media/amenity baseline direction
- CSDS-Lokniti / ABP Ananda 2024 WB post-poll survey — vote × demographics (regional WB rollup)
- WB CDWDSW — Lakshmir Bhandar scheme; enrollment trajectory estimates
- Pew India 2021 — religion-differential growth rate projections
- PIB press releases — PM Kisan WB joining (Apr-Jul 2021); Ujjwala 2.0; Jal Jeevan Mission

### Tertiary / journalistic (tier D)
- Indian Express / ThePrint — SSC scam coverage (Jul 2022); Partha Chatterjee arrest
- Wikipedia "Rachna Banerjee" — Hooghly PC 2024 winner (adjacent PC; context)
- Wikipedia "2024 Indian general election in West Bengal" — Arambagh PC 2024 result
- Wikipedia "RG Kar Medical College and Hospital rape and murder case" — Aug 2024 protests context
- Wikipedia "Bangladesh protests of 2024" — Hasina ouster; Yunus interim government; trade disruption
- Wikipedia "Swapan Dasgupta" — 2021 AE Tarakeswar candidacy
- Press reports — Tarakeswar pilgrim economy revival 2022-2024

### Tier-D/E reliance flags
- **Mahishya vote 2024** (D.16) — key load-bearing cell; 48% BJP / 40% AITC is estimate; tier D; actual CSDS subnational data not obtained
- **Caste sub-group shares** (C.2) — no caste census; 18.1% Mahishya is journalistic inference; ±5pp uncertainty
- **Dhaniakhali 5-GP data** (D.11-D.14) — whole-block proxy; actual 5-GP subset demographics unknown
- **Lakshmir Bhandar penetration** (C.10) — ~65% estimate by end-2024; actual WB CDWDSW dashboard data not fully accessed
- **Asset/media 2024** (C.14) — extrapolated from NFHS-5 2019-21 trajectory; smartphone 80% is estimated; Census HH-13 2024 not available

### v0 known gaps
1. Exact Arambagh PC 2024 party-wise totals and AC-198 specific breakdown beyond the CSV direct read
2. Dhaniakhali 5-GP level demographics — whole-block proxy
3. Lakshmir Bhandar exact enrollment penetration for AC 198 by end-2024
4. CSDS WB 2024 subnational AC-level cross-tabs (vote × caste × sub-unit)
5. Census 2021 / PLFS 2022-24 — not yet available; projections from Census 2011 carry high tier-E uncertainty by 2024

---

## H. Post-2024 validation anchors

> No post-2024 validation anchors fetched in v0. The 2026 WB Assembly Election result (AC 198 Tarakeswar) is the primary forward-looking out-of-sample gate.

### 2026 AE (out-of-sample — to be populated after election)
| Field | Value | Tier |
|---|---|---|
| Election | 2026 WB Assembly Election — AC 198 Tarakeswar | — |
| Result | TBD | — |
| Target AITC pct | ~47-49% (slow drift continuation) | E |
| Target BJP pct | ~41-43% | E |
| Calibration threshold | ±3pp on each major party | E |

---

*v0 — generated 2026-04-28, frozen at end-2024 state-of-knowledge. No post-2024 events referenced.*
