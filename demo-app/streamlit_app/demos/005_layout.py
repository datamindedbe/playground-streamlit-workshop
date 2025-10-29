
import streamlit as st

st.title("Layout")
st.text("How to organize your content.")

st.header("Columns")

st.text("Use columns to organize your content")
col1, col2 = st.columns(2)
with col1:
    # use it like you would use st
    col1.text("This is column 1")
with col2:
    col2.text("This is column 2")

st.text("you can play with the relative size and the gap between the columns")
col1, col2 = st.columns([1,3], gap="large")
with col1:
    col1.text("This is column 1")
with col2:
    col2.text("This is column 2")


st.header("Expander")

with st.expander("Click me"):
    st.text("This is a hidden text")


st.header("Tabs")

st.text("Organize your content in tabs. Note that they are loaded in one go, and the namespace of all widgets is the same!")

tab1, tab2 = st.tabs(["tab1", "tab2"])

with tab1:
    st.text("This is tab 1")
with tab2:
    st.text("This is tab 2")

st.header("Sidebar")
st.text("You can put widgets in the sidebar!")
# use it like you would use st.
st.sidebar.button("Click me")
st.sidebar.select_slider("Select a number", options=[1,2,3,4,5])


st.header("Containers")

con = st.container(border=True)
con.button("Click me", key="button1")
