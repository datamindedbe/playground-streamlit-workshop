import streamlit as st

st.header("GenAI")

st.subheader("Assignment 1: LLM with DataFrame Context")

st.markdown("""
- Create an application where a user can ask a question about the **2025 weather data**.
- The app must send the user's question **and** the `df` DataFrame (as a string) to the LLM.
- Display the LLM's answer.
    - **Hint 1**: Convert the DataFrame to a string using `df.to_string()`.
""")

# --- your code here ---

st.subheader("Assignment 2: LLM Data Enrichment")

st.markdown("""
- Create an LLM application that is able to enrich your existing DataFrame by adding a new column.
- The app must send the user's enrichment request **and** the `df` DataFrame to the LLM.
- Display the LLM's answer.
    - **Hint 1**: Convert the DataFrame to a comma-seperated string using `df.to_csv()`.
    - **Hint 2**: Explicitly mention in the instructions to return the data in csv-format, and only return the data itself.
""")

st.subheader("Assignment 3: LLM explaining an uploaded picture")

st.markdown("""
- Build functionality to upload an image (think about extensions!) to your app.
- Search for a picture of your choosing and save it locally.
- Pass your picture to an LLM, asking it to describe the picture.
- Get the LLM's feedback, and display it in your app.
""")


# --- your code here ---
