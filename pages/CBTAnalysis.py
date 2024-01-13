import streamlit as st
import pandas as pd
from streamlit.components.v1 import html
class Therapy:
    def __init__(self, condition):
        self.condition = condition
        self.answers = {}
        self.weights = {}

    def ask_questions(self, my_questions):
        for key, question in my_questions.items():
            unique_key = f"{self.condition}_{key}"  # Create a unique key
            st.write(f"{key}) {question}")
            answer = st.text_input(f"Answer for {key}:", key=unique_key)  # Pass the unique key
            rating = st.slider(f"Rate your answer for {key} (1-10):", 1, 10, 5)  # Slider for ratings
            self.answers[unique_key] = answer
            self.weights[unique_key] = rating


    def predict_problem_rating(self):
        total_weight = sum(self.weights.values())
        if total_weight == 0:
            st.warning("Warning: Total weight is zero. Please make sure to assign weights to the questions.")
            return None

        weighted_sum = sum(self.weights[key] for key in self.weights if key in self.answers)

        average_score = weighted_sum / 10
        return average_score

def main():
    st.markdown(
    """
    <style>
        .main {
            background-image: radial-gradient(circle, #f902da, #f363e6, #ff5900);

        }
      
        .title {
            color: #f0f0f0;
            font-size: 48px;
            text-align: center;
            font-weight: bold;
        }
        .st-bx{
            color: #0d0101;
            background-color: #f0f0f0;
        }
        .st-bt{
            background-color: #f0f0f0;
        }
            
        
        .css-c2zpwa:hover,css-c2zpwa:active,css-c2zpwa:focus{
            background: #ffffff;
        }
        
        
    </style>
    """,
    unsafe_allow_html=True)
    
    st.markdown('<p class="title">CBT Questionaire</p>', unsafe_allow_html=True)

    conditions = ["Intro-therapy", "ADHD", "PTSD", "BPD"]
    selected_condition = st.selectbox("Select for a condition:", conditions)

    therapy = Therapy(selected_condition)

    if selected_condition == "Intro-therapy":
        my_questions = {
            1: "What type of Emotions are you experiencing?",
            2: "At what time do you sleep?",
            3: "How do you interact with family or friends?",
            4: "At what time do you wake up?",
            5: "What are your goals?",
            6: "How do you see people around?",
            7: "How much do you eat?"
        }
    
    if selected_condition == "ADHD":
        my_questions = {
                1: "What are some common challenges you face in you?",
                2: "Can you identify specific situations where you feel your ADHD symptoms are most problematic or disruptive?",
                3: "How do you currently perceive your ADHD symptoms? Are there any negative thought patterns associated with them?",
                4: "Have you noticed any recurring thought patterns or beliefs about yourself and your abilities that might affect your self-esteem or motivation?",
                5: "How do you typically react when you realize you've made a mistake or forgotten something important due to your ADHD symptoms?",
                6: "Are there specific tasks or activities that you tend to procrastinate on? What thoughts or feelings arise when you're faced with these tasks?",
                7: "Can you recall times when you've successfully managed your ADHD symptoms or used effective strategies? What was different about those situations?"
            }
        
    if selected_condition == "PTSD":
        my_questions = {
                1: "Does your intuition tell you that what you remember is or was real, no matter how hard you try to disbelieve it?",
                2: "Does the memory keep returning, even after you try to forget it?",
                3: "Does the memory fit with your habits, fears, behaviors, symptoms, health problems, or the facts of your life as you know them?",
                4: "Is your memory of certain aspects of the traumatic event clear?",
                5: "Are certain aspects of the event cloudy?",
                6: "Does your memory come in fragments?",
                7: "Does remembering anything about the event bring you a sense of relief, understanding, or increased strength?"
            }
        
    if selected_condition == "BPD":
        my_questions = {
                1: "Are there any recurring negative thoughts or self-criticisms you've been experiencing?",
                2: "Can you identify any cognitive distortions in your thinking?",
                3: "Can you describe the intensity and nature of your emotions?",
                4: "What actions or behaviors have you engaged in recently that you'd like to discuss?",
                5: "Are there any strategies or skills you've been using to manage your emotions?",
                6: "Can you share any recent experiences or conflicts in your relationships?",
                7: "Are there any conflicts or inconsistencies in your self-image that you'd like to explore?"
            }
        
    therapy.ask_questions(my_questions)
    if st.button("Submit"):
        predicted_rating = therapy.predict_problem_rating()
        st.write(f"Predicted Problem Rating: {predicted_rating:.2f} (on a scale of 1-10)")
        st.write("If score is below 5 please have a chat with our bot, it is urgent")

if __name__ == "__main__":
    main()

