
import pymysql

def create_connection(host, port, database, user, password):
    conn = None
    try:
      conn = pymysql.connect(host=host, port=int(port), database=database, user=user, password=password)
    except Exception as e:
      print("Database connection failed due to {}".format(e))

    return conn

def user_check(username):

  ENDPOINT = "database-1.ctszvlohmh0g.us-east-2.rds.amazonaws.com"
  DBNAME = "testedb"
  USR = "admin"
  PORT = "3306"
  REGION="us-east-2a"
  PASSWORD = "wS4UV5mqHAkVxMbh"

  conn = create_connection(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password=PASSWORD)

  with conn:
    cur = conn.cursor()
    sql = "SELECT USERNAME FROM users WHERE USERNAME = '"+username+"';"
    cur.execute(sql)
    query = cur.fetchone()
    if query == None:
      return True
    else:
      return False

user_check('abc')
