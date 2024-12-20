import streamlit as st

from forms.contact import contact_form


@st.dialog("Contacto")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/brain-chip.png", width=230)
with col2:
    st.title("ShadowzSmilez", anchor=False)
    st.write(
        "Ingeniero Informatico y Gamer de Nacimiento"
    )
    if st.button("✉️ Contacto"):
        show_contact_form()


# --- TEXTO ADICIONAL EN LA PAGINA SUPERIOR ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 7 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of iniative on tasks
    """
)

# --- TEXTO ADICIONAL EN LA PAGINA INFERIOR ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python, PowerPlatform, SQL
    - Data Visualization: PowerBI, Google Data Studio, MS Excel
    - Modeling: Logistic regression, linear regression
    - Databases: SQL Server, My SQL, Oracle
    """
)