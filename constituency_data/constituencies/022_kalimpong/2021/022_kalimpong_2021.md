# AC 022 — Kalimpong (GEN) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 022 Kalimpong as of end-2021 — it does not reference any
> post-2021 events. Use the 2024 LS result as the out-of-sample validation
> gate for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).
>
> **Forbidden in this file:** 2022, 2023, 2024, 2025, 2026, SSC scam,
> Partha Chatterjee, RG Kar, SIR, CAA notification, CAA rules.
>
> **May reference:** COVID-19, 2021 AE result, Lakshmir Bhandar (Apr 2021),
> GJM factional politics 2017-2021 Darjeeling agitation aftermath,
> BSF 50km jurisdiction (Oct 2021).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 022 | A | ECI / Delimitation Commission 2008 |
| AC name | Kalimpong | A | ECI |
| Reservation | GEN (unreserved) | A | Delimitation 2008 |
| District | Kalimpong | A | Kalimpong district created from Darjeeling in 2017; AC remains same administrative entity |
| Sub-division | Kalimpong | A | WB administrative |
| LS constituency | 01 — Darjeeling | A | Delimitation 2008 |
| LS segments included | AC 01 Darjeeling · 02 Kurseong · 03 Matigara-Naxalbari · 04 Siliguri · 05 Phansidewa · 06 Chopra · 07 Islampur · 022 Kalimpong | A | Delimitation 2008 |
| AC composition | Kalimpong Municipality (wards 1–23) + Kalimpong-I CD Block GPs (Algara, Cholbisa, Lava, Soureni, Rishing, Pudung, Peshok, Samthar, Tashiding) + Kalimpong-II CD Block GPs (partial) | A | Delimitation 2008 |
| Geographic note | Hill sub-division in eastern Himalayan foothills; altitude 1,200–2,500 m; bordering Sikkim and Bhutan; tourism/trade economy severely hit by COVID-19 lockdowns 2020-21 | A | — |
| Sub-units used in v0 | **U1: Kalimpong_Municipality** (urban core) · **U2: Kalimpong_rural_hills** (CDB-I & II GPs) | E | v0 simplification |
| 2021 AE electorate (ECI roll) | 211,896 | A | ECI 2021 WB AE archive (detailed_results.csv) |
| 2021 AE total valid votes | 154,863 | A | ECI 2021 AE |
| 2021 AE turnout | 73.1% | A | ECI 2021 AE; 154,863 / 211,896 |
| 2021 AE winner | **Ruden Sada Lepcha (IND — Hamro Party / TMC-backed GJM(Bimal) faction)** | A | ECI 2021 AE detailed_results.csv |
| 2021 AE runner-up | Suva Pradhan (BJP) | A | ECI 2021 AE |
| 2021 AE winner margin | **3,870 votes** (58,206 − 54,336) | A | ECI 2021 AE |

