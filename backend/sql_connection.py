import mysql.connector

__cnx =None

def get_sql_connection():
    global __cnx
    if __cnx is None:
         cnx = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="@@jannat1300@@",
            database='grocery_store'
        )
         return cnx