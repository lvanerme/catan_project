def get_players(cursor):
  # needs board id to get specific tiles
  boardID = 4 # hard coded for testing

  # needs specific game id
  gameID = 28 # hard coded for testing
  
  cursor.execute(f"SELECT player.id FROM player JOIN game_player ON player.id=game_player.player_id JOIN game ON game_player.game_id = game.id WHERE game_id = {gameID}")
  playerID = cursor.fetchall()

  print(playerID)
