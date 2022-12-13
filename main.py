import psycopg2
import sys
import random

from queries.create_game import create_game
from queries.place_initial_pieces import place_initial_pieces
from queries.new_turn import new_turn
from queries.get_players import get_players
from queries.get_resources import get_resources
from queries.check_resources import check_resources
from queries.place_piece import place_piece
from queries.buy_dev_card import buy_dev_card
from queries.check_winner import check_winner
from queries.get_winner import get_winner


def main():

    connection = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
    cursor = connection.cursor()

    print("Welcome to Catan")
    print("Press enter to create a new game")

    sys.stdin.readline()
    game_id, board_id = create_game(cursor, connection)

    cursor.execute(f"""SELECT tile.location_row, tile.location_col, tile.type, tile.robber, tile.number 
                      FROM tile JOIN board ON tile.board_id = board.id
                      JOIN game on board.game_id = game.id
                      WHERE game_id = {game_id}""")

    rand_board = cursor.fetchall()

    for col in range(3):
      print(f"           {rand_board[col]}", end='')
    print("")
    print("")

    for col in range(3,7):
      print(f"       {rand_board[col]}", end='')
    print("")
    print("")

    for col in range(7,12):
      print(f"   {rand_board[col]}", end='')
    print("")
    print("")

    for col in range(12,16):
      print(f"       {rand_board[col]}", end='')
    print("")
    print("")

    for col in range(16,19):
      print(f"           {rand_board[col]}", end='')
    print("")

    print("Game created")
    print("Press enter to start game")
    sys.stdin.readline()

    place_initial_pieces(cursor, connection, game_id, board_id)

    players = get_players(cursor, game_id)

    player = 0
    while True:
      player_id = players[player][0]
      print(f"Player: {player_id}'s turn!")
      roll = random.randint(2,12)
      new_turn(cursor, connection, game_id, player_id, roll)

      print(f"Roll was: {roll}!")

      get_resources(cursor, connection, game_id, roll)

      while True:
        current_hand = check_resources(cursor, player_id)

        print(f"Here is your current hand: \n\t brick:{current_hand[2]} \n\t wood:{current_hand[3]} \n\t wheat:{current_hand[4]} \n\t ore:{current_hand[5]} \n\t sheep:{current_hand[6]} ")
        
        print("What would you like to do? \n Place Piece = 0 \t Buy Dev Card = 1 \t End turn = 2")
        move = sys.stdin.readline()

        print(move, type(move))
        if move == '0':
          success = place_piece(cursor, connection, player_id)

          if not success:
            print("Piece could not be placed")
            continue
          print("Piece placed")
        elif move == '1':
          dev_card = buy_dev_card(cursor, player_id, game_id)

          if not dev_card:
            print("Card could not be bought")
            continue
          print(f"Your Card: {dev_card}")
        else:
          break

      if check_winner(cursor, connection, game_id):
        break
        
      if player != 3:
        player += 1
      else:
        player = 0

    print(f"Player {player[0]} Wins!")

    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")


main()