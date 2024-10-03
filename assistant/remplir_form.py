from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Lancer le navigateur Chrome
driver = webdriver.Chrome()

# URL de votre formulaire Google
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfYR7hLK9PScRN2whr6sbdfVxS3VtDoa08VLq4Y79s-PKVdLg/viewform?vc=0&c=0&w=1&flr=0&usp=mail_form_link'  # Remplacez par l'URL de votre formulaire

driver.get(form_url)

# Attendre que la page se charge
time.sleep(2)

def remplir_formulaire():
    wait = WebDriverWait(driver, 10)

    # 1. Avez-vous déjà voyagé avec une compagnie de transport sur axe Abidjan-Korhogo ?
    voyage_axe = random.choice(['Oui', 'Non'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{voyage_axe}"]'))).click()
    print(f'Voyage axe choisi: {voyage_axe}')

    # 2. Connaissez-vous des compagnies de transports sur axe Abidjan-Korhogo ?
    connaissance_axe = random.choice(['Oui', 'Non', 'Autre :'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{connaissance_axe}"]'))).click()

    # 3. Si oui lesquelles ?
    if connaissance_axe == 'Oui':
        compagnies = ['UTRAKO', 'UTNA', 'CHONCO', 'LEOPARD', 'MTK', 'UTS', 'STB', 'CK']
        compagnie_choisie = random.choice(compagnies)
        wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{compagnie_choisie}"]'))).click()

    # 4. Par quel(s) moyen(s) avez-vous connu ?
    moyens = ['Affichage', 'Presse', 'Réseaux sociaux', 'Bouche à oreille', 'Radio', 'Télévision']
    for moyen in random.sample(moyens, 2):  # Choisir deux moyens aléatoires
        wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{moyen}"]'))).click()

    # 6. Connaissez-vous la compagnie de transport UTS ?
    connaissance_uts = random.choice(['Oui', 'Non'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{connaissance_uts}"]'))).click()

    # 7. Par quel moyen avez-vous connu ?
    moyens_uts = ['Affichage', 'Presse', 'Réseaux sociaux', 'Bouche à oreille', 'Radio', 'Télévision']
    moyen_uts_choisi = random.choice(moyens_uts)
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{moyen_uts_choisi}"]'))).click()

    # 8. Quels sont les services qu’offre UTS ?
    services = ['Service courrier', 'Service bagage et marchandises', 'Transport des passagers', 'Location des cars']
    for service in random.sample(services, 2):  # Choisir deux services aléatoires
        wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{service}"]'))).click()

    # 10. Avez-vous déjà voyagé avec la compagnie de transport UTS ?
    deja_voyage_uts = random.choice(['Oui', 'Non'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{deja_voyage_uts}"]'))).click()

    # 11. Si oui, quelle est la fréquence ?
    if deja_voyage_uts == 'Oui':
        frequence_voyage = random.choice(['Rarement', 'Occasionnellement', 'Toujours'])
        wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{frequence_voyage}"]'))).click()

    # 12. Avez-vous l'habitude de voyager avec des bagages à UTS ?
    bagages_uts = random.choice(['Oui', 'Non'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{bagages_uts}"]'))).click()

    # 13. Vos bagages sont-ils bien traités par les convoyeurs ?
    traitement_bagages = random.choice(['Bien traité', 'Mal traité', 'Pas du tout bien traité'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{traitement_bagages}"]'))).click()

    # 14. Avez-vous déjà perdu des bagages ou colis au cours d’un voyage ?
    perdu_bagages = random.choice(['Oui', 'Non'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{perdu_bagages}"]'))).click()

    # 16. Quel est votre moment de voyage préféré ?
    moment_voyage = random.choice(['La journée', 'La nuit', 'À tout moment'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{moment_voyage}"]'))).click()

    # 17. Avez-vous déjà fait une réservation en ligne à UTS ?
    reservation_en_ligne = random.choice(['Oui', 'Non'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{reservation_en_ligne}"]'))).click()

    # 18. Si oui, quel est votre avis sur le service ?
    if reservation_en_ligne == 'Oui':
        avis_reservation = random.choice(['Fiable', 'Pas fiable', 'Pas du tout fiable'])
        wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{avis_reservation}"]'))).click()

    # 19. Que pensez-vous du respect des horaires de départ de UTS ?
    respect_horaires = random.choice(['Respecter', 'Parfois respecter', 'Pas respecter', 'Pas du tout respecter'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{respect_horaires}"]'))).click()

    # 20. Que pensez-vous de la vitesse de conduite des chauffeurs de UTS ?
    vitesse_conduite = random.choice(['Bonne', 'Pas bonne', 'Très bonne'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{vitesse_conduite}"]'))).click()

    # 21. Que pensez-vous de l’hygiène des cars ?
    hygiene_cars = random.choice(['Bonne', 'Pas bonne', 'Très bonne'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{hygiene_cars}"]'))).click()

    # 22. Sur une échelle de 1 à 5 de l’accueil de UTS ?
    accueil_uts = random.randint(1, 5)
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{accueil_uts}"]'))).click()

    # 23. Que pensez-vous de l’emplacement de la gare ?
    accessibilite_gare = random.choice(['Accessible', 'Très Accessible', 'Pas accessible', 'Pas du tout accessible'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{accessibilite_gare}"]'))).click()

    # 24. Que pensez-vous du confort des cars de UTS ?
    confort_cars = random.choice(['Confortable', 'Pas confortable', 'Pas du tout confortable'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{confort_cars}"]'))).click()

    # 25. Que pensez-vous du traitement des colis, marchandises et bagages de UTS ?
    traitement_colis = random.choice(['Bien', 'Très bien', 'Mauvaise', 'Très mauvaise'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{traitement_colis}"]'))).click()

    # 26. Que pensez-vous de l’hygiène des cars de UTS ?
    hygiene_cars = random.choice(['Propre', 'Pas propre', 'Pas du tout propre'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{hygiene_cars}"]'))).click()

    # 27. Que pensez-vous de l’hygiène des gares ?
    hygiene_gares = random.choice(['Propre', 'Pas propre', 'Pas du tout propre'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{hygiene_gares}"]'))).click()

    # 28. Que pensez-vous de la vitesse de chargement et de déchargement ?
    vitesse_chargement = random.choice(['Rapide', 'Pas rapide', 'Très lent'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{vitesse_chargement}"]'))).click()

    # 29. Que pensez-vous de l’attente en gare avant de prendre son bus ?
    attente_gare = random.choice(['Acceptable', 'Pas acceptable', 'Très désagréable'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{attente_gare}"]'))).click()

    # 30. Que pensez-vous des horaires des bus ?
    horaires_buses = random.choice(['Acceptables', 'Pas acceptables', 'Très désagréables'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{horaires_buses}"]'))).click()

    # 31. Que pensez-vous du prix du billet ?
    prix_billet = random.choice(['Abordable', 'Chère', 'Pas du tout abordable'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{prix_billet}"]'))).click()

    # 32. Que pensez-vous de l’application mobile ?
    application_mobile = random.choice(['Facile à utiliser', 'Difficile à utiliser', 'Pas du tout intuitive'])
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{application_mobile}"]'))).click()

    # Soumettre le formulaire
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Soumettre"]'))).click()

try:
    remplir_formulaire()
finally:
    time.sleep(5)  # Attendre quelques secondes pour voir la soumission
    driver.quit()  # Fermer le navigateur
