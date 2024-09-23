
# Etude des Ventes d'une Entreprise

Ce projet simule un système de gestion des ventes pour une entreprise possédant plusieurs magasins dans différentes villes. Il utilise **PostgreSQL** pour la gestion de la base de données et **Faker** pour générer des données factices. Le projet comprend également des scripts pour exporter la base de données dans un fichier `.sql`.

## Table des matières
- [Structure de la base de données](#structure-de-la-base-de-données)
- [Technologies utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Exporter la base de données](#exporter-la-base-de-données)
- [Auteur](#auteur)

## Structure de la base de données

La base de données est composée des tables suivantes :

1. **vendeur** : Prénom, nom, téléphone, sexe
2. **produit** : Désignation, prix unitaire
3. **client** : Prénom, nom, téléphone, sexe, type (A, B, C)
4. **commande** : Référence au client, vendeur, date
5. **commande_produit** : Table de liaison entre commande et produit avec la quantité

## Technologies utilisées

- **Python** : Pour automatiser la génération de données et les interactions avec la base de données.
- **PostgreSQL** : Système de gestion de base de données relationnel.
- **Faker** : Bibliothèque Python pour générer des données factices.
- **psycopg2** : Bibliothèque Python pour interagir avec PostgreSQL.

## Installation

### Prérequis

- Python 3.x
- PostgreSQL
- Virtualenv (optionnel mais recommandé)

### Étapes

1. Clonez ce dépôt GitHub :

2. Créez un environnement virtuel et activez-le :

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sur Windows, utilisez .venv\Scripts\activate
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Créez la base de données PostgreSQL :

   ```bash
   sudo -u postgres psql
   CREATE DATABASE etude_vente;
   ```

5. Exécutez le script pour générer les données :

   ```bash
   python test.py
   ```

## Utilisation

Vous pouvez exécuter les scripts suivants :

- `test.py` : Génère des données aléatoires pour les tables `vendeur`, `produit`, `client`, et `commande`.
- `export.py` : Exporte la base de données PostgreSQL dans un fichier `.sql`.

### Exemple

```bash
python test.py  # Pour générer les données
python export.py  # Pour exporter la base de données dans un fichier .sql
```

## Exporter la base de données

Pour exporter la base de données dans un fichier `.sql`, exécutez simplement :

```bash
python export.py
```

Le fichier `.sql` sera généré dans le répertoire spécifié.
