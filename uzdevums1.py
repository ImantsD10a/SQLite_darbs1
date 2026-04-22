import sqlite3

conn = sqlite3.connect("biblioteka.db")
cursor = conn.cursor()

# Tabulas izveide
cursor.execute("""
CREATE TABLE IF NOT EXISTS gramatas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT,
    autors TEXT,
    gads INTEGER
)
""")

# Ievietojam latviešu grāmatas
cursor.execute("INSERT INTO gramatas (nosaukums, autors, gads) VALUES (?, ?, ?)",
               ("Dvēseļu putenis", "Aleksandrs Grīns", 1935))

cursor.execute("INSERT INTO gramatas (nosaukums, autors, gads) VALUES (?, ?, ?)",
               ("Lāčplēsis", "Andrejs Pumpurs", 1888))

cursor.execute("INSERT INTO gramatas (nosaukums, autors, gads) VALUES (?, ?, ?)",
               ("Cilvēka bērns", "Jānis Klīdzējs", 1956))

conn.commit()

# Izvadām visas grāmatas
print("Visas grāmatas:")
cursor.execute("SELECT * FROM gramatas")
for g in cursor.fetchall():
    print(g)

conn.close()
