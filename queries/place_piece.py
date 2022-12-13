import sys

from queries.check_resources import check_resources


def insert_piece(cur, conn, player_id, tile_id, piece_type, location) -> bool:

    hand = check_resources(cur, player_id)
    cur.execute(f"SELECT * FROM piece_count WHERE player_id = {player_id}")
    (id, player_id, settlement_cnt, city_cnt, road_cnt) = cur.fetchone()

    valid = False
    if piece_type == 'settlement':
        valid = _place_settlement(cur, hand, settlement_cnt)
    elif piece_type == 'city':
        valid = _place_city(cur, hand, city_cnt)
    elif piece_type == 'road':
        valid = _place_road(cur, hand, road_cnt)

    if not valid:
        return False
    
    cur.execute(f"INSERT INTO piece (player_id, type, location) VALUES ({player_id}, {piece_type}, {location}) RETURNING id")
    piece_id = cur.fetchone()[0]
    conn.commit()

    cur.execute(f"INSERT INTO tile_piece VALUES {piece_id}, {tile_id}")
    conn.commit()

    return True


def _place_settlement(cur, hand, settlement_cnt) -> bool:
    
    if settlement_cnt < 1:
        return False

    (id, player_id, brick, wood, wheat, ore, sheep) = hand
    if brick < 1 or wood < 1 or wheat < 1 or sheep < 1:
        return False

    cur.execute(f"UPDATE hand SET brick = {brick - 1}, wood = {wood - 1}, wheat = {wheat - 1}, sheep = {sheep - 1} WHERE hand.player_id = {player_id}")
    cur.execute(f"UPDATE piece_count SET settlement = settlement - 1 WHERE piece_count.player_id = {player_id}")
    cur.execute(f"UPDATE player SET points = points + 1 WHERE player.id = {player_id}")

    return True


def _place_city(cur, hand, city_cnt) -> bool:

    if city_cnt < 1:
        return False

    (id, player_id, brick, wood, wheat, ore, sheep) = hand
    if ore < 3 or wheat < 2:
        return False

    cur.execute(f"UPDATE hand SET ore = {brick - 3}, wheat = {wheat - 2} WHERE hand.player_id = {player_id}")
    cur.execute(f"UPDATE piece_count SET city = city - 1 WHERE piece_count.player_id = {player_id}")
    cur.execute(f"UPDATE player SET points = points + 2 WHERE player.id = {player_id}")

    return True


def _place_road(cur, hand, road_cnt) -> bool:

    if road_cnt < 1:
        return False

    (id, player_id, brick, wood, wheat, ore, sheep) = hand
    if wood < 2:
        return False

    cur.execute(f"UPDATE hand SET wood = {wood - 2} WHERE hand.player_id = {player_id}")
    cur.execute(f"UPDATE piece_count SET road = road - 1 WHERE piece_count.player_id = {player_id}")

    return True


def place_piece(cur, conn, player_id):
  print("Where would you like to place a piece? (row,col)")
  row, col = sys.stdin.readline()

  print("Where on the piece do you want to place it?(0-11)")
  location = sys.stdin.readline()

  cur.execute(f"SELECT tile_id FROM tile WHERE location_row = {row} AND location_col = {col}")
  tile_id = cur.fetchone()[0]

  print("What type of piece are you building?(settlement, city, road)")
  type_var = sys.stdin.readline()

  return insert_piece(cur, conn, player_id, tile_id, type_var, location)


