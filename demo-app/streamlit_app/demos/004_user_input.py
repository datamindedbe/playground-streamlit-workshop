

# Widget overview
# Dataframe

import pandas as pd
import streamlit as st

st.title("Widgets!! 🎚️🎛️")
st.text("Widgets can help get user input and return values that can be stored in variables.")

st.header("Basic widgets")

text = st.text_input("Text input")
number = st.number_input("Number input")
slider = st.slider("Slider")
selectbox = st.selectbox("Selectbox", options=["Option 1", "Option 2", "Option 3"])
checkbox = st.checkbox("Checkbox")
toggle = st.toggle("Toggle")
radio = st.radio("Radio", options=["Option 1", "Option 2", "Option 3"])
# button = st.button("Button")

st.markdown(f"""
You entered:
- Text: {text}
- Number: {number}
- Slider: {slider}
- Selectbox: {selectbox}
- Checkbox: {checkbox}
- Toggle: {toggle}
- Radio: {radio}
""")

st.header("Fancy widgets")

multiselect = st.multiselect("Multiselect", options=["Option 1", "Option 2", "Option 3"])
options = ["Client 1", "Client 2", "Client 3"]
pills = st.pills("Clients", options, selection_mode="multi")
options = ["North", "East", "South", "West"]
selection = st.segmented_control(
    "Directions", options, selection_mode="multi"
)

st.markdown(f"""
You selected:
- Multiselect: {multiselect}
- Pills: {pills}
- Segmented control: {selection}
""")


st.header("Data input")

st.subheader("Basic")
df = pd.DataFrame({
    "numbers": [1, 2, 3, 4, 5],
    "text": ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"],
    "bool": [True, False, True, False, True],
     "sales": [200, 550, 1000, 80, 100],
})
st.data_editor(df)

st.subheader("Fancy")


st.data_editor(
    df, 
    hide_index=True,
    num_rows="dynamic",
    column_config={
        "numbers": st.column_config.NumberColumn(
            format="%.2f",
        ),
        "text": st.column_config.SelectboxColumn(
            options=["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"],
        ),
        "bool": st.column_config.CheckboxColumn(
            width="small",
        ),
        "sales": st.column_config.ProgressColumn(
            "Sales volume",
            help="The sales volume in USD",
            format="$%f",
            min_value=0,
            max_value=1000,
        ),
    }
    )
