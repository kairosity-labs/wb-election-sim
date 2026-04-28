# Verifier report (n=24)

- composite chi-square: **626.94** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.45  · max joint cell |z|: 3.32  · aggregate vote max |z|: 3.08
- max axis gap: 27.67 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 30.83 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| education | E | 3.45 | 20.17 | 18.1 | 1 |
| class_of_worker | E | 3.28 | 13.71 | 12.1 | 1 |
| caste | E | 3.04 | 22.68 | 23.2 | 2 |
| amenities | C | 2.83 | 25.00 | 14.1 | 1 |
| migration | E | 2.82 | 27.67 | 22.5 | 2 |
| asset_media | C | 2.45 | 20.00 | 12.8 | 0 |
| workforce_status | E | 2.26 | 23.00 | 11.9 | 0 |
| occupation | E | 1.91 | 18.00 | 10.5 | 0 |
| gender | E | 1.51 | 15.36 | 4.5 | 0 |
| household_type | E | 1.07 | 9.33 | 1.9 | 0 |
| marital_status | E | 1.06 | 7.17 | 2.0 | 0 |
| economic_status | E | 0.86 | 7.17 | 1.7 | 0 |
| gp_location | E | 0.85 | 8.67 | 1.5 | 0 |
| age_cohort | E | 0.84 | 3.19 | 1.3 | 0 |
| mother_tongue | E | 0.54 | 1.20 | 0.6 | 0 |
| religion | E | 0.49 | 2.33 | 0.4 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| education | Graduate | 9.0 | 29.17 | +20.17 | +3.45 |
| class_of_worker | Employer | 2.0 | 14.29 | +12.29 | +3.28 |
| caste | Other_SC | 1.3 | 8.33 | +7.03 | +3.04 |
| amenities | Improved_sanitation_latrine | 75.0 | 100.0 | +25.00 | +2.83 |
| migration | Native | 64.0 | 91.67 | +27.67 | +2.82 |
| migration | Out_migrant | 0.5 | 4.17 | +3.67 | +2.55 |
| caste | Other_Hindu_middle_castes | 26.85 | 4.17 | -22.68 | -2.51 |
| asset_media | TV | 80.0 | 100.0 | +20.00 | +2.45 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 3.32 | 90.00 | 62.4 | 3 |  |
| amenity_given_gp | C | 3.26 | 45.00 | 18.7 | 1 |  |
| vote_given_caste | C | 3.25 | 65.00 | 37.2 | 2 |  |
| vote_given_religion | C | 3.16 | 40.00 | 19.4 | 1 |  |
| caste_given_religion | E | 3.13 | 100.00 | 24.1 | 2 |  |
| vote_given_gender | C | 2.83 | 50.00 | 17.5 | 1 |  |
| migration_given_religion | D | 2.74 | 65.00 | 16.0 | 1 |  |
| asset_given_gp | C | 2.65 | 35.00 | 15.8 | 1 |  |
| vote_given_welfare | C | 2.25 | 60.00 | 16.9 | 0 |  |
| asset_given_religion | C | 2.17 | 95.00 | 7.9 | 0 |  |
| caste_given_gp | E | 2.03 | 24.00 | 13.2 | 0 |  |
| religion_given_gp | E | 1.50 | 17.00 | 6.0 | 0 |  |
| asset_given_occupation | C | 1.27 | 85.00 | 10.5 | 0 |  |
| lang_given_religion | E | 0.46 | 75.00 | 0.7 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 3.08
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 29.17 | -20.83 | -2.04 | True |
| AITC | 40.0 | 70.83 | +30.83 | +3.08 | False |
| Left_INC_combined | 8.0 | 0.0 | -8.00 | -1.44 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -0.70 | True |

### vote_2019_LS_share (tier D)  max |z| = 2.65
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 29.17 | -18.83 | -1.85 | True |
| AITC | 44.0 | 70.83 | +26.83 | +2.65 | False |
| CPI_INC | 6.0 | 0.0 | -6.00 | -1.24 | True |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -0.70 | True |
