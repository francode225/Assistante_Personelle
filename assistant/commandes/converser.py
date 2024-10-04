from transformers import pipeline

generateur = pipeline('text-generation', model='gpt2')

prompt_de_base = """
Tu es AXELLE, une assistante personnelle créée par François que tu appellera chef. 
Ton rôle est d'aider François en tenant des conversations et en faisant des recherches. 
Tu dois être utile, informative, et amicale. 
Réponds de manière concise et intelligente. 
"""

def repondre_conversation(message_utilisateur):
    """Utilise GPT-2 pour générer une réponse avec un contexte de base."""
    prompt_complet = f"{prompt_de_base}\nFrançois: {message_utilisateur}\nAXELLE:"
    reponse = generateur(prompt_complet, max_length=50, num_return_sequences=1)[0]['generated_text']
    # Extraire la réponse après "AXELLE :" pour éviter de renvoyer le contexte
    reponse_finale = reponse.split("AXELLE:")[1].strip() if "AXELLE:" in reponse else reponse.strip()
    return reponse_finale
