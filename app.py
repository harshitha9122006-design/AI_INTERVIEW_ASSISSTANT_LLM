import streamlit as st
from groq import Groq
st.set_page_config(page_title="PLACEMENT PREPARATION",page_icon="😍",layout="centered")
st.title("AI_INTERVIEW_ASSISTANT")
st.caption("Practice and prepare for placement")
try:
  client=Groq(api_key=st.secrets["GROQ_API_KEY"])
except(Keyerror, FileNotFound):
  st.error("API Key is missing.Add it in advanced settings")
  st.stop()
role=st.selectbox('Job Title',['Machine learning engineer','Deveops engineer','Prompt engineer','Senior software engineer','Others'])
if role=="Others":
  st.text_input("Enter you job title","XXXXXX")
