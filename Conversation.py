import calendar
import wikipedia
import random
import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def parlez(audio):
    engine.say(audio)
    engine.runAndWait()


def enregistrement_audio():
    enreg = sr.Recognizer()

    with sr.Microphone() as source:
        print("je suis votre assistant vocal, je vous écoute...")
        audio = enreg.listen(source)

    data = " "

    try:
        data = enreg.recognize_google(audio)
        print("vous avez dit: " + data)

    except sr.UnknownValueError:
        print("l'assistant vocal n'a pas compris l'audio")

    except sr.RequestError as ex:
        print("demander une erreur à la reconnaissance vocale de google" + ex)

    return data


def reponse(text):
    print(text)

    tts = gTTS(text=text, lang="fr")
    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)


def appel(text):
    appellation_action = "assistant vocal"
    text = text.lower()
    if appellation_action in text:
        return True
    return False


def date_dujour():
    maintenant = datetime.datetime.now()
    jour_actuelle = datetime.datetime.today()
    semaine_actuelle = calendar.day_name[jour_actuelle.weekday()]
    mois_actuel = maintenant.day

    mois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre",
            "decembre"]

    ordinaux = ["le 1", "le 2", "le 3", "le 4", "le 5", "le 6", "le 7", "le 8" "le 9" "le 10" "le 11" "le 12"
                                                                        "le 13", "le 14", "le 15", "le 16", "le 17",
                "le 18", "le 19", "le 20", "le 21", "le 22", "le 23",
                "le 24", "le 25", "le 26", "le 27", "le 28", "le 29", "le 30", "le 31"]

    return f'aujourdhui cest {semaine_actuelle}, {mois[mois_actuel - 1]} le {ordinaux[jour_actuelle - 1]},'


def dire_bonjour(text):
    salut = ["salut", "hello", "salutations", "comment ça va", "quoi de bon", "bonjour", "quoi de neuf"]
    reponse = ["salut", "hello", "salutations", "comment ça va", "quoi de bon", "bonjour", "quoi de neuf"]

    for word in text.split():
        if word.lower() in salut:
            return random.choice(reponse) + "."

    return ""


def wikipedia_person(text):
    liste_wikipedia = text.split()
    for i in range(0, len(liste_wikipedia)):
        if i + 3 <= len(liste_wikipedia) - 1 and liste_wikipedia[i].lower() == "qui" and liste_wikipedia[
           i + 1].lower() == "est":
            return liste_wikipedia[i + 2] + " " + liste_wikipedia[i + 3]


while True:
    try:
        text = enregistrement_audio()
        speak = " "

        if appel():

            speak = speak + dire_bonjour()

            if "date" in text or "jour" in text or "mois" in text:
                get_today = date_dujour()
                speak = speak + " " + get_today

            elif "time" in text:
                maintenant = datetime.datetime.now()
                meridiem = ""
                if maintenant.hour >= 12:
                    meridiem = "apres midi"
                    heure = maintenant.hour - 12

                else:
                    meridiem = "avant midi"
                    heure = maintenant.hour

                if maintenant.minute < 10:
                    minute = "0" + str(maintenant.minute)
                else:
                    minute = str(maintenant.minute)

                speak = speak + " " + "il est" + str(heure) + ":" + minute + " " + meridiem + "."

            elif "wikipedia" in text or "Wikipedia" in text:
                if "qui est" in text:
                    person = wikipedia_person(text)
                    wiki = wikipedia.summary(person, sentences=2)
                    speak = speak + " " + wiki

            reponse(speak)

    except:
        parlez("je ne le sais pas.")
