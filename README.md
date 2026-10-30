# Analyse des journaux d'un pare-feu

## Présentation du projet

Ce projet consiste à analyser les journaux d'un pare-feu à l'aide de Python afin d'identifier les activités inhabituelles sur un réseau informatique.

L'objectif est de nettoyer les données, de calculer des indicateurs de sécurité et de produire des graphiques permettant de mieux comprendre le trafic réseau.

## Technologies utilisées

- Python 3
- Pandas : nettoyage et analyse des données.
- Matplotlib : création des graphiques.
- JSON : enregistrement des résultats.

## Structure du projet

```text
projet-analyse-CISSE-Maguette/
├── data/
│   └── logs_reseau.csv
├── figures/
│   ├── top_ports.png
│   ├── repartition_actions.png
│   └── volume_appareils.png
├── analyse.py
├── resultats.json
├── rapport.md
├── README.md
└── requirements.txt
```

## Fonctionnalités

- Suppression des doublons.
- Normalisation des protocoles.
- Remplacement des valeurs manquantes.
- Identification du port le plus utilisé.
- Calcul du taux de connexions refusées.
- Identification des adresses IP présentant des comportements suspects.
- Génération de trois graphiques.
- Enregistrement des résultats dans un fichier JSON.

## Installation

Installer les dépendances avec la commande :

```bash
pip install -r requirements.txt
```

## Exécution

Depuis le dossier principal du projet, exécuter :

```bash
python analyse.py
```

Les résultats sont enregistrés dans `resultats.json` et les graphiques dans le dossier `figures/`.

## Résultats principaux

- Nombre de lignes après nettoyage : 5440
- Port le plus utilisé : 443
- Taux de connexions refusées : 13.57 %
- Adresse IP présentant une activité de scan : 192.168.1.99
- Adresse IP présentant le plus grand volume envoyé : 192.168.1.11

Trois graphiques sont générés pour faciliter l'interprétation du trafic réseau.


## Auteur

Maguette CISSE

Projet réalisé dans le cadre d'un travail pratique en Python, Réseaux et Sécurité.