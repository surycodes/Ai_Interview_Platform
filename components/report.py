import streamlit as st

def report_screen():
    st.title("📊 Report")

    for i, r in enumerate(st.session_state.scores):
        st.write(f"Q{i+1}:")
        st.write(r)

    st.success("Done 🎉")