# Verifier report (n=500)

- composite chi-square: **610.65** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 5.18  · max joint cell |z|: 3.42  · aggregate vote max |z|: 1.52
- max axis gap: 6.0 pp  · max joint cell gap: 93.0 pp  · aggregate max gap: 1.5 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| mother_tongue | A | 5.18 | 3.57 | 34.5 | 1 |
| occupation | E | 3.29 | 5.37 | 15.5 | 1 |
| workforce_status | E | 3.00 | 6.00 | 17.3 | 2 |
| education | E | 2.96 | 5.20 | 23.7 | 2 |
| amenities | C | 2.44 | 5.40 | 11.1 | 0 |
| marital_status | E | 2.31 | 2.80 | 6.6 | 0 |
| asset_media | C | 2.06 | 3.00 | 8.8 | 0 |
| age_cohort | E | 1.07 | 1.43 | 4.5 | 0 |
| caste | E | 1.04 | 1.40 | 1.7 | 0 |
| economic_status | E | 0.96 | 1.40 | 1.9 | 0 |
| religion | E | 0.95 | 0.30 | 1.0 | 0 |
| migration | D | 0.94 | 1.00 | 2.8 | 0 |
| gender | E | 0.90 | 2.00 | 1.6 | 0 |
| class_of_worker | E | 0.44 | 1.30 | 0.3 | 0 |
| household_composition | E | 0.19 | 0.40 | 0.1 | 0 |
| gp_location | A | 0.18 | 0.30 | 0.1 | 0 |
| rajbanshi_status | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| mother_tongue | Other | 2.43 | 6.0 | +3.57 | +5.18 |
| occupation | Construction | 6.0 | 11.37 | +5.37 | +3.29 |
| workforce_status | Student | 11.0 | 6.8 | -4.20 | -3.00 |
| education | Secondary | 19.0 | 13.8 | -5.20 | -2.96 |
| workforce_status | Non_worker | 36.0 | 42.0 | +6.00 | +2.80 |
| education | Higher_Secondary | 12.0 | 8.2 | -3.80 | -2.61 |
| amenities | Wood_biomass_fuel | 57.0 | 51.6 | -5.40 | -2.44 |
| marital_status | Widowed | 8.0 | 5.2 | -2.80 | -2.31 |
| amenities | Improved_sanitation | 68.0 | 63.6 | -4.40 | -2.11 |
| asset_media | Banking_access | 88.0 | 85.0 | -3.00 | -2.06 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| asset_given_gp | C | 3.42 | 12.68 | 27.8 | 2 |  |
| asset_given_religion | E | 3.07 | 92.00 | 14.4 | 1 |  |
| caste_given_gp | E | 3.01 | 15.92 | 24.1 | 1 |  |
| asset_given_occupation | E | 2.86 | 36.89 | 39.5 | 2 |  |
| vote_given_caste | C | 2.70 | 20.00 | 41.3 | 1 |  |
| workforce_given_education | E | 2.69 | 18.00 | 40.2 | 4 |  |
| migration_given_religion | E | 2.34 | 80.00 | 18.2 | 0 |  |
| vote_given_religion | E | 1.94 | 52.00 | 18.4 | 0 |  |
| education_given_caste | E | 1.89 | 28.00 | 14.1 | 0 |  |
| vote_given_gender | C | 1.46 | 4.61 | 8.9 | 0 |  |
| amenities_given_gp | C | 1.43 | 3.37 | 3.1 | 0 |  |
| lang_given_religion | E | 1.41 | 90.00 | 7.7 | 0 |  |
| caste_given_religion | E | 1.06 | 1.70 | 1.7 | 0 |  |
| education_given_age_gender | E | 0.00 | 16.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |
| religion_given_gp | E | 0.00 | 0.00 | 0.0 | 0 | all parent values absent from axes (dropped: ['U1_Census_towns_cluster', 'U2_CDB_II_rural_GPs']) |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.52
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 51.27 | 51.2 | -0.07 | -0.03 | True |
| AITC | 39.5 | 38.0 | -1.50 | -0.69 | True |
| AIFB | 4.28 | 3.6 | -0.68 | -0.75 | True |
| INC | 2.45 | 1.4 | -1.05 | -1.52 | True |


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