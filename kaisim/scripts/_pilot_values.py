"""
_pilot_values.py — AC-specific tier-E values for the 10 pilot profiles.

For cells where AC-level research (CDB rollup or ward-level data) materially
deviates from the district rollup already in the CSV, these values override.
Both old and new are tier E, but the pilot is more specific; the _fill_ac.py
merger overwrites when tiers are equal.

For cells where district rollup is already reasonable, NOT populated here —
keep the district value.

Each pilot's full narrative + source URLs lives in constituencies/NNN_*.md §8.
"""

PILOTS = {
    95: {
        "name": "Bangaon Uttar",
        "sources_ref": "see /constituencies/095_bangaon_uttar.md §8",
        "values": {
            # AC 95: 7 GPs of CDB Bangaon + Bangaon Municipality. Pre-existing
            # in _fill_ac_95.py; repopulate to ensure consistency.
            "hindu_pct": (85.6, "E"),
            "muslim_pct": (13.7, "E"),
            "christian_pct": (0.3, "E"),
            "sarna_orp_pct": (0.0, "E"),
            "other_religion_pct": (0.4, "E"),
            "sc_total_pct": (46.0, "E"),
            "namasudra_matua_pct_est": (40.0, "E"),
            "st_total_pct": (3.6, "E"),
            "bengali_pct": (99.0, "E"),
            "hindi_pct": (0.5, "E"),
            "urdu_pct": (0.3, "E"),
            "literacy_overall_pct": (80.6, "E"),
            "literacy_male_pct": (84.3, "E"),
            "literacy_female_pct": (74.8, "E"),
            "agri_hh_pct": (55.0, "E"),
            "cultivator_pct": (20.0, "E"),
            "ag_labourer_pct": (30.0, "E"),
            "out_migrant_worker_pct_est": (11.0, "D"),
            "sir_deletion_count_est": (34109, "D"),
            "sir_deletion_pct_est": (12.4, "E"),
            "uc_bhadralok_pct_est": (10.0, "E"),
        },
    },
    210: {
        "name": "Nandigram",
        "sources_ref": "see /constituencies/210_nandigram.md §10",
        "values": {
            # AC 210: Nandigram-I + Nandigram-II CDBs.
            # Muslim ~+11pp above district (34% of Nandigram-I block, 12% of -II).
            "hindu_pct": (74.0, "E"),
            "muslim_pct": (25.9, "E"),
            "christian_pct": (0.0, "E"),
            "other_religion_pct": (0.1, "E"),
            "sarna_orp_pct": (0.0, "E"),
            "sc_total_pct": (16.5, "E"),
            "st_total_pct": (0.1, "E"),
            "bengali_pct": (98.5, "E"),
            "hindi_pct": (1.0, "E"),
            "urdu_pct": (0.3, "E"),
            "other_lang_pct": (0.2, "E"),
            "literacy_overall_pct": (86.5, "E"),
            "literacy_male_pct": (90.4, "E"),
            "literacy_female_pct": (82.3, "E"),
            "cultivator_pct": (16.0, "E"),
            "ag_labourer_pct": (46.0, "E"),
            "agri_hh_pct": (60.0, "E"),
            "fishworker_pct_est": (5.0, "E"),
            "out_migrant_worker_pct_est": (10.0, "D"),
            "sir_deletion_count_est": (2826, "D"),
            "sir_deletion_pct_est": (1.0, "E"),
            # Mahishya OBC is the headline caste (~50% of AC)
            "obc_mahishya_pct_est": (50.0, "E"),
            "uc_bhadralok_pct_est": (10.0, "E"),
        },
    },
    159: {
        "name": "Bhabanipur",
        "sources_ref": "see /constituencies/159_bhabanipur.md §8",
        "values": {
            # AC 159: KMC wards in Kolkata South. Bhabanipur ~42% Bengali Hindu
            # + 34% non-Bengali Hindu + 22-24% Muslim "mini-India" ward profile.
            "hindu_pct": (76.0, "E"),
            "muslim_pct": (22.0, "E"),
            "christian_pct": (0.9, "E"),
            "other_religion_pct": (1.1, "E"),
            "sarna_orp_pct": (0.0, "E"),
            "sc_total_pct": (5.4, "A"),  # Kolkata district Census 2011 tier A
            "st_total_pct": (0.2, "A"),
            "bengali_pct": (50.0, "E"),
            "hindi_pct": (30.0, "E"),
            "urdu_pct": (14.0, "E"),
            "other_lang_pct": (6.0, "E"),
            "literacy_overall_pct": (89.0, "E"),  # ward 70 = 94.2% A; high-literate urban
            "sir_deletion_count_est": (47094, "D"),
            "sir_deletion_pct_est": (22.8, "D"),
            "uc_bhadralok_pct_est": (30.0, "E"),
            "industrial_pct_est": (5.0, "E"),
            "govt_employee_pct_est": (12.0, "E"),
            "informal_sector_pct_est": (20.0, "E"),
        },
    },
    7: {
        "name": "Dinhata",
        "sources_ref": "see /constituencies/007_dinhata.md §10",
        "values": {
            # AC 7: Dinhata muni + Dinhata-II CDB + 4 GPs of Dinhata-I.
            # Muslim 35% (far higher than district 25.5%).
            "hindu_pct": (65.0, "E"),
            "muslim_pct": (34.5, "E"),
            "christian_pct": (0.2, "E"),
            "other_religion_pct": (0.3, "E"),
            "sarna_orp_pct": (0.0, "E"),
            "sc_total_pct": (43.9, "E"),
            "rajbanshi_pct_est": (37.0, "E"),  # AC headline; Rajbanshi ~85% of SC
            "st_total_pct": (0.45, "E"),
            "bengali_pct": (99.0, "E"),
            "rajbanshi_lang_pct": (2.0, "E"),  # Census L1 under-reports
            "hindi_pct": (0.5, "E"),
            "literacy_overall_pct": (73.0, "E"),
            "literacy_male_pct": (78.5, "E"),
            "literacy_female_pct": (66.7, "E"),
            "cultivator_pct": (32.0, "E"),
            "ag_labourer_pct": (45.0, "E"),
            "agri_hh_pct": (65.0, "E"),
            "sir_deletion_count_est": (36000, "E"),  # pro-rata from district 2.42L
            "sir_deletion_pct_est": (11.0, "E"),
        },
    },
    69: {
        "name": "Bharatpur",
        "sources_ref": "see /constituencies/069_bharatpur.md §8",
        "values": {
            # AC 69: Bharatpur-II CDB + 5 GPs of Bharatpur-I. Muslim ~58%
            # (below district 66%; Hindu-edge of Murshidabad Muslim belt).
            "hindu_pct": (42.0, "E"),
            "muslim_pct": (58.0, "E"),
            "christian_pct": (0.0, "E"),
            "other_religion_pct": (0.0, "E"),
            "sarna_orp_pct": (0.0, "E"),
            "bengali_pct": (99.0, "E"),
            "urdu_pct": (0.5, "E"),
            "hindi_pct": (0.3, "E"),
            "sir_deletion_count_est": (26500, "E"),  # AC pro-rata from 7.48L district
            "sir_deletion_pct_est": (10.0, "E"),
            "agri_hh_pct": (65.0, "E"),
        },
    },
    23: {
        "name": "Darjeeling",
        "sources_ref": "see /constituencies/023_darjeeling.md §8",
        "values": {
            # AC 23: Darjeeling municipality + Pulbazar CDB + Rangli Rangliot CDB
            # fringes. Nepali ~75%, Buddhist 12-16%, Christian 8-10%.
            "hindu_pct": (71.5, "E"),
            "muslim_pct": (3.0, "E"),
            "christian_pct": (9.0, "E"),
            # Buddhist ~14% is the "other_religion" bucket here
            "other_religion_pct": (16.5, "E"),
            "sarna_orp_pct": (0.0, "E"),
            "sc_total_pct": (7.0, "E"),
            "st_total_pct": (10.0, "E"),
            "nepali_pct": (75.0, "E"),
            "hindi_pct": (10.0, "E"),
            "bengali_pct": (7.0, "E"),
            "other_lang_pct": (8.0, "E"),
            "urdu_pct": (0.0, "E"),
            "santhali_pct": (0.0, "E"),
            "rajbanshi_lang_pct": (0.0, "E"),
            "kurmali_pct": (0.0, "E"),
            "literacy_overall_pct": (86.5, "E"),
            "tea_worker_pct_est": (25.0, "E"),
            "uc_bhadralok_pct_est": (0.0, "E"),  # not applicable - hill caste schema differs
        },
    },
    237: {
        "name": "Binpur",
        "sources_ref": "see /constituencies/237_binpur.md §10",
        "values": {
            # AC 237: Binpur-II CDB + Jamboni CDB. Weighted from block Census 2011.
            "hindu_pct": (75.3, "E"),
            "muslim_pct": (3.2, "E"),
            "christian_pct": (0.2, "E"),
            "sarna_orp_pct": (20.8, "E"),  # Tribal religion ~21% headline
            "other_religion_pct": (0.5, "E"),
            "sc_total_pct": (16.72, "E"),
            "st_total_pct": (35.32, "E"),
            "santhal_pct_est": (32.0, "E"),  # ~90% of ST
            "oraon_pct_est": (1.0, "E"),
            "munda_pct_est": (1.0, "E"),
            "other_st_pct_est": (1.3, "E"),
            "bengali_pct": (73.3, "E"),
            "santhali_pct": (23.9, "E"),
            "kurmali_pct": (1.6, "E"),
            "hindi_pct": (1.2, "E"),
            "literacy_overall_pct": (71.3, "E"),
            "literacy_male_pct": (81.3, "E"),
            "literacy_female_pct": (61.2, "E"),
            "bpl_household_pct_secc": (68.0, "C"),  # from DHDR 2007; tier C (dated)
            "obc_kurmi_pct_est": (12.0, "E"),  # Kurmi ~10-15%
            "agri_hh_pct": (70.0, "E"),
        },
    },
    216: {
        "name": "Kanthi Dakshin",
        "sources_ref": "see /constituencies/216_kanthi_dakshin.md §8",
        "values": {
            # AC 216: Contai-I CDB + Contai municipality + parts of Deshapran.
            # More Hindu-skewed than district.
            "hindu_pct": (95.0, "E"),
            "muslim_pct": (5.0, "E"),
            "christian_pct": (0.0, "E"),
            "other_religion_pct": (0.0, "E"),
            "sarna_orp_pct": (0.0, "E"),
            "sc_total_pct": (11.5, "E"),
            "st_total_pct": (0.3, "E"),
            "obc_mahishya_pct_est": (50.0, "E"),  # Headline — 45-55% Mahishya
            "uc_bhadralok_pct_est": (10.0, "E"),
            "bengali_pct": (98.5, "E"),
            "literacy_overall_pct": (90.0, "E"),
            "fishworker_pct_est": (4.0, "E"),
            "agri_hh_pct": (45.0, "E"),
            "cultivator_pct": (22.0, "E"),
        },
    },
    281: {
        "name": "Asansol Uttar",
        "sources_ref": "see /constituencies/281_asansol_uttar.md §8",
        "values": {
            # AC 281: northern wards of Asansol Municipal Corp. Heavily urban.
            # Muslim ~18%, Hindi-speaker ~38% (much heavier than Asansol Dakshin).
            "hindu_pct": (80.0, "E"),
            "muslim_pct": (18.0, "E"),
            "christian_pct": (0.75, "E"),
            "other_religion_pct": (1.25, "E"),  # Sikh + Jain + other
            "sarna_orp_pct": (0.0, "E"),
            "sc_total_pct": (13.5, "E"),
            "st_total_pct": (2.5, "E"),
            "bengali_pct": (48.5, "E"),
            "hindi_pct": (38.5, "E"),
            "urdu_pct": (10.0, "E"),
            "other_lang_pct": (3.0, "E"),
            "literacy_overall_pct": (85.5, "E"),
            "uc_bhadralok_pct_est": (30.0, "E"),
            "industrial_pct_est": (20.0, "E"),
            "informal_sector_pct_est": (25.0, "E"),
        },
    },
    14: {
        "name": "Madarihat",
        "sources_ref": "see /constituencies/014_madarihat.md §10",
        "values": {
            # AC 14: Madarihat-Birpara CDB (tea-garden belt). ST-reserved.
            "hindu_pct": (70.0, "E"),
            "muslim_pct": (5.0, "E"),
            "christian_pct": (16.0, "E"),  # Oraon/Munda mission conversion
            "sarna_orp_pct": (7.5, "E"),  # Sarna ~6-9%
            "other_religion_pct": (1.5, "E"),  # Buddhist Tamang etc.
            "sc_total_pct": (20.0, "E"),
            "st_total_pct": (52.5, "E"),
            "oraon_pct_est": (30.0, "E"),
            "munda_pct_est": (9.0, "E"),
            "santhal_pct_est": (4.0, "E"),
            "other_st_pct_est": (9.5, "E"),
            "bengali_pct": (22.5, "E"),
            "nepali_pct": (14.0, "E"),
            "hindi_pct": (7.0, "E"),  # Sadri creole folded here
            "santhali_pct": (2.5, "E"),
            "rajbanshi_lang_pct": (6.5, "E"),
            "other_lang_pct": (47.5, "E"),  # Sadri + Kurukh + Mundari + Toto
            "literacy_overall_pct": (70.0, "E"),
            "literacy_female_pct": (62.5, "E"),
            "tea_worker_pct_est": (60.0, "E"),  # Headline
            "agri_hh_pct": (65.0, "E"),
        },
    },
}
