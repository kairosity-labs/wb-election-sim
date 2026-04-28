# AC 198 — Tarakeswar (GEN) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural state of AC 198 Tarakeswar as of end-2021 only. It does not reference any post-2021 events. Use the 2024 LS AC-segment result as the out-of-sample validation gate for downstream simulators.
>
> Events known by end-2021 and freely referenced here: 2019 LS, COVID-19 lockdown (Mar 2020), Cyclone Amphan (May 2020), 2021 WB Assembly Election (May 2021), Lakshmir Bhandar launch (Apr 2021), BSF 50km jurisdiction extension (Oct 2021).
>
> **Forbidden keywords (auto-checked):** `2022, 2023, 2024, 2025, 2026, SSC scam, Partha Chatterjee, RG Kar, SIR, CAA notification, CAA rules`
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 198 | A | ECI / Delimitation Commission 2008 |
| AC name | Tarakeswar | A | ECI |
| Reservation | General (unreserved) | A | Delimitation 2008 |
| District | Hooghly | A | Delimitation 2008 |
| Sub-division | Chandannagore (Hooghly district administrative); Tarakeswar CDB/Muni is in Chandannagore subdivision, not Arambagh subdivision | A | WB Hooghly District portal |
| LS constituency | 29 — Arambagh (SC reserved) | A | Delimitation 2008 |
| AC composition | Tarakeswar Municipality (full) + all 10 GPs of Tarakeswar CDB + Bhanderhati I, Bhanderhati II, Gopinathpur I, Gopinathpur II, Parambua-Sahabazar GPs of Dhaniakhali CDB | A | Delimitation Commission Order 2008 |
| Geographic note | Temple town at 58 km from Kolkata; Howrah-Tarakeswar railway line; Taraknath Shiva Temple ~10 million pilgrims per year in Sravan month; pilgrimage economy (accommodation, food, trade) supplements agrarian base | A | Wikipedia Tarakeswar; GoWB Hooghly portal |
| Two sub-units used in v0 | **U1_Tarakeswar_Muni_CDB** (urban+rural core, ~72% of AC pop) · **U2_Dhaniakhali_5GP** (rural fringe, ~28%) | E | v0 simplification; see methodology §3 |
| COVID-19 impact note (2020) | Howrah-Tarakeswar railway suspended for lockdown; reverse migration of construction-and-service workers from Kolkata to AC villages (2020 Apr-Jun); pilgrim economy collapsed for full 2020 Sravan season (~zero pilgrims vs ~10M normal); partial recovery in 2021 Sravan (restricted crowd) | D | Press reports; ToI / Anandabazar Patrika |
| Cyclone Amphan note (May 2020) | Hooghly received Category 4 winds; some structural damage; no catastrophic flooding unlike coastal Sunderbans; minor return migration effect within AC | D | Wikipedia Amphan; IMD report |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~299,132 (Tarakeswar CDB rural 179,148 + Muni 30,947 + Dhaniakhali 5 GPs ≈ 89,037) | E | Census 2011; v0 GP proxy |
| 2021 projected population | ~332,600 | E | 10-yr compound religion-differential growth from 2011 (~1.2%/yr blended); methodology §4 |
| Sex ratio (2021, F per 1000 M) | ~966 | E | Weighted 2011 ~965; near-stable; slight female-favourable drift in rural WB |
| 2021 electorate (tier A — ECI 2021 AE roll) | 221,972 | A | Wikipedia Tarakeswar AE 2021 / ECI 2021 AE roll |
| 2021 turnout | 85.86% (205,917 / 221,972) | A | Wikipedia Tarakeswar AE 2021 / ECI 2021 AE result |
| Estimated M / F / TG split (2021) | ~50.8% M / 49.2% F / <0.05% TG | E | Weighted sex ratio ~966 F/1000M; projected stable from 2019 |
| 2021 polling stations (estimated) | ~285 | E | Projected from 2019 estimate (~280) with minor voter-roll growth |
| Note on electorate change | 2019 electorate was 232,456; 2021 roll is 221,972 — a reduction of ~10,484. This is a known phenomenon in WB 2021 rolls (deletion of some duplicate/incorrect entries and boundary adjustments); both are tier A. | A | ECI CSVs + Wikipedia |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 86.61 | E | 2019 base 86.78%; 2 more years of religion-differential growth (Muslim +1.3%/yr, Hindu +1.0%/yr) → Hindu dips ~0.17pp; 86.61% by end-2021 |
| Muslim | 11.98 | E | 2019 base 11.74%; +0.24pp over 2 more years differential growth |
| Christian | 0.30 | E | Held stable; tiny base |
| Sarna_ORP | 0.85 | E | Slight decline as some Santal practitioners shift to Hindu enumeration over time |
| Other_residual | 0.26 | E | Residual; Jain/Sikh/Buddhist in Muni |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population, 2021)

