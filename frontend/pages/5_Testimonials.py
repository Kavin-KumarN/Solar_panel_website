import streamlit as st
from utils.api_client import get_testimonials
from pathlib import Path
from components.header import render_header
from components.footer import render_footer

def load_css():
    css_path = Path(__file__).parent.parent / "assets/css/style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Testimonials", layout="wide")
    load_css()

    render_header()

    st.markdown("<div class='section'><h2>Customer Testimonials</h2></div>", unsafe_allow_html=True)
    testimonials = get_testimonials()

    if not testimonials:
        st.info("Testimonials will appear here soon.")
    else:
        for t in testimonials:
            st.markdown(
                f"""
                <div class="section">
                <strong>{t['customer_name']}</strong><br/>
                ⭐ {t['rating']} / 5<br/>
                <em>{t['review']}</em>
                </div>
                """,
                unsafe_allow_html=True
            )

    render_footer()


if __name__ == "__main__":
    main()
