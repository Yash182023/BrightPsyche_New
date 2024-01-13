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

# Render custom styles
st.markdown(custom_styles, unsafe_allow_html=True)
# Load your existing HTML file
with open("C:/Users/sharm/Downloads/ask-multiple-pdfs-main/ask-multiple-pdfs-main/output.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# st.markdown(html_content, unsafe_allow_html=True)
# Display the HTML content
st.components.v1.html(html_content, height=800,width=800, scrolling=True)
