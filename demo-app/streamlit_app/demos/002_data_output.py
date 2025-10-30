import streamlit as st
import pandas as pd

st.title("Data output overview")


st.header("Metrics")
st.metric(label="Temperature", value="70 °F", delta_color="normal")

st.header("Semi-structured data")
# create a json doc
json_doc = {
    "name": "John Doe",
    "age": 30,
    "skills": ["Python", "SQL", "Machine Learning"],
}

st.json(json_doc, expanded=True)


st.header("Structured data")
# Create a sample DataFrame
profiles = pd.DataFrame(
    {
        "Person": ["John Doe", "Jane Smith", "Bob Wilson", "Alice Brown"],
        "Level": ["Senior", "Mid", "Junior", "Senior"],
        "Level_code": ["L5", "L3", "L2", "L5"],
        "Level_number": [5, 3, 2, 5],
        "Client": ["ACME Corp", "TechStart", "BigCo", "Innovate Inc"],
    }
)


st.subheader("st.table()")
st.text("Super basic way of showing your data in a dataframe (or list).")
st.table(profiles)

st.subheader("st.dataframe()")
st.markdown(
    "Note that this is way cooler, as you can **sort, zoom, search, download** 🥳!"
)
st.dataframe(profiles)


st.header("Unstructured data")

st.subheader("Image files")
st.text(
    "A simple image in the folder, pointed to by a relative path from the root of the app."
)
st.image(
    "./streamlit_app/demos/dmlogo_nonstatic.png",
    width=200,
    caption="This is a caption of a non-static image",
)
st.image(
    "./streamlit_app/demos/dmlogo_wide.svg", width=200, caption="Even SVG support!"
)

st.subheader("Static Image files")
static_image = "app/static/dm-black.png"
st.markdown(
    f"This is a static file hosted at `{static_image}` (look in the `static` folder), made into a circle using some dirty css."
)


st.markdown(
    """
  <style>

    /*the main div*/
    .profileimg {
        width: 100px; /*max value according to image width, can be smaller but not larger*/
        height: 100px;
        position: relative;
        overflow: hidden;
        border-radius: 50%;
    }
    
    /*the img elements in the main div class*/
    .profilepic > img{
        display: inline;
        margin: 0 auto;
        margin-top: -35%; /*Tweak this one according to your need*/
    }
  
  </style>
""",
    unsafe_allow_html=True,
)

a = f"""
    <div style="display: flex; align-items: center; gap: 20px;">
        <div>
            <img src="{static_image}" class="profileimg" alt="Profile Picture of Dataminded">
        </div>
        <div>
            <h2 style="margin: 0">Dataminded</h2>
            <h5 style="margin: 5px 0 0 0; color: #666">Getting Data Done</h5>
        </div>
    </div>
"""
st.markdown(a, unsafe_allow_html=True)
