import subprocess

def export_database(db_name, db_user, output_file):
    try:
        # Commande pg_dump pour exporter la base de données
        subprocess.run([
            'pg_dump', 
            '-U', db_user,   # utilisateur PostgreSQL
            '-d', db_name,   # nom de la base de données
            '-f', output_file  # chemin de destination du fichier .sql
        ], check=True)
        
        print(f"La base de données {db_name} a été exportée avec succès vers {output_file}")
    
    except subprocess.CalledProcessError as e:
        print(f"Une erreur est survenue lors de l'exportation : {e}")

# Exécution du script avec les paramètres nécessaires
db_name = "etude_vente"  # Nom de la base de données
db_user = "postgres"     # Utilisateur PostgreSQL
output_file = "/home/thiara/Bureau/DEV DATA Sonatel Academy/postgres/Entreprise.sql"

export_database(db_name, db_user, output_file)
