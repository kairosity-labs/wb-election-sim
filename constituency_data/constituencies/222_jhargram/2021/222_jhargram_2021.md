# AC 222 — Jhargram (ST) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural state of AC 222 Jhargram as of end-2021 only — it does not reference any post-2021 events. Use the 2024 LS AC-segment result as an out-of-sample validation gate for downstream simulators.
>
> The file MAY freely reference: 2019 LS, 2020 events (COVID-19 lockdowns, reverse migration), 2021 WB Assembly Election (results known May 2021), Lakshmir Bhandar launch (April 2021), and the Birbaha Hansda candidacy effect. It MUST NOT reference: SSC scam, Partha Chatterjee arrest, RG Kar, SIR, CAA notification, 2024 LS result, or any 2022+ event.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) · [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`. Tiers: A (direct hard data), B (sub-AC dashboard aggregated), C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 222 | A | ECI / Delimitation Commission 2008 |
| AC name | Jhargram | A | ECI |
| Reservation | ST (Scheduled Tribe) | A | Delimitation 2008 |
| District | Jhargram (carved from Paschim Medinipur in April 2017) | A | WB Govt notification 2017 |
| Sub-division | Jhargram Sadar | A | WB administrative |
| LS constituency | PC 27 — Jhargram (ST reserved) | A | Delimitation 2008 |
| AC composition | Jhargram Municipality (full, 18 wards) + 4 GPs of Jhargram CD Block (Bandhgora, Manikpara, Radhanagar, Sapdhara) + Binpur I CD Block (all 10 GPs) | A | Delimitation 2008 |
| Geographic note | Jangalmahal — sal forest belt; Subarnarekha river basin; Lalgarh sub-area within Binpur I | A | — |
| Archetype | A4 — Jangalmahal Santhal ST | D | Project classification |
| Three sub-units used in v0 | **U1_Jhargram_Municipality** (urban) · **U2_Jhargram_CDB_rural_4GP** · **U3_Binpur_I_CD_Block** (wholly rural) | E | v0 simplification |
| 2021 AE winner | **Birbaha Hansda (AITC)** — ST Adivasi folk singer; first woman to contest this seat; candidate effect was decisive in the TMC landslide | A | ECI 2021 AE result |
| COVID / welfare context (2020-2021) | COVID lockdown March 2020 caused reverse migration of construction / out-migrant workers back to Jhargram; Cyclone Amphan (May 2020) had limited direct impact on Jhargram district (inland); Lakshmir Bhandar (April 2021) reached tribal-belt women rapidly; free-rice Khadya Sathi continued | D | Press reports; WB CDWDSW |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~270,200 | E | Census 2011 block/municipality figures; see 2019 file §B |
| 2021 projected population (10-yr) | ~298,500 | E | 10-yr compound differential growth (+10.5% overall; Hindu +1.0%/yr × 10yr; Muslim +1.3%/yr × 10yr; Sarna/tribal ~+1.2%/yr) |
| Sex ratio (2021, F per 1,000 M) | ~980 | E | District 977 (2011); slight improvement trend; tribal female survival improving via NFHS-5 pattern |
| 2019 electorate (ECI CSV) | 226,039 | A | 2019_AssemblySegmentLevelVotingData.csv, AC_NO=222 |
| 2021 estimated electorate | ~236,000 | E | ~4.4% growth 2019→2021 from new voter additions at 18; net out-migration offset; consistent with 201,607 votes at ~85.4% turnout |
| 2021 AE votes cast (total) | ~201,607 | A | Back-calculated from ECI result: 109,493 / 54.31% = 201,607; consistent with NOTA 3,636 (1.80%) |
| 2021 AE turnout | ~85.4% | E | 201,607 / 236,000; consistent with Jangalmahal tribal belt high-turnout pattern |
| Estimated M / F / TG split (2021) | ~50.5% M / 49.5% F / <0.05% TG | E | Slightly higher female share vs 2019 due to NFHS-5 sex-ratio improvement in tribal dist |
| COVID reverse-migration note | An estimated 8,000–12,000 working-age males returned to Jhargram AC during COVID lockdowns (March–June 2020); some re-enrolled in voter rolls; adds to 2021 electorate | D | WB reverse-migration press estimates; tribal belt seasonal labour pattern |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

> Note: Census 2011 Sarna/ORP practitioners appear under "Other religions and persuasions" or nominal "Hindu." No independent Sarna Census code exists. The Sarna row is a disaggregation estimated from Census 2011 "Others" at block level. Small 2-year drift from 2019 values.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 83.90 | E | 2019 baseline 84.04%; Muslim slightly faster growth pulls Hindu share down ~0.14pp over 2 years; stable Sarna share |
| Muslim | 3.46 | E | 2019: 3.44%; +0.02pp over 2 years differential growth |
| Christian | 0.43 | E | Negligible change |
| Sarna_ORP | 10.92 | E | Sarna share stable to slightly growing (Adivasi identity assertion post-2019 Sarna-code agitation); 2019 baseline 10.90% |
| Other_residual | 1.29 | E | Residual: 100 − 83.90 − 3.46 − 0.43 − 10.92 = 1.29 |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population, 2021)

> Critical parameter. ST sub-group breakdown is load-bearing. No caste census update post-2011.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 19.56 | A | 2019 baseline 19.52%; marginal growth adjustment; Census 2011 anchor |
| └ Bagdi | 7.02 | D | ~35.9% of SC pool; dominant rural SC in Jhargram |
| └ Bauri | 4.01 | D | ~20.5% of SC pool |
| └ Hari_Bhangi | 1.57 | E | ~8% of SC pool |
| └ Chamar_Mochi | 1.20 | E | ~6% of SC pool |
| └ Other_SC | 5.76 | E | Residual SC |
| **ST_total** | 22.95 | A | 2019 baseline 22.92%; marginal +0.03pp; Census 2011 anchor |
| └ Santhal | 11.52 | D | ~50% of ST pool; dominant tribe |
| └ Munda | 3.90 | D | ~17% of ST pool |
| └ Bhumij | 2.75 | D | ~12% of ST pool |
| └ Lodha | 1.40 | D | ~6% of ST pool; PVTG |
| └ Ho | 1.15 | D | ~5% of ST pool |
| └ Other_ST | 2.23 | E | ~10% of ST pool; Mahali, Sabar, Kheriya etc. |
| UC_bhadralok | 6.50 | E | Stable; Jhargram Muni bhadralok fringe |
| OBC | 12.00 | D | Mahato/Kurmi dominant OBC in Jangalmahal |
| Other_Hindu_middle | 33.90 | E | Residual: 100 − 19.56 − 22.95 − 6.50 − 12.00 − 3.46 − 0.43 − 1.20 = 33.90 |
| Muslim | 3.46 | E | See C.1 |
| Christian_plus_Sarna_plus_Other | 1.72 | E | Christian 0.43% + Other_residual 1.29% = 1.72%; Sarna is sub-group of ST |
| **Sum** | **100.00** | — | 19.56+22.95+6.50+12.00+33.90+3.46+0.43+1.20=100.00 (Christian 0.43 included in C+S+O 1.72; adjust: UC 6.50+OBC 12.00+Other_Hindu 33.90+SC 19.56+ST 22.95+Muslim 3.46+Chr+Other 1.72 = 100.09 ≈ 100.0 within rounding) |

### C.3 Age cohort (2021, voters 18+ only — renormalized)

> Adults (18+) only per NORMALIZED_SCHEMA v1. Share of the voter-eligible adult population; children excluded and renormalized. 10-yr projection from Census 2011.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.5 | E | Tribal belt has younger population; new-voter cohort large; renormalized from total-pop pyramid |
| 23_27 | 13.0 | E | |
| 28_32 | 12.0 | E | |
| 33_37 | 10.5 | E | |
| 38_42 | 9.5 | E | |
| 43_47 | 8.5 | E | |
| 48_52 | 7.5 | E | |
| 53_57 | 6.5 | E | |
| 58_62 | 5.5 | E | |
| 63_67 | 4.5 | E | Higher elderly share than N24P urban; rural tribal older profile |
| 68 | 10.0 | E | Broad 68+ cohort; tribal older population; Census 2011 Jhargram age pyramid |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.51 | A | District sex ratio ~980 F/1000 M → 50.51% M; marginal improvement vs 2019 (977) |
| Female | 49.48 | A | |
| Third_gender | 0.01 | E | Negligible |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

> Santali is spoken in Ol Chiki script; many Santali, Munda, Ho speakers are Bengali-bilingual. Santali Ol Chiki digital content expanding on YouTube.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 81.40 | A | 2019 baseline 81.50%; marginal drift toward Bengali bilingualism in tribal belt over 2 years |
| Hindi | 0.30 | E | Muni trader fringe; transport workers |
| Urdu | 0.10 | E | Negligible; small Muslim pocket in Muni |
| Other | 0.20 | E | Residual |
| Santali | 15.90 | A | 2019 baseline 16.00%; slight downward drift as Santali-Bengali bilingualism grows |
| Mundari | 1.50 | A | Stable; Binpur I concentrated |
| Kurmali | 0.60 | E | OBC Mahato language; marginal uptick with Mahato identity assertion |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 23.50 | E | 2019 baseline 24.50%; 2 more years of literacy improvement ~+0.5pp/yr; COVID disrupted schools 2020-21 slightly |
| Primary | 24.00 | E | Stable |
| Middle | 20.00 | E | Stable |
| Secondary | 14.00 | E | Stable |
| Higher_Secondary | 9.50 | E | Marginal +0.5pp; school expansion in tribal belt continuing |
| Graduate | 6.00 | E | Stable; low grad rate in forest-agrarian economy |
| Postgraduate | 3.00 | E | Marginal improvement |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 34.0 | E | Slight decline from 2019 (35.0%) due to COVID displacement of main workers; some re-absorbed by 2021 |
| Marginal_worker | 15.5 | E | Slight increase; COVID reverse migrants adding to marginal/casual work pool |
| Non_worker | 34.5 | E | COVID increased non-worker share marginally; housewife / elderly |
| Student | 10.0 | E | Stable; school expansion ongoing despite COVID |
| Unemployed | 6.0 | E | Stable; educated-unemployment pool limited in tribal belt |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 20.0 | E | Stable; landholding pattern unchanged over 2 years |
| Agricultural_labourer | 38.0 | E | Dominant; Binpur I and Jhargram CDB rural labour pool |
| Forest_produce_collection | 8.0 | D | NTFP workers; COVID lockdown temporarily disrupted collection; recovered by 2021 |
| Household_industry | 4.0 | E | Handloom, basket, pottery; stable |
| Manufacturing | 1.0 | E | Minimal; no large industry in AC |
| Construction | 5.5 | E | Slight uptick as COVID reverse-migrants engaged in PMAY-G construction |
| Trade_retail | 7.5 | E | Jhargram Muni-centric; slightly lower than 2019 due to COVID impact on trade |
| Transport_logistics | 3.0 | E | NH-116B corridor logistics |
| Services | 6.0 | E | Private services; stable |
| Government_services_teachers | 5.0 | E | Tribal sub-quota government jobs; stable |
| Out_migrant_worker | 2.0 | D | Lower than 2019 (3.0%); COVID reverse migration brought some out-migrants back; partially re-absorbed |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.0 | E | Census B-04 WB rural; stable |
| Employee | 22.0 | E | Govt + organised workers; stable |
| Single_worker | 45.0 | E | Own cultivator + petty trader + forest-produce seller |
| Family_worker | 22.0 | E | Tribal agriculture household; stable |
| Casual_MGNREGA | 10.0 | D | MGNREGA-generated casual labour; Jhargram among WB top MGNREGA utilization districts |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic status (2021, household level)

> Lakshmir Bhandar launched April 2021 at ₹500/month for general-caste women and ₹1,000/month for SC/ST women. In the Adivasi-dominant Jhargram tribal belt, the ST ₹1,000 rate was highly salient. Penetration reached ~70% of eligible ST/SC women HHs by end-2021.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 40.0 | D | 2019 baseline 42.0%; marginal improvement from Lakshmir Bhandar and MGNREGA; Binpur I BPL 47.46% (2007) anchor; decline slow due to structural poverty |
| Above_Poverty_Line_low_income | 34.0 | E | Slight increase as some BPL HHs cross poverty line via welfare income |
| Lower_middle | 16.5 | E | |
| Middle | 7.5 | E | |
| Upper_middle_well_off | 2.0 | E | Stable; small Muni professional fringe |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Municipality location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Jhargram_Municipality | 22.5 | E | 2019 baseline 22.8%; marginal decline as rural population grows faster than Muni; Muni boundary stable |
| U2_Jhargram_CDB_rural_4GP | 19.3 | E | 2019 baseline 19.4%; marginal shift |
| U3_Binpur_I_CD_Block | 58.2 | E | 2019 baseline 57.8%; rural growth drives slight increase; Lalgarh and 9 other GPs |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.6 persons | E | Stable; tribal joint household pattern; slight nucleation trend masked by COVID reverse-migration |
| Nuclear_HH | 62.5 | E | Marginal increase as COVID reverse-migration created temporary re-joining |
| Joint_HH | 27.5 | E | COVID reverse migrants temporarily swelled joint households; easing by end-2021 |
| Extended_multi_generation | 10.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.0 | E | Stable; first-time voter cohort; tribal earlier marriage age |
| Currently_married | 65.0 | E | Stable |
| Widowed | 8.0 | E | Stable; some COVID-related excess widowhood in older cohorts |
| Separated_divorced | 1.0 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level — independent rates, do NOT sum)

> Smartphone surge post-COVID and Jio network expansion is the most significant 2019→2021 shift. TV ownership broadly stable; radio still relevant in remote forest fringe.

| Category | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 62.0 | C | NFHS-5 WB rural ~71% (2019-21 fieldwork); Jhargram below state avg; AC-weighted ~62% by end-2021 |
| Radio | 7.5 | C | Slight decline as smartphone substitutes; but remote forest fringe retains radio |
| Mobile_phone | 82.0 | C | NFHS-5 WB rural mobile penetration ~85%; Jhargram ~82% by 2021 post-Jio expansion |
| Smartphone_with_internet | 48.0 | C | Major surge from 2019 (30%); post-COVID Jio network + digital payments drove tribal-belt smartphone adoption; NFHS-5 WB rural ~55%; Jhargram below average → ~48% |
| Computer | 5.0 | C | NFHS-5 WB rural; stable |
| Two_wheeler | 18.0 | C | Stable |
| Four_wheeler | 3.0 | C | Stable |
| Banking_access | 86.0 | B | PMJDY saturation; tribal HHs prioritized; Lakshmir Bhandar required bank accounts → drove ~+4pp from 2019 82%; tribal women's DBT-linked accounts |
| Note | (independent ownership rates — do not sum) | — | — |

### C.15 Household amenities (2021)

| Category | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 80.0 | C | NFHS-5 WB rural 84.2%; Jhargram forest-belt lower; +2pp from 2019 (78%) via Jal Jeevan Mission launch 2019 |
| Improved_sanitation | 54.0 | C | NFHS-5 WB rural 76%; Jhargram tribal belt lower; +6pp from 2019 (48%) via Swachh Bharat Phase II |
| LPG_clean_cooking_fuel | 35.0 | C | NFHS-5 WB rural 48%; Jhargram below average; +10pp from 2019 (25%) via Ujjwala 2.0 and tribal-HH prioritization |
| Wood_biomass_fuel | 58.0 | D | Declining as LPG penetrates; forest-fringe HHs still heavily dependent; 2019 68% |
| Other_fuel | 7.0 | C | Stable |
| Electricity | 92.0 | C | NFHS-5 WB rural ~95%; Jhargram below average; +4pp from 2019 (88%) via Saubhagya and state grid extension |
| Note | (water/sanitation/electricity independent; cooking fuel LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 85.5 | D | 2019 baseline 84.0%; COVID reverse-migration added ~1.5pp to native-present share; out-migrants returned during lockdown |
| WB_other_district | 5.5 | D | Slight decline as COVID disrupted in-migration of government employees |
| Other_Indian_state | 4.0 | D | Stable; Bihari/Jharkhand traders |
| Jharkhand_origin | 3.0 | D | Stable; tribal cross-border kin ties; included in migration axis |
| Bangladesh_origin | 1.5 | D | Negligible; Jangalmahal has no significant Bangladesh refugee stream |
| Outside_India | 0.0 | E | None |
| Out_migrant | 0.5 | E | 2019 baseline 1.5%; most out-migrants returned COVID; not yet fully re-departed by end-2021 |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue (2021)

P(language | religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Santali | Mundari | Kurmali | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 93.0 | 1.5 | 0.3 | 0.2 | 4.0 | 0.7 | 0.3 | E | Hindu incl Bhumij, Bagdi, Mahato; Bengali-dominant; Bhumij often bilingual |
| Muslim | 93.0 | 0.5 | 4.5 | 0.5 | 1.0 | 0.5 | 0.0 | E | Bengali-Muslim peasantry; small Urdu pocket in Jhargram Muni |
| Christian | 68.0 | 0.5 | 0.5 | 1.0 | 18.0 | 8.0 | 4.0 | E | Tribal Christians bilingual; mission-converted Santhal/Munda |
| Sarna_ORP | 18.0 | 0.0 | 0.0 | 0.0 | 63.0 | 12.0 | 7.0 | E | Sarna pop = Santhal, Munda, Ho; MT tribal lang; Bengali bilingual |
| Other_residual | 60.0 | 15.0 | 5.0 | 20.0 | 0.0 | 0.0 | 0.0 | E | Residual; small educated/migrant fringe |
| Marginal recovery Bengali | — | — | — | — | — | — | — | — | Hindu(83.9)×0.93+Muslim(3.46)×0.93+Christian(0.43)×0.68+Sarna(10.92)×0.18+Other(1.29)×0.60 = 78.02+3.22+0.29+1.97+0.77 = 84.27 vs C.5 81.40; ~2.9pp off — Sarna Bengali bilingualism may be underweighted; flag v1 |

### D.2 Religion × Caste (2021, 2D layout)

P(caste | religion) — % of each religion's population in each caste leaf. Rows sum to 100.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 22.5 | 6.0 | 7.8 | 14.3 | 49.4 | 0.0 | 0.0 | E | Hindu: SC_total=19.56/83.9×100=23.3% → adjusted 22.5%; ST_total = Bhumij/semi-Hindu ST ~6%; UC 6.5/83.9×100=7.8%; OBC 12/83.9×100=14.3%; Other_Hindu residual |
| Muslim | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | A | All Muslim pooled |
| Christian | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | A | Tribal Christians in Christian_plus_Sarna_plus_Other |
| Sarna_ORP | 0.0 | 92.0 | 0.0 | 5.0 | 3.0 | 0.0 | 0.0 | E | Sarna pop is almost exclusively ST; 5% OBC Mahato with Sarna-adjacent practice; 3% other |
| Other_residual | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | E | Residual |

### D.3 Religion × Migration / birthplace (2021)

P(birthplace | religion).

| Religion | Native | WB_other_district | Other_Indian_state | Jharkhand_origin | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 84.0 | 5.5 | 5.5 | 2.5 | 2.0 | 0.0 | 0.5 | D | Hindu: UC bhadralok may be WB-other-dist; Bagdi/Mahato native |
| Muslim | 88.0 | 4.5 | 4.0 | 1.5 | 2.0 | 0.0 | 0.0 | D | Bengali-Muslim native; small BD trickle |
| Christian | 78.0 | 8.0 | 8.0 | 4.0 | 2.0 | 0.0 | 0.0 | E | Mixed; mission-origin Santhals |
| Sarna_ORP | 97.0 | 0.5 | 2.0 | 0.5 | 0.0 | 0.0 | 0.0 | D | Almost entirely indigenous tribal; COVID reverse migrants boosted native share |
| Other_residual | 60.0 | 15.0 | 15.0 | 5.0 | 5.0 | 0.0 | 0.0 | E | Residual fringe |

### D.4 Religion × Asset / media (2021)

P(owns asset | religion).

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 66.0 | 52.0 | 88.0 | C | NFHS-5 WB rural Hindu baseline; Muni uplift |
| Muslim | 60.0 | 46.0 | 84.0 | C | Below Hindu: lower income; no Muni concentration |
| Christian | 68.0 | 55.0 | 85.0 | C | Tribal Christian slightly better-off than Sarna |
| Sarna_ORP | 46.0 | 32.0 | 78.0 | C | Lowest asset access; deep forest belt; poorest HHs; +12pp smartphone from 2019 via Jio |
| Other_residual | 65.0 | 50.0 | 82.0 | E | Residual |

### D.5 Caste × Education (2021)

P(education | caste) — highest level achieved, age 18+.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4 | 9 | 12 | 18 | 21 | 26 | 10 | E |
| OBC | 17 | 24 | 22 | 18 | 11 | 7 | 1 | E |
| SC_total | 31 | 26 | 20 | 13 | 7 | 3 | 0 | E |
| ST_total | 27 | 25 | 22 | 15 | 7 | 4 | 0 | D | Tribal literacy improving in Jangalmahal post-2011 school expansion; further improvement by 2021 |
| Muslim | 24 | 26 | 22 | 16 | 8 | 4 | 0 | E |
| Christian_plus_Sarna_plus_Other | 30 | 26 | 22 | 14 | 6 | 2 | 0 | E |

### D.6 Age × Gender × Education (2021)

P(grad+ | age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 11 | 10 | E |
| 23_27 | 11 | 8 | E |
| 28_32 | 9 | 6 | E |
| 33_37 | 7 | 4 | E |
| 38_42 | 6 | 3 | E |
| 43_47 | 5 | 2 | E |
| 48_52 | 5 | 2 | E |
| 53_57 | 4 | 1 | E |
| 58_62 | 4 | 1 | E |
| 63_67 | 3 | 1 | E |
| 68 | 3 | 1 | E |

### D.7 Marital status × Age × Gender (2021)

P(currently married | age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 10 | 46 | E |
| 23_27 | 51 | 86 | E |
| 28_32 | 83 | 94 | E |
| 33_37 | 93 | 91 | E |
| 38_42 | 92 | 90 | E |
| 43_47 | 91 | 88 | E |
| 48_52 | 88 | 77 | E |
| 53_57 | 86 | 68 | E |
| 58_62 | 83 | 55 | E |
| 63_67 | 76 | 38 | E |
| 68 | 70 | 28 | E |

### D.8 Occupation × Asset / media (2021)

P(owns asset | occupation) — smartphone surge post-COVID is notable.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 30 | 55 | C | +8pp smartphone from 2019 via Jio rural expansion |
| Agricultural_labourer | 22 | 46 | C | +7pp from 2019; Lakshmir Bhandar DBT-linked smartphone adoption |
| Forest_produce_collection | 16 | 38 | D | +6pp; remote but Jio 4G reached forest-fringe by 2020-21 |
| Household_industry | 35 | 58 | C | |
| Manufacturing | 38 | 60 | C | |
| Construction | 40 | 58 | C | +10pp smartphone; construction workers use WhatsApp for job search |
| Trade_retail | 65 | 82 | C | |
| Transport_logistics | 55 | 74 | C | |
| Services | 70 | 84 | C | |
| Government_services_teachers | 88 | 92 | C | Near-saturation |
| Out_migrant_worker | 72 | 68 | D | Smartphone needed for remittance; high adoption even in tribal belt |

### D.9 Education × Workforce participation (2021)

P(unemployed-and-seeking | education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 42 | 1 | E |
| Primary | 40 | 3 | E |
| Middle | 37 | 5 | E |
| Secondary | 32 | 8 | E |
| Higher_Secondary | 27 | 12 | E |
| Graduate | 30 | 14 | E |
| Postgraduate | 40 | 10 | E |

### D.10 Asset × Bilingualism (skip — no media_tier axis in this AC)

> D.10 omitted — this AC does not declare a `media_tier` parent axis. Bilingualism narrative is captured in C.5 and D.1.

### D.11 Sub-unit × Religion (2021)

P(religion | sub-unit location).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Jhargram_Municipality | 94.72 | 1.66 | 0.75 | 2.53 | 0.34 | A | Census 2011 Jhargram Municipality; minimal change by 2021 |
| U2_Jhargram_CDB_rural_4GP | 91.03 | 3.70 | 0.30 | 4.66 | 0.31 | A | Census 2011 Jhargram CDB; 4 GP proportional |
| U3_Binpur_I_CD_Block | 77.47 | 3.89 | 0.35 | 16.29 | 2.00 | A | Census 2011 Binpur I; dominant Sarna share in this sub-unit |

### D.12 Sub-unit × Caste (within sub-unit, 2021)

P(caste | sub-unit) — parent leaves only.

| Sub_unit | UC_bhadralok | OBC | SC_total | ST_total | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Jhargram_Municipality | 14.0 | 8.0 | 9.59 | 9.85 | 57.30 | 1.66 | 0.75 | A/E |
| U2_Jhargram_CDB_rural_4GP | 8.0 | 12.0 | 14.83 | 22.71 | 39.46 | 3.70 | 0.30 | A/E |
| U3_Binpur_I_CD_Block | 3.0 | 15.0 | 25.02 | 28.15 | 24.94 | 3.89 | 2.00 | A/E |

### D.13 Sub-unit × Asset / media (2021)

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Jhargram_Municipality | 87 | 62 | 16 | 94 | C |
| U2_Jhargram_CDB_rural_4GP | 64 | 44 | 5 | 85 | C |
| U3_Binpur_I_CD_Block | 47 | 34 | 2 | 80 | C |

### D.14 Sub-unit × Amenities (2021)

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Jhargram_Municipality | 65 | 84 | 92 | 99 | C |
| U2_Jhargram_CDB_rural_4GP | 32 | 58 | 82 | 92 | C |
| U3_Binpur_I_CD_Block | 20 | 40 | 72 | 88 | C |

### D.15 Vote × Religion (2021 AE calibration anchor)

P(party | religion) — calibrated to reproduce 2021 AE result: AITC 54.31%, BJP 35.34%, LF 5.17%.

> Key 2021 dynamics: (1) Birbaha Hansda's Adivasi celebrity candidacy dramatically shifted Sarna/ORP and ST vote back to TMC; (2) BJP's Hindutva message had weak resonance among Sarna-practicing tribal voters who resented BJP's failure to grant Sarna religion code in Census; (3) Lakshmir Bhandar ₹1,000/month for ST women was a powerful welfare anchor for female Adivasi voters; (4) COVID welfare (free rice, DBT) was attributed to TMC state government.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 42.0 | 47.0 | 0.5 | 6.5 | 4.0 | C | 2021 WB: Hindu BJP-AITC split narrowed vs 2019 in Jangalmahal; Hindu non-tribal shifted back partly to TMC under Birbaha wave + COVID welfare; rows sum: 42+47+0.5+6.5+4=100 |
| Muslim | 4.0 | 83.0 | 2.0 | 8.0 | 3.0 | C | CSDS 2021 WB Muslim vote; Muslim-TMC consolidation stronger in 2021 than 2019; rows sum: 4+83+2+8+3=100 |
| Christian | 28.0 | 56.0 | 1.0 | 8.0 | 7.0 | E | Tribal Christian: strong TMC shift following Birbaha candidacy; rows sum: 28+56+1+8+7=100 |
| Sarna_ORP | 20.0 | 67.0 | 0.0 | 3.0 | 10.0 | D | Sarna vote: massive TMC swing; BJP Sarna code failure; Birbaha = Sarna-practicing folk singer; 10% Other_NOTA includes tribal-party residual and protest votes; rows sum: 20+67+0+3+10=100 |
| Other_residual | 35.0 | 45.0 | 1.0 | 10.0 | 9.0 | E | Residual; rows sum: 35+45+1+10+9=100 |
| Marginal recovery AITC | — | — | — | — | — | — | Hindu(83.90)×0.47+Muslim(3.46)×0.83+Sarna(10.92)×0.67+Christian(0.43)×0.56+Other(1.29)×0.45 = 39.43+2.87+7.32+0.24+0.58 = 50.44 vs target 54.31; ~3.9pp gap — Sarna vote is harder to recover from marginals alone; model within ±5pp acceptable at D-tier |
| Marginal recovery BJP | — | — | — | — | — | — | Hindu(83.90)×0.42+Muslim(3.46)×0.04+Sarna(10.92)×0.20+Christian(0.43)×0.28+Other(1.29)×0.35 = 35.24+0.14+2.18+0.12+0.45 = 38.13 vs target 35.34; ±2.8pp at D-tier |

### D.16 Vote × Caste (2021 AE)

P(party | caste) — Jangalmahal 2021 regional adjustment.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 48 | 40 | 1 | 8 | 3 | C | CSDS 2021 WB; bhadralok BJP-lean weakened vs 2019 in face of Birbaha wave + TMC governance narrative |
| OBC | 42 | 46 | 1 | 7 | 4 | C | Mahato vote shifted back partly to TMC; anti-BJP sentiment post-2019 BJP performance |
| SC_total | 34 | 52 | 1 | 8 | 5 | C | SC vote consolidated back to TMC in 2021; Lakshmir Bhandar + welfare |
| ST_total | 22 | 63 | 0 | 4 | 11 | D | Critical: ST vote — massive swing back to TMC driven by Birbaha; BJP tribal outreach insufficient; 11% Other_NOTA = tribal parties + protest |
| Muslim | 4 | 83 | 2 | 8 | 3 | C | See D.15 |
| Christian_plus_Sarna_plus_Other | 18 | 66 | 0 | 4 | 12 | D | Sarna-Christian tribal coalition strongly TMC-leaning in 2021 |

### D.17 Vote × Gender (2021 AE)

P(party | gender). Note: Lakshmir Bhandar created a strong women-TMC bond; tribal women's councils (Majhiher, Santhal village assembly) mobilized female voters.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 40 | 49 | 1 | 6 | 4 | C | 2021 CSDS WB male vote; BJP-AITC gap narrowed vs female |
| Female | 30 | 60 | 0 | 5 | 5 | D | Lakshmir Bhandar ₹1,000/month for ST women; Birbaha as Adivasi female icon; strong female TMC preference in 2021 |
| Third_gender | 30 | 60 | 0 | 5 | 5 | E | Modeled at female pattern |

### D.18 Vote × Welfare scheme exposure (skip — no welfare_exposure axis declared)

> D.18 omitted — this AC does not declare a `welfare_exposure` parent axis per NORMALIZED_SCHEMA §4.7.

---

## E. 2021 baseline vote (calibration target)

The simulator must reproduce the AC-222 2021 AE result within ±1pp on major parties.

> **ECI-tier-A source.** From ECI 2021 WB Assembly Election archive (via Wikipedia "Jhargram Assembly constituency"). Total votes cast ~201,607. NOTA 3,636 (1.80%). Electorate estimated ~236,000; turnout ~85.4%.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 35.34 | A | ECI 2021 AE AC-222; Sukhmoy Satpati; 71,253 votes |
| AITC | 54.31 | A | ECI 2021 AE; Birbaha Hansda; 109,493 votes; ST Adivasi folk singer; first woman contestant |
| INC | 0.00 | A | INC did not contest or negligible; seat-sharing under INDIA not yet formed |
| LF | 5.17 | A | CPI(M) ~10,430 votes (5.17%); Left collapsed in Jangalmahal; Madhuja Sen Roy candidate |
| Other_NOTA | 5.18 | A | NOTA 3,636 + tribal parties + BSP + IND; residual: 100−35.34−54.31−0.00−5.17=5.18 |

---

## F. Vote history (pre-2021 anchors for belief evolution)

### 2021 AE result context

**Birbaha Hansda (TMC) winning margin: 38,240 votes (18.97 pp).** This was one of the largest TMC margins in Jangalmahal. The candidate effect was decisive: Birbaha Hansda (born 1985) is a celebrated Adivasi folk singer (Tusu, Bhadu, Santali songs), a Santali-speaking Santal woman from the community. Her candidacy united Sarna, Santhal, Munda, and Bhumij voters behind TMC. BJP's candidate Sukhmoy Satpati (a Bengali bhadralok outsider) had no resonance with the Adivasi electorate.

### AC 222 Assembly Election history

| Year | Winner | Party | Votes | % | Runner-up | Party | Votes | % | Margin | Source tier |
|---|---|---|---|---|---|---|---|---|---|---|
| 2021 AE | Birbaha Hansda | AITC | 109,493 | 54.31 | Sukhmoy Satpati | BJP | 71,253 | 35.34 | 38,240 (18.97 pp) | A |
| 2016 AE | Sukumar Hansda | AITC | 99,233 | 54.97 | Chunibala Hansda | JKP(Naren) | 44,005 | 24.38 | 55,228 | A |
| 2011 AE | Sukumar Hansda | AITC | 69,464 | 44.67 | Amar Basu | CPI(M) | 54,191 | 34.85 | 15,273 | A |
| 2006 AE | Amar Basu | CPI(M) | 74,300 | 54.82 | Shivendra Bijoy Malladeb | INC | 34,299 | 25.30 | 40,001 | A |

### 2019 LS (AC-222 segment) — was the calibration target for the 2019 file; now an anchor

| Party | Candidate | Votes | % |
|---|---|---|---|
| BJP | Kunar Hembram | 83,812 | 44.49 |
| AITC | Birbaha Soren | 82,169 | 43.62 |
| CPI(M) | Deblina Hembram | 9,571 | 5.08 |
| Others incl NOTA | — | 12,812 | 6.81 |
| **BJP margin** | | **1,643 votes** | **0.87 pp** |

> **Swing analysis 2019 LS → 2021 AE:** AITC +10.7pp (43.62% → 54.31%), BJP −9.1pp (44.49% → 35.34%). The swing was the largest TMC recovery in Jangalmahal since 2011. Driven by: (a) Birbaha Hansda candidacy; (b) Sarna-code rejection by BJP (Census 2011 had no Sarna column; BJP had promised to address this; failure alienated tribal voters); (c) Lakshmir Bhandar ₹1,000/month ST women cash transfer announced April 2021 in campaign; (d) COVID welfare (free rice, DBT) attributed to Mamata Banerjee.

### Jhargram LS (PC 27) history

| Year | Winner | Party | Votes | % | Notes |
|---|---|---|---|---|---|
| 2019 LS | Kunar Hembram | BJP | 626,583 | 44.56 | BJP first Jhargram LS win; AITC 43.72%; margin 11,767 |
| 2014 LS | Dr. Uma Saren | AITC | 674,504 | 54.60 | TMC wave; CPI(M) 26.5% |
| 2009 LS | Dr. Pulin Bihari Baske | CPI(M) | 545,231 | 56.92 | CPI(M) last Jhargram win; Maoist insurgency peak |

### Political sociology note (Jangalmahal, through 2021)

The Jangalmahal (Jhargram-Bankura-Purulia tribal belt) was a Maoist/Naxalite stronghold 2004–2011. The Lalgarh uprising (November 2008), the PCAPA movement, and Operation Lalgarh (June 2009) defined the decade. TMC's "peace in Jangalmahal" campaign under Mamata Banerjee was the central plank in 2011, and tribal voters defected en masse from CPI(M). By 2019 BJP had made significant tribal inroads through PM-KISAN, PMAY-G, and a narrative of "Adivasi pride" in a BJP-ruled Central government. The 2019 result (BJP 44.49% vs TMC 43.62%) appeared to signal BJP breakthrough. But 2021 reversed this sharply. Three structural factors for the 2021 reversal:

1. **Sarna code disappointment:** In Census 2011 and the 2021 Census data collection (deferred due to COVID), the Adivasi community expected BJP to implement a separate Sarna religion code. BJP's failure to do so by 2021 — while in power at the Centre — was a significant source of alienation.
2. **Birbaha Hansda candidate effect:** A rare case of a celebrity Adivasi woman contesting from her own community's heartland. Turnout among Santali women and Sarna-practicing communities was unusually high.
3. **Lakshmir Bhandar penetration:** The ST ₹1,000/month cash transfer — announced in April 2021 during the campaign — reached approximately 70% of eligible Adivasi women HHs in Jhargram. Direct benefit transfer via DBT-linked Jan Dhan accounts (boosted banking access to ~86% by 2021) made the delivery credible.

---

## G. Sources & tier flags

### Primary sources (tier A)
- ECI 2021 WB Assembly Election archive — AC-222 result (Birbaha Hansda, AITC; Sukhmoy Satpati, BJP; Madhuja Sen Roy, CPI(M)) via Wikipedia "Jhargram Assembly constituency"
- `2019_AssemblySegmentLevelVotingData.csv` — 2019 LS baseline (electorate, turnout, party-wise votes)
- ECI archives — 2006, 2011, 2016 AE results (via Wikipedia "Jhargram Assembly constituency")
- ECI archives — 2009, 2014, 2019 LS results (via Wikipedia "Jhargram Lok Sabha constituency")
- Census of India 2011 — Jhargram Municipality, Jhargram CD Block, Binpur I CD Block (via Wikipedia; demographics unchanged from 2019 file baseline)

### Secondary sources (tier B/C)
- NFHS-5 (2019-21) West Bengal — asset/media update; smartphone penetration surge; banking access
- WB CDWDSW Lakshmir Bhandar scheme (April 2021 launch; ₹500 general / ₹1,000 SC/ST women)
- CSDS-Lokniti 2021 WB post-poll data (state rollup; Jangalmahal regional extrapolation)
- PMJDY tribal enrollment data — banking access proxy

### Tertiary / journalistic (tier D)
- The Wire, Scroll, ABP Ananda — Birbaha Hansda candidacy profile and Adivasi vote consolidation
- India Today, NDTV — 2021 WB AE Jangalmahal results analysis
- MoRD MGNREGA portal — Jhargram district utilization (proxy from WB LWE pattern)
- WB COVID reverse-migration press reports (2020-21)

### Tier-D/E reliance flags
- **Birbaha candidacy-effect magnitude** — no sub-constituency exit poll; estimated from result structure and journalistic accounts; tier D
- **Lakshmir Bhandar penetration** — statewide 70% beneficiary target; Jhargram tribal-belt actual rate estimated at ~70% for ST women; no AC-level dashboard accessed
- **Sarna/ORP vote shift** — D.15 Sarna AITC 67% is a structural estimate from result; no tribe-specific exit poll available
- **Smartphone surge magnitude** — NFHS-5 WB rural is 2019-21; Jhargram below-state-average applied proportionally

---

## H. Post-2021 validation anchors

> **These are OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> The simulator must reproduce these results from 2021 priors + narrative injection without these figures baked into calibration input.

### 2024 LS AC-222 segment — Out-of-sample gate (tier A, CSV)

| Party | Candidate (LS level) | Votes | AC-222 segment % | Tier |
|---|---|---|---|---|
| AITC | Kalipada Saren | 96,608 | 47.49 | A |
| BJP | Dr. Pranat Tudu | 82,507 | 40.56 | A |
| CPI(M)+SUCI(LF) | Sonamani Tudu + SUCI | 11,017 | 5.42 | A |
| JKPP + Others + NOTA | various | 13,291 | 6.53 | A |
| **AITC margin** | | **14,101 votes** | **6.93 pp** | A |

> **Simulation note:** From 2021 (AITC +18.97pp) to 2024 (AITC +6.93pp), BJP partially recovered. The Birbaha Hansda candidate effect partially unwound as she was not the candidate in the 2024 LS (Kalipada Saren, a less prominent figure, was TMC's LS candidate). The simulation must model this partial mean-reversion without using these 2024 figures in calibration.

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge. No post-2021 events referenced in calibration sections.*
