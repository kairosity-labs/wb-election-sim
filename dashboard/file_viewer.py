import re
from pathlib import Path

import streamlit as st

from csv_viewer import render_csv_viewer
from events_viewer import render_events

CONSTITUENCIES_DIR = Path(__file__).parent.parent / "constituency_data" / "constituencies"
YEARS = ["2019", "2021", "2024"]


def _get_constituency_folder(ac_no: int) -> Path | None:
    for folder in CONSTITUENCIES_DIR.iterdir():
        if folder.is_dir() and re.match(rf"^{ac_no:03d}_", folder.name):
            return folder
    return None


def _read_file(path: Path) -> str | None:
    if path.exists() and path.stat().st_size > 0:
        return path.read_text(encoding="utf-8")
    return None


def _render_collapsible_markdown(content: str) -> None:
    """Split markdown on ## headings and render each section in an expander."""
    # Split on lines that start with one or more # followed by a space
    parts = re.split(r"(?m)^(#{1,6} .+)$", content)

    # parts alternates: [pre-heading text, heading, body, heading, body, ...]
    preamble = parts[0].strip()
    if preamble:
        st.markdown(preamble)

    i = 1
    while i < len(parts):
        heading_line = parts[i]          # e.g. "## B. Population & Electorate"
        body = parts[i + 1] if i + 1 < len(parts) else ""
        label = heading_line.lstrip("#").strip()
        with st.expander(label, expanded=False):
            st.markdown(body.strip())
        i += 2


def render_file_viewer(ac_no: int, ac_name: str) -> None:
    st.subheader(f"AC {ac_no:03d} — {ac_name}")

    folder = _get_constituency_folder(ac_no)
    if folder is None:
        st.error("Constituency folder not found.")
        return

    available_years = [y for y in YEARS if (folder / y).is_dir()]
    if not available_years:
        st.warning("No year data found for this constituency.")
        return

    # Top-level tabs: one per year + a shared Events tab
    top_tabs = st.tabs(available_years + ["Events"])
    year_tabs = top_tabs[: len(available_years)]
    events_tab = top_tabs[-1]

    for tab, year in zip(year_tabs, available_years):
        with tab:
            year_dir = folder / year
            ac_slug = folder.name

            data_md_path = year_dir / f"{ac_slug}_{year}.md"
            narrative_path = year_dir / "narrative.md"
            csv_dir = year_dir / "csv"

            file_tabs = st.tabs(["data.md", "narrative.md", "CSVs"])

            with file_tabs[0]:
                content = _read_file(data_md_path)
                if content:
                    _render_collapsible_markdown(content)
                else:
                    st.info("data.md not yet populated for this year.")

            with file_tabs[1]:
                content = _read_file(narrative_path)
                if content:
                    _render_collapsible_markdown(content)
                else:
                    st.info("narrative.md not yet populated for this year.")

            with file_tabs[2]:
                if csv_dir.is_dir():
                    render_csv_viewer(csv_dir)
                else:
                    st.info("No CSV folder for this year.")

    with events_tab:
        render_events(folder)
