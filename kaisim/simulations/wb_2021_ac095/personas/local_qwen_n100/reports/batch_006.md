# Verifier report (n=70)

- composite chi-square: **807.07** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.53  · max joint cell |z|: 6.28  · aggregate vote max |z|: 2.11
- max axis gap: 25.33 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 10.0 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| asset_media | C | 3.53 | 13.71 | 17.9 | 1 |
| migration | E | 3.22 | 11.00 | 12.9 | 1 |
| occupation | E | 3.09 | 25.33 | 23.6 | 1 |
| caste | E | 3.07 | 5.14 | 16.1 | 1 |
| household_type | E | 2.92 | 11.43 | 13.3 | 1 |
| economic_status | E | 2.35 | 12.14 | 13.6 | 0 |
| gp_location | E | 2.20 | 13.07 | 9.6 | 0 |
| workforce_status | E | 2.09 | 11.43 | 16.6 | 0 |
| education | E | 2.00 | 8.29 | 11.5 | 0 |
| amenities | C | 1.92 | 9.29 | 10.8 | 0 |
| religion | E | 1.61 | 7.57 | 5.4 | 0 |
| age_cohort | E | 1.60 | 4.36 | 7.7 | 0 |
| marital_status | E | 1.45 | 6.57 | 4.6 | 0 |
| class_of_worker | E | 1.38 | 11.33 | 3.2 | 0 |
| gender | E | 0.98 | 5.83 | 1.9 | 0 |
| mother_tongue | E | 0.92 | 1.20 | 1.7 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| asset_media | Banking | 88.0 | 74.29 | -13.71 | -3.53 |
| migration | WB_other_district | 9.0 | 20.0 | +11.00 | +3.22 |
| occupation | Agricultural_labourer | 28.0 | 53.33 | +25.33 | +3.09 |
| caste | OBC_specific | 2.0 | 7.14 | +5.14 | +3.07 |
| household_type | Extended_multi_generation | 6.0 | 14.29 | +8.29 | +2.92 |
| economic_status | Lower_middle | 25.0 | 12.86 | -12.14 | -2.35 |
| caste | Other_SC | 1.3 | 4.29 | +2.99 | +2.21 |
| gp_location | U1_Muni | 54.5 | 41.43 | -13.07 | -2.20 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 6.28 | 61.33 | 108.7 | 3 |  |
| asset_given_religion | C | 4.54 | 95.00 | 26.9 | 1 |  |
| migration_given_religion | D | 4.23 | 65.00 | 35.1 | 2 |  |
| vote_given_caste | C | 4.07 | 65.00 | 64.0 | 3 |  |
| caste_given_religion | E | 3.03 | 100.00 | 15.1 | 1 |  |
| asset_given_gp | C | 2.63 | 17.93 | 27.2 | 1 |  |
| asset_given_occupation | C | 2.36 | 80.00 | 19.3 | 0 |  |
| caste_given_gp | E | 2.25 | 15.02 | 18.1 | 0 |  |
| vote_given_religion | C | 2.22 | 40.00 | 13.1 | 0 |  |
| amenity_given_gp | C | 2.02 | 15.73 | 13.6 | 0 |  |
| religion_given_gp | E | 1.94 | 13.55 | 8.8 | 0 |  |
| vote_given_welfare | C | 1.72 | 65.00 | 21.4 | 0 |  |
| vote_given_gender | C | 1.45 | 6.50 | 5.6 | 0 |  |
| lang_given_religion | E | 0.65 | 75.00 | 1.6 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 1.71
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 44.29 | -5.71 | -0.96 | True |
| AITC | 40.0 | 50.0 | +10.00 | +1.71 | True |
| Left_INC_combined | 8.0 | 2.86 | -5.14 | -1.59 | True |
| Other_NOTA | 2.0 | 2.86 | +0.86 | +0.51 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.11
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 44.29 | -3.71 | -0.62 | True |
| AITC | 44.0 | 50.0 | +6.00 | +1.01 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.11 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.20 | True |
