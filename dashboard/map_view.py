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

    m = folium.Map(
        location=[23.5, 87.3],
        zoom_start=7,
        tiles="CartoDB positron",
        prefer_canvas=True,
    )

    inactive_features = []
    active_features = []
    for feature in gj["features"]:
        if feature["properties"]["AC_NO"] in active_acs:
            active_features.append(feature)
        else:
            inactive_features.append(feature)

    # Single batch layer for all 284 inactive ACs (no click needed)
    folium.GeoJson(
        {"type": "FeatureCollection", "features": inactive_features},
        style_function=lambda _: {
            "fillColor": INACTIVE_COLOR,
            "fillOpacity": 0.30,
            "color": "#bbb",
            "weight": 0.6,
        },
        tooltip=folium.GeoJsonTooltip(
            fields=["AC_NO", "AC_NAME"],
            aliases=["AC:", "Name:"],
            sticky=False,
        ),
        name="inactive",
    ).add_to(m)

    # Individual layer per active AC — popup contains just the AC number (parsed on click)
    for feature in active_features:
        ac_no = feature["properties"]["AC_NO"]
        ac_name = feature["properties"]["AC_NAME"]
        is_selected = ac_no == selected_ac

        folium.GeoJson(
            feature,
            style_function=lambda _, no=ac_no, sel=selected_ac: {
                "fillColor": SELECTED_COLOR if no == sel else ACTIVE_COLOR,
                "fillOpacity": 0.85 if no == sel else 0.65,
                "color": "#800" if no == sel else "#555",
                "weight": 2.5 if no == sel else 1.5,
            },
            tooltip=folium.Tooltip(
                f"<b>AC {ac_no:03d} — {ac_name}</b><br><i>Click to view data</i>",
                sticky=True,
            ),
            popup=folium.Popup(str(ac_no), max_width=10, show=False),
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
        returned_objects=["last_object_clicked_popup"],
        key="wb_map",
    )

    popup_val = result.get("last_object_clicked_popup") if result else None

    if popup_val is not None:
        try:
            ac_no = int(str(popup_val).strip())
            if ac_no in active_acs and ac_no != selected_ac:
                st.session_state["selected_ac"] = ac_no
                st.rerun()
        except ValueError:
            pass

    return st.session_state.get("selected_ac")
