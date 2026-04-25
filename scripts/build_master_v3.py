"""Build master V3 joining all years (2011, 2016, 2021) + SHRUG demographics."""
import csv, os
from collections import defaultdict

BASE = '/Users/atharvapandey/Kairosity/WBData/data'


def _first(row, keys):
    for k in keys:
        if k in row and row[k] not in (None, ''):
            return str(row[k]).strip()
    return ''


def load_detailed_results(year_dir):
    """Load ECI detailed_results_full.csv → per-AC winner + top candidates + totals."""
    path = f'{BASE}/electoral_history/{year_dir}/detailed_results_full.csv'
    if not os.path.exists(path):
        return {}

    AC_KEYS = ['AC NO.', 'AC No.', 'Constituency No.', 'ac_no', 'AC No', 'constituency_no']
    CAND_KEYS = ['CANDIDATE NAME', 'Candidate Name', 'candidate_name']
    PARTY_KEYS = ['PARTY', 'Party', 'Party Name', 'party']
    SEX_KEYS = ['SEX', 'Sex', 'Candidate Sex', 'sex']
    AGE_KEYS = ['AGE', 'Age', 'Candidate Age']
    TOTAL_KEYS = ['TOTAL', 'Total', 'Total Valid Votes', 'Total Votes', 'total']
    ELECTOR_KEYS = ['TOTAL ELECTORS', 'Total Electors', 'Electors', 'total_electors']

    by_ac = defaultdict(list)
    with open(path) as f:
        for row in csv.DictReader(f):
            ac_s = _first(row, AC_KEYS)
            try:
                ac_no = int(ac_s)
            except ValueError:
                continue
            by_ac[ac_no].append(row)

    summaries = {}
    for ac_no, cands in by_ac.items():
        def vtot(c):
            v = _first(c, TOTAL_KEYS)
            try:
                return int(str(v).replace(',', '').strip() or 0)
            except ValueError:
                return 0
        winner = max(cands, key=vtot) if cands else {}
        sorted_c = sorted(cands, key=vtot, reverse=True)
        runner_up = sorted_c[1] if len(sorted_c) > 1 else {}

        total_electors = 0
        for c in cands:
            te = _first(c, ELECTOR_KEYS)
            try:
                total_electors = int(str(te).replace(',', '').strip() or 0)
                if total_electors > 0:
                    break
            except ValueError:
                continue

        summaries[ac_no] = {
            'candidates': len(cands),
            'winner_name': _first(winner, CAND_KEYS),
            'winner_party': _first(winner, PARTY_KEYS),
            'winner_sex': _first(winner, SEX_KEYS),
            'winner_age': _first(winner, AGE_KEYS),
            'winner_votes': vtot(winner),
            'runner_up_name': _first(runner_up, CAND_KEYS),
            'runner_up_party': _first(runner_up, PARTY_KEYS),
            'runner_up_votes': vtot(runner_up),
            'margin': vtot(winner) - vtot(runner_up),
            'total_electors': total_electors,
        }
    return summaries


def load_shrug_ac_names():
    path = f'{BASE}/shrug/ac08_name_key.csv'
    d = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            if row['pc01_state_id'] != '19':
                continue
            ac_id = row['ac08_id']
            try:
                ac_num = int(ac_id.rsplit('-', 1)[-1])
            except ValueError:
                continue
            d[ac_num] = {
                'ac08_id': ac_id,
                'name': row['ac08_name'],
                'district': row['pc01_district_name'],
            }
    return d


def load_shrug_pca():
    path = f'{BASE}/shrug/shrug-pca11-csv/pc11_pca_clean_con08.csv'
    d = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            d[row['ac08_id']] = row
    return d


def load_eci11_summary():
    path = f'{BASE}/electoral_history/wb_ac_historical_summary.csv'
    d = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            if int(row['year']) == 2011:
                d[int(row['ac_no'])] = row
    return d


