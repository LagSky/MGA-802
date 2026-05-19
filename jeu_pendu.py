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
        
    nom_fichier = input(f" Entrez le nom du fichier (Entrée pour utiliser '{nom_fichier_defaut}') : ")
    if nom_fichier == "":
        nom_fichier = nom_fichier_defaut

    # Vérification de l'existence du fichier avec le module os
    if not os.path.exists(nom_fichier):
        print(" Le fichier spécifié est introuvable.")
        return []
 
    fichier = open(nom_fichier, "r", encoding="utf-8")
    lignes = fichier.readlines()
    fichier.close()

    # Nettoyage des mots avec une "list comprehension"
    mots_nettoyes = [enlever_accents(mot.strip().lower()) 
                 for mot in lignes 
                 if len(mot.strip()) > 0]
    return mots_nettoyes
    
def afficher_mot_cache(mot, lettres_devinees):
    
    # On affiche le mot avec des tirets pour les lettres cachées.
    affichage = ""
    for lettre in mot:
        if lettre in lettres_devinees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    return affichage

def jouer_partie(mots):
    
    # On gère la boucle principale d'une partie de pendu.
    mot_secret = random.choice(mots)
    chances = 6
    lettres_devinees = []
    lettres_essayees = []

    print("------------------------------")
    print("NOUVELLE PARTIE DE PENDU")
    print("------------------------------")

    # Boucle while classique pour gérer les chances
    while chances > 0:
        etat_actuel = afficher_mot_cache(mot_secret, lettres_devinees)
        print(f" Mot à deviner : {etat_actuel}")
        print(f" Chances restantes : {chances}")

        # Condition pour gagner la partie
        if "_" not in etat_actuel:
            print(f" Félicitations ! Vous avez gagné. Le mot était : {mot_secret}")
            return

        lettre = input(" Entrez une lettre : ").lower()
        lettre = enlever_accents(lettre)

        if len(lettre) != 1 or lettre not in "abcdefghijklmnopqrstuvwxyz":
            print(" Erreur : Veuillez entrer une seule lettre valide de l'alphabet.")
            continue

        if lettre in lettres_essayees:
            print(" Vous avez déjà essayé cette lettre.")
            continue

        lettres_essayees.append(lettre)

        if lettre in mot_secret:
            print(f"-> Bien joué ! La lettre '{lettre}' fait partie du mot.")
            lettres_devinees.append(lettre)
        else:
            print(f"-> Dommage ! La lettre '{lettre}' n'est pas dans le mot.")
            chances -= 1

    # Si la boucle while se termine, c'est qu'on a utilisé toutes les chances
    print(f" Vous avez perdu ! Le mot à trouver était : {mot_secret}")