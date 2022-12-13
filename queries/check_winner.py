def check_winner(cur, conn, game_id) -> int:

    cur.execute(f"""SELECT id, points 
                    FROM player 
                    JOIN game_player ON player.id = game_player.player_id
                    WHERE game_player.game_id = {game_id}"""
                )

    for player in cur.fetchall():
        if player[1] >= 10:
            cur.execute(f"UPDATE player SET winner = true WHERE id = {player[0]}")
            conn.commit()
            return player[0]
