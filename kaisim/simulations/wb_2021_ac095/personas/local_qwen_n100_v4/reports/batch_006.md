# Verifier report (n=72)

- composite chi-square: **1762.15** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 4.68  · max joint cell |z|: 31.64  · aggregate vote max |z|: 2.14
- max axis gap: 17.94 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 7.22 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| caste | E | 4.68 | 8.79 | 26.8 | 1 |
| amenities | C | 4.05 | 16.56 | 23.5 | 1 |
| migration | E | 3.17 | 17.94 | 20.6 | 1 |
| workforce_status | E | 2.93 | 15.83 | 16.2 | 1 |
| education | E | 2.27 | 7.67 | 10.3 | 0 |
| occupation | E | 2.13 | 11.08 | 8.6 | 0 |
| asset_media | C | 1.84 | 8.06 | 10.1 | 0 |
| marital_status | E | 1.62 | 8.56 | 5.6 | 0 |
| age_cohort | E | 1.56 | 6.00 | 9.0 | 0 |
| economic_status | E | 1.49 | 5.06 | 5.5 | 0 |
| religion | E | 1.21 | 5.50 | 2.8 | 0 |
| mother_tongue | E | 0.94 | 1.20 | 1.7 | 0 |
| class_of_worker | E | 0.89 | 2.00 | 0.8 | 0 |
| gp_location | E | 0.77 | 4.50 | 1.2 | 0 |
| household_type | E | 0.63 | 3.17 | 0.7 | 0 |
| gender | E | 0.48 | 2.86 | 0.5 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| caste | OBC_specific | 2.0 | 9.72 | +7.72 | +4.68 |
| amenities | Improved_drinking_water_source | 86.0 | 69.44 | -16.56 | -4.05 |
| migration | Native | 64.0 | 81.94 | +17.94 | +3.17 |
| workforce_status | Main_worker | 30.0 | 45.83 | +15.83 | +2.93 |
| education | Graduate | 9.0 | 16.67 | +7.67 | +2.27 |
| occupation | Services | 12.0 | 23.08 | +11.08 | +2.13 |
| workforce_status | Unemployed | 8.0 | 1.39 | -6.61 | -2.07 |
| amenities | Other_fuel | 5.0 | 0.0 | -5.00 | -1.95 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_religion | E | 31.64 | 100.00 | 1028.8 | 2 |  |
| migration_given_religion | D | 6.40 | 35.00 | 72.5 | 3 |  |
| vote_given_religion | C | 4.36 | 95.00 | 31.7 | 1 |  |
| amenity_given_gp | C | 4.23 | 30.56 | 35.4 | 2 |  |
| education_given_caste | E | 4.09 | 43.54 | 59.2 | 2 |  |
| asset_given_gp | C | 3.01 | 23.89 | 21.9 | 2 |  |
| asset_given_occupation | C | 2.54 | 85.00 | 25.4 | 1 |  |
| vote_given_gender | C | 2.46 | 19.67 | 20.1 | 0 |  |
| religion_given_gp | E | 2.16 | 13.22 | 9.6 | 0 |  |
| caste_given_gp | E | 2.11 | 17.33 | 17.6 | 0 |  |
| vote_given_caste | C | 1.95 | 65.00 | 23.5 | 0 |  |
| asset_given_religion | C | 1.36 | 65.00 | 3.5 | 0 |  |
| vote_given_welfare | C | 1.17 | 52.00 | 10.4 | 0 |  |
| lang_given_religion | E | 0.69 | 25.00 | 2.3 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 1.25
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 47.22 | -2.78 | -0.47 | True |
| AITC | 40.0 | 47.22 | +7.22 | +1.25 | True |
| Left_INC_combined | 8.0 | 4.17 | -3.83 | -1.20 | True |
| Other_NOTA | 2.0 | 1.39 | -0.61 | -0.37 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.14
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 47.22 | -0.78 | -0.13 | True |
| AITC | 44.0 | 47.22 | +3.22 | +0.55 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.14 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.21 | True |
