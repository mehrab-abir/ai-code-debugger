import streamlit as st
from google import genai
from dotenv import load_dotenv
from PIL import Image
import os, time

def stream_text(text):
    for word in text.split(' '):
        yield word + ' ';
        time.sleep(0.05)

load_dotenv()
apiKey = os.getenv("GEMINI_API_KEY")

st.header("AI Code Debugger")
st.subheader("Upload screenshots of error, get hints/solution with code")
st.divider()

images = st.file_uploader("Upload error's screenshots(maximum 3):",
                 type=["png","jpg","jpeg"],
                 accept_multiple_files=True)

if images:
    if (len(images)>3):
        st.error("Please upload no more than 3 images")
    else:
        option = st.selectbox("Select one option: ",("Hint","Solution with code"),index=None)

        btn = st.button("Debug",type="primary")

        if btn:
            if not images:
                st.error("Please upload image first")
            if not option:
                st.error("Select an option: Hint/Solution with code")
                
            if images and option:
                pill_images = []
                for img in images:
                    pil_img = Image.open(img)
                    pill_images.append(pil_img)

                client = genai.Client()
                
                if(option== "Hint"):
                    prompt = "Looking at the images, explain the error is and give me hint to fix the bug, do not give direct solution"
                else:
                    prompt = "Looking at the images, explain the error and give me the solution with code"
                
                with st.spinner("Finding solution..."):
                    response = client.models.generate_content(
                        model = "gemini-3-flash-preview",
                        contents = [pill_images,prompt]
                    )

                    st.write_stream(stream_text(response.text))

                
            
                
        

        

