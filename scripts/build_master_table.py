"""
Build the unified per-AC master table for West Bengal.

Joins:
  - Census 2011 PCA demographics (aggregated via village→AC crosswalk)
  - ECI 2011 Statistical Report (electorate, polling %, voters)
  - NFHS-5 district indicators (mapped AC→district)
  - MyNeta 2021 candidates (winner party baseline)
  - MyNeta 2026 partial candidates
  - AC metadata (name, district, SC/ST reservation)

Output: data/master/wb_ac_master.csv (one row per AC, ~294 rows)
"""
import csv, os
from collections import defaultdict

BASE = '/Users/atharvapandey/Kairosity/WBData/data'


def load_demographics():
    """PCA-aggregated demographics per AC."""
    d = {}
    with open(f'{BASE}/crosswalk/wb_ac_demographics.csv') as f:
        for row in csv.DictReader(f):
            try:
                ac = int(row['ac_no'])
            except ValueError:
                continue
            d[ac] = row
    return d


def load_eci_2011():
    """ECI 2011 Statistical Report per AC."""
    d = {}
    with open(f'{BASE}/electoral_history/wb_ac_historical_summary.csv') as f:
        for row in csv.DictReader(f):
            if int(row['year']) == 2011:
                d[int(row['ac_no'])] = row
    return d


def load_harvard_ac_info():
    """Get AC name + district from Harvard crosswalk."""
    ac_info = {}
    district_for_ac = {}
    with open(f'{BASE}/crosswalk/harvard_11587762.tab') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            try:
                ac_no = int(row['AC_no'])
            except ValueError:
                continue
            if ac_no not in ac_info:
                ac_info[ac_no] = row['AC_name'].strip('" ').strip()
                district_for_ac[ac_no] = row['District_name2011'].strip('" ').strip()
    return ac_info, district_for_ac


def load_myneta(path):
    """MyNeta candidates by constituency ID."""
    if not os.path.exists(path):
        return {}
    d = defaultdict(list)
    with open(path) as f:
        for row in csv.DictReader(f):
            try:
                cid = int(row['cid'] if 'cid' in row else row['constituency_id'])
            except (ValueError, KeyError):
                continue
            d[cid].append(row)
    return dict(d)


def load_nfhs_district():
    """Pivot NFHS-5 indicators to district-level dict."""
    d = defaultdict(dict)
    with open(f'{BASE}/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv') as f:
        for row in csv.DictReader(f):
            d[row['District'].strip().lower()][row['Indicator']] = row.get('NFHS-5', '')
    return dict(d)


def district_match(ac_district, nfhs_data):
    """Match AC district name to NFHS district key."""
    if not ac_district:
        return None
    k = ac_district.lower().strip()
    # Direct match
    if k in nfhs_data:
        return nfhs_data[k]
    # Try without "district" suffix or common variations
    for d_key in nfhs_data:
        if k in d_key or d_key in k:
            return nfhs_data[d_key]
    return None


