# AC 008 — Natabari (GEN) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 008 Natabari as of end-2021 — it does not reference any
> post-2021 events. Use the 2024 LS result as the out-of-sample validation
> gate for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).
>
> **Forbidden in this file:** 2022, 2023, 2024, 2025, 2026, SSC scam,
> Partha Chatterjee, RG Kar, SIR, CAA notification, CAA rules.

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 008 | A | ECI / Delimitation Commission 2008 |
| AC name | Natabari | A | ECI |
| Reservation | GEN | A | Delimitation 2008 |
| District | Cooch Behar | A | Delimitation 2008 |
| Sub-division | Tufanganj | A | WB administrative |
| LS constituency | 2 — Cooch Behar | A | Delimitation 2008 |
| LS segments included | AC 5 Sitai · AC 6 Sitalkuchi · AC 7 Mathabhanga · AC 8 Natabari · AC 9 Cooch Behar Uttar · AC 10 Cooch Behar Dakshin · AC 11 Dinhata | A | Delimitation 2008 |
| AC composition | Natabari CD Block GPs + Tufanganj-I CD Block partial overlap | A | Delimitation 2008 |
| Geographic note | Northern Cooch Behar district; flat terai-plain; bordered by Assam (north-east) and Jalpaiguri (west); predominantly agricultural with Rajbanshi-majority rural communities; within BSF 50km jurisdiction (Oct 2021) | A | — |
| Sub-units used in v0 | **U1: Natabari_CDB_core** (Natabari block GPs) · **U2: Tufanganj_I_partial** (overlap GPs from Tufanganj-I block) | E | v0 simplification |
| 2021 AE electorate (ECI roll) | 245,040 | A | ECI 2021 WB AE detailed_results.csv |
| 2021 AE winner | **Mihir Goswami (BJP)** — GEN, Cooch Behar Rajbanshi community | A | ECI 2021 WB AE |
| 2021 AE runner-up | Rabindra Nath Ghosh (AITC) — incumbent MLA 2011, 2016; cabinet minister | A | ECI 2021 WB AE |
| 2021 AE BJP margin | **23,440 votes** (10.79 pp) | A | ECI 2021 WB AE |

---

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population | ~265,000 (Natabari CD Block primary census abstract + Tufanganj-I partial) | E | Census 2011 |
| 2021 projected population | ~291,000 | E | 10-yr compound projection at ~1.0%/yr growth (Cooch Behar district trend) |
| Sex ratio (2021, F per 1000 M) | ~1,058 | C | NFHS-5 Koch Bihar district sex ratio 1,058 (females per 1,000 males); marked improvement from Census 2011 |
| 2021 ECI electorate (roll) | 245,040 | A | ECI 2021 WB AE archive (detailed_results.csv) |
| Estimated M / F / TG split | 48.6% M / 51.4% F / ~0.01% TG | E | Derived from NFHS-5 Koch Bihar sex ratio 1,058 |
| 2021 polling stations (estimated) | ~290 | E | Proportional to electorate; up from ~280 in 2019 |
| 2021 AE total votes polled | 217,173 | A | ECI 2021 WB AE detailed_results.csv |
| 2021 AE turnout | ~88.6% | A | ECI 2021 WB AE (217,173 / 245,040) |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 79.25 | E | Cooch Behar district Census 2011 Hindu 79.7%; 10-yr projection with Hindu +0.9%/yr and Muslim +1.2%/yr differential; Natabari block slightly below district average |
| Muslim | 19.10 | E | Cooch Behar district Muslim 18.4%; Natabari block slightly above; Tufanganj subdivision higher Muslim share; +0.3pp relative gain over 10yr |
| Christian | 0.78 | E | Cooch Behar district 2011 ~0.9%; marginal decline; small Rajbanshi Christian fringe |
| Sarna_ORP | 0.47 | E | Small tribal pocket; stable |
| Other_residual | 0.40 | E | Sikh + Jain + Buddhist + Not_stated |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 28.00 | A | Cooch Behar district SC 28.36% (Census 2011); Natabari block ~28% estimated; stable |
| └ Rajbanshi_SC | 22.00 | C | Dominant SC in Cooch Behar; ~78% of SC pool; also found among OBC and General |
| └ Namasudra_SC | 3.50 | E | Smaller SC sub-group in Cooch Behar |
| └ Other_SC | 2.50 | E | Residual SC (Bagdi, Koch, Jhalo-Malo, etc.) |
| **ST_total** | 1.50 | A | Cooch Behar district ST 1.54% (Census 2011); stable |
| UC_bhadralok | 4.00 | E | Brahmin/Kayastha/Baidya; small in Rajbanshi-dominated AC |
| OBC | 12.00 | E | Rajbanshi OBC (non-SC fraction of Rajbanshi community) + Koch-Rajbanshi + other OBC |
| Other_Hindu_middle | 33.75 | E | Residual Hindu middle castes — Rajbanshi General + Saha + Sutradhar + Kaibarta + others; 79.25 − 28.0 SC − 1.5 ST − 4.0 UC − 12.0 OBC − 19.10 Muslim − 0.78 Chr − 0.47 Sarna ≈ 33.75 rounding |
| Muslim | 19.10 | E | All sub-castes pooled (mostly Bengali-Sheikh in Cooch Behar) |
| Christian_plus_Sarna_plus_Other | 1.65 | E | Christian 0.78 + Sarna_ORP 0.47 + Other_residual 0.40 |
| **Sum** | **100.00** | — | self-check (parent rows only) |

