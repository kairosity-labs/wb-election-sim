# Verifier report (n=118)

- composite chi-square: **1910.6** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 4.37  · max joint cell |z|: 31.64  · aggregate vote max |z|: 2.74
- max axis gap: 11.64 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 9.15 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| caste | E | 4.37 | 7.36 | 26.6 | 1 |
| occupation | E | 2.66 | 11.64 | 17.6 | 1 |
| amenities | C | 2.23 | 8.90 | 10.2 | 0 |
| education | E | 2.05 | 6.05 | 16.3 | 0 |
| migration | E | 2.00 | 7.75 | 11.5 | 0 |
| asset_media | C | 1.87 | 8.22 | 9.7 | 0 |
| workforce_status | E | 1.73 | 7.29 | 8.1 | 0 |
| age_cohort | E | 1.63 | 4.89 | 6.8 | 0 |
| religion | E | 1.51 | 5.44 | 4.5 | 0 |
| marital_status | E | 1.35 | 5.12 | 5.0 | 0 |
| mother_tongue | E | 1.20 | 1.20 | 2.9 | 0 |
| household_type | E | 1.13 | 2.47 | 1.5 | 0 |
| gender | E | 1.00 | 4.62 | 2.0 | 0 |
| gp_location | E | 0.98 | 4.50 | 1.9 | 0 |
| economic_status | E | 0.83 | 2.97 | 1.4 | 0 |
| class_of_worker | E | 0.40 | 2.73 | 0.2 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| caste | OBC_specific | 2.0 | 7.63 | +5.63 | +4.37 |
| occupation | Services | 12.0 | 23.64 | +11.64 | +2.66 |
| amenities | Improved_sanitation_latrine | 75.0 | 83.9 | +8.90 | +2.23 |
| education | Graduate | 9.0 | 14.41 | +5.41 | +2.05 |
| migration | Bangladesh | 23.0 | 15.25 | -7.75 | -2.00 |
| asset_media | TwoWheeler | 35.0 | 43.22 | +8.22 | +1.87 |
| migration | Out_migrant | 0.5 | 1.69 | +1.19 | +1.84 |
| caste | Other_Hindu_middle_castes | 26.85 | 19.49 | -7.36 | -1.80 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_religion | E | 31.64 | 100.00 | 1028.0 | 2 |  |
| migration_given_religion | D | 7.40 | 35.00 | 88.5 | 3 |  |
| vote_given_religion | C | 4.36 | 95.00 | 39.7 | 2 |  |
| amenity_given_gp | C | 4.08 | 22.00 | 36.1 | 1 |  |
| education_given_caste | E | 3.73 | 41.67 | 75.9 | 3 |  |
| asset_given_gp | C | 3.45 | 21.44 | 34.1 | 2 |  |
| asset_given_occupation | C | 3.28 | 85.00 | 30.4 | 1 |  |
| religion_given_gp | E | 3.00 | 14.31 | 18.0 | 2 |  |
| vote_given_caste | C | 2.61 | 65.00 | 47.7 | 1 |  |
| caste_given_gp | E | 2.53 | 11.54 | 18.9 | 1 |  |
| asset_given_religion | C | 1.87 | 65.00 | 9.0 | 0 |  |
| vote_given_gender | C | 1.86 | 7.55 | 15.2 | 0 |  |
| vote_given_welfare | C | 1.49 | 52.00 | 17.1 | 0 |  |
| lang_given_religion | E | 0.89 | 25.00 | 3.4 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 2.03
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 44.92 | -5.08 | -1.10 | True |
| AITC | 40.0 | 49.15 | +9.15 | +2.03 | True |
| Left_INC_combined | 8.0 | 4.24 | -3.76 | -1.51 | True |
| Other_NOTA | 2.0 | 1.69 | -0.31 | -0.24 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.74
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 44.92 | -3.08 | -0.67 | True |
| AITC | 44.0 | 49.15 | +5.15 | +1.13 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.74 | False |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.55 | True |
