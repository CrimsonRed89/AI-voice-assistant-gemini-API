import google.generativeai as genai
import os
import speech_recognition as sr
import pyttsx3

genai.configure(api_key=os.environ["API_KEY"])
#$env:API_KEY="your api"
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def get_mic_input():
    with sr.Microphone() as source:
        print("Please speak something:")
        audio = recognizer.listen(source)  
        try:
    
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None


while True:
    mic_input = get_mic_input()
    
    if mic_input:
        if mic_input.lower() == "stop":
            print("Stopping the program.")
            break 

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Please provide a brief answer to: {mic_input}")

        print(response.text)
        

        engine.say(response.text)
        engine.runAndWait()