
import sqlite3
import base64
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def convertToBinaryData(filename):
    #Convert digital data to binary format
    #with open(filename, 'r') as file:
    #    blobData = file.read().decode("base64")
    return open(filename, "rb").read()

lista_nomes = []

for number in range(11):
	num = 100000+number
	nome = str(num)+'.png'
	nome = nome[1:]
	nome = 'figs/'+nome
	lista_nomes.append(nome)

i=0
for nome in lista_nomes:
	blob = convertToBinaryData(nome)
	with open("imageToSave"+str(i)+".png", "wb") as fh:
		fh.write(blob)
	i+=1

conn = create_connection('testDB.db')

with conn:
	#criando tabela de imagens
	sql = 'CREATE TABLE images(ID INTEGER PRIMARY KEY AUTOINCREMENT, IMAGE BLOB NOT NULL);'
	cur = conn.cursor()
	cur.execute(sql)
	#inserção das imagens na tabela no formato blob
	i = 1
	for nome in lista_nomes:
		blob = convertToBinaryData(nome)
		sql2 = 'INSERT INTO images(ID,IMAGE) VALUES(?,?)'
		parameters = (i,blob)
		cur = conn.cursor()
		cur.execute(sql2,parameters)
		i+=1
#	for i in range(11):
#		number = random.randint(1,11)
#		sql3 = 'SELECT ID FROM images WHERE ID = '+str(number)
#		cur = conn.cursor()
#		blob2 = cur.execute(sql3)
#		print(blob2)

