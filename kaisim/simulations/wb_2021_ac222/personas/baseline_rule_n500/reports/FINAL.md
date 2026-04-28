# Verifier report (n=500)

- composite chi-square: **684.59** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.3  · max joint cell |z|: 4.49  · aggregate vote max |z|: 1.31
- max axis gap: 5.6 pp  · max joint cell gap: 93.0 pp  · aggregate max gap: 2.91 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| marital_status | E | 3.30 | 4.00 | 12.8 | 1 |
| gp_location | E | 2.54 | 5.60 | 11.6 | 1 |
| caste | E | 2.51 | 4.72 | 15.5 | 1 |
| amenities | C | 2.48 | 3.60 | 7.9 | 0 |
| religion | E | 2.22 | 3.10 | 9.5 | 0 |
| mother_tongue | A | 2.00 | 2.90 | 10.9 | 0 |
| asset_media | C | 1.85 | 2.40 | 7.4 | 0 |
| education | E | 1.80 | 2.80 | 8.7 | 0 |
| age_cohort | E | 1.78 | 2.36 | 8.3 | 0 |
| workforce_status | E | 1.69 | 3.60 | 4.8 | 0 |
| migration | D | 1.66 | 1.20 | 6.3 | 0 |
| economic_status | E | 1.59 | 2.60 | 4.4 | 0 |
| occupation | E | 1.43 | 2.32 | 6.8 | 0 |
| household_composition | E | 1.19 | 1.60 | 1.7 | 0 |
| class_of_worker | E | 0.96 | 3.09 | 3.1 | 0 |
| gender | A | 0.55 | 1.24 | 0.6 | 0 |
| tribal_subgroup | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| marital_status | Widowed | 8.0 | 4.0 | -4.00 | -3.30 |
| gp_location | U3_Binpur_I_CD_Block | 57.8 | 52.2 | -5.60 | -2.54 |
| caste | ST_total | 22.92 | 18.2 | -4.72 | -2.51 |
| amenities | Electricity | 88.0 | 84.4 | -3.60 | -2.48 |
| religion | Sarna_ORP | 10.9 | 7.8 | -3.10 | -2.22 |
| gp_location | U1_Jhargram_Municipality | 22.8 | 26.6 | +3.80 | +2.03 |
| mother_tongue | Other | 0.2 | 0.6 | +0.40 | +2.00 |
| caste | Other_Hindu_middle_castes | 34.0 | 38.0 | +4.00 | +1.89 |
| asset_media | Computer | 5.0 | 6.8 | +1.80 | +1.85 |
| education | Secondary | 14.0 | 16.8 | +2.80 | +1.80 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_gp | A/E | 4.49 | 12.54 | 81.6 | 7 |  |
| asset_given_occupation | D | 3.95 | 50.00 | 59.3 | 3 |  |
| workforce_given_education | E | 2.70 | 14.00 | 38.3 | 1 |  |
| asset_given_gp | C | 2.68 | 8.31 | 23.6 | 1 |  |
| migration_given_religion | E | 2.25 | 28.33 | 26.1 | 0 |  |
| vote_given_religion | E | 2.18 | 50.00 | 33.3 | 0 |  |
| religion_given_gp | A | 1.93 | 4.41 | 10.9 | 0 |  |
| amenities_given_gp | C | 1.88 | 5.92 | 13.5 | 0 |  |
| asset_given_religion | None | 1.87 | 31.67 | 18.1 | 0 |  |
| lang_given_religion | E | 1.83 | 40.00 | 13.3 | 0 |  |
| vote_given_caste | C | 1.80 | 17.67 | 20.5 | 0 |  |
| education_given_caste | E | 1.63 | 13.89 | 21.5 | 0 |  |
| vote_given_gender | D | 1.54 | 4.89 | 12.1 | 0 |  |
| caste_given_religion | E | 1.47 | 5.44 | 6.6 | 0 |  |
| education_given_age_gender | E | 0.00 | 10.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here; higher female mortality risk) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.31
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 44.49 | 47.4 | +2.91 | +1.31 | True |
| AITC | 43.62 | 43.0 | -0.62 | -0.28 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | CPI | vote_values=['CPI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | JKP | vote_values=['JKP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | INC | vote_values=['INC'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BSP | vote_values=['BSP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | AKBJHP | vote_values=['AKBJHP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | SUCI | vote_values=['SUCI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |