import pywhatkit as kit

from assistant.speech import parler


def capture_ecran(nom_fichier):
    try:
        kit.take_screenshot(nom_fichier)
        parler(f"Capture d'écran enregistrée avec succès sous le nom : {nom_fichier}")
    except Exception as e:
        print(f"Erreur lors de la capture d'écran : {e}")