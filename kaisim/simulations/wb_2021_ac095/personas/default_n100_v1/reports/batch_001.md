# Verifier report (n=18)

- composite chi-square: **325.74** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.4  · max joint cell |z|: 3.02  · aggregate vote max |z|: 1.25
- max axis gap: 25.56 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 10.0 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| occupation | E | 2.40 | 14.18 | 8.8 | 0 |
| workforce_status | E | 2.37 | 25.56 | 8.8 | 0 |
| asset_media | C | 2.27 | 12.78 | 13.3 | 0 |
| migration | E | 2.16 | 21.44 | 7.2 | 0 |
| age_cohort | E | 1.74 | 12.29 | 7.7 | 0 |
| amenities | C | 1.71 | 16.11 | 9.1 | 0 |
| marital_status | E | 1.71 | 19.33 | 5.7 | 0 |
| class_of_worker | E | 1.68 | 20.00 | 6.4 | 0 |
| caste | E | 1.51 | 15.74 | 6.6 | 0 |
| gp_location | E | 1.33 | 15.61 | 3.5 | 0 |
| gender | E | 1.30 | 15.36 | 3.4 | 0 |
| education | E | 1.03 | 8.44 | 2.8 | 0 |
| economic_status | E | 0.82 | 8.33 | 1.9 | 0 |
| mother_tongue | E | 0.47 | 1.20 | 0.4 | 0 |
| religion | E | 0.43 | 2.33 | 0.3 | 0 |
| household_type | E | 0.38 | 3.78 | 0.2 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| occupation | Government_services_teachers | 4.0 | 18.18 | +14.18 | +2.40 |
| workforce_status | Main_worker | 30.0 | 55.56 | +25.56 | +2.37 |
| asset_media | Radio | 5.0 | 16.67 | +11.67 | +2.27 |
| migration | Bangladesh | 23.0 | 44.44 | +21.44 | +2.16 |
| age_cohort | 43_47 | 9.93 | 22.22 | +12.29 | +1.74 |
| workforce_status | Non_worker | 48.0 | 27.78 | -20.22 | -1.72 |
| marital_status | Currently_married | 64.0 | 83.33 | +19.33 | +1.71 |
| amenities | Improved_drinking_water_source | 86.0 | 100.0 | +14.00 | +1.71 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 3.02 | 82.00 | 32.8 | 1 |  |
| asset_given_gp | C | 2.24 | 35.14 | 13.9 | 0 |  |
| caste_given_gp | E | 2.20 | 28.86 | 15.7 | 0 |  |
| migration_given_religion | D | 1.97 | 65.00 | 7.0 | 0 |  |
| amenity_given_gp | C | 1.91 | 25.00 | 11.1 | 0 |  |
| vote_given_gender | C | 1.63 | 33.33 | 8.2 | 0 |  |
| vote_given_welfare | C | 1.57 | 65.00 | 14.5 | 0 |  |
| caste_given_religion | E | 1.51 | 100.00 | 6.5 | 0 |  |
| vote_given_caste | C | 1.36 | 65.00 | 9.5 | 0 |  |
| asset_given_religion | C | 1.36 | 95.00 | 3.6 | 0 |  |
| asset_given_occupation | C | 1.15 | 92.00 | 8.0 | 0 |  |
| vote_given_religion | C | 1.13 | 40.00 | 4.6 | 0 |  |
| lang_given_religion | E | 0.40 | 75.00 | 0.5 | 0 |  |
| religion_given_gp | E | 0.33 | 3.62 | 0.4 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 1.25
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 50.0 | +0.00 | +0.00 | True |
| AITC | 40.0 | 50.0 | +10.00 | +0.87 | True |
| Left_INC_combined | 8.0 | 0.0 | -8.00 | -1.25 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -0.61 | True |
