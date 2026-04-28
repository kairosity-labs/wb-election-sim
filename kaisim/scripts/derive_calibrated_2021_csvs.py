#!/usr/bin/env python3
"""
derive_calibrated_2021_csvs.py
Parse a 2021-calibrated MD's tables and emit companion CSVs.

The MD is the canonical source of truth; CSVs are derived. Re-run after any
MD edit to keep CSVs in sync.

Output structure (per AC NN):
  csv/NN_marginals.csv                — all 16 marginal axes (long format)
  csv/NN_joint_<id>.csv               — one CSV per joint table (wide format)
  csv/NN_vote_<axis>_2021.csv         — vote × demographic joints
  csv/NN_calibration_target_2021.csv  — section E aggregate

Run:
    python3 scripts/derive_calibrated_2021_csvs.py 095        # one AC
    python3 scripts/derive_calibrated_2021_csvs.py --all      # every *_2021.md
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONSTS_DIR = ROOT.parent / "constituency_data" / "constituencies"


def _ac_2021_dir(ac: str) -> Path:
    """Return constituency_data/constituencies/{ac}_*/2021 for a 3-digit AC id."""
    matches = sorted(CONSTS_DIR.glob(f"{ac}_*"))
    if not matches:
        raise FileNotFoundError(f"No constituency folder for AC {ac!r}")
    return matches[0] / "2021"


# Section blueprint. The structure is identical across all 2021-calibrated ACs;
# only the AC-number prefix on the CSV filename changes.
MARGINAL_AXES: dict[str, str] = {
    "C.1":  "religion",
    "C.2":  "caste",
    "C.3":  "age_cohort",
    "C.4":  "gender",
    "C.5":  "mother_tongue",
    "C.6":  "education",
    "C.7":  "workforce_status",
    "C.8":  "occupation",
    "C.9":  "class_of_worker",
    "C.10": "economic_status",
    "C.11": "gp_location",
    "C.12": "household_composition",
    "C.13": "marital_status",
    "C.14": "asset_media",
    "C.15": "amenities",
    "C.16": "migration",
}
JOINT_FILE_STEMS: dict[str, str] = {
    "D.1":  "joint_religion_lang",
    "D.2":  "joint_religion_caste",
    "D.3":  "joint_religion_migration",
    "D.4":  "joint_religion_asset",
    "D.5":  "joint_caste_education",
    "D.6":  "joint_age_gender_education",
    "D.7":  "joint_marital_age_gender",
    "D.8":  "joint_occupation_asset",
    "D.9":  "joint_education_workforce",
    "D.10": "joint_asset_bilingualism",
    "D.11": "joint_gp_religion",
    "D.12": "joint_gp_caste",
    "D.13": "joint_gp_asset",
    "D.14": "joint_gp_amenities",
    "D.15": "vote_religion_2021",
    "D.16": "vote_caste_2021",
    "D.17": "vote_gender_2021",
    "D.18": "vote_welfare_2021",
}


def build_sections(ac: str) -> dict[str, dict]:
    """Return SECTIONS dict with AC-prefixed filenames."""
    sections: dict[str, dict] = {}
    for sid, axis in MARGINAL_AXES.items():
        sections[sid] = {"csv": None, "kind": "marginal_long", "axis": axis}
    for sid, stem in JOINT_FILE_STEMS.items():
        sections[sid] = {"csv": f"{ac}_{stem}.csv", "kind": "wide"}
    return sections

META_ROW_MARKERS = ("sum", "note", "marginal recovery",
                    "population-wide", "(these are independent")

# Substrings (lowercased) in the first cell that mark a row as meta —
# i.e. an ECI Form-20 totals/electors/turnout/margin row, not a real datum.
META_ROW_SUBSTRINGS = (
    "marginal recovery", "population-wide", "(these are independent",
    "total polled", "total valid", "total votes", "total electors",
    "registered electors", "turnout", "lead over", "margin over",
    "bjp lead", "aitc margin", "bjp margin", "tmc margin",
)


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
    if first in {"sum", "note", ""}:
        return True
    for marker in META_ROW_SUBSTRINGS:
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


def write_marginal_csv(records: list[dict], ac: str, out_dir: Path) -> Path:
    """Write the consolidated long-format marginals CSV."""
    out = out_dir / f"{ac}_marginals.csv"
    fieldnames = ["axis", "category", "pct", "tier", "source", "is_subgroup"]
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(records)
    return out


def write_wide_csv(name: str, header: list[str], rows: list[list[str]], out_dir: Path) -> Path:
    out = out_dir / name
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    return out


def parse_calibration_target(md: str) -> tuple[list[str], list[list[str]]]:
    """Section E: AC segment estimate table (always the LAST table in §E).
    Returns (header, rows). Header is the verbatim MD column names."""
    e_match = re.search(r"^##\s+E\.", md, re.MULTILINE)
    if not e_match:
        return [], []
    section_text = md[e_match.end():]
    next_h2 = re.search(r"^##\s+", section_text, re.MULTILINE)
    if next_h2:
        section_text = section_text[:next_h2.start()]
    tables: list[list[str]] = []
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
        return [], []
    target = tables[-1]
    if len(target) < 3:
        return [], []
    header = [strip_md(c) for c in target[0].strip().strip("|").split("|")]
    rows = []
    for line in target[2:]:
        cells = [strip_md(c) for c in line.strip().strip("|").split("|")]
        if is_meta_row(cells):
            continue
        rows.append(cells)
    return header, rows


def find_md_for_ac(ac: str) -> Path:
    """Find <ac>_*_2021.md inside constituency_data/constituencies/{ac}_*/2021/."""
    ac_2021 = _ac_2021_dir(ac)
    matches = sorted(ac_2021.glob(f"{ac}_*_2021.md"))
    if not matches:
        raise FileNotFoundError(
            f"No MD file matching '{ac}_*_2021.md' in {ac_2021}")
    if len(matches) > 1:
        raise ValueError(f"Multiple MDs match '{ac}_*_2021.md': {matches}")
    return matches[0]


def derive_one(ac: str, verbose: bool = True) -> dict:
    """Parse the AC's MD and write its CSVs. Return a per-AC summary."""
    out_dir = _ac_2021_dir(ac) / "csv"
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = find_md_for_ac(ac)
    md = md_path.read_text()
    sections = build_sections(ac)

    summary = {
        "ac": ac,
        "md": md_path.name,
        "missing_sections": [],
        "marginal_axes_written": [],
        "joint_csvs_written": [],
        "calibration_target_rows": 0,
    }

    marginal_records: list[dict] = []

    for section_id, cfg in sections.items():
        parsed = parse_md_table(md, section_id)
        if not parsed:
            summary["missing_sections"].append(section_id)
            continue
        header, rows = parsed
        if cfg["kind"] == "marginal_long":
            axis = cfg["axis"]
            for r in rows:
                if len(r) < 4:
                    continue
                category_raw = r[0].strip()
                is_subgroup = "yes" if category_raw.startswith("└") else "no"
                category = category_raw.lstrip("└ ").strip()
                marginal_records.append({
                    "axis": axis,
                    "category": category,
                    "pct": r[1],
                    "tier": r[2],
                    "source": r[3] if len(r) > 3 else "",
                    "is_subgroup": is_subgroup,
                })
            if axis not in summary["marginal_axes_written"]:
                summary["marginal_axes_written"].append(axis)
        elif cfg["kind"] == "wide":
            out = write_wide_csv(cfg["csv"], header, rows, out_dir)
            summary["joint_csvs_written"].append(out.name)

    if marginal_records:
        marg_path = write_marginal_csv(marginal_records, ac, out_dir)
        if verbose:
            print(f"  wrote {marg_path.name} ({len(marginal_records)} rows)")

    cal_header, cal_rows = parse_calibration_target(md)
    if cal_rows and cal_header:
        cal_out = out_dir / f"{ac}_calibration_target_2021.csv"
        with cal_out.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(cal_header)        # preserve verbatim per-AC schema
            for r in cal_rows:
                # Pad/truncate to header length for clean CSV.
                if len(r) < len(cal_header):
                    r = r + [""] * (len(cal_header) - len(r))
                w.writerow(r[:len(cal_header)])
        summary["calibration_target_rows"] = len(cal_rows)
        if verbose:
            print(f"  wrote {cal_out.name} ({len(cal_rows)} rows)")

    if verbose:
        print(f"  wrote {len(summary['joint_csvs_written'])} joint CSVs")
        if summary["missing_sections"]:
            print(f"  ⚠ missing sections: {summary['missing_sections']}")

    return summary


