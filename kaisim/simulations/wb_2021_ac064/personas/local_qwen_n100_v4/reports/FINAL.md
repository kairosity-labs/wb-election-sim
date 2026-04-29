# Verifier report (n=100)

- composite chi-square: **479.6** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.23  · max joint cell |z|: 3.66  · aggregate vote max |z|: 1.06
- max axis gap: 11.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 5.1 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| amenities | C | 2.23 | 11.00 | 11.2 | 0 |
| workforce_status | E | 1.92 | 9.00 | 8.5 | 0 |
| migration | D | 1.60 | 3.00 | 5.4 | 0 |
| education | E | 1.60 | 6.00 | 7.8 | 0 |
| class_of_worker | E | 1.58 | 9.55 | 4.3 | 0 |
| occupation | E | 1.52 | 6.45 | 10.5 | 0 |
| economic_status | E | 1.49 | 6.00 | 5.7 | 0 |
| caste | E | 1.47 | 4.00 | 9.5 | 0 |
| household_composition | E | 1.47 | 4.00 | 2.6 | 0 |
| asset_media | C | 1.47 | 4.00 | 6.3 | 0 |
| mother_tongue | A | 1.36 | 2.50 | 4.6 | 0 |
| marital_status | E | 1.33 | 6.00 | 3.8 | 0 |
| gender | E | 1.30 | 6.50 | 3.4 | 0 |
| age_cohort | E | 1.11 | 2.48 | 3.4 | 0 |
| gp_location | D | 1.09 | 4.10 | 1.8 | 0 |
| religion | D | 0.95 | 1.00 | 1.6 | 0 |
| muslim_subcaste | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| amenities | LPG_clean_cooking_fuel | 42.0 | 31.0 | -11.00 | -2.23 |
| workforce_status | Student | 11.0 | 17.0 | +6.00 | +1.92 |
| workforce_status | Non_worker | 37.0 | 28.0 | -9.00 | -1.86 |
| amenities | Improved_sanitation | 62.0 | 53.0 | -9.00 | -1.85 |
| education | Secondary | 17.0 | 23.0 | +6.00 | +1.60 |
| amenities | Wood_biomass_fuel | 52.0 | 60.0 | +8.00 | +1.60 |
| migration | Bangladesh_origin | 2.5 | 0.0 | -2.50 | -1.60 |
| class_of_worker | Family_worker | 20.0 | 29.55 | +9.55 | +1.58 |
| education | Graduate | 7.0 | 11.0 | +4.00 | +1.57 |
| occupation | Manufacturing | 5.0 | 0.0 | -5.00 | -1.52 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| workforce_given_education | E | 3.66 | 47.73 | 29.5 | 1 |  |
| asset_given_gp | C | 2.94 | 26.46 | 30.7 | 1 |  |
| education_given_caste | E | 2.81 | 68.00 | 55.5 | 2 |  |
| caste_given_gp | A (SC/ST tier A); E (internal Hindu split) | 2.54 | 20.43 | 37.1 | 1 |  |
| vote_given_gender | C | 2.33 | 16.72 | 10.0 | 0 |  |
| amenities_given_gp | C | 2.29 | 23.85 | 18.4 | 0 |  |
| vote_given_caste | E | 2.24 | 65.00 | 34.3 | 0 |  |
| religion_given_gp | A | 1.81 | 19.03 | 8.3 | 0 |  |
| migration_given_religion | E | 1.54 | 80.00 | 8.4 | 0 |  |
| caste_given_religion | E | 1.49 | 100.00 | 8.4 | 0 |  |
| vote_given_religion | E | 1.46 | 45.00 | 6.4 | 0 |  |
| asset_given_occupation | D | 1.39 | 80.00 | 8.0 | 0 |  |
| lang_given_religion | E | 1.33 | 90.00 | 4.7 | 0 |  |
| asset_given_religion | E | 1.17 | 98.00 | 3.8 | 0 |  |
| education_given_age_gender | E | 0.00 | 16.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier None)  max |z| = 1.06
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 37.1 | 32.0 | -5.10 | -1.06 | True |
| AITC | 35.54 | 39.0 | +3.46 | +0.72 | True |
| INC | 18.01 | 20.0 | +1.99 | +0.52 | True |
| CPI | 5.87 | 7.0 | +1.13 | +0.48 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | JeSM | vote_values=['JeSM'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | SUCI | vote_values=['SUCI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BSP | vote_values=['BSP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BMUP | vote_values=['BMUP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |