# Verifier report (n=100)

- composite chi-square: **904.95** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 4.96  · max joint cell |z|: 3.76  · aggregate vote max |z|: 2.53
- max axis gap: 19.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 10.0 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| migration | E | 4.96 | 19.00 | 57.8 | 3 |
| education | E | 3.84 | 11.00 | 26.7 | 1 |
| workforce_status | E | 3.06 | 14.00 | 17.6 | 1 |
| household_type | E | 2.95 | 7.00 | 10.5 | 1 |
| caste | E | 2.86 | 7.85 | 16.6 | 1 |
| gender | E | 2.74 | 13.69 | 15.0 | 2 |
| amenities | C | 2.59 | 9.00 | 20.9 | 1 |
| class_of_worker | E | 2.39 | 15.50 | 9.9 | 0 |
| asset_media | C | 2.10 | 10.00 | 9.3 | 0 |
| age_cohort | E | 1.70 | 5.07 | 6.9 | 0 |
| marital_status | E | 1.57 | 4.00 | 4.3 | 0 |
| gp_location | E | 1.51 | 7.50 | 4.5 | 0 |
| occupation | E | 1.47 | 9.50 | 9.9 | 0 |
| economic_status | E | 1.21 | 5.00 | 2.1 | 0 |
| mother_tongue | E | 1.10 | 1.20 | 2.4 | 0 |
| religion | E | 1.02 | 4.00 | 2.7 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| migration | Out_migrant | 0.5 | 4.0 | +3.50 | +4.96 |
| migration | Native | 64.0 | 83.0 | +19.00 | +3.96 |
| education | Graduate | 9.0 | 20.0 | +11.00 | +3.84 |
| migration | Bangladesh | 23.0 | 10.0 | -13.00 | -3.09 |
| workforce_status | Main_worker | 30.0 | 44.0 | +14.00 | +3.06 |
| household_type | Extended_multi_generation | 6.0 | 13.0 | +7.00 | +2.95 |
| caste | OBC_specific | 2.0 | 6.0 | +4.00 | +2.86 |
| gender | Male | 51.31 | 65.0 | +13.69 | +2.74 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| migration_given_religion | D | 3.76 | 65.00 | 33.2 | 2 |  |
| education_given_caste | E | 3.39 | 78.00 | 82.9 | 4 |  |
| vote_given_caste | C | 3.25 | 64.00 | 43.6 | 3 |  |
| asset_given_gp | C | 3.23 | 22.23 | 32.0 | 2 |  |
| vote_given_welfare | C | 3.12 | 38.75 | 39.7 | 2 |  |
| amenity_given_gp | C | 2.94 | 17.74 | 32.7 | 2 |  |
| caste_given_religion | E | 2.93 | 100.00 | 16.4 | 1 |  |
| asset_given_occupation | C | 2.65 | 85.00 | 24.7 | 2 |  |
| vote_given_gender | C | 2.54 | 21.43 | 18.3 | 1 |  |
| vote_given_religion | C | 2.54 | 40.00 | 20.3 | 1 |  |
| asset_given_religion | C | 2.39 | 95.00 | 15.0 | 0 |  |
| religion_given_gp | E | 2.33 | 12.74 | 11.9 | 0 |  |
| caste_given_gp | E | 1.76 | 12.47 | 13.1 | 0 |  |
| lang_given_religion | E | 0.89 | 75.00 | 2.6 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 2.04
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 46.0 | -4.00 | -0.80 | True |
| AITC | 40.0 | 50.0 | +10.00 | +2.04 | True |
| Left_INC_combined | 8.0 | 3.0 | -5.00 | -1.84 | True |
| Other_NOTA | 2.0 | 1.0 | -1.00 | -0.71 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.53
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 46.0 | -2.00 | -0.40 | True |
| AITC | 44.0 | 50.0 | +6.00 | +1.21 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.53 | False |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.43 | True |
