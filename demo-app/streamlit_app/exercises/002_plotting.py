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
- Plot a bar chart showing the **average annual temperature** for each station.
- **Hint 1**: You'll need to `groupby` the `station_name` and get the `mean` of `avg_temp_celsius`.
- **Hint 2**: `st.bar_chart` is the simplest way.
""")

# --- your code here ---
