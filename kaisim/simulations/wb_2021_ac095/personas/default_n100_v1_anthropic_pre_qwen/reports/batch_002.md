# Verifier report (n=37)

- composite chi-square: **490.64** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.94  · max joint cell |z|: 3.04  · aggregate vote max |z|: 1.79
- max axis gap: 20.95 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 14.05 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| amenities | C | 2.94 | 20.95 | 15.8 | 1 |
| migration | E | 2.14 | 14.84 | 8.2 | 0 |
| caste | E | 1.95 | 10.63 | 8.9 | 0 |
| occupation | E | 1.74 | 12.00 | 9.3 | 0 |
| asset_media | C | 1.71 | 13.38 | 8.8 | 0 |
| gp_location | E | 1.71 | 13.96 | 5.8 | 0 |
| household_type | E | 1.40 | 10.54 | 3.7 | 0 |
| age_cohort | E | 1.27 | 5.81 | 4.5 | 0 |
| class_of_worker | E | 1.21 | 11.25 | 3.7 | 0 |
| economic_status | E | 1.14 | 7.73 | 3.3 | 0 |
| education | E | 0.98 | 6.78 | 2.8 | 0 |
| marital_status | E | 0.91 | 3.81 | 1.3 | 0 |
| workforce_status | E | 0.91 | 7.46 | 1.6 | 0 |
| mother_tongue | E | 0.67 | 1.20 | 0.9 | 0 |
| gender | E | 0.66 | 5.45 | 0.9 | 0 |
| religion | E | 0.61 | 1.00 | 0.4 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| amenities | Improved_sanitation_latrine | 75.0 | 54.05 | -20.95 | -2.94 |
| migration | Bangladesh | 23.0 | 37.84 | +14.84 | +2.14 |
| caste | Bagdi | 1.5 | 5.41 | +3.91 | +1.95 |
| amenities | Wood | 45.0 | 59.46 | +14.46 | +1.77 |
| occupation | Government_services_teachers | 4.0 | 12.5 | +8.50 | +1.74 |
| gp_location | U1_Muni | 54.5 | 40.54 | -13.96 | -1.71 |
| gp_location | U2_CDB_rural | 45.5 | 59.46 | +13.96 | +1.71 |
| asset_media | TwoWheeler | 35.0 | 21.62 | -13.38 | -1.71 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| amenity_given_gp | C | 3.04 | 32.27 | 20.8 | 1 |  |
| vote_given_gender | C | 3.00 | 37.50 | 20.3 | 1 |  |
| education_given_caste | E | 2.84 | 86.00 | 54.4 | 2 |  |
| vote_given_welfare | C | 2.39 | 65.00 | 25.1 | 0 |  |
| asset_given_gp | C | 2.31 | 28.33 | 19.9 | 0 |  |
| caste_given_gp | E | 2.16 | 19.45 | 17.5 | 0 |  |
| asset_given_occupation | C | 2.11 | 92.00 | 14.8 | 0 |  |
| caste_given_religion | E | 2.00 | 100.00 | 7.9 | 0 |  |
| migration_given_religion | D | 1.99 | 65.00 | 7.4 | 0 |  |
| vote_given_caste | C | 1.89 | 64.00 | 21.0 | 0 |  |
| asset_given_religion | C | 1.80 | 95.00 | 4.4 | 0 |  |
| vote_given_religion | C | 1.73 | 40.00 | 12.1 | 0 |  |
| religion_given_gp | E | 1.07 | 10.33 | 3.4 | 0 |  |
| lang_given_religion | E | 0.61 | 75.00 | 1.1 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 1.79
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 37.84 | -12.16 | -1.48 | True |
| AITC | 40.0 | 54.05 | +14.05 | +1.75 | True |
| Left_INC_combined | 8.0 | 0.0 | -8.00 | -1.79 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -0.87 | True |
