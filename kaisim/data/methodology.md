# Methodology — WB 2026 Constituency-Level Demographic Dataset

This document pairs with [`constituencies.csv`](constituencies.csv) and the per-AC profiles in [`../constituencies/`](../constituencies/). It defines the schema, the confidence-tier system, the source catalog, the imputation logic used when sources are sparser than the target granularity, and the known limitations the downstream SCM should be aware of.

State-level context lives in [`../DemographicParameters.md`](../DemographicParameters.md) — read that first; everything here is the constituency-level disaggregation of the same causal nodes.

---

## 1. Confidence tiers

Every data cell in `constituencies.csv` is paired with a `*_conf` column holding one of five tiers. The simulation should weight node certainty by `1 / var(tier)` (A high weight, E low).

| Tier | Definition | Typical sources |
|---|---|---|
| **A** | Direct AC / block hard data, canonical and primary. | Census 2011 AC tables (Religion C-01, SC C-08, ST C-09, Mother Tongue C-16, Workers B-series, Literacy); ECI 2026 electoral roll; Delimitation Commission 2008 order (reservation + AC↔block mapping). |
| **B** | State-govt or central-MIS dashboard, sub-AC granularity, aggregated up to AC via the Delimitation mapping. | SECC 2011 block-level BPL %; MGNREGA MIS district/block; Swasthya Sathi block/GP enrollment dashboard; Krishak Bandhu beneficiary rolls. |
| **C** | Published academic study or CSDS-Lokniti regional subsample. | CSDS-Lokniti 2021 WB post-poll; NFHS-5 district fact sheets; PLFS 2022-23; Sinharay (Matuas); ISAS-NUS 2024; Pew religion projections. |
| **D** | Journalistic estimate or party-internal leaked survey. | Anandabazar Patrika, Bartaman, The Hindu, ThePrint, Outlook, Business Standard, Deccan Herald, The Wire constituency profiles. |
| **E** | Modeled imputation (see §4). Anything derived without a direct per-AC source. | District caste share × within-district population weight; region-label stratification; OBC sub-group allocations. |

**Rule of thumb:** any cell whose value was *computed* rather than *looked up* is tier E, no matter how defensible the computation.

---

## 2. CSV schema

`constituencies.csv` is 294 rows × 125 columns, written by `scripts/bootstrap.py` from `data/raw/ac_list.csv`.

| Column group | Columns | Notes |
|---|---|---|
| **Identity** | `ac_no, ac_name, district, region_label, region_label_conf, reservation` | `ac_no` 1–294. `reservation` ∈ {GEN, SC, ST}. `region_label` is a tier-E coarse stratification (10 groups, see §3). |
| **Electorate** | `total_electors_2026, male_electors, female_electors, sir_deletion_count_est, sir_deletion_pct_est` | Post-SIR 2026 roll. Deletion counts derived from pre/post-SIR roll diff at AC granularity where ECI Form 7 audit reports exist; otherwise district-level deletion share × AC electorate weight (tier D/E). |
| **Religion** | `hindu_pct, muslim_pct, christian_pct, sarna_orp_pct, other_religion_pct` | Census 2011 C-01 rolled up to AC via Delimitation mapping (tier A). Sum = 100 ± 0.5. |
| **Caste — SC** | `sc_total_pct, namasudra_matua_pct_est, rajbanshi_pct_est, bagdi_pct_est, poundra_pct_est, other_sc_pct_est` | `sc_total_pct` is Census 2011 C-08 (tier A). Sub-groups (Namasudra/Matua, Rajbanshi, Bagdi, Poundra) are tier C/E — derived from state-level CPS/Mooknayak/Census SC-sub-caste tables × district SC composition proxies. |
| **Caste — ST** | `st_total_pct, santhal_pct_est, oraon_pct_est, munda_pct_est, bhumij_pct_est, other_st_pct_est` | `st_total_pct` tier A. Sub-groups tier C/E via Wikipedia "List of Scheduled Tribes in West Bengal" + Adibasikalyan Dept state-level shares × district ST composition. |
| **Caste — UC / OBC** | `uc_bhadralok_pct_est, obc_mahishya_pct_est, obc_sadgop_pct_est, obc_kurmi_pct_est, obc_teli_pct_est, obc_other_pct_est` | **All tier C/D/E** — no caste census since 1931 for non-SC/ST. Use academic estimates (Outlook bhadralok ~20%; Joshua Project Mahishya distribution; Kurmi concentration in Jangalmahal). |
| **Language** | `bengali_pct, hindi_pct, santhali_pct, urdu_pct, nepali_pct, rajbanshi_lang_pct, kurmali_pct, other_lang_pct` | Census 2011 C-16 Mother Tongue at district → AC weighting (tier A/B). Sum = 100 ± 0.5. |
| **Income / poverty** | `bpl_household_pct_secc, mgnrega_worker_share_pct, per_capita_income_band_est, agri_hh_pct, out_migrant_worker_pct_est` | SECC 2011 (tier B, block→AC); MGNREGA MIS (tier B); per-capita income band is a 5-bucket ordinal (tier D); out-migrant worker share from PLFS + Kerala/Maharashtra migrant surveys (tier C/D/E). |
| **Education** | `literacy_overall_pct, literacy_male_pct, literacy_female_pct, graduate_plus_pct_est, unemployed_educated_youth_est` | Census 2011 literacy at AC (tier A). Graduate+ and unemployed-educated are tier C/D from PLFS + NFHS-5 + SSC-scam-cohort journalism. |
| **Occupation** | `cultivator_pct, ag_labourer_pct, tea_worker_pct_est, fishworker_pct_est, industrial_pct_est, govt_employee_pct_est, informal_sector_pct_est` | Census 2011 B-series main-worker categories (tier A for cultivator, ag_labourer). Tea/fish/industrial/govt/informal are tier C/D from PLFS 2022-23 + sector reports (408 tea gardens, Dakshin Banga Matsyajibi Forum, MSME registry). |
| **Welfare schemes** | `lakshmir_bhandar_beneficiaries_est, krishak_bandhu_beneficiaries_est, swasthya_sathi_coverage_pct_est, khadya_sathi_coverage_pct_est, kanyashree_coverage_pct_est, old_age_widow_pension_est` | Swasthya Sathi + Kanyashree have district/block dashboards (tier B, aggregated to AC). Lakshmir Bhandar & old-age/widow pensions are published at state/district only — AC numbers are tier C/D/E estimates proportional to female-adult population. |
| **Provenance** | `sources_json` | A JSON array of `{field, url, tier, year, accessed}` per populated cell. Enables traceability from any value back to its authority. |

