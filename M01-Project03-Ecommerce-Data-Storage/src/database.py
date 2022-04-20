import mysql.connector
import random
import time
import datetime


# Global methods to push interact with the Database

# This method establishes the connection with the MySQL
def create_server_connection(host_name, user_name, user_password):
    # Implement the logic to create the server connection
    return mysql.connector.connect(host=host_name,
                                   user=user_name,
                                   passwd=user_password)


# This method will create the database
def create_switch_database(connection, db_name, switch_db):
    # For database creation use this method
    # If you have created your database using UI, no need to implement anything
    pass


# This method will establish the connection with the newly created DB
def create_db_connection(host_name, user_name, user_password, db_name):
    return mysql.connector.connect(host=host_name,
                                   user=user_name,
                                   passwd=user_password,
                                   database=db_name)


# Perform all single insert statements in the specific table through a single function call
def create_insert_query(connection, query):
    # This method will perform creation of the table
    # this can also be used to perform single data point insertion in the desired table
    cursor = connection.cursor()
    cursor.execute(query, query, query)
    connection.commit()
    print(cursor.rowcount, "was inserted")
    return


# retrieving the data from the table based on the given query
def select_query(self, connection, query):
    # fetching the data points from the table 
    cursor = connection.cursor()
    cursor.execute(query)
    selectQuery = cursor.fetchall()
    print(selectQuery)
    return selectQuery


# performing the execute many query over the table,
# this method will help us to inert multiple records using a single instance
def insert_many_data(connection, sql, val):
    # to perform multiple insert operation in teh database
    cursor = connection.cursor()
    cursor.execute(sql, val)
    connection.commit()
    print(cursor.rowcount, "was inserted")
    return
