import streamlit as st
from datetime import datetime
from deta import Deta
import plotly.express as px
import pandas as pd
from streamlit.components.v1 import html
# Load the environment variables
DETA_KEY = "YOUR_DATA_KEY"

# Initialize with a project key
deta = Deta(DETA_KEY)

# Create Deta Base instance
my_db = deta.Base("bright_psych_data")

# Custom CSS
custom_css = """
    <style>
        .main {
            background-image: radial-gradient(circle, #81b7c9,#0986b0);

        }
        .custom-header {
            color: #ffffff; 
            font-size: 40px;
            font-weight: bold;
            margin-bottom: 10px;
            text-align: center;
        }
        .custom-subheader {
            color: #ffffff; 
            font-size: 18px;
            margin-bottom: 5px;
            font-weight: bold;
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Ask questions before entries
st.markdown('<p class="custom-header">Daily Mood Tracker</p>', unsafe_allow_html=True)

current_date = datetime.now().strftime("%Y-%m-%d")
st.markdown(f'<p class="current-date">Date: {current_date}</p>', unsafe_allow_html=True)

# Dynamic input fields for user data
st.markdown('<p class="custom-subheader">Entry</p>', unsafe_allow_html=True)
user_id = st.text_input("Enter an ID value: (User ID)", key="user_id_input", value="")
Name = st.text_input("Enter your name:", key="name", value="")
activity = st.text_input("What activity did you engage in today?", key="activity_input", value="")
positive = st.text_input("Did you experience something positive today?", key="positive_input", value="")
mood = st.text_input("Rate your mood on a scale of 1 to 10:", key="mood_input", value="")

# Additional questions
sleep_quality = st.slider("How well did you sleep last night? (Rate from 1 to 10)", 1, 10, 5, key="sleep_quality_input")
stress_levels = st.slider("On a scale of 1 to 10, how would you rate your stress levels today?", 1, 10, 5, key="stress_levels_input")
mindfulness = st.radio("Did you practice mindfulness or meditation today?", ["Yes", "No"], key="mindfulness_input")
connection_to_others = st.slider("How connected do you feel to others? (Rate from 1 to 10)", 1, 10, 5, key="connection_to_others_input")

# Add current date and time to the entry
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
entry = {
    "Timestamp": timestamp,
    "Activity": activity,
    "ID": user_id,
    "Positive": positive,
    "Mood": mood,
    "SleepQuality": sleep_quality,
    "StressLevels": stress_levels,
    "Mindfulness": mindfulness,
    "ConnectionToOthers": connection_to_others,
    "Name": Name,
}

# Insert data into the Deta Base
if st.button("Save Entry"):
    result = my_db.put(entry)
    st.success("Entry saved successfully:")
    st.write(result)

# Data Analysis and Bar Charts
st.markdown('<p class="custom-header">Data Analysis</p>', unsafe_allow_html=True)

# Retrieve all entries from the Deta Base
entries = my_db.fetch().items

# Group entries by user ID
grouped_entries = {}
for entry in entries:
    user_id = entry.get("ID")
    if user_id not in grouped_entries:
        grouped_entries[user_id] = []
    grouped_entries[user_id].append(entry)

# Show bar charts for Mood, Connections to Others, Stress Levels, and Sleep Quality
st.markdown('<p class="custom-subheader">Bar Charts</p>', unsafe_allow_html=True)

# Dropdown to select a specific user ID
selected_user_id = st.selectbox("Select User ID", list(grouped_entries.keys()))

# Display bar charts for the selected user
st.markdown(f'<p class="custom-subheader">User ID: {selected_user_id}</p>', unsafe_allow_html=True)
df_selected_user = pd.DataFrame(grouped_entries[selected_user_id])

# Bar chart for Mood
fig_mood = px.bar(df_selected_user, x="Timestamp", y="Mood", labels={'y': 'Mood'}, title=f'Mood for User ID: {selected_user_id}')
st.plotly_chart(fig_mood, use_container_width=True)

# Bar chart for Connections to Others
fig_connections = px.bar(df_selected_user, x="Timestamp", y="ConnectionToOthers", labels={'y': 'Connections to Others'},
                         title=f'Connections to Others for User ID: {selected_user_id}')
st.plotly_chart(fig_connections, use_container_width=True)

# Bar chart for Stress Levels
fig_stress = px.bar(df_selected_user, x="Timestamp", y="StressLevels", labels={'y': 'Stress Levels'},
                    title=f'Stress Levels for User ID: {selected_user_id}')
st.plotly_chart(fig_stress, use_container_width=True)

# Bar chart for Sleep Quality
fig_sleep = px.bar(df_selected_user, x="Timestamp", y="SleepQuality", labels={'y': 'Sleep Quality'},
                   title=f'Sleep Quality for User ID: {selected_user_id}')
st.plotly_chart(fig_sleep, use_container_width=True)
from streamlit.components.v1 import html

# Define your javascript
my_js = """
alert("Please don't forget to enter you daily details!!!");
"""

# Wrapt the javascript as html code
my_html = f"<script>{my_js}</script>"

# Execute your app

html(my_html)