def discover_acs() -> list[str]:
    """Return all 3-digit AC numbers found as <NNN>_*_2021.md in constituency_data/."""
    out = []
    for p in sorted(CONSTS_DIR.glob("*/2021/*_2021.md")):
        m = re.match(r"^(\d{3})_", p.name)
        if m:
            out.append(m.group(1))
    return out


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("ac", nargs="?", default=None,
                    help="3-digit AC number (e.g. 095). Omit with --all.")
    p.add_argument("--all", action="store_true",
                    help="Derive for every <NNN>_*_2021.md in calibrated_2021/")
    args = p.parse_args()

    if args.all:
        targets = discover_acs()
    elif args.ac:
        targets = [args.ac.zfill(3)]
    else:
        p.error("provide an AC number or --all")
        return 2

    print(f"Deriving CSVs for {len(targets)} AC(s): {targets}")
    summaries = []
    for ac in targets:
        print(f"\n=== AC {ac} ===")
        try:
            s = derive_one(ac)
            summaries.append(s)
        except (FileNotFoundError, ValueError) as e:
            print(f"  ✗ {e}")
            summaries.append({"ac": ac, "error": str(e)})

    print("\n" + "=" * 72)
    print(f"SUMMARY ({len(summaries)} ACs)")
    print("=" * 72)
    for s in summaries:
        if "error" in s:
            print(f"  AC {s['ac']:>3}: ✗ {s['error']}")
            continue
        miss = len(s["missing_sections"])
        marg = len(s["marginal_axes_written"])
        joint = len(s["joint_csvs_written"])
        flag = "✓" if miss == 0 else "⚠"
        print(f"  AC {s['ac']:>3} {flag} marginals={marg}/16 "
              f"joints={joint}/18 cal_rows={s['calibration_target_rows']}"
              + (f"  missing={s['missing_sections']}" if miss else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
