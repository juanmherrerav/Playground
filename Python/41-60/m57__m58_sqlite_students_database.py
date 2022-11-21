import sqlite3


def connect():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    return connection, cursor


def create_table():
    connection, cursor = connect()
    sql = """
        CREATE TABLE IF NOT EXISTS students(
            id     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name   VARCHAR(25) NOT NULL,
            score  INTEGER NOT NULL
        )
    """
    if(cursor.execute(sql)):
        print("Table created")
    else:
        print("Unable to create Table")
    connection.close()


def insert(data):
    connection, cursor = connect()
    sql = """
         INSERT INTO students (name, score) VALUES(?,?)
    """
    if (cursor.execute(sql, data)):
        print("Saved Data")
    else:
        print("Unable to save data")
    connection.commit()
    connection.close()


def list_table():
    connection, cursor = connect()
    sql = """SELECT id, name, score from students"""
    cursor.execute(sql)
    for fila in cursor:
        print("ID   == ", fila[0])
        print("Name ==", fila[1])
        print("Score==", fila[2], "\n")
    connection.close()


def modify(db_id, score):
    connection, cursor = connect()
    sql = """ UPDATE students SET score = """+str(score)+""" where id = """+str(db_id)
    cursor.execute(sql)
    cursor.close()
    connection.commit()
    connection.close()


def delete(id):
    connection, cursor = connect()
    sql = "DELETE FROM students where id = "+str(id)
    cursor.execute(sql)
    cursor.close()
    connection.commit()
    connection.close()
    print("The record has been deleted")

if __name__ == "__main__":
    #create_table()
    #for i in range(3):
    #    name = input("Name : ")
    #    score = input("Score : ")
    #    row_data = name, score
    #    insert(row_data)
    list_table()
    modify(1,7)
    list_table()
    delete(2)
    list_table()
