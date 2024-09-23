

-- Création des tables
CREATE TABLE vendeur (
    id SERIAL PRIMARY KEY,
    prenom VARCHAR(50),
    nom VARCHAR(50),
    telephone VARCHAR(20),
    sexe CHAR(1)
);

CREATE TABLE produit (
    id SERIAL PRIMARY KEY,
    designation VARCHAR(100),
    prix_unitaire DECIMAL(10, 2)
);

CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    prenom VARCHAR(50),
    nom VARCHAR(50),
    telephone VARCHAR(20),
    sexe CHAR(1),
    type_client CHAR(1) -- Type de client : lettre ou chiffre
);

CREATE TABLE commande (
    id SERIAL PRIMARY KEY,
    client_id INT REFERENCES client(id),
    vendeur_id INT REFERENCES vendeur(id),
    date_commande DATE
);

CREATE TABLE commande_produit (
    commande_id INT REFERENCES commande(id),
    produit_id INT REFERENCES produit(id),
    quantite INT,
    PRIMARY KEY (commande_id, produit_id)
);



SELECT * FROM commande;
SELECT * FROM produit;

SELECT * FROM commande_produit;
DROP TABLE commande;
DROP TABLE commande_produit;

