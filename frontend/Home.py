import streamlit as st
from pathlib import Path
import requests

from utils.config import APP_NAME, TAGLINE, BACKEND_API_BASE_URL
from components.header import render_header
from components.cta import render_cta
from components.footer import render_footer


# ---------- Helpers ----------
def load_css():
    css_path = Path(__file__).parent / "assets" / "css" / "style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_image(img_name: str):
    return str(Path(__file__).parent / "assets" / "images" / img_name)


# ---------- Main Page ----------
def main():
    # MUST be first Streamlit command
    st.set_page_config(
        page_title=APP_NAME,
        page_icon="☀️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    load_css()

    # Header / Hero title
    render_header()

    # Hero section
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown(
            """
            <div class="section">
                <h2>Reduce Your Electricity Bills by Up to 90%</h2>
                <p>
                We design and install high-quality solar systems for homes,
                businesses, and factories. Start saving from day one with
                expert installation and government subsidy support.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        render_cta("Get Free Solar Consultation")
    with col2:
        st.image(load_image("hero.jpg"), use_container_width=True)

    st.markdown("<div class='section'><h2>Our Solar Services</h2></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.image(load_image("residential.jpg"), use_container_width=True)
        st.subheader("Residential Solar")
        st.write("Rooftop solar systems for independent homes and apartments.")

    with c2:
        st.image(load_image("commercial.jpg"), use_container_width=True)
        st.subheader("Commercial Solar")
        st.write("Solar solutions for offices, shops, malls, and institutions.")

    with c3:
        st.image(load_image("industrial.jpg"), use_container_width=True)
        st.subheader("Industrial Solar")
        st.write("High-capacity systems for factories and warehouses.")

    st.markdown("<div class='section'><h2>Why Choose Us</h2></div>", unsafe_allow_html=True)

    b1, b2, b3, b4 = st.columns(4)

    b1.metric("Experience", "10+ Years")
    b2.metric("Happy Clients", "500+")
    b3.metric("ROI Period", "3–5 Years")
    b4.metric("Panel Life", "25+ Years")

    st.markdown("<div class='section'><h2>Installation Process</h2></div>", unsafe_allow_html=True)

    steps = [
        "Free Site Visit & Feasibility",
        "System Design & Quotation",
        "Installation & Net Metering",
        "Power On & Maintenance Support"
    ]

    cols = st.columns(4)
    for i, step in enumerate(steps):
        with cols[i]:
            st.markdown(f"**Step {i + 1}**")
            st.write(step)

    st.markdown("<div class='section'><h2>What Our Customers Say</h2></div>", unsafe_allow_html=True)

    try:
        resp = requests.get(f"{BACKEND_API_BASE_URL}/testimonials", timeout=5)
        data = resp.json().get("data", [])

        if not data:
            st.info("Testimonials will appear here soon.")
        else:
            for t in data:
                with st.container():
                    st.markdown(
                        f"""
                        <div class="section">
                        <strong>{t['customer_name']}</strong> ({t.get('customer_type', '')})<br/>
                        ⭐ {t['rating']} / 5<br/>
                        <em>{t['review']}</em>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
    except Exception:
        st.warning("Unable to load testimonials at the moment.")
    # (Later sections like services, process, testimonials will go here)

    render_cta("Book a Free Site Visit")
    render_footer()


if __name__ == "__main__":
    main()
