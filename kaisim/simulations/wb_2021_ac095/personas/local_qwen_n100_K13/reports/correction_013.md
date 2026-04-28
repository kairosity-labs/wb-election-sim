# Verifier report (n=104)

- composite chi-square: **1908.91** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 9.01  · max joint cell |z|: 6.04  · aggregate vote max |z|: 5.08
- max axis gap: 28.31 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 24.42 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| migration | E | 9.01 | 28.31 | 160.3 | 4 |
| workforce_status | E | 5.31 | 23.85 | 50.6 | 2 |
| education | E | 4.67 | 15.27 | 46.6 | 2 |
| caste | E | 4.63 | 20.12 | 44.7 | 4 |
| amenities | C | 4.53 | 19.23 | 48.3 | 2 |
| asset_media | C | 4.36 | 17.12 | 32.3 | 2 |
| household_type | E | 4.03 | 11.35 | 22.8 | 2 |
| gender | E | 3.46 | 16.96 | 23.9 | 2 |
| class_of_worker | E | 2.82 | 16.33 | 12.9 | 1 |
| marital_status | E | 2.58 | 6.46 | 8.6 | 1 |
| economic_status | E | 2.40 | 9.73 | 8.1 | 0 |
| gp_location | E | 2.10 | 10.27 | 8.8 | 0 |
| occupation | E | 1.95 | 10.33 | 14.7 | 0 |
| age_cohort | E | 1.86 | 5.46 | 8.9 | 0 |
| mother_tongue | E | 1.12 | 1.20 | 2.5 | 0 |
| religion | E | 1.02 | 1.00 | 1.1 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| migration | Out_migrant | 0.5 | 6.73 | +6.23 | +9.01 |
| migration | Native | 64.0 | 92.31 | +28.31 | +6.01 |
| migration | Bangladesh | 23.0 | 0.0 | -23.00 | -5.57 |
| workforce_status | Main_worker | 30.0 | 53.85 | +23.85 | +5.31 |
| education | Graduate | 9.0 | 22.12 | +13.12 | +4.67 |
| caste | Other_Hindu_middle_castes | 26.85 | 6.73 | -20.12 | -4.63 |
| amenities | Improved_sanitation_latrine | 75.0 | 94.23 | +19.23 | +4.53 |
| asset_media | TV | 80.0 | 97.12 | +17.12 | +4.36 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| migration_given_religion | D | 6.04 | 65.00 | 78.6 | 2 |  |
| vote_given_gender | C | 5.74 | 50.00 | 63.4 | 2 |  |
| vote_given_caste | C | 5.33 | 64.00 | 79.1 | 3 |  |
| asset_given_gp | C | 5.31 | 33.28 | 60.4 | 3 |  |
| amenity_given_gp | C | 5.31 | 34.66 | 70.8 | 3 |  |
| vote_given_religion | C | 4.84 | 40.00 | 53.9 | 3 |  |
| caste_given_religion | E | 4.62 | 100.00 | 47.3 | 3 |  |
| vote_given_welfare | C | 3.94 | 45.00 | 56.5 | 3 |  |
| education_given_caste | E | 3.66 | 78.00 | 89.2 | 4 |  |
| asset_given_religion | C | 3.64 | 95.00 | 32.8 | 3 |  |
| asset_given_occupation | C | 3.52 | 85.00 | 33.2 | 2 |  |
| caste_given_gp | E | 3.36 | 19.34 | 39.4 | 2 |  |
| religion_given_gp | E | 2.28 | 12.65 | 15.4 | 0 |  |
| lang_given_religion | E | 1.00 | 75.00 | 3.0 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 5.08
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 32.69 | -17.31 | -3.53 | False |
| AITC | 40.0 | 64.42 | +24.42 | +5.08 | False |
| Left_INC_combined | 8.0 | 1.92 | -6.08 | -2.28 | True |
| Other_NOTA | 2.0 | 0.96 | -1.04 | -0.76 | True |

### vote_2019_LS_share (tier D)  max |z| = 4.20
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 32.69 | -15.31 | -3.12 | False |
| AITC | 44.0 | 64.42 | +20.42 | +4.20 | False |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.58 | False |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.46 | True |
