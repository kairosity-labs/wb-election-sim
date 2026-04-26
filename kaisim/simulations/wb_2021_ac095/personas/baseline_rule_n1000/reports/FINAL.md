# Verifier report (n=1000)

- composite chi-square: **1606.46** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 9.67  · max joint cell |z|: 10.01  · aggregate vote max |z|: 4.24
- max axis gap: 9.9 pp  · max joint cell gap: 38.67 pp  · aggregate max gap: 6.7 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| workforce_status | E | 9.67 | 9.90 | 215.2 | 5 |
| marital_status | E | 5.53 | 8.40 | 67.4 | 3 |
| caste | E | 5.28 | 5.72 | 48.0 | 3 |
| migration | E | 2.65 | 2.50 | 25.6 | 1 |
| age_cohort | E | 2.52 | 2.46 | 16.1 | 1 |
| mother_tongue | E | 2.31 | 0.50 | 8.0 | 0 |
| asset_media | C | 2.04 | 2.10 | 8.9 | 0 |
| occupation | E | 1.88 | 3.21 | 8.1 | 0 |
| amenities | C | 1.74 | 1.60 | 5.2 | 0 |
| household_type | E | 1.73 | 1.30 | 3.4 | 0 |
| class_of_worker | E | 1.39 | 1.08 | 2.4 | 0 |
| religion | E | 1.21 | 1.50 | 3.0 | 0 |
| education | E | 1.20 | 1.60 | 4.5 | 0 |
| economic_status | E | 1.17 | 1.30 | 2.3 | 0 |
| gp_location | E | 1.14 | 1.80 | 2.6 | 0 |
| gender | E | 0.10 | 0.12 | 0.0 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| workforce_status | Marginal_worker | 8.0 | 16.3 | +8.30 | +9.67 |
| workforce_status | Main_worker | 30.0 | 20.1 | -9.90 | -6.83 |
| workforce_status | Student | 6.0 | 1.4 | -4.60 | -6.13 |
| marital_status | Currently_married | 64.0 | 72.4 | +8.40 | +5.53 |
| workforce_status | Non_worker | 48.0 | 56.6 | +8.60 | +5.44 |
| marital_status | Widowed | 7.0 | 2.7 | -4.30 | -5.33 |
| caste | Muslim | 13.58 | 19.3 | +5.72 | +5.28 |
| workforce_status | Unemployed | 8.0 | 5.6 | -2.40 | -2.80 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_gp | E | 10.01 | 11.36 | 216.9 | 6 |  |
| asset_given_gp | C | 4.73 | 10.56 | 94.5 | 5 |  |
| vote_given_caste | C | 4.65 | 16.95 | 80.3 | 2 |  |
| vote_given_religion | C | 4.14 | 18.33 | 49.9 | 3 |  |
| asset_given_occupation | C | 4.01 | 27.78 | 70.8 | 5 |  |
| caste_given_religion | E | 3.23 | 2.32 | 14.2 | 1 |  |
| asset_given_religion | C | 2.69 | 31.67 | 25.9 | 1 |  |
| vote_given_welfare | C | 2.58 | 38.67 | 45.3 | 1 |  |
| vote_given_gender | C | 2.54 | 5.74 | 26.2 | 1 |  |
| amenity_given_gp | C | 2.45 | 3.58 | 13.7 | 0 |  |
| migration_given_religion | D | 2.22 | 10.00 | 10.4 | 0 |  |
| education_given_caste | E | 1.85 | 12.48 | 39.1 | 0 |  |
| lang_given_religion | E | 1.33 | 16.67 | 7.7 | 0 |  |
| religion_given_gp | E | 1.15 | 1.83 | 3.5 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 4.24
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 43.3 | -6.70 | -4.24 | False |
| AITC | 40.0 | 43.4 | +3.40 | +2.19 | True |
| Left_INC_combined | 8.0 | 11.6 | +3.60 | +4.20 | False |
| Other_NOTA | 2.0 | 1.7 | -0.30 | -0.68 | True |