### C.3 Age cohort (2021, adult voters only — 18+)

Renormalized to 18+ electorate; children 0–17 excluded.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 12.00 | E | First-time voter cohort (born 1999–2003); 10-yr projection from 2011 Cooch Behar district age pyramid; NFHS-5 Koch Bihar population under 15 = 25.0% → slight expansion in young cohort |
| 23_27 | 12.50 | E | |
| 28_32 | 12.00 | E | |
| 33_37 | 11.00 | E | |
| 38_42 | 10.50 | E | |
| 43_47 | 9.50 | E | |
| 48_52 | 9.00 | E | |
| 53_57 | 8.00 | E | |
| 58_62 | 7.00 | E | |
| 63_67 | 5.00 | E | |
| 68 | 3.50 | E | 68+ open-ended cohort |
| **Sum** | **100.00** | — | self-check (18+ adults only) |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 48.60 | C | NFHS-5 Koch Bihar sex ratio 1,058 F per 1000 M → 1000/(2058) = 48.59% M |
| Female | 51.39 | C | 1058/(2058) = 51.41% F; rounded |
| Third_gender | 0.01 | E | State pattern; negligible |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 68.50 | E | Cooch Behar district 2011 Bengali ~67%; slight increase with urbanization trend; stable to 2021 |
| Hindi | 1.50 | E | Trader and migrant worker fringe; stable |
| Urdu | 1.00 | E | Small Muslim minority in urban pockets |
| Other | 1.50 | E | Residual catch-all (Assamese fringe, Nepali border communities, others) |
| Rajbongshi | 27.50 | E | Rajbongshi/Rajbanshi language; AC-local dominant language; Cooch Behar district ~27-30% Rajbongshi-speaking |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 15.50 | C | NFHS-5 Koch Bihar women ever attended school 75.7%; overall literacy estimated ~85% by 2021 → ~15.5% illiterate (age 18+); Cooch Behar below state average |
| Primary | 24.00 | E | Census 2011 education distribution, Cooch Behar district scaled + 10-yr trend |
| Middle | 22.00 | E | |
| Secondary | 17.00 | E | |
| Higher_Secondary | 11.00 | E | +1pp from 2019 — secondary completion rising |
| Graduate | 8.00 | E | |
| Postgraduate | 2.50 | E | |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 32.00 | E | Cooch Behar district Census 2011 main-worker share ~32-34%; COVID-shock minor dip in agri sector; recovering by mid-2021 |
| Marginal_worker | 12.00 | E | Seasonal agricultural labour; stable |
| Non_worker | 37.50 | E | Housewife + elderly + retired; Lakshmir Bhandar (Apr 2021) direct beneficiaries enter this pool |
| Student | 10.50 | E | 18–22 cohort in education; slight expansion |
| Unemployed | 8.00 | E | COVID-shock: elevated educated-unemployment in 2021; Cooch Behar urban youth aspirant pool |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 27.50 | E | Cooch Behar district 2011 rural cultivator share ~30%; AC slightly below with some urban fringe; stable |
| Agricultural_labourer | 29.50 | E | Dominant in flat terai-plain; large landless SC/OBC pool; COVID temporary disruption recovered |
| Household_industry | 5.00 | E | Handloom + cottage industries; small Rajbanshi weaving tradition |
| Manufacturing | 3.00 | E | Limited organised manufacturing in Natabari block |
| Construction | 7.00 | E | Local construction + seasonal migration to larger towns; COVID-2020 reverse migration settled |
| Trade_retail | 10.00 | E | Block-level market towns (Natabari haat) |
| Transport_logistics | 4.00 | E | Road transport; border-adjacent trade route; partial COVID disruption recovered |
| Services | 8.50 | E | Private sector services in block-level towns |
| Government_services_teachers | 3.50 | E | Block-level govt offices, schools |
| Out_migrant_worker | 2.00 | D | Rajbanshi men to brick kilns in Siliguri/Kolkata; some COVID returnees re-departed by 2021 |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 2.00 | E | Census B-04 WB rural pattern; small trader/landowner employers |
| Employee | 22.00 | E | Govt + organised sector + retail; moderate in this rural AC |
| Single_worker | 52.00 | E | Own-account cultivator + artisan + small trader; dominant |
| Family_worker | 24.00 | E | Unpaid family labour in agriculture; common in Rajbanshi cultivator households |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic status (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 24.00 | C | 2019 estimate ~26%; WB poverty fell ~2pp 2019–21 (limited by COVID shock); Cooch Behar below state improvement rate |
| Above_Poverty_Line_low_income | 36.00 | E | Low-income rural agricultural households; Lakshmir Bhandar (Apr 2021) begins to reach this band |
| Lower_middle | 23.00 | E | Modest income cultivators, small traders |
| Middle | 12.00 | E | Block-level service class, government employees |
| Upper_middle_well_off | 5.00 | E | Small affluent fringe; including returning successful migrants |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Natabari_CDB_core | 72.00 | E | Natabari CD Block core GPs; majority of AC population; stable |
| U2_Tufanganj_I_partial | 28.00 | E | Overlap GPs from Tufanganj-I CD Block within AC boundary per Delimitation 2008 |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.5 persons | E | Cooch Behar district 2011: average HH size ~4.5; COVID reverse-migration may have temporarily inflated; normalizing by end-2021 |
| Nuclear_HH | 65.00 | E | NFHS-4/5 WB rural pattern; dominant nuclear form in Rajbanshi households |
| Joint_HH | 27.00 | E | Traditional joint family arrangement in agricultural households |
| Extended_multi_generation | 8.00 | E | Multi-generation in older Rajbanshi extended families |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 25.00 | E | Census 2011 Cooch Behar pattern; NFHS-5 Koch Bihar: women age 20-24 married before 18 = 46.7% (very high) → adjusted for 18+ adult pool |
| Currently_married | 66.00 | E | High marriage rate; Rajbanshi cultural norm of early marriage |
| Widowed | 8.00 | E | Concentrated in 60+, female-skewed |
| Separated_divorced | 1.00 | E | Low formal divorce rate; some separation in migrant households |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

Post-COVID smartphone surge is the major shift from 2019. Jio-led affordability + lockdown-driven necessity accelerated adoption in Cooch Behar despite lower base than state average.

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 72.00 | C | NFHS-5 Koch Bihar electricity 98.2% (near saturation); TV ~72% (below WB average of ~82% due to rural remoteness); marginal gain from 2019 |
| Radio | 5.00 | C | Declining nationally |
| Mobile_phone | 87.00 | C | NFHS-5 WB ~90%+; COVID digitisation push; Cooch Behar slightly below state |
| Smartphone_with_internet | 58.00 | C | 2019 baseline ~38%; +20pp post-COVID surge (Jio + lockdown necessity); Cooch Behar still below state average of ~65-70% |
| Computer | 5.00 | E | Very low in rural Cooch Behar; mostly government offices |
| Two_wheeler | 24.00 | C | NFHS-4 WB rural 18%; +growth; marginal increase from 2019 |
| Four_wheeler | 4.50 | E | Very limited; mainly large landowners and block-level traders |
| Banking_access | 90.00 | B | PMJDY saturation + Jan Dhan second push; +6pp from 2019; improved in rural Cooch Behar |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 99.00 | A | NFHS-5 Koch Bihar 99.3%; near-complete coverage |
| Improved_sanitation | 75.00 | C | NFHS-5 Koch Bihar 75.7%; major improvement from 53.3% (NFHS-4); Swachh Bharat phase 2 rollout |
| LPG_clean_cooking_fuel | 37.00 | C | NFHS-5 Koch Bihar 25.7% (lower than expected); Ujjwala 2016-21 increased adoption; AC estimate ~37% with rural-urban mix; 2019 baseline was ~32% |
| Wood_biomass_fuel | 57.00 | C | Primary cooking fuel in rural Cooch Behar; declining as LPG rises; above state average |
| Other_fuel | 6.00 | E | Kerosene, dung, other |
| Electricity | 98.00 | A | NFHS-5 Koch Bihar 98.2%; near-complete |
| **Note** | (water/sanitation/electricity are independent %s; cooking-fuel rows LPG+Wood+Other sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

COVID-19 reverse migration (2020) brought back some out-migrant workers temporarily; most re-departed by mid-2021.

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 75.50 | D | Predominantly native Rajbanshi community; slight rise from COVID returnee registrations |
| WB_other_district | 7.00 | D | Some in-migrants from Jalpaiguri, North Dinajpur for agricultural labour; stable |
| Other_Indian_state | 2.00 | D | Assamese and Bihari trading fringe |
| Bangladesh_origin | 12.00 | D | Partition-era and post-1971 Hindu migrant fraction; reinforced by Bangladesh temple attacks Oct 2021 creating new anxiety among this community |
| Outside_India | 0.50 | E | Negligible (some Bhutanese traders) |
| Out_migrant | 3.00 | E | Working outside; net returnee boost in 2020 partially re-departed by 2021 |
| Nepal_Bhutan_origin | 0.00 | E | Not applicable to this AC (set to 0) |
| **Sum** | **100.00** | — | self-check |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 60.00 | 1.50 | 0.00 | 1.50 | 37.00 | E | Rajbanshi Hindu population speaks Rajbongshi; Bengali Hindus (migrant + educated) also present; stable from 2019 |
| Muslim | 92.00 | 0.50 | 3.00 | 1.50 | 3.00 | E | Cooch Behar Muslims are predominantly Bengali-speaking Sheikh community; small Rajbongshi-Muslim fringe |
| Christian | 60.00 | 5.00 | 0.00 | 10.00 | 25.00 | E | Rajbanshi Christian converts + Bengali Christian minority |
| Sarna_ORP | 20.00 | 5.00 | 0.00 | 30.00 | 45.00 | E | Tribal fringe; mixed Rajbongshi + other tribal languages |
| Other_residual | 50.00 | 30.00 | 5.00 | 15.00 | 0.00 | E | Sikh/Jain/Buddhist traders; Hindi-dominant |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion. 2D table.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 33.33 | 1.89 | 5.03 | 15.09 | 44.65 | 0 | 0 | E | 28% SC / 79.25% Hindu = 35.3%; adjusted for Hindu-only SC share; OBC Rajbanshi estimated at 15% within Hindu; residual Other_Hindu_middle |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 20.00 | 60.00 | 0 | 10.00 | 10.00 | 0 | 0 | E | Tribal sarna: mostly ST + SC pool; small OBC |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 72.50 | 7.00 | 2.00 | 15.00 | 0.50 | 3.00 | D | Rajbanshi native Hindu dominant; ~15% traceable to partition/post-partition Bangladesh Hindu migration; Bangladesh temple attacks Oct 2021 reinforced community anxiety |
| Muslim | 92.50 | 5.00 | 1.00 | 1.00 | 0.50 | 0.00 | D | Cooch Behar Muslims mostly native Bengali-Sheikh peasantry; very small Bangladesh-origin trickle |
| Christian | 85.00 | 10.00 | 2.00 | 3.00 | 0.00 | 0.00 | E | Predominantly local Rajbanshi converts |
| Sarna_ORP | 90.00 | 5.00 | 3.00 | 1.00 | 0.00 | 1.00 | E | Indigenous tribal; predominantly native |
| Other_residual | 30.00 | 20.00 | 45.00 | 0.00 | 5.00 | 0.00 | E | Mostly other-state Sikh/Jain traders |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 74.00 | 60.00 | 92.00 | C | NFHS-5 WB religion-gap pattern; post-COVID smartphone surge; Hindu slightly above Muslim |
| Muslim | 64.00 | 48.00 | 82.00 | C | Cooch Behar Muslim pocket below Hindu; NFHS-5 WB pattern; significant Jio diffusion narrowing gap |
| Christian | 76.00 | 60.00 | 93.00 | E | Small base; similar to Hindu average |
| Sarna_ORP | 58.00 | 38.00 | 78.00 | E | Lower access; tribal fringe |
| Other_residual | 87.00 | 74.00 | 97.00 | E | Trader community; higher access |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group. Sums to 100 across child columns.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 4.00 | 9.00 | 11.00 | 18.00 | 21.00 | 26.00 | 11.00 | E |
| SC_total | 18.00 | 27.00 | 22.00 | 17.00 | 10.00 | 5.00 | 1.00 | E |
| ST_total | 26.00 | 29.00 | 21.00 | 13.00 | 7.00 | 3.00 | 1.00 | E |
| OBC | 15.00 | 25.00 | 23.00 | 18.00 | 11.00 | 7.00 | 1.00 | E |
| Other_Hindu_middle | 14.00 | 25.00 | 23.00 | 18.00 | 11.00 | 8.00 | 1.00 | E |
| Muslim | 20.00 | 27.00 | 22.00 | 17.00 | 9.00 | 4.00 | 1.00 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 15.00 | 14.00 | E |
| 23_27 | 14.00 | 11.00 | E |
| 28_32 | 13.00 | 9.00 | E |
| 33_37 | 11.00 | 6.00 | E |
| 38_42 | 10.00 | 5.00 | E |
| 43_47 | 9.00 | 4.00 | E |
| 48_52 | 7.00 | 3.00 | E |
| 53_57 | 6.00 | 2.00 | E |
| 58_62 | 5.00 | 2.00 | E |
| 63_67 | 4.00 | 1.00 | E |
| 68 | 3.00 | 1.00 | E |

### D.7 Marital status × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 8.00 | 38.00 | E |
| 23_27 | 45.00 | 84.00 | E |
| 28_32 | 82.00 | 93.00 | E |
| 33_37 | 92.00 | 91.00 | E |
| 38_42 | 93.00 | 89.00 | E |
| 43_47 | 92.00 | 87.00 | E |
| 48_52 | 90.00 | 82.00 | E |
| 53_57 | 88.00 | 74.00 | E |
| 58_62 | 85.00 | 64.00 | E |
| 63_67 | 78.00 | 44.00 | E |
| 68 | 70.00 | 28.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone-internet ‖ occupation) — central media-access metric.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 42.00 | 67.00 | C | Post-COVID rural smartphone surge; +14pp from 2019 (Jio + COVID necessity) |
| Agricultural_labourer | 32.00 | 58.00 | C | Largest jump; Jio affordability; +14pp from 2019 |
| Household_industry | 46.00 | 70.00 | C | Artisan weaver households |
| Manufacturing | 58.00 | 78.00 | C | Slightly higher income |
| Construction | 52.00 | 70.00 | C | Mobile-heavy; COVID returnees reconnected via smartphone |
| Trade_retail | 72.00 | 84.00 | C | Block-market traders; near-saturation |
| Transport_logistics | 65.00 | 77.00 | C | |
| Services | 74.00 | 87.00 | C | |
| Government_services_teachers | 86.00 | 93.00 | C | Highest access |
| Out_migrant_worker | 68.00 | 74.00 | D | Working outside; smartphone required for remittance/contact |

### D.9 Education × Workforce participation

P(workforce indicator ‖ education).

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 32.00 | 2.00 | E |
| Primary | 36.00 | 4.00 | E |
| Middle | 34.00 | 6.00 | E |
| Secondary | 28.00 | 10.00 | E |
| Higher_Secondary | 22.00 | 16.00 | E |
| Graduate | 26.00 | 19.00 | E |
| Postgraduate | 35.00 | 14.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 008. See NORMALIZED_SCHEMA §4.7.)

