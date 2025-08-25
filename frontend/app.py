import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

API_URL = "http://api:8000"

st.set_page_config(page_title="Real-Time Dashboard", page_icon="📊")

st_autorefresh(interval=10000, key="datarefresh")

st.title("Real-Time Traffic & Pollution Dashboard")

# Fetch data
def fetch_data():
    try:
        resp = requests.get(f"{API_URL}/data")
        return resp.json() if resp.status_code == 200 else []
    except:
        return []

def fetch_alerts():
    try:
        resp = requests.get(f"{API_URL}/alerts")
        return resp.json() if resp.status_code == 200 else []
    except:
        return []

data = fetch_data()
alerts = fetch_alerts()

alert_count = len(alerts)
st.markdown(f"### 🔔 Alerts: {alert_count}")

if alerts:
    with st.expander("View Alerts"):
        st.dataframe(pd.DataFrame(alerts))

if data:
    df = pd.DataFrame(data)
    
    # Traffic Graph
    traffic_df = df[df['type'] == 'traffic']
    if not traffic_df.empty:
        fig_traffic = px.line(
            traffic_df,
            x='hour',
            y=['expected', 'predicted'],
            title="Traffic Intensity: Expected vs Predicted"
        )
        st.plotly_chart(fig_traffic)

    # Pollution Graph
    pollution_df = df[df['type'] == 'pollution']
    if not pollution_df.empty:
        fig_pollution = px.line(
            pollution_df,
            x='hour',
            y=['expected', 'predicted'],
            title="Pollution Level: Expected vs Predicted"
        )
        st.plotly_chart(fig_pollution)
else:
    st.info("No data received yet.")
