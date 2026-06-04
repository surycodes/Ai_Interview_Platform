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
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 50px;
    font-weight: 700;
    color: #38bdf8;
    margin-top: 10px;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 25px;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 20px;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    background: linear-gradient(90deg,#2563eb,#06b6d4);
    color: white;
    font-size: 16px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    transform: scale(1.02);
    transition: 0.3s;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

.footer {
    text-align:center;
    color:#94a3b8;
    margin-top:40px;
    font-size:14px;
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
    '<div class="main-title">🤖 AI Interview Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Upload Resume • Practice Interview • Get AI Feedback</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.title("📋 Dashboard")

    if st.session_state.step == "upload":
        st.success("Current Step")
        st.write("📄 Resume Upload")

    elif st.session_state.step == "interview":
        st.success("Current Step")
        st.write("🎤 AI Interview")

    else:
        st.success("Current Step")
        st.write("📊 Interview Report")

# --------------------------------------------------
# PROGRESS BAR
# --------------------------------------------------
if st.session_state.step == "upload":
    st.progress(33)
    st.caption("Step 1 of 3 - Upload Resume")

elif st.session_state.step == "interview":
    st.progress(66)
    st.caption("Step 2 of 3 - AI Interview")

else:
    st.progress(100)
    st.caption("Step 3 of 3 - Final Report")

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
        🚀 Powered by AI • Resume Analysis • Interview Preparation
    </div>
    """,
    unsafe_allow_html=True
)
