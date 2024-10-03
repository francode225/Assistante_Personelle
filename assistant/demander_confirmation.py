from assistant.speech import parler, ecouter

def demander_confirmation(type_question):
    while True:
        parler(f"ai-je bien entendu {type_question}")
        reponse = ecouter(3).lower()
        if "oui" in reponse:
            break


