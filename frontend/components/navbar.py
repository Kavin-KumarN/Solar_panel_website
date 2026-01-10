import streamlit as st


def render_navbar():
    """
    Top navigation bar using Streamlit sidebar
    """
    with st.sidebar:
        st.markdown("## ☀️ Solar Energy Solutions")
        st.markdown("---")

        st.page_link("Home.py", label="Home")
        st.page_link("pages/2_About_Us.py", label="About Us")
        st.page_link("pages/3_Services.py", label="Services")
        st.page_link("pages/4_Why_Choose_Us.py", label="Why Choose Us")
        st.page_link("pages/5_Testimonials.py", label="Testimonials")
        st.page_link("pages/6_Contact_Us.py", label="Contact Us")
        st.page_link("pages/7_Privacy_Terms.py", label="Privacy & Terms")
