import pipwin
import speech_recognition as sr
import pyttsx3

# Initialiser le moteur de synthèse vocale
engine = pyttsx3.init()

def parler(texte):
    """Fait parler l'assistant."""
    engine.say(texte)
    engine.runAndWait()



def ecouter():
    """Écouter et reconnaître la parole."""
    recognizer = sr.Recognizer()

    # Spécifier l'index du microphone (l'index dans la liste commence à 0)
    # Ici l'index semble être 3 pour "Matrice microphones interne"
    microphone_index = 3
    with sr.Microphone(device_index=microphone_index) as source:
        ("Je vous écoute...")
        recognizer.adjust_for_ambient_noise(source)  # Ajuster en fonction du bruit ambiant
        audio = recognizer.listen(source)

        try:
            texte = recognizer.recognize_google(audio, language='fr-FR')
            parler(f"Vous avez dit : {texte}")
            return texte
        except sr.UnknownValueError:
            parler("Désolé, je n'ai pas compris.")
            return ""
        except sr.RequestError:
            parler("Désolé, il y a un problème de connexion.")
            return ""

print("Microphones disponibles :")
print(sr.Microphone.list_microphone_names())