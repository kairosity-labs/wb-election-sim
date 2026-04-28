import copy
import json
import re
from pathlib import Path

import folium
import streamlit as st
from streamlit_folium import st_folium

CONSTITUENCIES_DIR = Path(__file__).parent.parent / "constituency_data" / "constituencies"
GEOJSON_PATH = Path(__file__).parent / "data" / "wb_constituencies.geojson"

ACTIVE_COLOR = "#E07B39"
INACTIVE_COLOR = "#CCCCCC"
SELECTED_COLOR = "#C0392B"


@st.cache_data
def load_geojson() -> dict:
    with open(GEOJSON_PATH) as f:
        return json.load(f)


@st.cache_data
def get_active_ac_numbers() -> frozenset:
    active = set()
    for folder in CONSTITUENCIES_DIR.iterdir():
        if folder.is_dir():
            m = re.match(r"^(\d+)_", folder.name)
            if m:
                active.add(int(m.group(1)))
    return frozenset(active)


@st.cache_data
def get_ac_name_map() -> dict:
    gj = load_geojson()
    return {f["properties"]["AC_NO"]: f["properties"]["AC_NAME"] for f in gj["features"]}


def build_map(selected_ac: int | None) -> folium.Map:
    gj = load_geojson()
    active_acs = get_active_ac_numbers()

    m = folium.Map(location=[23.5, 87.3], zoom_start=7, tiles="CartoDB positron")

    # ── Inactive constituencies: single batch layer, no click needed ──────────
    inactive = {
        "type": "FeatureCollection",
        "features": [
            f for f in gj["features"] if f["properties"]["AC_NO"] not in active_acs
        ],
    }
    folium.GeoJson(
        inactive,
        style_function=lambda _: {
            "fillColor": INACTIVE_COLOR,
            "fillOpacity": 0.28,
            "color": "#bbb",
            "weight": 0.5,
        },
        tooltip=folium.GeoJsonTooltip(
            fields=["AC_NO", "AC_NAME"],
            aliases=["AC:", "Name:"],
            sticky=False,
            labels=True,
        ),
        name="inactive",
    ).add_to(m)

    # ── Active constituencies: one layer each, GeoJsonTooltip for click ID ───
    # GeoJsonTooltip binds to individual feature paths (sourceTarget),
    # so last_object_clicked_tooltip is set via the safe extractContent() branch.
    for feature in gj["features"]:
        ac_no = feature["properties"]["AC_NO"]
        if ac_no not in active_acs:
            continue

        ac_name = feature["properties"]["AC_NAME"]
        is_selected = ac_no == selected_ac

        # Inject a clean, parseable _id field so we can extract it from tooltip text
        feat = copy.deepcopy(feature)
        feat["properties"]["_id"] = f"ACNO_{ac_no:03d}"

        fill = SELECTED_COLOR if is_selected else ACTIVE_COLOR
        opacity = 0.85 if is_selected else 0.65
        border = "#800" if is_selected else "#555"
        weight = 2.5 if is_selected else 1.5

        folium.GeoJson(
            feat,
            style_function=lambda _, f=fill, o=opacity, b=border, w=weight: {
                "fillColor": f,
                "fillOpacity": o,
                "color": b,
                "weight": w,
            },
            # GeoJsonTooltip → binds to each feature's own path element
            tooltip=folium.GeoJsonTooltip(
                fields=["_id", "AC_NAME"],
                aliases=["", ""],
                sticky=True,
                labels=False,
                style="font-size:13px;padding:4px 8px;",
            ),
            name=f"ac_{ac_no}",
        ).add_to(m)

    return m


def render_map() -> int | None:
    selected_ac = st.session_state.get("selected_ac")
    active_acs = get_active_ac_numbers()

    m = build_map(selected_ac)

    result = st_folium(
        m,
        use_container_width=True,
        height=580,
        returned_objects=["last_object_clicked_tooltip"],
        key="wb_map",
    )

    tooltip_val = (result or {}).get("last_object_clicked_tooltip")
    if tooltip_val:
        # tooltip innerText looks like "ACNO_003\nCOOCHBEHAR UTTAR (SC)"
        hit = re.search(r"ACNO_0*(\d+)", str(tooltip_val))
        if hit:
            ac_no = int(hit.group(1))
            if ac_no in active_acs and ac_no != selected_ac:
                st.session_state["selected_ac"] = ac_no
                st.rerun()

    return st.session_state.get("selected_ac")
