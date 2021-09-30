import os
import playsound
import speech_recognition as sr
import wikipedia
from gtts import gTTS
import webbrowser
import winshell
from datetime import datetime
from pygame import mixer


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1

        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError:
            speak("désolé, je n'ai pas compris.")
        except sr.RequestError:
            speak("désolé le service demandé, n'est pas disponible")
    return said.lower()


def speak(text):
    tts = gTTS(text=text, lang='fr')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)


def respond():
    print("texte à partir de l'audio" + text)
    if 'youtube' in text:
        speak("Que voulez-vous chercher sur you tube")
        keyword = get_audio()
        if keyword != '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"voici ce que j'ai trouvé sur youtube {keyword}")
    elif 'recherche search' in text:
        speak("quel est l'objet de votre recherche?")
        query = get_audio()
        if query != '':
            result = wikipedia.summary(query, sentences=3)
            speak("resultat selon wikipedia")
            print(result)
            speak(result)
    elif 'jokes' in text:
        speak("vas dormir cless")
    elif 'time' in text:
        strTime = datetime.today().strftime(" il est %H:%M %p")
        print(strTime)
        speak(strTime)
    elif 'Music' in text or 'song' in text:
        speak("lecture en cours...")
        music_dir = "C:\\Users\\clessmatthaus\\Desktop\\Music"
        songs = os.listdir(music_dir)
        print(songs)
        playmusic(music_dir + "\\" + songs[0])
    elif 'stop' in text:
        speak("arrêt de la lecture.")
        stopmusic()
    elif 'bye' in text:
        speak("au revoir, bonne journée.")
        exit()


def playmusic(song):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()


def stopmusic():
    mixer.music.stop()


while True:
    print("j'écoute....")
    text = get_audio()
    respond()
