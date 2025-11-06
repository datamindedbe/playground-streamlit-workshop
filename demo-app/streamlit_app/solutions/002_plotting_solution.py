import streamlit as st
import plotly.express as px
from streamlit_app.connections.data import fetch_belgian_weather_data

st.set_page_config(layout="wide")
st.title("📊 Belgian Weather plots")


@st.cache_data(show_spinner="Fetching Belgian weather data")
def load_data():
    return fetch_belgian_weather_data()


df = load_data()

st.header("Assignment 1: Plotting a Pie Chart")

if not df.empty:
    total_precip_df = df.groupby("station_name")["precipitation_mm"].sum().reset_index()

    fig_pie = px.pie(
        total_precip_df,
        names="station_name",
        values="precipitation_mm",
        title="Total Annual Precipitation (mm) by Station",
    )
    st.plotly_chart(fig_pie)
else:
    st.info("Data is empty, skipping pie chart.")


st.header("Assignment 2: Plotting a Boxplot")

if not df.empty:
    # ANo aggregations for boxplots
    fig_box = px.box(
        df,
        x="station_name",
        y="avg_temp_celsius",
        color="station_name",  # Different color for each station
        title="Temperature Distribution by Station (2025)",
        labels={
            "station_name": "Station",
            "avg_temp_celsius": "Average Daily Temperature (°C)",
        },
    )

    st.plotly_chart(fig_box, use_container_width=True)
else:
    st.info("Data is empty, skipping box plot.")
