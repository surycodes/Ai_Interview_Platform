import streamlit as st

def init_session():
    if "step" not in st.session_state:
        st.session_state.step = "upload"
    if "questions" not in st.session_state:
        st.session_state.questions = []
    if "current_q" not in st.session_state:
        st.session_state.current_q = 0
    if "scores" not in st.session_state:
        st.session_state.scores = []