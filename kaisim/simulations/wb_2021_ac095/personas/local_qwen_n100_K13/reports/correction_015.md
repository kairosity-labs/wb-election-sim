# Verifier report (n=114)

- composite chi-square: **1457.9** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 8.54  · max joint cell |z|: 5.33  · aggregate vote max |z|: 4.09
- max axis gap: 21.09 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 18.77 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| migration | E | 8.54 | 21.09 | 122.9 | 4 |
| household_type | E | 4.80 | 11.23 | 29.9 | 2 |
| workforce_status | E | 4.66 | 20.00 | 39.0 | 2 |
| education | E | 4.17 | 11.18 | 30.9 | 1 |
| gender | E | 3.28 | 15.36 | 21.5 | 2 |
| amenities | C | 2.96 | 11.14 | 33.0 | 2 |
| caste | E | 2.88 | 11.94 | 24.8 | 1 |
| class_of_worker | E | 2.87 | 16.52 | 13.6 | 1 |
| gp_location | E | 2.85 | 13.27 | 16.2 | 2 |
| marital_status | E | 2.58 | 6.16 | 9.3 | 1 |
| asset_media | C | 2.57 | 11.49 | 15.6 | 1 |
| age_cohort | E | 2.09 | 5.86 | 9.6 | 0 |
| economic_status | E | 2.02 | 7.82 | 5.7 | 0 |
| occupation | E | 1.99 | 11.34 | 15.4 | 0 |
| mother_tongue | E | 1.18 | 1.20 | 2.8 | 0 |
| religion | E | 1.07 | 2.33 | 1.7 | 0 |
| welfare_exposure | None | 0.00 | 0.00 | 0.0 | 0 |
| welfare_dominant | None | 0.00 | 0.00 | 0.0 | 0 |

## Top 8 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| migration | Out_migrant | 0.5 | 6.14 | +5.64 | +8.54 |
| household_type | Extended_multi_generation | 6.0 | 16.67 | +10.67 | +4.80 |
| migration | Native | 64.0 | 85.09 | +21.09 | +4.69 |
| workforce_status | Main_worker | 30.0 | 50.0 | +20.00 | +4.66 |
| education | Graduate | 9.0 | 20.18 | +11.18 | +4.17 |
| migration | Bangladesh | 23.0 | 7.89 | -15.11 | -3.83 |
| gender | Male | 51.31 | 66.67 | +15.36 | +3.28 |
| gender | Female | 48.68 | 33.33 | -15.35 | -3.28 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| vote_given_caste | C | 5.33 | 64.00 | 79.1 | 3 |  |
| vote_given_gender | C | 4.54 | 36.84 | 41.4 | 2 |  |
| migration_given_religion | D | 4.40 | 65.00 | 48.5 | 2 |  |
| vote_given_welfare | C | 3.94 | 45.00 | 47.8 | 2 |  |
| vote_given_religion | C | 3.87 | 40.00 | 40.8 | 2 |  |
| amenity_given_gp | C | 3.72 | 22.61 | 46.5 | 3 |  |
| education_given_caste | E | 3.66 | 78.00 | 93.5 | 4 |  |
| asset_given_gp | C | 3.52 | 24.36 | 45.0 | 3 |  |
| asset_given_occupation | C | 3.17 | 85.00 | 31.3 | 2 |  |
| asset_given_religion | C | 2.94 | 95.00 | 22.2 | 2 |  |
| caste_given_religion | E | 2.85 | 100.00 | 25.1 | 3 |  |
| religion_given_gp | E | 2.33 | 12.74 | 12.7 | 0 |  |
| caste_given_gp | E | 2.06 | 14.60 | 21.9 | 0 |  |
| lang_given_religion | E | 1.00 | 75.00 | 3.1 | 0 |  |

## Aggregate vote share
### vote_aggregate_2019_LS (tier D)  max |z| = 4.09
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 50.0 | 38.6 | -11.40 | -2.44 | True |
| AITC | 40.0 | 58.77 | +18.77 | +4.09 | False |
| Left_INC_combined | 8.0 | 1.75 | -6.25 | -2.46 | True |
| Other_NOTA | 2.0 | 0.88 | -1.12 | -0.86 | True |

### vote_2019_LS_share (tier D)  max |z| = 3.18
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 48.0 | 38.6 | -9.40 | -2.01 | True |
| AITC | 44.0 | 58.77 | +14.77 | +3.18 | False |
| CPI_INC | 6.0 | 0.0 | -6.00 | -2.70 | False |
| Other_NOTA | 2.0 | 0.0 | -2.00 | -1.53 | True |
