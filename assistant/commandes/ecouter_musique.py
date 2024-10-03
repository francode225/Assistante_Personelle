from assistant.speech import parler, ecouter
import pywhatkit as kit

def ecouter_musique():
    while True:
        parler("Quelle musique voulez-vous écouter sur YouTube ?")
        recherche = ecouter(5)
        # Ouvre une recherche sur YouTube
        if recherche:
            parler(f"vous voulez ecouter {recherche}")
            kit.playonyt(recherche)
            # url = rechercher_video(recherche)
            # webbrowser.open(url)
            break
        else:
            parler("Je n'ai pas entendu pouvez-vous repeter ?")