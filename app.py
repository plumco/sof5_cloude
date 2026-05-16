import streamlit as st
import streamlit.components.v1 as components

# Set to wide mode and hide Streamlit's default sidebar
st.set_page_config(page_title="Huliot SO — Sales Order", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit's default top and bottom padding so your app takes up the whole screen
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

try:
    with open("preview GPT.html", "r", encoding="utf-8") as f:
        html_source_code = f.read()
        
    # Increase the height to 1200 and turn off inner scrolling to remove the double scrollbar
    components.html(html_source_code, height=1200, scrolling=False)

except FileNotFoundError:
    st.error("Could not find the file. Please make sure it is in the same folder.")