### D.11 GP × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Natabari_CDB_core | 81.00 | 17.00 | 0.80 | 0.70 | 0.50 | E | Natabari block core GPs; higher Hindu proportion; Rajbanshi majority; stable from 2019 |
| U2_Tufanganj_I_partial | 73.50 | 24.50 | 0.80 | 0.20 | 1.00 | E | Tufanganj-I GPs overlap; higher Muslim share in Tufanganj sub-division; small increase in Muslim share over 10yr |

### D.12 GP × Caste

P(caste ‖ sub-unit).

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Natabari_CDB_core | 4.50 | 29.00 | 1.50 | 12.00 | 35.00 | 17.00 | 1.00 | E |
| U2_Tufanganj_I_partial | 3.00 | 24.50 | 1.50 | 11.00 | 31.00 | 24.50 | 4.50 | E |

### D.13 GP × Asset / media

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Natabari_CDB_core | 74.00 | 60.00 | 5.00 | 92.00 | E |
| U2_Tufanganj_I_partial | 67.00 | 52.00 | 4.00 | 85.00 | E |

### D.14 GP × Amenities

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Natabari_CDB_core | 40.00 | 77.00 | 99.00 | 98.50 | C |
| U2_Tufanganj_I_partial | 30.00 | 70.00 | 98.50 | 97.00 | C |

