# Verifier report (n=24)

- composite chi-square: **596.47** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.58  · max joint cell |z|: 4.9  · aggregate vote max |z|: 3.08
- max axis gap: 24.17 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 30.83 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| workforce_status | E | 2.58 | 24.17 | 14.5 | 1 |
| gender | E | 2.32 | 23.69 | 10.8 | 0 |
| caste | E | 2.22 | 18.52 | 12.7 | 0 |
| education | E | 2.11 | 17.83 | 13.7 | 0 |
| amenities | C | 1.98 | 16.67 | 9.7 | 0 |
| migration | E | 1.97 | 19.33 | 7.8 | 0 |
| occupation | E | 1.96 | 18.00 | 14.7 | 0 |
| asset_media | C | 1.96 | 15.83 | 13.4 | 0 |
| economic_status | E | 1.83 | 15.50 | 5.2 | 0 |
| household_type | E | 1.34 | 11.67 | 3.7 | 0 |
| marital_status | E | 1.24 | 11.33 | 3.4 | 0 |
| age_cohort | E | 1.10 | 6.74 | 5.8 | 0 |
| religion | E | 0.81 | 6.50 | 1.4 | 0 |
| mother_tongue | E | 0.54 | 1.20 | 0.6 | 0 |
| class_of_worker | E | 0.53 | 2.00 | 0.3 | 0 |
| gp_location | E | 0.44 | 4.50 | 0.4 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| workforce_status | Main_worker | 30.0 | 54.17 | +24.17 | +2.58 |
| gender | Male | 51.31 | 75.0 | +23.69 | +2.32 |
| gender | Female | 48.68 | 25.0 | -23.68 | -2.32 |
| workforce_status | Non_worker | 48.0 | 25.0 | -23.00 | -2.26 |
| caste | OBC_specific | 2.0 | 8.33 | +6.33 | +2.22 |
| education | Middle | 22.0 | 4.17 | -17.83 | -2.11 |
| caste | Other_Hindu_middle_castes | 26.85 | 8.33 | -18.52 | -2.05 |
| education | Graduate | 9.0 | 20.83 | +11.83 | +2.03 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 4.90 | 96.00 | 67.1 | 3 |  |
| vote_given_religion | C | 3.41 | 40.00 | 21.2 | 1 |  |
| vote_given_caste | C | 3.19 | 65.00 | 33.3 | 1 |  |
| vote_given_welfare | C | 2.66 | 65.00 | 23.3 | 1 |  |
| asset_given_religion | C | 2.57 | 95.00 | 13.7 | 1 |  |
| vote_given_gender | C | 2.45 | 50.00 | 16.2 | 0 |  |
| asset_given_gp | C | 2.34 | 28.00 | 16.1 | 0 |  |
| caste_given_religion | E | 2.21 | 100.00 | 12.8 | 0 |  |
| migration_given_religion | D | 2.05 | 65.00 | 9.5 | 0 |  |
| amenity_given_gp | C | 2.00 | 28.33 | 16.2 | 0 |  |
| asset_given_occupation | C | 1.93 | 90.00 | 13.3 | 0 |  |
| caste_given_gp | E | 1.81 | 25.67 | 9.6 | 0 |  |
| religion_given_gp | E | 0.80 | 8.67 | 1.7 | 0 |  |
| lang_given_religion | E | 0.40 | 75.00 | 0.6 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 3.08
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 29.17 | -20.83 | -2.04 | True |
| AITC | 40.0 | 70.83 | +30.83 | +3.08 | False |
| Left_INC_combined | 8.0 | 0.0 | -8.00 | -1.44 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -0.70 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.65
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 29.17 | -18.83 | -1.85 | True |
| AITC | 44.0 | 70.83 | +26.83 | +2.65 | False |
| CPI_INC | 6.0 | 0.0 | -6.00 | -1.24 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -0.70 | True |
