def get_players(cursor, gameID) -> list(tuple):
  cursor.execute(f"SELECT player.id FROM player JOIN game_player ON player.id=game_player.player_id JOIN game ON game_player.game_id = game.id WHERE game_id = {gameID}")
  return cursor.fetchall()