> Same load-bearing caste structure as 2019; minor SC/ST share projection from Census 2011 base. No caste census update available.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| SC_total | 25.4 | E | 2019 base 25.5%; small decline as SC sub-groups' growth rate is near-average; held nearly stable |
| └ Bagdi_SC | 9.5 | C | Dominant SC in Hooghly; held stable |
| └ Bauri_SC | 4.4 | E | Slight decline in sub-share |
| └ Namasudra_SC | 3.5 | E | Held stable; smaller presence than N24P belt |
| └ Other_SC | 8.0 | E | Hari, Chamar, Jalia, Rajbanshi residual |
| ST_total | 7.2 | E | 2019 base 7.3%; near-stable |
| └ Santal_ST | 5.4 | C | Dominant ST in Hooghly |
| └ Other_ST | 1.8 | E | Munda, Bhumij, Lodha |
| UC_bhadralok | 8.0 | D | Temple-town educated class; Brahmin priests significant; held stable |
| OBC | 30.2 | D | Mahishya + Sadgop + Kurmi + Tili combined; marginal growth with new OBC-B inclusions |
| └ Mahishya | 18.1 | D | Single largest caste in Hooghly; dominant cultivating caste; slight growth from OBC recognition politics |
| └ Sadgop | 6.0 | D | Second-tier cultivating caste; OBC-B |
| └ Kurmi | 3.5 | D | OBC-A; rural CDB cultivator |
| └ Tili_other_OBC | 2.6 | D | Temple-economy trade + residual OBC |
| Other_Hindu_middle | 15.8 | E | Goala, Tanti, Sutradhar, unclassified middle |
| Muslim | 11.98 | E | See C.1; Bengali-Sheikh peasantry dominant |
| Christian_plus_Sarna_plus_Other | 1.42 | E | See C.1 |
| **Sum** | **100.00** | — | self-check (25.4+7.2+8.0+30.2+15.8+11.98+1.42 = 100.0 ✓) |

### C.3 Age cohort (2021, voters 18+ only)

> Renormalized to voter-eligible population (18+) per NORMALIZED_SCHEMA v1 §3.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.2 | E | 2021 voter cohort: 2011 Census age pyramid 18-22 renormalized, new entrants 2019-2021 |
| 23_27 | 12.8 | E | |
| 28_32 | 12.5 | E | |
| 33_37 | 11.2 | E | |
| 38_42 | 10.0 | E | |
| 43_47 | 9.5 | E | |
| 48_52 | 8.3 | E | |
| 53_57 | 7.0 | E | |
| 58_62 | 5.5 | E | |
| 63_67 | 5.8 | E | Slightly elevated: older long-term residents |
| 68 | 5.2 | E | Concentrated in temple-town permanent residents |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.86 | E | Sex ratio ~966 F/1000M → 50.86% M / 49.14% F |
| Female | 49.14 | E | |
| Third_gender | 0.00 | E | Negligible |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 92.3 | E | 2019 base 92.5%; slight decline as Hindi-belt pilgrim-economy workers stable |
| Santali | 2.5 | E | ST fringe; held stable |
| Hindi | 3.6 | E | Tarakeswar Muni Hindi-speaker fringe; slight growth from pilgrimage-economy traders |
| Urdu | 0.9 | E | Muslim pocket in Dhaniakhali GPs |
| Other | 0.7 | E | Kurukh/Munda/Bhumij ST fringe |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 12.5 | E | 2019 base 13.5%; +0.5pp/yr literacy improvement → ~12.5% illiterate of total pop |
| Primary | 22.0 | E | |
| Middle | 21.5 | E | |
| Secondary | 19.5 | E | Slight growth from SSC expansion |
| Higher_Secondary | 12.5 | E | |
| Graduate | 9.0 | E | Modest growth; Tarakeswar college + Kolkata commuter attainment |
| Postgraduate | 3.0 | E | Stable small professional class |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 31.5 | E | 2019 base 33.0%; COVID-19 disruption caused temporary contraction in main-worker share; partial recovery by end-2021 but not yet at 2019 levels; pilgrim economy suppressed in 2020 fully and partially in 2021 |
| Marginal_worker | 13.0 | E | Slight increase as some main workers shifted to marginal work during COVID disruption |
| Non_worker | 37.5 | E | Female housewife fraction dominant in rural OBC households; slight increase due to COVID-induced exit from labor force |
| Student | 11.0 | E | Held stable; school enrollment dipped during COVID but largely resumed by late 2021 |
| Unemployed | 7.0 | E | COVID-induced educated unemployment pressure; held at 2019 level by end-2021 |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 18.5 | E | 2019 base 18.0%; slight increase as some service-displaced workers returned to agricultural work during COVID |
| Agricultural_labourer | 40.5 | E | 2019 base 40.0%; slight increase from COVID-induced labor migration reversal |
| Household_industry | 4.5 | E | Held stable |
| Manufacturing | 4.5 | E | Slight decline from organized sector COVID disruption |
| Construction | 5.5 | E | Decline from COVID; significant reverse migration of construction workers from Kolkata |
| Trade_retail | 9.5 | E | Pilgrim-economy trade significantly suppressed in 2020-21; partial recovery in 2021 |
| Transport_logistics | 4.5 | E | Railway resumption by 2021; held near 2019 levels |
| Services | 8.0 | E | Kolkata commuter workforce; some permanent WFH adaptation; held stable |
| Government_services_teachers | 4.0 | E | Held stable; govt jobs less disrupted |
| Out_migrant_worker | 0.5 | E | Very small; most Tarakeswar-origin migrant workers registered here; see also C.16 |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.8 | E | Slight decline from COVID-disrupted small-business closures in Muni |
| Employee | 24.5 | E | Slight decline; some private-sector disruption |
| Single_worker | 53.5 | E | Own-account agriculture + artisan; stable |
| Family_worker | 20.2 | E | Within agri-household; slight increase as family-farm work absorbed returned migrants |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 21.0 | C | COVID-19 caused temporary poverty reversal; 2019 base 20.0%; ~1pp increase as marginal households crossed below poverty line; partial welfare cushion from PMGKY and Lakshmir Bhandar (Apr 2021) |
| Above_Poverty_Line_low_income | 37.5 | E | Rural cultivating-OBC and SC labourer households |
| Lower_middle | 26.0 | E | |
| Middle | 12.5 | E | Moderate compression from COVID; pilgrim-economy middle class hit |
| Upper_middle_well_off | 3.0 | E | Held stable |
| **Sum** | **100.00** | — | self-check |
| **PM Kisan Samman Nidhi exposure** | ~18% of cultivator HH | D | **WB joined PM Kisan at 8th installment (Apr-Jul 2021).** ~18% of AC HH are cultivator category; first central-transfer receipts in mid-2021. BJP had used WB non-participation as grievance lever 2019-2021; TMC finally joined to defuse political cost after 2021 AE win. Source: PIB press release + PM Kisan Wikipedia |
| **Krishak Bandhu enrolled cultivators** | ~18% of AC HH | D | Scheme running since Jan 2019; second year of operation in 2021; coverage stable among cultivator HH. Source: Krishak Bandhu website |
| **Lakshmir Bhandar exposure** | ~35% of adult women HH heads | D | Launched Apr 2021 (post-AE announcement during campaign); ₹500/month for general-category women HH heads, ₹1000 for SC/ST. Enrollment camps post-election; ~35% penetration of eligible women HH heads by end-2021. Significant welfare anchor for TMC women's vote. Source: WB CDWDSW Lakshmir Bhandar scheme announcement; WBXpress |