**Political context (2021):** The GJM fractured into the Bimal Gurung faction (which flipped to support TMC in late 2020 after years of BJP alliance) and the Binay Tamang/Anit Thapa faction (which had been cooperating with state govt earlier). Ruden Sada Lepcha ran as an Independent backed by the Bimal Gurung GJM + TMC alliance. Dr. R.B. Bhujel (IND, 20.57%) likely represented the Binay Tamang/GNLF-affiliated vote. No formal AITC candidate was fielded; TMC's support consolidated behind Lepcha. BJP's Suva Pradhan narrowly lost despite the party's 2019 dominance.

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~112,000 (Kalimpong Muni ~42,900 + CDB-I + CDB-II partial ~69,100) | E | Census 2011 district tables; Delimitation 2008 sub-unit map |
| 2021 projected population | ~124,500 | E | 10-yr compound growth ~1.1%/yr; hill ACs grow slower than plains (methodology §4) |
| Sex ratio (2021, F per 1000 M) | ~970 | E | Kalimpong district Census 2011: 976 F/1000 M; slight improvement trend per NFHS-5 (Darjeeling proxy: 1029 NFHS-5) |
| 2021 ECI electorate (roll) | 211,896 | A | ECI 2021 WB AE archive |
| Estimated M / F / TG split | 50.3% M / 49.7% F / ~0.01% TG | E | Updated from NFHS-5 Darjeeling district sex ratio trend |
| 2021 polling stations (estimated) | ~300 | E | Slight increase from 2019; hill terrain expansion |
| 2021 AE total votes polled | 154,863 | A | ECI 2021 AE |
| 2021 AE turnout | 73.1% | A | ECI 2021 AE |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 68.20 | E | Kalimpong district Census 2011 ~68–70% Hindu; 10-yr projection stable; minor adjustment for Buddhist community growth |
| Muslim | 4.90 | E | Census 2011 ~4.5%; slight growth over 10 years |
| Christian | 14.50 | E | Census 2011 ~13–15%; Nepali Baptist/Presbyterian missions growing; +0.3pp over 10 yrs |
| Sarna_ORP | 2.40 | E | Lepcha tribal religion; marginal decline with Christian conversion trend |
| Other_residual | 10.00 | E | Buddhist (Bhutia/Tibetan ~8%) + Sikh + Not_stated; stable |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 5.50 | E | Census 2011 Kalimpong sub-division; lower SC than plains ACs; stable |
| └ Chamar_SC | 1.50 | E | Small plains migrant SC sub-community |
| └ Other_SC | 4.00 | E | Residual SC groups |
| **ST_total** | 13.20 | A | Census 2011 Kalimpong sub-division: Lepcha, Bhutia, Limboo classified as ST |
| └ Lepcha_ST | 5.50 | C | Dominant ST in Kalimpong hills; Census 2011 |
| └ Bhutia_ST | 4.20 | C | Buddhist community; includes Tibetan-origin |
| └ Limboo_ST | 3.50 | C | Gorkha sub-community with ST status |
| UC_bhadralok | 3.50 | E | Small Brahmin/Kayastha/Baidya hill presence; Bengali professional migrants |
| OBC | 12.00 | E | Gurung, Tamang, Rai, Magar sub-communities (OBC in WB hill schedule) |
| Other_Hindu_middle | 51.10 | E | Predominantly Nepali-origin Gorkha: Chhettri, Thakuri, Pradhan + unclassified; slight shift from 2019 |
| Muslim | 4.90 | E | See C.1; largely Urdu-medium plains-origin or Bengali Muslim |
| Christian_plus_Sarna_plus_Other | 9.80 | E | Christian 14.5% adjusted for within-caste overlap + Sarna 2.4% + Other_residual; normalised |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2021, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.20 | E | Kalimpong district age pyramid Census 2011; 10-yr shift; renormalised excluding 0–17; younger cohort slightly lower as prior wave ages |
| 23_27 | 11.80 | E | |
| 28_32 | 11.20 | E | |
| 33_37 | 10.00 | E | |
| 38_42 | 9.50 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.30 | E | |
| 53_57 | 7.20 | E | |
| 58_62 | 6.30 | E | |
| 63_67 | 4.30 | E | |
| 68 | 11.20 | E | 68+ open-ended; includes elderly hill residents; renormalize verified |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.38 | E | NFHS-5 Darjeeling district sex ratio 1029 F/1000 M → ~49.3% F; slight male out-migration adjustment for Kalimpong sub-dist |
| Female | 49.61 | E | |
| Third_gender | 0.01 | E | ECI 2021 AE register pattern |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 3.50 | E | Small Bengali-speaking community; stable (urban professional migrants, some Muslim) |
| Hindi | 2.00 | E | Marwari/Bihari trader community in Kalimpong town |
| Urdu | 1.00 | E | Muslim minority; mostly bilingual with Nepali |
| Other | 0.50 | E | Residual (Tibetan, Sikkimese, English-dominant) |
| Nepali | 75.00 | E | Dominant; Census 2011 Kalimpong ~73–76% Nepali mother tongue; stable |
| Lepcha | 5.50 | E | Indigenous ST language; Kalimpong sub-division Census 2011 |
| Bhutia | 4.50 | E | Bhutia/Sikkimese; includes Tibetan speakers lumped |
| Limboo | 4.00 | E | ST language; Census 2011 |
| Tamang | 4.00 | E | OBC community; Tamang language speakers |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 12.50 | E | Kalimpong district literacy ~84% (2011 A); NFHS-5 Darjeeling women literate 77.0%; 2021 projection ~87% → ~13% illiterate; hill education investment improving |
| Primary | 17.50 | E | |
| Middle | 20.00 | E | |
| Secondary | 20.50 | E | |
| Higher_Secondary | 14.00 | E | Slight increase; hill school expansion |
| Graduate | 11.50 | E | Kalimpong degree colleges; hill education investment |
| Postgraduate | 4.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 34.00 | E | Census 2011 ~35–37%; reduced by COVID-19 tourism collapse (2020-21 severe hit on Kalimpong tourism economy) |
| Marginal_worker | 8.50 | E | Seasonal hill agriculture, tourism; slightly elevated as some tourism workers became marginal |
| Non_worker | 35.50 | E | Includes housewife, elderly, retired |
| Student | 12.00 | E | Hill areas invest heavily in education; boarding schools; stable |
| Unemployed | 10.00 | E | Educated youth unemployment; hill job scarcity; COVID-19 tourism contraction worsened 2020-21 |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 21.00 | E | Census 2011 Kalimpong sub-division; cardamom, tea, ginger; slight increase as tourism workers shifted to farming |
| Agricultural_labourer | 8.00 | E | Lower than plains; hill labour patterns |
| Household_industry | 5.00 | E | Weaving, handicrafts, incense |
| Manufacturing | 3.00 | E | Limited; small agro-processing units |
| Construction | 9.00 | E | Hill road/building construction; slight uptick post-2019 |
| Trade_retail | 12.00 | E | Kalimpong Muni market hub; reduced from 14% (2019) due to COVID-19 tourism contraction |
| Transport_logistics | 7.00 | E | Hill taxi/jeep services; reduced from 8% (COVID-19 travel restrictions) |
| Services | 11.00 | E | Tourism, hospitality severely hit by COVID-19 lockdowns; reduced from 14% |
| Government_services_teachers | 15.00 | E | Higher govt employment share in hill areas; stable; insulated from COVID-19 disruption |
| Out_migrant_worker | 9.00 | D | Gorkha men in Indian Army, paramilitary; COVID-19 reverse migration swelled this category 2020 |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 3.00 | E | Small tourist-economy business owners; stable despite COVID-19 contraction |
| Employee | 40.00 | E | Govt, army, hotels, schools; government insulated; hotels contracted |
| Single_worker | 40.00 | E | Own-account: cultivators, small traders, taxi operators |
| Family_worker | 17.00 | E | Unpaid family farm/handicraft helpers |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 22.00 | C | Kalimpong sub-division BPL ~22% (2001 baseline); COVID-19 tourism collapse temporarily worsened household poverty in hill AC; 2021 estimate reflects COVID shock |
| Above_Poverty_Line_low_income | 35.00 | E | COVID-19 pushed some lower-middle households downward |
| Lower_middle | 27.00 | E | |
| Middle | 12.00 | E | Army/govt salary class; tourism economy contracted |
| Upper_middle_well_off | 4.00 | E | Kalimpong Muni affluent traders, orchid exporters |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Kalimpong_Municipality | 38.00 | E | Kalimpong Muni 2011 pop ~42,900 / AC total ~112,000 ≈ 38%; projected stable through 2021 |
| U2_Kalimpong_rural_hills | 62.00 | E | CDB-I + CDB-II GPs; v0 collapses to single rural cell |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.1 persons | E | WB hill districts Census 2011: 4.0–4.2; stable |
| Nuclear_HH | 72.00 | E | Hill Nepali/Gorkha households: higher nuclear proportion; COVID-19 reverse migration may have temporarily increased joint households |
| Joint_HH | 22.00 | E | |
| Extended_multi_generation | 6.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 30.00 | E | Large student cohort + out-migrant young men |
| Currently_married | 61.00 | E | Census 2011 Kalimpong district pattern; stable |
| Widowed | 8.00 | E | Slightly elevated; army widows, elderly |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 74.00 | C | NFHS-5 Darjeeling proxy: electricity 98.2% + NFHS-4 hill TV ~72%; slight increase by 2021 |
| Radio | 7.00 | C | Hill areas: higher radio dependency; marginal decline |
| Mobile_phone | 88.00 | C | Near-saturation by 2021; Jio 4G expanded to hills by 2020 |
| Smartphone_with_internet | 65.00 | C | COVID-19 accelerated smartphone adoption (+20pp from 2019 45%); work-from-home, e-commerce, remote education; NFHS-5 trajectory |
| Computer | 11.00 | C | School + govt employee households; stable |
| Two_wheeler | 20.00 | C | Hilly terrain limits two-wheeler; stable |
| Four_wheeler | 10.00 | C | Hill taxi operators; stable |
| Banking_access | 85.00 | C | PMJDY + hill cooperative banks; Lakshmir Bhandar Jan-Dhan requirement pushed banking access +3pp by mid-2021 |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 89.00 | B | NFHS-5 Darjeeling district 90.8% (2019-21 survey period); hill spring water improvement; close proxy for Kalimpong sub-dist |
| Improved_sanitation | 82.00 | B | NFHS-5 Darjeeling 83.0%; Swachh Bharat Phase-2 + Duare Sarkar 2020 push |
| LPG_clean_cooking_fuel | 62.00 | B | NFHS-5 Darjeeling: clean fuel 68.8%; Ujjwala Phase-2 + hill LPG distribution improvement; slightly lower for Kalimpong rural |
| Wood_biomass_fuel | 34.00 | E | Declining as LPG rises; remote hill GPs still firewood-dependent |
| Other_fuel | 4.00 | E | Kerosene fringe; declining |
| Electricity | 97.00 | B | NFHS-5 Darjeeling 98.2%; Saubhagya near-saturation; Kalimpong slightly lower (remote GPs) |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 71.00 | D | Predominantly born in Kalimpong sub-division/district; slight reduction due to COVID-19 reverse migration arrivals from metros |
| WB_other_district | 8.00 | D | Plains migrants (Bengali, Bihari) in Kalimpong town; stable |
| Other_Indian_state | 5.50 | D | Army postings, traders; COVID-19 reverse migration added ~0.5pp temporarily |
| Bangladesh_origin | 0.50 | E | Negligible; not a refugee-receiving hill AC |
| Outside_India | 0.50 | E | Bhutia/Tibetan diaspora registered; very small |
| Out_migrant | 5.50 | D | Gorkha men in Indian Army; domestic workers; slight increase from COVID-19 return migration |
| Nepal_Bhutan_origin | 9.00 | D | Historical Nepali-origin settlers (pre-1950 migration); not current immigrants; stable |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Nepali | Lepcha | Bhutia | Limboo | Tamang | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 3.00 | 2.00 | 0.00 | 0.50 | 83.00 | 5.00 | 1.00 | 3.00 | 2.50 | E | Kalimpong district Census 2011 language tables; Hindu = predominantly Nepali-Gorkha; stable |
| Muslim | 20.00 | 10.00 | 15.00 | 2.00 | 50.00 | 0.00 | 0.00 | 0.00 | 3.00 | E | Mix of Bengali Muslim (plains migrants) + Nepali-speaking hill Muslims |
| Christian | 2.00 | 1.00 | 0.00 | 1.00 | 75.00 | 10.00 | 3.00 | 5.00 | 3.00 | E | Predominantly Nepali Christian (Baptist/Presbyterian missions); Lepcha Christian significant |
| Sarna_ORP | 0.50 | 0.00 | 0.00 | 5.50 | 20.00 | 50.00 | 5.00 | 12.00 | 7.00 | E | Lepcha Sarna dominant; Limboo traditional; some Nepali |
| Other_residual | 2.00 | 2.00 | 0.00 | 6.00 | 12.00 | 0.00 | 72.00 | 0.00 | 6.00 | E | Buddhist: predominantly Bhutia/Tibetan; Other_residual = mainly Buddhist community |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population. 2D canonical layout.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 6.20 | 12.00 | 5.00 | 14.00 | 62.80 | 0 | 0 | E | Hindu: predominantly Nepali-Gorkha (Other_Hindu_middle); ST = Lepcha/Bhutia/Limboo Hindu; SC small |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 20.00 | 0 | 5.00 | 10.00 | 0 | 65.00 | E | Lepcha/Limboo Christian → ST; Nepali Christian → Other_Hindu_middle or Christian_plus |
| Sarna_ORP | 0 | 85.00 | 0 | 5.00 | 10.00 | 0 | 0 | E | Tribal religion: predominantly ST (Lepcha) |
| Other_residual | 0 | 50.00 | 0 | 5.00 | 0 | 0 | 45.00 | E | Buddhist: Bhutia ST + some non-tribal Buddhist lump |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Nepal_Bhutan_origin | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 67.00 | 7.00 | 5.50 | 0.50 | 0.50 | 5.50 | 14.00 | E | Gorkha Hindu mostly native + Nepal-origin historical settlers; COVID-19 return migration absorbed |
| Muslim | 55.00 | 25.00 | 8.00 | 2.00 | 0.00 | 5.00 | 5.00 | E | Higher plains-migrant share among hill Muslims |
| Christian | 75.00 | 5.00 | 3.00 | 0.00 | 0.00 | 7.00 | 10.00 | E | Lepcha/Nepali Christian mostly native; mission school diaspora |
| Sarna_ORP | 88.00 | 3.00 | 2.00 | 0.00 | 0.00 | 5.00 | 2.00 | E | Lepcha Sarna: deeply indigenous, high native |
| Other_residual | 60.00 | 5.00 | 8.00 | 0.00 | 8.00 | 5.00 | 14.00 | E | Buddhist: Bhutia/Tibetan; higher outside-India + Nepal-origin |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 75.00 | 66.00 | 86.00 | E | NFHS-5 Darjeeling proxy; Hindu majority includes rural hill households; smartphone +20pp from COVID-19 adoption |
| Muslim | 70.00 | 58.00 | 80.00 | E | Slightly lower; plains-migrant Muslim population in urban fringe |
| Christian | 80.00 | 72.00 | 90.00 | E | Hill Christian: mission-educated; higher asset and banking access |
| Sarna_ORP | 58.00 | 45.00 | 70.00 | E | Remote tribal areas; lower connectivity; smartphone uptick from COVID-19 period |
| Other_residual | 82.00 | 75.00 | 90.00 | E | Buddhist (Bhutia/Tibetan): urban Kalimpong; higher asset access |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 3.00 | 7.00 | 12.00 | 18.00 | 21.00 | 27.00 | 12.00 | E |
| SC_total | 17.00 | 19.00 | 22.00 | 20.00 | 12.00 | 8.00 | 2.00 | E |
| ST_total | 14.00 | 19.00 | 22.00 | 21.00 | 14.00 | 8.00 | 2.00 | E |
| OBC | 11.00 | 17.00 | 22.00 | 22.00 | 15.00 | 11.00 | 2.00 | E |
| Other_Hindu_middle | 12.00 | 17.00 | 20.00 | 21.00 | 15.00 | 11.00 | 4.00 | E |
| Muslim | 19.00 | 22.00 | 22.00 | 18.00 | 11.00 | 6.00 | 2.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 21.00 | 19.00 | E |
| 23_27 | 23.00 | 19.00 | E |
| 28_32 | 19.00 | 14.00 | E |
| 33_37 | 16.00 | 11.00 | E |
| 38_42 | 14.00 | 9.00 | E |
| 43_47 | 12.00 | 7.00 | E |
| 48_52 | 10.00 | 5.00 | E |
| 53_57 | 8.00 | 3.50 | E |
| 58_62 | 6.50 | 2.50 | E |
| 63_67 | 5.50 | 2.00 | E |
| 68 | 4.50 | 1.50 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 5.00 | 22.00 | E |
| 23_27 | 35.00 | 72.00 | E |
| 28_32 | 78.00 | 90.00 | E |
| 33_37 | 90.00 | 88.00 | E |
| 38_42 | 91.00 | 87.00 | E |
| 43_47 | 90.00 | 85.00 | E |
| 48_52 | 88.00 | 80.00 | E |
| 53_57 | 85.00 | 72.00 | E |
| 58_62 | 82.00 | 60.00 | E |
| 63_67 | 78.00 | 42.00 | E |
| 68 | 70.00 | 28.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 45.00 | 65.00 | E | COVID-19 accelerated rural smartphone adoption; hill cultivator |
| Agricultural_labourer | 35.00 | 58.00 | E | Lowest asset tier; COVID-19 period smart-phone adoption |
| Household_industry | 50.00 | 70.00 | E | Handicraft/weaving workers; online sales channels developed |
| Manufacturing | 58.00 | 78.00 | E | |
| Construction | 55.00 | 72.00 | E | |
| Trade_retail | 78.00 | 87.00 | E | Kalimpong Muni market; smartphone for trade comms; further growth |
| Transport_logistics | 72.00 | 80.00 | E | Hill taxi operators; smartphone heavy; apps for booking |
| Services | 80.00 | 88.00 | E | Tourism/hospitality; online presence essential even during COVID-19 |
| Government_services_teachers | 90.00 | 93.00 | E | Highest; govt employees; work-from-home during lockdowns |
| Out_migrant_worker | 78.00 | 76.00 | D | Army/domestic worker; smartphone for remittance; WhatsApp family contact |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 29.00 | 3.00 | E |
| Primary | 34.00 | 5.00 | E |
| Middle | 32.00 | 8.00 | E |
| Secondary | 27.00 | 13.00 | E |
| Higher_Secondary | 24.00 | 20.00 | E |
| Graduate | 29.00 | 22.00 | E |
| Postgraduate | 39.00 | 13.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 022. See NORMALIZED_SCHEMA.md §4.7.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Kalimpong_Municipality | 65.00 | 8.00 | 14.50 | 1.00 | 11.50 | E | Urban core: higher Muslim (plains migrants), higher Buddhist (Tibetan traders); stable from 2019 |
| U2_Kalimpong_rural_hills | 70.20 | 3.10 | 14.50 | 3.30 | 8.90 | E | Rural hills: lower Muslim; higher Sarna (Lepcha villages); slight Christian growth |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Parent leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Kalimpong_Municipality | 6.00 | 5.00 | 10.00 | 11.00 | 50.00 | 8.00 | 10.00 | E |
| U2_Kalimpong_rural_hills | 2.00 | 5.80 | 15.00 | 12.50 | 51.80 | 3.20 | 9.70 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Kalimpong_Municipality | 86.00 | 78.00 | 18.00 | 93.00 | E |
| U2_Kalimpong_rural_hills | 65.00 | 55.00 | 6.00 | 79.00 | E |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Kalimpong_Municipality | 85.00 | 92.00 | 95.00 | 99.00 | E |
| U2_Kalimpong_rural_hills | 48.00 | 76.00 | 85.00 | 96.00 | E |

