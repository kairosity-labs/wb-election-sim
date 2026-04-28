# Methodology — 2021-Calibrated WB Assembly Constituencies

This document accompanies the per-AC `<NNN>_<slug>_2021.md` files and their derived CSVs. It records what shifts when re-calibrating to end-2021 from the 2019 baseline. Read [`methodology_2019.md`](methodology_2019.md) for the unchanged parts (tier taxonomy, schema rules, 16 marginal axes, 18 joint tables, validation gates).

## 1. Reading the calibrated file

The `_2021.md` artifact is **frozen at end-2021-state-of-knowledge** — written as if the year were end-2021 (after the May 2021 WB AE results were known) and we did not yet know:

- 2022 SSC scam exposure / Partha Chatterjee arrest (Jul 2022)
- 2023 panchayat elections / political violence
- 2024 LS results, CAA rules notification (Mar 2024)
- 2024 RG Kar protests (Aug 2024)
- 2025 SIR voter-roll revision
- 2026 AE candidate lists, polling

**Forbidden keywords (auto-checked by gate 5):** `2022, 2023, 2024, 2025, 2026, SSC scam, Partha Chatterjee, RG Kar, SIR, CAA notification, CAA rules`

The file MAY freely reference: 2019 LS, 2020 events (COVID-19, Cyclone Amphan, NRC protests), 2021 WB AE (results known by ~May 2021), Lakshmir Bhandar launch (Apr 2021), BSF 50km jurisdiction (Oct 2021), Thakurbari split (2020+), candidate profiles for 2021 AE.

## 2. What changes from the 2019 file

| Section | Shift |
|---|---|
| Title preamble | "Calibrated 2019" → "Calibrated 2021" |
| § B (population) | 8-year projection → 10-year projection from Census 2011 |
| § C marginals | Same 16 axes; values nudged for 2 more years of religion-differential growth, asset/media diffusion, etc. |
| § C.14 asset/media | Notable: smartphone +20-30pp from 2019 (post-COVID surge); TV saturated; banking via PMJDY further +5-10pp |
| § C.16 migration | Add Cyclone Amphan return migration (May 2020) where AC was affected; COVID return migration |
| § D joint tables | Same 18 tables; vote × demographics now anchor on 2021 AE result (D.15-D.18) |
| § E calibration target | **2021 AE result for the AC** (not 2019 LS) — ECI Form-20 / state archive |
| § F vote history | Adds 2019 LS AC-segment result as anchor (was the calibration target; now it's history) |
| § H validation anchors | Becomes 2024 LS AC-segment result (out-of-sample only) |

## 3. Calibration target

For each AC, the **2021 WB Assembly Election result** is the new ECI-tier-A calibration target:

- 2021 AE total electorate (ECI roll, tier A)
- 2021 AE valid votes per party (ECI archive, tier A)
- 2021 AE turnout (tier A)
- 2021 AE winning margin (tier A)

If precise ECI Form-20 not fetchable, use Wikipedia AE-2021 candidate-level result (tier A — sourced from ECI) or general election archive figures.

## 4. New events to incorporate (post-2019, pre-end-2021)

These events MAY appear in § F (vote history context) or § A (sub-unit notes) but only with a tier indicating they are 2020-2021 events known by end-2021:

- **2020 March-Aug**: COVID-19 lockdown; reverse migration; PMC-Bengal-Kerala return labour estimates
- **2020 May 20**: Cyclone Amphan landfall (24 Parganas, 2-Dinajpur most affected); ₹1L+ crore damage
- **2020-2021**: Lakshmir Bhandar conditional cash transfer launched April 2021 (women household heads, ₹500/₹1000 monthly)
- **2021 March-April**: WB Assembly Election campaign (Modi, Mamata rallies); CISF firing at Sitalkuchi (AC 5) Apr 10
- **2021 May 2**: AE results — TMC 213 / BJP 77 / others 4
- **2021 Oct 11**: BSF jurisdiction extended to 50km from Bangladesh border
- **2021 Oct 13-20**: Bangladesh temple attacks (Hindu refugee anxiety in border ACs)

## 5. Source list (additions to 2019 list)

- ECI 2021 WB Assembly Election archive: candidate-level results
- Wikipedia 2021 WB Assembly Election articles (per AC)
- WB CDWDSW Lakshmir Bhandar dashboard (penetration data, when available)
- NFHS-5 (2019-21) for asset/media diffusion update vs NFHS-4 (2015-16)

## 6. Validation gates

Same 5 gates as 2019. Use `kaisim/scripts/validate_calibrated_2019.py NNN` (gate logic is year-agnostic; only the freeze keyword list differs — adjust §1 above). Forbidden-keyword gate uses the list in §1 of this doc.

## 7. Reproducing v0

```bash
python3 kaisim/scripts/derive_calibrated_2021_csvs.py NNN  # one AC
python3 kaisim/scripts/derive_calibrated_2021_csvs.py --all  # every *_2021.md
```
