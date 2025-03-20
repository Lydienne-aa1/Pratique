#!/usr/bin/env python3
# Importation des modules nécessaires pour le programme
import os  # Pour interagir avec le système de fichiers
import platform  # Pour obtenir des informations sur le système d'exploitation
import psutil  # Pour des informations sur l'utilisation du disque et de la RAM
import csv  # Pour écrire des fichiers au format CSV
import wmi 


#PARTIE 2 : programme pour l'outil de verification de la sauvegarde 
# Fonction pour obtenir les informations d'un dossier  
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
            print("La sauvegarde est incorrecte ! Une mise à jour est nécessaire.")

        # Demander si l'utilisateur veut vérifier un autre dossier
        retry = input("Voulez-vous vérifier un autre dossier ? (O/N) : ").strip().lower()
        if retry != "o":
            break



def main():
    verify_backup()
    
if __name__=="__main__":
    main()