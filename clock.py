import time


# Fonction pour afficher l'heure
def afficher_heure(heures, minutes, secondes):
    """
    Affiche l'heure actuelle au format 12h ou 24h
    """
    if is_12_hour_format:
        suffix = "AM" if heures < 12 else "PM"
        heures_affiche = heures % 12
        heures_affiche = 12 if heures_affiche == 0 else heures_affiche
        print(f"{heures_affiche:02}:{minutes:02}:{secondes:02} {suffix}", end="\r")
    else:
        print(f"{heures:02}:{minutes:02}:{secondes:02}", end="\r")

# Fonction pour régler l'heure
def regler_heure(heure_tuple):
    """
   Met à jour l'heure actuelle après vérification de la validité
    """
    heures, minutes, secondes = heure_tuple
    if not (0 <= heures < 24):
        raise ValueError("Les heures  0 - 23.")
    if not (0 <= minutes < 60):
        raise ValueError("Les minutes  0 - 59.")
    if not (0 <= secondes < 60):
        raise ValueError("Les secondes  0 - 59.")
    return heure_tuple

# Fonction pour régler une alarme
def regler_alarme(alarme_tuple):
    """
    Définit une alarme et vérifie si l'heure actuelle correspond
    """
    return alarme_tuple

# Fonction pour basculer entre le format 12 heures et 24 heures
def basculer_format_affichage():
    """
    Basculer entre le format 12 heures et 24 heures pour l'affichage
    """
    global is_12_hour_format
    is_12_hour_format = not is_12_hour_format

## Fonction pour mettre en pause ou reprendre l'horloge
def basculer_pause_horloge():
    """
     Met en pause ou reprend la mise à jour de l'heure
    """
    global horloge_en_pause
    horloge_en_pause = not horloge_en_pause

# Fonction principale pour gérer l'horloge
def horloge():
    
    # Initialisation de l'heure et de l'alarme
    heures, minutes, secondes = 0, 0, 0  # Heure initiale
    alarme = None  # Pas d'alarme au départ

    while True:
        if not horloge_en_pause:
            afficher_heure(heures, minutes, secondes)
            time.sleep(1)  # Attente d'une seconde

            # Vérification de l'alarme
            if alarme and (heures, minutes, secondes) == alarme:
                print("\nAlarme ! Il est l'heure !")
                alarme = None  # Réinitialisation de l'alarme après déclenchement

            # Mise à jour de l'heure
            secondes += 1
            if secondes == 60:
                secondes = 0
                minutes += 1
            if minutes == 60:
                minutes = 0
                heures += 1
            if heures == 24:
                heures = 0

         # Exemple d'utilisation
        # Par exemple, basculer entre les formats en appelant basculer_format_affichage()
        # Mettre en pause ou reprendre l'horloge en appelant basculer_pause_horloge()
if __name__ == "__main__":
    horloge()