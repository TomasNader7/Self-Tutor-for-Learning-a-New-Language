
from gtts import gTTS
from googletrans import LANGUAGES, Translator
import speech_recognition as sr  # speech-to-text python library
import pyttsx3  # text-to-speech python library



# Function to print all suported languages
def display_supported_languages():
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")
   

# Display the supported languages
print('List of languages available: \n')
display_supported_languages()


while True:
    # Prompt the user to choose a language
    language_code = input('\nChoose the language code of the language you wish to learn: \n')

    # Display the user's choice\
    if language_code in LANGUAGES:
        print('\nYou entered:', language_code)
        print('Language chosen:', LANGUAGES[language_code])
        break
    else:
        print('\nInvalid language code. Please try again.')
    


def speech_to_text_and_save():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Recognizing...")
         # Recognize the speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print(f"Text: {text}")

        # Save the recognized text to a file
        with open("transcribed_text.txt", "w") as file:
            file.write(text)
            print("Transcribed text saved to transcribed_text.txt")
    except sr.UnknownValueError:
        # Handle the case where speech is unintelligible
        print("Could not understand audio.")
    except sr.RequestError as e:
        # Handle the case where there is an error with the Google Web Speech API
        print(f"Error connecting to Google API: {e}")
        

        
def text_to_speech():
    # Open the transcribed text file
    file = open('transcribed_text.txt')
    content = file.read()  # Read the content of the file
    file.close()

    translator = Translator()
    try:
        # Translate the content to the selected language
        translated_text = translator.translate(content, dest=language_code).text
        print(f"Translated Text: {translated_text}")
        
        # Convert the translated text to speech
        tts = gTTS(translated_text, lang=language_code, slow=False)
        tts.save('output.wav')  # Save the audio file
        print("Audio saved as output.wav")
    except Exception as e:
        # Handle the case where translation fails
        print(f"Translation failed: {e}")
    


if __name__ == "__main__":
    # Execute the functions to convert speech to text and then to translated speech
    speech_to_text_and_save()
    text_to_speech()
  