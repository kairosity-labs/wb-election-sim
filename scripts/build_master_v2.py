"""
Build master table V2 using SHRUG's AC-2008 aggregated PCA (villages + towns).

Improvements over V1:
- Uses SHRUG's weighted spatial aggregation (more accurate than name-match)
- Joins Village + Town PCA for full urban+rural coverage
- Uses ECI 2021 detailed_results for authoritative electorate
- Parses 2021 winners from successful_candidates
"""
import csv, os
from collections import defaultdict

BASE = '/Users/atharvapandey/Kairosity/WBData/data'


def load_shrug_ac_names():
    """AC 2008 id → (ac_num, name, district)"""
    path = f'{BASE}/shrug/ac08_name_key.csv'
    d = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            if row['pc01_state_id'] != '19':
                continue
            ac_id = row['ac08_id']
            m = ac_id.rsplit('-', 1)
            try:
                ac_num = int(m[-1])
            except ValueError:
                continue
            d[ac_id] = {
                'ac_num': ac_num,
                'name': row['ac08_name'],
                'district': row['pc01_district_name'],
            }
    return d


def load_shrug_pca(file_key):
    """Load SHRUG PCA file aggregated at specified key."""
    path = f'{BASE}/shrug/shrug-pca11-csv/{file_key}'
    d = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            key = row['ac08_id']
            d[key] = row
    return d


def load_shrug_td(file_key):
    """SHRUG Town Directory 2011 at AC level."""
    path = f'{BASE}/shrug/shrug-td11-csv/{file_key}'
    d = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            key = row['ac08_id']
            d[key] = row
    return d


def load_shrug_vd(file_key):
    """SHRUG Village Directory 2011 at AC level."""
    path = f'{BASE}/shrug/shrug-vd11-csv/{file_key}'
    d = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            key = row['ac08_id']
            d[key] = row
    return d


def load_eci_2021_detailed():
    """ECI 2021 detailed results — per-candidate row. Returns list per AC."""
    path = f'{BASE}/electoral_history/2021/detailed_results_full.csv'
    d = defaultdict(list)
    with open(path) as f:
        for row in csv.DictReader(f):
            try:
                ac_no = int(row.get('AC NO.', 0))
            except ValueError:
                continue
            d[ac_no].append(row)
    return dict(d)


def load_eci_2021_summary():
    """ECI 2021 constituency-level summary (electors, voters, polling, NOTA)."""
    path = f'{BASE}/electoral_history/2021/constituency_summary_full.csv'
    d = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            try:
                ac_no = int(row['ac_no'])
            except (ValueError, KeyError):
                continue
            d[ac_no] = row
    return d


def load_successful_candidates():
    """ECI 2021 successful candidates (winners only) from set_A 2-List csv."""
    path = f'{BASE}/electoral_history/2021/successful_candidates.csv'
    d = {}
    with open(path) as f:
        r = csv.reader(f)
        header = next(r)
        # Find column indices
        idx = {k: i for i, k in enumerate(header)}
        for row in r:
            if len(row) < len(header):
                continue
            ac_name = row[idx.get('CONSTITUENCY', 1)]
            winner = row[idx.get('WINNER', 2)]
            sex = row[idx.get('SEX', 3)]
            party = row[idx.get('PARTY', 4)]
            d[ac_name.upper().strip()] = {'winner': winner, 'sex': sex, 'party': party}
    return d


def load_eci_2011_summary():
    path = f'{BASE}/electoral_history/wb_ac_historical_summary.csv'
    d = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            if int(row['year']) != 2011:
                continue
            d[int(row['ac_no'])] = row
    return d


def load_nfhs_district():
    d = defaultdict(dict)
    with open(f'{BASE}/nfhs_5/district-level/NFHS-5-WB-West-Bengal.csv') as f:
        for row in csv.DictReader(f):
            d[row['District'].strip().lower()][row['Indicator']] = row.get('NFHS-5', '')
    return dict(d)


