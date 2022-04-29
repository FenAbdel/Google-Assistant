import pywhatkit as ggl
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
with sr.Microphone() as source :
    print("say what you want to search for ....")
    voice = listener.listen(source)
    command= listener.recognize_google(voice)

# Go to google and search
ggl.search(command)