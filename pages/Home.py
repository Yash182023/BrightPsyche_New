# import streamlit as st


# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

# st.write("# Welcome to  our website! 👋")



# st.markdown(
#     """
#     Welcome to [Your Website Name], your trusted companion on the journey to mental well-being and self-discovery. We understand that navigating the intricacies of mental health can be a challenging and personal experience. That's why we're here to offer a compassionate hand and a wealth of knowledge to guide you on your path to a healthier mind.""")

# st.subheader('Our Mission')

# st.markdown("""At [Your Website Name], our mission is to create a supportive online space where individuals can access valuable resources, expert insights, and connect with a community that shares their commitment to mental health. We believe that everyone deserves access to the tools and knowledge necessary for fostering emotional resilience and achieving a fulfilling life.""")

# st.subheader('What We Offer ?')

# st.markdown("""
# 1. Expert-Backed Information:
# Dive into a comprehensive collection of articles, blogs, and resources created by mental health professionals. Gain a deeper understanding of various mental health conditions, coping strategies, and wellness practices to empower yourself on your mental health journey.

# 2. Therapeutic Insights:
#    Explore a variety of therapeutic approaches and gain insights into how they can support your well-being. Whether you're curious about cognitive-behavioral therapy, mindfulness, or other modalities, our platform provides valuable information to help you make informed decisions.

# 3. Community Support:
#    Connect with a community of like-minded individuals who understand the challenges of navigating mental health. Share your experiences, provide support, and learn from others who are on similar paths. Our forums and discussion boards create a safe space for open dialogue and mutual understanding.

# 4. Online Therapy Resources:
#    Access information on reputable online therapy services, allowing you to connect with licensed professionals from the comfort of your own space. Discover the convenience and effectiveness of virtual therapy as you work towards your mental health goals.

# """)

# st.subheader('Why choose us ?')

# st.markdown("""

# - Compassionate Approach:
#   We approach mental health with empathy, understanding, and a commitment to reducing the stigma surrounding it. Our content is designed to uplift, inspire, and provide the support you need.

# - Holistic Wellness:
#   We believe in a holistic approach to mental health that encompasses emotional, physical, and social well-being. Our resources cover a wide range of topics to support you on your journey to a balanced and fulfilling life.

# - Trustworthy Information:
#   Rest assured that the information provided on our platform is curated by mental health professionals and experts. We prioritize accuracy and reliability to ensure you receive the most trustworthy guidance.
# """)

# import streamlit as st

# # Set page configuration
# st.set_page_config(
#     page_title="Hello",
#     page_icon="seedling:",
# )

# # Define custom CSS styles
# custom_styles = """
# <style>
#     .main {
#         font-family: 'Arial', sans-serif;
#         background-color: #f5f5f5;
#         color: #333;
#         line-height: 1.6;
#     }

#     h1, h2, h3, h4, h5, h6 {
#         color: #fa0f79;
#     }

#     .container {
#         max-width: 800px;
#         margin: 0 auto;
#     }

#     .welcome-section {
#         background-color: #ffffff;
#         padding: 20px;
#         border-radius: 10px;
#         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
#         margin-bottom: 20px;
#     }

#     .mission-section, .offer-section, .choose-us-section {
#         background-color: #f8f8f8;
#         padding: 20px;
#         border-radius: 10px;
#         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
#         margin-bottom: 20px;
#     }
# </style>
# """

# # Render custom styles
# st.markdown(custom_styles, unsafe_allow_html=True)

# # Content
# st.write("# Welcome to our website! :seedling:")

# st.markdown(
#     """
#     Welcome to [Your Website Name], your trusted companion on the journey to mental well-being and self-discovery. We understand that navigating the intricacies of mental health can be a challenging and personal experience. That's why we're here to offer a compassionate hand and a wealth of knowledge to guide you on your path to a healthier mind."""
# )

# st.subheader('Our Mission')

# st.markdown("""At [Your Website Name], our mission is to create a supportive online space where individuals can access valuable resources, expert insights, and connect with a community that shares their commitment to mental health. We believe that everyone deserves access to the tools and knowledge necessary for fostering emotional resilience and achieving a fulfilling life.""")

# st.subheader('What We Offer ?')

# st.markdown("""
# 1. Expert-Backed Information:
# Dive into a comprehensive collection of articles, blogs, and resources created by mental health professionals. Gain a deeper understanding of various mental health conditions, coping strategies, and wellness practices to empower yourself on your mental health journey.

# 2. Therapeutic Insights:
#    Explore a variety of therapeutic approaches and gain insights into how they can support your well-being. Whether you're curious about cognitive-behavioral therapy, mindfulness, or other modalities, our platform provides valuable information to help you make informed decisions.

# 3. Community Support:
#    Connect with a community of like-minded individuals who understand the challenges of navigating mental health. Share your experiences, provide support, and learn from others who are on similar paths. Our forums and discussion boards create a safe space for open dialogue and mutual understanding.

# 4. Online Therapy Resources:
#    Access information on reputable online therapy services, allowing you to connect with licensed professionals from the comfort of your own space. Discover the convenience and effectiveness of virtual therapy as you work towards your mental health goals.

# """)

# st.subheader('Why choose us ?')

# st.markdown("""

# - Compassionate Approach:
#   We approach mental health with empathy, understanding, and a commitment to reducing the stigma surrounding it. Our content is designed to uplift, inspire, and provide the support you need.

# - Holistic Wellness:
#   We believe in a holistic approach to mental health that encompasses emotional, physical, and social well-being. Our resources cover a wide range of topics to support you on your journey to a balanced and fulfilling life.

# - Trustworthy Information:
#   Rest assured that the information provided on our platform is curated by mental health professionals and experts. We prioritize accuracy and reliability to ensure you receive the most trustworthy guidance.
# """)

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