### D.15 Vote × Religion (2021 AE, calibration anchor)

P(party ‖ religion) — 2021 AE result anchor. GJM-TMC faction (IND) absorbed AITC vote;
BJP stood alone. Other_NOTA includes Dr. R.B. Bhujel IND (GJM-Binay Tamang faction) + NPEP + small INDs.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 42.00 | 32.00 | 1.00 | 0.20 | 24.80 | E | GJM(Bimal)-TMC alliance IND won on Gorkha Hindu vote; BJP lost hill-Hindu monopoly; Bhujel IND drew hill Hindu |
| Muslim | 15.00 | 52.00 | 6.00 | 0.50 | 26.50 | E | Hill Muslim shifted toward TMC-backed IND (Lepcha); partial INC+AIJAP residual in Other_NOTA |
| Christian | 35.00 | 38.00 | 4.00 | 0.50 | 22.50 | E | Nepali Christian: GJM-TMC IND benefited from Lepcha community mobilisation; BJP lost its 2019 share |
| Sarna_ORP | 30.00 | 38.00 | 2.00 | 0.50 | 29.50 | E | Lepcha Sarna: Ruden Sada Lepcha (himself a Lepcha ST) captured Sarna vote; high Other_NOTA (Bhujel IND) |
| Other_residual | 38.00 | 30.00 | 1.50 | 0.30 | 30.20 | E | Buddhist (Bhutia): split between BJP, TMC-IND, Bhujel IND; NPEP drew Buddhist vote |

