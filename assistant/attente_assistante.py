from assistant.speech import ecouter, parler


def attente_assitante():
    while True:
        commande = ecouter(5)
        if "axel" in commande or "assistante" in commande:
            return
        elif "stop" in commande or "arrêt" in commande or "arrête" in commande:
            break
