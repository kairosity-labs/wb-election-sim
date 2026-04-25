"""Parse ECI 2016 WB Statistical Report (set_B) XLSX files."""
import zipfile, os, csv, re
from xml.etree import ElementTree as ET

NS = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
SRC = '/Users/atharvapandey/Kairosity/WBData/data/electoral_history/eci_detailed/set_B'
DST = '/Users/atharvapandey/Kairosity/WBData/data/electoral_history/2016'
os.makedirs(DST, exist_ok=True)


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


def sheet_names_from_workbook(z):
    with z.open('xl/workbook.xml') as f:
        tree = ET.parse(f)
    sheets = []
    for s in tree.getroot().iter(f'{{{NS}}}sheet'):
        sheets.append({
            'name': s.get('name'),
            'rId': s.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'),
        })
    with z.open('xl/_rels/workbook.xml.rels') as f:
        rels = ET.parse(f)
    rel_map = {r.get('Id'): r.get('Target') for r in rels.getroot()}
    for s in sheets:
        s['path'] = 'xl/' + rel_map.get(s['rId'], 'worksheets/sheet1.xml')
    return sheets


def parse_sheet_rows(xml_data, ss):
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
                        val = ss[int(val)]
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


def parse_all_sheets(xlsx_path):
    with zipfile.ZipFile(xlsx_path) as z:
        ss = load_shared_strings(z)
        sheets = sheet_names_from_workbook(z)
        out = {}
        for s in sheets:
            with z.open(s['path']) as f:
                xml_data = f.read()
            out[s['name']] = parse_sheet_rows(xml_data, ss)
    return out


def simple_to_csv(sheets, csv_path):
    """Flatten all sheets into one CSV (each sheet gets all rows)."""
    if not sheets:
        return 0
    all_rows = []
    first_sheet = list(sheets.values())[0]
    for name, rows in sheets.items():
        for r in rows:
            all_rows.append([name] + list(r))
    with open(csv_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerows(all_rows)
    return len(all_rows)


def single_sheet_to_csv(xlsx_path, csv_path):
    sheets = parse_all_sheets(xlsx_path)
    first = next(iter(sheets.values()))
    with open(csv_path, 'w', newline='') as f:
        w = csv.writer(f)
        for r in first:
            if any(r):
                w.writerow(r)
    return len(first), len(sheets)


if __name__ == '__main__':
    mappings = [
        ('List of Successful Candidates.xlsx', 'successful_candidates.csv'),
        ('List Of Political Parties Participated.xlsx', 'parties_participated.csv'),
        ('Performance of Poltical Parties.xlsx', 'party_performance.csv'),
        ('Performance of women Candidates.xlsx', 'women_candidates.csv'),
        ('Detailed Results.xlsx', 'detailed_results.csv'),
    ]
    for src_name, dst_name in mappings:
        src = f'{SRC}/{src_name}'
        dst = f'{DST}/{dst_name}'
        if not os.path.exists(src):
            print(f"  ✗ missing: {src_name}")
            continue
        try:
            rows, sheets = single_sheet_to_csv(src, dst)
            print(f"  ✓ {dst_name}: {rows} rows, {sheets} sheets")
        except Exception as e:
            print(f"  ✗ {dst_name}: {e}")

    # Now parse detailed results per-AC
    path = f'{SRC}/Detailed Results.xlsx'
    if os.path.exists(path):
        sheets = parse_all_sheets(path)
        print(f"\nDetailed Results sheets: {len(sheets)}")
        # Flatten by AC
        all_candidates = []
        for sheet_name, rows in sheets.items():
            header_idx = None
            for i, r in enumerate(rows[:15]):
                joined = ' '.join(str(c).lower() for c in r)
                if 'candidate' in joined and 'party' in joined:
                    header_idx = i
                    break
            if header_idx is None:
                continue
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
                all_candidates.append(candidate_row)

        if all_candidates:
            all_fields = ['ac_no', 'ac_name']
            for r in all_candidates:
                for k in r:
                    if k not in all_fields:
                        all_fields.append(k)
            with open(f'{DST}/detailed_results_full.csv', 'w', newline='') as f:
                w = csv.DictWriter(f, fieldnames=all_fields)
                w.writeheader()
                w.writerows(all_candidates)
            print(f"Detailed results_full: {len(all_candidates)} candidate rows")
