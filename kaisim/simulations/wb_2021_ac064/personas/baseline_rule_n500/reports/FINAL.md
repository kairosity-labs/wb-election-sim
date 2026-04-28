# Verifier report (n=500)

- composite chi-square: **755.87** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.61  · max joint cell |z|: 5.67  · aggregate vote max |z|: 0.79
- max axis gap: 7.8 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 1.7 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| workforce_status | E | 3.61 | 7.80 | 27.3 | 2 |
| migration | D | 2.85 | 1.60 | 19.3 | 1 |
| marital_status | E | 2.76 | 4.40 | 16.1 | 1 |
| mother_tongue | A | 2.01 | 0.80 | 6.7 | 0 |
| religion | D | 1.94 | 4.30 | 9.6 | 0 |
| amenities | C | 1.93 | 4.00 | 7.6 | 0 |
| caste | E | 1.90 | 3.20 | 15.7 | 0 |
| gp_location | D | 1.84 | 3.00 | 5.5 | 0 |
| asset_media | C | 1.72 | 3.80 | 7.9 | 0 |
| economic_status | E | 1.66 | 3.40 | 4.9 | 0 |
| household_composition | E | 1.51 | 3.00 | 3.8 | 0 |
| age_cohort | E | 1.35 | 1.69 | 3.5 | 0 |
| class_of_worker | E | 1.31 | 1.55 | 1.8 | 0 |
| education | E | 1.30 | 2.40 | 4.1 | 0 |
| occupation | E | 1.11 | 2.84 | 2.5 | 0 |
| gender | E | 0.32 | 0.71 | 0.2 | 0 |
| muslim_subcaste | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| workforce_status | Non_worker | 37.0 | 44.8 | +7.80 | +3.61 |
| workforce_status | Student | 11.0 | 6.2 | -4.80 | -3.43 |
| migration | Outside_India | 0.5 | 1.4 | +0.90 | +2.85 |
| marital_status | Separated_divorced | 1.5 | 0.0 | -1.50 | -2.76 |
| marital_status | Never_married | 25.0 | 29.4 | +4.40 | +2.27 |
| migration | Out_migrant | 1.0 | 0.0 | -1.00 | -2.25 |
| migration | Other_Indian_state | 3.0 | 1.4 | -1.60 | -2.10 |
| mother_tongue | Urdu | 0.8 | 1.6 | +0.80 | +2.01 |
| religion | Hindu | 56.5 | 60.8 | +4.30 | +1.94 |
| amenities | Electricity | 93.0 | 90.8 | -2.20 | -1.93 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| asset_given_occupation | D | 5.67 | 42.36 | 73.8 | 1 |  |
| caste_given_gp | A (SC/ST tier A); E (internal Hindu split) | 4.30 | 7.93 | 50.9 | 2 |  |
| education_given_caste | E | 3.70 | 46.67 | 76.4 | 4 |  |
| workforce_given_education | E | 3.30 | 18.00 | 55.9 | 5 |  |
| asset_given_gp | C | 3.25 | 17.30 | 30.1 | 2 |  |
| vote_given_religion | E | 2.89 | 28.00 | 24.5 | 1 |  |
| vote_given_caste | E | 2.74 | 47.50 | 52.7 | 1 |  |
| migration_given_religion | E | 2.68 | 80.00 | 15.5 | 1 |  |
| asset_given_religion | E | 2.63 | 90.00 | 14.3 | 1 |  |
| caste_given_religion | E | 2.27 | 100.00 | 10.4 | 0 |  |
| amenities_given_gp | C | 2.09 | 7.99 | 11.4 | 0 |  |
| lang_given_religion | E | 2.02 | 90.00 | 10.9 | 0 |  |
| religion_given_gp | A | 1.41 | 6.52 | 11.4 | 0 |  |
| vote_given_gender | C | 1.34 | 4.05 | 7.4 | 0 |  |
| education_given_age_gender | E | 0.00 | 16.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier None)  max |z| = 0.79
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 37.1 | 35.4 | -1.70 | -0.79 | True |
| AITC | 35.54 | 36.2 | +0.66 | +0.31 | True |
| INC | 18.01 | 17.2 | -0.81 | -0.47 | True |
| CPI | 5.87 | 5.8 | -0.07 | -0.07 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | JeSM | vote_values=['JeSM'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | SUCI | vote_values=['SUCI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BSP | vote_values=['BSP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BMUP | vote_values=['BMUP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |