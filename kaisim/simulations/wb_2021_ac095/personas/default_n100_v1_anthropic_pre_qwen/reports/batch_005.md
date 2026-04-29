# Verifier report (n=94)

- composite chi-square: **592.96** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.3  · max joint cell |z|: 4.0  · aggregate vote max |z|: 1.39
- max axis gap: 9.98 pp  · max joint cell gap: 85.0 pp  · aggregate max gap: 2.0 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| migration | E | 2.30 | 9.98 | 10.0 | 0 |
| caste | E | 1.56 | 5.77 | 8.3 | 0 |
| asset_media | C | 1.56 | 5.02 | 9.1 | 0 |
| workforce_status | E | 1.46 | 6.51 | 4.2 | 0 |
| occupation | E | 1.24 | 6.38 | 5.0 | 0 |
| amenities | C | 1.24 | 4.43 | 4.3 | 0 |
| education | E | 1.24 | 4.43 | 4.6 | 0 |
| age_cohort | E | 1.11 | 3.19 | 5.0 | 0 |
| economic_status | E | 1.10 | 2.89 | 2.2 | 0 |
| class_of_worker | E | 1.07 | 7.03 | 1.7 | 0 |
| religion | E | 1.05 | 4.17 | 2.1 | 0 |
| marital_status | E | 0.98 | 4.43 | 3.1 | 0 |
| gp_location | E | 0.88 | 4.50 | 1.5 | 0 |
| gender | E | 0.78 | 4.01 | 1.2 | 0 |
| household_type | E | 0.71 | 1.74 | 0.6 | 0 |
| mother_tongue | E | 0.53 | 0.36 | 0.7 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| migration | Bangladesh | 23.0 | 32.98 | +9.98 | +2.30 |
| caste | OBC_specific | 2.0 | 4.26 | +2.26 | +1.56 |
| asset_media | Radio | 5.0 | 8.51 | +3.51 | +1.56 |
| asset_media | Computer | 12.0 | 17.02 | +5.02 | +1.50 |
| workforce_status | Student | 6.0 | 9.57 | +3.57 | +1.46 |
| asset_media | Banking | 88.0 | 92.55 | +4.55 | +1.36 |
| caste | Bagdi | 1.5 | 3.19 | +1.69 | +1.35 |
| migration | Native | 64.0 | 57.45 | -6.55 | -1.32 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 4.00 | 80.00 | 65.8 | 3 |  |
| vote_given_gender | C | 3.47 | 23.69 | 36.2 | 2 |  |
| amenity_given_gp | C | 3.10 | 17.00 | 28.0 | 2 |  |
| asset_given_gp | C | 2.51 | 17.11 | 23.9 | 1 |  |
| migration_given_religion | D | 2.38 | 85.00 | 16.2 | 0 |  |
| vote_given_religion | C | 2.36 | 60.00 | 14.6 | 0 |  |
| vote_given_caste | C | 2.36 | 64.00 | 28.5 | 0 |  |
| vote_given_welfare | C | 2.35 | 65.00 | 30.1 | 0 |  |
| caste_given_gp | E | 2.28 | 14.60 | 20.0 | 0 |  |
| religion_given_gp | E | 2.20 | 11.74 | 9.9 | 0 |  |
| lang_given_religion | E | 2.17 | 82.50 | 10.1 | 0 |  |
| asset_given_occupation | C | 1.87 | 85.00 | 20.1 | 0 |  |
| asset_given_religion | C | 1.72 | 35.00 | 5.6 | 0 |  |
| caste_given_religion | E | 1.61 | 6.20 | 8.4 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 1.39
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 50.0 | +0.00 | +0.00 | True |
| AITC | 40.0 | 40.43 | +0.43 | +0.08 | True |
| Left_INC_combined | 8.0 | 6.38 | -1.62 | -0.58 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.39 | True |
