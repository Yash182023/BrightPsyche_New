import streamlit as st
from pydub import AudioSegment
import tempfile

def main():
    st.title("Mindfulness Steps")

    # Apply custom CSS styling
    st.markdown(
        """
        <style>
            .title {
                color: #034525;
                font-size: 40px;
                text-align: center;
                margin-bottom: 20px;
                font-weight: bold;
            }
            h1{
                color:#034525;
            }
           .text {
            font-size: 16px;
            line-height: 1.5;
            color: #034525;
            margin-bottom: 20px; /* Adjust the value as needed */
            text-align: justify;
}


            .button {
                margin-top: 20px;
                padding: 10px 20px;
                font-size: 18px;
                cursor: pointer;
            }
            .main{
                background: radial-gradient(circle, #aae3c8 0%, #a1e3c8 50%, #8dd6c8 100%);

            }
        </style>
        """,
        unsafe_allow_html=True
    )

    meditation_steps = [
        "1)Find Your Quiet Spot: Find a cozy and quiet space where you won't be disturbed. It could be a corner in your room, a comfortable chair, or even a quiet park bench.",
        "2)Set a Time Limit: Start small. Decide on a reasonable time for your meditation session. Five minutes is perfect for beginners. You can always increase it as you get more comfortable.",
        "3)Get Comfortable: Sit comfortably on a cushion or chair. Make sure your back is straight, and your hands are resting on your lap or knees. Close your eyes gently or keep a soft gaze.",
        "4)Focus on Your Breath: Take a moment to notice your breath. Feel the sensation as you breathe in and out. It could be the air passing through your nostrils, the rise and fall of your chest, or the movement of your abdomen.",
        "5)Be Present: As you focus on your breath, your mind might wander. That's okay! When you notice it happening, gently guide your attention back to your breath. Be in the moment.",
        "6)No Judgments: Remember, there's no right or wrong here. If your mind wanders, don't be hard on yourself. Just acknowledge it and bring your focus back to your breath. It's a practice, not a perfect.",
        "7)Body Scan: If you want, scan your body from toes to head. Notice any sensations or tension, and let them go as you breathe.",
        "8)Loving-Kindness: Spread some love. In your mind, say phrases like May I/you be happy, may I/you be healthy, may I/you be safe, may I/you be at ease.",
        "9)Gradual End: As your session time ends, slowly bring your awareness back. Open your eyes, take a deep breath, and notice how you feel. Carry this sense of presence into the rest of your day.",
    ]

    # Display meditation steps with custom styling
    st.markdown('<p class="text">' + '<br>'.join(meditation_steps) + '</p>', unsafe_allow_html=True)

    # Voice selection
    voice_options = ["Male Voice", "Female Voice"]
    selected_voice = st.radio("Select Voice:", voice_options)

    # Play audio button
    if st.button("Play Audio"):
        # Load audio file based on the selected voice
        if selected_voice == "Male Voice":
            audio_path = "meditation_steps_male.wav"
        else:
            audio_path = "meditation_steps_female.wav"

        audio = AudioSegment.from_wav(audio_path)

        # Save audio to a temporary file
        temp_audio_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
        audio.export(temp_audio_path, format="wav")

        # Play the saved audio file
        st.audio(temp_audio_path, format="audio/wav", start_time=0, sample_rate=44100)

if __name__ == "__main__":
    main()
