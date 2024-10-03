import datetime

from assistant.speech import parler

def donner_heure():
    heure_actuelle = datetime.datetime.now().strftime("%H:%M")
    parler(f"Il est actuellement {heure_actuelle}")