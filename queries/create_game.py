import psycopg2

conn = psycopg2.connect("dbname=catan_database user=postgres password=postgres port=5434 ")
cur = conn.cursor()