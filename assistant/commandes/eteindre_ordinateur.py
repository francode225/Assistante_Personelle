import os

from assistant.demander_confirmation import demander_confirmation
from assistant.speech import parler, ecouter


def eteindre_ordinateur():
    parler("voulez-vous vraiment eteindre votre ordinateur")
    choix = ecouter(3)
    demander_confirmation("eteindre l'ordinateur")
    parler("J'éteins l'ordinateur.")
    os.system("shutdown /s /t 1")
