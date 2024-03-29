import sqlite3

conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

persons = [(1, 'James', 'Smith', 41), (2, 'Diana', 'Greene', 23), ...]
pets = [(1, 'Rusty', 'Dalmation', 4, 1), (2, 'Bella', 'Alaskan Malamute', 3, 0), ...]
person_pets = [(1, 1), (1,2), ...]

for person in persons:
    cursor.execute('INSERT INTO person VALUES (?, ?, ?, ?)', person)

for pet in pets:
    cursor.execute('INSERT INTO pet VALUES (?, ?, ?, ?, ?)', pet)

for person_pet in person_pets:
    cursor.execute('INSERT INTO person_pet VALUES (?, ?)', person_pet)

conn.commit()
conn.close()