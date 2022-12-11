# 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
# Lance's pat for github ^

import psycopg2
import sys

print("Connecting to database...")
connection = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
cursor = connection.cursor()
print("Connected")




def place_initial_pieces(gameID):
    insert_query = """ INSERT INTO turn ("gameID", "roll") VALUES (%s, %s)"""
    params_to_insert = (gameID, 0)
    cursor.execute(insert_query, params_to_insert)
    print("It should've inserted")

place_initial_pieces(1)

cursor.close()
connection.close()
print("PostgreSQL connection is closed")