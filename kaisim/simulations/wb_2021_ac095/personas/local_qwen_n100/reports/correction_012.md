# Verifier report (n=116)

- composite chi-square: **999.75** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 5.09  · max joint cell |z|: 5.74  · aggregate vote max |z|: 2.72
- max axis gap: 14.86 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 11.72 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| caste | E | 5.09 | 7.88 | 34.4 | 1 |
| amenities | C | 3.92 | 12.07 | 30.5 | 2 |
| asset_media | C | 2.60 | 9.66 | 23.4 | 1 |
| gender | E | 2.32 | 10.76 | 10.7 | 0 |
| occupation | E | 2.32 | 14.86 | 14.9 | 0 |
| gp_location | E | 2.09 | 9.67 | 8.8 | 0 |
| household_type | E | 1.97 | 4.34 | 4.6 | 0 |
| class_of_worker | E | 1.86 | 10.61 | 5.9 | 0 |
| education | E | 1.80 | 5.76 | 5.9 | 0 |
| marital_status | E | 1.78 | 5.59 | 6.4 | 0 |
| age_cohort | E | 1.71 | 5.18 | 9.8 | 0 |
| religion | E | 1.67 | 6.07 | 6.0 | 0 |
| workforce_status | E | 1.46 | 6.21 | 4.9 | 0 |
| economic_status | E | 1.45 | 5.59 | 4.7 | 0 |
| mother_tongue | E | 1.19 | 1.20 | 2.8 | 0 |
| migration | E | 1.15 | 4.03 | 4.7 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| caste | OBC_specific | 2.0 | 8.62 | +6.62 | +5.09 |
| amenities | Other_fuel | 5.0 | 12.93 | +7.93 | +3.92 |
| amenities | Improved_sanitation_latrine | 75.0 | 87.07 | +12.07 | +3.00 |
| asset_media | TV | 80.0 | 89.66 | +9.66 | +2.60 |
| asset_media | FourWheeler | 8.0 | 1.72 | -6.28 | -2.49 |
| gender | Male | 51.31 | 62.07 | +10.76 | +2.32 |
| gender | Female | 48.68 | 37.93 | -10.75 | -2.32 |
| occupation | Agricultural_labourer | 28.0 | 42.86 | +14.86 | +2.32 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 5.74 | 53.67 | 113.7 | 4 |  |
| caste_given_religion | E | 5.10 | 100.00 | 33.9 | 1 |  |
| migration_given_religion | D | 4.80 | 65.00 | 36.4 | 1 |  |
| asset_given_gp | C | 4.04 | 24.06 | 25.0 | 1 |  |
| amenity_given_gp | C | 3.97 | 24.69 | 33.6 | 2 |  |
| vote_given_caste | C | 3.94 | 44.00 | 65.7 | 4 |  |
| vote_given_religion | C | 3.56 | 40.00 | 24.8 | 1 |  |
| religion_given_gp | E | 2.89 | 15.08 | 17.3 | 2 |  |
| caste_given_gp | E | 2.79 | 18.77 | 26.2 | 1 |  |
| asset_given_occupation | C | 2.73 | 80.00 | 22.8 | 1 |  |
| vote_given_welfare | C | 2.70 | 65.00 | 35.0 | 2 |  |
| asset_given_religion | C | 2.39 | 95.00 | 21.7 | 0 |  |
| vote_given_gender | C | 1.95 | 13.64 | 11.6 | 0 |  |
| lang_given_religion | E | 0.89 | 75.00 | 2.8 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 2.58
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 42.24 | -7.76 | -1.67 | True |
| AITC | 40.0 | 51.72 | +11.72 | +2.58 | False |
| Left_INC_combined | 8.0 | 4.31 | -3.69 | -1.46 | True |
| Other_NOTA | 2.0 | 1.72 | -0.28 | -0.21 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.72
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 42.24 | -5.76 | -1.24 | True |
| AITC | 44.0 | 51.72 | +7.72 | +1.68 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.72 | False |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.54 | True |
