import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta


faker = Faker()

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="etude_vente",
    user="postgres",
    password="root"
)
cur = conn.cursor()

# # Liste des types de clients
# types_clients = ['A', 'B', 'C']

# # Générer et insérer les clients
# clients = []
# for _ in range(100):
#     sexe = random.choice(['M', 'F'])
#     telephone = faker.phone_number()[:20]
#     client = (faker.first_name_male() if sexe == 'M' else faker.first_name_female(),
#               faker.last_name(),
#               telephone,
#               sexe,
#               random.choice(types_clients))
    
#     # Insérer les données dans la table client
#     cur.execute("INSERT INTO client (prenom, nom, telephone, sexe, type_client) VALUES (%s, %s, %s, %s, %s) RETURNING id", client)
    
#     # Récupérer l'ID du client inséré
#     client_id = cur.fetchone()[0]
#     clients.append(client_id)

# vendeurs = []
# for _ in range(5):
#     sexe = random.choice(['M', 'F'])
#     telephone = faker.phone_number()[:20]  # Tronquer à 20 caractères
#     vendeur = (faker.first_name_male() if sexe == 'M' else faker.first_name_female(),
#                faker.last_name(),
#                telephone,
#                sexe)
#     vendeurs.append(vendeur)
#     cur.execute("INSERT INTO vendeur (prenom, nom, telephone, sexe) VALUES (%s, %s, %s, %s)", vendeur)

# Génération des produits (20 produits)
# produits = []
# for _ in range(20):
#     produit = (faker.word(), round(random.uniform(5.0, 500.0), 2))
#     produits.append(produit)
#     cur.execute("INSERT INTO produit (designation, prix_unitaire) VALUES (%s, %s)", produit)
# Générer les commandes (1500 commandes)
for _ in range(1500):
    client_id = random.randint(1, 100)
    vendeur_id = random.randint(1, 5)
    date_commande = faker.date_between(start_date='-2y', end_date='today')

    # Insertion de la commande avec récupération de l'ID
    cur.execute("""
        INSERT INTO commande (client_id, vendeur_id, date_commande)
        VALUES (%s, %s, %s) RETURNING id
    """, (client_id, vendeur_id, date_commande))
    
    # Récupérer l'ID de la commande insérée
    commande_id = cur.fetchone()[0]

    # Générer les produits pour chaque commande
    nb_produits = random.randint(1, 5)
    for _ in range(nb_produits):
        produit_id = random.randint(1, 20)
        quantite = random.randint(1, 10)
        cur.execute("""
            INSERT INTO commande_produit (commande_id, produit_id, quantite)
            VALUES (%s, %s, %s)
            ON CONFLICT (commande_id, produit_id) DO NOTHING
        """, (commande_id, produit_id, quantite))

# Valider la transaction
conn.commit()

# Fermer la connexion
cur.close()
conn.close()
