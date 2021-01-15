
import sqlite3
import base64
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
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

conn = create_connection('testDB.db')

with conn:
	for i in range(1):
		number = random.randint(1,11)
		sql3 = 'SELECT IMAGE FROM images WHERE ID = '+str(number)
		cur = conn.cursor()
		for row in cur.execute(sql3):
			blob = row
		with open("imageToSaveRandom.png", "wb") as fh:
			fh.write(blob[0])
		img = mpimg.imread('imageToSaveRandom.png')
		imgplot = plt.imshow(img)
		#plt.rcParams["axes.grid"]=False
		#plt.tick_params(axis = 'both', which = 'both', bottom = None, top = None)
		#plt.show()
		img = Image.open('imageToSaveRandom.png')
		img.show() 
		#blob2 = cur.execute(sql3)
		#print(blob2)

