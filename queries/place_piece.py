import psycopg2
import random

##


#place_piece(player_id, tile_id, location, type)


def main():
    conn = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
    cur = conn.cursor()
    
    ##needs to pipeline to take in unique input
    place_piece(cur, 1, 1, 'city', 3)
    
    conn.commit()
    cur.close()



def place_piece(cur, p_id, t_id, typee, location):
    ##adds a new piece, depending on type will withdraw resources form hand, subtract piece from inventory, and add points
    cur.execute("""INSERT INTO piece (tile_id, player_id, type, location) VALUES(%s, %s, %s, %s)""", (t_id, p_id, typee, location))
    match typee:
        case 'settlement':
            cur.execute("""UPDATE hand SET brick = brick - 1, wood = wood - 1, wheat = wheat - 1, sheep = sheep - 1 WHERE hand.player_id = %s""", (p_id,))
            cur.execute("""UPDATE piece_count SET settlement = settlement - 1 WHERE piece_count.player_id = %s""", (p_id,))
            cur.execute("""UPDATE player SET points = points + 1 WHERE player.id = %s""", (p_id),)
        case 'city':
            cur.execute("""UPDATE hand SET wheat = wheat - 2, ore = ore - 3 WHERE hand.player_id = %s""", (p_id,))
            cur.execute("""UPDATE piece_count SET city = city - 1 WHERE piece_count.player_id = %s""", (p_id,))
            cur.execute("""UPDATE player SET points = points + 2 WHERE player.id = %s""", (p_id,))
        case 'road':
            cur.execute("""UPDATE hand SET brick = brick - 1, wood - 1 WHERE hand.player_id = %s""", (p_id,))  
            cur.execute("""UPDATE piece_count SET road = road - 1 WHERE piece_count.player_id = %s""", (p_id,))

    return cur

main()