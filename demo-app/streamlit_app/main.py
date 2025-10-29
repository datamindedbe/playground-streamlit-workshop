import streamlit as st
import streamlit as st

st.logo(
    './streamlit_app/demos/dmlogo_wide.svg',
    link="https://streamlit.io/gallery",
    icon_image='./streamlit_app/demos/dmlogo_icon.svg',
)

DEMO_MODE = False

home = st.Page("home.py", title="Home", icon=":material/home:", default=True)

# Docs on creating pages: https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation
# Material icons: https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded

demo_output = st.Page("demos/001_basic_output.py", title="Basic output", icon=":material/output:", default=True)
demo_data = st.Page("demos/002_data_output.py", title="Data output", icon=":material/database:")
demo_flow = st.Page("demos/003_flow_control.py", title="Flow control", icon=":material/account_tree:")
demo_user_input = st.Page("demos/004_user_input.py", title="User input", icon=":material/input:")
demo_layout = st.Page("demos/005_layout.py", title="Layout", icon=":material/dashboard:")

exercise1= st.Page("exercises/001_forms.py", title="Forms", icon=":material/check_box:")
exercise2 = st.Page("exercises/002_plotting.py", title="Plotting", icon=":material/pie_chart:")
exercise3 = st.Page("exercises/003_genai.py", title="GenAI", icon=":material/book_4_spark:")

hackathon = st.Page("hackathon/app.py", title="Hackathon", icon=":material/destruction:")


# We switch the navigation based on a flag, this could also be a login flag
if DEMO_MODE:
    pg = st.navigation(
        {
            "Demos": [home],
        }
    )
else:
    pg = st.navigation(
        {
            "Demos": [demo_output, demo_data, demo_flow, demo_user_input, demo_layout],
            "Exercises": [exercise1, exercise2, exercise3],
            "Hackathon": [hackathon],
        }
    )

st.set_page_config(page_title="Streamlit Workshop", page_icon=":material/edit:")
pg.run()