if __name__ == '__main__':
    ac_names = load_shrug_ac_names()
    pca_v = load_shrug_pca('pc11_pca_clean_con08.csv')  # village-aggregated PCA
    td = load_shrug_td('pc11_td_clean_con08.csv')  # town directory
    vd = load_shrug_vd('pc11_vd_clean_con08.csv')  # village directory
    eci21 = load_eci_2021_summary()
    eci21_detail = load_eci_2021_detailed()
    eci11 = load_eci_2011_summary()
    winners = load_successful_candidates()
    nfhs = load_nfhs_district()

    print(f"SHRUG: {len(ac_names)} AC names, {len(pca_v)} PCA-V, {len(td)} TD, {len(vd)} VD")
    print(f"ECI 2021: {len(eci21)} ACs summary, {len(eci21_detail)} ACs detail")
    print(f"ECI 2011: {len(eci11)} ACs")
    print(f"Winners 2021: {len(winners)}")
    print(f"NFHS districts: {len(nfhs)}")

    # Build master
    os.makedirs(f'{BASE}/master', exist_ok=True)
    out_path = f'{BASE}/master/wb_ac_master_v2.csv'

    def pct(num, denom):
        try:
            return round(100.0 * float(num) / float(denom), 2) if float(denom) else None
        except (ValueError, TypeError, ZeroDivisionError):
            return None

    def fnum(v):
        try:
            return float(v) if v else 0
        except (ValueError, TypeError):
            return 0

    rows_out = []
    for ac_id, info in sorted(ac_names.items(), key=lambda x: x[1]['ac_num']):
        ac_num = info['ac_num']
        name = info['name']
        district = info['district']

        # PCA aggregation (SHRUG weighted)
        p = pca_v.get(ac_id, {})
        pop = fnum(p.get('pc11_pca_tot_p'))
        pop_m = fnum(p.get('pc11_pca_tot_m'))
        pop_f = fnum(p.get('pc11_pca_tot_f'))
        sc = fnum(p.get('pc11_pca_p_sc'))
        st = fnum(p.get('pc11_pca_p_st'))
        lit = fnum(p.get('pc11_pca_p_lit'))
        ill = fnum(p.get('pc11_pca_p_ill'))
        workers = fnum(p.get('pc11_pca_tot_work_p'))
        main_workers = fnum(p.get('pc11_pca_mainwork_p'))
        cultivators = fnum(p.get('pc11_pca_main_cl_p'))
        agri_labour = fnum(p.get('pc11_pca_main_al_p'))
        hh_industry = fnum(p.get('pc11_pca_main_hh_p'))
        other_work = fnum(p.get('pc11_pca_main_ot_p'))
        children_0_6 = fnum(p.get('pc11_pca_p_06'))
        households = fnum(p.get('pc11_pca_no_hh'))

        # Town directory: urban metrics
        t = td.get(ac_id, {})
        v = vd.get(ac_id, {})

        # ECI 2021 via detail (authoritative)
        detail = eci21_detail.get(ac_num, [])
        if detail:
            try:
                total_electors_2021 = int(detail[0].get('TOTAL ELECTORS', 0) or 0)
            except ValueError:
                total_electors_2021 = 0
            # Winner = candidate with highest total votes
            def vtot(c):
                try:
                    return int(str(c.get('TOTAL', '0')).replace(',', ''))
                except ValueError:
                    return 0
            winner_c = max(detail, key=vtot) if detail else {}
            winner_name = winner_c.get('CANDIDATE NAME', '').strip()
            winner_party = winner_c.get('PARTY', '').strip()
            winner_pct = fnum(winner_c.get('% VOTES POLLED', 0))
            winner_sex = winner_c.get('SEX', '').strip()
            winner_age = winner_c.get('AGE', '').strip()
            contest_count = len(detail)
            total_valid = sum(vtot(c) for c in detail)
        else:
            total_electors_2021 = 0
            winner_name = winner_party = winner_sex = winner_age = ''
            winner_pct = 0
            contest_count = 0
            total_valid = 0

        # ECI 2021 summary (polling, NOTA)
        s21 = eci21.get(ac_num, {})
        polling_2021 = fnum(s21.get('polling_pct'))
        nota_2021 = fnum(s21.get('nota'))

        # ECI 2011
        e11 = eci11.get(ac_num, {})
        electors_2011 = int(e11.get('total_electors', 0) or 0)
        polling_2011 = fnum(e11.get('polling_pct'))

        # Reservation
        ac_name_upper = name.upper()
        reservation = 'SC' if '(SC)' in ac_name_upper else 'ST' if '(ST)' in ac_name_upper else 'GEN'

        # NFHS match
        nfhs_row = nfhs.get(district.lower().strip(), {})

        rows_out.append({
            'ac_no': ac_num,
            'ac_name': name,
            'district': district,
            'reservation': reservation,

            # Demographics (Census 2011 via SHRUG AC-weighted PCA)
            'pop_total': int(pop),
            'pop_male': int(pop_m),
            'pop_female': int(pop_f),
            'pop_0_6': int(children_0_6),
            'sc_pop': int(sc),
            'st_pop': int(st),
            'literates': int(lit),
            'illiterates': int(ill),
            'households': int(households),
            'total_workers': int(workers),
            'main_workers': int(main_workers),
            'cultivators': int(cultivators),
            'agri_labourers': int(agri_labour),
            'hh_industry_workers': int(hh_industry),
            'other_workers': int(other_work),

            # Derived rates
            'sex_ratio': round(1000 * pop_f / pop_m, 0) if pop_m else None,
            'child_ratio_0_6': pct(children_0_6, pop),
            'sc_pct': pct(sc, pop),
            'st_pct': pct(st, pop),
            'literacy_pct': pct(lit, pop - children_0_6 if pop > children_0_6 else pop),
            'female_literacy_pct': pct(fnum(p.get('pc11_pca_f_lit')),
                                        fnum(p.get('pc11_pca_tot_f')) - fnum(p.get('pc11_pca_f_06'))),
            'workforce_participation_pct': pct(workers, pop),
            'agri_worker_share_pct': pct(cultivators + agri_labour, workers) if workers else None,
            'other_worker_share_pct': pct(other_work, workers) if workers else None,

            # Electoral
            'electors_2021': total_electors_2021,
            'polling_pct_2021': polling_2021,
            'nota_2021': int(nota_2021),
            'total_valid_votes_2021': total_valid,
            'candidates_2021': contest_count,
            'winner_2021': winner_name,
            'winner_party_2021': winner_party,
            'winner_sex_2021': winner_sex,
            'winner_age_2021': winner_age,
            'winner_vote_pct_2021': winner_pct,

            'electors_2011': electors_2011,
            'polling_pct_2011': polling_2011,

            # NFHS district
            'nfhs_under15_pct': nfhs_row.get('2. Population below age 15 years (%)', ''),
            'nfhs_sex_ratio': nfhs_row.get('3. Sex ratio of the total population (females per 1,000 males)', ''),
            'nfhs_female_school_pct': nfhs_row.get('12. Female population age 6 years and above who ever attended school (%)', ''),
            'nfhs_tfr': nfhs_row.get('26. Total fertility rate (children per woman)', ''),
        })

    # Write
    fieldnames = list(rows_out[0].keys())
    with open(out_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows_out)

    print(f"\n✓ Wrote: {out_path}")
    print(f"  Total ACs: {len(rows_out)}")

    # Validation
    demo_cov = sum(1 for r in rows_out if r['pop_total'])
    eci21_cov = sum(1 for r in rows_out if r['electors_2021'])
    winner_cov = sum(1 for r in rows_out if r['winner_2021'])

    print(f"\n=== Coverage ===")
    print(f"  Demographics (SHRUG PCA): {demo_cov}/294 ({100 * demo_cov / 294:.1f}%)")
    print(f"  ECI 2021 electorate: {eci21_cov}/294 ({100 * eci21_cov / 294:.1f}%)")
    print(f"  2021 winners: {winner_cov}/294 ({100 * winner_cov / 294:.1f}%)")

    total_pop = sum(r['pop_total'] for r in rows_out)
    total_elec_2021 = sum(r['electors_2021'] for r in rows_out)
    total_elec_2011 = sum(r['electors_2011'] for r in rows_out)
    print(f"\n=== Totals ===")
    print(f"  Sum population 2011: {total_pop:,} (state 91.3M; cov {100 * total_pop / 91_276_115:.1f}%)")
    print(f"  Sum electors 2021: {total_elec_2021:,} (state ~72.9M)")
    print(f"  Sum electors 2011: {total_elec_2011:,} (state 56.3M)")

    # Party breakdown 2021
    from collections import Counter
    parties = Counter(r['winner_party_2021'] for r in rows_out if r['winner_party_2021'])
    print(f"\n=== 2021 winner parties ===")
    for p, c in parties.most_common(10):
        print(f"  {p}: {c}")
