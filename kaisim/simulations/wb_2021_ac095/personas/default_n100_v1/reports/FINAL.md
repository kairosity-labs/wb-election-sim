# Verifier report (n=100)

- composite chi-square: **404.85** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 1.48  · max joint cell |z|: 3.2  · aggregate vote max |z|: 0.8
- max axis gap: 10.5 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 4.0 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| occupation | E | 1.48 | 10.50 | 6.8 | 0 |
| migration | E | 1.43 | 6.00 | 3.9 | 0 |
| asset_media | C | 1.38 | 4.00 | 3.6 | 0 |
| age_cohort | E | 1.13 | 3.77 | 3.4 | 0 |
| mother_tongue | E | 1.10 | 1.20 | 2.4 | 0 |
| religion | E | 1.02 | 4.00 | 2.7 | 0 |
| marital_status | E | 1.01 | 3.00 | 2.2 | 0 |
| caste | E | 0.99 | 3.50 | 3.0 | 0 |
| economic_status | E | 0.97 | 4.00 | 1.8 | 0 |
| education | E | 0.96 | 3.00 | 2.7 | 0 |
| gp_location | E | 0.90 | 4.50 | 1.6 | 0 |
| workforce_status | E | 0.84 | 3.00 | 1.4 | 0 |
| amenities | C | 0.60 | 3.00 | 1.4 | 0 |
| class_of_worker | E | 0.42 | 3.00 | 0.4 | 0 |
| gender | E | 0.34 | 1.69 | 0.2 | 0 |
| household_type | E | 0.00 | 0.00 | 0.0 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| occupation | Agricultural_labourer | 28.0 | 17.5 | -10.50 | -1.48 |
| migration | Bangladesh | 23.0 | 29.0 | +6.00 | +1.43 |
| asset_media | Radio | 5.0 | 8.0 | +3.00 | +1.38 |
| age_cohort | 18_22 | 12.77 | 9.0 | -3.77 | -1.13 |
| occupation | Household_industry | 4.0 | 7.5 | +3.50 | +1.13 |
| mother_tongue | Bengali | 98.8 | 100.0 | +1.20 | +1.10 |
| occupation | Construction | 6.0 | 10.0 | +4.00 | +1.07 |
| age_cohort | 43_47 | 9.93 | 13.0 | +3.07 | +1.03 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| amenity_given_gp | C | 3.20 | 17.00 | 27.0 | 2 |  |
| vote_given_gender | C | 3.00 | 20.25 | 29.9 | 2 |  |
| education_given_caste | E | 2.75 | 55.00 | 38.0 | 1 |  |
| vote_given_caste | C | 2.58 | 25.33 | 26.3 | 1 |  |
| asset_given_gp | C | 2.43 | 16.00 | 17.2 | 0 |  |
| asset_given_occupation | C | 2.12 | 45.00 | 22.9 | 0 |  |
| vote_given_religion | C | 1.97 | 40.00 | 8.0 | 0 |  |
| vote_given_welfare | C | 1.95 | 52.00 | 12.8 | 0 |  |
| religion_given_gp | E | 1.69 | 9.00 | 6.3 | 0 |  |
| caste_given_gp | E | 1.63 | 10.00 | 10.7 | 0 |  |
| asset_given_religion | C | 1.16 | 95.00 | 3.0 | 0 |  |
| migration_given_religion | D | 1.11 | 65.00 | 4.0 | 0 |  |
| lang_given_religion | E | 0.89 | 75.00 | 2.6 | 0 |  |
| caste_given_religion | E | 0.76 | 100.00 | 2.0 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 0.80
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 46.0 | -4.00 | -0.80 | True |
| AITC | 40.0 | 43.0 | +3.00 | +0.61 | True |
| Left_INC_combined | 8.0 | 8.0 | +0.00 | +0.00 | True |
| Other_NOTA | 2.0 | 1.0 | -1.00 | -0.71 | True |
