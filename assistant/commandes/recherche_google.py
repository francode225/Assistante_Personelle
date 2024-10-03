import webbrowser

from assistant.speech import parler, ecouter

def recherche_google():
    parler("Que voulez-vous chercher?")
    recherche = ecouter(5)
    webbrowser.open(f"https://www.google.com/search?q={recherche}")
