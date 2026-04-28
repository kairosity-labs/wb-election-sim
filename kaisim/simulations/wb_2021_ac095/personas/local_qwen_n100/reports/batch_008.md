# Verifier report (n=82)

- composite chi-square: **791.08** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.77  · max joint cell |z|: 6.28  · aggregate vote max |z|: 2.29
- max axis gap: 16.44 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 8.78 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| asset_media | C | 2.77 | 9.95 | 15.1 | 1 |
| caste | E | 2.65 | 4.90 | 13.8 | 1 |
| education | E | 2.55 | 9.12 | 14.8 | 1 |
| migration | E | 2.55 | 8.37 | 10.8 | 1 |
| workforce_status | E | 2.51 | 12.68 | 18.8 | 1 |
| household_type | E | 2.36 | 6.20 | 6.7 | 0 |
| occupation | E | 2.20 | 16.44 | 13.5 | 0 |
| religion | E | 2.13 | 9.24 | 9.2 | 0 |
| amenities | C | 2.08 | 6.71 | 9.1 | 0 |
| age_cohort | E | 1.74 | 3.80 | 7.7 | 0 |
| gp_location | E | 1.71 | 9.38 | 5.8 | 0 |
| economic_status | E | 1.64 | 5.90 | 4.7 | 0 |
| class_of_worker | E | 1.58 | 10.56 | 3.7 | 0 |
| gender | E | 1.53 | 8.45 | 4.7 | 0 |
| marital_status | E | 1.41 | 3.98 | 3.1 | 0 |
| mother_tongue | E | 1.00 | 1.20 | 2.0 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| asset_media | Banking | 88.0 | 78.05 | -9.95 | -2.77 |
| caste | OBC_specific | 2.0 | 6.1 | +4.10 | +2.65 |
| education | Graduate | 9.0 | 17.07 | +8.07 | +2.55 |
| migration | WB_other_district | 9.0 | 17.07 | +8.07 | +2.55 |
| workforce_status | Main_worker | 30.0 | 42.68 | +12.68 | +2.51 |
| education | Illiterate | 14.0 | 4.88 | -9.12 | -2.38 |
| household_type | Extended_multi_generation | 6.0 | 12.2 | +6.20 | +2.36 |
| workforce_status | Marginal_worker | 8.0 | 1.22 | -6.78 | -2.26 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 6.28 | 61.33 | 121.1 | 3 |  |
| vote_given_caste | C | 3.91 | 40.00 | 60.1 | 3 |  |
| asset_given_religion | C | 3.66 | 95.00 | 20.4 | 1 |  |
| migration_given_religion | D | 3.46 | 65.00 | 32.6 | 3 |  |
| asset_given_gp | C | 2.74 | 21.49 | 28.0 | 2 |  |
| caste_given_religion | E | 2.56 | 100.00 | 12.4 | 1 |  |
| amenity_given_gp | C | 2.44 | 16.59 | 14.8 | 0 |  |
| caste_given_gp | E | 2.39 | 19.08 | 20.0 | 0 |  |
| asset_given_occupation | C | 2.36 | 80.00 | 21.7 | 0 |  |
| vote_given_religion | C | 2.32 | 40.00 | 14.0 | 0 |  |
| religion_given_gp | E | 2.32 | 14.30 | 12.8 | 0 |  |
| vote_given_welfare | C | 1.95 | 65.00 | 26.3 | 0 |  |
| vote_given_gender | C | 1.61 | 7.58 | 7.3 | 0 |  |
| lang_given_religion | E | 0.67 | 75.00 | 1.7 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 1.86
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 46.34 | -3.66 | -0.66 | True |
| AITC | 40.0 | 48.78 | +8.78 | +1.62 | True |
| Left_INC_combined | 8.0 | 2.44 | -5.56 | -1.86 | True |
| Other_NOTA | 2.0 | 2.44 | +0.44 | +0.28 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.29
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 46.34 | -1.66 | -0.30 | True |
| AITC | 44.0 | 48.78 | +4.78 | +0.87 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.29 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.29 | True |
