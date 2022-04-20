import csv
import database as db

PW = "Nishad@2000"  #IMPORTANT! Put your MySQL Terminal password here.
ROOT = "root"
DB = "ecommerce_record"  #This is the name of the database we will create in the next step - call it whatever you like.
LOCALHOST = "localhost"
connection = db.create_server_connection(LOCALHOST, ROOT, PW)

# creating the schema in the DB 
db.create_switch_database(connection, DB, DB)


RELATIVE_CONFIG_PATH = '../config/'

USER = 'users'
ITEM = 'items'
ORDER = 'orders'

connection_db = db.create_db_connection(LOCALHOST, ROOT, PW, DB)
cursor = connection_db.cursor()

# Create the tables through python code here
# if you have created the table in UI, then no need to define the table structure
# If you are using python to create the tables, call the relevant query to complete the creation

with open(RELATIVE_CONFIG_PATH+USER+'.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    val.pop(0)
    query = f"INSERT INTO {USER} values(%s, %s, %s, %s, %s, %s)"
    cursor.executemany(query, val)
    connection_db.commit()
    print(cursor.rowcount, "was inserted")


with open(RELATIVE_CONFIG_PATH+ITEM+'.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    val.pop(0)
    query1 = f"INSERT INTO {ITEM} values(%s, %s, %s, %s, %s, %s)"
    cursor.executemany(query, val)
    connection_db.commit()
    print(cursor.rowcount, "was inserted")


with open(RELATIVE_CONFIG_PATH+ORDER+'.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    val.pop(0)
    query2 = f"INSERT INTO {ORDER} values(%s, %s, %s, %s, %s, %s)"
    cursor.executemany(query, val)
    connection_db.commit()
    print(cursor.rowcount, "was inserted")


