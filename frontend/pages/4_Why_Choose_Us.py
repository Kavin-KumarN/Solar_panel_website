import streamlit as st
from pathlib import Path
from components.header import render_header
from components.footer import render_footer


def load_css():
    css_path = Path(__file__).parent.parent / "assets/css/style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Why Choose Us", layout="wide")
    load_css()

    render_header()

    st.markdown(
        """
        <div class="section">
        <h2>Why Choose Us</h2>
        <ul>
            <li>✔ 10+ years of solar expertise</li>
            <li>✔ End-to-end project handling</li>
            <li>✔ Government subsidy assistance</li>
            <li>✔ High-quality panels & inverters</li>
            <li>✔ Dedicated after-sales support</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()


if __name__ == "__main__":
    main()
