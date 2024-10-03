import webbrowser
from assistant.speech import parler

def naviguateur():
    parler("J'ouvre le navigateur.")
    webbrowser.open("https://")