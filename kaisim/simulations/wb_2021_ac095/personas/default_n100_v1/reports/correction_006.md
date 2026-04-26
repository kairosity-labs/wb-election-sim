# Verifier report (n=100)

- composite chi-square: **619.36** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 1.9  · max joint cell |z|: 4.0  · aggregate vote max |z|: 1.43
- max axis gap: 8.0 pp  · max joint cell gap: 85.0 pp  · aggregate max gap: 2.0 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| migration | E | 1.90 | 8.00 | 7.0 | 0 |
| amenities | C | 1.44 | 5.00 | 5.5 | 0 |
| caste | E | 1.43 | 6.00 | 7.9 | 0 |
| asset_media | C | 1.38 | 4.00 | 7.5 | 0 |
| age_cohort | E | 1.33 | 3.51 | 6.1 | 0 |
| workforce_status | E | 1.26 | 6.00 | 3.4 | 0 |
| class_of_worker | E | 1.19 | 7.50 | 2.4 | 0 |
| marital_status | E | 1.18 | 3.00 | 2.8 | 0 |
| economic_status | E | 1.17 | 3.00 | 2.1 | 0 |
| religion | E | 1.04 | 4.00 | 2.1 | 0 |
| education | E | 0.96 | 4.00 | 3.7 | 0 |
| occupation | E | 0.93 | 5.50 | 2.7 | 0 |
| gp_location | E | 0.90 | 4.50 | 1.6 | 0 |
| household_type | E | 0.84 | 2.00 | 0.9 | 0 |
| gender | E | 0.74 | 3.69 | 1.1 | 0 |
| mother_tongue | E | 0.55 | 0.30 | 0.7 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| migration | Bangladesh | 23.0 | 31.0 | +8.00 | +1.90 |
| amenities | Improved_drinking_water_source | 86.0 | 91.0 | +5.00 | +1.44 |
| caste | OBC_specific | 2.0 | 4.0 | +2.00 | +1.43 |
| asset_media | Radio | 5.0 | 8.0 | +3.00 | +1.38 |
| age_cohort | 63_67 | 3.55 | 6.0 | +2.45 | +1.33 |
| age_cohort | 48_52 | 8.51 | 5.0 | -3.51 | -1.26 |
| workforce_status | Student | 6.0 | 9.0 | +3.00 | +1.26 |
| migration | Native | 64.0 | 58.0 | -6.00 | -1.25 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 4.00 | 80.00 | 64.4 | 2 |  |
| vote_given_gender | C | 3.71 | 24.64 | 40.9 | 3 |  |
| amenity_given_gp | C | 3.20 | 17.00 | 32.0 | 2 |  |
| asset_given_gp | C | 2.73 | 18.00 | 22.5 | 1 |  |
| vote_given_religion | C | 2.45 | 60.00 | 15.4 | 0 |  |
| vote_given_caste | C | 2.45 | 64.00 | 32.5 | 0 |  |
| caste_given_gp | E | 2.45 | 14.00 | 20.2 | 0 |  |
| vote_given_welfare | C | 2.44 | 65.00 | 31.9 | 0 |  |
| migration_given_religion | D | 2.38 | 85.00 | 14.3 | 0 |  |
| religion_given_gp | E | 2.31 | 12.00 | 11.1 | 0 |  |
| lang_given_religion | E | 2.17 | 82.50 | 10.3 | 0 |  |
| asset_given_occupation | C | 1.99 | 45.00 | 23.8 | 0 |  |
| asset_given_religion | C | 1.51 | 35.00 | 5.8 | 0 |  |
| caste_given_religion | E | 1.48 | 6.20 | 8.0 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 1.43
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 49.0 | -1.00 | -0.20 | True |
| AITC | 40.0 | 40.0 | +0.00 | +0.00 | True |
| Left_INC_combined | 8.0 | 8.0 | +0.00 | +0.00 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.43 | True |