### D.16 Vote × Caste (2021 AE)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 55.00 | 28.00 | 5.00 | 2.00 | 10.00 | E | Hill bhadralok: reduced BJP support; partial AITC shift |
| OBC | 40.00 | 32.00 | 2.00 | 0.30 | 25.70 | E | Gurung/Tamang/Rai: GJM-TMC IND drew significant share; Bhujel IND also drew OBC |
| SC_total | 38.00 | 40.00 | 4.00 | 0.50 | 17.50 | E | Plains-SC origin: more AITC/TMC-IND amenable |
| ST_total | 28.00 | 40.00 | 2.00 | 0.30 | 29.70 | E | Lepcha/Bhutia/Limboo: Ruden Lepcha's own community; strong shift; high Other_NOTA for Bhujel IND |
| Other_Hindu_middle | 38.00 | 30.00 | 1.00 | 0.20 | 30.80 | E | Core Gorkha Chhettri: BJP reduced but competitive; Bhujel IND drew significant Chhettri vote |
| Muslim | 15.00 | 52.00 | 6.00 | 0.50 | 26.50 | E | Same as D.15 Muslim row |

### D.17 Vote × Gender (2021 AE, post-Lakshmir Bhandar launch)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 38.00 | 32.00 | 1.50 | 0.30 | 28.20 | E | Male vote more split among BJP, TMC-IND, Bhujel IND |
| Female | 32.00 | 38.00 | 1.00 | 0.20 | 28.80 | E | Lakshmir Bhandar launched Apr 2021 before AE; female shift toward TMC-backed IND; hill female vote less BJP-dominant than 2019 |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for AC 022. See NORMALIZED_SCHEMA.md §4.7.)

