import time

# Variables globales
horloge_en_pause = False  # La pause est désactivée par défaut
is_12_hour_format = False  # Le format par défaut est 24 heures

# Fonction pour régler l'heure
def regler_heure():
    """
    Permet à l'utilisateur de régler l'heure manuellement.
    """
    try:
        heures = int(input("Entrez les heures (0-23) : "))
        minutes = int(input("Entrez les minutes (0-59) : "))
        secondes = int(input("Entrez les secondes (0-59) : "))
        if not (0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60):
            raise ValueError("Valeurs invalides pour l'heure.")
        return heures, minutes, secondes
    except ValueError as e:
        print(e)
        return regler_heure()  # Si les valeurs sont incorrectes, on redemande l'heure

# Fonction pour afficher l'heure
def afficher_heure(heures, minutes, secondes):
    """
    Affiche l'heure actuelle selon le format choisi (12h ou 24h).
    """
    if is_12_hour_format:
        # Si c'est le format 12h, on ajoute AM/PM
        suffix = "AM" if heures < 12 else "PM"
        heures_affiche = heures % 12  # Conversion pour 12h
        heures_affiche = 12 if heures_affiche == 0 else heures_affiche  # Correction pour l'heure 0
        print(f"{heures_affiche:02}:{minutes:02}:{secondes:02} {suffix}", end="\r")
    else:
        # Si c'est le format 24h, on affiche l'heure directement
        print(f"{heures:02}:{minutes:02}:{secondes:02}", end="\r")

# Fonction pour basculer entre le format 12h et 24h
def basculer_format_affichage():
    """
    Permet de basculer entre le format 12 heures et 24 heures pour l'affichage de l'heure.
    """
    global is_12_hour_format
    is_12_hour_format = not is_12_hour_format  # Change le format d'affichage

# Fonction pour mettre en pause ou reprendre l'horloge
def basculer_pause_horloge():
    """
    Met en pause ou reprend l'affichage de l'heure.
    """
    global horloge_en_pause
    horloge_en_pause = not horloge_en_pause  # Change l'état de la pause

# Fonction principale pour gérer l'horloge
def horloge(heures, minutes, secondes):
    """
    Fonction principale pour afficher et mettre à jour l'heure.
    """
    global horloge_en_pause
    while True:
        if not horloge_en_pause:  # Si l'horloge n'est pas en pause
            afficher_heure(heures, minutes, secondes)  # Affiche l'heure actuelle
            time.sleep(1)  # Attend 1 seconde avant de mettre à jour

            # Mise à jour de l'heure
            secondes += 1
            if secondes == 60:
                secondes = 0
                minutes += 1
            if minutes == 60:
                minutes = 0
                heures += 1
            if heures == 24:
                heures = 0  # Si on atteint 24 heures, on recommence à 0

if __name__ == "__main__":
    # Demander à l'utilisateur s'il veut le format 12h ou 24h
    choix_format = input("Voulez-vous utiliser le format 12 heures ou 24 heures ? (12/24) : ")
    if choix_format == "12":
        is_12_hour_format = True  # Si l'utilisateur choisit le format 12 heures

    # Demander à l'utilisateur de régler l'heure
    print("Réglage de l'heure...")
    heures, minutes, secondes = regler_heure()  # Appeler la fonction pour régler l'heure

    # Lancer l'horloge avec l'heure définie par l'utilisateur
    horloge(heures, minutes, secondes)