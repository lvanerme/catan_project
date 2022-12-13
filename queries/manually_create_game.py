import sys

def manually_create_game(cursor):
  # insert into game
  cursor.execute("INSERT INTO game (status) VALUES (true) RETURNING id")
  game_id = cursor.fetchone()[0]

  # insert board
  cursor.execute(f"INSERT INTO board (game_id) VALUES (%s) RETURNING id", (game_id,))
  board_id = cursor.fetchone()[0]

  row = 5
  col = 3
  going_up = True
  for row_iter in range(0,row):
    col_iter = 0
    while col_iter < col:
      print(f"Enter tile type for position '{row_iter}, {col_iter}'")
      tile_type = sys.stdin.readline()
      robber = False
      if tile_type.lower() == 'desert':
        robber = True

      print(f"Enter number on tile for position '{row_iter}, {col_iter}'")
      tile_number = sys.stdin.readline()

      cursor.execute(f"INSERT INTO tile (board_id, type, location_row, location_col, robber) VALUES {board_id, tile_type, row_iter,  col_iter, tile_number, robber}")
      col_iter += 1

    if col == 5: going_up = False
    if going_up: col += 1
    else: col -= 1


