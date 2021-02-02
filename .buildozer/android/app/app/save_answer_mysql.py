
import pymysql

def create_connection(host, port, database, user, password):
    conn = None
    try:
      conn = pymysql.connect(host=host, port=int(port), database=database, user=user, password=password)
    except Exception as e:
      print("Database connection failed due to {}".format(e))

    return conn

def save_answer(answer,table_name):

  ENDPOINT = "database-1.ctszvlohmh0g.us-east-2.rds.amazonaws.com"
  DBNAME = "testedb"
  USR = "admin"
  PORT = "3306"
  REGION="us-east-2a"
  PASSWORD = "wS4UV5mqHAkVxMbh"

  conn = create_connection(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password=PASSWORD)

  with conn:
    cur = conn.cursor()
    values = []
    for key in answer.items():
      values.append(key[1])
    values = tuple(values)
    if table_name == 'labels':
      sql2 = "INSERT INTO labels(GRADE, GENDER, COLOR, AGE, HAIR, SMILE, EXTRA, ID, USERNAME) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    else:
      sql2 = "INSERT INTO users(USERNAME, GENDER, COLOR, AGE) VALUES(%s,%s,%s,%s)"
    cur.execute(sql2,values)
    conn.commit()
