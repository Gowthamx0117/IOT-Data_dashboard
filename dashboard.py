import streamlit as st
import requests
import pandas as pd
import time

st.title("📊 IoT Data Dashboard")

st.write("This dashboard displays real-time temperature and humidity data.")

while True:
    try:
        response = requests.get("http://127.0.0.1:5000/get-data")
        if response.status_code == 200:
            data = response.json()
            if data:
                df = pd.DataFrame(data)
                st.line_chart(df.set_index(df.index))
            else:
                st.warning("No data received yet.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")

    time.sleep(5)  # Refresh every 5 seconds
