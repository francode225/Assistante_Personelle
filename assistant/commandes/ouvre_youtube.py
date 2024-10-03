import webbrowser

from assistant.speech import parler


def ouvre_youtube():
    parler("J'ouvre YouTube.")
    webbrowser.open("https://www.youtube.com")