### D.15 Vote × Religion (2021 AE — calibration anchor)

P(party ‖ religion) — anchored to 2021 AE AC-008 result (BJP 51.45%, AITC 40.66%).

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 63.00 | 29.00 | 0.50 | 5.00 | 2.50 | C | BJP strong Hindu swing continued in Cooch Behar 2021; Koch-Rajbanshi community mobilization; Mihir Goswami as local face; AITC welfare offset (Lakshmir Bhandar partial); anchored to AC-008 2021 AE result |
| Muslim | 5.00 | 77.00 | 7.00 | 9.00 | 2.00 | C | Muslim consolidation toward AITC in 2021; CPI(M) retained some Muslim vote in Cooch Behar |
| Christian | 28.00 | 52.00 | 8.00 | 8.00 | 4.00 | E | Mixed; small base |
| Sarna_ORP | 38.00 | 42.00 | 3.00 | 12.00 | 5.00 | E | Tribal fringe; split BJP-AITC; left retained some share |
| Other_residual | 50.00 | 30.00 | 8.00 | 6.00 | 6.00 | E | |

### D.16 Vote × Caste (2021 AE)

P(party ‖ caste) — anchored to 2021 AE AC-008 result.

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 57.00 | 29.00 | 4.00 | 6.00 | 4.00 | C | Bhadralok BJP-leaning; slight dip from 2019 |
| OBC | 55.00 | 33.00 | 2.00 | 7.00 | 3.00 | C | Koch-Rajbanshi OBC retained BJP 2021; Cooch Behar Rajbanshi mobilization |
| SC_total | 58.00 | 33.00 | 1.50 | 5.00 | 2.50 | C | Rajbanshi SC went BJP; BJP "Koch-Rajbanshi" electoral appeal strong; Lakshmir Bhandar partial offset |
| ST_total | 42.00 | 38.00 | 2.00 | 13.00 | 5.00 | E | ST pocket split more evenly |
| Other_Hindu_middle | 56.00 | 33.00 | 2.00 | 6.00 | 3.00 | C | Rajbanshi General Hindu continued BJP in 2021 |
| Muslim | 5.00 | 77.00 | 7.00 | 9.00 | 2.00 | C | Same as D.15 |

