import streamlit as st
from pathlib import Path
from components.header import render_header
from components.footer import render_footer
from utils.config import APP_NAME


def load_css():
    css_path = Path(__file__).parent.parent / "assets/css/style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="About Us", layout="wide")
    load_css()

    render_header()

    st.markdown(
        """
        <div class="section">
        <h2>About Our Company</h2>
        <p>
        We are a solar energy solutions provider committed to helping homes,
        businesses, and industries reduce electricity costs and carbon footprint.
        With over a decade of experience, our team delivers reliable,
        high-performance solar installations across India.
        </p>

        <p>
        From feasibility study to installation and maintenance,
        we handle everything end-to-end.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()


if __name__ == "__main__":
    main()