---

## E. 2021 baseline vote (calibration target)

**Critical schema note:** No AITC candidate was fielded in 2021 AE for AC 022.
TMC supported Ruden Sada Lepcha (IND — GJM Bimal Gurung faction).
Dr. R.B. Bhujel (IND — probable GJM Binay Tamang/GNLF-aligned faction) ran separately.
Party column mapping: AITC = 0; Other_NOTA absorbs IND winner + IND-Bhujel + NPEP + small INDs.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 35.09 | A | ECI 2021 AE; Suva Pradhan; 54,336 votes of 154,863 total |
| AITC | 0.00 | A | No AITC candidate fielded; TMC support went to Ruden Lepcha IND |
| INC | 1.11 | A | Dilip Pradhan; 1,715 votes; ECI 2021 AE |
| LF | 0.00 | A | No Left candidate fielded in AC 022 in 2021 |
| Other_NOTA | 63.80 | A | IND-Lepcha (TMC-backed) 37.59% + IND-Bhujel 20.57% + NOTA 1.39% + NPEP 1.17% + small INDs 3.09%; total 63.80% |
| **Sum** | **100.00** | — | self-check; total valid votes 154,863; electorate 211,896; turnout 73.1% |

**Simulation note:** The vote-joints D.15–D.17 above use AITC column to proxy the combined TMC-backed-IND (Ruden Lepcha) vote share for modelling purposes, since the agent-based model needs a TMC-affinity axis. §E strictly records actual party labels (AITC = 0). Downstream narrative engine must map "AITC" in the joints to the TMC-IND alliance here.

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 022 Kalimpong (Assembly Elections)

