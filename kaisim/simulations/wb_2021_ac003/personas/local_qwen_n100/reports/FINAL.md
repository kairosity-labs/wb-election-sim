# Verifier report (n=100)

- composite chi-square: **392.81** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.46  · max joint cell |z|: 3.1  · aggregate vote max |z|: 0.51
- max axis gap: 10.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 2.5 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| economic_status | E | 2.46 | 9.00 | 16.3 | 0 |
| occupation | E | 2.36 | 10.00 | 18.6 | 0 |
| education | E | 2.10 | 6.00 | 14.2 | 0 |
| asset_media | C | 2.04 | 7.00 | 16.4 | 0 |
| mother_tongue | A | 1.58 | 3.51 | 6.9 | 0 |
| workforce_status | E | 1.54 | 5.00 | 6.4 | 0 |
| migration | D | 1.53 | 4.00 | 8.2 | 0 |
| marital_status | E | 1.47 | 4.00 | 3.4 | 0 |
| class_of_worker | E | 1.47 | 9.00 | 4.3 | 0 |
| amenities | C | 1.41 | 7.00 | 5.2 | 0 |
| age_cohort | E | 1.39 | 3.93 | 8.7 | 0 |
| caste | E | 1.37 | 6.80 | 4.8 | 0 |
| religion | E | 1.23 | 4.70 | 3.3 | 0 |
| household_composition | E | 1.18 | 4.00 | 2.2 | 0 |
| gender | E | 1.00 | 5.00 | 2.0 | 0 |
| gp_location | A | 0.91 | 3.30 | 1.6 | 0 |
| rajbanshi_status | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| economic_status | Middle | 12.0 | 4.0 | -8.00 | -2.46 |
| occupation | Services | 10.0 | 20.0 | +10.00 | +2.36 |
| economic_status | BPL_household | 24.0 | 33.0 | +9.00 | +2.11 |
| education | Graduate | 9.0 | 15.0 | +6.00 | +2.10 |
| asset_media | Radio | 4.0 | 0.0 | -4.00 | -2.04 |
| asset_media | Mobile_phone | 84.0 | 91.0 | +7.00 | +1.91 |
| education | Higher_Secondary | 12.0 | 18.0 | +6.00 | +1.85 |
| asset_media | Four_wheeler | 5.0 | 1.0 | -4.00 | -1.84 |
| asset_media | Computer | 6.0 | 2.0 | -4.00 | -1.68 |
| occupation | Transport_logistics | 5.0 | 10.0 | +5.00 | +1.62 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| asset_given_occupation | E | 3.10 | 92.00 | 18.6 | 1 |  |
| education_given_caste | E | 2.64 | 30.85 | 25.8 | 1 |  |
| asset_given_gp | C | 2.58 | 26.21 | 17.8 | 1 |  |
| lang_given_religion | E | 2.46 | 90.00 | 15.5 | 0 |  |
| workforce_given_education | E | 2.23 | 38.00 | 25.2 | 0 |  |
| amenities_given_gp | C | 2.12 | 16.21 | 11.4 | 0 |  |
| migration_given_religion | E | 1.71 | 80.00 | 11.5 | 0 |  |
| vote_given_caste | C | 1.65 | 40.00 | 16.0 | 0 |  |
| vote_given_religion | E | 1.63 | 52.00 | 6.2 | 0 |  |
| asset_given_religion | E | 1.60 | 92.00 | 5.9 | 0 |  |
| caste_given_gp | E | 1.47 | 15.71 | 9.6 | 0 |  |
| caste_given_religion | E | 1.03 | 100.00 | 2.3 | 0 |  |
| vote_given_gender | C | 0.94 | 4.81 | 3.3 | 0 |  |
| education_given_age_gender | E | 0.00 | 16.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |
| religion_given_gp | E | 0.00 | 0.00 | 0.0 | 0 | all parent values absent from axes (dropped: ['U1_Census_towns_cluster', 'U2_CDB_II_rural_GPs']) |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 0.51
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 51.27 | 51.0 | -0.27 | -0.05 | True |
| AITC | 39.5 | 42.0 | +2.50 | +0.51 | True |
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