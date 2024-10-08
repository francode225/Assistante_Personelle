import datetime
import time

import pygame
import pipwin
import speech_recognition as sr
import pyttsx3

# Initialiser le moteur de synthèse vocale
engine = pyttsx3.init()

def parler(texte):
    """Fait parler l'assistant."""
    engine.say(texte)
    engine.runAndWait()



""" Liste des microphones disponibles
print("Microphones disponibles :")
microphones = sr.Microphone.list_microphone_names()
for i, microphone_name in enumerate(microphones):
    print(f"{i}: {microphone_name}") """

# Remplacez "3" par l'index correct que vous obtiendrez après avoir listé les microphones
def ecouter(temps_phrase: int):
    # Initialiser pygame mixer
    pygame.mixer.init()

    # Charger le son que tu veux jouer

    son_debut_path = "C:/Users/HP/assistante_personnelle/musique/debut.ogg"  # Remplace par le chemin de ton fichier son
    son_fin_path = "C:/Users/HP/assistante_personnelle/musique/fin 2.mp3."  # Remplace par le chemin de ton fichier son

    son_debut = pygame.mixer.Sound(son_debut_path)
    son_fin = pygame.mixer.Sound(son_fin_path)

    son_debut.set_volume(0.5)
    son_fin.set_volume(0.5)
    recognizer = sr.Recognizer()

    # Choisir l'index du microphone après avoir listé ceux disponibles
    microphone_index = 3  # Remplacez par l'index correct

    try:
        with sr.Microphone(device_index=microphone_index) as source:
            son_debut.play()
            print("J'écoute...")
            recognizer.adjust_for_ambient_noise(source)  # Ajuster pour le bruit ambiant
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=temps_phrase)

            try:
                commande = recognizer.recognize_google(audio, language='fr-FR')
                son_fin.play()
                time.sleep(1)  # Attendre un peu pour que le son se joue
                print(f"Vous avez dit : {commande}")
                return commande.lower()
            except sr.UnknownValueError:
                print("Désolé, je n'ai pas compris.")
                return ""
            except sr.RequestError:
                print("Désolé, problème de connexion.")
                return ""
    except AssertionError as e:
        print(f"Erreur de microphone : {e}")
        return ""

def demander_nom():
    parler("quel est votre prenom ")
    nom = ecouter(5)
    if nom != '':
        parler(f"bonjour chef {nom}")
    while nom == '' :
        parler("Je n'ai pas entendu votre nom. Pouvez vous repeter s'il vous plait ?")
    return nom

def saluer_utilisateur():
    """Salue l'utilisateur en fonction de l'heure actuelle."""
    heure_actuelle = datetime.datetime.now().hour  # Obtenir l'heure actuelle
    if 5 <= heure_actuelle < 12:  # De 5h à 11h59
        parler("Bonjour!")
    elif 12 <= heure_actuelle < 18:  # De 12h à 17h59
        parler("Bonjour!")  # Vous pouvez personnaliser cela pour l'après-midi si vous le souhaitez
    else:  # De 18h à 4h59
        parler("Bonsoir!")

