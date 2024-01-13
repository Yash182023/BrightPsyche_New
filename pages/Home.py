import streamlit as st
from datetime import datetime
import pandas as pd


# Set page configuration
st.set_page_config(
    page_title="BrightPsych",
    page_icon="seedling",
)

# Define custom CSS styles
custom_styles = """
<style>
    .main {
        font-family: 'Arial', sans-serif;
        color: #333;
        line-height: 1.6;
        background: radial-gradient(circle, hsl(40, 100%, 90%) 0%, hsl(40, 100%, 80%) 100%);

    }

    h1, h2, h3, h4, h5, h6 {
        color: #fa0f79;
    }

    .container {
        max-width: 800px;
        margin: 0 auto;
    }

    .section {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
</style>
"""

# Render custom styles
st.markdown(custom_styles, unsafe_allow_html=True)

# Section: Welcome
st.markdown("# Welcome to BrightPsych! :seedling:")

st.markdown(
    """
    Welcome to BrightPsych, your trusted destination for mental well-being. Our platform offers a range of services to support you on your journey to emotional health and self-discovery. Explore the features below and embark on a path towards a brighter mind.
    """
)

# Section: Empathetic Chat Bot
st.markdown("## Empathetic Chat Bot")
st.markdown(
    """
    Connect with our empathetic chat bot for a supportive conversation. Whether you need someone to talk to or seek guidance, our chat bot is here for you.
    """
)
# Your chat bot implementation goes here

# Section: CBT Analysis
st.markdown("## CBT Analysis of Disorders")
st.markdown(
    """
    Explore Cognitive Behavioral Therapy (CBT) analyses of common disorders, including PTSD, ADHD, and BPD. Gain insights into effective therapeutic approaches.
    """
)
# Your CBT analysis implementation goes here

# Section: Daily Mood Tracking
st.markdown("## Daily Mood Tracking")
st.markdown(
    """
    Track your daily mood and well-being by answering a few questions. Understand patterns, set goals, and prioritize your mental health.
    """
)
# Your daily mood tracking implementation goes here

# Section: Data Analysis
st.markdown("## Data Analysis of 'Student_Mental_Health' Dataset")
st.markdown(
    """
    Dive into the analysis of a dataset focused on student mental health. Discover trends, correlations, and insights to promote a supportive environment.
    """
)
# Your data analysis implementation goes here

# Section: Mindfulness Session
st.markdown("## Mindfulness Session")
st.markdown(
    """
    Join our mindfulness session for guided meditation and relaxation. Nurture a peaceful mind and enhance your overall well-being.
    """
)
# Your mindfulness session implementation goes here

# Footer Section
st.markdown("<footer class='custom-footer'>", unsafe_allow_html=True)
# Footer Section
st.markdown("---")
st.write("© 2024 BrightPsych. All rights reserved.")
st.write("Contact us at: [info@brightpsych.com](mailto:info@brightpsych.com)")

st.markdown("</footer>", unsafe_allow_html=True)