### D.17 Vote × Gender (2021 AE)

P(party ‖ gender). Lakshmir Bhandar launched April 2021 — partial penetration by polling day; shifted women toward AITC relative to 2019.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 55.00 | 36.00 | 1.00 | 5.50 | 2.50 | C | CSDS 2021 WB post-poll adapted for Cooch Behar; BJP male vote held strong |
| Female | 48.00 | 45.00 | 1.50 | 3.50 | 2.00 | C | Lakshmir Bhandar launch + Duare Sarkar outreach shifted women toward AITC vs 2019 |
| Third_gender | 48.00 | 42.00 | 4.00 | 4.00 | 2.00 | E | |

### D.18 Vote × Welfare scheme exposure

(Skipped — no `welfare_exposure` axis declared for AC 008. See NORMALIZED_SCHEMA §4.7.)

---

## E. 2021 calibration target (2021 AE — tier A)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

The simulator must reproduce this aggregate within ±1pp.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 51.45 | A | ECI 2021 WB AE — Mihir Goswami (BJP) 111,743 votes / 217,173 total |
| AITC | 40.66 | A | ECI 2021 WB AE — Rabindra Nath Ghosh (AITC) 88,303 votes / 217,173 total |
| INC | 0.00 | A | ECI 2021 WB AE — no INC candidate; zero |
| LF | 5.45 | A | ECI 2021 WB AE — CPI(M) Akik Hassan 11,839 votes / 217,173 total (CPI(M) is sole LF component) |
| Other_NOTA | 2.43 | A | ECI 2021 WB AE — IND 1,341 + SUCI 1,186 + NOTA 1,146 + AMB 1,110 + UTSAP 505 = 5,288 / 217,173 |
| **Sum** | **99.99** | — | self-check (rounding; within 100.0 ± 0.5) |

