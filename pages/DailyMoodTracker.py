# # import streamlit as st
# # import pandas as pd
# # from datetime import datetime
# # from plyer import notification

# # class MentalHealthTracker:
# #     def __init__(self, user_id):
# #         self.user_id = user_id
# #         self.daily_answers = {}
# #         self.weekly_suggestions = {}

# #     def ask_daily_questions(self, daily_questions):
# #         today_date = datetime.now().strftime("%Y-%m-%d")
# #         st.subheader(f"Daily Questions - {today_date}")

# #         for key, question in daily_questions.items():
# #             unique_key = f"{today_date}_{key}"
# #             st.write(f"{key}) {question}")
# #             answer = st.text_input(f"Answer for {key}:", key=unique_key)
# #             self.daily_answers[unique_key] = answer

# #     def save_daily_answers_to_csv(self, filename):
# #         df = pd.DataFrame(list(self.daily_answers.items()), columns=['Question ID', 'Answer'])
# #         df.to_csv(filename, index=False)
# #         st.success(f"Daily Answers saved to {filename}")

# #     def set_daily_reminder(self, reminder_time):
# #         # Set a daily reminder using plyer
# #         now = datetime.now()
# #         notification_time = datetime.strptime(reminder_time, "%H:%M")

# #         # Calculate time until the next daily reminder
# #         time_until_reminder = (datetime.combine(now.date(), notification_time.time()) - now).total_seconds()

# #         # Schedule the reminder
# #         notification.notify(
# #             title=f"Daily Reminder",
# #             message="Don't forget to answer your daily mental health questions!",
# #             timeout=int(time_until_reminder),
# #         )

# # def main():
# #     st.markdown(
# #     """
# #     <style>
# #         .main {
# #             background-color: #14839f;  /* Set your desired background color */
# #         }
      
# #         .title {
# #             color: #f0f0f0;
# #             font-size: 48px;
# #             text-align: center;
# #             font-weight: bold;
# #         }
# #         .st-bx{
# #             color: #0d0101;
# #         }
# #         .st-bt{
# #             background-color: #f0f0f0;
# #         }
# #     </style>
# #     """,
# #     unsafe_allow_html=True)
# #     st.markdown('<p class="title">Mental Health Tracker App</p>', unsafe_allow_html=True)


# #     # User ID
# #     user_id = st.text_input('Enter User ID:', key='user_id')


# #     # Create MentalHealthTracker instance
# #     mental_health_tracker = MentalHealthTracker(user_id)

# #     # Daily Questions
# #     daily_questions = {
# #         1: "How would you rate your overall mood today?",
# #         2: "Did you engage in any physical activity today?",
# #         3: "What is one positive thing that happened today?",
# #         4: "Is there anything on your mind that you'd like to share?",
# #         # Add more daily questions as needed
# #     }

# #     # Set a daily reminder
# #     reminder_time = st.text_input("Set a daily reminder time (HH:MM):", "09:00")
# #     mental_health_tracker.set_daily_reminder(reminder_time)

# #     # Ask daily questions
# #     mental_health_tracker.ask_daily_questions(daily_questions)

# #     if st.button("Save Daily Answers"):
# #         st.button("Save Daily Answers", key="save_button")
# #         mental_health_tracker.save_daily_answers_to_csv(f"{user_id}_daily_answers.csv")

# # if __name__ == "__main__":
# #     main()
# # import streamlit as st
# # from datetime import datetime
# # from deta import Deta


# # # Load the environment variables
# # DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # # Initialize with a project key
# # deta = Deta(DETA_KEY)
# # my_db = deta.Base("data_reports")
# # class MentalHealthTracker:
# #     def __init__(self, user_id):
# #         self.user_id = user_id
# #         self.daily_answers = {}

# #     def ask_daily_questions(self, daily_questions):
# #         today_date = datetime.now().strftime("%Y-%m-%d")
# #         st.subheader(f"Daily Questions - {today_date}")

# #         for key, question in daily_questions.items():
# #             unique_key = f"{today_date}_{key}"
# #             st.write(f"{key}) {question}")
# #             answer = st.text_input(f"Answer for {key}:", key=unique_key)
# #             self.daily_answers[unique_key] = answer

