import streamlit as st
from resume_generator import generate_resume
from utils import save_resume

st.set_page_config(page_title="AI Resume Automation", layout="centered")

st.title("📄 AI Resume Automation System")
st.write("Generate a professional resume using AI")

api_key = st.text_input("Enter OpenAI API Key", type="password")

name = st.text_input("Full Name")
role = st.text_input("Job Role")
experience = st.text_area("Work Experience")
skills = st.text_area("Skills")
education = st.text_area("Education")

if st.button("Generate Resume"):
    if not api_key:
        st.error("Please enter API key")
    else:
        resume = generate_resume(
            api_key, name, role, experience, skills, education
        )

        save_resume(resume)

        st.success("Resume Generated Successfully!")
        st.text(resume)
