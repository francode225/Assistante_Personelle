from assistant.commandes.calculatrice import calculatrice
from assistant.commandes.calendrier import calendrier
from assistant.commandes.capture_ecran import capture_ecran
from assistant.commandes.ecouter_musique import ecouter_musique
from assistant.commandes.envoyer_message_whatsapp import envoyer_message_whatsapp
from assistant.commandes.eteindre_ordinateur import eteindre_ordinateur
from assistant.commandes.heure import donner_heure
from assistant.commandes.naviguateur import naviguateur
from assistant.commandes.ouvre_youtube import ouvre_youtube
from assistant.commandes.ouvrir_whatsapp import ouvrir_whatsapp
from assistant.commandes.recherche_google import recherche_google
from assistant.commandes.recherche_wikipedia import recherche_wikipedia
from assistant.commandes.regarder_video import regarder_video
from assistant.demander_confirmation import demander_confirmation
from assistant.speech import parler, ecouter
from assistant.attente_assistante import attente_assitante
from assistant.commandes.converser import repondre_conversation

# Fonction pour exécuter des commandes
def executer_commande(commande):

    if "heure" in commande:
        donner_heure()

    elif "navigateur" in commande:
        return naviguateur()

    elif "ouvre whatsapp" in commande or "lance whatsapp" in commande:
        return  ouvrir_whatsapp()

    elif "ouvre youtube" in commande or "lance youtube" in commande:
        return ouvre_youtube()

    elif "calendrier" in commande:
        return calendrier()

    elif "calculatrice" in commande:
        return calculatrice()

    elif "cherche" in commande or "google" in commande:
        return recherche_google()

    elif "musique" in commande or "chanson" in commande :
        return ecouter_musique()
    elif "video" in commande or "youtube" in commande :
        return regarder_video()

    elif "éteins l'ordinateur" in commande or "arrête l'ordinateur" in commande or "arrêt de ordinateur" in commande:
        return eteindre_ordinateur()

    elif "wikipedia" in commande:
        parler("que voulez-vous rechercher sur wikipedia")
        recherche = ecouter(7)
        parler(recherche_wikipedia(recherche))

    elif "capture d'écran" in commande:
        parler("quelle nom voulez vous donner à la capture ?")
        nom =ecouter(5)
        demander_confirmation(nom)
        return capture_ecran(nom)

    elif "whatsapp" in commande:
        return envoyer_message_whatsapp()

    elif 'stop' in commande:
        parler("D'accord, je m'arrête.")
        exit()

    else:
        while True:
            parler("commençons la conversation")
            message = ecouter(5)
            parler(repondre_conversation(message))
            if 'stop conversation' in commande:
                break


    parler("Appelez moi si vous avez besoin de quelques choses")
    attente_assitante()


