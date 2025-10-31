import streamlit as st

st.title("Forms")

st.header("Assignment 1: Interactive Filter Form")

st.success(
    "We've already set up a function that queries Belgian weather data, called `fetch_belgian_weather_data`!",
    icon="✅",
)

st.markdown("""
*  Show all data on Belgian weather as a table in your app.
*  Find a way to filter your data based on **station name** (`st.multiselect`).
*  Add a **date range slider** to data filter by date (`st.slider`).
*  Display the filtered data after a button is pressed.
*  Find out a way to show the location of a weather station on a map.
    - **Hint**: Take a look at the available columns in the weather dataset
""")

# --- your code here ---

st.header("Assignment 2: Caching")

st.warning(
    "The app re-runs the *entire* BigQuery query every time something changes in the state of your app. This is slow and expensive!",
    icon="💸",
)

st.markdown("""
- Add **caching** to your `load_data()` function.
""")

# --- your code here ---
