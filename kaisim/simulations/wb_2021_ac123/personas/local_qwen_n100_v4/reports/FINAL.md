# Verifier report (n=100)

- composite chi-square: **338.46** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 1.93  · max joint cell |z|: 4.35  · aggregate vote max |z|: 1.51
- max axis gap: 9.07 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 7.54 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| economic_status | E | 1.93 | 9.00 | 6.3 | 0 |
| workforce_status | E | 1.73 | 7.00 | 8.8 | 0 |
| amenities | C | 1.62 | 8.00 | 5.7 | 0 |
| caste | E | 1.53 | 5.36 | 8.3 | 0 |
| migration | D | 1.47 | 4.00 | 3.0 | 0 |
| asset_media | C | 1.43 | 4.00 | 4.5 | 0 |
| gp_location | E | 1.42 | 7.10 | 4.1 | 0 |
| occupation | E | 1.40 | 5.97 | 9.4 | 0 |
| class_of_worker | E | 1.40 | 9.07 | 3.9 | 0 |
| education | E | 1.23 | 3.00 | 3.4 | 0 |
| marital_status | E | 1.11 | 3.00 | 2.4 | 0 |
| age_cohort | E | 0.88 | 2.71 | 1.7 | 0 |
| household_composition | E | 0.84 | 3.00 | 1.2 | 0 |
| mother_tongue | E | 0.82 | 1.20 | 1.5 | 0 |
| gender | A/E | 0.81 | 4.04 | 1.3 | 0 |
| religion | A/E | 0.50 | 1.58 | 0.6 | 0 |
| aila_displacement_status | D | 0.00 | 0.00 | 0.0 | 0 |
| bheri_economy_dependent | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| economic_status | BPL_household | 32.0 | 41.0 | +9.00 | +1.93 |
| workforce_status | Marginal_worker | 14.0 | 20.0 | +6.00 | +1.73 |
| amenities | Wood_biomass_fuel | 58.0 | 66.0 | +8.00 | +1.62 |
| caste | Other_Hindu_middle_castes | 2.28 | 0.0 | -2.28 | -1.53 |
| migration | WB_other_district | 8.0 | 4.0 | -4.00 | -1.47 |
| asset_media | Four_wheeler | 2.0 | 0.0 | -2.00 | -1.43 |
| workforce_status | Non_worker | 42.0 | 35.0 | -7.00 | -1.42 |
| gp_location | U1_CDB_Sandeshkhali_I | 53.9 | 61.0 | +7.10 | +1.42 |
| gp_location | U2_CDB_Sandeshkhali_II_AC_share | 46.1 | 39.0 | -7.10 | -1.42 |
| occupation | Household_industry | 3.5 | 0.0 | -3.50 | -1.40 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| asset_given_occupation | D | 4.35 | 65.00 | 38.6 | 2 |  |
| caste_given_gp | A/E | 2.81 | 9.01 | 18.0 | 1 |  |
| education_given_caste | E | 2.24 | 40.00 | 31.0 | 0 |  |
| vote_given_gender | C | 2.21 | 16.33 | 11.8 | 0 |  |
| workforce_given_education | E | 2.09 | 30.00 | 20.4 | 0 |  |
| asset_given_gp | C | 1.85 | 10.87 | 4.8 | 0 |  |
| amenities_given_gp | C | 1.81 | 9.74 | 6.9 | 0 |  |
| vote_given_religion | E | 1.70 | 55.00 | 12.5 | 0 |  |
| vote_given_caste | C | 1.70 | 55.00 | 23.5 | 0 |  |
| caste_given_religion | E | 1.56 | 100.00 | 8.4 | 0 |  |
| migration_given_religion | E | 1.40 | 85.00 | 7.1 | 0 |  |
| asset_given_religion | E | 1.06 | 85.00 | 2.1 | 0 |  |
| lang_given_religion | E | 0.74 | 95.00 | 1.5 | 0 |  |
| religion_given_gp | A | 0.50 | 2.94 | 0.9 | 0 |  |
| education_given_age_gender | E | 0.00 | 10.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 79.98 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier None)  max |z| = 1.51
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 52.46 | 60.0 | +7.54 | +1.51 | True |
| BJP | 38.83 | 33.0 | -5.83 | -1.20 | True |
| CPI | 2.81 | 2.0 | -0.81 | -0.49 | True |
| INC | 1.43 | 2.0 | +0.57 | +0.48 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | Others | vote_values=['Others'] not present in sampled population (field=vote_2019_LS) |