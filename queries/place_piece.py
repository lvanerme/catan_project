def place_piece(cur, p_id, t_id, typeVar, location):
    ##adds a new piece, depending on type will withdraw resources form hand, subtract piece from inventory, and add points
    cur.execute("""INSERT INTO piece (tile_id, player_id, type, location) VALUES(%s, %s, %s, %s)""", (t_id, p_id, typeVar, location))
    if typeVar == 'settlement':
        cur.execute("""UPDATE hand SET brick = brick - 1, wood = wood - 1, wheat = wheat - 1, sheep = sheep - 1 WHERE hand.player_id = %s""", (p_id,))
        cur.execute("""UPDATE piece_count SET settlement = settlement - 1 WHERE piece_count.player_id = %s""", (p_id,))
        cur.execute("""UPDATE player SET points = points + 1 WHERE player.id = %s""", (p_id),)
    if typeVar == 'city':
        cur.execute("""UPDATE hand SET wheat = wheat - 2, ore = ore - 3 WHERE hand.player_id = %s""", (p_id,))
        cur.execute("""UPDATE piece_count SET city = city - 1 WHERE piece_count.player_id = %s""", (p_id,))
        cur.execute("""UPDATE player SET points = points + 2 WHERE player.id = %s""", (p_id,))
    if typeVar == 'road':
        cur.execute("""UPDATE hand SET brick = brick - 1, wood - 1 WHERE hand.player_id = %s""", (p_id,))  
        cur.execute("""UPDATE piece_count SET road = road - 1 WHERE piece_count.player_id = %s""", (p_id,))

    return cur
