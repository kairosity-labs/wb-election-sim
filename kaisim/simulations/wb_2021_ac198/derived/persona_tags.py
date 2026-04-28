"""Generic persona-tag derivation that works across all 10 calibrated ACs.

Tags are the matching surface between a persona and a news event's `tags` list.
This file uses ONLY canonical axis fields shared by all 10 ACs (per the
NORMALIZED_SCHEMA v1) — so it can be copied verbatim into any AC's
`derived/persona_tags.py`.

Some AC-localized tags (matua_refugee, petrapole_economy, garden_worker,
rajbanshi_assertive) live in the AC-specific persona_tags.py if present;
this generic version covers the universal ones.

Vocabulary (must match the news YAMLs' tags + valence keys):

    # identity
    woman, elderly, school_age_household,
    upper_caste_hindu, bhadralok,
    matua_refugee, muslim_voter,
    sc_voter, st_voter, obc_voter,

    # economic / occupational
    cultivator, ag_labourer, urban_trader,
    out_migrant_household, govt_employee,
    bpl_household, lower_middle_household,

    # welfare beneficiary (5 active 2019 schemes)
    krishak_bandhu_beneficiary, kanyashree_household,
    sabuj_sathi_household, swasthya_sathi_beneficiary,
    khadya_sathi_beneficiary,

    # prior-party signals (used by loss_aversion_kicker, masked in
    # `blind_to_prior` simulation variant)
    bjp_supporter, tmc_supporter, left_inc_supporter,
"""
from __future__ import annotations


# Centralized list of the prior-party tags. Variant C (blind_to_prior) drops
# these from each agent's tag set BEFORE they're delivered to targeting,
# so the news scorer can't preferentially route negative-valence events
# at the agent's existing party — which biases simulation toward "this
# agent stays put because nothing salient reaches them."
PRIOR_PARTY_TAGS = frozenset({
    "bjp_supporter",
    "tmc_supporter",
    "left_inc_supporter",
})


def derive_tags(persona) -> set[str]:
    """Tag set for one persona, derived from canonical axis fields.

    Persona is the kaisim.pipeline.core.persona.Persona dataclass, so we
    read from `persona.fields` (= canonical codes, see NORMALIZED_SCHEMA).
    """
    f = persona.fields
    tags: set[str] = set()

    # ---- identity ----
    religion = f.get("religion")
    if religion == "Muslim":
        tags.add("muslim_voter")

    caste = f.get("caste")
    # Generic SC tags — every AC has one of {Namasudra_Matua, Bagdi, Poundra,
    # Other_SC, Rajbanshi_SC, etc.}; bucket all into sc_voter.
    sc_codes = {
        "Namasudra_Matua", "Bagdi", "Poundra", "Other_SC",
        "Rajbanshi_SC", "Bhumij_SC", "Lohar_SC",
    }
    if caste in sc_codes:
        tags.add("sc_voter")
    if caste == "Namasudra_Matua" and f.get("migration") == "Bangladesh":
        tags.add("matua_refugee")

    if caste in {"ST_total"} or (caste and caste.startswith("ST_")):
        tags.add("st_voter")
    if caste == "OBC_specific":
        tags.add("obc_voter")
    if caste == "UC_bhadralok":
        tags.add("upper_caste_hindu")
        tags.add("bhadralok")

    # ---- demographic ----
    if f.get("gender") == "Female":
        tags.add("woman")
    if f.get("age_cohort") in {"63_67", "68plus"}:
        tags.add("elderly")
    if f.get("age_cohort") in {"18_22", "23_27"} and \
       f.get("workforce_status") == "Student":
        tags.add("school_age_household")

    # ---- occupational ----
    occ = f.get("occupation", "")
    if occ == "Cultivator":
        tags.add("cultivator")
    elif occ == "Agricultural_labourer":
        tags.add("ag_labourer")
    elif occ in {"Trade_retail", "Transport"}:
        tags.add("urban_trader")
    elif occ == "Out_migrant_worker":
        tags.add("out_migrant_household")
    elif occ == "Government_services_teachers":
        tags.add("govt_employee")

    # ---- economic strata ----
    econ = f.get("economic_status")
    if econ == "BPL_household":
        tags.add("bpl_household")
    elif econ == "Above_Poverty_Line_low_income":
        tags.add("lower_middle_household")

    # ---- welfare beneficiaries (only ACs that derive welfare_exposure) ----
    we = f.get("welfare_exposure") or {}
    for scheme, on in we.items():
        if not on:
            continue
        tags.add(f"{scheme.lower()}_beneficiary")
    # household-level proxies for kanyashree/sabuj_sathi
    if we.get("Kanyashree"):
        tags.add("kanyashree_household")
    if we.get("Sabuj_Sathi"):
        tags.add("sabuj_sathi_household")

    # ---- prior-party tags ----
    initial_vote = f.get("vote_2019_LS")
    if initial_vote == "BJP":
        tags.add("bjp_supporter")
    elif initial_vote == "AITC":
        tags.add("tmc_supporter")
    elif initial_vote in {"INC", "LF"}:
        tags.add("left_inc_supporter")

    return tags


def derive_media_engagement(persona) -> float:
    """0.3 (no asset) to 1.5 (TV+Smartphone+Computer) multiplier on broadcast reach."""
    am = persona.fields.get("asset_media") or {}
    score = 0.3
    if am.get("TV"):         score += 0.4
    if am.get("Smartphone"): score += 0.4
    if am.get("Computer"):   score += 0.2
    if am.get("Mobile"):     score += 0.1
    return round(min(1.5, score), 2)