# #     def save_daily_answers_to_deta(self, deta_base):
# #         data_to_insert = {
# #             "Timestamp": datetime.now(),
# #             "Activity": self.daily_answers.get("activity", ""),
# #             "ID": self.daily_answers.get("id_value", ""),
# #             "Positive": self.daily_answers.get("positive", ""),
# #             "Mood": self.daily_answers.get("mood", ""),
# #         }

# #         # Insert data into Deta Base
# #         result = my_db.put(data_to_insert)

# #         # Display the result
# #         st.success("Daily Answers saved successfully to Deta Base:")
# #         st.write(result)

   

# # def main():
# #     st.markdown(
# #     """
# #     <style>
# #         .main {
# #             background-color: #14839f;  /* Set your desired background color */
# #         }
      
# #         .title {
# #             color: #f0f0f0;
# #             font-size: 48px;
# #             text-align: center;
# #             font-weight: bold;
# #         }
# #         .st-bx{
# #             color: #0d0101;
# #         }
# #         .st-bt{
# #             background-color: #f0f0f0;
# #         }
# #     </style>
# #     """,
# #     unsafe_allow_html=True)
# #     st.markdown('<p class="title">Mental Health Tracker App</p>', unsafe_allow_html=True)

# #     # User ID
# #     user_id = st.text_input('Enter User ID:', key='user_id')

# #     # Create Deta Base instance
# #     deta_base = deta.Base("mental_health_data")

# #     # Create MentalHealthTracker instance
# #     mental_health_tracker = MentalHealthTracker(user_id)

# #     # Daily Questions
# #     daily_questions = {
# #         "activity": "What activity did you engage in today?",
# #         "id_value": "Enter an ID value:",
# #         "positive": "Did you experience something positive today?",
# #         "mood": "Rate your mood on a scale of 1 to 10:",
# #         # Add more daily questions as needed
# #     }

# #     # Set a daily reminder
# #     reminder_time = st.text_input("Set a daily reminder time (HH:MM):", "09:00")
# #     mental_health_tracker.set_daily_reminder(reminder_time)

# #     # Ask daily questions
# #     mental_health_tracker.ask_daily_questions(daily_questions)

# #     if st.button("Save Daily Answers"):
# #         st.button("Save Daily Answers", key="save_button")
# #         mental_health_tracker.save_daily_answers_to_deta(deta_base)

# # if __name__ == "__main__":
# #     main()
# # import streamlit as st
# # from datetime import datetime
# # from deta import Deta

# # # Load the environment variables
# # DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # # Initialize with a project key
# # deta = Deta(DETA_KEY)
# # my_db = deta.Base("data_reports")

# # class MentalHealthTracker:
# #     def __init__(self, user_id):
# #         self.user_id = user_id
# #         self.daily_answers = {}

# #     def ask_daily_questions(self, daily_questions):
# #         today_date = datetime.now().strftime("%Y-%m-%d")
# #         st.subheader(f"Daily Questions - {today_date}")

# #         for key, question in daily_questions.items():
# #             unique_key = f"{today_date}_{key}"
# #             st.write(f"{key}) {question}")
# #             answer = st.text_input(f"Answer for {key}:", key=unique_key)
# #             self.daily_answers[unique_key] = answer

# #     def save_daily_answers_to_deta(self, deta_base):
# #         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# #         data_to_insert = {
# #             "Timestamp": timestamp,
# #             "Activity": self.daily_answers.get("activity", ""),
# #             "ID": self.daily_answers.get("id_value", ""),
# #             "Positive": self.daily_answers.get("positive", ""),
# #             "Mood": self.daily_answers.get("mood", ""),
# #         }

# #     # Insert data into Deta Base
# #         result = my_db.put(data_to_insert)

# #     # Display the result
# #         st.success("Daily Answers saved successfully to Deta Base:")
# #         st.write(result)


# # def main():
# #     st.markdown(
# #     """
# #     <style>
# #         .main {
# #             background-color: #14839f;  /* Set your desired background color */
# #         }
      
# #         .title {
# #             color: #f0f0f0;
# #             font-size: 48px;
# #             text-align: center;
# #             font-weight: bold;
# #         }
# #         .st-bx{
# #             color: #0d0101;
# #         }
# #         .st-bt{
# #             background-color: #f0f0f0;
# #         }
# #     </style>
# #     """,
# #     unsafe_allow_html=True)
# #     st.markdown('<p class="title">Mental Health Tracker App</p>', unsafe_allow_html=True)

