# Verifier report (n=100)

- composite chi-square: **1132.7** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 5.46  · max joint cell |z|: 5.97  · aggregate vote max |z|: 1.83
- max axis gap: 25.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 9.14 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| workforce_status | E | 5.46 | 25.00 | 52.1 | 3 |
| education | E | 5.04 | 11.50 | 38.9 | 2 |
| occupation | E | 3.74 | 15.42 | 43.5 | 1 |
| household_composition | E | 3.49 | 10.00 | 14.6 | 1 |
| amenities | C | 3.04 | 15.00 | 28.3 | 3 |
| marital_status | E | 2.95 | 8.00 | 11.7 | 1 |
| migration | D | 2.53 | 6.50 | 19.0 | 1 |
| economic_status | E | 2.45 | 11.00 | 11.4 | 0 |
| class_of_worker | E | 2.23 | 14.13 | 8.8 | 0 |
| age_cohort | E | 2.12 | 4.95 | 14.0 | 0 |
| caste | E | 2.11 | 6.57 | 9.1 | 0 |
| gender | E | 1.99 | 9.94 | 7.9 | 0 |
| asset_media | C | 1.84 | 8.00 | 14.6 | 0 |
| religion | B | 1.40 | 6.89 | 4.0 | 0 |
| gp_location | E | 0.90 | 3.60 | 1.3 | 0 |
| mother_tongue | E | 0.75 | 0.56 | 1.1 | 0 |
| abhishek_loyalty | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| workforce_status | Main_worker | 30.0 | 55.0 | +25.00 | +5.46 |
| education | Graduate | 5.5 | 17.0 | +11.50 | +5.04 |
| occupation | Fishing_pisciculture | 12.0 | 27.42 | +15.42 | +3.74 |
| household_composition | Extended_multi_generation | 9.0 | 19.0 | +10.00 | +3.49 |
| workforce_status | Non_worker | 38.0 | 22.0 | -16.00 | -3.30 |
| amenities | LPG_clean_cooking_fuel | 42.0 | 27.0 | -15.00 | -3.04 |
| marital_status | Widowed | 8.0 | 16.0 | +8.00 | +2.95 |
| education | Illiterate | 20.5 | 9.0 | -11.50 | -2.85 |
| amenities | Wood_biomass_fuel | 50.0 | 63.0 | +13.00 | +2.60 |
| workforce_status | Unemployed | 8.0 | 1.0 | -7.00 | -2.58 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| workforce_given_education | E | 5.97 | 65.00 | 62.7 | 2 |  |
| amenities_given_gp | C | 4.51 | 33.35 | 71.5 | 4 |  |
| migration_given_religion | E | 4.48 | 80.00 | 42.2 | 1 |  |
| education_given_caste | E | 3.68 | 54.00 | 77.3 | 5 |  |
| asset_given_gp | C | 3.37 | 40.00 | 39.7 | 2 |  |
| caste_given_gp | B/A | 3.31 | 23.31 | 52.8 | 3 |  |
| vote_given_gender | C | 3.25 | 25.62 | 23.4 | 2 |  |
| asset_given_occupation | D | 3.13 | 88.00 | 38.5 | 2 |  |
| religion_given_gp | A | 2.89 | 21.63 | 29.6 | 2 |  |
| vote_given_religion | — | 2.77 | 45.00 | 21.6 | 1 |  |
| vote_given_caste | C | 2.77 | 18.00 | 25.9 | 1 |  |
| asset_given_religion | E | 2.46 | 95.00 | 8.8 | 0 |  |
| caste_given_religion | E | 1.76 | 100.00 | 6.5 | 0 |  |
| lang_given_religion | E | 0.73 | 92.00 | 1.5 | 0 |  |
| education_given_age_gender | E | 0.00 | 13.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate; fishing hazard; higher widow share) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.83
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 52.86 | 62.0 | +9.14 | +1.83 | True |
| BJP | 35.69 | 32.0 | -3.69 | -0.77 | True |
| CPI | 8.19 | 5.0 | -3.19 | -1.16 | True |
| INC | 0.99 | 1.0 | +0.01 | +0.01 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | Others | vote_values=['Other'] not present in sampled population (field=vote_2019_LS) |