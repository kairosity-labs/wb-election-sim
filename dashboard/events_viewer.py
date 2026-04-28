from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components
import yaml

SCOPE_COLOR = {
    "national": "#7B2D8B",
    "state":    "#1565C0",
    "district": "#00796B",
    "AC":       "#E65100",
}
SCOPE_LABEL = {
    "national": "National",
    "state":    "State",
    "district": "District",
    "AC":       "AC",
}
INTENSITY_COLOR = ["", "#CFD8DC", "#90A4AE", "#F9A825", "#EF6C00", "#B71C1C"]

VALENCE_EMOJI = {"positive": "▲", "negative": "▼", "ambient": "◆"}
VALENCE_COLOR = {"positive": "#2E7D32", "negative": "#C62828", "ambient": "#546E7A"}


def _load_events(constituency_folder: Path) -> list[dict]:
    path = constituency_folder / "events.yaml"
    if not path.exists():
        return []
    with open(path) as f:
        data = yaml.safe_load(f)
    events = data.get("events", [])
    for e in events:
        e["_sort_date"] = str(e.get("date") or e.get("date_start") or "9999")
    return sorted(events, key=lambda e: e["_sort_date"])


def _event_card_html(ev: dict) -> str:
    slug         = ev.get("slug", "")
    date         = ev.get("date") or ev.get("date_start", "")
    date_end     = ev.get("date_end", "")
    temporal     = ev.get("temporal", "episodic")
    scope        = ev.get("scope", "AC")
    intensity    = ev.get("intensity", 1)
    headline     = ev.get("headline", "")
    summary      = ev.get("summary", "").strip()
    tags         = ev.get("tags", [])
    valence      = ev.get("valence", {})
    broadcast    = ev.get("broadcast", False)
    sources      = ev.get("sources", [])

    scope_col  = SCOPE_COLOR.get(scope, "#555")
    scope_lbl  = SCOPE_LABEL.get(scope, scope)
    dot_col    = INTENSITY_COLOR[min(max(intensity, 1), 5)]
    is_chronic = temporal == "chronic"
    border_style = "dashed" if is_chronic else "solid"
    date_range   = f"{date} → {date_end}" if date_end and date_end != date else str(date)

    tags_html = " ".join(
        f'<span style="background:#eceff1;color:#455a64;border-radius:3px;'
        f'padding:1px 6px;font-size:11px;margin:2px;">{t.replace("_"," ")}</span>'
        for t in tags
    )

    valence_html = " ".join(
        f'<span style="color:{VALENCE_COLOR.get(v,"#555")};font-size:12px;">'
        f'{VALENCE_EMOJI.get(v,"?")} {g.replace("_"," ")}</span>'
        for g, v in valence.items()
    )

    sources_html = "".join(
        f'<div style="font-size:11px;margin-top:2px;">'
        f'<a href="{s}" target="_blank" style="color:#1565c0;">{s[:80]}{"…" if len(s)>80 else ""}</a>'
        f'</div>'
        for s in sources
    ) if sources else ""

    broadcast_badge = (
        '<span style="background:#fce4ec;color:#c62828;border-radius:3px;'
        'padding:1px 6px;font-size:11px;margin-left:6px;">📡 broadcast</span>'
        if broadcast else ""
    )
    chronic_badge = (
        '<span style="background:#e8eaf6;color:#303f9f;border-radius:3px;'
        'padding:1px 6px;font-size:11px;margin-left:6px;">⟳ chronic</span>'
        if is_chronic else ""
    )

    detail_id = f"det_{slug}"

    return f"""
    <div style="display:flex;margin-bottom:16px;align-items:flex-start;">
      <!-- dot column -->
      <div style="display:flex;flex-direction:column;align-items:center;
                  width:36px;flex-shrink:0;padding-top:4px;">
        <div style="width:16px;height:16px;border-radius:50%;
                    background:{dot_col};border:2px solid #90a4ae;"></div>
        <div style="width:2px;flex:1;background:#cfd8dc;margin-top:2px;
                    border-left:2px {border_style} #b0bec5;"></div>
      </div>
      <!-- card -->
      <div style="flex:1;margin-left:12px;border:1px {border_style} #cfd8dc;
                  border-left:3px solid {scope_col};border-radius:4px;
                  background:#fafafa;overflow:hidden;">
        <!-- header row -->
        <div style="padding:8px 12px;cursor:pointer;user-select:none;"
             onclick="(function(){{
               var d=document.getElementById('{detail_id}');
               d.style.display=d.style.display==='none'?'block':'none';
               var arr=document.getElementById('{detail_id}_arr');
               arr.textContent=d.style.display==='none'?'▶':'▼';
             }})()">
          <div style="display:flex;align-items:center;justify-content:space-between;">
            <div style="font-size:11px;color:#78909c;font-family:monospace;">
              {date_range}
              <span style="background:{scope_col};color:#fff;border-radius:3px;
                           padding:1px 6px;font-size:10px;margin-left:6px;">{scope_lbl}</span>
              {'★' * intensity}<span style="color:#b0bec5;">{'☆' * (5-intensity)}</span>
              {broadcast_badge}{chronic_badge}
            </div>
            <span id="{detail_id}_arr" style="color:#90a4ae;font-size:12px;">▶</span>
          </div>
          <div style="font-size:13px;font-weight:600;color:#212121;margin-top:4px;
                      line-height:1.4;">{headline}</div>
          {f'<div style="margin-top:4px;">{valence_html}</div>' if valence_html else ''}
        </div>
        <!-- expandable detail -->
        <div id="{detail_id}" style="display:none;padding:8px 12px 12px;
                                      border-top:1px solid #e0e0e0;">
          {f'<div style="font-size:12px;color:#424242;line-height:1.6;white-space:pre-wrap;">{summary}</div>' if summary else ''}
          {f'<div style="margin-top:8px;">{tags_html}</div>' if tags_html else ''}
          {f'<div style="margin-top:8px;">{sources_html}</div>' if sources_html else ''}
        </div>
      </div>
    </div>
    """


