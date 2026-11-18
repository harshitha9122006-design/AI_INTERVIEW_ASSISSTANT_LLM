import streamlit as st
from groq import groq
st.set_page_config(page_title="PLACEMENT PREPARATION",page_icon="😍",layout="centered")
st.title("AI_INTERVIEW_ASSISTANT")
st.caption("Practice and prepare for placement")
try:
  client=Groq(api_key=st.secrets["GROQ_API_KEY"])
except (Keyerror, FileNotFound);
st.error("API Key is missing.Add it in advanced settings")
st.stop()
