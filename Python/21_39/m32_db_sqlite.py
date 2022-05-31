""" Sqlite basic example """

import sqlite3
import sys


def connect():
    """ Connect to database """
    conn = sqlite3.connect('m32_db.sqlite.db')
    cur = conn.cursor()
    return conn, cur


def create_table_agenda():
    """ Create table """
    connection, cursor = connect()
    create_agenda_table = """
        CREATE TABLE IF NOT EXISTS agenda ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(50) NOT NULL,
            phone VARCHAR(14)
        );
    """
    success = cursor.execute(create_agenda_table)
    if success:
        print("Table created")
    else:
        print("Table not created")
    connection.commit()
    connection.close()


def insert(datos):
    connection, cursor = connect()
    insert_agenda = """
        INSERT INTO agenda (nombre, phone) VALUES (?, ?);
    """
    params = (datos[0],datos[1],)
    success = cursor.execute(insert_agenda, params)
    if success:
        print("Inserted")
    else:
        print("Not inserted")
    connection.commit()
    connection.close()


def display_table():
    connection, cursor = connect()
    select_query = """
        SELECT id, nombre, phone FROM agenda;
    """
    success = cursor.execute(select_query)
    if success:
        for row in success:
            print(f"ID is { str(row[0]).rjust(3, ' ')}  Name : {str(row[1]).rjust(50, ' ')}  Phone : {str(row[2]).rjust(10, ' ')} ")

def update(datos):
    connection, cursor = connect()
    update_query = """
        UPDATE agenda set phone = ? WHERE id = ?;
    """
    success = cursor.execute(update_query,datos)
    if success:
        print("Updated")
    else:
        print("Not Updated")
    connection.commit()
    connection.close()

def delete(id):
    connection, cursor = connect()
    update_query = """
        DELETE FROM agenda WHERE id = ?;
    """
    success = cursor.execute(update_query,id)
    if success:
        print("deleted")
    else:
        print("Not deleted")
    connection.commit()
    connection.close()

def bulk_insert():
    insert(("Jose", "569877456"))
    insert(("Katelynn Medhurst", "269090545"))
    insert(("Michale Sporer", "157169088"))
    insert(("Leatha Stiedemann", "165325923"))
    insert(("Karlee Stamm", "277445121"))
    insert(("Henri Mueller", "734105331"))
    insert(("Luna Hoppe", "403425308"))
    insert(("Humberto Gulgowski", "989098393"))
    insert(("Sim Bednar", "277304165"))
    insert(("Vincenzo Goldner", "324489027"))
    insert(("Gerald Kreiger", "282070171"))
    insert(("Pauline Schulist", "326459285"))
    insert(("June Kshlerin", "142468683"))
    insert(("Kenyon Huel", "662324827"))
    insert(("Tianna Smith", "578622929"))
    insert(("Antonetta Hauck", "448711920"))
    insert(("Ashlee O'Connell", "507371731"))
    insert(("Aiyana Hills", "797287421"))
    insert(("Riley Will", "797345417"))
    insert(("Orland Connelly", "768885092"))
    insert(("Sarah Strosin", "132784720"))
    insert(("Wilford Krajcik", "376836842"))
    insert(("Pinkie Schmidt", "206371290"))
    insert(("Jairo Lebsack", "385647423"))
    insert(("Maria", "569877456"))
    insert(("Elenea", "569877456"))

def process():
    print(sys.version)
    print(type(sys.version))
    print("Processing SQLITE Code. ..")
    create_table_agenda()
    print("*"*50)
    print("Insertar datos")
    #bulk_insert()
    update(("0000001",52))
    delete((51,))
    display_table()

process()
