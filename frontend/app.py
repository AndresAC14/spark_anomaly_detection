import streamlit as st
import requests
import pandas as pd
from streamlit_autorefresh import st_autorefresh

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Real-Time Alerts Dashboard", page_icon="🔔")

# Refresh every 10 seconds (10000 ms)
st_autorefresh(interval=10000, key="alertrefresh")

st.title("Real-Time Alerts Dashboard")

def fetch_alerts():
    try:
        response = requests.get(f"{API_URL}/alerts")
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except Exception as e:
        st.error(f"Failed to fetch alerts: {e}")
        return []

alerts = fetch_alerts()
alert_count = len(alerts)

# Bell icon with badge
st.markdown(
    f"""
    <style>
    .notification {{
        position: relative;
        display: inline-block;
        font-size: 24px;
        margin-right: 10px;
    }}
    .badge {{
        position: absolute;
        top: -5px;
        right: -10px;
        padding: 5px 10px;
        border-radius: 50%;
        background: red;
        color: white;
        font-size: 12px;
    }}
    </style>

    <div class="notification">
        🔔
        <span class="badge">{alert_count}</span>
    </div>
    """,
    unsafe_allow_html=True
)

# Display alerts if available
if alert_count > 0:
    with st.expander("View Alerts"):
        df = pd.DataFrame(alerts)
        st.dataframe(df)
else:
    st.info("No alerts available yet.")
