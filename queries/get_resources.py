import psycopg2
import random

##get the resources for a player
def main():
    conn = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
    cur = conn.cursor()
    
    ##needs to pipeline to take in unique input
    resources = get_resources(cur, 1, 9)
    print(resources)
    
    conn.commit()
    cur.close()



def get_resources(cur, g_id, roll):
    pass


main()