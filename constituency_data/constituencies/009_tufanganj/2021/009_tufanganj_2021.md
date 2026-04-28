# AC 009 — Tufanganj (GEN) — Calibrated 2021 Population Snapshot

> **Frozen at end-2021.** This file describes the demographic and behavioural
> state of AC 009 Tufanganj as of end-2021 only — it does not reference any
> post-2021 events. Use post-2021 elections (2024 LS) as out-of-sample
> validation gates for downstream simulators.
>
> Companion artifacts: [`methodology_2021.md`](../../../../../../constituency_data/methodology_2021.md) ·
> [`csv/`](csv/) (machine-parseable joint tables)
>
> All tables use the standardized 4-column format: `Category | % | Tier | Source`.
> Tiers: A (direct hard data), B (sub-AC dashboard aggregated),
> C (academic/CSDS regional), D (journalistic), E (modeled imputation).

---

## A. Identity (as of 2021)

| Field | Value | Tier | Source |
|---|---|---|---|
| AC number | 009 | A | ECI / Delimitation Commission 2008 |
| AC name | Tufanganj | A | ECI |
| Reservation | GEN (General) | A | Delimitation 2008 |
| District | Cooch Behar | A | Delimitation 2008 |
| Sub-division | Tufanganj | A | WB administrative |
| LS constituency | 02 — Cooch Behar (SC reserved) | A | Delimitation 2008 |
| LS segments included | AC 005 Mekhliganj · 006 Mathabhanga · 007 Cooch Behar Uttar · 008 Cooch Behar Dakshin · 009 Tufanganj · 010 Sitalkuchi · 011 Sitai | A | Delimitation 2008 |
| AC composition | Tufanganj Municipality (full) + Tufanganj II CD Block (full) + 4 GPs of Tufanganj I CD Block: Andaran Fulbari I, Balabhut, Dhalpal I, Nakkatigachh | A | Delimitation 2008 |
| Geographic note | North Bengal plains, Tufanganj subdivision; borders Assam; Torsa and Kaljani river basin; Bangladesh-adjacent northern corridor | A | — |
| Sub-units used in v0 | **U1: Tufanganj_Municipality** (urban) · **U2: Tufanganj_II_CDB_and_rural** (Tufanganj II full + 4 GPs from Tufanganj I) | E | v0 simplification |

## B. 2021 population & electorate

| Field | Value | Tier | Source |
|---|---|---|---|
| 2011 base population (estimated) | ~210,000 (Tufanganj Muni 20,998 + Tufanganj II CDB 186,726 + ~4/72 rural share of Tufanganj I ≈ ~13,800) | E | Census 2011; v0 GP-share approximation |
| 2021 projected population | ~233,000 | E | 10-yr compound religion-differential growth from Census 2011 (methodology §4): Hindu ~1.0%/yr · Muslim ~1.3%/yr; AC pop-weighted ~1.05%/yr |
| Sex ratio (2021, F per 1000 M) | ~1,058 | B | NFHS-5 (2019-21) Koch Bihar district: 1,058 F per 1,000 M — notable improvement from Census 2011 baseline of 952 |
| 2021 estimated electorate (18+) | 234,311 | A | ECI 2021 WB Assembly Election — AC 009 total electors (electoral_history/2021/detailed_results.csv) |
| Estimated M / F / TG split (2021) | 49.3% M / 50.6% F / <0.1% TG | E | Derived from NFHS-5 sex ratio 1058; improved female share vs 2019 |
| 2021 valid votes cast | 209,378 | A | ECI 2021 AE — sum of all candidate + NOTA votes |
| 2021 turnout | ~89.4% | A | 209,378 valid / 234,311 electorate |
| 2021 polling stations (estimated) | ~260 | E | Projected from 2019 ~250; electorate growth |

---

## C. Marginal distributions (16 attribute axes)

### C.1 Religion (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Hindu | 84.20 | E | 2019 baseline 84.5%; 2yr Muslim differential growth (+~0.15pp); Tufanganj II CDB 2011: 85.60% Hindu anchor; pop-weighted with Muni and 4 GPs |
| Muslim | 15.30 | E | 2019 baseline 15.0%; slight 2yr relative gain (+0.3pp); Tufanganj II 14.15%; rural GP pocket higher |
| Christian | 0.30 | E | Unchanged; Cooch Behar district baseline; small urban pocket |
| Sarna_ORP | 0.10 | E | Marginal; stable |
| Other_residual | 0.10 | E | Sikh + Jain + Buddhist + Not_stated lumped |
| **Sum** | **100.00** | — | self-check |

