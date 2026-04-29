# Verifier report (n=48)

- composite chi-square: **1831.06** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 6.36  · max joint cell |z|: 31.64  · aggregate vote max |z|: 1.75
- max axis gap: 31.83 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 6.0 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| amenities | C | 6.36 | 31.83 | 55.1 | 1 |
| caste | E | 3.22 | 20.60 | 24.1 | 2 |
| education | E | 2.86 | 11.83 | 10.0 | 1 |
| gp_location | E | 2.66 | 19.08 | 14.1 | 2 |
| asset_media | C | 2.60 | 18.75 | 17.3 | 1 |
| economic_status | E | 2.24 | 13.42 | 8.3 | 0 |
| migration | E | 2.18 | 13.08 | 12.6 | 0 |
| gender | E | 2.13 | 15.36 | 9.1 | 0 |
| workforce_status | E | 2.08 | 13.75 | 8.8 | 0 |
| age_cohort | E | 1.89 | 9.31 | 8.6 | 0 |
| household_type | E | 1.53 | 9.42 | 3.9 | 0 |
| marital_status | E | 1.49 | 7.17 | 4.1 | 0 |
| occupation | E | 1.15 | 8.09 | 5.1 | 0 |
| class_of_worker | E | 0.83 | 6.96 | 1.6 | 0 |
| mother_tongue | E | 0.76 | 1.20 | 1.2 | 0 |
| religion | E | 0.75 | 3.42 | 1.1 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| amenities | Improved_drinking_water_source | 86.0 | 54.17 | -31.83 | -6.36 |
| caste | Other_Hindu_middle_castes | 26.85 | 6.25 | -20.60 | -3.22 |
| education | Graduate | 9.0 | 20.83 | +11.83 | +2.86 |
| caste | Namasudra_Matua | 39.5 | 58.33 | +18.83 | +2.67 |
| gp_location | U1_Muni | 54.5 | 35.42 | -19.08 | -2.66 |
| gp_location | U2_CDB_rural | 45.5 | 64.58 | +19.08 | +2.66 |
| asset_media | Smartphone | 50.0 | 31.25 | -18.75 | -2.60 |
| caste | SC_total (rollup) | 43.0 | 60.42 | +17.42 | +2.44 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_religion | E | 31.64 | 100.00 | 1029.6 | 3 |  |
| migration_given_religion | D | 7.33 | 35.00 | 74.5 | 2 |  |
| amenity_given_gp | C | 5.08 | 39.52 | 40.2 | 1 |  |
| vote_given_religion | C | 4.36 | 95.00 | 27.2 | 1 |  |
| education_given_caste | E | 3.39 | 92.00 | 45.9 | 2 |  |
| asset_given_gp | C | 3.05 | 25.55 | 15.1 | 1 |  |
| caste_given_gp | E | 3.03 | 26.74 | 24.3 | 1 |  |
| vote_given_gender | C | 2.52 | 25.50 | 23.2 | 1 |  |
| asset_given_occupation | C | 2.36 | 85.00 | 19.5 | 0 |  |
| vote_given_welfare | C | 2.32 | 52.00 | 18.1 | 0 |  |
| asset_given_religion | C | 2.18 | 65.00 | 15.2 | 0 |  |
| religion_given_gp | E | 2.02 | 16.00 | 9.2 | 0 |  |
| vote_given_caste | C | 1.39 | 65.00 | 13.5 | 0 |  |
| lang_given_religion | E | 0.61 | 25.00 | 1.8 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 0.53
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 47.92 | -2.08 | -0.29 | True |
| AITC | 40.0 | 43.75 | +3.75 | +0.53 | True |
| Left_INC_combined | 8.0 | 6.25 | -1.75 | -0.45 | True |
| Other_NOTA | 2.0 | 2.08 | +0.08 | +0.04 | True |

### vote_2019_LS_share (tier D)  max |z| = 1.75
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 47.92 | -0.08 | -0.01 | True |
| AITC | 44.0 | 43.75 | -0.25 | -0.03 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -1.75 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -0.99 | True |
