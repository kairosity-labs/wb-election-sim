# Verifier report (n=100)

- composite chi-square: **348.7** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.45  · max joint cell |z|: 2.94  · aggregate vote max |z|: 0.72
- max axis gap: 12.44 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 3.5 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| education | E | 2.45 | 7.00 | 10.5 | 0 |
| workforce_status | E | 2.36 | 11.00 | 10.6 | 0 |
| caste | E | 2.17 | 5.20 | 7.6 | 0 |
| amenities | C | 2.11 | 5.00 | 9.9 | 0 |
| occupation | E | 1.96 | 12.44 | 19.6 | 0 |
| mother_tongue | A | 1.58 | 2.43 | 5.1 | 0 |
| economic_status | E | 1.53 | 3.00 | 3.3 | 0 |
| migration | D | 1.53 | 4.00 | 5.7 | 0 |
| religion | E | 1.49 | 5.70 | 4.6 | 0 |
| age_cohort | E | 1.47 | 4.95 | 5.8 | 0 |
| class_of_worker | E | 1.41 | 8.33 | 4.1 | 0 |
| asset_media | C | 1.38 | 6.00 | 5.0 | 0 |
| marital_status | E | 1.25 | 6.00 | 3.5 | 0 |
| household_composition | E | 1.11 | 5.00 | 2.3 | 0 |
| gp_location | A | 0.63 | 2.30 | 0.8 | 0 |
| gender | E | 0.20 | 1.00 | 0.1 | 0 |
| rajbanshi_status | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| education | Graduate | 9.0 | 16.0 | +7.00 | +2.45 |
| workforce_status | Main_worker | 32.0 | 43.0 | +11.00 | +2.36 |
| caste | UC_bhadralok | 4.5 | 9.0 | +4.50 | +2.17 |
| amenities | Electricity | 94.0 | 99.0 | +5.00 | +2.11 |
| workforce_status | Unemployed | 9.0 | 3.0 | -6.00 | -2.10 |
| occupation | Agricultural_labourer | 32.0 | 44.44 | +12.44 | +1.96 |
| occupation | Construction | 6.0 | 0.0 | -6.00 | -1.86 |
| amenities | Other_fuel | 5.0 | 1.0 | -4.00 | -1.84 |
| occupation | Cultivator | 20.0 | 29.63 | +9.63 | +1.77 |
| mother_tongue | Other | 2.43 | 0.0 | -2.43 | -1.58 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_gp | E | 2.94 | 9.00 | 13.0 | 1 |  |
| lang_given_religion | E | 2.47 | 90.00 | 10.2 | 0 |  |
| workforce_given_education | E | 2.44 | 62.00 | 27.5 | 0 |  |
| asset_given_gp | C | 2.42 | 25.33 | 14.9 | 0 |  |
| asset_given_occupation | E | 2.37 | 78.00 | 19.9 | 0 |  |
| amenities_given_gp | C | 2.26 | 12.00 | 11.0 | 0 |  |
| caste_given_religion | E | 1.95 | 100.00 | 4.9 | 0 |  |
| education_given_caste | E | 1.69 | 28.00 | 24.3 | 0 |  |
| migration_given_religion | E | 1.66 | 80.00 | 9.2 | 0 |  |
| vote_given_religion | E | 1.52 | 52.00 | 6.3 | 0 |  |
| vote_given_caste | C | 1.52 | 60.00 | 17.6 | 0 |  |
| asset_given_religion | E | 1.47 | 92.00 | 3.9 | 0 |  |
| vote_given_gender | C | 1.04 | 4.81 | 3.0 | 0 |  |
| education_given_age_gender | E | 0.00 | 16.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |
| religion_given_gp | E | 0.00 | 0.00 | 0.0 | 0 | all parent values absent from axes (dropped: ['U1_Census_towns_cluster', 'U2_CDB_II_rural_GPs']) |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 0.72
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 51.27 | 51.0 | -0.27 | -0.05 | True |
| AITC | 39.5 | 43.0 | +3.50 | +0.72 | True |
| AIFB | 4.28 | 4.0 | -0.28 | -0.14 | True |
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