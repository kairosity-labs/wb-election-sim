# Verifier report (n=106)

- composite chi-square: **917.75** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 4.32  · max joint cell |z|: 5.99  · aggregate vote max |z|: 2.6
- max axis gap: 14.86 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 7.17 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| amenities | C | 4.32 | 10.85 | 30.5 | 2 |
| migration | E | 2.86 | 11.68 | 16.2 | 1 |
| caste | E | 2.69 | 8.93 | 17.7 | 1 |
| gender | E | 2.45 | 11.90 | 12.0 | 0 |
| asset_media | C | 2.32 | 8.68 | 19.8 | 0 |
| occupation | E | 2.32 | 14.86 | 14.9 | 0 |
| workforce_status | E | 2.31 | 11.21 | 11.5 | 0 |
| economic_status | E | 2.31 | 8.19 | 11.1 | 0 |
| household_type | E | 2.31 | 5.32 | 6.2 | 0 |
| class_of_worker | E | 1.86 | 10.61 | 5.9 | 0 |
| education | E | 1.85 | 6.02 | 6.1 | 0 |
| marital_status | E | 1.74 | 4.42 | 5.2 | 0 |
| gp_location | E | 1.71 | 8.27 | 5.9 | 0 |
| age_cohort | E | 1.56 | 4.92 | 8.2 | 0 |
| religion | E | 1.52 | 5.79 | 5.0 | 0 |
| mother_tongue | E | 1.13 | 1.20 | 2.6 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| amenities | Other_fuel | 5.0 | 14.15 | +9.15 | +4.32 |
| migration | Bangladesh | 23.0 | 11.32 | -11.68 | -2.86 |
| caste | OBC_specific | 2.0 | 5.66 | +3.66 | +2.69 |
| amenities | Improved_sanitation_latrine | 75.0 | 85.85 | +10.85 | +2.58 |
| gender | Male | 51.31 | 63.21 | +11.90 | +2.45 |
| gender | Female | 48.68 | 36.79 | -11.89 | -2.45 |
| occupation | Agricultural_labourer | 28.0 | 42.86 | +14.86 | +2.32 |
| asset_media | FourWheeler | 8.0 | 1.89 | -6.11 | -2.32 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 5.99 | 56.95 | 114.5 | 3 |  |
| migration_given_religion | D | 3.78 | 65.00 | 31.2 | 2 |  |
| vote_given_caste | C | 3.77 | 40.00 | 60.4 | 3 |  |
| asset_given_gp | C | 3.60 | 22.72 | 27.6 | 2 |  |
| amenity_given_gp | C | 3.37 | 22.19 | 27.4 | 2 |  |
| caste_given_gp | E | 3.13 | 21.67 | 26.0 | 2 |  |
| religion_given_gp | E | 2.79 | 14.96 | 16.1 | 2 |  |
| asset_given_religion | C | 2.78 | 95.00 | 24.5 | 2 |  |
| asset_given_occupation | C | 2.73 | 80.00 | 22.8 | 1 |  |
| caste_given_religion | E | 2.70 | 100.00 | 17.4 | 1 |  |
| vote_given_welfare | C | 2.58 | 65.00 | 36.4 | 1 |  |
| vote_given_religion | C | 2.36 | 40.00 | 14.5 | 0 |  |
| vote_given_gender | C | 1.88 | 8.97 | 8.6 | 0 |  |
| lang_given_religion | E | 0.86 | 75.00 | 2.6 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 1.51
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 46.23 | -3.77 | -0.78 | True |
| AITC | 40.0 | 47.17 | +7.17 | +1.51 | True |
| Left_INC_combined | 8.0 | 4.72 | -3.28 | -1.25 | True |
| Other_NOTA | 2.0 | 1.89 | -0.11 | -0.08 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.60
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 46.23 | -1.77 | -0.37 | True |
| AITC | 44.0 | 47.17 | +3.17 | +0.66 | True |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.60 | False |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.47 | True |
