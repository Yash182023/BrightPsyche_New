import streamlit as st

# Custom CSS styles
custom_styles = """
<style>
    .main {
        font-family: 'Arial', sans-serif;
        background: radial-gradient(circle,white,grey);
        color: #333;
        line-height: 1.6;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #000000
    }

    .container {
        max-width: 800px;
        margin: 0 auto;
    }
</style>
"""

st.markdown(custom_styles, unsafe_allow_html=True)


st.markdown("# About Us :seedling:")

st.markdown(
    """
    Welcome to BrightPsych, your trusted companion on the journey to mental well-being and self-discovery. At BrightPsych, we are dedicated to creating a supportive online space where individuals can access valuable resources, expert insights, and connect with a community that shares their commitment to mental health.
    """
)

st.subheader('Our Mission')

st.markdown("""
At BrightPsych, our mission is to empower individuals by providing a compassionate hand and a wealth of knowledge to guide them on their path to a healthier mind. We understand that navigating the intricacies of mental health can be a challenging and personal experience, and we are here to offer support and encouragement every step of the way.
""")

st.subheader('Our Team')

st.markdown("""
Meet the dedicated team behind BrightPsych, a group of passionate individuals with expertise in mental health, technology, and related fields. We believe in the power of collaboration and are committed to creating an inclusive and user-centric platform.
""")

st.subheader('Values and Approach')

st.markdown("""
BrightPsych is founded on core values of empathy, inclusivity, accuracy, and a commitment to reducing the stigma surrounding mental health. We approach mental health with understanding and strive to provide accurate and reliable information to support our community on their mental health journey.
""")

st.subheader('User-Centric Focus')

st.markdown("""
Our platform is designed with a user-centric focus, prioritizing the well-being of our community. We aim to meet the diverse needs of our users by offering a variety of resources, expert-backed information, and a supportive online community where individuals can connect and share their experiences.
""")

st.subheader('Privacy and Security')

st.markdown("""
We prioritize the privacy and security of our users. BrightPsych has implemented measures to protect user data, ensuring a safe and confidential environment for individuals to explore mental health resources and engage with the platform.
""")

st.markdown(
    """
    Thank you for being a part of the BrightPsych community. We invite you to explore our platform, connect with others, and discover the resources that can support you on your mental health journey. If you have any questions or feedback, feel free to reach out to us at [info@brightpsych.com](mailto:info@brightpsych.com
""")