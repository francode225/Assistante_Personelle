import datetime
import pywhatkit as kit

from assistant.demander_confirmation import demander_confirmation
from assistant.speech import parler, ecouter


def envoyer_message_whatsapp():
    try:
        # Demander à l'utilisateur s'il veut envoyer le message à une personne ou dans un groupe
        parler("Voulez-vous envoyer le message à une personne ou dans un groupe ?")
        destination = ecouter(5).lower()  # Écoute la réponse de l'utilisateur

        if "groupe" in destination:
            parler("Dites le nom du groupe WhatsApp.")
            groupe = ecouter(10)  # Écoute le nom du groupe
            numero_sans_espace = groupe  # Utiliser le nom du groupe comme destination
        else:
            parler("Dite moi le numéro de téléphone WhatsApp sur lequel vous voulez envoyer le message.")
            telephone = ecouter(7)
            demander_confirmation("le numero")
            numero = f"+225{telephone}"  # Numéro au format international
            numero_sans_espace = numero.replace(" ", "")

        # Demander si l'utilisateur veut envoyer le message immédiatement ou le programmer
        parler("Voulez-vous envoyer le message immédiatement ou le programmer à une heure spécifique ?")
        choix_temps = ecouter(5).lower()

        if "programmer" in choix_temps:
            # Demander l'heure et les minutes pour la programmation
            parler("Dites l'heure à laquelle vous voulez envoyer le message.")
            heure = int(ecouter(2))  # Écoute l'heure
            demander_confirmation("l'heure")
            parler("Dites la minutes de l'heure à laquelle vous voulez envoyer le message..")
            demander_confirmation("le nombre de minute")
            minute = int(ecouter(2))  # Écoute les minutes
        else:
            # Utiliser l'heure et la minute actuelles pour l'envoi immédiat
            heure = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute + 2  # Ajoute un léger décalage

        # Préparer le message
        parler("Dites le message que vous voulez envoyer.")
        ecoute = ecouter(10)
        message_assistante = "Ce message est envoyé par l'assistante personnelle `AXELLE` de _MR YEO_"
        message = f" *{message_assistante.upper()}* \n {ecoute}"

        # Envoie le message à un numéro via WhatsApp
        kit.sendwhatmsg(numero_sans_espace, message, heure, minute)
        parler("Message envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi du message : {e}")

