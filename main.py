# 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
# Lance's pat for github ^

import psycopg2

print("Connecting to database...")
connection = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
cursor = connection.cursor()
print("Connected")

cursor.execute("SELECT * FROM game")

print(cursor.fetchall())


cursor.close()
connection.close()
print("PostgreSQL connection is closed")