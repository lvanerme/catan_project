import psycopg2
from psycopg2.extensions import AsIs
import random


def main():
    conn = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
    cur = conn.cursor()

    create_game(cur)

    conn.commit()
    cur.close()


def create_game(cur):

    # insert into game
    cur.execute("INSERT INTO game (status) VALUES (true) RETURNING id")
    game_id = cur.fetchone()[0]

    # insert board
    gameID = AsIs('"gameID"')
    cur.execute(f"INSERT INTO board (game_id) VALUES (%s) RETURNING id", (game_id,))
    board_id = cur.fetchone()[0]

    # insert tiles
    tile_values = get_tile_values(board_id)
    args = ','.join(cur.mogrify("(%s,%s,%s,%s,%s)", i).decode('utf-8') for i in tile_values)
    cur.execute(f"INSERT INTO tile (board_id, number, location_row, location_col, robber) VALUES {args}")

    return cur


def get_tile_values(board_id) -> list:
    tile_numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12, -1]
    tiles = []

    for col in range(0, 3):
        tile = get_tile(board_id, 0, col, tile_numbers)
        tile_numbers.remove(tile[1])
        tiles.append(tile)

    for col in range(0, 4):
        tile = get_tile(board_id, 1, col, tile_numbers)
        tile_numbers.remove(tile[1])
        tiles.append(tile)

    for col in range(0, 5):
        tile = get_tile(board_id, 2, col, tile_numbers)
        tile_numbers.remove(tile[1])       
        tiles.append(tile)

    for col in range(0, 4):
        tile = get_tile(board_id, 3, col, tile_numbers)
        tile_numbers.remove(tile[1])        
        tiles.append(tile)

    for col in range(0, 3):
        tile = get_tile(board_id, 4, col, tile_numbers)
        tile_numbers.remove(tile[1]) 
        tiles.append(tile)

    return tiles


def get_tile(board_id, row, col, tile_numbers: list) -> tuple:
    num = random.choice(tile_numbers)

    robber = True if num == -1 else False
    tile = (board_id, num, row, col, robber)

    return tile




main()

