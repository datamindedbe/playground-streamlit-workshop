import time
import streamlit as st

st.title("Flow control")


st.header("Button behavior")
result = st.button("Click me")
if result:
    st.text("You clicked the button")

result = st.button("Now click me")
if result:
    st.text("You clicked the second button")
    st.text("Did you notice the first result was cleared?")

st.header("Loading content")
load = st.button("Load", key="load")
if load:
    with st.spinner("Loading..."):
        st.text("This is a spinner")
        time.sleep(2)

st.text("This is a text")

st.header("Progress")

start_progress = st.button("Start progress", key="start_progress")
bar = st.progress(value=0, text="This is a progress bar")

if start_progress:
    for i in range(101):
        time.sleep(0.1)
        bar.progress(value=i, text=f"This is a progress bar {i}%")


st.header("Caching")

def load_uncached():
    time.sleep(2)
    return "This is a text"

@st.cache_data(ttl=10, show_spinner=True)
def load_cached():
    time.sleep(2)
    return "This is cached text"

load1 = st.button("load uncached", key="load_uncached")
load2 = st.button("load cached", key="load_cached")

if load1:
    st.text(load_uncached())
if load2:
    st.text(load_cached())
