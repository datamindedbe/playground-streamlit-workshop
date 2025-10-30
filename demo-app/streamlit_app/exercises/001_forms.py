import streamlit as st
from streamlit_app.connections.data import fetch_sandi_data

# Get the data
df = fetch_sandi_data()

st.title("Forms")

st.header("Assignment 1: Form")

st.markdown("""
**Assignment**:
- print all data as a table
- add a dropdown to filter on the levels
- add a multiselect to filter on the clients
""")

# --- your code here ---


st.header("Assignment 2: Form")

st.markdown("""
**Assignment**:
- Add caching to the data!
""")

# --- your code here ---
