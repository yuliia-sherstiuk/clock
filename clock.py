
def afficher_heure(heures, minutes, secondes):
    """
    Affiche l'heure actuelle au format hh:mm:ss
    """
    print(f"{heures:02}:{minutes:02}:{secondes:02}", end="\r"),end="\r" 
# Fonction pour régler l'heure
def regler_heure(heure_tuple):
    
    heures, minutes, secondes = heure_tuple
    if not (0 <= heures < 24):
        raise ValueError("l'heure 0 - 23.")
    if not (0 <= minutes < 60):
        raise ValueError("minutes 0 - 59.")
    if not (0 <= secondes < 60):
        raise ValueError("secundes 0 - 59.")
    return heure_tuple
# Fonction pour régler une alarme
def regler_alarme(alarme_tuple):
    """
    Définit une alarme et vérifie si l'heure actuelle correspond
    """
    return alarme_tuple

# Algorithme principal
def horloge():
    """
    Programme principal qui gère l'heure et l'alarme
    """
    # Initialisation de l'heure et de l'alarme
    heures, minutes, secondes = 0, 0, 0  # Heure initiale
    alarme = None  # Pas d'alarme au départ

    while True:
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