Every data column has a paired `<col>_conf` column. Identity columns (except `region_label`) do not have conf columns because they are definitional.

---

## 3. Region labels (tier E)

`region_label` is a modeled 10-group stratification mapping district → region. It is a *tier-E* column because regions in DemographicParameters.md §4 are not strict partitions of districts (e.g., "Matua belt" spans parts of N24P, Nadia, S24P; "tea garden belt" spans parts of Jalpaiguri, Alipurduar, Darjeeling). The simplified mapping (see `scripts/bootstrap.py:DISTRICT_REGION`):

| Region | Districts |
|---|---|
| North Bengal Hills | Darjeeling, Kalimpong |
| North Bengal Plains | Cooch Behar, Alipurduar, Jalpaiguri |
| Border / Muslim-majority North | Uttar Dinajpur, Dakshin Dinajpur, Malda, Murshidabad |
| Presidency / Matua Belt | Nadia, North 24 Parganas |
| Kolkata Metro | Kolkata, Howrah |
| Hooghly / Burdwan Rural | Hooghly, Purba Bardhaman, Birbhum |
| Burdwan Industrial | Paschim Bardhaman |
| South 24 Parganas / Sundarbans | South 24 Parganas |
| Purba Medinipur Coast | Purba Medinipur |
| Jangalmahal | Paschim Medinipur, Jhargram, Purulia, Bankura |

Downstream consumers (especially the SCM) should prefer district- or AC-level conditioning over region-label whenever available; region is a fallback stratum.

---

## 4. Imputation logic for sub-AC sources → AC granularity

Most central/state datasets are at block, GP, or district level, not AC level. We map them up to AC as follows:

1. **Block → AC (tier B):** The Delimitation Commission 2008 order (parsed by `scripts/parse_delimitation_wb.py` from `data/raw/pdfs/delimitation_order_2008.pdf`, pages 517-539) lists the exact CDB / Municipality / Notified Area components that make up each AC. The output `data/raw/delimitation_ac_components.csv` has 625 component rows across 294/294 ACs. For a block-level metric `m` (e.g., SECC BPL%, Swasthya Sathi enrollment, MGNREGA worker share), the AC value is the population-weighted average of the member blocks:

   ```
   AC_value = Σ_i ( m_block_i × pop_block_i ) / Σ_i pop_block_i
   ```

   where `pop_block_i` is Census 2011 block population. If an AC spans only *part* of a block (common in urban ACs), the area or household count within that block's portion is used; absent that, equal-split is used and the cell is downgraded to tier C.

2. **District → AC (tier E):** For metrics with only district granularity (Lakshmir Bhandar enrollment, old-age/widow pensions, Census 2011 Wikipedia district rollup), the AC value is the district value × `AC_pop / district_pop`, i.e., we assume uniform within-district distribution. This is crude — it captures cross-district variation (Murshidabad 66% Muslim vs Purba Medinipur 15%) but collapses within-district heterogeneity (Muslim-majority ACs within Hindu-majority districts look like the district average). Flagged tier E.

   `scripts/aggregate_census_district_to_ac.py` implements this for Census 2011 religion / SC-ST / literacy / language columns, producing `data/raw/census2011_wb_ac_district_rollup.csv`. The merger respects existing pilot-level tier-E values (pilot ACs with CDB-level imputation are not overwritten by district rollup) because `tier_beats(E, E) = False`.

