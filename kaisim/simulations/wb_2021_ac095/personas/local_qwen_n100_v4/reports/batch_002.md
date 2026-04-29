# Verifier report (n=24)

- composite chi-square: **1576.42** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.92  · max joint cell |z|: 31.64  · aggregate vote max |z|: 1.44
- max axis gap: 36.67 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 14.17 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| workforce_status | E | 3.92 | 36.67 | 23.6 | 2 |
| education | E | 3.45 | 20.17 | 18.7 | 1 |
| migration | E | 3.25 | 31.83 | 27.4 | 3 |
| asset_media | C | 3.22 | 21.33 | 25.8 | 2 |
| amenities | C | 1.98 | 14.00 | 6.9 | 0 |
| occupation | E | 1.93 | 18.00 | 9.8 | 0 |
| caste | E | 1.59 | 15.33 | 8.6 | 0 |
| religion | E | 1.56 | 5.50 | 3.0 | 0 |
| gender | E | 1.51 | 15.36 | 4.5 | 0 |
| household_type | E | 1.34 | 11.50 | 3.8 | 0 |
| age_cohort | E | 1.27 | 5.14 | 5.0 | 0 |
| marital_status | E | 1.24 | 11.33 | 3.4 | 0 |
| class_of_worker | E | 1.21 | 13.18 | 2.6 | 0 |
| economic_status | E | 0.86 | 4.17 | 1.2 | 0 |
| mother_tongue | E | 0.54 | 1.20 | 0.6 | 0 |
| gp_location | E | 0.03 | 0.33 | 0.0 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| workforce_status | Main_worker | 30.0 | 66.67 | +36.67 | +3.92 |
| education | Graduate | 9.0 | 29.17 | +20.17 | +3.45 |
| migration | Native | 64.0 | 95.83 | +31.83 | +3.25 |
| asset_media | Banking | 88.0 | 66.67 | -21.33 | -3.22 |
| migration | Bangladesh | 23.0 | 0.0 | -23.00 | -2.68 |
| workforce_status | Non_worker | 48.0 | 20.83 | -27.17 | -2.66 |
| asset_media | Radio | 5.0 | 16.67 | +11.67 | +2.62 |
| migration | Out_migrant | 0.5 | 4.17 | +3.67 | +2.55 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_religion | E | 31.64 | 100.00 | 1012.1 | 1 |  |
| vote_given_religion | C | 4.36 | 95.00 | 28.5 | 1 |  |
| asset_given_gp | C | 4.06 | 50.73 | 28.0 | 1 |  |
| asset_given_religion | C | 3.43 | 65.00 | 20.7 | 1 |  |
| education_given_caste | E | 3.39 | 92.00 | 50.1 | 2 |  |
| migration_given_religion | D | 3.20 | 35.00 | 22.2 | 2 |  |
| religion_given_gp | E | 2.43 | 16.00 | 9.7 | 0 |  |
| caste_given_gp | E | 2.14 | 31.73 | 13.2 | 0 |  |
| vote_given_gender | C | 2.12 | 25.50 | 12.2 | 0 |  |
| amenity_given_gp | C | 1.91 | 25.00 | 10.3 | 0 |  |
| asset_given_occupation | C | 1.80 | 85.00 | 10.3 | 0 |  |
| vote_given_caste | C | 1.69 | 64.00 | 12.3 | 0 |  |
| vote_given_welfare | C | 1.64 | 52.00 | 10.8 | 0 |  |
| lang_given_religion | E | 0.58 | 25.00 | 1.2 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 1.44
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 41.67 | -8.33 | -0.82 | True |
| AITC | 40.0 | 54.17 | +14.17 | +1.42 | True |
| Left_INC_combined | 8.0 | 0.0 | -8.00 | -1.44 | True |
| Other_NOTA | 2.0 | 4.17 | +2.17 | +0.76 | True |

### vote_2019_LS_share (tier D)  max |z| = 1.24
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 41.67 | -6.33 | -0.62 | True |
| AITC | 44.0 | 54.17 | +10.17 | +1.00 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -1.24 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -0.70 | True |