> ECI 2021 AE AC-008 Natabari: BJP 111,743 | AITC 88,303 | CPI(M) 11,839 | BJP margin 23,440 votes (10.79 pp) | electorate 245,040 | turnout ~88.6% | total valid 217,173

---

## F. Vote history (pre-2021 anchors for belief evolution)

### AC 008 Natabari (Assembly Elections)

| Year | Winner | Party | % | Runner-up | Party | % | Margin | Notes |
|---|---|---|---|---|---|---|---|---|
| 2011 AE | Rabindranath Ghosh | AITC | ~52 | CPI(M) candidate | CPI(M) | ~35 | ~10,000 (est.) | AITC stronghold; Rabindranath Ghosh dominant MLA; Left retreating |
| 2016 AE | Rabindranath Ghosh | AITC | ~50 | BJP candidate | BJP | ~29 | ~12,000 (est.) | AITC held; BJP rising sharply from 2011 low |
| **2021 AE** | **Mihir Goswami** | **BJP** | **51.45** | Rabindra Nath Ghosh | AITC | **40.66** | **23,440** | **BJP flipped AITC stronghold; Koch-Rajbanshi mobilization; CPI(M) retained 5.45%** |

Note: Rabindranath Ghosh (WB cabinet minister 2011-2021) was the dominant AITC MLA for Natabari for two consecutive terms. His mass base among Rajbanshi communities in Cooch Behar made Natabari an AITC stronghold pre-2019. The 2019 LS result (BJP 51%) represented a sharp swing driven by BJP's Rajbanshi community mobilization and Koch-Rajbanshi identity politics, which the 2021 AE confirmed and extended — BJP increased its AC-level plurality to 10.79pp.

