import streamlit as st

st.title("Plotting Belgian Weather")

st.header("Assignment 1: Plotting a Pie Chart")

st.markdown("""
**Assignment**:
- Plot a pie chart showing the share of **total annual precipitation** for each station.
    - **Hint 1**: You'll need to `groupby` the `station_name` and `sum` the `precipitation_mm`.
    - **Hint 2**: Use `st.plotly_chart` with `plotly.express.pie` for a nice chart.
""")

# --- your code here ---

st.header("Assignment 2: Plot a Bar Chart")

st.markdown("""
**Assignment**:
- Plot a **boxplot** to show the full distribution (min, max, median, quartiles) of `avg_temp_celsius` for each `station_name`.
    - **Hint 1**: Use `st.plotly_chart` with `plotly.express.box`. You can pass the full DataFrame `df` directly to it.
""")

# --- your code here ---
