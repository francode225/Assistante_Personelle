from assistant.speech import ecouter, parler, demander_nom, saluer_utilisateur
from assistant.commande import executer_commande, rechercher_video
from assistant.attente_assistante import attente_assitante

if __name__ == "__main__":
    #parler(f" {saluer_utilisateur()}, je suis  votre assistante personnelle et je suis à votre service")
    attente_assitante()
    #nom_utilisateur =demander_nom()
    while True:
        parler(f"chef  comment puis-je vous aider ?")
        commande = ecouter(5)
        executer_commande(commande)
        if 'stop' in commande:
            break