if __name__ == '__main__':
    print("Loading inputs...")
    demo = load_demographics()
    eci = load_eci_2011()
    ac_info, ac_district = load_harvard_ac_info()
    myneta_21 = load_myneta(f'{BASE}/candidates_2026/wb_2021_candidates.csv')
    myneta_26 = load_myneta(f'{BASE}/candidates_2026/wb_2026_candidates.csv')
    nfhs = load_nfhs_district()

    print(f"  demographics: {len(demo)} ACs")
    print(f"  eci 2011: {len(eci)} ACs")
    print(f"  ac_info: {len(ac_info)} ACs")
    print(f"  myneta 2021: {len(myneta_21)} ACs")
    print(f"  myneta 2026: {len(myneta_26)} ACs")
    print(f"  nfhs districts: {len(nfhs)}")

    # Build master: all 294 ACs
    os.makedirs(f'{BASE}/master', exist_ok=True)
    out_path = f'{BASE}/master/wb_ac_master.csv'

    # Select NFHS indicators of interest
    NFHS_INDICATORS = [
        '2. Population below age 15 years (%)',
        '3. Sex ratio of the total population (females per 1,000 males)',
        '7. Children under age 5 years whose birth was registered (%)',
        '12. Female population age 6 years and above who ever attended school (%)',
        '26. Total fertility rate (children per woman)',
    ]

    header = [
        'ac_no', 'ac_name', 'district', 'reservation',
        # Demographics from Census PCA (aggregated)
        'villages_mapped', 'census_pop', 'census_pop_m', 'census_pop_f',
        'census_sc_pop', 'census_st_pop', 'census_literates', 'census_total_workers',
        'census_cultivators', 'census_agri_labourers', 'census_hh_industry_workers',
        'census_other_workers', 'census_households',
        # Derived census rates
        'census_sc_pct', 'census_st_pct', 'census_literacy_rate_pct',
        'census_workforce_participation_pct', 'census_agri_worker_share_pct',
        # ECI 2011 electoral data
        'eci2011_electors', 'eci2011_voters', 'eci2011_polling_pct',
        # MyNeta 2021 candidate counts
        'myneta21_candidates', 'myneta21_parties',
        # MyNeta 2026 partial
        'myneta26_candidates',
        # NFHS district fallback
    ] + [f'nfhs_{i + 1}' for i in range(len(NFHS_INDICATORS))]

    rows = []
    for ac_no in range(1, 295):
        d = demo.get(ac_no, {})
        e = eci.get(ac_no, {})
        dist = ac_district.get(ac_no, '')
        name = ac_info.get(ac_no, e.get('ac_name', ''))

        # Detect reservation from AC name
        resv = ''
        if '(SC)' in name or 'SC)' in name:
            resv = 'SC'
        elif '(ST)' in name or 'ST)' in name:
            resv = 'ST'

        pop = int(d.get('total_population', 0) or 0)
        pop_m = int(d.get('total_males', 0) or 0)
        pop_f = int(d.get('total_females', 0) or 0)
        sc = int(d.get('sc_pop', 0) or 0)
        st = int(d.get('st_pop', 0) or 0)
        lit = int(d.get('literates', 0) or 0)
        tw = int(d.get('total_workers', 0) or 0)
        cult = int(d.get('cultivators', 0) or 0)
        aglab = int(d.get('agri_labourers', 0) or 0)
        hhind = int(d.get('household_industry_workers', 0) or 0)
        other = int(d.get('other_workers', 0) or 0)
        hh = int(d.get('no_households', 0) or 0)

        def pct(num, denom):
            return round(100.0 * num / denom, 2) if denom > 0 else None

        agri_share = pct(cult + aglab, tw) if tw else None

        nfhs_row = district_match(dist, nfhs)
        nfhs_vals = []
        for ind in NFHS_INDICATORS:
            nfhs_vals.append(nfhs_row.get(ind, '') if nfhs_row else '')

        myneta21_list = myneta_21.get(ac_no, [])
        myneta21_parties = sorted({r['party'] for r in myneta21_list if r.get('party')})

        rows.append({
            'ac_no': ac_no,
            'ac_name': name,
            'district': dist,
            'reservation': resv,
            'villages_mapped': d.get('villages_mapped', 0),
            'census_pop': pop,
            'census_pop_m': pop_m,
            'census_pop_f': pop_f,
            'census_sc_pop': sc,
            'census_st_pop': st,
            'census_literates': lit,
            'census_total_workers': tw,
            'census_cultivators': cult,
            'census_agri_labourers': aglab,
            'census_hh_industry_workers': hhind,
            'census_other_workers': other,
            'census_households': hh,
            'census_sc_pct': pct(sc, pop),
            'census_st_pct': pct(st, pop),
            'census_literacy_rate_pct': pct(lit, pop),
            'census_workforce_participation_pct': pct(tw, pop),
            'census_agri_worker_share_pct': agri_share,
            'eci2011_electors': e.get('total_electors', ''),
            'eci2011_voters': e.get('total_voters', ''),
            'eci2011_polling_pct': e.get('polling_pct', ''),
            'myneta21_candidates': len(myneta21_list),
            'myneta21_parties': ';'.join(myneta21_parties),
            'myneta26_candidates': len(myneta_26.get(ac_no, [])),
            **{f'nfhs_{i + 1}': v for i, v in enumerate(nfhs_vals)},
        })

    with open(out_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        w.writerows(rows)

    print(f"\nMaster table: {out_path} ({len(rows)} rows)")

    # Validation
    total_pop = sum(r['census_pop'] for r in rows)
    total_eci_electors = sum(int(r['eci2011_electors']) if r['eci2011_electors'] else 0 for r in rows)
    total_sc = sum(r['census_sc_pop'] for r in rows)
    total_st = sum(r['census_st_pop'] for r in rows)
    covered_acs = sum(1 for r in rows if r['villages_mapped'])

    print(f"\n=== Validation ===")
    print(f"ACs with villages mapped: {covered_acs}/294 ({100 * covered_acs / 294:.1f}%)")
    print(f"Total mapped census population: {total_pop:,} (WB 2011 state total: ~91.3M)")
    print(f"  coverage: {100 * total_pop / 91_276_115:.1f}%")
    print(f"Total SC population: {total_sc:,} (state total 21,463,270)")
    print(f"  coverage: {100 * total_sc / 21_463_270:.1f}%")
    print(f"Total 2011 electors (from ECI): {total_eci_electors:,} (state total 56.28M)")
    print(f"\nSample AC rows:")
    for r in rows[:2] + rows[100:102]:
        print(f"  AC {r['ac_no']} {r['ac_name']} [{r['district']}]: pop={r['census_pop']:,}, lit={r['census_literacy_rate_pct']}%, SC={r['census_sc_pct']}%, electors={r['eci2011_electors']}, polling={r['eci2011_polling_pct']}%")
