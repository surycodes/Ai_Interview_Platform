import streamlit as st
from services.ai_engine import evaluate_answer

# 🔊 Voice output
from gtts import gTTS

# 🎤 Browser audio
from streamlit_webrtc import webrtc_streamer  # pyright: ignore


# -----------------------------
# 🔊 Text to Speech
# -----------------------------
def speak(text):
    tts = gTTS(text)
    tts.save("voice.mp3")


# -----------------------------
# 💬 Main Interview Screen
# -----------------------------
def interview_screen():

    # Safety check
    if "questions" not in st.session_state:
        st.warning("⚠️ Please upload resume first")
        return

    qs = st.session_state.questions
    idx = st.session_state.current_q

    # Progress bar
    st.progress((idx + 1) / len(qs))

    if idx < len(qs):

        st.markdown(f"### Question {idx+1}")
        st.write(qs[idx])

        # 🔊 Play question
        if st.button("🔊 Play Question"):
            speak(qs[idx])
            st.audio("voice.mp3")

        st.divider()

        # -------------------------
        # ✍️ TEXT INPUT
        # -------------------------
        st.subheader("✍️ Type your answer")
        text_answer = st.text_area("Write your answer here", key=f"text_{idx}")

        st.divider()

        # -------------------------
        # 🎤 VOICE INPUT (FIXED)
        # -------------------------
        st.subheader("🎤 Voice Input")

        ctx = webrtc_streamer(
            key=f"voice_{idx}",
            media_stream_constraints={
                "audio": True,
                "video": False
            }
        )

        if ctx.state.playing:
            st.success("🎤 Recording... Speak now")
        else:
            st.info("👉 Click START to enable microphone")

        st.caption("🎧 Allow microphone access in browser")

        # -------------------------
        # 🧠 SESSION STATE
        # -------------------------
        if "feedback" not in st.session_state:
            st.session_state.feedback = ""

        # -------------------------
        # ✅ SUBMIT
        # -------------------------
        if st.button("Submit Answer"):

            if not text_answer:
                st.warning("⚠️ Please provide an answer")
            else:
                st.session_state.feedback = evaluate_answer(qs[idx], text_answer)

        # -------------------------
        # 📊 FEEDBACK
        # -------------------------
        if st.session_state.feedback:

            st.markdown("### 📊 Feedback")
            st.write(st.session_state.feedback)

            # 🔊 Play feedback
            if st.button("🔊 Play Feedback"):
                speak(st.session_state.feedback)
                st.audio("voice.mp3")

            # Next question
            if st.button("Next Question"):
                st.session_state.current_q += 1
                st.session_state.feedback = ""

    else:
        st.success("🎉 Interview Completed!")