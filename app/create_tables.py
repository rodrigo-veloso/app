
import pymysql

def create_connection(host, port, database, user, password):
    conn = None
    try:
      conn = pymysql.connect(host=host, port=int(port), database=database, user=user, password=password)
    except Exception as e:
      print("Database connection failed due to {}".format(e))

    return conn

def create_tables():

  ENDPOINT = "database-1.ctszvlohmh0g.us-east-2.rds.amazonaws.com"
  DBNAME = "testedb"
  USR = "admin"
  PORT = "3306"
  REGION="us-east-2a"
  PASSWORD = "wS4UV5mqHAkVxMbh"

  conn = create_connection(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password=PASSWORD)

  with conn:
    sql = 'DROP TABLE labels;'
    cur = conn.cursor()
    cur.execute(sql)
    sql = 'DROP TABLE users;'
    cur.execute(sql)
    sql = 'DROP TABLE images;'
    cur.execute(sql)
    sql = 'CREATE TABLE users(USERNAME VARCHAR(20) PRIMARY KEY, GENDER INTEGER, COLOR INTEGER, AGE INTEGER);'
    cur.execute(sql)
    sql = 'CREATE TABLE images(ID INTEGER PRIMARY KEY AUTO_INCREMENT, IMAGE BLOB);'    
    cur.execute(sql)
    sql = 'CREATE TABLE labels(ANSWER_ID INTEGER PRIMARY KEY AUTO_INCREMENT, GRADE FLOAT, GENDER INTEGER, COLOR INTEGER, AGE INTEGER, HAIR INTEGER, SMILE INTEGER, EXTRA INTEGER, ID INTEGER, USERNAME VARCHAR(20), FOREIGN KEY (ID) REFERENCES images(ID), FOREIGN KEY (USERNAME) REFERENCES users(USERNAME));'
    cur.execute(sql)

create_tables()
