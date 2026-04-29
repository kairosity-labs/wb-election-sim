# Verifier report (n=100)

- composite chi-square: **1863.82** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 4.29  · max joint cell |z|: 31.64  · aggregate vote max |z|: 2.86
- max axis gap: 12.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 14.0 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| caste | E | 4.29 | 10.85 | 28.4 | 1 |
| migration | E | 2.50 | 12.00 | 18.2 | 0 |
| education | E | 2.45 | 7.00 | 13.1 | 0 |
| amenities | C | 2.31 | 8.00 | 11.4 | 0 |
| marital_status | E | 1.96 | 7.00 | 7.7 | 0 |
| economic_status | E | 1.85 | 6.00 | 4.9 | 0 |
| workforce_status | E | 1.75 | 8.00 | 6.5 | 0 |
| gender | E | 1.74 | 8.69 | 6.0 | 0 |
| household_type | E | 1.68 | 4.00 | 3.2 | 0 |
| occupation | E | 1.57 | 10.30 | 10.9 | 0 |
| age_cohort | E | 1.52 | 4.94 | 9.3 | 0 |
| asset_media | C | 1.38 | 5.00 | 6.8 | 0 |
| gp_location | E | 1.31 | 6.50 | 3.4 | 0 |
| religion | E | 1.30 | 5.00 | 3.3 | 0 |
| mother_tongue | E | 1.10 | 1.20 | 2.4 | 0 |
| class_of_worker | E | 0.70 | 4.60 | 0.9 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| caste | OBC_specific | 2.0 | 8.0 | +6.00 | +4.29 |
| migration | Native | 64.0 | 76.0 | +12.00 | +2.50 |
| caste | Other_Hindu_middle_castes | 26.85 | 16.0 | -10.85 | -2.45 |
| education | Graduate | 9.0 | 16.0 | +7.00 | +2.45 |
| amenities | Improved_drinking_water_source | 86.0 | 78.0 | -8.00 | -2.31 |
| migration | Out_migrant | 0.5 | 2.0 | +1.50 | +2.13 |
| marital_status | Widowed | 7.0 | 12.0 | +5.00 | +1.96 |
| economic_status | Middle | 12.0 | 6.0 | -6.00 | -1.85 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_religion | E | 31.64 | 100.00 | 1030.8 | 3 |  |
| migration_given_religion | D | 5.21 | 35.00 | 56.9 | 4 |  |
| vote_given_religion | C | 4.36 | 95.00 | 46.5 | 2 |  |
| education_given_caste | E | 4.00 | 50.00 | 73.7 | 3 |  |
| amenity_given_gp | C | 3.68 | 22.00 | 30.3 | 1 |  |
| asset_given_gp | C | 3.57 | 24.58 | 34.0 | 2 |  |
| asset_given_occupation | C | 3.11 | 85.00 | 29.4 | 1 |  |
| vote_given_caste | C | 2.75 | 65.00 | 40.2 | 1 |  |
| religion_given_gp | E | 2.63 | 13.92 | 13.8 | 1 |  |
| vote_given_gender | C | 2.21 | 17.50 | 19.4 | 0 |  |
| caste_given_gp | E | 2.20 | 14.77 | 18.6 | 0 |  |
| asset_given_religion | C | 1.52 | 65.00 | 7.4 | 0 |  |
| vote_given_welfare | C | 1.32 | 52.00 | 12.9 | 0 |  |
| lang_given_religion | E | 0.83 | 25.00 | 3.0 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 2.86
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 41.0 | -9.00 | -1.80 | True |
| AITC | 40.0 | 54.0 | +14.00 | +2.86 | False |
| Left_INC_combined | 8.0 | 3.0 | -5.00 | -1.84 | True |
| Other_NOTA | 2.0 | 2.0 | +0.00 | +0.00 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.53
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 41.0 | -7.00 | -1.40 | True |
| AITC | 44.0 | 54.0 | +10.00 | +2.01 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.53 | False |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.43 | True |
