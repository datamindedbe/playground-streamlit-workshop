import io
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_app.connections.data import fetch_belgian_weather_data
from streamlit_app.connections.ai import (
    get_ai_response_on_image,
    get_ai_response_on_stringified_dataframe,
)
from PIL import Image

# Make sure we do not overflow the prompt
PROMPT_INPUT_LENGTH_UPPER_LIMIT = 10_000_000


@st.cache_data(show_spinner="Fetching Belgian weather data")
def load_data():
    return fetch_belgian_weather_data()


st.set_page_config(layout="wide")
st.title("🦾 GenAI Weather Analyst")

st.header("Assignment 1: LLM with DataFrame Context")

prompt_1 = st.text_input(
    "Ask a question about the 2025 Belgian weather data:",
    "What was the hottest day recorded in this dataset?",
)

df = load_data()

if st.button("Analyze 2025 Data"):
    if not df.empty and prompt_1:
        with st.spinner("AI is considering your question..."):
            data_string = df.to_string()

            # Truncate data if it's too large for the prompt
            if len(data_string) > PROMPT_INPUT_LENGTH_UPPER_LIMIT:
                data_string = (
                    data_string[:PROMPT_INPUT_LENGTH_UPPER_LIMIT]
                    + "\n... (data truncated)"
                )

            response = get_ai_response_on_stringified_dataframe(
                prompt=prompt_1, stringified_dataframe=data_string
            )
            st.markdown(response)
    elif df.empty:
        st.error("No 2025 data loaded to analyze.")
    else:
        st.warning("Please enter a question.")

st.header("Assignment 2: LLM Data Enrichment")

# Create a small sample df that contains values on each category
bins = [-np.inf, 15, 20, 25, np.inf]
labels = ["Cold", "Mild", "Warm", "Hot"]

df["temp_category"] = pd.cut(
    df["avg_temp_celsius"], bins=bins, labels=labels, right=True
)

sample_df = df.groupby("temp_category", observed=True).head(3)
sample_df = sample_df.drop("temp_category", axis=1)
sample_df = sample_df.sort_values(by="avg_temp_celsius", ascending=False)

# Show the input dataframe
st.subheader("📦 Original Weather Data")
st.dataframe(sample_df)

if st.button("Enrich my data"):
    # Get the enriched data as stringified comma-seperated values from the AI
    enrich_prompt = """
    Please analyze the `avg_temp_celsius` (mean temperature) column and add a new column named 
    `temp_category` with a value of 'Hot' (t >= 25), 'Warm' (20 <= t < 25), 'Mild' (15 <= t < 20), 
    or 'Cold' (t < 15). 

    Return *only* the new, complete data in csv format.
    Add the new column immediately after the `avg_temp_celsius` column.
    Do not add any other text like 'Here is the data' or backticks.
    """

    with st.spinner("AI is enriching your data..."):
        enriched_data_string = get_ai_response_on_stringified_dataframe(
            prompt=enrich_prompt,
            stringified_dataframe=sample_df.to_csv(
                index=False
            ),  # Send the original data
        )

        if enriched_data_string:
            try:
                # We use io.StringIO to treat the string as a file
                # We use read_csv because the AI should return the data as comma-seperated values
                new_df = pd.read_csv(io.StringIO(enriched_data_string))

                st.subheader("🪄 AI-enriched Weather Data")
                st.dataframe(new_df)

            except Exception as e:
                st.error(f"Failed to parse AI response into a DataFrame: {e}")
                st.text("Raw AI Output:")
                st.code(enriched_data_string)
        else:
            st.error("Did not get a response from the AI.")

st.header("Assignment 3: LLM explaining an uploaded picture")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["png", "jpg", "jpeg", "webp", "bmp", "tiff"],
    accept_multiple_files=False,
)

img = None

if uploaded_file is not None:
    try:
        file_bytes = uploaded_file.read()
        img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
    except Exception as e:
        st.error(f"That doesn't look like a valid image file. Details: {e}")
        st.stop()

    # Show small preview
    st.image(img, caption="Preview of the selected image", width=300)


if img:
    submitted = st.button("Let AI analyze my picture")

    if submitted:
        with st.spinner("AI is checking out your image..."):
            prompt = "Describe this image"
            try:
                response = get_ai_response_on_image(prompt, img)
                st.subheader("Response")
                st.write(response)
            except Exception as e:
                st.error(f"Generation failed: {e}")
else:
    st.info("Please upload an image to enable analysis.")
