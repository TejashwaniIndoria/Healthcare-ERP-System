import sqlite3
import os


DATABASE_PATH = os.path.join(
    os.path.dirname(__file__),
    "hospital.db"
)


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


with open("database/tables.sql", "r") as file:

    sql = file.read()

    cursor.executescript(sql)


connection.commit()

connection.close()


print("Database initialized successfully")