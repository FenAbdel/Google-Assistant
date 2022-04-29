import pywhatkit as ggl
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def print_talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source :
    print_talk("say what you want to search for ....")
    command= listener.recognize_google(listener.listen(source))

# Go to google and search
ggl.search(command)