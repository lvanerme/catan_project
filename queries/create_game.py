import psycopg2
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
    cur.execute("INSERT INTO board (game_id) VALUES (%s) RETURNING id", (game_id))
    board_id = cur.fetchone()[0]

    # insert tiles
    tile_values = get_tile_values(board_id)

    return cur


def get_tile_values(board_id) -> list:
    tile_numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12, -1]
    tiles = []

    for col in range(0, 3):
        num = random.choice(tile_numbers)
        tile_numbers.remove(num)

        tile = (board_id, num, 0, col, False)
        tiles.append(tile)

    for col in range(0, 4):
        num = random.choice(tile_numbers)
        tile_numbers.remove(num)

        tile = (board_id, num, 1, col, False)
        tiles.append(tile)

    for col in range(0, 5):
        num = random.choice(tile_numbers)
        tile_numbers.remove(num)

        tile = (board_id, num, 2, col, False)
        tiles.append(tile)

    for col in range(0, 4):
        num = random.choice(tile_numbers)
        tile_numbers.remove(num)

        tile = (board_id, num, 3, col, False)
        tiles.append(tile)

    for col in range(0, 3):
        num = random.choice(tile_numbers)
        tile_numbers.remove(num)

        tile = (board_id, num, 4, col, False)
        tiles.append(tile)

    return tiles

main()

