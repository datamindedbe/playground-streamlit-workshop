import streamlit as st

st.set_page_config(layout="wide")

st.title("The Blank Canvas Weather Hackathon 🌪️☀️🌧️")

# Nice picture
st.image(
    "https://images.unsplash.com/photo-1584269910288-f58f0283239d?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=2067",
    caption="What will you build? Photo by NOAA on Unsplash",
    use_container_width=True,
)

st.header("Your Mission: Build Something Awesome")

st.markdown("""
Welcome, builders!

Your mission for this hackathon is simple: **grab some data and build something cool.**

We've provided you with a 🇧🇪 Belgium-centered version of the **2025 NOAA GSOD weather data**. It's a rich dataset full of temperatures, wind speeds, precipitation, and more.
""")

st.subheader("The Only Rule: You do you")

st.markdown("""
What should you build? **That's for you to decide.**

There are no pre-defined problems to solve or features to build. We want to see what *you* find interesting.
We hope this hackathon encourages you to build something *you* think is cool.

- Is it a predictive model?
- A beautiful data visualization dashboard?
- A helpful alert system?
- A public-facing app that solves a problem you've always wondered about?
- A deep-dive analysis that reveals a hidden trend?

Yes. It's any of those. Or something else entirely. 🚀
""")

st.header("Where to start? The Data & The Docs!")

st.markdown("""
1.  **Explore the Data:** What columns are available? What do `max`, `min`, and `prcp` mean? What do the station codes tell you?
2.  **Explore the Docs:** How does Streamlit work? How can you add a button, a slider, or a chart?

Here are the links that will help you:
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Streamlit Docs")
    st.markdown("""
    * [Main Documentation](https://docs.streamlit.io/)
    * [Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
    * [Gallery of App Examples](https://streamlit.io/gallery)
    """)

with col2:
    st.subheader("Weather Dataset Docs")
    st.markdown("""
    * [Kaggle: Dataset Column Descriptions](https://www.kaggle.com/datasets/noaa/gsod)
    * [Official NOAA GSOD Page](https://www.ncei.noaa.gov/products/land-based-station/global-summary-of-the-day)
    """)


st.divider()
st.header("Good luck. Have fun. Build something awesome.")
st.balloons()
