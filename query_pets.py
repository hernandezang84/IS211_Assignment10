import sqlite3

def query_person(person_id):
    cursor.execute('SELECT * FROM person WHERE id = ?', (person_id,))
    return cursor.fetchone()

def query_pets(person_id):
    cursor.execute('SELECT * FROM pet INNER JOIN person_pet ON pet.id = person_pet.pet_id WHERE person_pet.person_id = ?', (person_id,))
    return cursor.fetchall()

conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

while True:
    person_id = int(input("Enter a person's ID number or -1 to exit: "))
    if person_id == -1:
        break

    person = query_person(person_id)
    if person:
        print(f"{person[1]} {person[2]} is {person[3]} years old.")
        pets = query_pets(person_id)
        for pet in pets:
            print(f"{person[1]} {person[2]} owns {pet[1]}, a {pet[2]}, which is {pet[3]} years old.")
    else:
        print("No person found with that ID.")

conn.close()