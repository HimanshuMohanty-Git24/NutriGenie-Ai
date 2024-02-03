# NutriGenie-Ai 🍏💻

End-to-End Nutritionist Generative AI Doctor using Google Gemini Pro Vision Large Image Models.
![image](https://github.com/HimanshuMohanty-Git24/NutriGenie-Ai/assets/94133298/1a946072-4a89-456a-9d5d-44473fd66602)


# Demo 📦✅

Live App link : [NutriGenie](https://nutrigenie-ai.streamlit.app/)

## Overview

NutriGenie-Ai is an application that leverages Google Gemini Pro Vision Large Image Models to provide nutritional analysis of your meals. The AI-powered nutritionist analyzes images of your meals, calculates total calories, provides details on each food item's calorie intake, and offers a nutritional breakdown.

## Tech Stack

- [Streamlit](https://streamlit.io/): Frontend framework for creating web applications with Python.
- [Google Gemini Pro Vision](https://cloud.google.com/blog/topics/inside-google-cloud/advanced-solutions-for-vision-and-text-using-gemini-pro): Large image models for advanced vision and text solutions.
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/): Python Imaging Library to handle images.
- [NumPy](https://numpy.org/): Library for numerical operations.
- [TensorFlow](https://www.tensorflow.org/): Open-source machine learning framework.
- [Streamlit Webrtc](https://github.com/whitphx/streamlit-webrtc): Streamlit extension for real-time video processing.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HimanshuMohanty-Git24/NutriGenie-Ai.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd NutriGenie-Ai
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain Google Gemini Pro Vision API Key:**
   - Visit the [Google Makersuite](https://makersuite.google.com/app/).
   - Create a new project or select an existing one.
   - Create API credentials (API key) and use it in project.

5. **Set up environment variables:**
   - Create a `.env` file in the project root.
   - Add your Google API key to the `.env` file:
     ```env
     GOOGLE_API_KEY=your_api_key_here
     ```

6. **Run the app:**
   ```bash
   streamlit run app.py
   ```

7. **Access the app:**
   Open your web browser and go to [http://localhost:8501](http://localhost:8501).

## Usage

1. Choose the upload method: either "Upload Photo" or "Take a Picture."
2. Upload an image of your meal or capture one using the camera.
3. Click "Analyse my Meal" to get a detailed nutritional analysis.

## Important Note

Ensure that you use your own Google Gemini Pro Vision API key for accessing the advanced image models. Protect your API key and avoid sharing it publicly.

Feel free to contribute, report issues, or suggest improvements!