3. **State-level share → AC (tier D/E):** For sub-caste shares (e.g., Rajbanshi % of SC, Mahishya % of OBC) where only state-level composition is published, we:
   - Use the state SC/ST/OBC shares from Census 2011 / Adibasikalyan / Joshua Project.
   - Qualitatively tilt shares by district per DemographicParameters.md (e.g., Rajbanshi heavily in Cooch Behar-Jalpaiguri-N Dinajpur; Matua heavily in Bangaon-Ranaghat-Nadia; Santhal heavily in Jangalmahal).
   - Result is tier E — downstream consumers should treat as a prior, not a measurement.

4. **SIR deletion district totals → AC (tier D/E):** Outlook, FreePressJournal etc. report SIR deletions by district (Murshidabad 7.48L, Malda 4.59L, etc.). We allocate to ACs proportional to pre-SIR AC electorate × a religion-weighted uplift factor for Muslim-majority ACs (since SIR deletions were disproportionately concentrated in Muslim-majority wards per the Free Press Journal analysis). This is an explicit model; downstream should treat as tier D.

All imputation steps are documented in the individual `scrape_*.py` and `build_constituencies_csv.py` scripts, plus in the per-AC MD profile's §8 (Sources & caveats) when the imputation is material.

---

## 5. Verification

`scripts/validate_csv.py` (runs before any merge) enforces:

| Check | Threshold | Action on fail |
|---|---|---|
| Row count = 294 | exact | stop, emit diff vs `ac_list.csv` |
| Column count matches `scripts/bootstrap.py:build_header()` | exact | stop |
| `sum(religion_pct)` per row | 100 ± 0.5 | warn, log AC |
| `sum(language_pct)` per row | 100 ± 0.5 | warn |
| `namasudra_matua_pct_est + rajbanshi_pct_est + bagdi_pct_est + poundra_pct_est + other_sc_pct_est ≈ sc_total_pct` | ±1 | warn |
| District roll-up of `literacy_overall_pct × total_electors` → district Census 2011 literacy | ±5% | warn, flag district for redo |
| Every populated cell has a non-null `*_conf` | exact | stop |
| Every populated cell has a `sources_json` entry referencing it | exact | warn |

External cross-references (Trivedi Centre / ECI Form 20 spot-checks) are done per pilot profile during Step 3 and documented in §8 of the respective MD file.

---

## 6. Known limitations

- **No caste census post-1931 for non-SC/ST castes.** Every OBC and UC number is an estimate. Do not report these as ground truth to end consumers.
- **SECC 2011 is 15 years old.** BPL thresholds and household composition have shifted, especially with WB's specific welfare-scheme rollout. Treat BPL% as structural poverty exposure, not current income.
- **Census 2011 is 15 years old.** Religion ratios have drifted (Muslim share grew faster than Hindu share 2001–11; extrapolation to 2026 is non-trivial). The raw Census 2011 numbers are what we store; any 2026 adjustment is a separate modeled column (not currently included — flag if SCM requests it).
- **Out-migrant worker counts are estimates.** WB's out-migration to Kerala/Maharashtra/Tamil Nadu is real and large (1–2M to Kerala alone per PMC/Springer), but per-AC attribution is inferred from PLFS + remittance surveys, not directly measured.
- **Swasthya Sathi enrollment at AC level requires block→AC aggregation.** The state dashboard exposes GP and block. When blocks straddle ACs, we apply population weighting; when GPs do, we use household count weighting from SECC.
- **Lakshmir Bhandar has no public AC-level dashboard.** Beneficiary counts are state/district press releases. AC-level numbers are estimates proportional to female-adult population from Census 2011 — tier C at best.
- **2026 electorate (`total_electors_2026`) reflects post-SIR roll.** SIR concluded shortly before Phase 1 (23 April 2026); the roll used here is the final roll after supplementary additions. Some ~33 lakh adjudication-pending voters may or may not be restored by Phase 2 — check `sources_json` for the scrape date.

---

## 7. Reproducing

From `/home/ubuntu/kaisim`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/requirements.txt

# Step 1: scaffold (already done; re-run is idempotent)
python3 scripts/bootstrap.py

# Step 2: source ingestion (scripts added incrementally)
python3 scripts/download_census2011.py
python3 scripts/parse_delimitation_pdf.py
python3 scripts/scrape_eci_roll.py
python3 scripts/scrape_secc2011.py
python3 scripts/scrape_mgnrega.py
python3 scripts/scrape_swasthya_sathi.py
# ... one script per source, each writing to data/raw/*.csv

# Step 4 (Pass A): breadth auto-fill
python3 scripts/build_constituencies_csv.py

# Validate
python3 scripts/validate_csv.py
```

---

## 8. Source catalog

See [`sources.md`](sources.md) for the full URL catalog with access dates.
