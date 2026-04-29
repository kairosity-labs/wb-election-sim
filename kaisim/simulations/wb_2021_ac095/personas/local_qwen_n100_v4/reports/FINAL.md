# Verifier report (n=100)

- composite chi-square: **436.35** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.13  · max joint cell |z|: 3.74  · aggregate vote max |z|: 2.53
- max axis gap: 10.31 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 6.0 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| migration | E | 2.13 | 4.00 | 6.7 | 0 |
| education | E | 1.93 | 8.00 | 12.4 | 0 |
| religion | E | 1.78 | 7.00 | 6.6 | 0 |
| occupation | E | 1.68 | 10.31 | 10.5 | 0 |
| workforce_status | E | 1.47 | 4.00 | 2.6 | 0 |
| asset_media | C | 1.47 | 4.00 | 3.8 | 0 |
| age_cohort | E | 1.33 | 2.94 | 4.7 | 0 |
| marital_status | E | 1.18 | 3.00 | 2.9 | 0 |
| amenities | C | 1.17 | 3.00 | 2.1 | 0 |
| mother_tongue | E | 1.10 | 1.20 | 2.4 | 0 |
| caste | E | 0.99 | 4.50 | 3.4 | 0 |
| gender | E | 0.94 | 4.69 | 1.8 | 0 |
| household_type | E | 0.94 | 4.00 | 1.8 | 0 |
| gp_location | E | 0.70 | 3.50 | 1.0 | 0 |
| economic_status | E | 0.59 | 1.00 | 0.5 | 0 |
| class_of_worker | E | 0.48 | 3.85 | 0.4 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| migration | Out_migrant | 0.5 | 2.0 | +1.50 | +2.13 |
| education | Middle | 22.0 | 14.0 | -8.00 | -1.93 |
| education | Secondary | 18.0 | 25.0 | +7.00 | +1.82 |
| religion | Hindu | 81.0 | 88.0 | +7.00 | +1.78 |
| occupation | Cultivator | 18.0 | 7.69 | -10.31 | -1.68 |
| occupation | Services | 12.0 | 20.51 | +8.51 | +1.64 |
| religion | Muslim | 18.0 | 12.0 | -6.00 | -1.56 |
| workforce_status | Unemployed | 8.0 | 4.0 | -4.00 | -1.47 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 3.74 | 41.67 | 60.4 | 3 |  |
| religion_given_gp | E | 2.86 | 15.04 | 16.8 | 2 |  |
| asset_given_occupation | C | 2.75 | 85.00 | 19.9 | 1 |  |
| asset_given_gp | C | 2.66 | 17.71 | 18.5 | 1 |  |
| migration_given_religion | D | 2.55 | 65.00 | 11.3 | 1 |  |
| vote_given_caste | C | 2.36 | 65.00 | 27.7 | 0 |  |
| vote_given_religion | C | 2.15 | 40.00 | 11.4 | 0 |  |
| amenity_given_gp | C | 2.10 | 12.20 | 9.2 | 0 |  |
| vote_given_gender | C | 1.79 | 11.93 | 13.0 | 0 |  |
| caste_given_gp | E | 1.72 | 12.06 | 11.0 | 0 |  |
| vote_given_welfare | C | 1.70 | 52.00 | 16.3 | 0 |  |
| asset_given_religion | C | 1.46 | 95.00 | 4.7 | 0 |  |
| caste_given_religion | E | 0.84 | 100.00 | 2.1 | 0 |  |
| lang_given_religion | E | 0.79 | 75.00 | 2.3 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 1.11
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 49.0 | -1.00 | -0.20 | True |
| AITC | 40.0 | 43.0 | +3.00 | +0.61 | True |
| Left_INC_combined | 8.0 | 5.0 | -3.00 | -1.11 | True |
| Other_NOTA | 2.0 | 3.0 | +1.00 | +0.71 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.53
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 49.0 | +1.00 | +0.20 | True |
| AITC | 44.0 | 43.0 | -1.00 | -0.20 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.53 | False |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.43 | True |