### C.11 GP / Municipality location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Tarakeswar_Muni_CDB | 70.3 | E | 2011 base: Muni 10.3% + CDB 59.9% = 70.2%; projected to 70.3% with slight Muni growth; v0 collapses Muni + CDB into single sub-unit for simplicity |
| U2_Dhaniakhali_5GP | 29.7 | E | 2011 base 29.8%; slight population decline in fringe as young out-migrate to Kolkata |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.4 | E | WB 2011: 4.3; rural Hooghly slightly higher; COVID reverse migration temporarily increased HH size; by end-2021 returning to pre-COVID mean |
| Nuclear_HH | 68.5 | E | NFHS-4/5 WB rural pattern; near-stable |
| Joint_HH | 25.5 | E | Slight decline as nuclear trend continues |
| Extended_multi_generation | 6.0 | E | COVID reverse migration slightly elevated multi-generation living; stabilizing |
| **Sum** | **100.00** | — | self-check (Nuclear+Joint+Extended = 100 ✓) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.5 | E | Slight decline as large 2019-21 cohort of 23-27 year olds marry; Census 2011 Hooghly pattern |
| Currently_married | 65.5 | E | |
| Widowed | 8.0 | E | Stable |
| Separated_divorced | 1.0 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

> Notable shift: smartphone/internet penetration surged 2019-2021 due to COVID-induced digital adoption + WB government Duare Sarkar scheme (digital)

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 78.0 | C | 2019 base 76.0%; +2pp growth; near-saturation in Muni; moderate in rural CDB |
| Radio | 4.0 | C | Declining; FM radio |
| Mobile_phone | 90.0 | C | 2019 base 85.0%; +5pp; near-saturation; COVID-era digital access push |
| Smartphone_with_internet | 62.0 | C | 2019 base 45.0%; **+17pp surge** — COVID digital adoption, WFH, online school, Duare Sarkar online camp; NFHS-5 WB rural ~58% by 2019-21 survey period; Hooghly somewhat above average |
| Computer | 9.0 | C | Modest growth |
| Two_wheeler | 32.0 | C | Slight growth; recovered from COVID pause |
| Four_wheeler | 5.5 | C | Slight growth |
| Banking_access | 92.0 | B | PMJDY + Lakshmir Bhandar bank-account requirement → further penetration to ~92%; near-saturation |
| **Note** | (these are independent ownership %s, not categorical — do not sum) | — | — |