# #     # User ID
# #     user_id = st.text_input('Enter User ID:', key='user_id')

# #     # Create MentalHealthTracker instance
# #     mental_health_tracker = MentalHealthTracker(user_id)

# #     # Daily Questions
# #     daily_questions = {
# #         "activity": "What activity did you engage in today?",
# #         "id_value": "Enter an ID value:",
# #         "positive": "Did you experience something positive today?",
# #         "mood": "Rate your mood on a scale of 1 to 10:",
# #         # Add more daily questions as needed
# #     }

# #     # Ask daily questions
# #     mental_health_tracker.ask_daily_questions(daily_questions)

# #     if st.button("Save Daily Answers"):
# #         st.button("Save Daily Answers", key="save_button")
# #         mental_health_tracker.save_daily_answers_to_deta(my_db)

# # if __name__ == "__main__":
# #     main()
# import streamlit as st
# from datetime import datetime
# from deta import Deta

# # Load the environment variables
# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)
# my_db = deta.Base("data_reports")

# class MentalHealthTracker:
#     def __init__(self, user_id):
#         self.user_id = user_id
#         self.daily_answers = {}

#     def ask_daily_questions(self, daily_questions):
#         today_date = datetime.now().strftime("%Y-%m-%d")
#         st.subheader(f"Daily Questions - {today_date}")

#         for key, question in daily_questions.items():
#             unique_key = f"{today_date}_{key}"
#             st.write(f"{key}) {question}")
#             answer = st.text_input(f"Answer for {key}:", key=unique_key)
#             self.daily_answers[unique_key] = answer

