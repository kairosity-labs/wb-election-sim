import pdfplumber, re, csv, os
from concurrent.futures import ThreadPoolExecutor

YEARS_DIR = '/Users/atharvapandey/Kairosity/WBData/data/electoral_history/Constituency-Data/Constituency_Data_Extraction/states/West_Bengal'

def parse_year(year):
    path = f'{YEARS_DIR}/{year}/Statistical_Report.pdf'
    if not os.path.exists(path):
        return year, []
    try:
        with pdfplumber.open(path) as pdf:
            full = '\n'.join((p.extract_text() or '') for p in pdf.pages)
    except Exception as e:
        print(f"  {year}: ERROR {e}")
        return year, []

    summaries = re.split(r'(?=CONSTITUENCY\s*:\s*\d+-)', full)
    rows = []
    for s in summaries:
        m = re.search(r'CONSTITUENCY\s*:\s*(\d+)-(.+?)[\n\r]', s)
        if not m:
            continue
        ac_no, ac_name = int(m.group(1)), m.group(2).strip()

        def fnum(pat):
            mm = re.search(pat, s, re.IGNORECASE | re.MULTILINE)
            return int(mm.group(1).replace(',', '')) if mm else None

        poll = re.search(r'POLLING PERCENTAGE\s+([\d.]+)', s)
        total_electors = fnum(r'3\.\s*TOTAL\s+\d+\s+\d+\s+\d+\s+(\d+)')
        total_voters = fnum(r'III\s*\.\s*VOTERS[\s\S]*?4\.\s*TOTAL\s+(\d+)') or fnum(r'IV\.\s*VOTES[\s\S]*?TOTAL\s+(\d+)')
        if ac_no and total_electors:
            rows.append({
                'year': int(year),
                'ac_no': ac_no,
                'ac_name': ac_name,
                'total_electors': total_electors,
                'polling_pct': float(poll.group(1)) if poll else None,
                'total_voters': total_voters,
            })
    return year, rows


if __name__ == '__main__':
    years = sorted(os.listdir(YEARS_DIR))
    print(f"Years: {years}")

    with ThreadPoolExecutor(max_workers=6) as ex:
        results = list(ex.map(parse_year, years))

    all_rows = []
    for y, rs in results:
        print(f"  {y}: {len(rs)} ACs")
        all_rows.extend(rs)

    out = '/Users/atharvapandey/Kairosity/WBData/data/electoral_history/wb_ac_historical_summary.csv'
    with open(out, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['year', 'ac_no', 'ac_name', 'total_electors', 'polling_pct', 'total_voters'])
        w.writeheader()
        w.writerows(all_rows)
    print(f"\nTotal rows: {len(all_rows)}")
    print(f"Saved: {out}")

    from collections import defaultdict
    by_year = defaultdict(list)
    for r in all_rows:
        by_year[r['year']].append(r)
    for y in sorted(by_year):
        rs = by_year[y]
        elec = sum(r['total_electors'] for r in rs if r['total_electors'])
        polls = [r['polling_pct'] for r in rs if r['polling_pct']]
        avg_poll = sum(polls) / len(polls) if polls else 0
        print(f"  {y}: {len(rs)} ACs, electorate {elec / 1e6:.2f}M, avg poll {avg_poll:.1f}%")