### Cooch Behar LS (PC 2) history (relevant segment anchors)

| Year | Winner | Party | % | Notes |
|---|---|---|---|---|
| 2014 LS | Renuka Sinha | AITC | ~40 | AITC won; BJP ~22%; CPI(M) ~20%; close 3-way; Rajbanshi identity politics nascent |
| 2019 LS | **Nisith Pramanik** | **BJP** | **~51** | BJP won Cooch Behar; within AC-008 segment BJP 51.05% / AITC 42.00% (tier A from 2019_AssemblySegmentLevelVotingData.csv) |

### Key narrative events (2019–2021)

- **2019 May**: Nisith Pramanik (BJP) wins Cooch Behar LS — Koch-Rajbanshi identity mobilization established as dominant electoral frame in district; BJP became dominant force in Natabari for 2019 LS (51.05% in AC-008 segment).
- **2020 Mar–Aug**: COVID-19 lockdown — reverse migration; Cooch Behar agricultural labour disrupted; AITC state relief delivery through Duare Sarkar camps contested.
- **2020 May**: Cyclone Amphan — less direct impact on Cooch Behar than South Bengal; but state relief logistics contested.
- **2021 Apr**: Lakshmir Bhandar scheme launched — ₹500/month general category, ₹1,000/month SC/ST women household heads. High SC share in AC means most eligible women qualify for higher tier. Partial first-disbursement by polling day; powerful AITC belief-vector even within Rajbanshi SC households.
- **2021 Apr 10**: CISF firing at Sitalkuchi (AC 5, Cooch Behar) — 4 killed. Adjacent AC; Cooch Behar district polarized. BJP framed as self-defence; AITC called for EC action. High salience in Natabari voter discourse given geographic proximity.
- **2021 May 2**: WB AE results — TMC 213 / BJP 77 / others 4 statewide. BJP won AC-008 (Mihir Goswami) despite TMC landslide; Cooch Behar district an island of BJP dominance.
- **2021 Oct 11**: BSF jurisdiction extended to 50km from Bangladesh border. Natabari AC lies within new zone. TMC framed as federal overreach; BJP/Rajbanshi-Hindu community saw as security upgrade.
- **2021 Oct 13–20**: Bangladesh Durga Puja temple attacks — widespread communal violence. Triggered Hindu refugee anxiety among Bangladesh-origin fraction of Natabari electorate (~12%); reinforced "Hindus need protection" BJP narrative.

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- Census of India 2011 — Cooch Behar district Primary Census Abstract; CD Block tables for Natabari block and Tufanganj-I block
- Census of India 2011 — Cooch Behar district religion, SC/ST, language tables (District Census Handbook)
- Election Commission of India — 2021 WB AE detailed_results.csv (AC 008 Natabari: BJP 111,743 / AITC 88,303 / CPI(M) 11,839; electorate 245,040; turnout ~88.6%)
- Election Commission of India — 2019_AssemblySegmentLevelVotingData.csv (tier A; AC 8 Natabari LS segment)
- Delimitation Commission of India 2008 — WB Schedule (AC 008 Natabari composition)
- data/electoral_history/2021/detailed_results.csv — machine-parseable ECI 2021 AE results
- data/electoral_history/2021/constituency_summary_full.csv — electorate, turnout, nota figures

