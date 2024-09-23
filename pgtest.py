import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(
        user='postgres',  # Remplacez par votre utilisateur
        password='your_password',  # Remplacez par votre mot de passe
        database='Entreprise',  # Remplacez par le nom de votre base de données
        host='localhost'
    )

    # Exemple : récupérer des vendeurs
    rows = await conn.fetch('SELECT * FROM Vendeurs')
    for row in rows:
        print(row)

    await conn.close()

# Exécutez la fonction principale
asyncio.run(main())
