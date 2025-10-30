import streamlit as st
from streamlit_app.connections.data import fetch_belgian_weather_data

st.title("Plotting")


# Get the data
df = fetch_belgian_weather_data()

st.header("Assignment 1: Plotting")

st.markdown("""
**Assignment**:

- Plot a pie chart with the level distribution
""")

# --- your code here ---

st.header("Assignment 2: Plot a bar chart")

st.markdown("""
**Assignment**:

- Plot a bar chart with the level distribution
""")


# --- your code here ---
