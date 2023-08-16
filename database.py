from random import randint
import mysql.connector
from mysql.connector import Error

def create_connection(host_name,user_name,user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host =  host_name,
            database = user_name,
            user = user_password,
            password = db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_read_query(connection,query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occured")
