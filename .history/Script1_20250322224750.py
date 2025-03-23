#!/usr/bin/env python3
#Modules nécessaires pour la realisations de notre programme
import os #Module utilisé pour l'interraction avec le système de fichiers
import platform #Module utilisé pour l'obtention des informations sur le système d'exploitation
import wmi#Module utilisé ppour l'interraction avec les informations de système d'exploitation
import psutil#Module utilisé pour l'interraction avec les ressources et processus
import math#Module utilisé pour le travail des calculs

#Partie1: script pour l'outil d'audit système
#la foction utlisée pour avoir la version du bios

def get_bios_version():
    try:
        if platform.system() == "Windows":  # Si le système est Windows
            bios = wmi.WMI().Win32_BIOS()[0]
            return bios.SMBIOSBIOSVersion
        else:  # Pour les systèmes non Windows
            return os.popen("dmidecode -s bios-version").read().strip()  # Commande système Linux pour le BIOS
    except Exception as e:
        return f"Erreur : {e}"  # Gestion des erreurs si la commande échoue
 #LA Fonction utilisé pour obtenir l'espace de disque disponible    
    
def get_disk_space():
    disk_path = "C:\\" 
    freespace=math.ceil(psutil.disk_usage(disk_path).free/(1024**3))
    space=freespace
    
    return space
    
#la  quantité de RAM disponible
def get_ram():
    ram_info = psutil.virtual_memory()
    return f"{ram_info.total//(1024**3)} GO RAM"

#la version de SE
def get_os_version():
    return platform.system()+" "+platform.version()

#eNREGISTRER LES INFO DANS UN DOSSIER PCINFO
def save_info_to_file(file,data):
    directory = "C:\\PCInfo" #le dossier qui va contenir les infos
    if not os.path.exists(directory):#Créer un fichier si il n'exicte pas 
        os.makedirs(directory)
    
    file_path = os.path.join(directory ,f"{file}.txt")
    #Pour ecreire dans un fichier 
    with open(file_path, "w")  as file:
        
        file.write(str(data))#enregistré les infos imortant
    print(f"Les Informations ont été enregistrées dasn {file_path}")

#la fonction utilisé pour l'audit système
def  audit_system():
    while True:#cette boucle est utilisée pour afficher les options
        print("\n---PC INFO ---")
        print("1.Bios version")
        print("2.HDD free space")
        print("3.RAM")
        print("4.OS version")
        print("5.Quitter")
        choix = input("choississez une option : ")
        
        #Affichés les infos selon l'option choisi
        if choix == "1":
           print(f"Bios version: {get_bios_version()}")
           save_info_to_file("Bios",get_bios_version())
        elif choix == "2":
            print(f"Espace disque libre: {get_disk_space()}")
            save_info_to_file("Disk_free",get_disk_space())
        elif choix == "3":
            print(f"RAM:{get_ram()}")
            save_info_to_file("RAM",get_ram())
        elif choix == "4":
            print(f"Version os: {get_os_version()}")
            save_info_to_file("version_os", get_os_version())
        elif choix == "5":
            break
        else:
            print("option invalide. veuillez réessayer.")
        

#affichage du menu principal
def main():
    audit_system()
    
#Point d'entré du programme
if __name__=="__main__":
    main()