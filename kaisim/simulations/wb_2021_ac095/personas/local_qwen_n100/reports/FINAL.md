# Verifier report (n=100)

- composite chi-square: **594.1** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.52  · max joint cell |z|: 3.58  · aggregate vote max |z|: 2.53
- max axis gap: 13.71 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 6.0 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| asset_media | C | 2.52 | 12.00 | 14.1 | 1 |
| amenities | C | 2.29 | 8.00 | 14.5 | 0 |
| occupation | E | 2.23 | 13.24 | 16.2 | 0 |
| caste | E | 2.14 | 3.00 | 7.8 | 0 |
| class_of_worker | E | 1.98 | 13.71 | 5.3 | 0 |
| education | E | 1.90 | 8.00 | 7.4 | 0 |
| household_type | E | 1.68 | 4.00 | 3.2 | 0 |
| marital_status | E | 1.57 | 5.00 | 4.9 | 0 |
| religion | E | 1.53 | 6.00 | 5.0 | 0 |
| workforce_status | E | 1.53 | 7.00 | 4.2 | 0 |
| age_cohort | E | 1.43 | 4.77 | 9.0 | 0 |
| gender | E | 1.34 | 6.69 | 3.6 | 0 |
| economic_status | E | 1.21 | 5.00 | 3.8 | 0 |
| gp_location | E | 1.10 | 5.50 | 2.4 | 0 |
| mother_tongue | E | 1.10 | 1.20 | 2.4 | 0 |
| migration | E | 1.04 | 5.00 | 3.5 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| asset_media | TwoWheeler | 35.0 | 47.0 | +12.00 | +2.52 |
| amenities | Other_fuel | 5.0 | 10.0 | +5.00 | +2.29 |
| occupation | Cultivator | 18.0 | 4.76 | -13.24 | -2.23 |
| caste | OBC_specific | 2.0 | 5.0 | +3.00 | +2.14 |
| class_of_worker | Employee | 28.0 | 14.29 | -13.71 | -1.98 |
| education | Primary | 23.0 | 15.0 | -8.00 | -1.90 |
| amenities | Improved_sanitation_latrine | 75.0 | 83.0 | +8.00 | +1.85 |
| occupation | Agricultural_labourer | 28.0 | 40.48 | +12.48 | +1.80 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 3.58 | 51.67 | 77.1 | 4 |  |
| asset_given_gp | C | 3.19 | 21.27 | 24.5 | 1 |  |
| amenity_given_gp | C | 2.80 | 19.51 | 21.8 | 2 |  |
| religion_given_gp | E | 2.79 | 14.96 | 16.2 | 2 |  |
| asset_given_religion | C | 2.64 | 95.00 | 18.1 | 1 |  |
| vote_given_caste | C | 2.58 | 28.89 | 28.8 | 1 |  |
| migration_given_religion | D | 2.43 | 65.00 | 12.8 | 0 |  |
| asset_given_occupation | C | 2.36 | 80.00 | 18.2 | 0 |  |
| caste_given_religion | E | 2.14 | 100.00 | 6.9 | 0 |  |
| vote_given_religion | C | 2.14 | 40.00 | 8.4 | 0 |  |
| vote_given_welfare | C | 2.11 | 65.00 | 26.9 | 0 |  |
| vote_given_gender | C | 1.75 | 8.17 | 10.0 | 0 |  |
| caste_given_gp | E | 1.64 | 7.37 | 7.7 | 0 |  |
| lang_given_religion | E | 0.83 | 75.00 | 2.4 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 0.82
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 49.0 | -1.00 | -0.20 | True |
| AITC | 40.0 | 44.0 | +4.00 | +0.82 | True |
| Left_INC_combined | 8.0 | 6.0 | -2.00 | -0.74 | True |
| Other_NOTA | 2.0 | 1.0 | -1.00 | -0.71 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.53
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 49.0 | +1.00 | +0.20 | True |
| AITC | 44.0 | 44.0 | +0.00 | +0.00 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.53 | False |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.43 | True |
