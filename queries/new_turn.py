import psycopg2
import random

##creates a new turn with a game id and a roll
def main():
    conn = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
    cur = conn.cursor()

    ##needs to pipeline to take in unique input
    new_turn(cur, 1, 8)

    conn.commit()
    cur.close()



def new_turn(cur, g_id, roll):
    
    #insert into turn 
    cur.execute("""INSERT INTO turn (game_id, roll) VALUES(%s, %s)""", (g_id, roll))
    return cur

main()