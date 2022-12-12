# 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
# Lance's pat for github ^

import psycopg2
from queries.create_game import create_game

print("Connecting to database...")
connection = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
cursor = connection.cursor()
print("Connected")

cursor.execute("SELECT * FROM game")

print(cursor.fetchall())

#game_id = create_game(cursor, connection)
# place_initial_pieces()
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
