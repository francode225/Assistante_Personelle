
from assistant.speech import parler, ecouter
import pywhatkit as kit
def regarder_video():
    while True:
        parler("Quelle video voulez-vous regarder sur YouTube ?")
        recherche = ecouter(5)
        # Ouvre une recherche sur YouTube
        if recherche:
            parler(f"vous voulez regarder {recherche}")
            kit.playonyt(recherche)
            break
        else:
            parler("Je n'ai pas entendu pouvez-vous repeter ?")