import streamlit as st
from utils.config import APP_NAME, TAGLINE


def render_header():
    """
    Page header / hero section
    """
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title(APP_NAME)
    st.subheader(TAGLINE)
    st.markdown("</div>", unsafe_allow_html=True)
