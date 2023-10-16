import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="PaSs_KyCx_1234",
)

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS user_data")
mydb.commit()  # Commit the changes to create the database

cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

cursor.close()  # Close the cursor
mydb.close()    # Close the database connection
