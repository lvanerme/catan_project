def check_resources(cur, player_id) -> tuple:
    cur.execute(f"SELECT * FROM hand WHERE player_id = {player_id}")
    
    return cur.fetchone()


