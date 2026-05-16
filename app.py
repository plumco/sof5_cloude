import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Huliot SO — Sales Order", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit's default top header and completely remove all padding
st.markdown("""
    <style>
        /* Hide the Streamlit top menu bar */
        header[data-testid="stHeader"] {
            display: none !important;
        }
        /* Remove padding to push the app to the absolute edges */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
    </style>
""", unsafe_allow_html=True)

try:
    with open("preview GPT.html", "r", encoding="utf-8") as f:
        html_source_code = f.read()
        
    components.html(html_source_code, height=1200, scrolling=False)

except FileNotFoundError:
    st.error("Could not find the file. Please make sure it is in the same folder.")
