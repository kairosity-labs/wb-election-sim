"""WB-specific: derive identity tags + media engagement from a Persona.

Tag vocabulary matches what the news events YAML uses for `tags` and `valence`:
    matua_refugee, woman, elderly, upper_caste_hindu, bhadralok, muslim_voter,
    cultivator, ag_labourer, urban_trader, petrapole_economy,
    out_migrant_household, school_age_household,
    lakshmir_bhandar_beneficiary, krishak_bandhu_beneficiary,
    swasthya_sathi_beneficiary, khadya_sathi_beneficiary,
    kanyashree_household, sabuj_sathi_household,
    bjp_supporter, tmc_supporter
"""
from __future__ import annotations


def derive_tags(persona) -> set[str]:
    f = persona.fields
    tags: set[str] = set()

    # Religion + caste
    if f.get("religion") == "Muslim":
        tags.add("muslim_voter")
    if f.get("caste") == "Namasudra_Matua" and f.get("migration") == "Bangladesh":
        tags.add("matua_refugee")
    if f.get("caste") == "UC_bhadralok":
        tags.add("upper_caste_hindu")
        tags.add("bhadralok")
    if f.get("caste") in {"OBC_specific", "Other_Hindu_middle_castes"}:
        tags.add("upper_caste_hindu")  # mild — they're not SC

    # Demographic
    if f.get("gender") == "Female":
        tags.add("woman")
    if f.get("age_cohort") in {"63_67", "68plus"}:
        tags.add("elderly")
    if f.get("age_cohort") in {"18_22", "23_27"} and \
       f.get("workforce_status") == "Student":
        tags.add("school_age_household")

    # Occupational
    occ = f.get("occupation", "")
    if occ == "Cultivator":
        tags.add("cultivator")
    elif occ == "Agricultural_labourer":
        tags.add("ag_labourer")
    elif occ in {"Trade_retail", "Transport"}:
        tags.add("urban_trader")
        if occ == "Transport":
            tags.add("petrapole_economy")
    elif occ == "Out_migrant_worker":
        tags.add("out_migrant_household")

    # Welfare beneficiaries (from welfare_exposure flags)
    we = f.get("welfare_exposure") or {}
    for scheme, on in we.items():
        if on:
            tags.add(f"{scheme.lower()}_beneficiary")

    # Household-level proxy: parental Kanyashree/Sabuj exposure
    if we.get("Kanyashree"):
        tags.add("kanyashree_household")
    if we.get("Sabuj_Sathi"):
        tags.add("sabuj_sathi_household")

    # Initial party signal from generated 2019 vote prior
    initial_vote = f.get("vote_2019_LS")
    if initial_vote == "BJP":
        tags.add("bjp_supporter")
    elif initial_vote == "AITC":
        tags.add("tmc_supporter")

    return tags


def derive_media_engagement(persona) -> float:
    """0.3 (no-asset) to 1.4 (smartphone+TV+computer) multiplier on broadcast reach."""
    am = persona.fields.get("asset_media") or {}
    score = 0.3
    if am.get("TV"):           score += 0.4
    if am.get("Smartphone"):   score += 0.4
    if am.get("Computer"):     score += 0.2
    if am.get("Mobile"):       score += 0.1
    return round(min(1.5, score), 2)
