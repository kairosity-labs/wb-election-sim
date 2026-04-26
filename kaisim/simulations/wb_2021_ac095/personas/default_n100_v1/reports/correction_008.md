# Verifier report (n=124)

- composite chi-square: **753.21** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 1.81  · max joint cell |z|: 4.59  · aggregate vote max |z|: 0.64
- max axis gap: 7.45 pp  · max joint cell gap: 85.0 pp  · aggregate max gap: 2.42 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| migration | E | 1.81 | 6.84 | 6.6 | 0 |
| workforce_status | E | 1.72 | 3.68 | 3.6 | 0 |
| amenities | C | 1.66 | 6.45 | 3.9 | 0 |
| caste | E | 1.58 | 3.21 | 7.0 | 0 |
| education | E | 1.54 | 4.32 | 6.5 | 0 |
| religion | E | 1.50 | 5.29 | 4.5 | 0 |
| asset_media | C | 1.35 | 4.68 | 8.5 | 0 |
| marital_status | E | 1.12 | 1.87 | 2.0 | 0 |
| occupation | E | 1.12 | 5.02 | 3.0 | 0 |
| age_cohort | E | 1.11 | 2.97 | 3.5 | 0 |
| class_of_worker | E | 1.10 | 7.45 | 3.2 | 0 |
| gp_location | E | 0.83 | 3.69 | 1.4 | 0 |
| economic_status | E | 0.81 | 3.00 | 1.0 | 0 |
| mother_tongue | E | 0.61 | 0.39 | 0.8 | 0 |
| gender | E | 0.61 | 2.72 | 0.7 | 0 |
| household_type | E | 0.54 | 1.16 | 0.4 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| migration | Bangladesh | 23.0 | 29.84 | +6.84 | +1.81 |
| workforce_status | Student | 6.0 | 9.68 | +3.68 | +1.72 |
| amenities | Improved_sanitation_latrine | 75.0 | 68.55 | -6.45 | -1.66 |
| caste | Bagdi | 1.5 | 3.23 | +1.73 | +1.58 |
| education | Higher_Secondary | 11.0 | 15.32 | +4.32 | +1.54 |
| religion | Hindu | 81.0 | 86.29 | +5.29 | +1.50 |
| religion | Muslim | 18.0 | 12.9 | -5.10 | -1.48 |
| asset_media | Banking | 88.0 | 91.94 | +3.94 | +1.35 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| vote_given_gender | C | 4.59 | 27.57 | 67.0 | 4 |  |
| education_given_caste | E | 3.59 | 72.00 | 71.5 | 3 |  |
| amenity_given_gp | C | 3.53 | 18.93 | 42.3 | 3 |  |
| asset_given_gp | C | 3.16 | 18.89 | 29.4 | 2 |  |
| vote_given_caste | C | 2.98 | 64.00 | 46.8 | 2 |  |
| religion_given_gp | E | 2.78 | 12.83 | 15.5 | 2 |  |
| vote_given_religion | C | 2.62 | 60.00 | 15.9 | 1 |  |
| caste_given_gp | E | 2.61 | 11.40 | 16.8 | 1 |  |
| vote_given_welfare | C | 2.56 | 65.00 | 36.5 | 1 |  |
| migration_given_religion | D | 2.38 | 85.00 | 11.8 | 0 |  |
| lang_given_religion | E | 2.17 | 82.50 | 10.7 | 0 |  |
| asset_given_occupation | C | 2.07 | 45.00 | 24.8 | 0 |  |
| asset_given_religion | C | 1.78 | 35.00 | 9.1 | 0 |  |
| caste_given_religion | E | 1.51 | 4.14 | 6.9 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 0.64
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 47.58 | -2.42 | -0.54 | True |
| AITC | 40.0 | 41.94 | +1.94 | +0.44 | True |
| Left_INC_combined | 8.0 | 6.45 | -1.55 | -0.64 | True |
| Other_NOTA | 2.0 | 1.61 | -0.39 | -0.31 | True |
