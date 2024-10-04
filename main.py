from assistant.commandes.converser import repondre_conversation
from assistant.speech import ecouter, parler, demander_nom, saluer_utilisateur
from assistant.commande import executer_commande
from assistant.attente_assistante import attente_assitante

if __name__ == "__main__":
   #repondre_conversation("Comment vas-tu ?")
   # parler("Bonjour chef, je suis AXELLE votre assistante personnelle et je suis à votre service")
   attente_assitante()
   #nom_utilisateur =demander_nom()
   while True:
        parler(f"chef comment puis-je vous aider ?")
        commande = ecouter(5)
        if 'stoppe' in commande or "stop" in commande:
            break
        executer_commande(commande)


