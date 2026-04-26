# Verifier report (n=74)

- composite chi-square: **504.95** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.48  · max joint cell |z|: 3.46  · aggregate vote max |z|: 1.23
- max axis gap: 12.14 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 3.24 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| migration | E | 2.48 | 12.14 | 11.0 | 0 |
| marital_status | E | 2.00 | 10.43 | 8.0 | 0 |
| workforce_status | E | 1.98 | 10.54 | 5.9 | 0 |
| economic_status | E | 1.89 | 9.08 | 9.2 | 0 |
| age_cohort | E | 1.81 | 6.29 | 6.8 | 0 |
| caste | E | 1.81 | 4.36 | 8.8 | 0 |
| asset_media | C | 1.68 | 7.97 | 10.0 | 0 |
| amenities | C | 1.33 | 7.70 | 5.0 | 0 |
| gp_location | E | 1.24 | 7.20 | 3.1 | 0 |
| occupation | E | 1.21 | 8.00 | 5.8 | 0 |
| mother_tongue | E | 0.95 | 1.20 | 1.8 | 0 |
| household_type | E | 0.88 | 4.38 | 1.3 | 0 |
| religion | E | 0.86 | 2.78 | 1.3 | 0 |
| class_of_worker | E | 0.85 | 5.71 | 1.2 | 0 |
| education | E | 0.79 | 3.19 | 1.8 | 0 |
| gender | E | 0.47 | 2.74 | 0.4 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| migration | Bangladesh | 23.0 | 35.14 | +12.14 | +2.48 |
| marital_status | Never_married | 28.0 | 17.57 | -10.43 | -2.00 |
| workforce_status | Main_worker | 30.0 | 40.54 | +10.54 | +1.98 |
| economic_status | BPL_household | 22.0 | 31.08 | +9.08 | +1.89 |
| caste | Bagdi | 1.5 | 4.05 | +2.55 | +1.81 |
| age_cohort | 43_47 | 9.93 | 16.22 | +6.29 | +1.81 |
| economic_status | Lower_middle | 25.0 | 16.22 | -8.78 | -1.75 |
| asset_media | FourWheeler | 8.0 | 2.7 | -5.30 | -1.68 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 3.46 | 80.00 | 55.5 | 3 |  |
| amenity_given_gp | C | 2.83 | 17.00 | 19.5 | 1 |  |
| vote_given_gender | C | 2.70 | 21.00 | 24.3 | 1 |  |
| asset_given_gp | C | 2.57 | 19.18 | 17.4 | 1 |  |
| vote_given_caste | C | 2.31 | 64.00 | 27.0 | 0 |  |
| vote_given_religion | C | 2.27 | 40.00 | 11.3 | 0 |  |
| migration_given_religion | D | 2.05 | 65.00 | 8.7 | 0 |  |
| asset_given_occupation | C | 2.02 | 85.00 | 20.6 | 0 |  |
| caste_given_gp | E | 2.00 | 15.14 | 18.6 | 0 |  |
| vote_given_welfare | C | 1.97 | 65.00 | 25.8 | 0 |  |
| caste_given_religion | E | 1.80 | 100.00 | 7.6 | 0 |  |
| religion_given_gp | E | 1.78 | 11.29 | 7.6 | 0 |  |
| asset_given_religion | C | 1.33 | 95.00 | 3.9 | 0 |  |
| lang_given_religion | E | 0.79 | 75.00 | 2.0 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 1.23
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 47.3 | -2.70 | -0.46 | True |
| AITC | 40.0 | 43.24 | +3.24 | +0.57 | True |
| Left_INC_combined | 8.0 | 5.41 | -2.59 | -0.82 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.23 | True |
