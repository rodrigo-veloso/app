
import pymysql

def create_connection(host, port, database, user, password):
    conn = None
    try:
      conn = pymysql.connect(host=host, port=int(port), database=database, user=user, password=password)
    except Exception as e:
      print("Database connection failed due to {}".format(e))

    return conn

def convertToBinaryData(filename):
    return open(filename, "rb").read()

lista_nomes = []

for number in range(10000):
	num = 100000+number
	nome = str(num)+'.png'
	nome = nome[1:]
	nome = 'figs/'+nome
	lista_nomes.append(nome)

ENDPOINT = "database-1.ctszvlohmh0g.us-east-2.rds.amazonaws.com"
DBNAME = "testedb"
USR = "admin"
PORT = "3306"
REGION="us-east-2a"
PASSWORD = "wS4UV5mqHAkVxMbh"

conn = create_connection(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password=PASSWORD)

with conn:
  for nome in lista_nomes:
    blob = convertToBinaryData(nome)
    cur = conn.cursor()

  i = 1
  for nome in lista_nomes:
    print(i)
    blob = convertToBinaryData(nome)
    sql2 = "INSERT INTO images(ID, IMAGE) VALUES(%s,%s)"
    cur.execute(sql2,(i,blob))
    i+=1
  conn.commit()


