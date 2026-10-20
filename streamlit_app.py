from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
STATIC_DASHBOARD_FILE = APP_DIR / "static" / "Branch_Gap_Radar_Pro.html"
DASHBOARD_URL = "/~/+/app/static/Branch_Gap_Radar_Pro.html"

st.set_page_config(
    page_title="Branch Gap Radar Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu, header, footer { visibility: hidden; }
      .stApp { background: #f4f7fb; }
      .block-container {
        max-width: 100%;
        padding: 0 !important;
      }
      [data-testid="stAppViewContainer"] > .main {
        overflow: hidden;
      }
      iframe[title="streamlit.components.v1.html"] {
        display: block;
        border: 0;
        width: 100%;
      }
      .launch-card {
        max-width: 760px;
        margin: 11vh auto 24px;
        padding: 42px;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        background: #ffffff;
        box-shadow: 0 22px 60px rgba(15, 23, 42, .09);
        text-align: center;
      }
      .launch-mark {
        display: grid;
        place-items: center;
        width: 58px;
        height: 58px;
        margin: 0 auto 18px;
        border-radius: 16px;
        background: #2563eb;
        color: #ffffff;
        font-size: 22px;
        font-weight: 800;
      }
      .launch-card h1 { margin: 0; color: #172033; }
      .launch-card p { color: #64748b; line-height: 1.65; }
    </style>
    """,
    unsafe_allow_html=True,
)


if not STATIC_DASHBOARD_FILE.exists():
    st.error("Dashboard HTML file is missing from the deployment.")
    st.stop()

st.markdown(
    """
    <section class="launch-card">
      <div class="launch-mark">BG</div>
      <h1>Branch Gap Radar Pro</h1>
      <p>Open the full dashboard to upload your stock Excel file, review branch gaps and download the professional multi-sheet report.</p>
    </section>
    """,
    unsafe_allow_html=True,
)
st.link_button(
    "Open Branch Gap Radar Pro",
    DASHBOARD_URL,
    type="primary",
    use_container_width=True,
)
st.caption("Excel data is processed inside your browser and is not stored by this Streamlit app.")
