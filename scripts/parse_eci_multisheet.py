"""
Parse multi-sheet ECI 2021 XLSX files (one sheet per constituency).

The XLSX stylesheet is malformed (ECI's fault), so we bypass openpyxl entirely
and parse the raw XML inside the .xlsx zip.
"""
import zipfile, os, csv, re
from xml.etree import ElementTree as ET

NS = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'


def load_shared_strings(z):
    try:
        with z.open('xl/sharedStrings.xml') as f:
            tree = ET.parse(f)
    except KeyError:
        return []
    ss = []
    for si in tree.getroot().iter(f'{{{NS}}}si'):
        texts = [t.text or '' for t in si.iter(f'{{{NS}}}t')]
        ss.append(''.join(texts))
    return ss


def parse_sheet_xml(xml_data, shared_strings):
    rows_out = []
    root = ET.fromstring(xml_data)
    for row_el in root.iter(f'{{{NS}}}row'):
        row = []
        for c in row_el.iter(f'{{{NS}}}c'):
            typ = c.get('t')
            val = ''
            v = c.find(f'{{{NS}}}v')
            if v is not None:
                val = v.text or ''
                if typ == 's':
                    try:
                        val = shared_strings[int(val)]
                    except (ValueError, IndexError):
                        pass
            elif typ == 'inlineStr':
                t = c.find(f'.//{{{NS}}}t')
                if t is not None:
                    val = t.text or ''
            row.append(val)
        if any(str(v).strip() for v in row):
            rows_out.append(row)
    return rows_out


def sheet_names_from_workbook(z):
    """Return list of (sheet_name, rId) in order."""
    with z.open('xl/workbook.xml') as f:
        tree = ET.parse(f)
    sheets = []
    for s in tree.getroot().iter(f'{{{NS}}}sheet'):
        sheets.append({
            'name': s.get('name'),
            'sheetId': s.get('sheetId'),
            'rId': s.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'),
        })
    # Read rels
    with z.open('xl/_rels/workbook.xml.rels') as f:
        rels = ET.parse(f)
    rel_map = {}
    for r in rels.getroot():
        rel_map[r.get('Id')] = r.get('Target')
    for s in sheets:
        s['path'] = 'xl/' + rel_map.get(s['rId'], 'worksheets/sheet1.xml')
    return sheets


def parse_xlsx_all_sheets(xlsx_path):
    out = {}
    with zipfile.ZipFile(xlsx_path) as z:
        ss = load_shared_strings(z)
        sheets = sheet_names_from_workbook(z)
        for s in sheets:
            try:
                with z.open(s['path']) as f:
                    xml_data = f.read()
                rows = parse_sheet_xml(xml_data, ss)
                out[s['name']] = rows
            except Exception as e:
                print(f"    ! failed sheet {s['name']}: {e}")
    return out


def flatten_constituency_summaries(sheet_data):
    """Each sheet is one AC. Extract the AC's fielded summary into a row."""
    rows = []
    for sheet_name, sheet_rows in sheet_data.items():
        # Find AC number + name from early rows
        ac_num = None
        ac_name = None
        fields = {}
        for r in sheet_rows[:40]:
            joined = ' | '.join(str(c) for c in r)
            m = re.search(r'(\d+)\s*[-–]\s*(.+)', joined)
            if m and not ac_num and len(m.group(2)) > 3 and not any(ch.isdigit() for ch in m.group(2)[:20]):
                ac_num, ac_name = int(m.group(1)), m.group(2).strip()
            # Capture label:value pairs
            if len(r) >= 2 and r[0] and r[1]:
                key = str(r[0]).strip()
                val = str(r[1]).strip()
                if key and val:
                    fields[key] = val
        rows.append({
            'sheet': sheet_name,
            'ac_num': ac_num,
            'ac_name': ac_name,
            'raw_fields': fields,
        })
    return rows


