# WB Election Simulation — 2026

Multi-agent simulation of the West Bengal 2026 Legislative Assembly elections (polling 23–29 April 2026, results 4 May 2026). Constituency-level persona generation grounded in Census 2011 demographics, ECI 2011/2016/2021 electoral history, NFHS-5 health indicators, and 2026 candidate affidavits.

## Where to look first

| File | What it is |
|---|---|
| [`STATUS.md`](STATUS.md) | Current state of all data layers, validation against state totals, and remaining gaps |
| [`SCHEMA_COVERAGE.md`](SCHEMA_COVERAGE.md) | The 17-field per-AC target schema and which source fills each field |
| [`DATA_SOURCES.md`](DATA_SOURCES.md) | Every data source with URLs, licenses, and access notes |
| [`data/master/wb_ac_master_v3.csv`](data/master/wb_ac_master_v3.csv) | **The ground-truth table — 294 ACs × 48 columns** |

## Quick stats

- **294/294** WB Assembly Constituencies covered for 2011, 2016, and 2021 election results
- **244/294** ACs have full Census 2011 demographics (50 urban ACs pending — see STATUS.md)
- 2016 winners: AITC 211, INC 44, CPM 26, BJP 3 (matches actuals)
- 2021 winners: AITC 215, BJP 76 (matches actuals)
- 129 of 294 seats (43.9%) changed hands 2016 → 2021

## Pipeline (reproducible)

All ETL is in [`scripts/`](scripts/):

```
scripts/parse_eci_reports.py        # parse 1962-2011 ECI Stat Report PDFs
scripts/parse_eci_2021_xlsx.py      # parse 2021 ECI XLSX (single-sheet)
scripts/parse_eci_multisheet.py     # parse 294-sheet 2021 XLSX (constituency-wise)
scripts/parse_eci_2016_xlsx.py      # parse 2016 ECI XLSX
scripts/build_crosswalk.py          # village→AC crosswalk (Harvard LS-2009)
scripts/build_master_table.py       # v1 — name-matched aggregation
scripts/build_master_v2.py          # v2 — SHRUG-weighted aggregation
scripts/build_master_v3.py          # v3 — joins 2011+2016+2021 + demographics  ← current
```

Re-run any step with `python3 scripts/<script>.py`.

## Re-acquiring data not in this repo

Files listed in `.gitignore` (the 333MB India PCA xlsx, SHRUG fragment-key CSVs, scanned SIR PDFs, etc.) are too large for GitHub. To rebuild from scratch see [`DATA_SOURCES.md`](DATA_SOURCES.md). Most reproducible routes:

1. **Census 2011 village PCA (333 MB):** [data.gov.in](https://www.data.gov.in/catalog/villagetown-wise-primary-census-abstract-2011-west-bengal) — register, download per-district XLSX, run `parse_eci_*.py` analogue
2. **SHRUG 2.1:** [devdatalab.org/shrug_download](https://www.devdatalab.org/shrug_download/) — click the CSV button on each module
3. **SIR 2026 rolls:** [voters.eci.gov.in](https://voters.eci.gov.in/download-eroll?stateCode=S25) — per-AC PDF download (CAPTCHA gated)
4. **Cloned upstream repos:** see `data/raw/` references in `STATUS.md`

## Layers

```
Layer 1 — Demographics      Census 2011 PCA + SHRUG AC-aggregation + NFHS-5
Layer 2 — Electoral         ECI 2011/2016/2021 + LokDhaba historical
Layer 3 — Candidates        MyNeta/ADR 2021 baseline + 2026 partial
Layer 4 — Live signals      SIR 2026 (post-deletion electorate), Phase 1 turnout
Layer 5 — News/issues       (planned) Bengali TV transcripts, salience scoring
```

## License & attribution

Election Commission of India data (ECI Statistical Reports) — public domain. SHRUG — CC-BY-NC-SA 4.0 (Development Data Lab). NFHS-5 — CC-BY 4.0 (IIPS / Pratap Vardhan repo). Census 2011 — Government of India, NDSAP. ADR/MyNeta — public domain. Internal pipeline code — TBD.