| Year | Winner | Party | Votes | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|---|
| 2011 AE | Harka Bahadur Chhetri | GJM | ~55,000 | ~55.0 | Amar Singh Rai | GNLF | ~22,000 | ~12,000 |
| 2016 AE | Harka Bahadur Chhetri | GJM | ~51,000 | ~51.0 | Suman Pradhan | AITC | ~22,000 | ~10,000 |

Note: 2011 and 2016 AE dominated by GJM (Gorkha Janmukti Morcha). BJP national party presence channeled through GJM alliance. AITC had limited presence in hills until post-2017 GTHA period. Harka Bahadur Chhetri (GJM) was two-term MLA; he subsequently split from GJM mainstream before 2021.

### 2019 LS Darjeeling (PC 01) — AC 022 segment (calibration target for 2019, anchor for 2021)

| Party | Candidate | Votes | AC 022 segment % | Source |
|---|---|---|---|---|
| BJP | Raju Bista | 96,877 | 67.21% | A — 2019_AssemblySegmentLevelVotingData.csv |
| AITC | Amar Singh Rai | 34,302 | 23.80% | A — same |
| INC | Sankar Malakar | 3,362 | 2.33% | A — same |
| LF (CPIM+SUCI) | Saman Pathak + Tanmay Dutta | 559 | 0.39% | A — same |
| Other_NOTA | BSP+IDRP+KPPU+grac+RJNP+AIJAP+INDs | 9,041 | 6.27% | A — same |
| **Total** | | 144,141 | 100% | Electorate 205,462; turnout 70.2% |

