# Verifier report (n=109)

- composite chi-square: **1653.94** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 8.77  · max joint cell |z|: 5.49  · aggregate vote max |z|: 4.58
- max axis gap: 24.99 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 21.47 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| migration | E | 8.77 | 24.99 | 142.0 | 4 |
| workforce_status | E | 4.87 | 21.38 | 42.7 | 2 |
| education | E | 4.41 | 12.10 | 38.0 | 2 |
| household_type | E | 4.22 | 11.28 | 24.6 | 2 |
| caste | E | 3.73 | 15.84 | 33.4 | 3 |
| gender | E | 3.65 | 17.50 | 26.7 | 2 |
| amenities | C | 3.59 | 14.91 | 34.5 | 2 |
| asset_media | C | 3.30 | 12.66 | 24.0 | 2 |
| class_of_worker | E | 2.82 | 16.33 | 12.9 | 1 |
| marital_status | E | 2.77 | 6.76 | 9.8 | 1 |
| gp_location | E | 2.58 | 12.30 | 13.3 | 2 |
| economic_status | E | 2.09 | 8.28 | 5.9 | 0 |
| age_cohort | E | 1.98 | 5.67 | 9.5 | 0 |
| occupation | E | 1.95 | 10.33 | 14.7 | 0 |
| mother_tongue | E | 1.15 | 1.20 | 2.6 | 0 |
| religion | E | 1.05 | 1.57 | 1.3 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| migration | Out_migrant | 0.5 | 6.42 | +5.92 | +8.77 |
| migration | Native | 64.0 | 88.99 | +24.99 | +5.44 |
| workforce_status | Main_worker | 30.0 | 51.38 | +21.38 | +4.87 |
| migration | Bangladesh | 23.0 | 3.67 | -19.33 | -4.80 |
| education | Graduate | 9.0 | 21.1 | +12.10 | +4.41 |
| household_type | Extended_multi_generation | 6.0 | 15.6 | +9.60 | +4.22 |
| caste | Other_Hindu_middle_castes | 26.85 | 11.01 | -15.84 | -3.73 |
| gender | Male | 51.31 | 68.81 | +17.50 | +3.65 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| vote_given_gender | C | 5.49 | 47.06 | 58.1 | 2 |  |
| vote_given_caste | C | 5.33 | 64.00 | 79.1 | 3 |  |
| migration_given_religion | D | 5.29 | 65.00 | 64.3 | 2 |  |
| amenity_given_gp | C | 4.39 | 27.54 | 53.5 | 3 |  |
| vote_given_religion | C | 4.34 | 40.00 | 46.6 | 3 |  |
| asset_given_gp | C | 4.24 | 26.30 | 52.2 | 3 |  |
| vote_given_welfare | C | 3.94 | 45.00 | 50.8 | 3 |  |
| caste_given_religion | E | 3.71 | 100.00 | 34.7 | 3 |  |
| education_given_caste | E | 3.66 | 78.00 | 83.9 | 3 |  |
| asset_given_occupation | C | 3.52 | 85.00 | 33.2 | 2 |  |
| asset_given_religion | C | 2.94 | 95.00 | 27.4 | 2 |  |
| caste_given_gp | E | 2.35 | 16.26 | 28.6 | 0 |  |
| religion_given_gp | E | 2.28 | 12.65 | 13.4 | 0 |  |
| lang_given_religion | E | 1.00 | 75.00 | 3.1 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 4.58
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 35.78 | -14.22 | -2.97 | False |
| AITC | 40.0 | 61.47 | +21.47 | +4.58 | False |
| Left_INC_combined | 8.0 | 1.83 | -6.17 | -2.37 | True |
| Other_NOTA | 2.0 | 0.92 | -1.08 | -0.81 | True |

### vote_2019_LS_share (tier D)  max |z| = 3.67
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 35.78 | -12.22 | -2.55 | False |
| AITC | 44.0 | 61.47 | +17.47 | +3.67 | False |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.64 | False |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.49 | True |
