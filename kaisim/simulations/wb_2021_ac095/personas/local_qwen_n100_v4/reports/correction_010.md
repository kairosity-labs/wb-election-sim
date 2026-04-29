# Verifier report (n=112)

- composite chi-square: **1823.97** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.89  · max joint cell |z|: 31.64  · aggregate vote max |z|: 2.67
- max axis gap: 12.53 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 8.21 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| caste | E | 3.89 | 7.21 | 22.7 | 1 |
| occupation | E | 2.81 | 12.53 | 16.8 | 1 |
| education | E | 2.20 | 8.61 | 18.3 | 0 |
| migration | E | 2.19 | 8.71 | 12.7 | 0 |
| amenities | C | 2.18 | 8.93 | 10.8 | 0 |
| asset_media | C | 2.14 | 9.64 | 10.4 | 0 |
| age_cohort | E | 1.78 | 5.62 | 9.2 | 0 |
| religion | E | 1.76 | 6.50 | 6.2 | 0 |
| marital_status | E | 1.76 | 7.46 | 7.7 | 0 |
| workforce_status | E | 1.73 | 7.50 | 7.1 | 0 |
| household_type | E | 1.31 | 2.93 | 2.1 | 0 |
| mother_tongue | E | 1.17 | 1.20 | 2.7 | 0 |
| economic_status | E | 1.09 | 4.46 | 2.3 | 0 |
| gp_location | E | 0.96 | 4.50 | 1.8 | 0 |
| gender | E | 0.86 | 4.05 | 1.5 | 0 |
| class_of_worker | E | 0.69 | 4.72 | 0.5 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| caste | OBC_specific | 2.0 | 7.14 | +5.14 | +3.89 |
| occupation | Services | 12.0 | 24.53 | +12.53 | +2.81 |
| education | Middle | 22.0 | 13.39 | -8.61 | -2.20 |
| migration | Bangladesh | 23.0 | 14.29 | -8.71 | -2.19 |
| amenities | Improved_sanitation_latrine | 75.0 | 83.93 | +8.93 | +2.18 |
| asset_media | TwoWheeler | 35.0 | 44.64 | +9.64 | +2.14 |
| education | Higher_Secondary | 11.0 | 16.96 | +5.96 | +2.02 |
| education | Graduate | 9.0 | 14.29 | +5.29 | +1.95 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_religion | E | 31.64 | 100.00 | 1023.4 | 2 |  |
| migration_given_religion | D | 5.21 | 35.00 | 55.5 | 3 |  |
| vote_given_religion | C | 4.36 | 95.00 | 37.8 | 2 |  |
| amenity_given_gp | C | 3.97 | 22.00 | 35.6 | 1 |  |
| education_given_caste | E | 3.91 | 41.67 | 72.8 | 3 |  |
| asset_given_gp | C | 3.53 | 22.50 | 32.7 | 2 |  |
| asset_given_occupation | C | 3.11 | 85.00 | 28.8 | 1 |  |
| religion_given_gp | E | 2.90 | 14.21 | 16.5 | 2 |  |
| caste_given_gp | E | 2.37 | 14.36 | 19.1 | 0 |  |
| vote_given_caste | C | 2.36 | 65.00 | 42.6 | 0 |  |
| vote_given_gender | C | 1.81 | 7.84 | 14.2 | 0 |  |
| asset_given_religion | C | 1.52 | 65.00 | 8.0 | 0 |  |
| vote_given_welfare | C | 1.47 | 52.00 | 13.8 | 0 |  |
| lang_given_religion | E | 0.83 | 25.00 | 3.2 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 1.77
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 45.54 | -4.46 | -0.94 | True |
| AITC | 40.0 | 48.21 | +8.21 | +1.77 | True |
| Left_INC_combined | 8.0 | 4.46 | -3.54 | -1.38 | True |
| Other_NOTA | 2.0 | 1.79 | -0.21 | -0.16 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.67
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 45.54 | -2.46 | -0.52 | True |
| AITC | 44.0 | 48.21 | +4.21 | +0.90 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.67 | False |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.51 | True |