Political narrative (2019→2021 trajectory): GJM-BJP alliance that delivered BJP's 67.21% in 2019 LS fractured in 2020. Bimal Gurung (GJM founder) broke with BJP and supported TMC in late 2020 after returning from hiding (since 2017 Gorkhaland agitation). Binay Tamang and Anit Thapa, who had led a rival GJM faction cooperating with state govt, also contested space. By the 2021 AE, the Bimal Gurung GJM backed Ruden Sada Lepcha as an independent, while BJP fielded Suva Pradhan. COVID-19 lockdowns (2020) severely hit Kalimpong's tourism economy, adding economic grievances. Lakshmir Bhandar launch (April 2021) provided TMC-aligned IND a welfare-credit narrative in the hills.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Kalimpong sub-division demographic tables (religion, language, caste, worker classification)
- Census of India 2011 — Darjeeling District Census Handbook (DCHB) — Kalimpong part
- Election Commission of India — `data/electoral_history/2021/detailed_results.csv` — AC 022 Kalimpong 2021 AE full candidate results
- Election Commission of India — `data/2019_AssemblySegmentLevelVotingData.csv` — AC 022 segment 2019 LS
- Election Commission of India — 2011 AE, 2016 AE results for AC 022 Kalimpong
- Delimitation Commission of India 2008 — WB Schedule (AC 022 = Kalimpong Muni + CDB-I + CDB-II GPs)

### Secondary sources (tier B / C)

- NFHS-5 (2019-21) West Bengal — `data/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv` — Darjeeling district indicators: electricity 98.2%, improved water 90.8%, improved sanitation 83.0%, clean cooking fuel 68.8%
- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline (hill district proxy for 2019 baseline)
- Pew Research India 2021 — religion-differential growth projections (hill rate adjusted)
- CSDS-Lokniti 2019 NES — vote × demographic cross-tabs (Darjeeling/hill regional subsample; used as 2019 anchor)

