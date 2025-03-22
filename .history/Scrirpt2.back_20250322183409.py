#!/usr/bin/env python3
#Introduction  des modules du le programme
import os #Interaction avec le système de fichiers 
import platform #Obtention des données  sur le système d'exploitation
import psutil #Pour écrire des données sur l'utilisation du disque et de la Ram 
import csv #Pour la redaction des fichiers au format cvs
import vmi #Interaction avec windows Management instruction


#Partie 2: programmme pour l'outil de verification de la sauvergade
#Obtention des informations d'un dossier 
def get_folder_info (folder_path):
    total_size = 0
    file_count = 0
    for root, _, files in os.walk(folder_path):  #Parcours les sous-dossiers et fichiers 
        file_count += len(files) #compter les fichiers 
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file)) #calculer la taille totale
    return total_size, file_count

#Verification si la sauvergade est correcte 
def verify_backup():
    while True:
        print("\n--- Vérification de sauvegarde ---") 
        
        #Script pour demander à l'utilisateur d'entrer le chemin du dossier utilisateur 
        while True: 
            user_folder = input("Entrez le chemin du dosssier utilisateur :")
            if os.path.exists(user_folder):
                break
            print("dossier invalide ,veuillez entrer un chemin correct.")
            
        #script pour demander à m'utilisateur d'entrer le chemin du dossier sauvegarde
        while True:
            backup_folder = input("Entrez le chemin du dossier de sauvegarde :")
            if os.path.exists(backup_folder):
                break
            print("Dossier Invalide, veuillez entrer un chemin correct .")
            
        #Script pour comparer les informations des deux dossiers 
        print("Verification en cours....")
        user_size, user_files = get_folder_info(user_folder)
        backup_size, backup_files = get_folder_info(backup_folder)

if user_size == backup_size and user_files == backup_files:
    print("Backup est correct!")
else:
    print("la sauvegarde est incorrecte ! une mise à jour est nécessaire.")
    
    # Demander si l'utilisateur veut vérifier un autre dossier
        $retry = input("Voulez-vous vérifier un autre dossier ? (o/n) : ").strip().lower()
        if retry != "o":
            break
        
#Fonction principale

def main():
    verify_backup()
    
#le point d'entrer du srcipt

if __name__== "__main__":
    main()


        
 
    