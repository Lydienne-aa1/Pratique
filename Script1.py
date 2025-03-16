#!/usr/bin/env python3
# Importation des modules nécessaires pour le programme
import os  # Pour interagir avec le système de fichiers
import platform  # Pour obtenir des informations sur le système d'exploitation
import psutil  # Pour des informations sur l'utilisation du disque et de la RAM
import csv  # Pour écrire des fichiers au format CSV

# --- PARTIE 1 : OUTIL D'AUDIT SYSTÈME ---
# Fonction pour obtenir la version du BIOS
def get_bios_version():
    try:
        if platform.system() == "Windows":  # Si le système est Windows
            import wmi  # Librairie spécifique à Windows pour accéder aux informations matérielles
            bios = wmi.WMI().Win32_BIOS()[0]
            return bios.SMBIOSBIOSVersion
        else:  # Pour les systèmes non Windows
            return os.popen("dmidecode -s bios-version").read().strip()  # Commande système Linux pour le BIOS
    except Exception as e:
        return f"Erreur : {e}"  # Gestion des erreurs si la commande échoue

# Fonction pour obtenir l'espace disque disponible
def get_disk_space():
    disk_info = psutil.disk_usage('/')  # Obtenir l'espace disque
    return f"{disk_info.free // (1024**3)} Go libres"  # Convertir l'espace disponible en Go

# Fonction pour obtenir la quantité de RAM
def get_ram():
    ram_info = psutil.virtual_memory()
    return f"{ram_info.total // (1024**3)} Go RAM"  # Convertir la RAM totale en Go

# Fonction pour obtenir la version du système d'exploitation
def get_os_version():
    return platform.system() + " " + platform.version()  # Retourne le nom et la version du système d'exploitation

# Fonction pour enregistrer les informations système dans un fichier
def save_info_to_file(data, file_type):
    directory = "C:\\PCInfo"  # Dossier où les informations seront enregistrées
    if not os.path.exists(directory):  # Créer le dossier s'il n'existe pas
        os.makedirs(directory)

    file_path = os.path.join(directory, f"system_info.{file_type}")

    # Écriture dans un fichier texte
    if file_type == "txt":
        with open(file_path, "w") as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")  # Enregistrer chaque information clé : valeur

    # Écriture dans un fichier CSV
    elif file_type == "csv":
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Information", "Valeur"])  # En-tête des colonnes
            for key, value in data.items():
                writer.writerow([key, value])  # Enregistrer chaque information sous forme de ligne
    print(f"Les informations ont été enregistrées dans {file_path}")

# Fonction pour effectuer un audit du système
def audit_system():
    while True:  # Boucle pour afficher les options
        print("\n--- PC INFO ---")
        print("1. BIOS version")
        print("2. HDD free space")
        print("3. RAM")
        print("4. OS version")
        print("5. Enregistrer les infos")
        print("6. Quitter")
        choix = input("Choisissez une option : ")

        # Collecte des données système
        system_data = {
            "BIOS Version": get_bios_version(),
            "HDD Free Space": get_disk_space(),
            "RAM": get_ram(),
            "OS Version": get_os_version()
        }

        # Afficher ou gérer les informations en fonction du choix utilisateur
        if choix == "1":
            print(f"BIOS Version: {system_data['BIOS Version']}")
        elif choix == "2":
            print(f"Espace disque libre: {system_data['HDD Free Space']}")
        elif choix == "3":
            print(f"RAM: {system_data['RAM']}")
        elif choix == "4":
            print(f"Version OS: {system_data['OS Version']}")
        elif choix == "5":
            file_type = input("Choisissez le format (txt/csv) : ").lower()
            if file_type in ["txt", "csv"]:
                save_info_to_file(system_data, file_type)
            else:
                print("Format invalide.")
        elif choix == "6":
            break  # Quitter la boucle et terminer l'outil
        else:
            print("Option invalide. Veuillez réessayer.")

# --- PARTIE 2 : OUTIL DE VÉRIFICATION DE SAUVEGARDE ---
# Fonction pour obtenir les informations d'un dossier (taille totale et nombre de fichiers)
def get_folder_info(folder_path):
    total_size = 0
    file_count = 0
    for root, _, files in os.walk(folder_path):  # Parcourir les sous-dossiers et fichiers
        file_count += len(files)  # Compter les fichiers
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))  # Calculer la taille totale
    return total_size, file_count

# Fonction pour vérifier si une sauvegarde est correcte
def verify_backup():
    while True:
        print("\n--- Vérification de Sauvegarde ---")
        # Demander le chemin du dossier utilisateur
        while True:
            user_folder = input("Entrez le chemin du dossier utilisateur : ")
            if os.path.exists(user_folder):
                break
            print("Dossier invalide, veuillez entrer un chemin correct.")

        # Demander le chemin du dossier de sauvegarde
        while True:
            backup_folder = input("Entrez le chemin du dossier de sauvegarde : ")
            if os.path.exists(backup_folder):
                break
            print("Dossier invalide, veuillez entrer un chemin correct.")

        # Comparaison des informations entre les deux dossiers
        print("Vérification en cours...")
        user_size, user_files = get_folder_info(user_folder)
        backup_size, backup_files = get_folder_info(backup_folder)

        if user_size == backup_size and user_files == backup_files:
            print("BackUp est correct!")
        else:
            print(" La sauvegarde est incorrecte ! Une mise à jour est nécessaire.")

        # Demander si l'utilisateur veut vérifier un autre dossier
        retry = input("Voulez-vous vérifier un autre dossier ? (O/N) : ").strip().lower()
        if retry != "o":
            break

# --- MENU PRINCIPAL ---
def main():
    while True:  # Afficher le menu principal
        print("\n--- MENU PRINCIPAL ---")
        print("1. Outil d'audit système")
        print("2. Vérification de sauvegarde")
        print("3. Quitter")
        choix = input("Choisissez une option : ")

        # Appeler les fonctions selon le choix
        if choix == "1":
            audit_system()
        elif choix == "2":
            verify_backup()
        elif choix == "3":
            print("Programme terminé.")
            break
        else:
            print("Option invalide, veuillez réessayer.")

# Point d'entrée du programme
if __name__ == "__main__":
    main()
