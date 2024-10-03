import os
from assistant.speech import parler

def calculatrice():
    parler("J'ouvre la calculatrice.")
    os.system("calc")
