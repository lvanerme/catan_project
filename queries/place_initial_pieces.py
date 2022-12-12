# 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
# Lance's pat for github ^

import psycopg2
import sys

def main():
    print("Connecting to database...")
    connection = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
    cursor = connection.cursor()
    print("Connected")

    place_initial_pieces(cursor)

    connection.commit()

    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")

def place_initial_pieces(cursor):
   # needs board id to get specific tiles
    boardID = 4 # hard coded for testing

    # needs specific game id
    gameID = 20 # hard coded for testing

    for int in range(1,3):
        # There is probably a better way to do this, but as of now it works
        player = {(1): 1, (2): 2, (3): 3, (4): 4, (5): 4, (6): 3, (7): 2, (8): 1}[int]

        print("Player: " + str(player))
        cursor.execute("INSERT INTO turn (game_id, player_id, roll) VALUES (%s, %s, %s) RETURNING id", (gameID, player, 0)) 

        print("Enter tile row and col for settlement placement (row, col):")
        row, col = sys.stdin.readline().split(',')
        cursor.execute("SELECT id FROM tile WHERE board_id = %s and location_row = %s and location_col = %s", (boardID, row, col))
        tileID = cursor.fetchone()[0]

        print("Enter tile number for settlement placement (0,2,4,6,8,10):")
        settlementLocationOnTile = sys.stdin.readline()
        cursor.execute("INSERT INTO piece (tile_id, player_id, type, location) VALUES (%s, %s, %s, %s)", (tileID, player, "settlement", settlementLocationOnTile))

        print("Enter tile row and col for road placement (row, col):")
        row, col = sys.stdin.readline().split(',')
        cursor.execute("SELECT id FROM tile WHERE board_id = %s and location_row = %s and location_col = %s", (boardID, row, col))
        tileID = cursor.fetchone()[0]

        print("Enter tile number for road placement (1,3,5,7,9):")
        roadLocationOnTile = sys.stdin.readline()
        cursor.execute("INSERT INTO piece (tile_id, player_id, type, location) VALUES (%s, %s, %s, %s)", (tileID, player, "road", roadLocationOnTile))

main()

