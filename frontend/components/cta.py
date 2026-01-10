import streamlit as st


def render_cta(text="Get Free Solar Consultation"):
    """
    Reusable CTA button
    """
    st.markdown("<div class='section'>", unsafe_allow_html=True)

    clicked = st.button(text)

    if clicked:
        st.switch_page("pages/6_Contact_Us.py")

    st.markdown("</div>", unsafe_allow_html=True)
