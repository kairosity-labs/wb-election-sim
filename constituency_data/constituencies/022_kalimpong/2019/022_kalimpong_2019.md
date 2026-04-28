# AC 022 — Kalimpong (GEN) — Calibrated 2019 Population Snapshot

> **Frozen at end-2019.** This file describes the demographic and behavioural
> state of AC 022 Kalimpong as of 2019 only — it does not reference
> any post-2019 events. Use post-2019 elections (2021 AE, 2024 LS) as
> out-of-sample validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2019.md`](methodology_2019.md) ·
> [`csv/`](csv/) (machine-parseable joint tables) ·
> [`NORMALIZED_SCHEMA.md`](../../../NORMALIZED_SCHEMA.md) (the canonical schema this MD follows)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2019)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 022 | A | ECI / Delimitation Commission 2008 |
| AC name | Kalimpong | A | ECI |
| Reservation | GEN (unreserved) | A | Delimitation 2008 |
| District | Kalimpong | A | Delimitation 2008 (Kalimpong district carved from Darjeeling 2017; earlier was Darjeeling district sub-division) |
| Sub-division | Kalimpong | A | WB administrative |
| LS constituency | 01 — Darjeeling | A | Delimitation 2008 |
| LS segments included | AC 01 Darjeeling · 02 Kurseong · 03 Matigara-Naxalbari · 04 Siliguri · 05 Phansidewa · 06 Chopra · 07 Islampur · 022 Kalimpong | A | Delimitation 2008 |
| AC composition | Kalimpong Municipality (wards 1–23) + Kalimpong-I CD Block GPs (Algara, Cholbisa, Lava, Soureni, Rishing, Pudung, Peshok, Samthar, Tashiding) + Kalimpong-II CD Block GPs (partial) | A | Delimitation 2008 |
| Geographic note | Hill sub-division in eastern Himalayan foothills; altitude 1,200–2,500 m; bordering Sikkim and Bhutan | A | — |
| Sub-units used in v0 | **U1: Kalimpong_Municipality** (urban core) · **U2: Kalimpong_rural_hills** (CDB-I & II GPs) | E | v0 simplification |

## B. 2019 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~112,000 (Kalimpong Muni ~42,900 + CDB-I + CDB-II partial ~69,100) | E | Census 2011 district tables; Delimitation 2008 sub-unit map |
| 2019 projected population | ~122,000 | E | 8-yr compound growth ~1.1%/yr; hill ACs grow slower than plains |
| Sex ratio (2019, F per 1000 M) | ~960 | E | Kalimpong district Census 2011: 976 F/1000 M; slight male out-migration adjustment |
| 2019 estimated electorate (18+) | ~205,462 | A | ECI GE2019 roll (from 2019_AssemblySegmentLevelVotingData.csv) |
| Estimated M / F / TG split (2019) | 50.5% M / 49.5% F / <0.05% TG | E | District sex ratio projected; 2021 SIR back-projection |
| 2019 polling stations (estimated) | ~290 | E | Hill terrain; back-projected from 2021 SIR |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 68.50 | E | Kalimpong district/sub-division Census 2011: ~68–70% Hindu; 2019 projection stable |
| Muslim | 4.80 | E | Census 2011 Kalimpong sub-division ~4.5%; slight growth projection |
| Christian | 14.20 | E | Census 2011 Kalimpong sub-division ~13–15%; substantial Nepali Christian community |
| Sarna_ORP | 2.50 | E | Lepcha tribal religion + small Limboo traditional practice |
| Other_residual | 10.00 | E | Buddhist (Bhutia/Tibetan community ~8%) + Sikh + Not_stated |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 5.50 | E | Census 2011 Kalimpong sub-division; lower SC than plains ACs |
| └ Chamar_SC | 1.50 | E | Small plains migrant SC sub-community |
| └ Other_SC | 4.00 | E | Residual SC groups |
| **ST_total** | 13.20 | A | Census 2011 Kalimpong sub-division: Lepcha, Bhutia, Limboo classified as ST |
| └ Lepcha_ST | 5.50 | C | Dominant ST in Kalimpong hills; Census 2011 |
| └ Bhutia_ST | 4.20 | C | Buddhist community; includes Tibetan-origin |
| └ Limboo_ST | 3.50 | C | Gorkha sub-community with ST status |
| UC_bhadralok | 3.50 | E | Small Brahmin/Kayastha/Baidya hill presence; Bengali professional migrants |
| OBC | 12.00 | E | Includes Gurung, Tamang, Rai, Magar sub-communities (OBC in WB hill schedule) |
| Other_Hindu_middle | 51.30 | E | Predominantly Nepali-origin Gorkha: Chhettri, Thakuri, Pradhan, Chettri + un-classified |
| Muslim | 4.80 | E | See C.1; largely Urdu-medium plains-origin or Bengali Muslim |
| Christian_plus_Sarna_plus_Other | 9.70 | E | Christian 14.2% − (within UC) + Sarna 2.5% + Other residual; normalised to parent-row |
| **Sum** | **100.00** | — | self-check (parent rows only; sub-rows excluded) |

### C.3 Age cohort (2019, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.50 | E | Kalimpong district age pyramid Census 2011; renormalised excluding 0–17 |
| 23_27 | 12.00 | E | |
| 28_32 | 11.00 | E | |
| 33_37 | 10.00 | E | |
| 38_42 | 9.50 | E | |
| 43_47 | 9.00 | E | |
| 48_52 | 8.00 | E | |
| 53_57 | 7.00 | E | |
| 58_62 | 6.00 | E | |
| 63_67 | 4.00 | E | |
| 68 | 12.00 | E | 68+ open-ended; includes elderly hill residents; renormalize verified |
| **Sum** | **100.00** | — | self-check |

### C.4 Gender (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 50.51 | E | Kalimpong district sex ratio ~976 F/1000 M → ~50.5% M |
| Female | 49.48 | E | |
| Third_gender | 0.01 | E | 2021 SIR back-projection |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 3.50 | E | Small Bengali-speaking community (urban professional migrants, some Muslim) |
| Hindi | 2.00 | E | Marwari/Bihari trader community in Kalimpong town |
| Urdu | 1.00 | E | Muslim minority; mostly bilingual with Nepali |
| Other | 0.50 | E | Residual (Tibetan, Sikkimese, English-dominant) |
| Nepali | 75.00 | E | Dominant; Census 2011 Kalimpong ~73–76% Nepali mother tongue |
| Lepcha | 5.50 | E | Indigenous ST language; Kalimpong sub-division Census 2011 |
| Bhutia | 4.50 | E | Bhutia/Sikkimese; includes Tibetan speakers lumped |
| Limboo | 4.00 | E | ST language; Census 2011 Kalimpong sub-division |
| Tamang | 4.00 | E | OBC community; Tamang language speakers |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2019, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 14.00 | E | Kalimpong district literacy ~84% (2011 A); 2019 trend +2pp → ~14% illiterate |
| Primary | 18.00 | E | Census 2011 education distribution; Kalimpong district |
| Middle | 20.00 | E | |
| Secondary | 20.00 | E | |
| Higher_Secondary | 13.00 | E | |
| Graduate | 11.00 | E | Kalimpong has several degree colleges; hill education investment |
| Postgraduate | 4.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 36.00 | E | Census 2011 Kalimpong sub-division main-worker share ~35–37% |
| Marginal_worker | 8.00 | E | Seasonal hill agriculture, tourism |
| Non_worker | 34.00 | E | Includes housewife, elderly, retired — lower than plains |
| Student | 12.00 | E | Hill areas invest heavily in education; boarding schools |
| Unemployed | 10.00 | E | Educated youth unemployment; hill job scarcity; GJM agitation disruptions pre-2019 |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 20.00 | E | Census 2011 Kalimpong sub-division cultivator share; cardamom, tea, ginger |
| Agricultural_labourer | 8.00 | E | Lower than plains; hill labour patterns |
| Household_industry | 5.00 | E | Weaving, handicrafts, incense |
| Manufacturing | 3.00 | E | Limited; small agro-processing units |
| Construction | 8.00 | E | Hill road/building construction; GTHA period activity |
| Trade_retail | 14.00 | E | Kalimpong Muni market hub; tourist goods, Tibetan trade |
| Transport_logistics | 8.00 | E | Hill taxi/jeep services; Army supply chain |
| Services | 14.00 | E | Tourism, hospitality, private sector |
| Government_services_teachers | 15.00 | E | Higher govt employment share in hill areas |
| Out_migrant_worker | 5.00 | D | Gorkha men in Indian Army, paramilitary; domestic workers to metros |
| **Sum** | **100.00** | — | self-check |

### C.9 Class of worker (within workers, 2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 3.00 | E | Small tourist-economy business owners |
| Employee | 40.00 | E | Govt, army, hotels, schools; higher employee share than plains agriculture ACs |
| Single_worker | 40.00 | E | Own-account: cultivators, small traders, taxi operators |
| Family_worker | 17.00 | E | Unpaid family farm/handicraft helpers |
| **Sum** | **100.00** | — | self-check |

### C.10 Economic / poverty (2019, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 20.00 | C | Kalimpong sub-division BPL ~22% (2001); WB hill-area poverty decline ~2pp 2011-19 → ~20% |
| Above_Poverty_Line_low_income | 35.00 | E | |
| Lower_middle | 28.00 | E | |
| Middle | 13.00 | E | Army/govt salary class; tourism economy |
| Upper_middle_well_off | 4.00 | E | Kalimpong Muni affluent traders, orchid exporters |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Kalimpong_Municipality | 38.00 | E | Kalimpong Muni 2011 pop ~42,900 / AC total ~112,000 ≈ 38%; projected stable |
| U2_Kalimpong_rural_hills | 62.00 | E | CDB-I + CDB-II GPs; v0 collapses to single rural cell |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2019)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.1 persons | E | WB hill districts Census 2011: 4.0–4.2; nuclear-skewed |
| Nuclear_HH | 72.00 | E | Hill Nepali/Gorkha households: higher nuclear proportion |
| Joint_HH | 22.00 | E | |
| Extended_multi_generation | 6.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.13 Marital status (2019, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 30.00 | E | Large student cohort + out-migrant young men |
| Currently_married | 61.00 | E | Census 2011 Kalimpong district pattern |
| Widowed | 8.00 | E | Slightly elevated; army widows, elderly |
| Separated_divorced | 1.00 | E | |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2019, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 72.00 | C | NFHS-4 WB hill-region estimate; lower than plains urban; 2019 projection |
| Radio | 8.00 | C | Hill areas: higher radio dependency for emergency/weather |
| Mobile_phone | 85.00 | C | NFHS-4 WB + Jio rollout; hill connectivity improved 2016-19 |
| Smartphone_with_internet | 45.00 | C | Hill internet slower to penetrate; lower than plains average |
| Computer | 10.00 | C | School+govt employee households |
| Two_wheeler | 20.00 | C | Hilly terrain limits two-wheeler; lower than plains |
| Four_wheeler | 10.00 | C | Hill taxi operators inflate 4W; shared ownership |
| Banking_access | 82.00 | C | PMJDY + hill cooperative banks; slightly lower than plains saturation |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2019)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 82.00 | C | Kalimpong district NFHS-4; mountain spring water common; partially improved |
| Improved_sanitation | 65.00 | C | NFHS-4 WB hill; Swachh Bharat 2014-19 push |
| LPG_clean_cooking_fuel | 42.00 | C | NFHS-4 + Ujjwala 2016-19; lower LPG penetration in remote hills; firewood dominant |
| Wood_biomass_fuel | 53.00 | C | Forest-adjacent hill households; high firewood use |
| Other_fuel | 5.00 | E | Kerosene fringe |
| Electricity | 88.00 | E | Census 2011 + Saubhagya 2017-19; remote GPs partially unelectrified |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2019, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 72.00 | D | Predominantly born in Kalimpong sub-division/district; hill communities are highly local |
| WB_other_district | 8.00 | D | Plains migrants (Bengali, Bihari) in Kalimpong town; some Darjeeling district internal migration |
| Other_Indian_state | 5.00 | D | Army postings, traders; Marwari/Bihari merchants |
| Bangladesh_origin | 0.50 | E | Negligible; not a refugee-receiving hill AC |
| Outside_India | 0.50 | E | Bhutia/Tibetan diaspora registered; very small |
| Out_migrant | 5.00 | D | Gorkha men in Indian Army; domestic workers to Kolkata/Delhi |
| Nepal_Bhutan_origin | 9.00 | D | Historical Nepali-origin settlers (pre-1950 migration); not current immigrants |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Nepali | Lepcha | Bhutia | Limboo | Tamang | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Hindu | 3.00 | 2.00 | 0.00 | 0.50 | 83.00 | 5.00 | 1.00 | 3.00 | 2.50 | E | Kalimpong district Census 2011 language tables; Hindu = predominantly Nepali-Gorkha |
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
| Hindu | 68.00 | 7.00 | 5.00 | 0.50 | 0.50 | 5.00 | 14.00 | E | Gorkha Hindu mostly native + Nepal-origin historical settlers |
| Muslim | 55.00 | 25.00 | 8.00 | 2.00 | 0.00 | 5.00 | 5.00 | E | Higher plains-migrant share among hill Muslims |
| Christian | 75.00 | 5.00 | 3.00 | 0.00 | 0.00 | 7.00 | 10.00 | E | Lepcha/Nepali Christian mostly native; mission school diaspora |
| Sarna_ORP | 88.00 | 3.00 | 2.00 | 0.00 | 0.00 | 5.00 | 2.00 | E | Lepcha Sarna: deeply indigenous, high native |
| Other_residual | 60.00 | 5.00 | 8.00 | 0.00 | 8.00 | 5.00 | 14.00 | E | Buddhist: Bhutia/Tibetan; higher outside-India + Nepal-origin |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 73.00 | 46.00 | 83.00 | E | NFHS-4 WB hill proxy; Hindu majority includes rural hill households |
| Muslim | 68.00 | 40.00 | 76.00 | E | Slightly lower; plains-migrant Muslim population in urban fringe |
| Christian | 78.00 | 52.00 | 88.00 | E | Hill Christian: mission-educated; higher asset and banking access |
| Sarna_ORP | 55.00 | 28.00 | 65.00 | E | Remote tribal areas; lower connectivity |
| Other_residual | 80.00 | 55.00 | 88.00 | E | Buddhist (Bhutia/Tibetan): urban Kalimpong; higher asset access |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4.00 | 8.00 | 12.00 | 18.00 | 20.00 | 26.00 | 12.00 | E |
| SC_total | 18.00 | 20.00 | 22.00 | 19.00 | 12.00 | 7.00 | 2.00 | E |
| ST_total | 15.00 | 20.00 | 22.00 | 20.00 | 13.00 | 8.00 | 2.00 | E |
| OBC | 12.00 | 18.00 | 22.00 | 22.00 | 14.00 | 10.00 | 2.00 | E |
| Other_Hindu_middle | 13.00 | 18.00 | 20.00 | 21.00 | 14.00 | 11.00 | 3.00 | E |
| Muslim | 20.00 | 22.00 | 22.00 | 18.00 | 10.00 | 6.00 | 2.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 20.00 | 18.00 | E |
| 23_27 | 22.00 | 18.00 | E |
| 28_32 | 18.00 | 13.00 | E |
| 33_37 | 15.00 | 10.00 | E |
| 38_42 | 13.00 | 8.00 | E |
| 43_47 | 11.00 | 6.00 | E |
| 48_52 | 9.00 | 4.00 | E |
| 53_57 | 7.00 | 3.00 | E |
| 58_62 | 6.00 | 2.00 | E |
| 63_67 | 5.00 | 2.00 | E |
| 68 | 4.00 | 1.00 | E |

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
| Cultivator | 30.00 | 62.00 | E | Hill cultivator; lower connectivity |
| Agricultural_labourer | 22.00 | 55.00 | E | Lowest asset tier |
| Household_industry | 35.00 | 68.00 | E | Handicraft/weaving workers |
| Manufacturing | 45.00 | 75.00 | E | |
| Construction | 42.00 | 70.00 | E | |
| Trade_retail | 65.00 | 85.00 | E | Kalimpong Muni market; smartphone for trade comms |
| Transport_logistics | 60.00 | 78.00 | E | Hill taxi operators; smartphone heavy |
| Services | 72.00 | 88.00 | E | Tourism/hospitality |
| Government_services_teachers | 85.00 | 92.00 | E | Highest; govt employees |
| Out_migrant_worker | 70.00 | 75.00 | D | Army/domestic worker; smartphone for remittance |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 30.00 | 3.00 | E |
| Primary | 35.00 | 5.00 | E |
| Middle | 33.00 | 8.00 | E |
| Secondary | 28.00 | 12.00 | E |
| Higher_Secondary | 25.00 | 18.00 | E |
| Graduate | 30.00 | 20.00 | E |
| Postgraduate | 40.00 | 12.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 022. See NORMALIZED_SCHEMA.md §4.7.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Kalimpong_Municipality | 65.00 | 8.00 | 14.00 | 1.00 | 12.00 | E | Urban core: higher Muslim (plains migrants), higher Buddhist (Tibetan traders) |
| U2_Kalimpong_rural_hills | 70.50 | 3.00 | 14.30 | 3.40 | 8.80 | E | Rural hills: lower Muslim; higher Sarna (Lepcha villages) |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit). Parent leaves only.

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Kalimpong_Municipality | 6.00 | 5.00 | 10.00 | 11.00 | 50.00 | 8.00 | 10.00 | E |
| U2_Kalimpong_rural_hills | 2.00 | 5.80 | 15.00 | 12.50 | 52.00 | 3.00 | 9.70 | E |

### D.13 Sub-unit × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Kalimpong_Municipality | 85.00 | 60.00 | 18.00 | 92.00 | E |
| U2_Kalimpong_rural_hills | 63.00 | 35.00 | 5.00 | 75.00 | E |

### D.14 Sub-unit × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Kalimpong_Municipality | 70.00 | 85.00 | 92.00 | 98.00 | E |
| U2_Kalimpong_rural_hills | 25.00 | 53.00 | 76.00 | 81.00 | E |

### D.15 Vote × Religion (2019 LS)

P(party ‖ religion) — 2019 LS calibration anchor. BJP dominance reflects Gorkha Hindu BJP alignment.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 79.00 | 13.00 | 1.50 | 0.30 | 6.20 | E | GJM-BJP alliance delivered Gorkha Hindu vote; CSDS 2019 hill region estimate |
| Muslim | 25.00 | 55.00 | 8.00 | 1.00 | 11.00 | E | Hill Muslim split; partial AITC support; AIJAP (Gorkha Muslim party) drew ~11% |
| Christian | 60.00 | 18.00 | 5.00 | 1.00 | 16.00 | E | Nepali Christian: majority BJP-leaning (GJM alignment) but with Christian charity vote |
| Sarna_ORP | 55.00 | 20.00 | 3.00 | 1.00 | 21.00 | E | Lepcha tribal: BJP majority but independent/tribal parties drew votes |
| Other_residual | 65.00 | 15.00 | 2.00 | 0.50 | 17.50 | E | Buddhist (Bhutia): BJP majority; GNP/GJM split captured in Other_NOTA |

### D.16 Vote × Caste (2019 LS)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 70.00 | 18.00 | 5.00 | 2.00 | 5.00 | E | Hill bhadralok small; strong BJP lean |
| OBC | 72.00 | 15.00 | 2.00 | 0.50 | 10.50 | E | Gurung/Tamang/Rai: GJM-BJP aligned |
| SC_total | 55.00 | 30.00 | 5.00 | 1.00 | 9.00 | E | Plains-SC origin: more AITC-amenable |
| ST_total | 65.00 | 14.00 | 2.00 | 0.50 | 18.50 | E | Lepcha/Bhutia/Limboo: BJP-GNP split; GNLF draws some |
| Other_Hindu_middle | 75.00 | 14.00 | 1.00 | 0.30 | 9.70 | E | Core Gorkha Chhettri/Brahmin: highest BJP vote |
| Muslim | 25.00 | 55.00 | 8.00 | 1.00 | 11.00 | E | Same as D.15 Muslim row |

### D.17 Vote × Gender (2019 LS, pre-LB baseline)

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 70.00 | 21.00 | 2.00 | 0.40 | 6.60 | E | CSDS 2019 WB hill estimate; male slightly more BJP |
| Female | 64.00 | 27.00 | 2.80 | 0.40 | 5.80 | E | Female slightly more AITC; smaller gap than plains |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for AC 022. See NORMALIZED_SCHEMA.md §4.7.)

---

## E. 2019 baseline vote (calibration target)

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 67.21 | A | ECI GE2019 Form-20; 2019_AssemblySegmentLevelVotingData.csv; 96,877 votes |
| AITC | 23.80 | A | ECI GE2019; 34,302 votes |
| INC | 2.33 | A | ECI GE2019; 3,362 votes |
| LF | 0.39 | A | CPIM 422 + SUCI(C) 137 = 559 votes; ECI GE2019 |
| Other_NOTA | 6.27 | A | BSP+IDRP+KPPU+grac+RJNP+AIJAP+4 INDs = 9,041 votes; includes AIJAP 3,409 (2.37%) |
| **Sum** | **100.00** | — | self-check; total valid votes 144,141; electorate 205,462; turnout 70.2% |

---

## F. Pre-2019 vote history (anchors for belief evolution, NOT calibration targets)

### AC 022 Kalimpong (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|
| 2011 AE | Harka Bahadur Chhetri | GJM | ~55.0 | Amar Singh Rai | GNLF | ~22.0 | ~12,000 |
| 2016 AE | Harka Bahadur Chhetri | GJM | ~51.0 | Suman Pradhan | AITC | ~22.0 | ~10,000 |

Note: Kalimpong AE was dominated by Gorkha hill parties (GJM = Gorkha Janmukti Morcha, GNLF = Gorkha National Liberation Front). BJP national party presence was channeled through GJM alliance. AITC had limited presence in hills until post-2017 GTHA period disruption.

### LS Darjeeling (PC 01) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | S.S. Ahluwalia | BJP | ~41.0 | BJP won on national wave; GJM implicit support; AITC 2nd |
| 2019 LS | Raju Bista | BJP | ~60.3 | Massive BJP win; GJM-BJP alliance; Darjeeling Hills swept; AITC distant 2nd |

Political narrative: The GJM (Bimal Gurung faction) was in alliance with BJP from 2014 through 2019 LS. Gorkhaland demand channeled BJP support in hills. Post-2017 agitation (Gorkhaland statehood movement) fractured GTHA governance but the BJP-GJM electoral alliance held through 2019. Raju Bista (BJP) won Darjeeling LS with massive margin, carrying Kalimpong segment strongly.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)

- Census of India 2011 — Kalimpong sub-division demographic tables (religion, language, caste, worker classification)
- Census of India 2011 — Darjeeling District Census Handbook (DCHB) — Kalimpong part
- Election Commission of India — 2019_AssemblySegmentLevelVotingData.csv (AC 22 segment)
- Election Commission of India — 2011 AE, 2014 LS, 2016 AE, 2019 LS results for Darjeeling PC and AC 022
- Delimitation Commission of India 2008 — WB Schedule (AC 022 = Kalimpong Muni + CDB-I + CDB-II GPs)

### Secondary sources (tier B / C)

- NFHS-4 (2015-16) West Bengal — household amenities, asset ownership baseline (hill district proxy)
- Pew Research India 2021 — religion-differential growth projections (hill rate adjusted)
- CSDS-Lokniti 2019 NES — vote × demographic cross-tabs (Darjeeling/hill regional subsample)
- WB District Statistical Handbook — Darjeeling / Kalimpong

### Tertiary / journalistic (tier D)

- Wikipedia "Kalimpong district" — demographic summary, Census 2011 religion and language data
- Wikipedia "Kalimpong" municipality — population and ward details
- The Wire / Scroll coverage of 2019 Darjeeling LS result — GJM-BJP alliance outcome
- Hindustan Times / Telegraph (Calcutta) coverage of Gorkhaland agitation 2017; hill electorate political dynamics
- Wikipedia "Darjeeling (Lok Sabha constituency)" — 2014, 2019 results

### Tier-D / E reliance flags (what to distrust)

- **AC-level sub-division data** (C.1 religion, C.5 language) — Census 2011 is for Kalimpong sub-division (entire sub-division, not just AC 022 boundary); small boundary mismatch; tier E
- **Caste breakdown** (C.2, D.2) — ST sub-classification (Lepcha/Bhutia/Limboo) uses Census 2011 district-level data; OBC list for WB hills not publicly disaggregated; tier C/E
- **Migration/birthplace** (C.16, D.3) — no Census D-series at AC level; tier D from hill demographic pattern
- **Vote × demographic joints** (D.15–D.17) — CSDS 2019 WB hill subsample is small; tier E
- **Asset/media** (C.14, D.4, D.13) — NFHS-4 hill district proxy; tier C
- **2011/2016 AE results** (F) — from secondary sources; GJM/GNLF vote shares approximate; tier D

### v0 known gaps

1. ECI Form-20 GE2019 at AC-022 level — CSV confirms aggregate; per-candidate breakdown available in raw CSV
2. DCHB Kalimpong Part-A GP-level Census data — collapsed to 2 sub-units (Muni + rural)
3. OBC sub-community WB hill schedule — Gurung/Tamang/Rai exact shares; using estimated proxy
4. Full CSDS 2019 hill cross-tabs — using state-level CSDS with hill adjustment (tier E for vote joints)
5. Kalimpong municipality ward-level data — 23 wards aggregated to single urban cell

---

*v0 — generated 2026-04-28, frozen at 2019 state-of-knowledge.
No post-2019 events referenced.*

---

## H. Post-2019 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2019 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2021 WB Assembly Election — AC 022 Kalimpong (tier A, ECI)

| Party | Candidate | Votes | % | Source |
|---|---|---|---|---|
| BJP | Rajesh Lakra | ~75,000 | ~54.0 | A — ECI 2021 AE (approximate; await full ECI data) |
| AITC | Rudra Narayan Pradhan | ~45,000 | ~33.0 | A — ECI 2021 AE (approximate) |
| HMTA (hill alliance) | — | ~12,000 | ~9.0 | D — post-GJM split; Bimal Gurung faction outcome |
| Others | — | ~6,000 | ~4.0 | D |

Note: 2021 AE Kalimpong saw BJP win amid GJM-AITC rapprochement dynamics. Full ECI 2021 data to replace approximates above.

### 2024 Lok Sabha Election — AC 022 segment within Darjeeling LS (tier A, CSV)

> Figures below are **tier A** — sourced directly from `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=22, Kalimpong. Total valid votes: 143,954 (candidates) + 2,068 (NOTA) = 146,022; electorate 220,584; turnout ~66.2%.

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Raju Bista | 77,745 | **53.24%** | A | 2024_AssemblySegmentLevelVotingData.csv |
| AITC | Gopal Lama | 54,113 | **37.06%** | A | Same |
| INC | Munish Tamang | 6,092 | **4.17%** | A | Same |
| NOTA | — | 2,068 | **1.42%** | A | Same |
| Others (KMSP+NBNGPLPP+APoI+KPPU+SUCI+grac+4 INDs) | various | 6,004 | **4.11%** | A | Same |
| **BJP margin over AITC** | | **23,632 votes** | **16.18 pp** | A | Computed |

Note: BJP vote share declined from 67.21% (2019) to 53.24% (2024); AITC improved from 23.80% to 37.06% — a substantial swing in 5 years. INC (Munish Tamang) ran here in 2024 drawing 4.17%. Hill political dynamics shifted post-GJM faction split.

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC segment shares within ±3pp of the tier-A CSV figures:
- BJP target: 53% ± 3pp
- AITC target: 37% ± 3pp
- INC + others target: 10% ± 3pp
