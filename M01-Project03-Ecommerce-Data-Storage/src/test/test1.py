import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Nishad@2000", database="ecommerce_record")
    
mycursor = mydb.cursor()

mycursor.execute("describe users")

for i in mycursor:
    print(i)