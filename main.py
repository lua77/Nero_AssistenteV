import speech_recognition as sr
import pyttsx3

machine = pyttsx3.init()
r = sr.Recognizer()

with sr.Microphone() as source:
    voz = r.listen(source)
    comando = r.recognize_google(voz, language='pt-BR').lower()
    print(comando)

    machine.say(comando)
    machine.runAndWait()