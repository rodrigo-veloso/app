
import pymysql

import pymysql

def create_connection(host, port, database, user, password):
    conn = None
    try:
      conn = pymysql.connect(host=host, port=int(port), database=database, user=user, password=password)
    except Exception as e:
      print("Database connection failed due to {}".format(e))

    return conn

ENDPOINT = "database-1.ctszvlohmh0g.us-east-2.rds.amazonaws.com"
DBNAME = "testedb"
USR = "admin"
PORT = "3306"
REGION="us-east-2a"
PASSWORD = "wS4UV5mqHAkVxMbh"

conn = create_connection(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password=PASSWORD)

with conn:
  #sql = 'CREATE TABLE labels(ANSWER_ID INTEGER PRIMARY KEY AUTO_INCREMENT, GRADE FLOAT, GENDER INTEGER, AGE INTEGER, HAIR INTEGER, SMILE INTEGER, ID INTEGER, FOREIGN KEY (ID) REFERENCES images(ID));'
  cur = conn.cursor()
  sql = 'SELECT * FROM labels;'
  cur.execute(sql)
  print(cur.fetchall())
