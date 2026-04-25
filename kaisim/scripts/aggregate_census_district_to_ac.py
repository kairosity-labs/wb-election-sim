#!/usr/bin/env python3
"""
aggregate_census_district_to_ac.py
Tier-B district → AC rollup for Census 2011 demographic columns.

Input:
  data/raw/census2011_wb_district.csv (23 rows, one per WB district)
  data/raw/ac_list.csv                (294 rows)

Strategy (tier B):
  Every AC inherits its district's Census 2011 percentages. This is the
  coarsest defensible rollup — it captures cross-district variation
  (Murshidabad 66% Muslim vs Purba Medinipur 15% Muslim) but collapses
  within-district heterogeneity. The methodology notes this trade-off in §4.

  A future tier-A pass using Delimitation AC↔CDB mapping +
  CDB-level Census data would replace this for within-district variation.

Output:
  data/raw/census2011_wb_ac_district_rollup.csv
  Columns: ac_no + all percentage columns from the district CSV
  Tier: B for every cell.

Run:
    python3 scripts/aggregate_census_district_to_ac.py
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AC_LIST = ROOT / "data" / "raw" / "ac_list.csv"
CENSUS_DISTRICT = ROOT / "data" / "raw" / "census2011_wb_district.csv"
OUT = ROOT / "data" / "raw" / "census2011_wb_ac_district_rollup.csv"


def main() -> None:
    with AC_LIST.open() as f:
        ac_list = list(csv.DictReader(f))

    with CENSUS_DISTRICT.open() as f:
        reader = csv.DictReader(f)
        district_data = {row["district"]: row for row in reader}

    # Output columns = ac_no + ac_name + district + (all district columns
    # except "district" which is the join key).
    census_cols = [
        c for c in next(iter(district_data.values())).keys() if c != "district"
    ]
    out_cols = ["ac_no", "ac_name", "district"] + census_cols

    rows: list[dict] = []
    missing_districts: set[str] = set()
    for ac in ac_list:
        district = ac["district"]
        d = district_data.get(district)
        if not d:
            missing_districts.add(district)
            continue
        row = {"ac_no": ac["ac_no"], "ac_name": ac["ac_name"], "district": district}
        for c in census_cols:
            row[c] = d.get(c, "")
        rows.append(row)

    if missing_districts:
        raise SystemExit(f"Districts in ac_list not found in Census CSV: {missing_districts}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=out_cols)
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {OUT} — {len(rows)} rows (294 expected)")
    # Sanity check: show AC 95
    for r in rows:
        if r["ac_no"] == "95":
            print(f"\n--- AC 95 rollup ---")
            for c in ["district", "hindu_pct", "muslim_pct", "sc_pct", "literacy_rate_overall_pct", "bengali_pct"]:
                print(f"  {c:35s} = {r[c]}")
            break


if __name__ == "__main__":
    main()
