import random
import os

def enlever_accents(texte):
    
    # Remplace les lettres avec des accents  par leur équivalent sans accent.
        
    accents = {'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
               'à': 'a', 'â': 'a',
               'î': 'i', 'ï': 'i',
               'ô': 'o',
               'û': 'u', 'ù': 'u',
               'ç': 'c'}
    texte_sans_accent = ""
    for char in texte:
        if char in accents:
            texte_sans_accent += accents[char]
        else:
            texte_sans_accent += char
    return texte_sans_accent

def charger_mots(nom_fichier_defaut="mots_pendu.txt"):
    
    # Demande le fichier à l'utilisateur et charge les mots.
        
    nom_fichier = input(f"Entrez le nom du fichier (Entrée pour utiliser '{nom_fichier_defaut}') : ")
    if nom_fichier == "":
        nom_fichier = nom_fichier_defaut

    # Vérification de l'existence du fichier avec le module os
    if not os.path.exists(nom_fichier):
        print("Le fichier spécifié est introuvable.")
        return []
 
    fichier = open(nom_fichier, "r", encoding="utf-8")
    lignes = fichier.readlines()
    fichier.close()

    # Nettoyage des mots avec une "list comprehension"
    mots_nettoyes = [enlever_accents(mot.strip().lower()) 
                 for mot in lignes 
                 if len(mot.strip()) > 0]