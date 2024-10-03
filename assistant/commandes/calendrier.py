import os

from assistant.speech import parler

def calendrier():
    parler("J'ouvre le calendrier.")
    os.system("start outlookcal:")