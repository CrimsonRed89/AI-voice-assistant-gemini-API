# Voice AI Assistant with Gemini API
A real-time voice AI assistant that uses Google's Gemini API to generate text responses based on your speech input and reads the responses aloud. This assistant runs continuously until you say "stop."

## Features
Speech-to-Text: Captures voice input from the microphone and converts it to text.
AI-Powered Response: Uses Gemini API to generate responses.
Text-to-Speech: Reads responses back to the user in a natural-sounding voice. 
Looped Operation: Continuously listens for input and responds until you say "stop."

## Requirements
Python 3.7+
Libraries:
google-generativeai: For accessing the Gemini API.
SpeechRecognition: For capturing and transcribing speech.
pyttsx3: For Text-to-Speech output.
pyaudio: Required for SpeechRecognition to access the microphone.

## Installation
1. Clone the Repository:
bash
```
git clone https://github.com/your-username/voice-ai-assistant
cd voice-ai-assistant
```
2. Install Dependencies:
bash
```
pip install google-generativeai SpeechRecognition pyttsx3 pyaudio
```
Note: If you encounter issues with pyaudio, you may need to install the PyAudio wheel file manually.

3. Set up the Gemini API Key:
Obtain your API key from Google Gemini and set it as an environment variable:

On Linux/macOS:
bash
```
export API_KEY="your_api_key_here"
```

On Windows Command Prompt:
cmd
```
set API_KEY="your_api_key_here"
```

On Windows PowerShell:
powershell
```
$env:API_KEY="your_api_key_here"
```

## Usage
Run the Python script to start the assistant:
bash
```
python assistant.py
```

## Instructions
1. Launch the Script: After starting the script, the assistant begins by listening for your input.
2. Speak Your Query: Speak into the microphone; the assistant will transcribe your words and send them to the Gemini API for processing.
3. Receive and Hear the Response: The assistant reads the generated response back to you.
4. Stop Command: Say "stop" to exit the assistant.
   
## Code Overview
The assistant operates in three main steps:

Input: Captures voice input using SpeechRecognition.
AI Processing: Sends the text input to the Gemini API using google.generativeai to get a response.
Output: Uses pyttsx3 to convert the AI response into audio and reads it aloud.

## Customization
Change TTS Voice:
Modify the voice and rate properties in the engine.setProperty function to adjust the voice type and speed.

Error Handling:
The script has basic error handling for transcription and API errors. Customize error messages or actions as desired.

## Contributing
Feel free to submit issues or pull requests to enhance the assistant!
