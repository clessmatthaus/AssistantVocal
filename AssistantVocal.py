import os
import playsound
import speech_recognition as sr
import wikipedia
from gtts import gTTS
import webbrowser


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("exception" + str(e))
    return said


def speak(text):
    tts = gTTS(text=text, lang='fr')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)


while True:
    text = get_audio().lower()
    if 'facebook' in text:
        speak("ok connection sur facebook")
        webbrowser.open_new_tab("https://fr-fr.facebook.com/")
    elif 'wikipedia' in text:
        speak("connection page wikipedia")
        query = text.replace("recherche", "")
        result = wikipedia.summary(query, sentences=3)
        speak("resultat selon wikipedia")
        print(result)
        speak(result)
    elif 'bonjour' in text:
        speak("bonjour cless, comment vas-tu?")
    elif 'good' in text:
        speak('je vais bien, merci')
    elif 'story' in text:
        speak("Tom Sawyer")
    elif 'thank' in text:
        speak("je t'enprie beaugoss")
    elif 'news' in text:
        speak("rien de spécial")
    elif 'bye' in text:
        speak("au revoir, à la prochaine")
    elif 'bonn' in text:
        speak("merci, bonne journée à toi aussi")
