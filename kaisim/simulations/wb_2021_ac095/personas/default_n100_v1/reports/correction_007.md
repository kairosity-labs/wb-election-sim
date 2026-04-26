# Verifier report (n=114)

- composite chi-square: **696.51** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.27  · max joint cell |z|: 4.24  · aggregate vote max |z|: 0.56
- max axis gap: 9.21 pp  · max joint cell gap: 85.0 pp  · aggregate max gap: 2.63 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| amenities | C | 2.27 | 9.21 | 9.2 | 0 |
| gp_location | E | 1.72 | 8.01 | 5.9 | 0 |
| economic_status | E | 1.34 | 5.19 | 3.9 | 0 |
| caste | E | 1.33 | 6.16 | 7.5 | 0 |
| class_of_worker | E | 1.30 | 8.14 | 2.8 | 0 |
| age_cohort | E | 1.28 | 3.99 | 4.9 | 0 |
| asset_media | C | 1.25 | 5.26 | 8.2 | 0 |
| religion | E | 1.11 | 4.09 | 2.5 | 0 |
| marital_status | E | 1.11 | 2.65 | 2.5 | 0 |
| migration | E | 1.07 | 4.19 | 3.6 | 0 |
| occupation | E | 1.01 | 4.74 | 3.1 | 0 |
| education | E | 0.94 | 3.70 | 3.0 | 0 |
| workforce_status | E | 0.85 | 1.89 | 0.8 | 0 |
| gender | E | 0.66 | 3.08 | 0.9 | 0 |
| mother_tongue | E | 0.59 | 0.32 | 0.7 | 0 |
| household_type | E | 0.36 | 1.44 | 0.3 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| amenities | Improved_sanitation_latrine | 75.0 | 65.79 | -9.21 | -2.27 |
| gp_location | U1_Muni | 54.5 | 46.49 | -8.01 | -1.72 |
| gp_location | U2_CDB_rural | 45.5 | 53.51 | +8.01 | +1.72 |
| economic_status | BPL_household | 22.0 | 27.19 | +5.19 | +1.34 |
| caste | SC_total (rollup) | 43.0 | 36.84 | -6.16 | -1.33 |
| economic_status | Upper_middle_well_off | 3.0 | 0.88 | -2.12 | -1.33 |
| amenities | LPG | 50.0 | 43.86 | -6.14 | -1.31 |
| class_of_worker | Family_worker | 20.0 | 27.91 | +7.91 | +1.30 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| vote_given_gender | C | 4.24 | 26.48 | 53.9 | 4 |  |
| amenity_given_gp | C | 3.53 | 18.93 | 38.2 | 3 |  |
| education_given_caste | E | 3.35 | 72.00 | 64.9 | 3 |  |
| asset_given_gp | C | 3.16 | 18.89 | 30.2 | 1 |  |
| caste_given_gp | E | 3.00 | 15.36 | 24.1 | 1 |  |
| vote_given_religion | C | 2.62 | 60.00 | 15.5 | 1 |  |
| vote_given_caste | C | 2.62 | 64.00 | 41.6 | 1 |  |
| religion_given_gp | E | 2.43 | 12.23 | 12.0 | 0 |  |
| migration_given_religion | D | 2.38 | 85.00 | 10.5 | 0 |  |
| vote_given_welfare | C | 2.32 | 65.00 | 31.6 | 0 |  |
| lang_given_religion | E | 2.17 | 82.50 | 10.6 | 0 |  |
| asset_given_occupation | C | 1.97 | 45.00 | 23.5 | 0 |  |
| asset_given_religion | C | 1.53 | 35.00 | 7.6 | 0 |  |
| caste_given_religion | E | 1.22 | 5.99 | 7.6 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 0.56
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 47.37 | -2.63 | -0.56 | True |
| AITC | 40.0 | 41.23 | +1.23 | +0.27 | True |
| Left_INC_combined | 8.0 | 7.02 | -0.98 | -0.39 | True |
| Other_NOTA | 2.0 | 1.75 | -0.25 | -0.19 | True |
