import streamlit as st

st.title("Forms")

st.header("Assignment 1: Interactive Filter Form")

st.markdown("""
**Assignment**:
1.  Print all data on Belgian weather as a table 
    - The function to load the data is called `fetch_belgian_weather_data`
2.  Create a **Form** (`st.form`) to hold the filters.
3.  Inside the form, add a **multiselect** to filter by **station name** (`st.multiselect`).
4.  Inside the form, add a **date range slider** to filter by date (`st.slider`).
5.  Add a "Submit" button (`st.form_submit_button`).
6.  **Outside** the form, display the filtered data in a table (`st.dataframe`).
7.  ⚠️ Map as extra assignment
""")

# --- your code here ---

st.header("Assignment 2: Caching")

st.markdown("""
**Assignment**:
- The app re-runs the *entire* BigQuery query every time. This is slow and expensive!
- Add **caching** to your `load_data()` function to fix this.
""")

# --- your code here ---
