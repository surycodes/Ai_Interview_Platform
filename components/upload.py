import streamlit as st
from services.ai_engine import generate_questions, evaluate_answer
from services.parser import extract_text  # 👈 add this

def upload_screen():

    # Session setup
    if "questions" not in st.session_state:
        st.session_state.questions = []
        st.session_state.current_q = 0
        st.session_state.show_next = False

    # 👇 NEW: File uploader instead of text input
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    resume_text = ""

    if uploaded_file:
        resume_text = extract_text(uploaded_file)  # 👈 convert PDF → text
        st.success("✅ Resume uploaded successfully")

    # Generate questions
    if st.button("Generate Questions") and resume_text:
        st.session_state.questions = generate_questions(resume_text)
        st.session_state.current_q = 0
        st.session_state.show_next = False

    qs = st.session_state.questions
    idx = st.session_state.current_q

    # Interview flow
    if qs and idx < len(qs):
        st.markdown(f"### Question {idx+1}")
        st.write(qs[idx])

        ans = st.text_area("Your Answer", key=f"ans_{idx}")

        if st.button("Submit Answer"):
            res = evaluate_answer(qs[idx], ans)
            st.write("### 📊 Feedback")
            st.write(res)
            st.session_state.show_next = True

        if st.session_state.show_next:
            if st.button("Next Question"):
                st.session_state.current_q += 1
                st.session_state.show_next = False

    # Completion
    if qs and idx >= len(qs):
        st.success("🎉 Interview Completed!")