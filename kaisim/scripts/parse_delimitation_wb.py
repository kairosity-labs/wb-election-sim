#!/usr/bin/env python3
"""
parse_delimitation_wb.py
Extract WB AC↔component (CDB/Municipality/Notified-Area) mapping from the
Delimitation Commission of India 2008 Order.

Source PDF: data/raw/pdfs/delimitation_order_2008.pdf
WB section: Schedule XXX, pages 517-539 (Table A — Assembly Constituencies).

Identity (ac_no / ac_name / district / reservation) is taken from the canonical
ac_list.csv — this script only extracts the component mapping.

Output: data/raw/delimitation_ac_components.csv
  Columns: ac_no, ac_name, district, reservation,
           component_type, component_name, coverage, gps_list

component_type ∈ { CDB, Municipality, Notified_Area, Unparsed }
coverage ∈ { full, partial }

Run:
    python3 scripts/parse_delimitation_wb.py
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

import pdfplumber

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "data" / "raw" / "pdfs" / "delimitation_order_2008.pdf"
AC_LIST = ROOT / "data" / "raw" / "ac_list.csv"
OUT = ROOT / "data" / "raw" / "delimitation_ac_components.csv"

WB_START_PAGE = 517
WB_END_PAGE = 539  # inclusive


def load_ac_list() -> dict[int, dict]:
    with AC_LIST.open() as f:
        return {int(r["ac_no"]): r for r in csv.DictReader(f)}


def extract_wb_text() -> str:
    parts: list[str] = []
    with pdfplumber.open(PDF) as pdf:
        for i in range(WB_START_PAGE - 1, WB_END_PAGE):
            t = pdf.pages[i].extract_text() or ""
            parts.append(t)
    return "\n".join(parts)


# Locate an AC entry's starting line.  Accepts:
#   "95. BANGAON UTTAR 1. ..."   (standard — number, dot, space, NAME)
#   "182.                1. CDB..."  (name wrapped to next line)
#   "70 REJINAGAR 1. CDB..."     (missing dot — seen in ACs 70-71)
# Rejects district-section headers "N - DISTRICT: NAME".
AC_HEADER_START_RE = re.compile(r"^\s*(?P<no>\d{1,3})\.?\s+(?=[A-Z0-9]|$)")


def chunk_acs(raw: str) -> list[tuple[int, str]]:
    """Return list of (ac_no, extent_text) pairs.

    extent_text is everything from the AC's own "1." up to the next AC header,
    with wrapped lines joined by single spaces.
    """
    lines = [ln for ln in raw.splitlines() if ln.strip()]
    # First pass: mark lines where AC_HEADER_START_RE matches AND the AC number
    # makes sense in sequence (1..294).  The order is ascending, so we only
    # accept a new header if ac_no == last_ac_no + 1 (with small gaps tolerated
    # for the district-section injections).
    starts: list[tuple[int, int]] = []  # (line_idx, ac_no)
    last_ac = 0
    for i, ln in enumerate(lines):
        m = AC_HEADER_START_RE.match(ln)
        if not m:
            continue
        no = int(m.group("no"))
        if 1 <= no <= 294 and no == last_ac + 1:
            # Also verify this line isn't a district-section header
            # ("9 - DISTRICT: ...") — those don't end with "."
            if "DISTRICT" in ln.upper() and ":" in ln:
                continue
            starts.append((i, no))
            last_ac = no

    chunks: list[tuple[int, str]] = []
    for j, (line_idx, ac_no) in enumerate(starts):
        next_idx = starts[j + 1][0] if j + 1 < len(starts) else len(lines)
        block_lines = lines[line_idx:next_idx]
        joined = " ".join(block_lines).strip()
        # Strip leading "NN." of this AC's own header.
        joined = re.sub(rf"^\s*{ac_no}\.\s+", "", joined, count=1)
        chunks.append((ac_no, joined))
    return chunks


def split_components(extent: str) -> list[str]:
    """Split on 'NN. ' component markers.

    Only splits on whitespace + digit + '.' + space (with digit ∈ 1..9 only —
    this keeps us from splitting on 'Bangaon-1.' or similar)."""
    parts = re.split(r"(?:(?<=\s)|^)([1-9])\.\s+", extent)
    if len(parts) < 3:
        return [extent.strip()] if extent.strip() else []
    components: list[str] = []
    # parts = [pre, "1", chunk1, "2", chunk2, ...]
    for k in range(2, len(parts), 2):
        components.append(parts[k].strip())
    return components


def clean_component(c: str) -> str:
    """Scrub stray '(SC)' / '(ST)' reservation markers, page-number noise,
    and district-header leakage from PDF layout quirks."""
    # Reservation markers on continuation lines.
    c = re.sub(r"\s*\((SC|ST)\)\s*", " ", c)
    # District-section headers "N - DISTRICT : NAME" that straddle page breaks.
    c = re.sub(r"\s*\d+\s*[-–]\s*DISTRICT\s*:\s*[A-Z0-9\s]+$", "", c, flags=re.IGNORECASE)
    # Page-number noise like " 517 3 " (footer/header artefacts).
    c = re.sub(r"\s+\d{3}\s+\d+\s*[-–]\s*DISTRICT.*$", "", c, flags=re.IGNORECASE)
    c = re.sub(r"\s+\d{3}\s*$", "", c)
    # Typo: "ofCDB" → "of CDB"
    c = re.sub(r"\bofCDB\b", "of CDB", c)
    # Inline "N." without space ("2.Tufanganj"): these are stray AC-index markers
    # from continuation; we drop everything from the "N." to end because this
    # component was never properly split.
    c = re.sub(r"\s*,?\s*\d+\.\s*[A-Z].*$", "", c)
    # Trailing conjunctions/punctuation.
    c = re.sub(r"\s*[,&.]\s*(?:and)?\s*$", "", c, flags=re.IGNORECASE)
    c = re.sub(r"\s+and\s*$", "", c, flags=re.IGNORECASE)
    c = re.sub(r"\s+&\s*$", "", c)
    c = re.sub(r"\s+", " ", c).strip()
    return c


def parse_component(comp: str) -> tuple[str, str, str, list[str]]:
    """Classify one component into (type, name, coverage, gps)."""
    c = clean_component(comp).rstrip(",").rstrip(".").strip()

    # "GPs of CDB <name>" — partial CDB
    m = re.search(r"GPs?\s+of\s+CDB\s+([A-Za-z0-9\-\s/']+?)(?:\s+and\b|\s*$|\s*,)", c, re.IGNORECASE)
    if m:
        cdb_name = m.group(1).strip().rstrip(",")
        # Also handle "(Part)" suffix that appears on some.
        cdb_name = re.sub(r"\s*\(Part\)$", "", cdb_name).strip()
        gp_part = c[: c.lower().rfind("gps of")].strip().rstrip(",").rstrip(".")
        gps = [g.strip() for g in re.split(r",|\s+and\s+", gp_part) if g.strip()]
        return ("CDB", cdb_name, "partial", gps)

    # "CDB <name>" — full CDB (may have suffix like "- I" / "-II")
    m = re.match(r"CDB\s+([A-Za-z0-9\-\s/']+)$", c, re.IGNORECASE)
    if m:
        return ("CDB", m.group(1).strip(), "full", [])

    # "<name> Municipality" alt form
    m = re.match(r"([A-Za-z0-9\-\s/']+?)\s+Municipality$", c, re.IGNORECASE)
    if m:
        return ("Municipality", m.group(1).strip(), "full", [])

    # "<name> (M)" / "<name> (MC)"
    m = re.match(r"(.+?)\s*\((?:M|MC)\)$", c)
    if m:
        return ("Municipality", m.group(1).strip(), "full", [])

    # "<name> (NA)" / "<name> NA"
    m = re.match(r"(.+?)\s*(?:\(NA\)|\sNA)$", c)
    if m:
        return ("Notified_Area", m.group(1).strip(), "full", [])

    # "<name> (M Corp)" or "<name> M Corp" — Municipal Corporation
    m = re.match(r"(.+?)\s*(?:\(M\s*Corp\)|M\s*Corp)$", c, re.IGNORECASE)
    if m:
        return ("Municipality", m.group(1).strip() + " (Corp)", "full", [])

    # "Ward Nos. ... of <name> (M)" / "<name> M Corp" — partial municipality
    m = re.match(r"Ward\s+Nos?\.?\s*(.+?)\s+of\s+(.+?)(?:\s*\(M\)|\s*M\s*Corp)?$", c, re.IGNORECASE)
    if m:
        wards = [w.strip() for w in re.split(r",|\s+and\s+", m.group(1)) if w.strip()]
        return ("Municipality_partial", m.group(2).strip(), "partial", wards)

    # "CDB <name>" — allow with no trailing word boundary (handles "CDB Mal").
    m = re.match(r"CDB\s+([A-Za-z0-9\-\s/']+)", c, re.IGNORECASE)
    if m and len(c) - len(m.group(0)) < 3:
        return ("CDB", m.group(1).strip(), "full", [])

    # Bare name ending in "(M)" anywhere (handles "Coochbehar(M)" no space).
    m = re.match(r"^([A-Za-z0-9\-\s/']+?)\s*\(M\)$", c)
    if m:
        return ("Municipality", m.group(1).strip(), "full", [])

    # "<GPs> GPs of <name>" — partial CDB (without "CDB" prefix, rare form).
    m = re.search(r"GPs?\s+of\s+([A-Za-z0-9\-\s/']+?)(?:\s*$|\s+and\b)", c, re.IGNORECASE)
    if m:
        cdb_name = m.group(1).strip()
        gp_part = c[: c.lower().rfind("gps of")].strip().rstrip(",").rstrip(".")
        gps = [g.strip() for g in re.split(r",|\s+and\s+", gp_part) if g.strip()]
        return ("CDB", cdb_name, "partial", gps)

    return ("Unparsed", c, "full", [])


# Hand-filled rows for ACs whose header our regex fails on (name on wrap line).
# Sourced by inspection of Delimitation 2008 PDF page 531.
HAND_FILL: dict[int, list[tuple[str, str, str, list[str]]]] = {
    182: [
        ("CDB", "Udaynarayanpur", "full", []),
        ("CDB", "Amta-I", "partial",
         ["Anulia", "Balichak", "Basantapur", "Kanpur", "Khosalpur"]),
    ],
    183: [
        ("CDB", "Jagatballavpur", "partial",
         ["Baragachhia-I", "Baragachhia-II", "Hantal Anantabati",
          "Jagatballavpur-I", "Jagatballavpur-II", "Pantihal",
          "Shankarhati-I", "Shankarhati-II", "Shialdanga", "Maju"]),
        ("CDB", "Domjur", "partial",
         ["Begari", "Domjur", "Dakshin-Jhapardaha",
          "Parbatipur", "Rudrapur", "Uttar Jhapardaha", "Makardah-I"]),
    ],
}


def main() -> None:
    ac_list = load_ac_list()
    raw = extract_wb_text()
    chunks = chunk_acs(raw)
    chunk_map = {no: ext for no, ext in chunks}

    rows: list[list] = []
    missing_acs: list[int] = []
    for ac_no in range(1, 295):
        ac = ac_list.get(ac_no)
        if ac is None:
            continue
        if ac_no in HAND_FILL:
            for ctype, cname, coverage, gps in HAND_FILL[ac_no]:
                rows.append([ac_no, ac["ac_name"], ac["district"], ac["reservation"],
                             ctype, cname, coverage, "|".join(gps)])
            continue
        extent = chunk_map.get(ac_no)
        if not extent:
            missing_acs.append(ac_no)
            continue
        comps = split_components(extent)
        if not comps:
            missing_acs.append(ac_no)
            continue
        for c in comps:
            ctype, cname, coverage, gps = parse_component(c)
            rows.append([ac_no, ac["ac_name"], ac["district"], ac["reservation"],
                         ctype, cname, coverage, "|".join(gps)])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ac_no", "ac_name", "district", "reservation",
                    "component_type", "component_name", "coverage", "gps_list"])
        w.writerows(rows)

    ac_with_components = len({r[0] for r in rows})
    print(f"AC entries parsed    : {len(chunks)}/292 expected from PDF (+2 hand-filled)")
    print(f"ACs with components  : {ac_with_components}/294")
    print(f"Rows written         : {len(rows)}")
    if missing_acs:
        print(f"Still missing AC     : {missing_acs}")

    # Show AC 95 as sanity check.
    print("\n--- AC 95 Bangaon Uttar components ---")
    for r in rows:
        if r[0] == 95:
            print(r)


if __name__ == "__main__":
    main()
