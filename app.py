### Health Management APP
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

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

def input_image_setup(uploaded_file):
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
    else:
        raise FileNotFoundError("No file uploaded")
##initialize our streamlit app

st.set_page_config(page_title="Nutri-Genie App",page_icon=":apple:",layout="wide",initial_sidebar_state="collapsed")

st.header("Nutri-Genie App")
# input=st.text_input("Input Prompt: ",key="input")
input = ""
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me the total calories")

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
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)