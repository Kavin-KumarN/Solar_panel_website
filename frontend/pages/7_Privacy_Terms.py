import streamlit as st
from pathlib import Path
from components.header import render_header
from components.footer import render_footer


def load_css():
    css_path = Path(__file__).parent.parent / "assets/css/style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Privacy & Terms", layout="wide")
    load_css()

    render_header()

    st.markdown(
        """
        <div class="section">
        <h2>Privacy Policy & Terms</h2>
        <p>
        We respect your privacy. Any information submitted through this website
        is used solely for contacting you regarding solar services.
        We do not share your data with third parties.
        </p>

        <p>
        All installations and services are subject to site conditions and
        applicable government regulations.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()


if __name__ == "__main__":
    main()
