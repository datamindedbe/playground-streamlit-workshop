import streamlit as st

st.title("GenAI Weather Analyst 🤖")

st.header("Assignment 1: LLM with DataFrame Context")

st.markdown("""
**Assignment**:

- Create an application where a user can ask a question about the **2025 weather data**.
- The app must send the user's question **and** the `df` DataFrame (as a string) to the LLM.
- Display the LLM's answer.
- **Hint**: Convert the DataFrame to a string using `df.to_string()`.
""")

# --- your code here ---

st.header("Assignment 2: LLM with Google Search")

st.markdown("""
**Assignment**:

- Create an application where a user can ask for the **current weather** in a Belgian city.
- The LLM must use **Google Search** to find the real-time answer.
- Display the result.
- **Hint**: You'll need to add the `tools` key to your API payload.
""")

# --- your code here ---