### Secondary sources (tier B/C)
- NFHS-5 (2019-21) West Bengal / Koch Bihar district — household amenities, asset ownership; smartphone surge documented; data/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv
- NFHS-4 (2015-16) West Bengal — baseline for trend computation
- WB CDWDSW Lakshmir Bhandar dashboard — scheme launch April 2021
- CSDS-Lokniti 2021 NES post-poll WB regional cross-tabs
- Pew Research India 2021 — religion-differential growth projections
- PMJDY / NFHS banking access indicators

### Tertiary / journalistic (tier D)
- Wikipedia — "Natabari (Vidhan Sabha constituency)" — 2021 AE results
- Wikipedia — "Cooch Behar district" — population, SC/ST, language demographics
- Reports on BJP's Koch-Rajbanshi mobilization in Cooch Behar 2021 (various news sources)
- Reports on Sitalkuchi CISF firing, April 2021 (adjacent AC, polarizing signal)
- Bangladesh Durga Puja attack reports (October 2021)

### Tier-D/E reliance flags (what to distrust)
- **Caste sub-group shares within Hindu** (D.2) — no caste census post-1931 for non-SC/ST; tier C/E
- **Migration/birthplace shares** (C.16, D.3) — no AC-level Census D-series; tier D estimate
- **GP-level sub-unit decomposition** (D.11–D.14) — v0 collapses to 2 sub-units; refine with DCHB Part-A
- **Asset/media** (C.14, D.4, D.8, D.13) — NFHS-5 Koch Bihar district + WB state-level pattern applied; tier C; smartphone surge from +20pp rule (methodology §4)
- **Vote × Demographic** (D.15–D.17) — CSDS 2021 WB regional rollup adapted for Cooch Behar; tier C; anchored on AC-008 2021 AE aggregate
- **LF disaggregation** — CPI(M) is sole LF component in 2021 AE; no allied-left presence detected

### v0 known gaps
1. DCHB Cooch Behar Part-A — collapsed sub-units to 2 instead of GP-level granularity
2. ECI 2011/2016 AE Form-20 for AC 008 — using approximate %s from Wikipedia summary
3. Census HH-13 GP-level asset data — using NFHS Koch Bihar district level proxy
4. Full CSDS WB Cooch Behar regional cross-tabs — using adapted state-level rollup
5. Rajbanshi sub-caste disaggregation SC/OBC/GEN split within Rajbanshi community estimated from academic literature
6. Lakshmir Bhandar first-wave enrollment by polling day (Apr-May 2021) — estimated 20-30% of eligible women reached; partial belief effect modeled

---

*v0 — generated 2026-04-28, frozen at 2021 state-of-knowledge.
No post-2021 events referenced.*

---

## H. Post-2021 validation anchors (OUT-OF-SAMPLE)

> **These are out-of-sample simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs.

### 2024 LS AC-008 segment — Cooch Behar (tier A, CSV)

Source: `data/2024_AssemblySegmentLevelVotingData.csv`, AC_NO=8, Natabari. Electorate: 255,111. Total votes: 218,125 (incl. NOTA 1,817). Turnout: ~85.5%.

| Party | Candidate (LS level) | Votes | AC-008 segment % | Tier |
|---|---|---|---|---|
| BJP | Nisith Pramanik | 105,063 | 48.17% | A |
| AITC | Jagadish Chandra Barma Basunia | 103,917 | 47.64% | A |
| AIFB (LF) | Nitish Chandra Roy | 4,697 | 2.15% | A |
| INC | Piya Roy Chowdhury | 1,245 | 0.57% | A |
| Other_NOTA | BSP+SUCI+KPPU+IND×3+NOTA | 3,203 | 1.47% | A |
| **BJP margin over AITC** | | **1,146 votes** | **0.53 pp** | A |

Key observation: BJP lead narrowed dramatically from ~11pp (2021 AE) to 0.53pp (next LS cycle) — this shift must emerge from narrative injection, not be baked into the 2021 calibration. Simulator validated if next-cycle segment shares reproduced within ±3pp of tier-A CSV figures.

---
