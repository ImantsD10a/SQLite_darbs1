import sqlite3

conn = sqlite3.connect("biblioteka.db")
cursor = conn.cursor()

# vēl 2 grāmatas
cursor.execute("INSERT INTO gramatas (nosaukums, autors, gads) VALUES (?, ?, ?)",
               ("Zvejnieka dēls", "Vilis Lācis", 1933))

cursor.execute("INSERT INTO gramatas (nosaukums, autors, gads) VALUES (?, ?, ?)",
               ("Uz jauno krastu", "Vilis Lācis", 1945))

conn.commit()

# konkrēta autora grāmatas
print("\nVilis Lācis grāmatas:")
cursor.execute("SELECT * FROM gramatas WHERE autors = ?", ("Vilis Lācis",))
for g in cursor.fetchall():
    print(g)

# grāmatas pēc 2000. gada
print("\nGrāmatas pēc 2000. gada:")
cursor.execute("SELECT * FROM gramatas WHERE gads > 2000")
for g in cursor.fetchall():
    print(g)

# kārtošana pēc gada
print("\nGrāmatas sakārtotas pēc gada:")
cursor.execute("SELECT * FROM gramatas ORDER BY gads")
for g in cursor.fetchall():
    print(g)

conn.close()
