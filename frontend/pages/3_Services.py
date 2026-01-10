import streamlit as st
from pathlib import Path
from components.header import render_header
from components.footer import render_footer


def load_css():
    css_path = Path(__file__).parent.parent / "assets/css/style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Services", layout="wide")
    load_css()

    render_header()

    st.markdown("<div class='section'><h2>Our Services</h2></div>", unsafe_allow_html=True)

    st.subheader("Residential Solar")
    st.write("Affordable rooftop solar systems for independent homes and apartments.")

    st.subheader("Commercial Solar")
    st.write("Optimized solar solutions for offices, shops, and institutions.")

    st.subheader("Industrial Solar")
    st.write("High-capacity solar plants for factories and warehouses.")

    render_footer()


if __name__ == "__main__":
    main()
