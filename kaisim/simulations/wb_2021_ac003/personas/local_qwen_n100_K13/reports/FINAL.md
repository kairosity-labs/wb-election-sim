# Verifier report (n=100)

- composite chi-square: **1085.91** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 4.2  · max joint cell |z|: 5.43  · aggregate vote max |z|: 1.53
- max axis gap: 18.33 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 7.5 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| amenities | C | 4.20 | 15.00 | 37.0 | 2 |
| education | E | 4.19 | 12.00 | 34.9 | 1 |
| workforce_status | E | 3.64 | 17.00 | 31.0 | 2 |
| class_of_worker | E | 3.50 | 18.33 | 25.0 | 2 |
| migration | D | 3.27 | 12.00 | 21.6 | 1 |
| household_composition | E | 3.14 | 8.00 | 12.3 | 1 |
| gp_location | A | 3.11 | 11.30 | 19.3 | 2 |
| occupation | E | 2.99 | 18.00 | 24.1 | 1 |
| age_cohort | E | 2.73 | 8.95 | 20.7 | 2 |
| gender | E | 2.60 | 13.00 | 13.5 | 2 |
| caste | E | 2.58 | 10.60 | 14.3 | 1 |
| asset_media | C | 2.51 | 11.00 | 20.6 | 1 |
| economic_status | E | 2.34 | 10.00 | 16.9 | 0 |
| marital_status | E | 2.08 | 10.00 | 8.7 | 0 |
| mother_tongue | A | 1.58 | 2.51 | 5.0 | 0 |
| religion | E | 0.57 | 0.80 | 0.6 | 0 |
| rajbanshi_status | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| amenities | Improved_drinking_water_source | 85.0 | 100.0 | +15.00 | +4.20 |
| education | Graduate | 9.0 | 21.0 | +12.00 | +4.19 |
| workforce_status | Main_worker | 32.0 | 49.0 | +17.00 | +3.64 |
| class_of_worker | Employer | 2.0 | 8.33 | +6.33 | +3.50 |
| class_of_worker | Employee | 25.0 | 6.67 | -18.33 | -3.28 |
| migration | Native | 84.0 | 96.0 | +12.00 | +3.27 |
| household_composition | Extended_multi_generation | 7.0 | 15.0 | +8.00 | +3.14 |
| gp_location | Census_towns_cluster | 15.7 | 27.0 | +11.30 | +3.11 |
| gp_location | CDB_II_rural_GPs | 84.3 | 73.0 | -11.30 | -3.11 |
| occupation | Agricultural_labourer | 32.0 | 50.0 | +18.00 | +2.99 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| asset_given_gp | C | 5.43 | 38.30 | 60.6 | 2 |  |
| workforce_given_education | E | 4.88 | 50.00 | 44.7 | 1 |  |
| amenities_given_gp | C | 4.86 | 28.30 | 60.5 | 4 |  |
| vote_given_gender | C | 4.55 | 38.00 | 52.1 | 2 |  |
| caste_given_gp | E | 3.83 | 18.26 | 26.1 | 1 |  |
| migration_given_religion | E | 3.65 | 80.00 | 28.9 | 1 |  |
| vote_given_caste | C | 2.93 | 40.00 | 31.1 | 1 |  |
| asset_given_occupation | E | 2.91 | 78.00 | 36.0 | 2 |  |
| caste_given_religion | E | 2.63 | 100.00 | 14.4 | 1 |  |
| lang_given_religion | E | 2.39 | 90.00 | 10.1 | 0 |  |
| asset_given_religion | E | 2.25 | 92.00 | 20.7 | 0 |  |
| vote_given_religion | E | 2.12 | 52.00 | 10.9 | 0 |  |
| education_given_caste | E | 2.04 | 28.00 | 23.7 | 0 |  |
| education_given_age_gender | E | 0.00 | 16.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |
| religion_given_gp | E | 0.00 | 0.00 | 0.0 | 0 | all parent values absent from axes (dropped: ['U1_Census_towns_cluster', 'U2_CDB_II_rural_GPs']) |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.53
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 51.27 | 46.0 | -5.27 | -1.05 | True |
| AITC | 39.5 | 47.0 | +7.50 | +1.53 | True |
| AIFB | 4.28 | 5.0 | +0.72 | +0.36 | True |
| INC | 2.45 | 2.0 | -0.45 | -0.29 | True |


## Partial-coverage telemetry

### Skipped / partial joints
| joint | reason | n parent values dropped |
|---|---|---|
| asset_given_occupation | 1 parent value(s) dropped — not in this AC's axis value-space | 1 |
| religion_given_gp | all parent values absent from axes (dropped: ['U1_Census_towns_cluster', 'U2_CDB_II_rural_GPs']) | 2 |

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | Others | vote_values=['Others'] not present in sampled population (field=vote_2019_LS) |