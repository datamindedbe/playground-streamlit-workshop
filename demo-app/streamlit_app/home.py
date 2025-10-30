import streamlit as st

st.title("My First Streamlit App")

# Add a text input
user_input = st.text_input("Enter your name:", "")

# Add a button
if st.button("Say hello"):
    if user_input:
        st.write(f"Hello, {user_input}! 👋")
    else:
        st.write("Please enter your name!")

# Add some sample widgets
st.sidebar.header("Sample Controls")

# Add a slider
number = st.sidebar.slider("Select a number:", 0, 100, 50)
st.write(f"Selected number: {number}")

# Add a selectbox
option = st.sidebar.selectbox(
    "What's your favorite color?", ["Red", "Green", "Blue", "Yellow"]
)
st.write(f"Your favorite color is {option}")
