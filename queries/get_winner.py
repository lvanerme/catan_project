def get_winner(cur, game_id):
  cur.execute(f"SELECT id, winner FROM player WHERE winner = true INNER JOIN game_player ON game_id = {game_id}")

  return cur.fetchall()
