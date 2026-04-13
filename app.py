import sys, os
sys.path.insert(0, os.getcwd())

import streamlit as st
from utils.session import init_session
from components.upload import upload_screen
from components.interview import interview_screen
from components.report import report_screen

st.set_page_config(page_title="AI Interview", layout="centered")

init_session()

if st.session_state.step == "upload":
    upload_screen()
elif st.session_state.step == "interview":
    interview_screen()
else:
    report_screen()