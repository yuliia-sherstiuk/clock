import time
import threading

# Variables globales
horloge_en_pause = threading.Event()  
horloge_en_pause.set()  
is_12_hour_format = False  
alarme_reglee = False  
heure_alarme = (0, 0, 0)  
horloge_active = True  

# Fonction de changement de format d'heure (12/24 heures)
def basculer_format_affichage():
    global is_12_hour_format
    is_12_hour_format = not is_12_hour_format

# Fonction d'affichage de l'heure actuelle
def afficher_heure(heures, minutes, secondes):
    if is_12_hour_format:
        suffix = "AM " if heures < 12 else "PM "
        heures_affiche = heures % 12 or 12
        print(f"\rl'heure {heures_affiche:02}:{minutes:02}:{secondes:02} {suffix}", end="")
    else:
        print(f"\rl'heure {heures:02}:{minutes:02}:{secondes:02}", end="")

# Fonction de réglage de l'heure
def regler_heure():
    try:
        heures = int(input("\nEntrez les heures (0-23) : "))
        minutes = int(input("Entrez les minutes (0-59) : "))
        secondes = int(input("Entrez les seconds (0-59) : "))
        if not (0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60):
            raise ValueError("ERROR.ERROR")
        return heures, minutes, secondes
    except ValueError as e:
        print(e)
        return regler_heure()
# Fonction de réglage de l'alarme
def regler_alarme():
    global alarme_reglee, heure_alarme
    try:
        heures = int(input("\nEntrez l'heure de l'alarme (0-23) : "))
        minutes = int(input("Entrez les minutes de l'alarme (0-59) : "))
        secondes = int(input("Entrez les secondes de l'alarme (0-59) : "))
        if not (0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60):
            raise ValueError("Error. Error")
        heure_alarme = (heures, minutes, secondes)
        alarme_reglee = True
        print(f"\n l'alarme {heures:02}:{minutes:02}:{secondes:02}")
    except ValueError as e:
        print(e)
        regler_alarme()

# Vérification de l'heure de l'alarme
def verifier_alarme(heures, minutes, secondes):
    global heure_alarme
    if alarme_reglee and (heures, minutes, secondes) == heure_alarme:
        print("\n Alarme ! Il est l'heure !")
        return True
    return False

# Fonction de l'horloge
def horloge(heures, minutes, secondes):
    global horloge_active, horloge_en_pause
    while horloge_active:
        horloge_en_pause.wait()  

       
        afficher_heure(heures, minutes, secondes)

        if verifier_alarme(heures, minutes, secondes):
            print("\nL'alarme s'est déclenchée !")

        time.sleep(1)

        # Heure de mise à jour
        secondes += 1
        if secondes == 60:
            secondes = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            heures += 1
        if heures == 24:
            heures = 0

# Fonction pour travailler avec des commandes
def gerer_interactions():
    global horloge_active
    while horloge_active:
        print("\n Menu : \n (p) - pause/reprendre,\n (s) - stop")
        choix = input(f"\n\033[s\033[1A\033[100DSélectionnez une option:\033[u ").lower()
       
        if choix == "p":  
            if horloge_en_pause.is_set():
                horloge_en_pause.clear()  
                print("\n L'horloge est en pause. ")
            else:
                horloge_en_pause.set()  
                print("\n L'horloge continue de fonctionner.")
        elif choix == 's': 
            horloge_active = False
            horloge_en_pause.set()  
            print("\n L'horloge s'est arrêtée.")
            break

if __name__ == "__main__":
    # Entrer le format de l'heure
    choix_format = input("Voulez-vous utiliser le format 12 heures ou 24 heures ? (12/24) : ")
    if choix_format == "12":
        is_12_hour_format = True

    # Réglage de l'heure
    print("Réglage de l'heure...")
    heures, minutes, secondes = regler_heure()

   # Demande de réglage de l'alarme immédiatement après le réglage de l'heure
    regler_alarme()

    # Exécutez l'horloge dans un thread séparé
    thread_horloge = threading.Thread(target=horloge, args=(heures, minutes, secondes))
    thread_horloge.start()

   # Lancer le menu pour le contrôle dans le thread principal
    gerer_interactions()