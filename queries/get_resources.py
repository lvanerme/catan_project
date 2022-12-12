import psycopg2

def main():
    conn = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
    cur = conn.cursor()
    c2 = conn.cursor()
    
    ##needs to pipeline to take in unique input
    get_resources(cur, c2, 1, 9)
    
    conn.commit()
    cur.close()



def get_resources(cur, c2, g_id, roll):
    cur.execute("""SELECT tile.number, tile.type, piece.type, piece.player_id, tile.robber, board.game_id FROM board INNER JOIN tile ON board.id = 
    tile.board_id INNER JOIN tile_pieces ON tile.id = tile_pieces.tile_id INNER JOIN piece ON piece.id = tile_pieces.piece_id WHERE tile.number = %s AND board.game_id = %s""", (roll, g_id, ))
    tile = cur.fetchone()
    while tile != None:
        result = str(tile)
        result = result[1:len(result)-1]
        result = str(result).split(', ')
        resource = result[1]
        resource = resource[1:len(resource)-1]
        placement = result[2]
        placement = placement[1:len(placement)-1]
        player = result[3]
        robber = result[4]
        if robber == 'False':
            if placement == 'settlement':
                if resource == 'wood':
                    c2.execute("""UPDATE hand SET wood = wood + 1 WHERE hand.player_id = %s""", (player,))
                if resource == 'brick':
                    c2.execute("""UPDATE hand SET brick = brick + 1 WHERE hand.player_id = %s""", (player,))
                if resource == 'ore':
                    c2.execute("""UPDATE hand SET ore = ore + 1 WHERE hand.player_id = %s""", (player,))
                if resource == 'sheep':
                    c2.execute("""UPDATE hand SET sheep = sheep + 1 WHERE hand.player_id = %s""", (player,))
                if resource == 'wheat':
                    c2.execute("""UPDATE hand SET wheat = wheat + 1 WHERE hand.player_id = %s""", (player,))
            if placement == 'city':
                if resource == 'wood':
                    c2.execute("""UPDATE hand SET wood = wood + 2 WHERE hand.player_id = %s""", (player,))
                if resource == 'brick':
                    c2.execute("""UPDATE hand SET brick = brick + 2 WHERE hand.player_id = %s""", (player,))
                if resource == 'ore':
                    c2.execute("""UPDATE hand SET ore = ore + 2 WHERE hand.player_id = %s""", (player,))
                if resource == 'sheep':
                    c2.execute("""UPDATE hand SET sheep = sheep + 2 WHERE hand.player_id = %s""", (player,))
                if resource == 'wheat':
                    c2.execute("""UPDATE hand SET wheat = wheat + 2 WHERE hand.player_id = %s""", (player,))
        tile = cur.fetchone()


main()
