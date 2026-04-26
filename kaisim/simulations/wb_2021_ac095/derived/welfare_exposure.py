"""WB-specific welfare scheme exposure derivation, calibrated to **end-2019**.

Two functions:

`derive`:    multi-flag exposure ∈ {Krishak_Bandhu, Kanyashree, Sabuj_Sathi,
             Swasthya_Sathi, Khadya_Sathi}. Each flag is a Bernoulli decision
             based on prior persona fields (occupation, gender, age, etc.).

`dominant`:  collapses the multi-flag exposure into a single label drawn from
             {Krishak_Bandhu, Kanyashree, Sabuj_Sathi, Swasthya_Sathi,
              Khadya_Sathi, None}, per the configured WelfareOverlapReducer.
             Composite labels (from "mean" reducer) are mapped to "None" so
             the verifier can join against the vote_welfare table.

Take-up rates calibrated against end-2019 sources (auditable):

    Swasthya Sathi  ~28% population (50 lakh families / ~9 cr pop). Universal
                    coverage only declared December 2020. Pre-2020 enrollment
                    skewed to SHG members, ASHA / ICDS / civic volunteers,
                    and select target groups.
                    [Down to Earth, 1 Dec 2020]
                    [Tata AIG / HDFC ERGO scheme summaries]

    Krishak Bandhu  ~5% by 2019 LS (May 2019, scheme launched Jan 2019); ~10%
                    by end-2019 (3 lakh enrolled at Dec-2019 Duare Sarkar
                    camps; ~70 lakh WB farmers in total).
                    [Krishi Jagran — 3 lakh by Dec 2019]
                    [Wikipedia — Krishak Bandhu Scheme]

    Khadya Sathi    ~80% population (7.49 cr / 10 cr); higher in BPL/APL-low,
                    near-zero in upper-middle.
                    [WBPDS official help portal]

    Kanyashree      ~43% of eligible girls (13-18 unmarried in school).
                    [Wikipedia — Kanyashree Prakalpa]

    Sabuj Sathi     bicycle distributed once to Class 9-12 students; cumulative
                    ~1 cr by 2019. Active proxy ~30% of class-9-12-aged girls.

The "None" pool — voters with zero scheme exposure — must NOT be squeezed to
zero. The vote_welfare_2019 conditional table includes a "No state-scheme
exposure" row that calibrates the BJP-leaning unenrolled segment; missing
that pool causes aggregate vote miscalibration (BJP undershoot).
"""
from __future__ import annotations

from pipeline.persona_generation.blending import make_welfare_overlap


def derive(rng, ctx, axis, persona, persona_config=None, **kwargs):
    occ      = persona.get("occupation")
    gender   = persona.get("gender")
    age      = persona.get("age_cohort")
    econ     = persona.get("economic_status")
    marital  = persona.get("marital_status")
    hh_type  = persona.get("household_type")
    edu      = persona.get("education")

    flags = {f: False for f in axis.flags}

    # Krishak Bandhu — very low take-up by end-2019 (scheme only 11 months old)
    if occ == "Cultivator":
        flags["Krishak_Bandhu"] = rng.random() < 0.10
    elif occ == "Agricultural_labourer":
        flags["Krishak_Bandhu"] = rng.random() < 0.05

    # Kanyashree + Sabuj Sathi are HOUSEHOLD-LEVEL schemes targeting school-age
    # girls (mostly 13-18, i.e. mostly NON-voters). The CSV row label
    # ("Kanyashree (girl-student HH)") is explicit about this. Three pathways:
    #   1. Personal: voter is herself a still-in-school 18_22 female
    #   2. Parental: voter is a married parent of a likely school-age girl
    #   3. Grandparental: voter is 53+ in a Joint_HH with school-age granddaughter
    # WB ~22 lakh active K1+K2 / ~2 cr voter HHs ≈ 11% of HHs, so ~22% of adult
    # voters in those HHs perceive the household-level effect.
    p_kany = 0.0
    p_sabuj = 0.0

    # 1. Personal eligibility (still-in-school 18-22 female)
    if gender == "Female" and age == "18_22" and edu in {"Higher_Secondary", "Graduate", "Postgraduate"}:
        p_kany = max(p_kany, 0.40)
        p_sabuj = max(p_sabuj, 0.30)

    # 2. Parental — currently married, age compatible with having a 13-18 daughter
    #    (mother typically 33-48; broaden to 28-52 for late/early kids).
    if marital == "Currently_married":
        if age in {"33_37", "38_42", "43_47"}:
            p_kany = max(p_kany, 0.30)
            p_sabuj = max(p_sabuj, 0.20)
        elif age in {"28_32", "48_52"}:
            p_kany = max(p_kany, 0.15)
            p_sabuj = max(p_sabuj, 0.10)

    # 3. Grandparental — Joint_HH with a school-age granddaughter
    if age in {"53_57", "58_62", "63_67"} and hh_type in {"Joint_HH", "Extended_multi_generation"}:
        p_kany = max(p_kany, 0.10)
        p_sabuj = max(p_sabuj, 0.07)

    flags["Kanyashree"] = rng.random() < p_kany
    flags["Sabuj_Sathi"] = rng.random() < p_sabuj

    # Swasthya Sathi — pre-universal-rollout; ~28% population end-2019,
    # skewed to SHG / ASHA / ICDS women + lower-income groups
    if gender == "Female" and econ in {"BPL_household", "Above_Poverty_Line_low_income"}:
        # SHG / ASHA / ICDS networks concentrated among lower-income women
        flags["Swasthya_Sathi"] = rng.random() < 0.45
    elif econ in {"BPL_household", "Above_Poverty_Line_low_income"}:
        flags["Swasthya_Sathi"] = rng.random() < 0.30
    elif econ == "Lower_middle":
        flags["Swasthya_Sathi"] = rng.random() < 0.20
    else:
        flags["Swasthya_Sathi"] = rng.random() < 0.10

    # Khadya Sathi — ~80% population, steeply income-tilted
    if econ in {"BPL_household", "Above_Poverty_Line_low_income"}:
        flags["Khadya_Sathi"] = rng.random() < 0.95
    elif econ == "Lower_middle":
        flags["Khadya_Sathi"] = rng.random() < 0.80
    elif econ == "Middle":
        flags["Khadya_Sathi"] = rng.random() < 0.40
    else:
        flags["Khadya_Sathi"] = rng.random() < 0.10

    return flags


def dominant(rng, ctx, axis, persona, persona_config=None, **kwargs):
    flags = persona.get("welfare_exposure", {})
    method = "precedence"
    precedence = ["Krishak_Bandhu", "Kanyashree", "Sabuj_Sathi",
                  "Swasthya_Sathi", "Khadya_Sathi"]
    if persona_config is not None:
        method = persona_config.get("vote.welfare_overlap.method", method)
        precedence = persona_config.get("vote.welfare_overlap.precedence", precedence)
    reducer = make_welfare_overlap(method, precedence)
    vote_welfare = ctx.joint("vote_given_welfare")
    label, _ = reducer.reduce(flags, vote_welfare.table, vote_welfare.parties)
    if "+" in label:
        return "None"
    return label