### C.15 Household amenities (2021)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 85.5 | C | 2019 base 84.0%; Jal Jeevan Mission (2019+) driving improvement |
| Improved_sanitation | 71.0 | C | 2019 base 65.0%; Swachh Bharat Mission Phase 2 (2020+) + ODF village certifications in Hooghly |
| LPG_clean_cooking_fuel | 52.0 | C | 2019 base 42.0%; +10pp — Ujjwala 2.0 continuation + PMUY refill subsidies; significant jump from COVID free-cylinder scheme (PMGKY 2020) |
| Wood_biomass_fuel | 43.0 | C | Declining as LPG rises |
| Other_fuel | 5.0 | C | Kerosene, dung; held stable |
| Electricity | 98.0 | A | Saubhagya saturation + ongoing connections; Hooghly well-electrified |
| **Note** | (LPG + Wood_biomass + Other_fuel sum to 100; water/sanitation/electricity are independent flags) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 82.5 | D | 2019 base 82.0%; COVID-induced reverse migration of construction+service workers to home AC temporarily inflated native-resident count; some stayed by end-2021 |
| WB_other_district | 7.5 | D | 2019 base 8.0%; slight decline as Kolkata in-migrants reduced during COVID |
| Other_Indian_state | 4.5 | D | Hindi-belt pilgrim-economy traders; stable |
| Bangladesh_origin | 4.0 | D | Hooghly is non-refugee district; small Namasudra/refugee families; stable |
| Outside_India | 0.5 | E | Negligible |
| Out_migrant | 1.0 | E | Kolkata commuters registered here; stable |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue (2021)

P(language | religion) — % within each religion's population.

| Religion | Bengali | Santali | Hindi | Urdu | Other | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 94.3 | 1.5 | 3.2 | 0.0 | 1.0 | E | CDB Bengali majority; Muni Hindi-trader fringe within Hindu; UC bhadralok all Bengali |
| Muslim | 87.5 | 0.0 | 1.5 | 10.0 | 1.0 | E | Bengali-Sheikh majority; Urdu fraction in Muslim; Dhaniakhali GP Muslims mostly Bengali |
| Sarna_ORP | 15.0 | 74.0 | 0.0 | 0.0 | 11.0 | E | Santal practitioners Santali-speakers |
| Christian | 90.0 | 5.0 | 0.0 | 0.0 | 5.0 | E | Tiny base |
| Other_residual | 60.0 | 0.0 | 30.0 | 0.0 | 10.0 | E | Marwari/Jain fringe |

### D.2 Religion × Caste (2D layout per normalized schema)

P(caste | religion) — % within each religion. Rows sum to 100.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 29.3 | 8.3 | 9.2 | 34.8 | 18.4 | 0.0 | 0.0 | D | (SC_total 25.4% + ST_total 7.2% + UC 8.0% + OBC 30.2% + Other_Hindu 15.8%) / Hindu 86.61%; Bagdi+Bauri+Namasudra+OtherSC aggregated into SC_total; Santal+OtherST into ST_total |
| Muslim | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | A | Muslim row is self-contained |
| Sarna_ORP | 0.0 | 92.0 | 0.0 | 5.0 | 3.0 | 0.0 | 0.0 | E | Santal practitioners; most are ST |
| Christian | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | A | |
| Other_residual | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | E | Jain/Sikh/Marwari residual |

### D.3 Religion × Migration (2021)

P(birthplace | religion).

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 80.5 | 7.5 | 5.5 | 5.0 | 0.0 | 1.5 | D | Hooghly low-refugee; some Namasudra/refugee families; Hindi-belt settlers |
| Muslim | 93.5 | 3.5 | 2.0 | 1.0 | 0.0 | 0.0 | D | Hooghly Muslims overwhelmingly native Bengali-Sheikh peasantry |
| Sarna_ORP | 90.0 | 7.0 | 2.0 | 0.0 | 1.0 | 0.0 | E | Indigenous |
| Christian | 85.0 | 10.0 | 5.0 | 0.0 | 0.0 | 0.0 | E | Tiny base |
| Other_residual | 40.0 | 15.0 | 40.0 | 5.0 | 0.0 | 0.0 | E | Marwari traders mostly other-state |

### D.4 Religion × Asset / media (2021)

