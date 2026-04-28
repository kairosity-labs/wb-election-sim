# Source registry — WB constituency calibration

Empirical audit of source citations across the first 30 calibrated 2019 AC files
([constituency_data/constituencies/](../../constituency_data/constituencies/))
revealed that ~85% of every Tier-A/B/C cell traces back to one of seven
canonical sources. This registry maps each source to the scraper that fetches
it, so future ACs (264 left) don't require manual web search.

## When to use which scraper

| Source family | Coverage in first 30 ACs | Scraper | What it produces |
|---|---|---|---|
| Census 2011 PCA, religion, SC/ST, literacy | 30/30 | already in [data/shrug/](../../data/shrug/) + [data/census_2011/](../../data/census_2011/) | block + village PCA |
| ECI / Delimitation 2008 metadata | 30/30 | one-time, in [data/master/](../../data/master/) | AC↔district↔LS map |
| Wikipedia AC + LS infoboxes (history) | 30/30 | [`scrape_wikipedia_ac.py`](scrape_wikipedia_ac.py) | per-AC JSON + history CSV |
| TCPD LokDhaba (clean ECI mirror) | 30/30 (substitutes 4 sources) | [`scrape_lokdhaba.py`](scrape_lokdhaba.py) | per-year AC results CSVs |
| ECI Form-20 PS-level results | 16/30 | [`scrape_ceo_wb_form20.py`](scrape_ceo_wb_form20.py) | per-AC PS results CSV |
| NFHS-5 district fact sheets | 30/30 | [`scrape_nfhs_district.py`](scrape_nfhs_district.py) | district × indicator long CSV |
| CSDS-Lokniti 2019 NES | 29/30 | manual (`data/csds_lokniti_2019.csv` — ship with repo) | state cross-tabs (one-time) |

## Run order for a new AC

```bash
# 1) Already done once for the project — skip if files exist:
python3 scripts/scrapers/scrape_lokdhaba.py --all
python3 scripts/scrapers/scrape_nfhs_district.py --all
python3 scripts/scrapers/scrape_wikipedia_ac.py --all

# 2) Per AC, fetch the PS-level Form-20 (most expensive):
python3 scripts/scrapers/scrape_ceo_wb_form20.py --election ge2019 --ac 95

# 3) Now the per-AC MD author has zero web search to do —
#    the relevant rows are all in data/{lokdhaba,wikipedia,nfhs_5,ceo_wb_form20}/.
```

## Cost / token savings

The first 30 ACs were authored by reading ~6 web sources per AC and summarizing
them into the MD. With these scrapers the data is pre-fetched into typed CSVs
and the MD author only does **synthesis** (joining + tier-tagging), not
**discovery**. Empirically this collapses the per-AC token budget from
~80k input tokens (search + read) to ~12k (CSV reads).

## Adding a new source family

1. Add a row to the table above.
2. Drop a new `scrape_<source>.py` next to the existing scrapers, following the
   shape of [`_common.py`](_common.py): cache raw fetches under
   `data/raw/scrapers/<source>/`, write parsed CSVs under `data/<source>/`.
3. Update [`structured-data-layer/SKILL.md`](../../kaisim/pipeline/skills/structured-data-layer/SKILL.md)
   §Procedure to add the new scraper to the run-order list.

## Limitations / TODO

- **LokDhaba endpoint** — verify exact API path; the `/api/elections/...`
  pattern is what the SPA uses internally but may need an auth header for
  some queries. If empty, fall back to their CSV download endpoint.
- **CEO WB Form-20** — URL pattern varies year-to-year; pass
  `--url-template` after one manual confirmation per election.
- **NFHS-5** — fact-sheet PDF schema changes between districts; the parser is
  permissive but expect ~5% indicator-extraction noise. Spot-check before
  promoting to Tier-A.
- **DCHB Part-A (GP-level Census)** — scraper not built; censusindia.gov.in
  blocks programmatic access. Manual one-time fetch + parse remains the path.