def render_events(constituency_folder: Path) -> None:
    events = _load_events(constituency_folder)
    if not events:
        st.info("No events.yaml found for this constituency.")
        return

    scope_filter = st.multiselect(
        "Filter by scope",
        options=["national", "state", "district", "AC"],
        default=["national", "state", "district", "AC"],
        key=f"scope_filter_{constituency_folder.name}",
    )
    min_intensity = st.slider(
        "Minimum intensity",
        min_value=1, max_value=5, value=1,
        key=f"intensity_{constituency_folder.name}",
    )

    visible = [
        e for e in events
        if e.get("scope", "AC") in scope_filter
        and e.get("intensity", 1) >= min_intensity
    ]

    if not visible:
        st.info("No events match the current filters.")
        return

    legend_html = " ".join(
        f'<span style="background:{c};color:#fff;border-radius:3px;'
        f'padding:2px 8px;font-size:11px;margin:2px;">{SCOPE_LABEL[s]}</span>'
        for s, c in SCOPE_COLOR.items()
    )
    cards_html = "".join(_event_card_html(e) for e in visible)

    html = f"""
    <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
                max-width:860px;padding:4px 0;">
      <div style="margin-bottom:12px;font-size:12px;color:#78909c;">
        Scope: {legend_html}
        &nbsp;|&nbsp; Intensity: ★ low → ★★★★★ high
        &nbsp;|&nbsp; <span style="border-left:3px solid #888;padding-left:4px;">solid = episodic</span>
        &nbsp;&nbsp;<span style="border-left:3px dashed #888;padding-left:4px;">dashed = chronic</span>
      </div>
      {cards_html}
    </div>
    """

    estimated_height = 90 * len(visible) + 80
    components.html(html, height=min(estimated_height, 3200), scrolling=True)
