import streamlit as st
from google import genai
from dotenv import load_dotenv
import os, time

st.header("AI Code Debugger")
st.subheader("Upload screenshots of error, get hints/solution with code")
st.divider()

st.write("Upload error's screenshots:")
images = st.file_uploader("Upload Files",
                 type=["png","jpg","jpeg"],
                 accept_multiple_files=True)

if images:
    if (len(images)>3):
        st.error("Please upload no more than 3 images")

option = st.selectbox("Select one option: ",("Hint","Solution with code"),index=None)

btn = st.button("Debug",type="primary")

if btn:
    if not images:
        st.error("Please upload image first")
    if not option:
        st.error("Select an option: Hint/Solution with code")
        

load_dotenv()

apiKey = os.getenv("GEMINI_API_KEY")

client = genai.Client()

response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = "explain useEffect() to a react js beginner"
)

st.write(response.text)
        
        

