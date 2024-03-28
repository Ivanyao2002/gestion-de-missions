# database.py
import mysql.connector


def create_connection():
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='gestion_missions'
        )
        return db
    except mysql.connector.Error as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return None


def create_mission_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Mission(
                libele TEXT,
                description TEXT,
                duree INT
            )
            """
        )
        connection.commit()
    except mysql.connector.Error as e:
        print(f"Erreur lors de la création de la table : {e}")


def insert_mission(connection, libele, description, duree):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO Mission (libele, description, duree) VALUES (%s, %s, %s)"
        values = (libele, description, duree)
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as e:
        print(f"Erreur lors de l'insertion de la mission : {e}")


# Exemple d'utilisation
db_connection = create_connection()
if db_connection:
    create_mission_table(db_connection)
    db_connection.close()
