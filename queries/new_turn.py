def new_turn(cur, game_id, player_id, roll) -> int:
    cur.execute(f"INSERT INTO turn (game_id, player_id, roll) VALUES({game_id}, {player_id}, {roll}) RETURNING id")

    return cur.fetchone()[0]
