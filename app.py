### Health Management APP
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables
import time
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file, img_file_buffer):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    elif img_file_buffer is not None:
        # Check if an image has been captured
        # Read the image file buffer as bytes
        bytes_data = img_file_buffer.getvalue()

        image_parts = [
            {
                "mime_type": "image/jpeg",  # Assuming JPEG format
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
##initialize our streamlit app

st.set_page_config(page_title="Nutri-Genie App",page_icon=":apple:",initial_sidebar_state="collapsed")

st.header("Nutri-Genie App 🥙")
# input=st.text_input("Input Prompt: ",key="input")
# Add GitHub icon and link
st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Visit-brightgreen?style=for-the-badge&logo=github)](https://github.com/HimanshuMohanty-Git24/NutriGenie-Ai)")
input = ""
# Choose upload method
upload_option = st.radio("Choose upload method:", ("Upload Photo", "Take a Picture"))

uploaded_file = None
img_file_buffer = None

if upload_option == "Upload Photo":
    uploaded_file = st.file_uploader("Upload your meal Image...", type=["jpg", "jpeg", "png"])
    image = ""
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
else:
    img_file_buffer = st.camera_input("Capture your meal")

submit = st.button("Analyse my Meal🍴")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               FOOD ITEMS AND CALORIES:

                1. Item 1 - XXX calories
                2. Item 2 - XXX calories
                3. Item 3 - XXX calories

                TOTAL CALORIES:
                Your total caloric intake from this meal is XXX calories.

                NUTRITIONAL ANALYSIS:
                Based on my assessment, this meal contains the following ratios of macronutrients:

                - Carbohydrates: XX%
                - Protein: XX%
                - Fat: XX%

                RECOMMENDATION:
                [Your food is healthy/Your food is not healthy] because [detailed explanation of why it is or is not healthy].
                I would recommend [specific suggestions to improve meal healthiness] to help optimize your nutritional intake.
"""

## If submit button is clicked

if submit:
    with st.spinner('Analyzing your meal...'):
        image_data = input_image_setup(uploaded_file, img_file_buffer)
        response = get_gemini_repsonse(input_prompt, image_data, "")
        st.subheader("Your Nutritional Analysis:")
        st.write(response)