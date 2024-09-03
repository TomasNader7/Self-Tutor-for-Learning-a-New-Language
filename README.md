# Speech Translator and Text-to-Speech Converter
This Python program enables users to record speech, transcribe it to text, translate the text into a different language, and convert the translated text into speech. The program leverages libraries like speech_recognition, googletrans, and gtts to achieve these functionalities.

# FEATURES
<ul> <li><b>Speech Recognition:</b> Converts spoken language into written text.</li> <li><b>Text Translation:</b> Translates the transcribed text into a user-selected language.</li> <li><b>Text-to-Speech Conversion:</b> Converts the translated text back into spoken language.</li> <li><b>Language Support:</b> Allows users to choose from a wide range of languages supported by Google Translate.</li> </ul>

# PREREQUISITES
Before running this program, ensure you have the following Python libraries installed:

<ul> <li><code>gTTS</code>: Google's Text-to-Speech API.</li> <li><code>googletrans</code>: Google Translate API.</li> <li><code>speech_recognition</code>: Speech-to-Text conversion library.</li> <li><code>pyttsx3</code>: Python Text-to-Speech library.</li> </ul>
<ol> <li><b>You can install these dependencies using pip:</b> <pre><code>
pip install gtts googletrans==4.0.0-rc1 SpeechRecognition pyttsx3</code></pre>

# USAGE
<ol> <li><b>Run the Program:</b> <pre><code>python &lt;script_name&gt;.py</code></pre> Replace <code>&lt;script_name&gt;</code> with the name of your Python script. </li> <li><b>Select Language:</b> <ul> <li>The program will display a list of supported languages with their respective codes.</li> <li>Enter the language code of the language you want to translate the text into.</li> </ul> </li> <li><b>Record Speech:</b> <ul> <li>The program will prompt you to speak.</li> <li>Speak clearly into the microphone.</li> </ul> </li> <li><b>Transcription:</b> <ul> <li>Your speech will be transcribed and saved to a file named <code>transcribed_text.txt</code>.</li> </ul> </li> <li><b>Translation and Text-to-Speech:</b> <ul> <li>The transcribed text will be translated to your selected language.</li> <li>The translated text will be converted to speech and saved as <code>output.wav</code>.</li> </ul> </li> </ol>

# PROGRAM WORKFLOW
<ol> <li><b>Language Selection:</b> <ul> <li>The user is presented with a list of supported languages.</li> <li>The user selects a language by entering the corresponding language code.</li> </ul> </li> <li><b>Speech-to-Text:</b> <ul> <li>The user records their speech.</li> <li>The program transcribes the speech into text and saves it in <code>transcribed_text.txt</code>.</li> </ul> </li> <li><b>Text Translation and Speech Conversion:</b> <ul> <li>The transcribed text is translated into the selected language.</li> <li>The translated text is converted into an audio file (<code>output.wav</code>).</li> </ul> </li> </ol>

# ERROR HANDLING
<ul> <li>The program includes basic error handling to manage: <ul> <li>Invalid language codes.</li> <li>Unintelligible speech.</li> <li>Connection issues with the Google Web Speech API.</li> <li>Translation failures.</li> </ul> </li> </ul>
