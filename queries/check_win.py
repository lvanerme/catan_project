def check_win(cur, c2, g_id):
    
    cur.execute("""SELECT * FROM player INNER JOIN game_player ON game_player.player_id = player.id WHERE game_player.game_id = %s""", (g_id,))
    player = cur.fetchone()
    p_id = -1
    points = -1
    while player != None:
        print(player)
        result = str(player)
        result = result[1:len(result)-1]
        result = str(result).split(', ')
        p_id = result[0]
        points = result[1]
        print(p_id, points)
        if int(points) >= 10:
            c2.execute("""UPDATE player SET winner = true WHERE id = %s""", (p_id,))
            c2.execute("""UPDATE game SET status = false WHERE id = %s""", (g_id,))
            return True
        player = cur.fetchone()
