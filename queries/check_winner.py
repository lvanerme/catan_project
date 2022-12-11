import psycopg2
import random


def main():
    conn = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
    cur = conn.cursor()
    ##needs pipeline to get standard input, but is set up to handle it
    winner_id = check_winner(cur, 1)
    print(winner_id)

    conn.commit()
    cur.close()



def check_winner(cur, g_id):
    winner_id = -1
    #check the winner, returns player id if winner, -1 if no one has won yet

    cur.execute( """SELECT winner, player_id FROM player 
       INNER JOIN game_player ON game_player.player_id = player.id 
       WHERE game_id = %s and winner = true""", (g_id,))
       
    result = cur.fetchone()
    if result != None:
        winner_id = result[1]
    return winner_id

main()