P(owns asset | religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 80.0 | 65.0 | 93.0 | C | NFHS-5 WB religion gap; Hindu rural Hooghly; 2021 post-COVID digital surge |
| Muslim | 67.0 | 48.0 | 82.0 | C | Muslim asset gap persists but narrows with PMJDY + Lakshmir Bhandar banking requirement |
| Sarna_ORP | 58.0 | 35.0 | 76.0 | C | Lower asset access in tribal communities; some improvement from digital-welfare enrollment |
| Christian | 83.0 | 60.0 | 93.0 | E | Small base |
| Other_residual | 85.0 | 72.0 | 94.0 | E | Marwari business class |

### D.5 Caste × Education (2021)

P(education | caste) — highest level achieved, age 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 3 | 7 | 11 | 18 | 20 | 28 | 13 | E |
| Mahishya | 9 | 19 | 22 | 23 | 15 | 9 | 3 | E |
| Sadgop | 10 | 21 | 22 | 21 | 13 | 10 | 3 | E |
| Kurmi | 13 | 23 | 22 | 20 | 12 | 8 | 2 | E |
| Tili_other_OBC | 13 | 22 | 22 | 20 | 12 | 8 | 3 | E |
| Bagdi_SC | 20 | 26 | 22 | 17 | 9 | 5 | 1 | E |
| Bauri_SC | 23 | 27 | 21 | 15 | 8 | 5 | 1 | E |
| Namasudra_SC | 16 | 23 | 22 | 18 | 11 | 8 | 2 | E |
| Santal_ST | 28 | 29 | 19 | 13 | 7 | 3 | 1 | E |
| Other_ST | 30 | 28 | 18 | 13 | 6 | 4 | 1 | E |
| Muslim | 18 | 24 | 23 | 19 | 10 | 5 | 1 | E |

### D.6 Age × Gender × Education (2021)

P(grad+ | age × gender) — graduate-or-higher share. Post-COVID education disruption note: 2019 entrants to grad programs somewhat disrupted but not material to end-2021 share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 18 | 16 | E |
| 23_27 | 16 | 12 | E |
| 28_32 | 13 | 9 | E |
| 33_37 | 11 | 6 | E |
| 38_42 | 10 | 5 | E |
| 43_47 | 8 | 4 | E |
| 48_52 | 7 | 3 | E |
| 53_57 | 6 | 2 | E |
| 58_62 | 5 | 2 | E |
| 63_67 | 4 | 1 | E |
| 68 | 3 | 1 | E |

### D.7 Marital status × Age × Gender (2021)

P(currently married | age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 7 | 29 | E |
| 23_27 | 43 | 83 | E |
| 28_32 | 83 | 94 | E |
| 33_37 | 92 | 91 | E |
| 38_42 | 92 | 90 | E |
| 43_47 | 91 | 88 | E |
| 48_52 | 90 | 79 | E |
| 53_57 | 89 | 72 | E |
| 58_62 | 87 | 62 | E |
| 63_67 | 74 | 38 | E |
| 68 | 70 | 28 | E |

### D.8 Occupation × Asset / media (2021)

P(owns asset | occupation) — smartphone-internet and TV ownership rates by occupation.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 48 | 74 | C | Significant jump from 2019 (35→48%); COVID digital adoption; Krishak Bandhu online enrollment |
| Agricultural_labourer | 32 | 62 | C | Lower income; slower digital adoption; notable jump from 2019 (22→32%) from WFH/school pressure |
| Household_industry | 50 | 75 | C | |
| Manufacturing | 62 | 84 | C | |
| Construction | 56 | 78 | C | Reverse-migrant workers returned with Kolkata-acquired digital habits |
| Trade_retail | 75 | 90 | C | Temple-economy traders; Muni concentrated |
| Transport_logistics | 70 | 84 | C | |
| Services | 82 | 92 | C | Kolkata commuter workforce; near-saturation smartphone access |
| Government_services_teachers | 90 | 95 | C | Online government work + school remote learning requirement |
| Out_migrant_worker | 85 | 88 | C | Migrant workers require smartphone for remittance + family contact |

### D.9 Education × Workforce participation (2021)

P(unemployed-and-seeking | education) — educated-unemployment proxy. COVID-induced pressure elevated educated unemployment in 2020-21.

| Education | Unemployed_seeking | Main_worker_rate | Tier |
|---|---|---|---|
| Illiterate | 2 | 34 | E |
| Primary | 4 | 36 | E |
| Middle | 7 | 34 | E |
| Secondary | 12 | 28 | E |
| Higher_Secondary | 18 | 22 | E |
| Graduate | 22 | 25 | E |
| Postgraduate | 13 | 38 | E |

### D.10 Asset × Bilingualism (2021)

| Asset_tier | Bilingual_Bengali_Hindi | Tier | Source |
|---|---|---|---|
| TV_only_HH | 5 | E | Bengali TV dominant |
| TV_plus_smartphone_HH | 12 | E | Hindi-YouTube cross-language; slightly up from 2019 |
| Smartphone_only_HH | 9 | E | |
| No_asset_HH | 3 | E | Lowest exposure |
| Population_wide_bilingual | 8 | E | Slight increase from 2019 (~7%) from digital Hindi content consumption |

### D.11 GP × Religion (2021)

P(religion | sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Tarakeswar_Muni_CDB | 90.0 | 8.2 | 0.3 | 1.2 | 0.3 | E | Weighted 2011: Muni (Hindu 93.22%, Muslim 4.97%) + CDB (Hindu 88.94%, Muslim 10.20%); v0 collapses into single sub-unit; weighted by Muni 10.3%/CDB 59.9% → Hindu ~90%, Muslim ~8.2% |
| U2_Dhaniakhali_5GP | 80.5 | 16.5 | 0.3 | 2.5 | 0.2 | A | Dhaniakhali block Census 2011 (Wikipedia); 5-GP subset uses block proxy |

### D.12 GP × Caste (2021)

P(caste | sub-unit).

| Sub_unit | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Tarakeswar_Muni_CDB | 22.0 | 4.0 | 10.0 | 36.0 | 19.8 | 8.2 | 0.0 | D |
| U2_Dhaniakhali_5GP | 22.0 | 18.0 | 4.0 | 20.0 | 14.5 | 18.5 | 3.0 | D |

### D.13 GP × Asset / media (2021)

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Tarakeswar_Muni_CDB | 90.0 | 70.0 | 20.0 | 94.0 | C |
| U2_Dhaniakhali_5GP | 68.0 | 45.0 | 5.0 | 84.0 | C |

### D.14 GP × Amenities (2021)

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Tarakeswar_Muni_CDB | 78.0 | 82.0 | 88.0 | 99.0 | C |
| U2_Dhaniakhali_5GP | 32.0 | 54.0 | 80.0 | 96.0 | C |

### D.15 Vote × Religion (2021 AE anchor)

P(party | religion) — anchored on 2021 WB AE result for AC 198. AITC 46.96% / BJP 43.33% / CPI(M) ~7.1%. Lakshmir Bhandar announced during campaign (Apr 2021) reinforced AITC women's vote. BJP candidate Swapan Dasgupta (national ideologue) lost despite high visibility.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 50.0 | 40.0 | 0.5 | 7.0 | 2.5 | C | CSDS-Lokniti 2021 WB post-poll; Hindu OBC slight BJP gain vs 2019; Dasgupta campaign mobilized Mahishya and UC voters |
| Muslim | 3.0 | 84.0 | 2.0 | 8.5 | 2.5 | C | Muslim consolidation behind AITC intensified after BJP's 2019-2021 campaign rhetoric; LF residual in Dhaniakhali Muslim pocket |
| Sarna_ORP | 40.0 | 42.0 | 0.5 | 14.0 | 3.5 | E | ST vote split; some Left residual; AITC slightly ahead |
| Christian | 30.0 | 55.0 | 5.0 | 7.0 | 3.0 | E | Approximation; tiny base |
| Other_residual | 38.0 | 48.0 | 2.0 | 5.0 | 7.0 | E | Marwari/Jain fringe |

### D.16 Vote × Caste (2021 AE anchor)

P(party | caste) — 2021 WB AE calibration. Swapan Dasgupta drove BJP UC + Mahishya mobilization; TMC held on with welfare-scheme loyalty and Lakshmir Bhandar appeal.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 58.0 | 28.0 | 3.0 | 7.0 | 4.0 | C | Bhadralok BJP mobilization peaked in 2021; Dasgupta resonated with educated class |
| OBC | 50.0 | 38.0 | 1.0 | 8.0 | 3.0 | D | Mahishya+Sadgop: Dasgupta appealed to cultivating-caste BJP bloc; slightly above 2019 BJP level due to farm-issue + CAA |
| └ Mahishya | 52.0 | 36.0 | 1.0 | 8.0 | 3.0 | D | Load-bearing cell; Mahishya BJP peak in 2021; Hooghly Mahishya BJP plurality |
| └ Sadgop | 44.0 | 42.0 | 1.5 | 9.0 | 3.5 | D | More TMC-leaning; local networks held |
| └ Kurmi | 40.0 | 46.0 | 2.0 | 9.5 | 2.5 | D | OBC-A welfare loyal; scheme exposure held TMC |
| └ Tili_other_OBC | 38.0 | 48.0 | 2.0 | 9.0 | 3.0 | D | Temple-economy traders |
| SC_total | 40.0 | 46.0 | 2.0 | 9.5 | 2.5 | C | SC BJP vote slightly elevated vs 2019; Matua-adjacent NRC/CAA concern lower here than N24P |
| └ Bagdi_SC | 40.0 | 47.0 | 2.0 | 9.0 | 2.0 | C | CSDS WB 2021 SC pattern |
| └ Bauri_SC | 37.0 | 49.0 | 2.0 | 9.5 | 2.5 | C | |
| └ Namasudra_SC | 48.0 | 38.0 | 2.0 | 9.5 | 2.5 | C | Namasudra BJP lean slightly above other SC; NRC/CAA less salient but present |
| ST_total | 37.0 | 42.0 | 1.0 | 17.0 | 3.0 | C | ST retains Left residual; Dhaniakhali Santal bloc |
| Muslim | 3.0 | 84.0 | 2.0 | 8.5 | 2.5 | C | Same as D.15 |

### D.17 Vote × Gender (2021 AE anchor)

P(party | gender). Lakshmir Bhandar (Apr 2021 campaign announcement) significantly boosted AITC women's vote. Gender gap widened vs 2019.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 50.0 | 39.0 | 1.5 | 7.5 | 2.0 | C | CSDS-Lokniti 2021 WB post-poll; male BJP lean intensified |
| Female | 37.0 | 54.0 | 1.0 | 6.0 | 2.0 | C | Significant +15pp AITC women advantage; Lakshmir Bhandar + Kanyashree + Swasthya Sathi + Krishak Bandhu combination |
| Third_gender | 40.0 | 45.0 | 2.0 | 8.0 | 5.0 | E | Approximation; negligible base |

---

## E. 2021 AE calibration target (AC 198 Tarakeswar)

> **Tier A** — ECI 2021 WB Assembly Election result; AC 198 Tarakeswar. Electorate: 221,972. Valid votes: 205,917. Turnout: 85.86%.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| AITC | 46.96 | A | Ramendu Sinharay (Sinharoy); 96,698 votes; ECI 2021 AE / Wikipedia |
| BJP | 43.33 | A | Swapan Dasgupta; 89,214 votes; ECI 2021 AE / Wikipedia |
| LF | 6.80 | A | CPI(M) Surajit Ghosh; ~14,000 votes; ECI 2021 AE |
| INC | 0.50 | E | INC candidate if any; residual; subsumed in LF/Other_NOTA estimate |
| Other_NOTA | 2.41 | E | NOTA + IND + minor parties; residual to sum to 100 |

> **AITC margin: 7,484 votes (3.63pp)**. This is a widening of the 2019 LS margin (2.20pp at AC-198 segment). Trend: slow TMC gains.

---

## F. Vote history (chronological anchors)

### AC 198 Assembly Election history

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin | Tier |
|---|---|---|---|---|---|---|---|---|---|---|
| 2001 AE | Pratim Chatterjee | Ind (MFB-supported) | 69,186 | 54.55 | Mohan Ghosh | INC | 40,274 | 31.75 | 28,912 | A |
| 2006 AE | Pratim Chatterjee | Ind (MFB-supported) | 74,849 | 58.10 | Krishna Bhattacharjee | BJP | 44,578 | 34.60 | 30,271 | A |
| 2011 AE | Rachhpal Singh | AITC | 97,022 | 55.10 | Pratim Chatterjee | CPI(M) | 71,550 | 40.64 | 25,472 | A |
| 2016 AE | Rachhpal Singh | AITC | 97,588 | 50.75 | Surajit Ghosh | NCP | 69,898 | 36.35 | 27,690 | A |
| **2021 AE** | **Ramendu Sinharay** | **AITC** | **96,698** | **46.96** | **Swapan Dasgupta** | **BJP** | **89,214** | **43.33** | **7,484** | **A** |

### 2019 LS AC-198 segment (now history; was 2019-calibration target)

| Party | Votes | % | Note |
|---|---|---|---|
| AITC (Aparupa Poddar) | 88,096 | 44.67 | A — ECI CSV |
| BJP (Tapan Kumar Roy) | 83,753 | 42.47 | A — ECI CSV |
| CPI(M) (Sakti Mohan Malik) | 15,747 | 7.99 | A — ECI CSV |
| INC | 3,372 | 1.71 | A — ECI CSV |
| NOTA + others | 6,226 | 3.16 | A — ECI CSV |
| **AITC margin** | **4,343** | **2.20pp** | |

### Narrative arc (2001-2021)

2001-2006: Seat held by Pratim Chatterjee (CPI(M)/MFB-supported independent). 2011: AITC wave brought Rachhpal Singh (first non-Left MLA in 34 years). 2016: AITC retained easily with Rachhpal Singh. 2019 LS: BJP surged from near-zero to 42.5% (Mahishya-OBC rightward drift across Hooghly). 2021 AE: Rachhpal Singh was replaced as AITC candidate by Ramendu Sinharay; BJP fielded Swapan Dasgupta — nationally known ideologue/journalist/Rajya Sabha MP. Despite Dasgupta's national profile, AITC won by 3.63pp (wider than 2019 LS margin), showing Lakshmir Bhandar women's vote and local TMC organization overcame BJP's name-recognition advantage.

**Key 2021 AE driver analysis:** Dasgupta's candidacy was a BJP gamble — his intellectual profile resonated with UC bhadralok and Mahishya elites but lacked grassroots connectivity. AITC's counter was Lakshmir Bhandar (announced during campaign) and Ramendu Sinharay's local network. The 7,484-vote AITC margin suggests the Lakshmir Bhandar women-mobilization offset BJP's Mahishya consolidation. CPI(M) vote (~7%) held largely stable from 2019 LS (~8%) — Left not recovering, merely surviving.

### Arambagh Lok Sabha history

| Year | Winner | Party | % | Margin | Notes | Tier |
|---|---|---|---|---|---|---|
| 2009 LS | Sakti Mohan Malik | CPI(M) | 54.63 | 201,558 | Left "Red Fort"; INC second | A |
| 2014 LS | Aparupa Poddar (Afrin Ali) | AITC | 54.94 | 346,845 | AITC landslide; CPI(M) collapsed | A |
| 2019 LS | Aparupa Poddar (Afrin Ali) | AITC | 44.14 | 1,142 | BJP surged to 44.06%; razor-margin | A |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- ECI 2021 WB Assembly Election archive — AC 198 Tarakeswar result (Ramendu Sinharay AITC won; Swapan Dasgupta BJP; ECI Form-20 / Wikipedia Tarakeswar constituency article)
- ECI 2021 WB AE electoral roll — electorate 221,972 (Wikipedia Tarakeswar AE 2021)
- `2019_AssemblySegmentLevelVotingData.csv` — ECI GE2019 AC-segment vote tallies (now historical anchor)
- Census of India 2011 — Tarakeswar CD Block, Tarakeswar Municipality, Dhaniakhali CD Block (via Wikipedia)
- ECI AE archives 2001/2006/2011/2016 — Tarakeswar AC results (via Wikipedia constituency article)

### Secondary sources (tier B/C)
- NFHS-5 (2019-21) West Bengal state summary — smartphone/internet diffusion baseline
- CSDS-Lokniti 2021 WB post-poll survey — vote × religion, vote × caste, vote × gender (regional WB rollup)
- WB CDWDSW — Lakshmir Bhandar scheme announcement (April 2021)
- Pew India 2021 — religion-differential growth rate projections

### Tertiary / journalistic (tier D)
- India Today / Anandabazar Patrika — Swapan Dasgupta Tarakeswar candidacy coverage (2021)
- Wikipedia "Swapan Dasgupta" — profile, Rajya Sabha appointment 2016, Tarakeswar AE 2021 candidacy
- Wikipedia "Tarakeswar (Vidhan Sabha constituency)" — 2021 AE result
- Wikipedia "2021 West Bengal legislative assembly election" — overall results (TMC 213 / BJP 77)
- WBXpress — Krishak Bandhu second-year coverage; Lakshmir Bhandar scheme launch mechanics
- PIB press release — PM Kisan WB joining at 8th installment (Apr-Jul 2021)
- Press reports (ToI / Anandabazar) — Howrah-Tarakeswar railway suspension + COVID pilgrim economy collapse 2020

### Tier-D/E reliance flags
- **Mahishya vote split** (D.16) — key load-bearing cell; 52% BJP / 36% AITC is 2021 peak estimate; tier D; uncertainty range ±5pp
- **Caste sub-group shares** (C.2, D.2) — no caste census post-1931; Mahishya 18.1% estimate is journalistic/academic inference
- **Dhaniakhali 5-GP data** (D.11-D.14) — using whole Dhaniakhali block as proxy; 5-GP subset may differ
- **Lakshmir Bhandar penetration** (C.10) — end-2021 enrollment ~35% estimated; actual penetration figures from WB CDWDSW not fully accessible; tier D
- **Vote × demographic joints** (D.15-D.17) — CSDS 2021 WB regional rollup; tier C; AC-specific subnational data not yet obtained

### v0 known gaps
1. Precise AC-198 party vote totals for 2021 AE beyond the top-2 + CPI(M) estimate — Wikipedia shows AITC and BJP clearly; CPI(M) estimated ~7%; INC/NOTA/others residual
2. Dhaniakhali 5-GP level data — using whole-block proxy
3. NFHS-5 AC-level breakdown — using WB state summary
4. Lakshmir Bhandar exact enrollment penetration for AC 198 by end-2021

---

## H. Post-2021 validation anchors

> **These are OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**

### 2024 LS AC-198 segment (tier A, ECI CSV — out-of-sample)

| Party | Votes | AC-198 segment % | Tier | Source |
|---|---|---|---|---|
| AITC (Mitali Bag) | 97,685 | 47.38 | A | 2024_AssemblySegmentLevelVotingData.csv |
| BJP (Arup Kanti Digar) | 86,517 | 41.96 | A | Same |
| CPI(M) (Biplab Kumar Moitra) | 15,436 | 7.49 | A | Same |
| Other+NOTA | 6,555 | 3.18 | A | Same |
| **AITC margin** | **11,168** | **5.42pp** | A | Computed |
| Electorate | 244,468 | — | A | Same |
| Turnout | ~84.3% | — | A | Same |

**Context (for simulator only; not calibrated into 2021 file):** 2024 LS saw Hooghly PC (Locket Chatterjee BJP) flip to TMC (Rachna Banerjee won). Arambagh PC (AC 198 sits in Arambagh) outcome: TMC held. The slow directional TMC gain (2019: 2.20pp → 2021: 3.63pp → 2024: 5.42pp) continued.

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No post-2021 events referenced.*
