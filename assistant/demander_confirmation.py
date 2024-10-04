from assistant.speech import parler, ecouter

def demander_confirmation(type_question):
    while True:
        parler(f"vous avez dit {type_question} ai-je bien entendu ?")
        reponse = ecouter(3).lower()
        if "oui" in reponse or 'ouais' in reponse:
            break


