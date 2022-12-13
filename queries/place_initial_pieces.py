import sys
from queries.get_players import get_players

def place_initial_pieces(cursor, game_id, board_id):
  players = get_players(cursor, game_id)
  print(players)

  for player_id in players:
    execute_queries(cursor, player_id[0], game_id, board_id)
  
  for player_id in reversed(players):
    execute_queries(cursor, player_id[0], game_id, board_id)


def execute_queries(cursor, player, game_id, board_id):
  print(f"Player: {player}")

  cursor.execute("INSERT INTO turn (game_id, player_id, roll) VALUES (%s, %s, %s) RETURNING id", (game_id, player, 0)) 

  print("Enter tile row and col for settlement placement (row, col):")
  row, col = sys.stdin.readline().split(',')
  cursor.execute("SELECT id FROM tile WHERE board_id = %s and location_row = %s and location_col = %s", (board_id, row, col))
  tile_id = cursor.fetchone()[0]

  print("Enter tile number for settlement placement (0,2,4,6,8,10):")
  settlement_location_on_tile = sys.stdin.readline()
  cursor.execute("INSERT INTO piece (player_id, type, location) VALUES (%s, %s, %s) RETURNING id", (player, "settlement", settlement_location_on_tile))
  piece_id = cursor.fetchone()[0]

  cursor.execute(f"INSERT INTO tile_piece (piece_id, tile_id) VALUES ({piece_id}, {tile_id})")

  print("Enter tile row and col for road placement (row, col):")
  row, col = sys.stdin.readline().split(',')
  cursor.execute("SELECT id FROM tile WHERE board_id = %s and location_row = %s and location_col = %s", (board_id, row, col))
  tile_id = cursor.fetchone()[0]

  print("Enter tile number for road placement (1,3,5,7,9):")
  road_location_on_tile = sys.stdin.readline()
  cursor.execute("INSERT INTO piece (player_id, type, location) VALUES (%s, %s, %s) RETURNING id", (player, "road", road_location_on_tile))
  piece_id = cursor.fetchone()[0]

  cursor.execute(f"INSERT INTO tile_piece (piece_id, tile_id) VALUES ({piece_id}, {tile_id})")



