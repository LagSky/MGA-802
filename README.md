<h1 align="center"> Jeu du Pendu</h1>
<p <p align="center">
<small>
<em>Mini-Projet en MGA-802</em><br>
<em>Auteur : Vincent Condette </em> <br>
<em>vincent.condette.1@ens.etsmtl.ca</em>
</small>
</p>

---

## Table des matières

- [Aperçu du projet](#aperçu-du-projet)
- [Fonctionnalités](#fonctionnalités)
- [Instructions d'exécution](#instructions-dexécution)
- [Flux d'exécution](#flux-dexécution)

---

## Aperçu du projet

Il s'agit d'un programme Python du célèbre **Jeu du Pendu**, réalisé dans le cadre du cours MGA802 à l'ÉTS. Le joueur dispose de **6 chances** pour deviner un mot caché, choisi aléatoirement depuis un fichier dictionnaire. Le jeu se joue entièrement dans le terminal.

---

## Fonctionnalités

- **Gestion automatique des accents** lors de la lecture du fichier et de la saisie utilisateur (é, à...).
- **Gestion des erreurs de saisie** : caractères multiples, chiffres, symboles et lettres déjà essayées.
- **Relancer des parties** : le joueur peut rejouer autant de fois qu'il le souhaite sans relancer le programme.
- **Indice** : lorsqu'il ne reste qu'une seule chance, le jeu révèle la tranche alphabétique (ex. : *de A à E*) d'une lettre manquante choisie aléatoirement.
- **Dictionnaire modifiable** : le joueur peut choisir son propre fichier `.txt` de mots au lancement.

---

## Instructions d'exécution

### Prérequis

- Python 3.x installé sur votre machine.
- Un fichier `mots_pendu.txt` contenant un mot par ligne, placé dans le même répertoire que le script.

### Lancement

Ouvrez un terminal dans le dossier du projet et exécutez :

```bash
python jeu_pendu.py
```



---

## Flux d'exécution

Le projet est structuré autour de cinq fonctions indépendantes, appelées par une fonction principale `main()`.

```
main()
    │
    ├─► charger_mots()
    │     ├─► Demande le nom du fichier à l'utilisateur
    │     ├─► Vérifie l'existence du fichier
    │     ├─► enlever_accents()  ← appliquée à chaque mot
    │     └─► Retourne la liste de mots nettoyés ou une erreur
    │
    ├─► jouer_partie()
    │       ├─► Choisit un mot aléatoire
    │       │
    │       ├─► [boucle principale : while chances > 0]
    │       │     ├─► afficher_mot_cache()  ← à chaque tour
    │       │     ├─► enlever_accents()     ← sur la saisie joueur
    │       │     ├─► Vérifie la saisie (longueur, alphabet, doublon)
    │       │     ├─► Lettre correcte → ajout à lettres_devinees
    │       │     └─► Lettre fausse   → chances -= 1
    │       │
    │       ├─► [si chances == 1] → indice()
    │       │
    │       └─► Victoire (_ absent) ou Défaite (chances == 0)
    │
    └─► rejouer ? (o/n)