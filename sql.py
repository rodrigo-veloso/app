
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

conn = create_connection('testDB.db')
grade = input('Qual a nota?')
typee = 1
with conn:
	sql = 'CREATE TABLE nome5(ID INTEGER PRIMARY KEY AUTOINCREMENT, GRADE REAL, TYPE INTEGER);'
	cur = conn.cursor()
	#cur.execute(sql)
	sql2 = 'INSERT INTO nome5(GRADE,TYPE) VALUES(?,?)'
	parameters = (grade,typee)
	cur = conn.cursor()
	cur.execute(sql2,parameters)

