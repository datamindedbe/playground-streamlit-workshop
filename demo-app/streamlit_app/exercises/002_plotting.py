import streamlit as st

st.header("Plotting")

st.subheader("Assignment 1: Plotting a Pie Chart")

st.info(
    "Looking for an extra layer of plotting polish? [plotly](https://plotly.com/python/) is an interactive plotting library that plays nicely with streamlit!",
    icon="💅",
)

st.markdown("""
- Plot a pie chart showing the share of **total annual precipitation** for each weather station.
    - **Hint**: You'll need to `groupby` the `station_name` and `sum` the `precipitation_mm`.
""")

# --- your code here ---

st.subheader("Assignment 2: Plotting a Boxplot")

st.markdown("""
- Plot a **boxplot** to show the full distribution (min, max, median, quartiles) of `avg_temp_celsius` for each `station_name`.
    - Try out _both_ the built-in bar chart functionality, and the overlay with `plotly`
""")

# --- your code here ---
