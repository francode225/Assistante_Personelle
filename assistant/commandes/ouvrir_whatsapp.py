import webbrowser

from assistant.speech import parler

def ouvrir_whatsapp():
    parler("J'ouvre WhatsApp.")
    webbrowser.open("https://web.whatsapp.com")