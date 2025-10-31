import streamlit as st


# Set page title
st.title("Text output overview")

st.header("Text")
st.subheader("Normal text")

# Add some body text
st.write("""
This is a basic demonstration of Streamlit's capabilities.
Streamlit makes it easy to create beautiful web apps for data science and machine learning.
         
You can use emojis directly, or shortcodes:
👋 :wave:
         
Material design icons are available too:
:material/delete:
""")

st.text("Let's add a divider")
st.divider()  # 👈 Draws a horizontal rule
st.text("and some text below it.")

st.caption(
    "Sometimes you're in need of captions for footnotes, or other explanatory text."
)
st.caption("This has **markdown** and :red[color] support as well! :sunglasses:")
st.caption(
    "You can even add help, hover me! 👉",
    help="This is not the tooltip you're looking for...",
)

st.subheader("Markdown")

st.markdown("""
> **Note:** you can use *markdown* to style your text and easily add [links](https://www.streamlit.io).
> Explore the documentation to learn more!
""")

st.subheader("Code")
st.text(
    "Code environment with highlighting, line numbers and copy button (line wrapping optional)."
)
example_yaml = """
user:
  name: John Doe
  age: 30
  roles:
    - admin
    - developer
  
settings:
  theme: dark
  notifications: true
  preferences:
    language: en-US
    timezone: UTC
    display:
      show_sidebar: true
      font_size: 14px
"""

st.code(example_yaml, language="yaml", line_numbers=True)

st.subheader("Math")
st.latex(r"""
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    """)


st.subheader("Information boxes")

st.text("You can use built-in message boxes, with optional and customizable icons:")
st.info("info box - useful for general information", icon=":material/info:")
st.success(
    "success box - great for showing when things work!", icon=":material/check_circle:"
)
st.warning(
    "warning box - use it to alert users about potential issues",
    icon=":material/warning:",
)
st.error("error box - for when something goes wrong", icon=":material/error:")
st.error("error box - custom flame icon", icon="🔥")
st.error("error box - no icon")


st.header("Pro stuff")

st.subheader("Writing")
st.write("core writing function is st.write()")

st.subheader("HTML")
st.html("<h1>Hey boomer, where's your <i>closing</i> tag?</h1>")

# Add a note in a special container
# with st.container(border=True):
#     st.text("This is a container with a border")
