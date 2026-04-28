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

selected_ac = render_map()

if selected_ac:
    st.divider()
    ac_name_map = get_ac_name_map()
    ac_name = ac_name_map.get(selected_ac, f"AC {selected_ac}")
    render_file_viewer(selected_ac, ac_name)
else:
    st.markdown(
        """
        <div style="
            margin-top: 2rem;
            color: #aaa;
            font-size: 1.05rem;
            text-align: center;
        ">
            Click a highlighted constituency on the map to view its data.
        </div>
        """,
        unsafe_allow_html=True,
    )