def constituency_summary_to_csv(xlsx_path, out_csv):
    """Parse ECI 'Constituency Data Summary' — each sheet = 1 AC."""
    sheets = parse_xlsx_all_sheets(xlsx_path)
    print(f"  loaded {len(sheets)} sheets")

    # Each sheet has same structure: metrics rows for candidates + electors + voters
    # Extract a structured record per AC
    def extract_ac(rows):
        r = {'ac_no': None, 'ac_name': None}
        full_text = '\n'.join(' | '.join(str(c) for c in row) for row in rows)
        # AC header line like "1 - Mekliganj" or "Constituency : 1-Mekliganj"
        m = re.search(r'CONSTITUENCY.*?:\s*(\d+)\s*[-–]\s*([^\n|]+)', full_text, re.IGNORECASE)
        if not m:
            m = re.search(r'(\d+)\s*[-–]\s*([A-Z][a-zA-Z .()]+)', full_text)
        if m:
            r['ac_no'] = int(m.group(1))
            r['ac_name'] = m.group(2).strip()

        def fnum(pat):
            mm = re.search(pat, full_text, re.IGNORECASE)
            if mm:
                v = mm.group(1).replace(',', '').strip()
                try:
                    return int(v)
                except ValueError:
                    try:
                        return float(v)
                    except ValueError:
                        return None
            return None

        r['nominated'] = fnum(r'NOMINATION\s+FILED[^\d]*(\d+)')
        r['rejected'] = fnum(r'NOMINATION\s+REJECTED[^\d]*(\d+)')
        r['contested'] = fnum(r'CONTESTED[^\d]*(\d+)')
        r['electors_male'] = fnum(r'ELECTORS[\s\S]*?(?:GENERAL|TOTAL)[^\d]*(\d{3,})')
        r['electors_total'] = fnum(r'TOTAL\s+ELECTORS[^\d]*(\d+)') or fnum(r'II\.\s*ELECTORS[\s\S]*?TOTAL[^\d]*(\d{3,})')
        r['voters_total'] = fnum(r'III\.\s*VOTERS[\s\S]*?TOTAL[^\d]*(\d{3,})') or fnum(r'TOTAL VOTERS[^\d]*(\d+)')
        r['polling_pct'] = fnum(r'POLLING\s+PERCENTAGE[^\d]*([\d.]+)')
        r['rejected_votes'] = fnum(r'REJECTED VOTES[^\d]*(\d+)')
        r['valid_votes'] = fnum(r'VALID VOTES[^\d]*(\d+)')
        r['nota'] = fnum(r'NONE OF THE ABOVE[^\d]*(\d+)') or fnum(r'NOTA[^\d]*(\d+)')
        return r

    outs = []
    for sheet_name, rows in sheets.items():
        rec = extract_ac(rows)
        rec['sheet'] = sheet_name
        outs.append(rec)

    with open(out_csv, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['sheet', 'ac_no', 'ac_name', 'nominated', 'rejected', 'contested',
                                           'electors_male', 'electors_total', 'voters_total',
                                           'polling_pct', 'valid_votes', 'rejected_votes', 'nota'])
        w.writeheader()
        w.writerows(outs)
    return len(outs)


def detailed_results_to_csv(xlsx_path, out_csv):
    """Parse ECI 'Detailed Results' — each sheet = 1 AC with candidate x vote table."""
    sheets = parse_xlsx_all_sheets(xlsx_path)
    print(f"  loaded {len(sheets)} sheets")
    all_rows = []
    for sheet_name, rows in sheets.items():
        # Find the header row and then candidates
        header_idx = None
        for i, r in enumerate(rows[:15]):
            joined = ' '.join(str(c).lower() for c in r)
            if 'candidate' in joined and 'party' in joined:
                header_idx = i
                break
        if header_idx is None:
            continue
        # Find AC info above header
        pre = '\n'.join(' '.join(str(c) for c in r) for r in rows[:header_idx])
        m = re.search(r'(\d+)\s*[-–]\s*([A-Z][a-zA-Z .()]+)', pre)
        ac_no = int(m.group(1)) if m else None
        ac_name = m.group(2).strip() if m else sheet_name

        header = [str(c).strip() for c in rows[header_idx]]
        for r in rows[header_idx + 1:]:
            if not any(r):
                continue
            candidate_row = {'ac_no': ac_no, 'ac_name': ac_name}
            for i, col in enumerate(r):
                if i < len(header):
                    candidate_row[header[i]] = col
            all_rows.append(candidate_row)

    if all_rows:
        # Collect all fields in order
        all_fields = ['ac_no', 'ac_name']
        for r in all_rows:
            for k in r:
                if k not in all_fields:
                    all_fields.append(k)
        with open(out_csv, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=all_fields)
            w.writeheader()
            w.writerows(all_rows)
    return len(all_rows)


if __name__ == '__main__':
    SRC = '/Users/atharvapandey/Kairosity/WBData/data/electoral_history/eci_detailed/set_A'
    DST = '/Users/atharvapandey/Kairosity/WBData/data/electoral_history/2021'
    os.makedirs(DST, exist_ok=True)

    print("\n=== 8-Constituency Data Summary ===")
    n = constituency_summary_to_csv(
        f'{SRC}/8-Constituency Data Summary.xlsx',
        f'{DST}/constituency_summary_full.csv')
    print(f"  → {n} ACs")

    print("\n=== 9-Candidate Data Summary ===")
    n = constituency_summary_to_csv(
        f'{SRC}/9-Candidate Data Summary.xlsx',
        f'{DST}/candidate_summary_full.csv')
    print(f"  → {n} ACs")

    print("\n=== 10-Detailed Results ===")
    n = detailed_results_to_csv(
        f'{SRC}/10-Detailed Results.xlsx',
        f'{DST}/detailed_results_full.csv')
    print(f"  → {n} candidate-rows")