### C.2 Caste / community (within total population)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| **SC_total** | 47.00 | A | Pop-weighted: Tufanganj II CDB (53.8%) + Muni (23.03%) + 4 GPs Tufanganj I (~46%); Census 2011 anchor; stable to 2021 |
| └ Rajbanshi_SC | 43.00 | C | ~91.5% of SC pool; dominant SC community in Cooch Behar; Rajbanshi ~75% of SC in district (The Print) |
| └ Other_SC | 4.00 | E | Namasudra, Bagdi, Chamar residual |
| **ST_total** | 1.50 | A | Tufanganj II 2.1% + Muni 0.41% weighted; Census 2011 anchor |
| UC_bhadralok | 5.00 | E | Brahmin/Kayastha concentrated in Muni; stable |
| OBC | 4.00 | E | Koch (non-SC), Teli, Sutradhar etc.; stable |
| Other_Hindu_middle | 27.00 | E | Residual Hindu (84.2 − 47 − 1.5 − 5 − 4) ≈ 26.7 → rounded 27; stable from 2019 |
| Muslim | 15.30 | E | All sub-castes pooled; see C.1 update |
| Christian_plus_Sarna_plus_Other | 0.20 | E | C.1 residual combined |
| **Sum** | **100.00** | — | self-check |

### C.3 Age cohort (2021, adult voters only — 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| 18_22 | 11.00 | E | 2yr cohort aging from 2019 pyramid; slight shift as 2019 18-22 ages into 20-24; Cooch Behar Census 2011 age pyramid renormalized for 18+ adults |
| 23_27 | 12.00 | E | Stable |
| 28_32 | 11.50 | E | Stable |
| 33_37 | 10.50 | E | Stable |
| 38_42 | 9.50 | E | Stable |
| 43_47 | 9.00 | E | Stable |
| 48_52 | 8.00 | E | Stable |
| 53_57 | 7.50 | E | Slight aging-in |
| 58_62 | 6.50 | E | Slight aging-in |
| 63_67 | 7.50 | E | |
| 68 | 7.00 | E | 68+ open-ended; slight aging-in from 2019 |
| **Sum** | **100.00** | — | self-check (renormalized from Census 2011 after excluding 0–17; 2yr cohort-aging applied) |

### C.4 Gender (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Male | 49.27 | B | NFHS-5 Koch Bihar sex ratio 1,058 F per 1,000 M → 1000/2058 = 48.59%; electorate pattern may differ; use ~49.3% M for adult voter share (ECI roll tends to be closer to parity) |
| Female | 50.72 | B | Derived; NFHS-5 Koch Bihar improved female ratio |
| Third_gender | 0.01 | E | Marginal |
| **Sum** | **100.00** | — | self-check |

### C.5 Mother tongue (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Bengali | 79.00 | E | Stable from 2019; district dominant |
| Hindi | 0.50 | E | Muni trader + migrant fringe; stable |
| Urdu | 0.50 | E | Muslim urban pocket; stable |
| Other | 0.50 | E | Residual catch-all; stable |
| Rajbongshi | 19.50 | C | Rajbongshi spoken by Rajbanshi SC (~43% of pop); significant in Tufanganj; Census 2011 Cooch Behar pattern; stable |
| **Sum** | **100.00** | — | self-check |

### C.6 Education level (2021, age 7+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Illiterate | 20.00 | E | 2019: ~22%; 2yr literacy trend improvement ~1pp/yr → ~20%; NFHS-5 Koch Bihar women literate 79.2% (B); literacy gains continuing |
| Primary | 22.00 | E | Stable |
| Middle | 20.00 | E | Stable |
| Secondary | 17.50 | E | Slight increase with mid-school expansion |
| Higher_Secondary | 10.50 | E | Slight increase |
| Graduate | 7.50 | E | Slight increase; college expansion in Cooch Behar |
| Postgraduate | 2.50 | E | Slight increase |
| **Sum** | **100.00** | — | self-check |

### C.7 Workforce status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Main_worker | 31.00 | E | COVID-19 impact: slight dip from 2019 32%; reverse migration returned some workers; 2020 disruption stabilised by 2021 |
| Marginal_worker | 14.00 | E | Slight uptick from 2019 13%; COVID-19 pushed some full workers to marginal category |
| Non_worker | 38.00 | E | Stable; Lakshmir Bhandar (Apr 2021) may slightly shift female non-workers to welfare recipient category — minor in raw workforce terms |
| Student | 9.00 | E | Stable |
| Unemployed | 8.00 | E | Stable; COVID-19 disruption offset by return migration from metro centres |
| **Sum** | **100.00** | — | self-check |

