import streamlit as st

# --- PAGE STUP ---
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    #icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    #icon=":material/bar_chart:",
)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    #icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITHOUT SECTION] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITHOUT SECTION] ---
pg = st.navigation(
    {
    "Info": [about_page],
    "Projects": [project_1_page, project_2_page], 
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("assets/logo2.png")
st.sidebar.text("Practicando Python 🫡 by Shadowz Smilez")

# --- RUN NAVIGATION ---
pg.run()