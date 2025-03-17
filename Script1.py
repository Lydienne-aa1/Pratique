#!/usr/bin/env python3
# Importation des modules nécessaires pour le programme
import os  # Pour interagir avec le système de fichiers
import platform  # Pour obtenir des informations sur le système d'exploitation

#PARTIE 1 :  programme pour l'OUTIL D'AUDIT SYSTÈME
# Fonction pour obtenir la version du BIOS
def get_bios_version():
    try:
        if platform.system() == "Windows":  # Si le système est Windows
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
def save_info_to_file(file,data):
    directory = "C:\\PCInfo"  # Dossier où les informations seront enregistrées
    if not os.path.exists(directory):  # Créer le dossier s'il n'existe pas
        os.makedirs(directory)

    file_path = os.path.join(directory, f"{file}.txt")

    # Écriture dans un fichier texte
  
    with open(file_path, "w") as file:
        for key, value in data.items():
            file.write(data)  # Enregistrer chaque information clé : valeur
    print(f"Les informations ont été enregistrées dans {file_path}")

# Fonction pour effectuer un audit du système
def audit_system():
    while True:  # Boucle pour afficher les options
        print("\n--- PC INFO ---")
        print("1. BIOS version")
        print("2. HDD free space")
        print("3. RAM")
        print("4. OS version")
        print("5. Quitter")
        choix = input("Choisissez une option : ")

        # Afficher ou gérer les informations en fonction du choix utilisateur
        if choix == "1":
            print(f"BIOS Version: {get_bios_version()}")
            save_info_to_file("Bios",get_bios_version())
        elif choix == "2":
            print(f"Espace disque libre: {get_disk_space()}")
            save_info_to_file("disque",)
        elif choix == "3":
            print(f"RAM: {get_ram()}",get_disk_space())
            save_info_to_file()
        elif choix == "4":
            print(f"Version OS: {get_os_version()}")
            save_info_to_file("version_os",get_os_version())
        elif choix == "5":
            break
        else:
            print("Option invalide. Veuillez réessayer.")


# programme pour le menu principal
def main():
    audit_system()

# Point d'entrée du programme
if __name__ == "__main__":
    main()