def load_myneta(path):
    if not os.path.exists(path):
        return {}
    d = defaultdict(list)
    with open(path) as f:
        for row in csv.DictReader(f):
            cid_str = row.get('cid') or row.get('constituency_id') or row.get('ac_no') or ''
            try:
                cid = int(cid_str)
            except (ValueError, TypeError):
                continue
            d[cid].append(row)
    return dict(d)


def load_nfhs():
    d = defaultdict(dict)
    with open(f'{BASE}/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv') as f:
        for row in csv.DictReader(f):
            d[row['District'].strip().lower()][row['Indicator']] = row.get('NFHS-5', '')
    return dict(d)


def fnum(v, default=0):
    try:
        return float(v) if v else default
    except (ValueError, TypeError):
        return default


def pct(num, denom):
    try:
        return round(100.0 * float(num) / float(denom), 2) if float(denom) else None
    except (ValueError, TypeError, ZeroDivisionError):
        return None


if __name__ == '__main__':
    ac_names = load_shrug_ac_names()
    pca = load_shrug_pca()
    d21 = load_detailed_results('2021')
    d16 = load_detailed_results('2016')
    e11 = load_eci11_summary()
    m21 = load_myneta(f'{BASE}/candidates_2026/wb_2021_candidates.csv')
    m26 = load_myneta(f'{BASE}/candidates_2026/wb_2026_candidates.csv')
    nfhs = load_nfhs()

    print(f"SHRUG ACs: {len(ac_names)}, PCA rows: {len(pca)}")
    print(f"ECI 2021: {len(d21)}, 2016: {len(d16)}, 2011: {len(e11)}")
    print(f"MyNeta 2021: {len(m21)}, 2026: {len(m26)}")
    print(f"NFHS districts: {len(nfhs)}")

    os.makedirs(f'{BASE}/master', exist_ok=True)
    out = f'{BASE}/master/wb_ac_master_v3.csv'

    rows = []
    for ac_num in range(1, 295):
        info = ac_names.get(ac_num, {})
        name = info.get('name', '')
        district = info.get('district', '')
        ac08 = info.get('ac08_id', f'2008-19-{ac_num:03d}')

        p = pca.get(ac08, {})
        pop = fnum(p.get('pc11_pca_tot_p'))
        pop_m = fnum(p.get('pc11_pca_tot_m'))
        pop_f = fnum(p.get('pc11_pca_tot_f'))
        p06 = fnum(p.get('pc11_pca_p_06'))
        sc = fnum(p.get('pc11_pca_p_sc'))
        st = fnum(p.get('pc11_pca_p_st'))
        lit = fnum(p.get('pc11_pca_p_lit'))
        f_lit = fnum(p.get('pc11_pca_f_lit'))
        f_06 = fnum(p.get('pc11_pca_f_06'))
        workers = fnum(p.get('pc11_pca_tot_work_p'))
        cultivators = fnum(p.get('pc11_pca_main_cl_p'))
        agri_lab = fnum(p.get('pc11_pca_main_al_p'))
        hh_ind = fnum(p.get('pc11_pca_main_hh_p'))
        other_w = fnum(p.get('pc11_pca_main_ot_p'))
        hh = fnum(p.get('pc11_pca_no_hh'))

        r21 = d21.get(ac_num, {})
        r16 = d16.get(ac_num, {})
        r11 = e11.get(ac_num, {})

        # Reservation
        upper = name.upper()
        resv = 'SC' if '(sc)' in name.lower() else 'ST' if '(st)' in name.lower() else 'GEN'

        # NFHS
        nfhs_r = nfhs.get(district.lower().strip(), {})

        rows.append({
            'ac_no': ac_num,
            'ac_name': name,
            'district': district,
            'reservation': resv,

            # Census 2011 demographics (SHRUG AC-weighted)
            'pop_total': int(pop),
            'pop_m': int(pop_m),
            'pop_f': int(pop_f),
            'pop_0_6': int(p06),
            'households': int(hh),
            'sc_pop': int(sc),
            'st_pop': int(st),
            'literates': int(lit),
            'workers_total': int(workers),
            'cultivators': int(cultivators),
            'agri_labourers': int(agri_lab),
            'hh_industry_workers': int(hh_ind),
            'other_workers': int(other_w),

            # Derived rates
            'sex_ratio': round(1000 * pop_f / pop_m) if pop_m else None,
            'sc_pct': pct(sc, pop),
            'st_pct': pct(st, pop),
            'literacy_pct': pct(lit, pop - p06 if pop > p06 else pop),
            'female_literacy_pct': pct(f_lit, pop_f - f_06 if pop_f > f_06 else pop_f),
            'workforce_pct': pct(workers, pop),
            'agri_share_pct': pct(cultivators + agri_lab, workers) if workers else None,

            # ECI 2011
            'electors_2011': int(fnum(r11.get('total_electors'))),
            'polling_2011': fnum(r11.get('polling_pct')),

            # ECI 2016
            'electors_2016': r16.get('total_electors', 0),
            'winner_2016': r16.get('winner_name', ''),
            'winner_party_2016': r16.get('winner_party', ''),
            'winner_sex_2016': r16.get('winner_sex', ''),
            'margin_2016': r16.get('margin', 0),
            'candidates_2016': r16.get('candidates', 0),

            # ECI 2021
            'electors_2021': r21.get('total_electors', 0),
            'winner_2021': r21.get('winner_name', ''),
            'winner_party_2021': r21.get('winner_party', ''),
            'winner_sex_2021': r21.get('winner_sex', ''),
            'winner_age_2021': r21.get('winner_age', ''),
            'winner_votes_2021': r21.get('winner_votes', 0),
            'runner_up_party_2021': r21.get('runner_up_party', ''),
            'runner_up_votes_2021': r21.get('runner_up_votes', 0),
            'margin_2021': r21.get('margin', 0),
            'candidates_2021': r21.get('candidates', 0),

            # Switch indicator (did party change 2016→2021?)
            'party_switch_16_21': 'YES' if (r16.get('winner_party') and r21.get('winner_party') and r16.get('winner_party').strip() != r21.get('winner_party').strip()) else 'NO',

            # MyNeta candidates
            'myneta21_cand_count': len(m21.get(ac_num, [])),
            'myneta26_cand_count': len(m26.get(ac_num, [])),

            # NFHS indicators
            'nfhs_under15_pct': nfhs_r.get('2. Population below age 15 years (%)', ''),
            'nfhs_female_school_pct': nfhs_r.get('12. Female population age 6 years and above who ever attended school (%)', ''),
            'nfhs_tfr': nfhs_r.get('26. Total fertility rate (children per woman)', ''),
        })

    with open(out, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

    print(f"\n✓ Wrote: {out} ({len(rows)} ACs × {len(rows[0])} cols)")

    # Validation
    print(f"\n=== Coverage ===")
    print(f"  Demographics: {sum(1 for r in rows if r['pop_total'])}/294")
    print(f"  2011 results: {sum(1 for r in rows if r['electors_2011'])}/294")
    print(f"  2016 winners: {sum(1 for r in rows if r['winner_2016'])}/294")
    print(f"  2021 winners: {sum(1 for r in rows if r['winner_2021'])}/294")

    # Party-level summaries
    from collections import Counter
    print(f"\n=== 2016 party wins ===")
    c16 = Counter(r['winner_party_2016'] for r in rows if r['winner_party_2016'])
    for p, n in c16.most_common(8):
        print(f"  {p}: {n}")

    print(f"\n=== 2021 party wins ===")
    c21 = Counter(r['winner_party_2021'] for r in rows if r['winner_party_2021'])
    for p, n in c21.most_common(8):
        print(f"  {p}: {n}")

    # Switches
    switches = sum(1 for r in rows if r['party_switch_16_21'] == 'YES')
    print(f"\n=== Seat switches 2016→2021: {switches}/294 ===")
