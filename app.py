import sys
import os
import streamlit as st

sys.path.insert(0, os.getcwd())

from utils.session import init_session
from components.upload import upload_screen
from components.interview import interview_screen
from components.report import report_screen

# Page Configuration
st.set_page_config(
    page_title="AI Interview Bot",
    page_icon="🤖",
    layout="centered"
)

# Initialize Session
init_session()

# Header
st.markdown(
    """
    <h1 style='text-align:center;'>
        <span style='color:red;'>🤖</span> AI Interview Bot
    </h1>
    """,
    unsafe_allow_html=True
)

st.divider()

# Navigation
if st.session_state.step == "upload":

    with st.chat_message("assistant"):
        st.write(
            "👋 Hi! Upload your resume and I'll generate interview questions based on your profile."
        )

    upload_screen()

elif st.session_state.step == "interview":

    with st.chat_message("assistant"):
        st.write(
            "🎤 Welcome to the interview round. Let's begin!"
        )

    interview_screen()

else:

    with st.chat_message("assistant"):
        st.write(
            "📊 Interview completed. Here is your performance report."
        )

    report_screen()