#     def save_daily_answers_to_deta(self, my_db):
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         data_to_insert = {
#             "Timestamp": timestamp,
#             "Activity": self.daily_answers.get("activity", ""),
#             "ID": self.daily_answers.get("id_value", ""),
#             "Positive": self.daily_answers.get("positive", ""),
#             "Mood": self.daily_answers.get("mood", ""),
#         }

#         # Debugging statements
#         st.write("Data to insert:")
#         st.write(data_to_insert)

#         # Insert data into Deta Base
#         result = my_db.put(data_to_insert)

#         # Debugging statements
        
#         # Display the result
#         st.success("Daily Answers saved successfully to Deta Base:")
#         st.write(result)

# def main():
#     st.markdown(
#         """
#         <style>
#             .main {
#                 background-color: #14839f;  /* Set your desired background color */
#             }
          
#             .title {
#                 color: #f0f0f0;
#                 font-size: 48px;
#                 text-align: center;
#                 font-weight: bold;
#             }
#             .st-bx{
#                 color: #0d0101;
#             }
#             .st-bt{
#                 background-color: #f0f0f0;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True)
#     st.markdown('<p class="title">Mental Health Tracker App</p>', unsafe_allow_html=True)

#     # Use st.session_state to persist the object across runs
#     if 'mental_health_tracker' not in st.session_state:
#         user_id = st.text_input('Enter User ID:', key='user_id')
#         st.session_state.mental_health_tracker = MentalHealthTracker(user_id)

#     # Create MentalHealthTracker instance
#     mental_health_tracker = st.session_state.mental_health_tracker

#     # Daily Questions
#     daily_questions = {
#         "activity": "What activity did you engage in today?",
#         "id_value": "Enter an ID value:",
#         "positive": "Did you experience something positive today?",
#         "mood": "Rate your mood on a scale of 1 to 10:",
#         # Add more daily questions as needed
#     }

#     # Ask daily questions
#     mental_health_tracker.ask_daily_questions(daily_questions)

#     if st.button("Save Daily Answers"):
#         st.button("Save Daily Answers", key="save_button")
#         mental_health_tracker.save_daily_answers_to_deta(my_db)

# if __name__ == "__main__":
#     main()
# import streamlit as st
# from datetime import datetime
# from deta import Deta

# # Load the environment variables
# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)

# # Create Deta Base instance
# my_db = deta.Base("data_reports")

# # Ask questions before entries
# st.header("Daily Entry Questions")


# # Dynamic input fields for user data
# st.subheader("Entry")
# activity = st.text_input(f"What activity did you engage in today?", value="")
# user_id = st.text_input(f"Enter an ID value: (User ID)", value="")
# positive = st.text_input(f"Did you experience something positive today?", value="")
# mood = st.text_input(f"Rate your mood on a scale of 1 to 10:", value="")

# # Add current date and time to the entry
# timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# entry = {
#     "Timestamp": timestamp,
#     "Activity": activity,
#     "ID": user_id,
#     "Positive": positive,
#     "Mood": mood,
# }

# # Insert data into the Deta Base
# if st.button("Save Entry"):
#     result = my_db.put(entry)
#     st.success("Entry saved successfully:")
#     st.write(result)
# import streamlit as st
# from datetime import datetime
# from deta import Deta

# # Load the environment variables
# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)

# # Create Deta Base instance
# my_db = deta.Base("bright_psych_data")

# # Custom CSS
# custom_css = """
#     <style>
#         .main {
#             background-color: #14839f;
#         }
#         .custom-header {
#             color: #ffffff; /* Set your desired color for headers */
#             font-size: 40px;
#             font-weight: bold;
#             margin-bottom: 10px;
#             text-align: center;
#         }
#         .custom-subheader {
#             color: #ffffff; /* Set your desired color for subheaders */
#             font-size: 18px;
#             margin-bottom: 5px;
#             font-weight: bold;
#         }
#     </style>
# """
# st.markdown(custom_css, unsafe_allow_html=True)

# # Ask questions before entries
# st.markdown('<p class="custom-header">Daily Mood Tracker</p>', unsafe_allow_html=True)

# current_date = datetime.now().strftime("%Y-%m-%d")
# st.markdown(f'<p class="current-date">Date: {current_date}</p>', unsafe_allow_html=True)

# # Dynamic input fields for user data
# st.markdown('<p class="custom-subheader">Entry</p>', unsafe_allow_html=True)
# user_id = st.text_input("Enter an ID value: (User ID)", key="user_id_input", value="")
# Name = st.text_input("Enter your name:", key="name", value="")
# activity = st.text_input("What activity did you engage in today?", key="activity_input", value="")
# positive = st.text_input("Did you experience something positive today?", key="positive_input", value="")
# mood = st.text_input("Rate your mood on a scale of 1 to 10:", key="mood_input", value="")

# # Additional questions
# sleep_quality = st.slider("How well did you sleep last night? (Rate from 1 to 10)", 1, 10, 5, key="sleep_quality_input")
# stress_levels = st.slider("On a scale of 1 to 10, how would you rate your stress levels today?", 1, 10, 5, key="stress_levels_input")
# mindfulness = st.radio("Did you practice mindfulness or meditation today?", ["Yes", "No"], key="mindfulness_input")
# connection_to_others = st.slider("How connected do you feel to others? (Rate from 1 to 10)", 1, 10, 5, key="connection_to_others_input")

# # Add current date and time to the entry
# timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# entry = {
#     "Timestamp": timestamp,
#     "Activity": activity,
#     "ID": user_id,
#     "Positive": positive,
#     "Mood": mood,
#     "SleepQuality": sleep_quality,
#     "StressLevels": stress_levels,
#     "Mindfulness": mindfulness,
#     "ConnectionToOthers": connection_to_others,
#     "Name": Name,
# }

# # Insert data into the Deta Base
# if st.button("Save Entry"):
#     result = my_db.put(entry)
#     st.success("Entry saved successfully:")
#     st.write(result)

# import streamlit as st
# from datetime import datetime
# from deta import Deta
# import plotly.express as px
# import pandas as pd

# # Load the environment variables
# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)

# # Create Deta Base instance
# my_db = deta.Base("bright_psych_data")

# # Custom CSS
# custom_css = """
#     <style>
#         .main {
#             background-color: #14839f;
#         }
#         .custom-header {
#             color: #ffffff; /* Set your desired color for headers */
#             font-size: 40px;
#             font-weight: bold;
#             margin-bottom: 10px;
#             text-align: center;
#         }
#         .custom-subheader {
#             color: #ffffff; /* Set your desired color for subheaders */
#             font-size: 18px;
#             margin-bottom: 5px;
#             font-weight: bold;
#         }
#     </style>
# """
# st.markdown(custom_css, unsafe_allow_html=True)

# # Ask questions before entries
# st.markdown('<p class="custom-header">Daily Mood Tracker</p>', unsafe_allow_html=True)

# current_date = datetime.now().strftime("%Y-%m-%d")
# st.markdown(f'<p class="current-date">Date: {current_date}</p>', unsafe_allow_html=True)

# # Dynamic input fields for user data
# st.markdown('<p class="custom-subheader">Entry</p>', unsafe_allow_html=True)
# user_id = st.text_input("Enter an ID value: (User ID)", key="user_id_input", value="")
# Name = st.text_input("Enter your name:", key="name", value="")
# activity = st.text_input("What activity did you engage in today?", key="activity_input", value="")
# positive = st.text_input("Did you experience something positive today?", key="positive_input", value="")
# mood = st.text_input("Rate your mood on a scale of 1 to 10:", key="mood_input", value="")

# # Additional questions
# sleep_quality = st.slider("How well did you sleep last night? (Rate from 1 to 10)", 1, 10, 5, key="sleep_quality_input")
# stress_levels = st.slider("On a scale of 1 to 10, how would you rate your stress levels today?", 1, 10, 5, key="stress_levels_input")
# mindfulness = st.radio("Did you practice mindfulness or meditation today?", ["Yes", "No"], key="mindfulness_input")
# connection_to_others = st.slider("How connected do you feel to others? (Rate from 1 to 10)", 1, 10, 5, key="connection_to_others_input")

# # Add current date and time to the entry
# timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# entry = {
#     "Timestamp": timestamp,
#     "Activity": activity,
#     "ID": user_id,
#     "Positive": positive,
#     "Mood": mood,
#     "SleepQuality": sleep_quality,
#     "StressLevels": stress_levels,
#     "Mindfulness": mindfulness,
#     "ConnectionToOthers": connection_to_others,
#     "Name": Name,
# }

# # Insert data into the Deta Base
# if st.button("Save Entry"):
#     result = my_db.put(entry)
#     st.success("Entry saved successfully:")
#     st.write(result)

# # Data Analysis and Bar Charts
# st.markdown('<p class="custom-header">Data Analysis</p>', unsafe_allow_html=True)

# # Retrieve all entries from the Deta Base
# entries = my_db.fetch().items

# # Group entries by user ID
# grouped_entries = {}
# for entry in entries:
#     user_id = entry.get("ID")
#     if user_id not in grouped_entries:
#         grouped_entries[user_id] = []
#     grouped_entries[user_id].append(entry)

# # Show bar charts for Mood, Connections to Others, Stress Levels, and Sleep Quality
# st.markdown('<p class="custom-subheader">Bar Charts for Each Person</p>', unsafe_allow_html=True)

# for user_id, user_entries in grouped_entries.items():
#     st.markdown(f'<p class="custom-subheader">User ID: {user_id}</p>', unsafe_allow_html=True)
#     df_user = pd.DataFrame(user_entries)
    
#     # Bar chart for Mood
#     fig_mood = px.bar(df_user, x="Timestamp", y="Mood", labels={'y': 'Mood'}, title=f'Mood for User ID: {user_id}')
#     st.plotly_chart(fig_mood, use_container_width=True)

#     # Bar chart for Connections to Others
#     fig_connections = px.bar(df_user, x="Timestamp", y="ConnectionToOthers", labels={'y': 'Connections to Others'},
#                              title=f'Connections to Others for User ID: {user_id}')
#     st.plotly_chart(fig_connections, use_container_width=True)

#     # Bar chart for Stress Levels
#     fig_stress = px.bar(df_user, x="Timestamp", y="StressLevels", labels={'y': 'Stress Levels'},
#                         title=f'Stress Levels for User ID: {user_id}')
#     st.plotly_chart(fig_stress, use_container_width=True)

#     # Bar chart for Sleep Quality
#     fig_sleep_quality = px.bar(df_user, x="Timestamp", y="SleepQuality", labels={'y': 'Sleep Quality'},
#                                title=f'Sleep Quality for User ID: {user_id}')
#     st.plotly_chart(fig_sleep_quality, use_container_width=True)
import streamlit as st
from datetime import datetime
from deta import Deta
import plotly.express as px
import pandas as pd
from streamlit.components.v1 import html
# Load the environment variables
DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

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