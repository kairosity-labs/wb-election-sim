"""
Build village→AC crosswalk for West Bengal using SHRUG constituency keys.

Inputs:
  - shrid_frag_con08_key.csv : SHRID (village ID) → AC 2008 mapping with fragment weights
  - ac08_name_key.csv         : AC ID → name + district
  - wb_village_pca.csv        : 40,218 WB villages with 94 census columns
  - harvard crosswalk         : polling-booth-to-village (for validation)

Output: wb_village_ac_crosswalk.csv
Strategy:
  SHRUG's shrid2 links to 2011 Population Census via pc11 ids. We need to map
  Census 2011 village (state=19, district, subdistt, village_code) to SHRID
  using the 'shrug-pc-keys' module (not yet downloaded). For now we use a
  simpler approach: merge WB villages with the Harvard polling-booth data.
"""
import csv, os
from collections import defaultdict

BASE = '/Users/atharvapandey/Kairosity/WBData/data'

def load_harvard_crosswalk():
    """Harvard LS crosswalk: District × Block × Village → AC_no."""
    path = f'{BASE}/crosswalk/harvard_11587762.tab'
    rows = []
    with open(path, 'r') as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            rows.append({
                'district_no': row['District_no2011'].strip(),
                'district_name': row['District_name2011'].strip('" '),
                'block_no': row['Block_no2011'].strip(),
                'block_name': row['Block_name2011'].strip('" '),
                'village_code': row['Vill_no2011'].strip(),
                'village_name': row['Vill_name2011'].strip('" '),
                'ac_no': row['AC_no'].strip(),
                'ac_name': row['AC_name'].strip('" '),
                'ps_id': row['PS_id'].strip(),
                'electors': int(row['Electors']) if row['Electors'].strip().isdigit() else 0,
            })
    return rows

def aggregate_to_ac(crosswalk, pca_path):
    """Aggregate WB village PCA data to AC level using the crosswalk."""
    # Load PCA village rows
    pca_by_code = {}
    with open(pca_path, 'r') as f:
        r = csv.DictReader(f)
        for row in r:
            if row['Level'] != 'VILLAGE':
                continue
            # Key: (state_code, district_code, subdistt_code, town_village_code)
            code = row['Town/Village'].zfill(6)
            district = row['District'].zfill(3)
            subdistt = row['Subdistt'].zfill(5)
            pca_by_code[(district, subdistt, code)] = row

    print(f"PCA villages indexed: {len(pca_by_code)}")

    # Harvard crosswalk uses different codes. Build by village name within block.
    # Group crosswalk villages by (district_name, block_name, village_name)
    from collections import defaultdict
    hv_index = defaultdict(list)
    for cw in crosswalk:
        hv_index[(cw['district_name'].lower().strip(), cw['block_name'].lower().strip(), cw['village_name'].lower().strip())].append(cw)

    # AC-level aggregation: for each AC, sum PCA fields for villages mapped via Harvard
    ac_summary = defaultdict(lambda: {
        'ac_name': '',
        'villages_mapped': 0,
        'total_population': 0,
        'total_males': 0,
        'total_females': 0,
        'sc_pop': 0,
        'st_pop': 0,
        'literates': 0,
        'total_workers': 0,
        'agri_labourers': 0,
        'cultivators': 0,
        'household_industry_workers': 0,
        'other_workers': 0,
        'no_households': 0,
        'non_workers': 0,
    })

    # This is a simplified aggregation using Harvard crosswalk (LS-based, matches AC).
    # Limitations: name matching is fuzzy; Harvard is LS 2009 but WB AC delimitation
    # is also 2008, so AC numbering correspondence is valid for WB.
    mapped_villages = set()
    unmapped_pca_count = 0
    for (district, subdistt, code), row in pca_by_code.items():
        # Try to find this village in Harvard
        name = row['Name'].lower().strip()
        # Search by name (less precise)
        matches = []
        for (dn, bn, vn), items in hv_index.items():
            if vn == name:
                matches.extend(items)
        if matches:
            # Assign to first match's AC (could split weighted if multiple)
            m = matches[0]
            ac_no = m['ac_no']
            key = ac_no
            s = ac_summary[key]
            s['ac_name'] = m['ac_name']
            s['villages_mapped'] += 1
            s['total_population'] += int(row['TOT_P'] or 0)
            s['total_males'] += int(row['TOT_M'] or 0)
            s['total_females'] += int(row['TOT_F'] or 0)
            s['sc_pop'] += int(row['P_SC'] or 0)
            s['st_pop'] += int(row['P_ST'] or 0)
            s['literates'] += int(row['P_LIT'] or 0)
            s['total_workers'] += int(row['TOT_WORK_P'] or 0)
            s['agri_labourers'] += int(row.get('MAIN_AL_P', '0') or 0)
            s['cultivators'] += int(row.get('MAIN_CL_P', '0') or 0)
            s['household_industry_workers'] += int(row.get('MAIN_HH_P', '0') or 0)
            s['other_workers'] += int(row.get('MAIN_OT_P', '0') or 0)
            s['no_households'] += int(row['No_HH'] or 0)
            s['non_workers'] += int(row['NON_WORK_P'] or 0)
            mapped_villages.add(code)
        else:
            unmapped_pca_count += 1

    print(f"Mapped PCA villages to AC: {len(mapped_villages)}")
    print(f"Unmapped PCA villages: {unmapped_pca_count}")
    return ac_summary


if __name__ == '__main__':
    print("Loading Harvard crosswalk...")
    cw = load_harvard_crosswalk()
    print(f"  {len(cw)} crosswalk rows")

    # Show coverage
    acs = set(r['ac_no'] for r in cw)
    print(f"  Unique ACs: {len(acs)}")

    pca_path = f'{BASE}/census_2011/village_pca/wb_village_pca.csv'
    print(f"\nAggregating PCA to AC...")
    ac_summary = aggregate_to_ac(cw, pca_path)

    out = f'{BASE}/crosswalk/wb_ac_demographics.csv'
    fieldnames = ['ac_no','ac_name','villages_mapped','total_population','total_males','total_females',
                  'sc_pop','st_pop','literates','total_workers','agri_labourers','cultivators',
                  'household_industry_workers','other_workers','no_households','non_workers']
    with open(out, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for ac_no, s in sorted(ac_summary.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 0):
            row = {'ac_no': ac_no, **s}
            w.writerow(row)

    print(f"\nSaved: {out}")
    print(f"ACs with demographics: {len(ac_summary)}")
    # Sample
    for ac, s in list(ac_summary.items())[:3]:
        print(f"  AC {ac} ({s['ac_name']}): villages={s['villages_mapped']}, pop={s['total_population']:,}, SC={s['sc_pop']:,}, literate={s['literates']:,}")
