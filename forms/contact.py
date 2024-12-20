import re

import streamlit as st
import requests


# WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    # Basic regex pattern form email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Nombre")
        email = st.text_input("Email")
        message = st.text_area("Tu Mensaje")
        submit_button = st.form_submit_button("Enviar")

        if submit_button:
            if not  WEBHOOK_URL:
                st.error("Email service is not set up. Please try again later.", icon="✉️")
                st.stop()
            if not  name:
                st.error("Por favor ingrese su nombre.", icon="🧑‍🦲")
                st.stop()
            if not  email:
                st.error("Por favor ingrese su dirección de correo electrónico.", icon="📧")
                st.stop()
            if not  is_valid_email(email):
                st.error("Por favor ingrese una dirección de correo electrónico válida.", icon="📧")
                st.stop()
            if not  message:
                st.error("Por favor ingrese su mensaje.", icon="💬")
                st.stop()

        # --- Preparar la data para enviar correo por medio del webhook url especificado
#        data = {"email": email, "name": name, "message": message}
#        response = requests.post(WEBHOOK_URL, json=data)

#        if response.status_code == 200:
#            st.success("Mensaje enviado correctamente! 🎉", icon="🚀")
#        else:
#            st.error("Ha ocurrido un error al enviar su mensaje", icon="😱")
