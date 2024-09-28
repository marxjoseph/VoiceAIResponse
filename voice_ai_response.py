import os
import google.generativeai as genai
import speech_recognition as sr
from dotenv import load_dotenv

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

# Load environment variables from .env file
load_dotenv()

# Now you can access the API key
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Use Google Web Speech API for recognition and let AI respond
try:
    audio_input = recognizer.recognize_google(audio)
    print("You said: " + audio_input)
    print(model.generate_content(audio_input).text)
except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")
