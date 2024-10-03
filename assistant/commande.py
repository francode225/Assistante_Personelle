import pywhatkit as kit
from googleapiclient.discovery import build
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
from assistant.demander_confirmation import demander_confirmation
from assistant.speech import parler, ecouter
from assistant.attente_assistante import attente_assitante

youtube = build('youtube', 'v3', developerKey='AIzaSyCpjnyVm182r92QoqF3YFvta3A0jfnkykE')
def rechercher_video(titre):
    req = youtube.search().list(q=titre, part='id,snippet', maxResults=1)
    res = req.execute()
    video_id = res['items'][0]['id']['videoId']
    return f"https://www.youtube.com/watch?v={video_id}"

# Fonction pour exécuter des commandes
def executer_commande(commande):

    if "heure" in commande:
        donner_heure()

    elif "navigateur" in commande:
        return naviguateur()

    elif ("ouvre whatsapp" in commande):
        return  ouvrir_whatsapp()

    elif ("youtube" in commande):
        return ouvre_youtube()

    elif "calendrier" in commande:
        return calendrier()

    elif "calculatrice" in commande:
        return calculatrice()

    elif ("cherche" in commande or "google" in commande):
        return recherche_google()

    elif ("musique" in commande):
        return ecouter_musique()

    elif "éteins l'ordinateur" in commande or "arrête l'ordinateur" in commande or "arrêt de ordinateur" in commande:
        return eteindre_ordinateur()

    elif ("capture d'écran" in commande):
        parler("quelle nom voulez vous donner à la capture ?")
        nom =ecouter(5)
        demander_confirmation("le nom")
        return capture_ecran(nom)

    elif "whatsapp" in commande:
        return envoyer_message_whatsapp()

    elif 'stop' in commande:
        parler("D'accord, je m'arrête.")

    else:
        parler("Je n'ai pas cette commande.")

    parler("Appelez moi si vous avez besoin de quelques choses")
    attente_assitante()


