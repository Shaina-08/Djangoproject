import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Shaina05@',
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE IF NOT EXISTS bhard')

print("all done")
