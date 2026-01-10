import streamlit as st
from utils.config import CONTACT_PHONE, CONTACT_EMAIL


def render_footer():
    """
    Footer with contact details
    """
    st.markdown(
        f"""
        <div class="footer">
            <p><strong>Contact</strong></p>
            <p>📞 {CONTACT_PHONE}</p>
            <p>✉️ {CONTACT_EMAIL}</p>
            <p>© 2026 Solar Energy Solutions. All rights reserved.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
