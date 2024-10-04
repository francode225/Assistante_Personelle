from assistant.speech import ecouter, parler


def attente_assitante():
    while True:
        commande = ecouter(5)
        if "stoppe" in commande or "arrêt" in commande or "arrête" in commande:
            break
        elif "axel" in commande or "assistante" in commande:
            return
