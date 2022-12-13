import psycopg2
import sys

from queries.create_game import create_game
from queries.place_initial_pieces import place_initial_pieces

def main():

    connection = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
    cursor = connection.cursor()

    print("Welcome to Catan")
    print("Press enter to create a new game")

    sys.stdin.readline()
    game_id = create_game(cursor, connection)

    print("Game created")
    print("Press enter to start game")
    sys.stdin.readline()

    place_initial_pieces(cursor, connection, 28, 12)

    # players = get_players(game_id)

    # player = 0
    # while True:
    #     # take_turn(game_id, players[player])
        
    #     # if check_win(game_id):
    #         # break
        
    #     if player != 3:
    #         player += 1
    #     else:
    #         player = 0

    # # get_winner(game_id)

    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")


main()