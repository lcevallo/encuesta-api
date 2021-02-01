import pymysql.cursors
import psycopg2


# Function return a connection.
def getConnectionMysql():
    # You can change the connection arguments.
    connectionMysqlEncuestas = pymysql.connect(
        host="10.0.0.8", port=3306, user="lcevallosc",
        charset='utf8mb4',
        passwd="Ulaica2019-", db="db_lime_276",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connectionMysqlEncuestas


def getConnectionEkudemic():
    connectionPostgresEkudemic = psycopg2.connect(
        host="db.ulvr.edu.ec",
        database="ekudemic",
        user="desarrollo4",
        password="charmander")

    return connectionPostgresEkudemic
