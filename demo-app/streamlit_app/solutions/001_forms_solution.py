import streamlit as st
import pandas as pd
from streamlit_app.connections.data import fetch_belgian_weather_data

st.set_page_config(layout="wide")
st.title("🌧️ Belgian Weather Dashboard 2025")


# --- SOLUTION FOR ASSIGNMENT 2 ---
# We add the @st.cache_data decorator.
@st.cache_data(show_spinner="Fetching Belgian weather data")
def load_data():
    return fetch_belgian_weather_data()


# Load the data (now cached!)
main_df = load_data()

# --- SOLUTION FOR ASSIGNMENT 1 ---

st.header("Assignment 1: Interactive Filter Form")

# Get the dynamic values for the filters from our DataFrame

st.write("Use the filters below to control the data shown in the table.")

# 2. Create the multiselect for stations
all_stations = main_df["station_name"].unique()
selected_stations = st.multiselect(
    "Choose a selection of Belgian weather stations",
    options=all_stations,
    default=None,
    placeholder="No stations selected",
)

# Date range slider, boundaries are dynamically determined
min_date = main_df["date"].min()
max_date = main_df["date"].max()
selected_date_range = st.slider(
    "Select Date Range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    format="YYYY-MM-DD",
)

# Add a button
submitted = st.button("Apply Filters")


if submitted:
    # Use the filter values to create a new, filtered DataFrame
    df_filtered = main_df.loc[
        (main_df["station_name"].isin(selected_stations))
        & (main_df["date"] >= pd.to_datetime(selected_date_range[0]))
        & (main_df["date"] <= pd.to_datetime(selected_date_range[1]))
    ]

    st.dataframe(df_filtered)

    # Show stations on a map of Belgium
    st.subheader(
        f"Map of {len(df_filtered['station_name'].unique())} selected stations"
    )
    st.map(df_filtered, latitude="lat", longitude="lon")

else:
    st.info("Click 'Apply Filters' to see the data.")
