# Verifier report (n=96)

- composite chi-square: **1870.6** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 4.43  · max joint cell |z|: 31.64  · aggregate vote max |z|: 2.83
- max axis gap: 12.27 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 14.17 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| caste | E | 4.43 | 12.27 | 31.6 | 2 |
| education | E | 2.62 | 7.67 | 13.6 | 1 |
| amenities | C | 2.52 | 8.92 | 13.7 | 1 |
| migration | E | 2.46 | 12.04 | 13.1 | 0 |
| marital_status | E | 2.11 | 7.17 | 8.2 | 0 |
| economic_status | E | 2.05 | 6.79 | 5.9 | 0 |
| workforce_status | E | 1.83 | 8.54 | 6.2 | 0 |
| occupation | E | 1.73 | 8.45 | 9.2 | 0 |
| gender | E | 1.58 | 8.06 | 5.0 | 0 |
| asset_media | C | 1.50 | 5.62 | 7.1 | 0 |
| age_cohort | E | 1.43 | 4.61 | 9.9 | 0 |
| religion | E | 1.40 | 5.50 | 3.8 | 0 |
| household_type | E | 1.39 | 3.38 | 2.2 | 0 |
| gp_location | E | 1.09 | 5.54 | 2.4 | 0 |
| mother_tongue | E | 1.08 | 1.20 | 2.3 | 0 |
| class_of_worker | E | 0.44 | 3.00 | 0.3 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| caste | OBC_specific | 2.0 | 8.33 | +6.33 | +4.43 |
| caste | Other_Hindu_middle_castes | 26.85 | 14.58 | -12.27 | -2.71 |
| education | Graduate | 9.0 | 16.67 | +7.67 | +2.62 |
| amenities | Improved_drinking_water_source | 86.0 | 77.08 | -8.92 | -2.52 |
| migration | Native | 64.0 | 76.04 | +12.04 | +2.46 |
| marital_status | Widowed | 7.0 | 12.5 | +5.50 | +2.11 |
| economic_status | Middle | 12.0 | 5.21 | -6.79 | -2.05 |
| amenities | Improved_sanitation_latrine | 75.0 | 83.33 | +8.33 | +1.89 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_religion | E | 31.64 | 100.00 | 1034.1 | 3 |  |
| migration_given_religion | D | 5.45 | 35.00 | 59.8 | 4 |  |
| vote_given_religion | C | 4.36 | 95.00 | 46.5 | 2 |  |
| education_given_caste | E | 4.00 | 50.00 | 75.9 | 3 |  |
| amenity_given_gp | C | 3.64 | 22.00 | 31.6 | 2 |  |
| asset_given_gp | C | 3.50 | 24.36 | 31.5 | 2 |  |
| vote_given_caste | C | 2.88 | 65.00 | 41.1 | 1 |  |
| asset_given_occupation | C | 2.84 | 85.00 | 27.1 | 1 |  |
| religion_given_gp | E | 2.59 | 13.87 | 13.3 | 1 |  |
| caste_given_gp | E | 2.59 | 18.18 | 22.3 | 1 |  |
| vote_given_gender | C | 2.40 | 19.23 | 21.0 | 0 |  |
| asset_given_religion | C | 1.36 | 65.00 | 6.3 | 0 |  |
| vote_given_welfare | C | 1.29 | 52.00 | 11.6 | 0 |  |
| lang_given_religion | E | 0.79 | 25.00 | 2.9 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 2.83
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 40.62 | -9.38 | -1.84 | True |
| AITC | 40.0 | 54.17 | +14.17 | +2.83 | False |
| Left_INC_combined | 8.0 | 3.12 | -4.88 | -1.76 | True |
| Other_NOTA | 2.0 | 2.08 | +0.08 | +0.06 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.48
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 40.62 | -7.38 | -1.45 | True |
| AITC | 44.0 | 54.17 | +10.17 | +2.01 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.48 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.40 | True |
