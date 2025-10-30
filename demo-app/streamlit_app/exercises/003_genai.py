import streamlit as st

st.title("GenAI Weather Analyst")

st.header("Assignment 1: LLM with DataFrame Context")

st.markdown("""
**Assignment**:

- Create an application where a user can ask a question about the **2025 weather data**.
- The app must send the user's question **and** the `df` DataFrame (as a string) to the LLM.
- Display the LLM's answer.
    - **Hint 1**: Convert the DataFrame to a string using `df.to_string()`.
""")

# --- your code here ---

st.header("Assignment 2: LLM with Google Search")

st.markdown("""
**Assignment**:

- Create an LLM application that is able to enrich your existing DataFrame by adding a new column.
- The app must send the user's enrichment request **and** the `df` DataFrame to the LLM.
- Display the LLM's answer.
    - **Hint 1**: Convert the DataFrame to a comma-seperated string using `df.to_csv()`.
    - **Hint 2**: Explicitly mention in the instructions to return the data in csv-format, and only return the data itself.
""")

# --- your code here ---
