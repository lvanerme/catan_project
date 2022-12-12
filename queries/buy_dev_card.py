def buy_dev_card(cur, player_id) -> bool:

    cur.execute(f"SELECT * FROM hand WHERE player_id = {player_id}")
    (id, player_id, brick, wood, wheat, ore, sheep) = cur.fetchall()[0]

    if wheat < 1 or ore < 1 or sheep < 1:
        return False

    

