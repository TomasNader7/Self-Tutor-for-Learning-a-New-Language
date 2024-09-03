Speech Translator and Text-to-Speech Converter: 
This Python program enables users to record speech, transcribe it to text, translate the text into a different language, and convert the translated text into speech. The program leverages libraries like speech_recognition, googletrans, and gtts to achieve these functionalities.

FEATURES
Speech Recognition: Converts spoken language into written text.
Text Translation: Translates the transcribed text into a user-selected language.
Text-to-Speech Conversion: Converts the translated text back into spoken language.
Language Support: Allows users to choose from a wide range of languages supported by Google Translate.

PREREQUISITES
Before running this program, ensure you have the following Python libraries installed:

gTTS: Google's Text-to-Speech API.
googletrans: Google Translate API.
speech_recognition: Speech-to-Text conversion library.
pyttsx3: Python Text-to-Speech library.
You can install these dependencies using pip:
pip install gtts googletrans==4.0.0-rc1 SpeechRecognition pyttsx3

USAGE
Run the Program:
python <script_name>.py
Replace <script_name> with the name of your Python script.

Select Language:
The program will display a list of supported languages with their respective codes.
Enter the language code of the language you want to translate the text into.

Record Speech:
The program will prompt you to speak.
Speak clearly into the microphone.

Transcription:
Your speech will be transcribed and saved to a file named transcribed_text.txt.

Translation and Text-to-Speech:
The transcribed text will be translated to your selected language.
The translated text will be converted to speech and saved as output.wav.

PROGRAM WORKFLOW
Language Selection:
The user is presented with a list of supported languages.
The user selects a language by entering the corresponding language code.

Speech-to-Text:
The user records their speech.
The program transcribes the speech into text and saves it in transcribed_text.txt.

Text Translation and Speech Conversion:
The transcribed text is translated into the selected language.
The translated text is converted into an audio file (output.wav).

ERROR HANDLING
The program includes basic error handling to manage:
Invalid language codes.
Unintelligible speech.
Connection issues with the Google Web Speech API.
Translation failures.
