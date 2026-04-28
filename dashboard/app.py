import streamlit as st

from map_view import get_ac_name_map, render_map
from file_viewer import render_file_viewer

st.set_page_config(
    page_title="WB Constituency Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("West Bengal Constituency Dashboard")
st.caption(
    "10 focus constituencies are highlighted — click one to explore its data. "
    "Gray constituencies have no data yet."
)

col_map, col_viewer = st.columns([1, 1], gap="medium")

with col_map:
    selected_ac = render_map()

with col_viewer:
    if selected_ac:
        ac_name_map = get_ac_name_map()
        ac_name = ac_name_map.get(selected_ac, f"AC {selected_ac}")
        render_file_viewer(selected_ac, ac_name)
    else:
        st.markdown(
            """
            <div style="
                display: flex;
                align-items: center;
                justify-content: center;
                height: 500px;
                color: #888;
                font-size: 1.1rem;
                text-align: center;
                border: 2px dashed #ddd;
                border-radius: 8px;
            ">
                ← Click a highlighted constituency on the map<br>to view its data
            </div>
            """,
            unsafe_allow_html=True,
        )
