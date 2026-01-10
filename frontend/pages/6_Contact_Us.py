import streamlit as st
from pathlib import Path

from utils.api_client import submit_lead
from components.header import render_header
from components.footer import render_footer


def load_css():
    css_path = Path(__file__).parent.parent / "assets/css/style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Contact Us", layout="wide")
    load_css()

    render_header()

    st.markdown(
        "<div class='section'><h2>Get a Free Solar Consultation</h2></div>",
        unsafe_allow_html=True
    )

    with st.form("contact_form"):
        name = st.text_input("Name *")
        phone = st.text_input("Phone *")
        email = st.text_input("Email")
        location = st.text_input("Location")
        user_type = st.selectbox(
            "Customer Type",
            ["Residential", "Commercial", "Industrial"]
        )
        user_message = st.text_area("Message")

        submitted = st.form_submit_button("Submit")

        if submitted:
            payload = {
                "name": name,
                "phone": phone,
                "email": email,
                "location": location,
                "user_type": user_type,
                "message": user_message,
            }

            success, response_message = submit_lead(payload)

            if success:
                st.success(response_message)
            else:
                st.error(response_message)

    render_footer()


if __name__ == "__main__":
    main()
