import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Huliot SO — Sales Order", layout="wide")

try:
    # This exactly matches your uploaded HTML file name
    with open("preview GPT.html", "r", encoding="utf-8") as f:
        html_source_code = f.read()
        
    components.html(html_source_code, height=800, scrolling=True)

except FileNotFoundError:
    st.error("Could not find the file. Please make sure it is in the same folder.")
