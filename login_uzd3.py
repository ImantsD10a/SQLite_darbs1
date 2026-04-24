import sqlite3
import hashlib
from datetime import datetime

conn = sqlite3.connect("lietotaji.db")
cursor = conn.cursor()

# tabula
cursor.execute("""
CREATE TABLE IF NOT EXISTS lietotaji (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lietotajvards TEXT UNIQUE,
    parole TEXT,
    izveidots TEXT
)
""")

def hash_parole(parole):
    return hashlib.sha256(parole.encode()).hexdigest()

# reģistrācija
def registret(lietotajvards, parole):
    try:
        hashed = hash_parole(parole)
        datums = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute(
            "INSERT INTO lietotaji (lietotajvards, parole, izveidots) VALUES (?, ?, ?)",
            (lietotajvards, hashed, datums)
        )
        conn.commit()
        print("Reģistrācija veiksmīga!")
    except:
        print("Lietotājs jau eksistē!")

# pieslēgšanās
def login(lietotajvards, parole):
    hashed = hash_parole(parole)

    cursor.execute(
        "SELECT * FROM lietotaji WHERE lietotajvards = ? AND parole = ?",
        (lietotajvards, hashed)
    )

    if cursor.fetchone():
        print("Pieslēgšanās veiksmīga!")
    else:
        print("Nepareizs lietotājvārds vai parole!")

# lietotāju saraksts
def visi_lietotaji():
    print("\nVisi lietotāji:")
    cursor.execute("SELECT * FROM lietotaji")
    for u in cursor.fetchall():
        print(u)

# tests
registret("janis", "1234")
registret("anna", "abcd")

login("janis", "1234")
login("janis", "nepareiza")

visi_lietotaji()

conn.close()
