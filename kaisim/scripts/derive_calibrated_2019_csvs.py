#!/usr/bin/env python3
"""
derive_calibrated_2019_csvs.py
Parse the MD tables in `data/calibrated_2019/095_bangaon_uttar_2019.md` and
emit companion CSVs to `data/calibrated_2019/csv/`.

The MD is the canonical source of truth; CSVs are derived. Re-run after any
MD edit to keep CSVs in sync.

Output structure:
  csv/095_marginals.csv         — all 15 marginal axes in long format:
                                  axis, category, pct, tier, source
  csv/095_joint_<id>.csv        — one CSV per joint table:
                                  for D.1-style 2-axis tables — wide format
                                  for vote-tables — wide format with party cols
  csv/095_calibration_target_2019.csv — section E aggregate

Run:
    python3 scripts/derive_calibrated_2019_csvs.py
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD_PATH = ROOT / "data" / "calibrated_2019" / "095_bangaon_uttar_2019.md"
OUT_DIR = ROOT / "data" / "calibrated_2019" / "csv"


# Map section header → (csv filename, kind, axis labels)
# kind ∈ {"marginal_long", "wide", "skip"}
# For marginals: rows go into one big long CSV.
# For joints: each gets its own wide CSV (one row per category of axis_x).
SECTIONS: dict[str, dict] = {
    # Marginals — written into one long-format CSV
    "C.1": {"csv": None, "kind": "marginal_long", "axis": "religion"},
    "C.2": {"csv": None, "kind": "marginal_long", "axis": "caste"},
    "C.3": {"csv": None, "kind": "marginal_long", "axis": "age_cohort"},
    "C.4": {"csv": None, "kind": "marginal_long", "axis": "gender"},
    "C.5": {"csv": None, "kind": "marginal_long", "axis": "mother_tongue"},
    "C.6": {"csv": None, "kind": "marginal_long", "axis": "education"},
    "C.7": {"csv": None, "kind": "marginal_long", "axis": "workforce_status"},
    "C.8": {"csv": None, "kind": "marginal_long", "axis": "occupation"},
    "C.9": {"csv": None, "kind": "marginal_long", "axis": "class_of_worker"},
    "C.10": {"csv": None, "kind": "marginal_long", "axis": "economic_status"},
    "C.11": {"csv": None, "kind": "marginal_long", "axis": "gp_location"},
    "C.12": {"csv": None, "kind": "marginal_long", "axis": "household_composition"},
    "C.13": {"csv": None, "kind": "marginal_long", "axis": "marital_status"},
    "C.14": {"csv": None, "kind": "marginal_long", "axis": "asset_media"},
    "C.15": {"csv": None, "kind": "marginal_long", "axis": "amenities"},
    "C.16": {"csv": None, "kind": "marginal_long", "axis": "migration"},
    # Joints — each gets its own CSV (wide format preserved as parsed)
    "D.1": {"csv": "095_joint_religion_lang.csv", "kind": "wide"},
    "D.2": {"csv": "095_joint_religion_caste.csv", "kind": "wide"},
    "D.3": {"csv": "095_joint_religion_migration.csv", "kind": "wide"},
    "D.4": {"csv": "095_joint_religion_asset.csv", "kind": "wide"},
    "D.5": {"csv": "095_joint_caste_education.csv", "kind": "wide"},
    "D.6": {"csv": "095_joint_age_gender_education.csv", "kind": "wide"},
    "D.7": {"csv": "095_joint_marital_age_gender.csv", "kind": "wide"},
    "D.8": {"csv": "095_joint_occupation_asset.csv", "kind": "wide"},
    "D.9": {"csv": "095_joint_education_workforce.csv", "kind": "wide"},
    "D.10": {"csv": "095_joint_asset_bilingualism.csv", "kind": "wide"},
    "D.11": {"csv": "095_joint_gp_religion.csv", "kind": "wide"},
    "D.12": {"csv": "095_joint_gp_caste.csv", "kind": "wide"},
    "D.13": {"csv": "095_joint_gp_asset.csv", "kind": "wide"},
    "D.14": {"csv": "095_joint_gp_amenities.csv", "kind": "wide"},
    "D.15": {"csv": "095_vote_religion_2019.csv", "kind": "wide"},
    "D.16": {"csv": "095_vote_caste_2019.csv", "kind": "wide"},
    "D.17": {"csv": "095_vote_gender_2019.csv", "kind": "wide"},
    "D.18": {"csv": "095_vote_welfare_2019.csv", "kind": "wide"},
}

META_ROW_MARKERS = ("sum", "note", "marginal recovery",
                    "population-wide", "(these are independent")


def strip_md(text: str) -> str:
    """Remove markdown bold/italic and surrounding spaces from a cell."""
    if text is None:
        return ""
    s = text.strip()
    s = re.sub(r"\*\*(.*?)\*\*", r"\1", s)
    s = re.sub(r"\*(.*?)\*", r"\1", s)
    s = s.strip()
    return s


def is_meta_row(cells: list[str]) -> bool:
    if not cells:
        return True
    first = cells[0].lower().strip()
    # Whole-cell exact match for "sum"/"note" (these are stand-alone meta rows)
    if first in {"sum", "note", ""}:
        return True
    # Substring match for the longer markers
    for marker in ("marginal recovery", "population-wide", "(these are independent"):
        if marker in first:
            return True
    return False


def parse_md_table(md: str, section_id: str) -> tuple[list[str], list[list[str]]] | None:
    """Find the heading `### {section_id} ...` and return (header_cells, rows).
    Stops at the next table or the next heading."""
    # Match the heading line (starts with ### then section_id)
    pattern = rf"^###\s+{re.escape(section_id)}\b.*?$"
    matches = list(re.finditer(pattern, md, re.MULTILINE))
    if not matches:
        return None
    start = matches[0].end()
    # Walk lines until we hit a `|`-table; collect contiguous `|` lines.
    lines = md[start:].split("\n")
    table_lines: list[str] = []
    in_table = False
    for line in lines:
        if line.lstrip().startswith("|"):
            in_table = True
            table_lines.append(line)
        elif in_table:
            break
    if len(table_lines) < 3:
        return None
    # First is header, second is separator, rest are data.
    header_cells = [strip_md(c) for c in table_lines[0].strip().strip("|").split("|")]
    rows: list[list[str]] = []
    for line in table_lines[2:]:
        cells = [strip_md(c) for c in line.strip().strip("|").split("|")]
        if is_meta_row(cells):
            continue
        rows.append(cells)
    return header_cells, rows


def write_marginal_csv(records: list[dict]) -> Path:
    """Write the consolidated long-format marginals CSV."""
    out = OUT_DIR / "095_marginals.csv"
    fieldnames = ["axis", "category", "pct", "tier", "source", "is_subgroup"]
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(records)
    return out


def write_wide_csv(name: str, header: list[str], rows: list[list[str]]) -> Path:
    out = OUT_DIR / name
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    return out


def parse_calibration_target(md: str) -> list[list[str]]:
    """Section E: AC 95 segment estimate table."""
    # Find the AC 95 segment table specifically (the second table in section E,
    # has header containing "AC 95 segment 2019 %").
    e_match = re.search(r"^##\s+E\.", md, re.MULTILINE)
    if not e_match:
        return []
    section_text = md[e_match.end():]
    # Stop at next H2.
    next_h2 = re.search(r"^##\s+", section_text, re.MULTILINE)
    if next_h2:
        section_text = section_text[:next_h2.start()]
    # Extract all tables; keep the second (segment estimate).
    tables = []
    lines = section_text.split("\n")
    current_table: list[str] = []
    for line in lines:
        if line.lstrip().startswith("|"):
            current_table.append(line)
        else:
            if current_table:
                tables.append(current_table)
                current_table = []
    if current_table:
        tables.append(current_table)
    if not tables:
        return []
    # Use the LAST table (AC 95 segment estimate) — that's the calibration target.
    target = tables[-1]
    if len(target) < 3:
        return []
    rows = []
    for line in target[2:]:
        cells = [strip_md(c) for c in line.strip().strip("|").split("|")]
        if is_meta_row(cells):
            continue
        rows.append(cells)
    return rows


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    md = MD_PATH.read_text()

    marginal_records: list[dict] = []
    joint_csvs_written = []

    for section_id, cfg in SECTIONS.items():
        parsed = parse_md_table(md, section_id)
        if not parsed:
            print(f"WARN: section {section_id} table not found")
            continue
        header, rows = parsed
        if cfg["kind"] == "marginal_long":
            axis = cfg["axis"]
            for r in rows:
                if len(r) < 4:
                    continue
                # Detect sub-row indent ("└" prefix in MD) before stripping it.
                category_raw = r[0].strip()
                is_subgroup = "yes" if category_raw.startswith("└") else "no"
                category = category_raw.lstrip("└ ").strip()
                pct = r[1]
                tier = r[2]
                source = r[3] if len(r) > 3 else ""
                marginal_records.append({
                    "axis": axis,
                    "category": category,
                    "pct": pct,
                    "tier": tier,
                    "source": source,
                    "is_subgroup": is_subgroup,
                })
        elif cfg["kind"] == "wide":
            out = write_wide_csv(cfg["csv"], header, rows)
            joint_csvs_written.append(out.name)

    if marginal_records:
        marg_path = write_marginal_csv(marginal_records)
        print(f"Wrote {marg_path.name} ({len(marginal_records)} rows)")

    # Calibration target
    cal_rows = parse_calibration_target(md)
    if cal_rows:
        cal_out = OUT_DIR / "095_calibration_target_2019.csv"
        with cal_out.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["party", "ac95_segment_pct_estimate", "tier", "note"])
            for r in cal_rows:
                if len(r) >= 4:
                    w.writerow(r[:4])
        print(f"Wrote {cal_out.name} ({len(cal_rows)} rows)")

    print(f"Wrote {len(joint_csvs_written)} joint CSVs:")
    for n in joint_csvs_written:
        print(f"  - {n}")


if __name__ == "__main__":
    main()
