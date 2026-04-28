# Verifier report (n=100)

- composite chi-square: **1174.15** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 4.5  · max joint cell |z|: 8.11  · aggregate vote max |z|: 4.31
- max axis gap: 21.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 21.54 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| economic_status | E | 4.50 | 21.00 | 31.2 | 1 |
| occupation | E | 4.07 | 16.92 | 36.4 | 1 |
| workforce_status | E | 3.79 | 17.00 | 25.3 | 1 |
| education | E | 3.73 | 9.00 | 27.5 | 1 |
| migration | D | 3.52 | 12.00 | 39.5 | 4 |
| gp_location | E | 3.43 | 17.10 | 23.5 | 2 |
| household_composition | E | 3.37 | 8.00 | 15.1 | 1 |
| marital_status | E | 3.32 | 9.00 | 14.2 | 1 |
| amenities | C | 3.08 | 12.00 | 35.0 | 3 |
| asset_media | C | 2.58 | 12.00 | 22.1 | 1 |
| caste | E | 2.55 | 12.36 | 18.2 | 1 |
| age_cohort | E | 1.85 | 3.43 | 7.1 | 0 |
| class_of_worker | E | 1.65 | 11.46 | 5.0 | 0 |
| gender | A/E | 1.41 | 7.04 | 4.0 | 0 |
| mother_tongue | E | 0.82 | 1.20 | 1.5 | 0 |
| religion | A/E | 0.50 | 0.58 | 0.4 | 0 |
| aila_displacement_status | D | 0.00 | 0.00 | 0.0 | 0 |
| bheri_economy_dependent | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| economic_status | BPL_household | 32.0 | 53.0 | +21.00 | +4.50 |
| occupation | Fishing_prawn_bheri | 10.0 | 26.92 | +16.92 | +4.07 |
| workforce_status | Main_worker | 28.0 | 45.0 | +17.00 | +3.79 |
| education | Graduate | 5.5 | 14.0 | +8.50 | +3.73 |
| migration | Out_migrant | 3.0 | 9.0 | +6.00 | +3.52 |
| gp_location | U1_CDB_Sandeshkhali_I | 53.9 | 71.0 | +17.10 | +3.43 |
| gp_location | U2_CDB_Sandeshkhali_II_AC_share | 46.1 | 29.0 | -17.10 | -3.43 |
| household_composition | Extended_multi_generation | 6.0 | 14.0 | +8.00 | +3.37 |
| marital_status | Widowed | 8.0 | 17.0 | +9.00 | +3.32 |
| amenities | Electricity | 88.0 | 98.0 | +10.00 | +3.08 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 8.11 | 44.50 | 128.2 | 4 |  |
| caste_given_gp | A/E | 5.15 | 17.71 | 52.2 | 2 |  |
| vote_given_gender | C | 5.01 | 38.24 | 51.4 | 2 |  |
| migration_given_religion | E | 4.67 | 85.00 | 51.6 | 3 |  |
| workforce_given_education | E | 4.37 | 42.73 | 31.4 | 1 |  |
| asset_given_religion | E | 4.31 | 85.00 | 34.5 | 2 |  |
| vote_given_religion | E | 4.30 | 55.00 | 40.4 | 2 |  |
| asset_given_occupation | D | 3.74 | 65.00 | 45.4 | 2 |  |
| vote_given_caste | C | 3.50 | 55.00 | 42.0 | 1 |  |
| amenities_given_gp | C | 3.24 | 19.31 | 47.5 | 2 |  |
| caste_given_religion | E | 2.97 | 100.00 | 20.6 | 1 |  |
| asset_given_gp | C | 2.80 | 24.62 | 24.6 | 2 |  |
| lang_given_religion | E | 0.73 | 95.00 | 1.5 | 0 |  |
| religion_given_gp | A | 0.53 | 2.14 | 0.6 | 0 |  |
| education_given_age_gender | E | 0.00 | 10.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 79.98 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier None)  max |z| = 4.31
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 52.46 | 74.0 | +21.54 | +4.31 | False |
| BJP | 38.83 | 24.0 | -14.83 | -3.04 | False |
| CPI | 2.81 | 1.0 | -1.81 | -1.10 | True |
| INC | 1.43 | 1.0 | -0.43 | -0.36 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | Others | vote_values=['Others'] not present in sampled population (field=vote_2019_LS) |