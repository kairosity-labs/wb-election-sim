# Verifier report (n=56)

- composite chi-square: **460.45** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.17  · max joint cell |z|: 3.36  · aggregate vote max |z|: 1.07
- max axis gap: 12.86 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 3.57 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| asset_media | C | 2.17 | 9.43 | 11.7 | 0 |
| workforce_status | E | 2.10 | 12.86 | 8.0 | 0 |
| migration | E | 1.94 | 10.93 | 7.2 | 0 |
| amenities | C | 1.54 | 8.93 | 3.1 | 0 |
| occupation | E | 1.54 | 10.86 | 9.7 | 0 |
| education | E | 1.48 | 6.93 | 7.3 | 0 |
| gender | E | 1.41 | 9.40 | 4.0 | 0 |
| caste | E | 1.28 | 5.57 | 6.3 | 0 |
| class_of_worker | E | 1.13 | 10.71 | 2.3 | 0 |
| age_cohort | E | 1.09 | 4.36 | 3.9 | 0 |
| economic_status | E | 0.93 | 5.36 | 2.2 | 0 |
| marital_status | E | 0.88 | 5.64 | 2.0 | 0 |
| mother_tongue | E | 0.82 | 1.20 | 1.4 | 0 |
| religion | E | 0.75 | 2.93 | 1.0 | 0 |
| household_type | E | 0.49 | 2.79 | 0.4 | 0 |
| gp_location | E | 0.40 | 2.64 | 0.3 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| asset_media | Computer | 12.0 | 21.43 | +9.43 | +2.17 |
| workforce_status | Main_worker | 30.0 | 42.86 | +12.86 | +2.10 |
| asset_media | Radio | 5.0 | 10.71 | +5.71 | +1.96 |
| migration | Bangladesh | 23.0 | 33.93 | +10.93 | +1.94 |
| workforce_status | Non_worker | 48.0 | 35.71 | -12.29 | -1.84 |
| occupation | Services | 12.0 | 21.43 | +9.43 | +1.54 |
| amenities | Improved_sanitation_latrine | 75.0 | 66.07 | -8.93 | -1.54 |
| occupation | Cultivator | 18.0 | 7.14 | -10.86 | -1.50 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| amenity_given_gp | C | 3.36 | 34.17 | 26.0 | 1 |  |
| education_given_caste | E | 3.27 | 80.00 | 57.0 | 2 |  |
| vote_given_gender | C | 2.56 | 27.27 | 24.5 | 1 |  |
| asset_given_gp | C | 2.12 | 19.50 | 15.7 | 0 |  |
| vote_given_welfare | C | 1.97 | 65.00 | 21.7 | 0 |  |
| vote_given_religion | C | 1.96 | 40.00 | 8.6 | 0 |  |
| vote_given_caste | C | 1.96 | 64.00 | 21.0 | 0 |  |
| asset_given_occupation | C | 1.87 | 85.00 | 17.8 | 0 |  |
| caste_given_gp | E | 1.80 | 15.67 | 15.6 | 0 |  |
| religion_given_gp | E | 1.62 | 10.75 | 7.2 | 0 |  |
| migration_given_religion | D | 1.56 | 65.00 | 5.4 | 0 |  |
| caste_given_religion | E | 1.27 | 100.00 | 5.5 | 0 |  |
| asset_given_religion | C | 1.18 | 95.00 | 3.0 | 0 |  |
| lang_given_religion | E | 0.69 | 75.00 | 1.5 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 1.07
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 46.43 | -3.57 | -0.53 | True |
| AITC | 40.0 | 42.86 | +2.86 | +0.44 | True |
| Left_INC_combined | 8.0 | 5.36 | -2.64 | -0.73 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.07 | True |
