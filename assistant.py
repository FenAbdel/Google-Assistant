import pywhatkit as ggl
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)    

with sr.Microphone() as source :
    text = "say what you want to search for ...."
    print(text)
    engine.say(text)
    engine.runAndWait()
    command= listener.recognize_google(listener.listen(source))

# Go to google and search
ggl.search(command)