import m57__m58_sqlite_students_database as db

def menu():
    print("*"* 48)
    print("""
           1. Insert
           2. List
           3. Modify
           4. Delete
           5. Quit
           """)
    print("*"* 48)
    option = int(input())
    return option

while True:
    option = menu()
    if option == 1:
        name = input("Name: ")
        score = input("Score: ")
        data = name, score
        print(type(data))
        db.insert(data)
    if option == 2:
        db.list_table()
    if option == 3:
        db_id = int(input("Student id: "))
        score = int(input("New Score: "))
        db.modify(db_id, score)
    if option == 4:
        db_id = int(input("Student id: "))
        db.delete(db_id)
    if option == 5:
        print("See you soon")
        break
    else:
        print("Choose between the given options \n")
