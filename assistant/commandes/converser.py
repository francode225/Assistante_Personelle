import requests

# Remplacez par votre token Hugging Face
TOKEN = "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"

# URL de l'API pour GPT-Neo
API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-1.3B"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

# Prompt de base pour guider les réponses de l'assistante
prompt_de_base = """
Tu es AXELLE, une assistante personnelle qui parle principalement en français, créée par François que tu appelles "chef". 
Ton rôle est d'aider François en tenant des conversations et en faisant des recherches. 
Tu dois être utile, informative, et amicale. 
Réponds de manière concise et intelligente. 
"""


def repondre_conversation(message_utilisateur):
    """Génère une réponse avec un contexte de base en utilisant l'API de Hugging Face."""
    prompt_complet = f"{prompt_de_base}\nFrançois: {message_utilisateur}\nAXELLE:"
    payload = {
        "inputs": prompt_complet,
        "parameters": {
            "max_new_tokens": 50,
            "do_sample": True,
            "top_k": 50,
            "top_p": 0.95,
            "temperature": 0.7
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Vérifie si la requête a réussi

        # Extraction de la réponse du modèle
        reponse = response.json()[0]['generated_text']

        # Extraire la partie après "AXELLE:" pour éviter de renvoyer le prompt complet
        if "AXELLE:" in reponse:
            reponse_finale = reponse.split("AXELLE:")[1].strip()
        else:
            reponse_finale = reponse.strip()

        print(reponse_finale)
        return reponse_finale

    except Exception as e:
        print(f"Erreur lors de la génération de la réponse : {e}")
        return "Désolé, une erreur est survenue."



