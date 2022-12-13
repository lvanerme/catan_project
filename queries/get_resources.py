import psycopg2
import random

##get the resources for a player
def main():
    conn = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
    cur = conn.cursor()
    c2 = conn.cursor()
    
    ##needs to pipeline to take in unique input
    get_resources(cur, c2, 1, 9)
    
    conn.commit()
    cur.close()



def get_resources(cur, conn, game_id, roll):
    cur.execute(f"""SELECT tile.number, tile.type, piece.type, piece.player_id, tile.robber, board.game_id FROM board INNER JOIN tile ON board.id = 
    tile.board_id INNER JOIN tile_pieces ON tile.id = tile_pieces.tile_id INNER JOIN piece ON piece.id = tile_pieces.piece_id WHERE tile.number = {roll} AND board.game_id = {game_id}""")
    tiles = cur.fetchall()
    
    for tile in tiles:
        (number, tile_type, piece_type, player_id, robber, game_id) = tile
        if robber:
            continue

        num = 1 if piece_type == 'settlement' else 2

        cur.execute(f"SELECT {tile_type} FROM hand WHERE player_id = {player_id}")
        num_of_resource = cur.fetchone()[0]
        cur.execute(f"UPDATE hand set {tile_type} = {num_of_resource + num} WHERE hand.player_id = {player_id}")


main()
