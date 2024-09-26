from assistant.speech import ecouter, parler

if __name__ == "__main__":
    parler("Bonjour, comment puis-je vous aider ?")
    while True:
        commande = ecouter()
        if 'stop' in commande:
            parler("D'accord, je m'arrête.")
            break