### C.8 Occupation (within main + marginal workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Cultivator | 22.00 | E | Stable; COVID-19 reverse migration briefly increased cultivator count |
| Agricultural_labourer | 34.00 | E | Slight decrease vs 2019 35%; some shift to construction due to return migration |
| Household_industry | 5.00 | E | Stable |
| Manufacturing | 3.00 | E | Stable; very limited organised sector |
| Construction | 7.00 | E | Slight increase from 2019 6%; COVID-19 return migrants re-entered construction |
| Trade_retail | 10.00 | E | Stable; Muni hub |
| Transport_logistics | 5.00 | E | Stable |
| Services | 7.00 | E | Stable |
| Government_services_teachers | 4.00 | E | Stable |
| Out_migrant_worker | 3.00 | D | Slight uptick recovery post-COVID-19; Assam tea garden + metro cities corridor |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.9 Class of worker (within workers, 2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Employer | 1.50 | E | Stable |
| Employee | 22.00 | E | Stable |
| Single_worker | 52.00 | E | Own-account cultivator + artisan + small trader dominant; stable |
| Family_worker | 24.50 | E | Stable |
| **Sum** | **100.00** | — | self-check (across workers) |

### C.10 Economic / poverty (2021, household level)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| BPL_household | 26.00 | C | 2019: ~28%; WB poverty trend decline continues ~1pp/yr; COVID-19 may have reversed some gains; net ~26%; Cooch Behar district BPL high SC share |
| Above_Poverty_Line_low_income | 35.00 | E | Stable |
| Lower_middle | 23.00 | E | Slight uptick as some BPL households cross threshold |
| Middle | 13.00 | E | Slight uptick |
| Upper_middle_well_off | 3.00 | E | Stable; Muni small affluent fringe |
| **Sum** | **100.00** | — | self-check |

### C.11 GP / Sub-unit location (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| U1_Tufanganj_Municipality | 9.00 | E | 2011: Muni 20,998 / AC ~233,000 projected = ~9.0%; minor decline in urban share as rural area grew slightly faster |
| U2_Tufanganj_II_CDB_and_rural | 91.00 | E | Tufanganj II CDB + 4 GPs Tufanganj I; remainder |
| **Sum** | **100.00** | — | self-check |

### C.12 Household composition (2021)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Avg_HH_size | 4.4 persons | E | WB 2011: 4.3; North Bengal slightly higher; minor change 2yr |
| Nuclear_HH | 67.00 | E | NFHS-5 WB rural trend; slight increase from 2019 66% |
| Joint_HH | 26.00 | E | Slight decrease |
| Extended_multi_generation | 7.00 | E | Stable |
| **Sum** | **100.00** | — | self-check (3 partition rows) |

### C.13 Marital status (2021, age 18+)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Never_married | 26.00 | E | Stable; Census 2011 Cooch Behar pattern; NFHS-5 Koch Bihar women married before 18: 46.7% still high but adult never-married cohort at 18+ stable |
| Currently_married | 65.00 | E | Stable; rural-dominant AC; high marriage rate |
| Widowed | 8.00 | E | Stable; concentrated in 60+; female-skewed |
| Separated_divorced | 1.00 | E | Stable |
| **Sum** | **100.00** | — | self-check |

### C.14 Asset / media access (2021, household level)

| Flag | % of HH owning | Tier | Source / Note |
|---|---|---|---|
| Television | 72.00 | C | 2019 baseline 68%; +4pp over 2yr; NFHS-5 WB rural TV saturation trend; urban Muni near-saturated |
| Radio | 5.00 | C | Declining; minor drop from 2019 6% |
| Mobile_phone | 88.00 | C | 2019: 82%; post-COVID-19 mobile adoption accelerated; PMJDY + welfare delivery via mobile boosted |
| Smartphone_with_internet | 60.00 | C | 2019: 38%; +22pp — COVID-19 drove major smartphone surge in rural North Bengal; Jio cheapened data; NFHS-5 WB rural smartphone diffusion; methodology §C.14 shift +20-30pp |
| Computer | 5.00 | C | Stable; negligible rural penetration change |
| Two_wheeler | 23.00 | C | 2019: 22%; slight uptick |
| Four_wheeler | 4.00 | C | Stable |
| Banking_access | 90.00 | B | 2019: 85%; PMJDY near-saturation + Lakshmir Bhandar (Apr 2021) Jan Dhan accounts required → +5pp push; Koch Bihar PMJDY high enrollment; methodology §C.14 +5-10pp |
| **Note** | (independent ownership %s — do not sum) | — | — |

### C.15 Household amenities (2021)

| Flag | % of HH with | Tier | Source / Note |
|---|---|---|---|
| Improved_drinking_water_source | 99.00 | B | NFHS-5 Koch Bihar: 99.3% improved water — near universal coverage; up from NFHS-4 98.8%; AC weighted ~99% |
| Improved_sanitation | 75.00 | B | NFHS-5 Koch Bihar: 75.7% improved sanitation (up from NFHS-4 53.3%); Swachh Bharat Phase 2 impact; AC ~75% |
| LPG_clean_cooking_fuel | 26.00 | B | NFHS-5 Koch Bihar: 25.7% clean cooking; up from NFHS-4 13.7%; Ujjwala Phase 1+2; AC ~26%; rural lag persists |
| Wood_biomass_fuel | 69.00 | C | Dominant rural fuel; declining as LPG uptake increases; estimated 2019 67% → 69% accounting for some reversal |
| Other_fuel | 5.00 | C | Kerosene, dung, etc.; stable |
| Electricity | 98.00 | B | NFHS-5 Koch Bihar: 98.2% electricity; Saubhagya scheme near-completion; AC ~98% |
| **Note** | (water/sanitation/electricity independent; cooking-fuel rows sum to 100) | — | — |

### C.16 Migration / birthplace (2021, all ages)

| Category | % | Tier | Source / Note |
|---|---|---|---|
| Native | 78.00 | D | 2019: 78%; COVID-19 reverse migration from metro centres mostly temporary; stable by end-2021; BSF 50km jurisdiction (Oct 2021) did not alter native share |
| WB_other_district | 8.00 | D | Stable; some in-migration from Jalpaiguri, North Dinajpur |
| Other_Indian_state | 3.00 | D | Stable; Assamese, Bihari, migrant workers |
| Bangladesh_origin | 8.00 | D | Stable; Hindu refugee population (post-1947 + 1971); border anxiety present in community post Bangladesh temple attacks (Oct 2021) but no new migration wave |
| Outside_India | 0.50 | E | Negligible; minor Nepal/Bhutan-origin in border fringe |
| Out_migrant | 2.50 | E | COVID-19 disrupted out-migration; partial recovery by end-2021; registered here but working outside |
| Nepal_Bhutan_origin | 0.00 | E | Border area; set 0 — negligible for AC level; included in Outside_India |
| **Sum** | **100.00** | — | self-check (78+8+3+8+0.5+2.5 = 100.0) |

---

## D. Joint conditional distributions

### D.1 Religion × Mother tongue

P(language ‖ religion) — % within each religion's population.

| Religion | Bengali | Hindi | Urdu | Other | Rajbongshi | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 73.00 | 0.50 | 0.00 | 0.50 | 26.00 | E | Stable from 2019; Rajbongshi speakers predominantly Hindu Rajbanshi-SC; Cooch Behar Census 2011 pattern |
| Muslim | 92.00 | 1.00 | 4.50 | 2.50 | 0.00 | E | Stable; Bengali-Muslim (Koch Bihar pattern); small Urdu-speaking pocket in Muni |
| Christian | 90.00 | 5.00 | 0.00 | 5.00 | 0.00 | E | Tiny base; Bengali + mission-school families |
| Sarna_ORP | 60.00 | 10.00 | 0.00 | 30.00 | 0.00 | E | Tribal languages; approximated |
| Other_residual | 70.00 | 20.00 | 0.00 | 10.00 | 0.00 | E | Marwari/other trader pop |

### D.2 Religion × Caste

P(caste ‖ religion) — % within each religion's population.

| Religion | SC_total | ST_total | UC_bhadralok | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hindu | 53.85 | 1.78 | 5.92 | 4.73 | 31.95 | 0 | 1.78 | E | Stable from 2019; SC 47/84.2=55.8% of Hindu → minor AC-blend adjustment for Muni dilution; ~53.85% |
| Muslim | 0 | 0 | 0 | 0 | 0 | 100 | 0 | A | self-evident |
| Christian | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |
| Sarna_ORP | 0 | 90 | 0 | 5 | 5 | 0 | 0 | E | Tribal sub-castes route to ST_total |
| Other_residual | 0 | 0 | 0 | 0 | 0 | 0 | 100 | A | self-evident |

### D.3 Religion × Migration

P(birthplace ‖ religion) — % within each religion.

| Religion | Native | WB_other_district | Other_Indian_state | Bangladesh_origin | Outside_India | Out_migrant | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| Hindu | 75.00 | 8.00 | 3.00 | 11.50 | 0.50 | 2.00 | D | Stable from 2019; Rajbanshi Hindu largely native; Bangladesh-origin subset from pre-1971 trickle |
| Muslim | 90.00 | 5.00 | 2.00 | 2.00 | 0.50 | 0.50 | D | Stable; Koch Bihar Muslims mostly native Bengali-peasantry |
| Christian | 80.00 | 12.00 | 5.00 | 3.00 | 0.00 | 0.00 | E | Mixed; mission community |
| Sarna_ORP | 85.00 | 10.00 | 5.00 | 0.00 | 0.00 | 0.00 | E | Tribal population locally rooted |
| Other_residual | 40.00 | 15.00 | 40.00 | 5.00 | 0.00 | 0.00 | E | Marwari/trader community mostly other-state |

### D.4 Religion × Asset / media

P(owns flag ‖ religion) — % within each religion; updated for 2021 smartphone surge.

| Religion | Television | Smartphone_with_internet | Banking_access | Tier | Source |
|---|---|---|---|---|---|
| Hindu | 73.00 | 61.00 | 91.00 | C | 2019 baseline shifted up: TV +4pp; Smartphone +22pp (COVID-19 surge); Banking +5pp (Lakshmir Bhandar Jan Dhan drive); NFHS-5 WB religion gap pattern |
| Muslim | 63.00 | 51.00 | 80.00 | C | Similar absolute gains but lower base; NFHS-5 WB Muslim HH asset gap persists |
| Christian | 83.00 | 62.00 | 94.00 | E | Small base; educated; higher smartphone adoption |
| Sarna_ORP | 58.00 | 34.00 | 74.00 | E | Marginal tribal population; slower smartphone adoption |
| Other_residual | 92.00 | 80.00 | 97.00 | E | Trader/upper-income; near-saturated |

### D.5 Caste × Education

P(highest education ‖ caste) — adults 18+, % within caste group; 2yr improvement modest.

| Caste | Illiterate | Primary | Middle | Secondary | Higher_Secondary | Graduate | Postgraduate | Tier |
|---|---|---|---|---|---|---|---|---|
| UC_bhadralok | 7.00 | 12.00 | 14.00 | 20.00 | 18.00 | 21.00 | 8.00 | E |
| SC_total | 22.00 | 24.00 | 21.00 | 17.00 | 9.00 | 5.50 | 1.50 | E |
| ST_total | 26.00 | 26.00 | 20.00 | 15.00 | 7.50 | 4.00 | 1.50 | E |
| OBC | 16.00 | 22.00 | 20.00 | 19.00 | 13.00 | 8.00 | 2.00 | E |
| Other_Hindu_middle | 16.00 | 23.00 | 21.00 | 18.50 | 11.50 | 7.50 | 2.50 | E |
| Muslim | 20.00 | 25.00 | 21.00 | 17.50 | 10.00 | 5.00 | 1.50 | E |

### D.6 Age × Gender × Education

P(grad+ ‖ age × gender) — graduate-or-higher share; 5-year cohorts.

| Age_cohort | Male_grad_plus | Female_grad_plus | Tier |
|---|---|---|---|
| 18_22 | 13.00 | 11.00 | E |
| 23_27 | 14.00 | 10.00 | E |
| 28_32 | 12.00 | 8.00 | E |
| 33_37 | 10.00 | 6.00 | E |
| 38_42 | 8.50 | 4.50 | E |
| 43_47 | 7.50 | 3.50 | E |
| 48_52 | 6.50 | 2.50 | E |
| 53_57 | 5.50 | 2.00 | E |
| 58_62 | 4.50 | 1.50 | E |
| 63_67 | 3.50 | 1.00 | E |
| 68 | 3.00 | 1.00 | E |

### D.7 Marital × Age × Gender

P(currently married ‖ age × gender).

| Age_cohort | Male | Female | Tier |
|---|---|---|---|
| 18_22 | 6.00 | 28.00 | E |
| 23_27 | 40.00 | 80.00 | E |
| 28_32 | 78.00 | 92.00 | E |
| 33_37 | 88.00 | 90.00 | E |
| 38_42 | 90.00 | 88.00 | E |
| 43_47 | 90.00 | 84.00 | E |
| 48_52 | 88.00 | 78.00 | E |
| 53_57 | 86.00 | 68.00 | E |
| 58_62 | 82.00 | 55.00 | E |
| 63_67 | 76.00 | 40.00 | E |
| 68 | 68.00 | 28.00 | E |

### D.8 Occupation × Asset / media

P(owns smartphone ‖ occupation) — updated for 2021 smartphone surge.

| Occupation | Smartphone_with_internet | Television | Tier | Source |
|---|---|---|---|---|
| Cultivator | 46.00 | 64.00 | C | 2019: 28%/60%; COVID-19 smartphone surge +18pp for cultivators; North Bengal rural agriculture |
| Agricultural_labourer | 38.00 | 54.00 | C | 2019: 20%/50%; significant jump; PMJDY + welfare delivery via mobile |
| Household_industry | 50.00 | 69.00 | C | 2019: 32%/65% |
| Manufacturing | 62.00 | 78.00 | C | Stable growth |
| Construction | 56.00 | 69.00 | C | 2019: 38%/65%; COVID-19 return migrants brought smartphones |
| Trade_retail | 76.00 | 88.00 | C | 2019: 62%/85%; Muni concentrated; high adoption |
| Transport_logistics | 70.00 | 82.00 | C | 2019: 55%/78% |
| Services | 78.00 | 88.00 | C | 2019: 65%/85% |
| Government_services_teachers | 90.00 | 95.00 | C | Near-saturated |
| Out_migrant_worker | 78.00 | 75.00 | D | Heavy smartphone use for remittances; slight TV decline as away |

### D.9 Education × Workforce participation

| Education | Main_worker_rate | Unemployed_seeking | Tier |
|---|---|---|---|
| Illiterate | 30.00 | 2.00 | E |
| Primary | 34.00 | 3.00 | E |
| Middle | 32.00 | 6.00 | E |
| Secondary | 28.00 | 8.00 | E |
| Higher_Secondary | 22.00 | 15.00 | E |
| Graduate | 25.00 | 19.00 | E |
| Postgraduate | 35.00 | 13.00 | E |

### D.10 Asset / media × Bilingualism

(Skipped — no `media_tier` axis declared for AC 009. See NORMALIZED_SCHEMA.md §4.7.)

### D.11 Sub-unit × Religion

P(religion ‖ sub-unit).

| Sub_unit | Hindu | Muslim | Christian | Sarna_ORP | Other_residual | Tier | Source |
|---|---|---|---|---|---|---|---|
| U1_Tufanganj_Municipality | 82.00 | 16.50 | 1.00 | 0.10 | 0.40 | E | Stable from 2019; Muni 2011 pattern; urban Muslim slightly higher than rural |
| U2_Tufanganj_II_CDB_and_rural | 84.80 | 14.90 | 0.20 | 0.10 | 0.00 | A | Tufanganj II CDB 2011: 85.60% Hindu, 14.15% Muslim (A); 4 GP rural share weighted; marginal 2yr drift |

### D.12 Sub-unit × Caste

P(caste ‖ sub-unit).

| Sub_unit | UC_bhadralok | SC_total | ST_total | OBC | Other_Hindu_middle | Muslim | Christian_plus_Sarna_plus_Other | Tier |
|---|---|---|---|---|---|---|---|---|
| U1_Tufanganj_Municipality | 12.00 | 23.00 | 0.50 | 6.00 | 40.50 | 16.50 | 1.50 | E |
| U2_Tufanganj_II_CDB_and_rural | 4.00 | 50.50 | 1.60 | 3.70 | 24.70 | 14.90 | 0.60 | E |

### D.13 Sub-unit × Asset / media

Updated for 2021 smartphone surge.

| Sub_unit | Television | Smartphone_with_internet | Computer | Banking_access | Tier |
|---|---|---|---|---|---|
| U1_Tufanganj_Municipality | 88.00 | 74.00 | 13.00 | 96.00 | C |
| U2_Tufanganj_II_CDB_and_rural | 69.00 | 56.00 | 3.00 | 89.00 | C |

### D.14 Sub-unit × Amenities

Updated for NFHS-5 Koch Bihar district values.

| Sub_unit | LPG_clean_cooking_fuel | Improved_sanitation | Improved_drinking_water_source | Electricity | Tier |
|---|---|---|---|---|---|
| U1_Tufanganj_Municipality | 68.00 | 87.00 | 99.00 | 99.00 | B |
| U2_Tufanganj_II_CDB_and_rural | 22.00 | 73.00 | 99.00 | 98.00 | B |

### D.15 Vote × Religion (2021 AE anchor)

P(party ‖ religion) — anchored on 2021 AE result; BJP 54.7% total. Rajbanshi SC Hindu community delivered strong BJP vote.

| Religion | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Hindu | 62.00 | 31.00 | 2.00 | 2.00 | 3.00 | D | Rajbanshi-SC Hindu BJP swing; 2021 AE AC-level result anchors total at 54.7% BJP; Hindu ~84.2% of voters → estimated 62% BJP among Hindu |
| Muslim | 4.00 | 64.00 | 28.00 | 2.00 | 2.00 | D | INC consolidated Muslim vote in Tufanganj (Rabin Roy INC got 2.85% total = ~17% of Muslim vote); AITC dominant Muslim bloc |
| Christian | 30.00 | 50.00 | 10.00 | 6.00 | 4.00 | E | Approximation; small base |
| Sarna_ORP | 42.00 | 38.00 | 5.00 | 10.00 | 5.00 | E | Tribal North Bengal mixed; slight BJP gain |
| Other_residual | 52.00 | 28.00 | 10.00 | 5.00 | 5.00 | E | Trader/upper residual |

### D.16 Vote × Caste (2021 AE anchor)

| Caste | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| UC_bhadralok | 65.00 | 22.00 | 5.00 | 5.00 | 3.00 | D | BJP bhadralok consolidation 2021 stronger than 2019 |
| OBC | 48.00 | 36.00 | 6.00 | 7.00 | 3.00 | D | Mixed; slight BJP gain |
| SC_total | 63.00 | 30.00 | 3.00 | 2.00 | 2.00 | D | Rajbanshi SC dominant BJP bloc; 2021 result anchor — BJP 54.7% implies very strong SC support; Malati Rava Roy (BJP, SC reserved) enhanced community identification |
| ST_total | 44.00 | 36.00 | 4.00 | 12.00 | 4.00 | D | Stable tribal pattern; slight BJP gain |
| Other_Hindu_middle | 56.00 | 36.00 | 3.00 | 3.00 | 2.00 | D | BJP Hindu consolidation |
| Muslim | 4.00 | 64.00 | 28.00 | 2.00 | 2.00 | D | Same as D.15 Muslim row |

### D.17 Vote × Gender (2021 AE anchor)

P(party ‖ gender) — Lakshmir Bhandar launched Apr 2021 (after voting); CISF Sitalkuchi firing context.

| Gender | BJP | AITC | INC | LF | Other_NOTA | Tier | Source |
|---|---|---|---|---|---|---|---|
| Male | 57.00 | 37.00 | 2.00 | 2.50 | 1.50 | D | 2021 AE BJP male strong; BJP 54.7% total; male BJP-leaning pattern in Cooch Behar; ECI data anchor |
| Female | 52.00 | 43.00 | 3.00 | 1.50 | 0.50 | D | Female BJP vote high in Rajbanshi belt; Malati Rava Roy (female BJP candidate) may have boosted female BJP share; note Lakshmir Bhandar launched post-voting |

### D.18 Vote × Welfare

(Skipped — no `welfare_exposure` axis declared for AC 009. See NORMALIZED_SCHEMA.md §4.7.)

---

## E. 2021 baseline vote (calibration target)

**Locked schema: 4 columns, 5 rows summing to 100.0 ± 0.5.**

2021 WB Assembly Election result for AC 009 Tufanganj — tier A, ECI.

| Party | ac_segment_pct | tier | note |
|---|---|---|---|
| BJP | 54.69 | A | Malati Rava Roy 114,503 votes / 209,378 total valid; data/electoral_history/2021/detailed_results.csv |
| AITC | 39.79 | A | Pranab Kumar Dey 83,305 votes / 209,378 total valid |
| INC | 2.85 | A | Rabin Roy 5,973 votes / 209,378 total valid |
| LF | 0.00 | A | No LF candidate contested; LF collapsed |
| Other_NOTA | 2.67 | A | NOTA 2,069 + IND Sushil Das 1,461 + IND Barman 601 + IND Layek 552 + SUCI 491 + AMB 423 = 5,597 / 209,378 |
| **Sum** | **100.00** | — | self-check |

---

## F. Pre-2021 vote history (anchors for belief evolution, NOT calibration targets)

### AC 009 (Assembly Elections)

| Year | Winner | Party | Votes | % | Runner-up | Party | % | Margin |
|---|---|---|---|---|---|---|---|---|
| 2011 AE | Arghya Roy Pradhan | AITC | 73,721 | ~52% | Dhananjoy Rava | CPI(M) | ~48% (est) | ~6,182 |
| 2016 AE | Fazal Karim Miah | AITC | 85,052 | ~54% | Shyamal Choudhury | INC | ~44% | ~15,270 |

Notes:
- 2011: AITC held against Left stronghold; Rajbanshi SC community behind AITC.
- 2016: Fazal Karim Miah (AITC, Muslim candidate) won; INC as runner-up; Left collapsed; RSP-INC vote-transfer dynamics.
- Both 2011 and 2016 were AITC-held; BJP did not win or come close in either election.
- BJP was near-zero in both 2011 and 2016 AE in Tufanganj, making the 2019 LS surge (49.5% BJP) and 2021 AE win (54.7% BJP) a dramatic realignment, powered by Rajbanshi SC swing and Nisith Pramanik's organisational drive.

### 2019 LS Cooch Behar (PC 02) — AC 009 segment (prior anchor)

| Party | Votes | % | Notes |
|---|---|---|---|
| BJP | 98,776 | 49.50% | ECI 2019 LS AC-segment data |
| AITC | 91,290 | 45.75% | ECI 2019 LS |
| INC | 1,999 | 1.00% | |
| LF (RSP + SUCI) | 5,829 | 2.70% | RSP 5,392 + SUCI(C) 437 |
| Other_NOTA | 1,660 | 0.83% | IND |

Notes:
- 2019 LS: BJP won overall Cooch Behar LS seat (Nisith Pramanik); AC 009 gave BJP 49.5% — historic first BJP lead in this AC at any level.
- Rajbanshi SC mobilisation on citizenship/identity issues drove the swing from near-zero (2016 AE) to 49.5% (2019 LS).
- 2021 AE consolidated this swing further to 54.7% (BJP won by 31,198 votes / 14.9pp margin).

### LS Cooch Behar (PC 02) historical

| Year | Winner | Party | % | Notes |
|---|---|---|---|
| 2014 LS | Renuka Sinha | AITC | ~44% | Left second; BJP ~15%; Congress ~12% |
| 2019 LS | Nisith Pramanik | BJP | ~48% | First BJP win; AITC 44.4%; massive Rajbanshi SC swing |

---

## G. Sources & tier flags

### Primary sources (tier A — direct hard data)
- Census of India 2011 — Tufanganj II CD Block primary census abstract (religion, SC/ST, literacy, worker categories)
- Census of India 2011 — Tufanganj Municipality demographics (SC 23.03%, ST 0.41%, pop 20,998)
- Census of India 2011 — Cooch Behar district demographics
- Election Commission of India — `data/electoral_history/2021/detailed_results.csv` AC 009: BJP 114,503 · AITC 83,305 · INC 5,973 · NOTA 2,069 · IND/SUCI/AMB 3,528; electorate 234,311; total valid 209,378
- Election Commission of India — `data/2019_AssemblySegmentLevelVotingData.csv` AC 009: BJP 98,776 · AITC 91,290 · RSP 5,392 · INC 1,999; electorate 225,957
- Delimitation Commission of India 2008 — WB Schedule (AC 009 = Tufanganj Muni + Tufanganj II CDB + 4 GPs of Tufanganj I CDB)

### Secondary sources (tier B / C)
- NFHS-5 (2019-21) Koch Bihar district — household amenities (sanitation 75.7%, water 99.3%, LPG 25.7%, electricity 98.2%), sex ratio 1,058 F/1000M; `data/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv`
- NFHS-4 (2015-16) West Bengal — household asset ownership, media baseline; smartphone/TV/banking as 2019 anchors
- Pew Research India — religion-differential growth projections (Hindu ~1.0%/yr · Muslim ~1.3%/yr)
- CSDS-Lokniti 2021 WB NES — vote × demographic conditionals for 2021 AE (WB regional rollup)
- WB District Statistical Handbook — Cooch Behar
- PMJDY enrollment data — banking access baseline

### Tertiary / journalistic (tier D)
- The Print (2021): "Who are Rajbanshis" — Rajbanshi ~75% of SC in Cooch Behar belt; BJP appeal
- Scroll.in (2016): BJP Cooch Behar statehood demands; Rajbanshi mobilization history
- Wikipedia — Tufanganj Assembly constituency (2021 AE result confirmation)
- Wikipedia — Tufanganj I, Tufanganj II CD Blocks (Census 2011 data)
- news reports: COVID-19 reverse migration to North Bengal agricultural belt (2020); BSF 50km jurisdiction extension (Oct 2021); Bangladesh temple attacks (Oct 2021) and Cooch Behar Hindu border community anxiety

### Tier-D / E reliance flags (what to distrust)
- **Caste sub-group shares within Hindu** (D.2, C.2) — no caste census post-1931 for non-SC/ST; Rajbanshi % within SC estimated; tier C/E
- **Sub-unit population split** (C.11) — Muni + CDB-II full, but 4 GPs from Tufanganj-I estimated; refine with DCHB Part-A
- **Migration/birthplace** (C.16, D.3) — no public AC-level Census D-series; tier D from district pattern
- **Asset/media** (C.14, D.4, D.13) — NFHS-5 district-level amenities (tier B) but smartphone/mobile from NFHS state-level + trend extrapolation (tier C)
- **Vote × Demographic** (D.15–D.17) — 2021 AE total anchors calibration target (tier A); internal religion/caste/gender splits modeled (tier D) from CSDS 2021 WB regional rollup adjusted for Cooch Behar Rajbanshi pattern
- **Mother tongue / Rajbongshi split** (C.5, D.1) — no AC-level language census; Rajbongshi share estimated from SC proportion; tier C/E
- **Age distribution** (C.3) — district-level age pyramid; no AC-specific data; tier E

### v0 known gaps
1. DCHB Cooch Behar Part-A — collapsed sub-units to 2 instead of full GP-level disaggregation
2. Smartphone/internet household data — no AC-level NFHS-5 sub-district data; using district NFHS-5 for amenities + state-level NFHS-5 for smartphone trend
3. Census HH-13 GP-level — using NFHS district-level proxy for asset/media
4. Census D-series migration — using qualitative/journalistic anchor
5. CSDS-Lokniti 2021 WB AE full cross-tabs — using Cooch Behar-adjusted rollup for D.15-D.17

---

*v0 — generated 2026-04-28, frozen at end-2021 state-of-knowledge.
No post-2021 events referenced. COVID-19, Lakshmir Bhandar (Apr 2021), BSF 50km jurisdiction (Oct 2021), 2021 AE result may be referenced.*

---

## H. Post-2021 validation anchors

> **OUT-OF-SAMPLE simulation gates — NOT part of the frozen 2021 calibration.**
> Use these as validation targets for downstream simulator runs. The
> validator's leakage gate exempts §H from the no-future-leakage check.

### 2024 Lok Sabha Election — AC 009 segment within Cooch Behar LS (PC 02) (tier A)

| Party | Candidate (LS level) | Votes | AC segment % | Tier | Source |
|---|---|---|---|---|---|
| BJP | Nisith Pramanik | 104,302 | 48.86% | A | data/2024_AssemblySegmentLevelVotingData.csv |
| AITC | Jagadish Chandra Barma Basunia | 97,807 | 45.82% | A | Same |
| RSP | (candidate) | 4,316 | 2.02% | A | Same |
| Others + NOTA | various | 6,917 | 3.24% | A | Same (NOTA 2,128 + other parties) |
| **Electorate** | | 245,696 | — | A | Same |
| **Total valid** | | 213,470 | — | A | Computed |

Note: AITC won the overall Cooch Behar LS seat in 2024 (Jagadish Chandra Barma Basunia), but at the AC 009 segment level BJP retained a narrow lead (48.86% vs 45.82%) — a narrowing from the 2021 AE 14.9pp BJP margin to a ~3pp margin. The simulator running from the 2021 calibration must model the post-2021 period belief evolution.

### Calibration test

The simulator is considered validated on this seat if it reproduces 2024 LS AC segment shares within ±3pp of tier-A figures:
- BJP target: 48.9% ± 3pp
- AITC target: 45.8% ± 3pp
- LF+Others combined target: ~5.3% ± 3pp
