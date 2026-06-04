import sys
import os
import streamlit as st

sys.path.insert(0, os.getcwd())

from utils.session import init_session
from components.upload import upload_screen
from components.interview import interview_screen
from components.report import report_screen

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🎯",
    layout="centered"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

.stApp {
    background-color: #f8fafc;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #1e3a8a;
    margin-top: 10px;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    font-size: 16px;
    color: #64748b;
    margin-bottom: 25px;
}

.card {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 2px 12px rgba(0,0,0,0.08);
    border: 1px solid #e2e8f0;
    margin-top: 15px;
}

.stButton > button {
    background: #2563eb;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.4rem 1rem;
    width: auto;
    min-width: 120px;
    height: 38px;
    font-size: 14px;
    font-weight: 500;
}

.stButton > button:hover {
    background: #1d4ed8;
}

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 40px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SESSION
# --------------------------------------------------
init_session()

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    '<div class="main-title">AI Interview Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Practice Interviews with AI-Powered Resume Analysis</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# PROGRESS BAR
# --------------------------------------------------
if st.session_state.step == "upload":
    st.progress(33)
    st.caption("Step 1 of 3 • Upload Resume")

elif st.session_state.step == "interview":
    st.progress(66)
    st.caption("Step 2 of 3 • Interview Round")

else:
    st.progress(100)
    st.caption("Step 3 of 3 • Performance Report")

# --------------------------------------------------
# CONTENT AREA
# --------------------------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

if st.session_state.step == "upload":
    upload_screen()

elif st.session_state.step == "interview":
    interview_screen()

else:
    report_screen()

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    """
    <div class="footer">
        Powered by AI • Resume Analysis • Interview Preparation
    </div>
    """,
    unsafe_allow_html=True
)
