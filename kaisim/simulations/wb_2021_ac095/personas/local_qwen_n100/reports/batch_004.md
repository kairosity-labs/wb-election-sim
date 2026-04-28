# Verifier report (n=47)

- composite chi-square: **914.22** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 5.1  · max joint cell |z|: 6.59  · aggregate vote max |z|: 1.73
- max axis gap: 24.17 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 6.81 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| asset_media | C | 5.10 | 24.17 | 47.4 | 2 |
| migration | E | 4.47 | 18.74 | 30.0 | 2 |
| amenities | C | 3.28 | 20.74 | 23.9 | 1 |
| education | E | 2.35 | 14.17 | 14.3 | 0 |
| caste | E | 2.15 | 9.71 | 10.4 | 0 |
| economic_status | E | 2.15 | 15.19 | 8.2 | 0 |
| age_cohort | E | 1.94 | 9.22 | 12.2 | 0 |
| gp_location | E | 1.94 | 14.07 | 7.5 | 0 |
| household_type | E | 1.88 | 12.55 | 6.9 | 0 |
| occupation | E | 1.74 | 15.75 | 12.3 | 0 |
| workforce_status | E | 1.48 | 9.45 | 6.2 | 0 |
| religion | E | 1.46 | 8.36 | 4.3 | 0 |
| marital_status | E | 1.35 | 8.85 | 4.0 | 0 |
| mother_tongue | E | 0.76 | 1.20 | 1.1 | 0 |
| class_of_worker | E | 0.57 | 5.00 | 0.6 | 0 |
| gender | E | 0.04 | 0.26 | 0.0 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| asset_media | Banking | 88.0 | 63.83 | -24.17 | -5.10 |
| migration | WB_other_district | 9.0 | 27.66 | +18.66 | +4.47 |
| amenities | Improved_sanitation_latrine | 75.0 | 95.74 | +20.74 | +3.28 |
| asset_media | TV | 80.0 | 97.87 | +17.87 | +3.06 |
| migration | Bangladesh | 23.0 | 4.26 | -18.74 | -3.05 |
| education | Middle | 22.0 | 36.17 | +14.17 | +2.35 |
| asset_media | Smartphone | 50.0 | 34.04 | -15.96 | -2.19 |
| caste | OBC_specific | 2.0 | 6.38 | +4.38 | +2.15 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 6.59 | 87.00 | 105.7 | 3 |  |
| asset_given_religion | C | 6.11 | 95.00 | 54.6 | 2 |  |
| migration_given_religion | D | 5.48 | 65.00 | 45.0 | 2 |  |
| asset_given_gp | C | 4.03 | 31.57 | 45.0 | 3 |  |
| amenity_given_gp | C | 4.03 | 37.86 | 32.6 | 1 |  |
| caste_given_gp | E | 3.22 | 26.00 | 18.4 | 1 |  |
| vote_given_caste | C | 3.16 | 65.00 | 38.0 | 1 |  |
| caste_given_religion | E | 2.09 | 100.00 | 9.7 | 0 |  |
| asset_given_occupation | C | 1.94 | 90.00 | 15.1 | 0 |  |
| vote_given_welfare | C | 1.85 | 65.00 | 19.2 | 0 |  |
| vote_given_religion | C | 1.51 | 40.00 | 6.4 | 0 |  |
| vote_given_gender | C | 1.40 | 14.17 | 6.7 | 0 |  |
| religion_given_gp | E | 1.36 | 11.74 | 5.6 | 0 |  |
| lang_given_religion | E | 0.51 | 75.00 | 1.0 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 0.98
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 48.94 | -1.06 | -0.15 | True |
| AITC | 40.0 | 46.81 | +6.81 | +0.95 | True |
| Left_INC_combined | 8.0 | 4.26 | -3.74 | -0.95 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -0.98 | True |

### vote_2019_LS_share (tier D)  max |z| = 1.73
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 48.94 | +0.94 | +0.13 | True |
| AITC | 44.0 | 46.81 | +2.81 | +0.39 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -1.73 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -0.98 | True |
