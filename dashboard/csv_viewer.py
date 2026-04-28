from pathlib import Path

import pandas as pd
import streamlit as st


def render_csv_viewer(csv_dir: Path) -> None:
    csv_files = sorted(csv_dir.glob("*.csv"))

    if not csv_files:
        st.info("No CSVs available for this year.")
        return

    names = [f.name for f in csv_files]
    choice = st.selectbox("Select CSV file", names, key=f"csv_select_{csv_dir}")

    if choice:
        path = csv_dir / choice
        try:
            df = pd.read_csv(path)
            st.dataframe(df, use_container_width=True)
        except Exception as e:
            st.error(f"Could not read {choice}: {e}")
