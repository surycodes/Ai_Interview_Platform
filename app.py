import sys
import os
import streamlit as st

sys.path.insert(0, os.getcwd())

from utils.session import init_session
from components.upload import upload_screen
from components.interview import interview_screen
from components.report import report_screen

st.set_page_config(
page_title="AI Interview Bot",
page_icon="🤖",
layout="centered"
)

init_session()

st.markdown(
""" <h1 style='text-align:center;'>🤖 AI Interview Bot</h1> <p style='text-align:center;color:gray;'>
Upload your resume and chat with your AI interviewer </p>
""",
unsafe_allow_html=True
)

st.divider()

if st.session_state.step == "upload":
st.chat_message("assistant").write(
"👋 Hi! Upload your resume and I'll generate interview questions based on your profile."
)
upload_screen()

elif st.session_state.step == "interview":
st.chat_message("assistant").write(
"🎤 Welcome to the interview round. Let's begin!"
)
interview_screen()

else:
st.chat_message("assistant").write(
"📊 Interview completed. Here is your performance report."
)
report_screen()
