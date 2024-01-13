import streamlit as st

custom_styles = """
<style>
    .main {
        font-family: 'Arial', sans-serif;
        color: #333;
        line-height: 1.6;
        background: #ffffff;

    }
    
</style>
"""


st.markdown(custom_styles, unsafe_allow_html=True)
with open("output.html", "r", encoding="utf-8") as file:
    html_content = file.read()

st.components.v1.html(html_content, height=800,width=800, scrolling=True)
