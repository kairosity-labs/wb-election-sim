"""
TCPD LokDhaba scraper — Ashoka Trivedi Centre for Political Data.

LokDhaba publishes the cleanest mirror of ECI Form-20 results across all
Indian Assembly + Lok Sabha elections. Its public API endpoints serve JSON.
We pull WB Assembly + LS results for the years used by this project
(2011, 2014, 2016, 2019, 2021, 2024) and write canonical CSVs.

API endpoints (verified Apr 2026):
  https://lokdhaba.ashoka.edu.in/api/elections/{electionType}/{stateName}/{year}
    where electionType in {AE, GE} and stateName e.g. West_Bengal

Output:
  data/lokdhaba/AE_West_Bengal_2021.csv
  data/lokdhaba/GE_West_Bengal_2019.csv
  ...
  data/lokdhaba/lokdhaba_long.csv  (all years stacked)

Schema columns (subset; LokDhaba returns 60+):
  ac_no, ac_name, year, election_type, candidate, party, party_alliance,
  votes, vote_share_pct, position, margin, turnout_pct, electors

Usage:
    python3 scripts/scrapers/scrape_lokdhaba.py --years 2014 2019 2021 2024
    python3 scripts/scrapers/scrape_lokdhaba.py --all
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from _common import ROOT, fetch

OUT_DIR = ROOT / "data" / "lokdhaba"
OUT_DIR.mkdir(parents=True, exist_ok=True)

API = "https://lokdhaba.ashoka.edu.in/api/elections/{etype}/{state}/{year}"

# (election_type, year) pairs relevant to this project
TARGETS = [
    ("AE", 2011), ("AE", 2016), ("AE", 2021), ("AE", 2026),
    ("GE", 2014), ("GE", 2019), ("GE", 2024),
]

# Columns we consider canonical; rest pass through into _raw_extra
CORE_COLS = [
    "Constituency_No", "Constituency_Name", "Year", "Election_Type",
    "Candidate", "Party", "Alliance", "Votes", "Vote_Share_Percentage",
    "Position", "Margin", "Turnout_Percentage", "Electors",
]


def fetch_year(etype: str, year: int) -> list[dict] | None:
    url = API.format(etype=etype, state="West_Bengal", year=year)
    try:
        text = fetch(url, source="lokdhaba", sleep=1.0)
    except Exception as e:
        print(f"  ! {etype} {year}: fetch failed: {e}")
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # LokDhaba sometimes wraps payload as {"data": [...]}
        try:
            wrap = json.loads(text)
            return wrap.get("data") if isinstance(wrap, dict) else None
        except Exception:
            print(f"  ! {etype} {year}: not JSON")
            return None


def write_year_csv(rows: list[dict], etype: str, year: int) -> Path:
    out = OUT_DIR / f"{etype}_West_Bengal_{year}.csv"
    if not rows:
        out.write_text("")
        return out
    cols = list({k for r in rows for k in r.keys()})
    cols.sort(key=lambda c: (CORE_COLS.index(c) if c in CORE_COLS else 999, c))
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return out


def emit_long(all_rows: list[dict]) -> None:
    if not all_rows:
        return
    out = OUT_DIR / "lokdhaba_long.csv"
    cols = ["election_type", "year", "ac_no", "ac_name", "candidate",
            "party", "alliance", "votes", "vote_share_pct", "position",
            "margin", "turnout_pct", "electors"]
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in all_rows:
            w.writerow({
                "election_type": r.get("Election_Type"),
                "year": r.get("Year"),
                "ac_no": r.get("Constituency_No"),
                "ac_name": r.get("Constituency_Name"),
                "candidate": r.get("Candidate"),
                "party": r.get("Party"),
                "alliance": r.get("Alliance"),
                "votes": r.get("Votes"),
                "vote_share_pct": r.get("Vote_Share_Percentage"),
                "position": r.get("Position"),
                "margin": r.get("Margin"),
                "turnout_pct": r.get("Turnout_Percentage"),
                "electors": r.get("Electors"),
            })


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--years", type=int, nargs="*")
    p.add_argument("--all", action="store_true")
    args = p.parse_args()

    if args.all:
        targets = TARGETS
    elif args.years:
        targets = [(et, y) for et, y in TARGETS if y in args.years]
    else:
        p.error("pass --all or --years 2019 2021")

    all_rows: list[dict] = []
    for etype, year in targets:
        print(f"[fetch] {etype} {year}")
        rows = fetch_year(etype, year)
        if not rows:
            continue
        # Ensure year+type are stamped on every row
        for r in rows:
            r.setdefault("Year", year)
            r.setdefault("Election_Type", etype)
        path = write_year_csv(rows, etype, year)
        all_rows.extend(rows)
        print(f"        wrote {len(rows)} rows → {path.name}")
    emit_long(all_rows)
    print(f"\nDone. {len(all_rows)} total rows across {len(targets)} (type, year) pairs.")


if __name__ == "__main__":
    main()
