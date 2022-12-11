import psycopg2

conn = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
cur = conn.cursor()

cur.execute("SELECT * FROM game")

print(cur.fetchall())