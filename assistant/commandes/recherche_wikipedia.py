import wikipedia

def recherche_wikipedia(terme):
    """Recherche la première ligne d'un article Wikipedia."""
    try:
        resultat = wikipedia.summary(terme, sentences=3)
        return resultat
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Trop de résultats pour {terme}. Veuillez préciser."
    except wikipedia.exceptions.PageError:
        return "Aucune page trouvée."