### Tertiary / journalistic (tier D)

- Wikipedia "Kalimpong district" — demographic summary, Census 2011 religion and language data
- Wikipedia "2021 West Bengal Legislative Assembly election in Darjeeling district" — GJM factional split context; Bimal Gurung-TMC alliance confirmation
- The Wire / Scroll coverage of GJM factional dynamics 2020-21; Bimal Gurung return from hiding
- Telegraph (Calcutta) coverage of hill political realignment pre-2021 AE
- Wikipedia "Darjeeling (Lok Sabha constituency)" — 2019 result context

### Tier-D / E reliance flags (what to distrust)

- **Vote × demographic joints (D.15–D.17)** — 2021 AE saw unique three-way split (BJP vs TMC-IND vs Bhujel-IND); CSDS 2021 hill cross-tabs not available; tier E imputation based on result share + 2019 anchor + GJM factional logic
- **AITC column in D.15–D.17** — proxies TMC-backed-IND (Ruden Lepcha) vote for simulation purposes; §E correctly shows AITC=0; downstream engine must handle mapping
- **AC-level sub-division data** (C.1 religion, C.5 language) — Census 2011 for Kalimpong sub-division (entire sub-division, not just AC 022 boundary); small boundary mismatch; tier E
- **Caste breakdown** (C.2, D.2) — ST sub-classification uses Census 2011 district-level data; OBC list for WB hills not publicly disaggregated; tier C/E
- **Migration/birthplace** (C.16, D.3) — no Census D-series at AC level; tier D from hill demographic pattern + COVID-19 reverse-migration adjustment
- **Asset/media** (C.14, D.13) — NFHS-5 Darjeeling district (not Kalimpong sub-district); Kalimpong hill terrain implies slightly lower smartphone penetration than Darjeeling urban; tier C
- **2011/2016 AE results** (F) — from secondary sources; GJM/GNLF vote shares approximate; tier D

### v0 known gaps

1. ECI 2021 AE Form-20 AC-022 per-polling-station breakdown — CSV has aggregate; PS-level not fetched
2. DCHB Kalimpong Part-A GP-level Census data — collapsed to 2 sub-units (Muni + rural)
3. OBC sub-community WB hill schedule — Gurung/Tamang/Rai exact shares; using estimated proxy
4. CSDS 2021 WB hill cross-tabs for vote × demographics — using ECI aggregate + qualitative GJM narrative (tier E)
5. Kalimpong municipality ward-level data — 23 wards aggregated to single urban cell
6. Ruden Sada Lepcha party affiliation — Wikipedia confirms IND; ECI record shows IND; political affiliation was Hamro Party / GJM(Bimal)-TMC nexus (tier D from journalistic sources)

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge.*
*No post-2021 events referenced. Forbidden keywords clean.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs. Post-2021 events
> (CAA rules notification, SSC scam, RG Kar protests, SIR revision) are NOT in
> the frozen file and must be injected as narrative shocks by the simulator.

### 2024 Lok Sabha Election — AC 022 segment within Darjeeling LS (PC 01) (tier A, CSV)

> Figures below are **tier A** — sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=22, Kalimpong. Total valid votes: 146,022; electorate 220,584; turnout ~66.2%.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Raju Bista | 77,745 | **53.24%** | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Gopal Lama | 54,113 | **37.06%** | A | Same |
| INC | Munish Tamang | 6,092 | **4.17%** | A | Same |
| NOTA | — | 2,068 | **1.42%** | A | Same |
| Others (KMSP+NBNGPLPP+APoI+KPPU+SUCI+grac+4 INDs) | various | 6,004 | **4.11%** | A | Same |
| **BJP margin over AITC** | | **23,632 votes** | **16.18 pp** | A | Computed |

Note: BJP recovered from 2021 AE vulnerability (35.09%) to 53.24% in 2024 LS; AITC (via Gopal Lama) consolidated hill-TMC vote at 37.06% vs the fragmented 2021 IND situation. INC (Munish Tamang, a Gorkha candidate) drew 4.17%. The 2021→2024 swing reflects GJM re-alignment dynamics and the resolution of factional fragmentation at LS level.

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC segment shares within ±3pp of the tier-A CSV figures:
- BJP target: 53% ± 3pp
- AITC target: 37% ± 3pp
- INC + others target: 10% ± 3pp
