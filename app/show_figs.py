
import pymysql
import base64
import random

def create_connection(host, port, database, user, password):
    conn = None
    try:
      conn = pymysql.connect(host=host, port=int(port), database=database, user=user, password=password)
    except Exception as e:
      print("Database connection failed due to {}".format(e))

    return conn

def convertToBinaryData(filename):
    #Convert digital data to binary format
    #with open(filename, 'r') as file:
    #    blobData = file.read().decode("base64")
    return open(filename, "rb").read()

def get_fig():

  ENDPOINT = "database-1.ctszvlohmh0g.us-east-2.rds.amazonaws.com"
  DBNAME = "testedb"
  USR = "admin"
  PORT = "3306"
  REGION="us-east-2a"
  PASSWORD = "wS4UV5mqHAkVxMbh"

  conn = create_connection(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password=PASSWORD)

  with conn:
    number = random.randint(1,10000)
    sql3 = 'SELECT * FROM images WHERE ID = '+str(number)
    cur = conn.cursor()
    cur.execute(sql3)
    query = cur.fetchone()
    image_id = query[0]
    blob = query[1]
    with open("app/image.png", "wb") as fh:
      fh.write(blob)
    return image_id, "app/image.png"

get_fig()
