import random


def create_game(cur, conn) -> int:

    # insert into game
    cur.execute("INSERT INTO game (status) VALUES (true) RETURNING id")
    game_id = cur.fetchone()[0]

    # insert board
    cur.execute(f"INSERT INTO board (game_id) VALUES (%s) RETURNING id", (game_id,))
    board_id = cur.fetchone()[0]

    # insert tiles
    tile_values = _get_tile_values(board_id)
    tile_args = ','.join(cur.mogrify("(%s,%s,%s,%s,%s)", i).decode('utf-8') for i in tile_values)
    cur.execute(f"INSERT INTO tile (board_id, number, location_row, location_col, robber) VALUES {tile_args}")

    _insert_player_values(cur, game_id)

    dev_card_values = _get_dev_card_values(game_id)
    dev_card_args = ','.join(cur.mogrify("(%s,%s,%s,%s)", i).decode('utf-8') for i in dev_card_values)
    cur.execute(f"INSERT INTO dev_card (hand_id, type, active, game_id) VALUES {dev_card_args}")

    conn.commit()

    return game_id


def _get_tile_values(board_id) -> list:
    tile_numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12, -1]
    tiles = []

    for col in range(0, 3):
        tile = get_tile(board_id, 0, col, tile_numbers)
        tile_numbers.remove(tile[1])
        tiles.append(tile)

    for col in range(0, 4):
        tile = get_tile(board_id, 1, col, tile_numbers)
        tile_numbers.remove(tile[1])
        tiles.append(tile)

    for col in range(0, 5):
        tile = get_tile(board_id, 2, col, tile_numbers)
        tile_numbers.remove(tile[1])       
        tiles.append(tile)

    for col in range(0, 4):
        tile = get_tile(board_id, 3, col, tile_numbers)
        tile_numbers.remove(tile[1])        
        tiles.append(tile)

    for col in range(0, 3):
        tile = get_tile(board_id, 4, col, tile_numbers)
        tile_numbers.remove(tile[1]) 
        tiles.append(tile)

    return tiles


def get_tile(board_id, row, col, tile_numbers: list) -> tuple:
    num = random.choice(tile_numbers)

    robber = True if num == -1 else False
    tile = (board_id, num, row, col, robber)

    return tile


def _insert_player_values(cur, game_id):

    # insert players
    player_values = _get_player_values()
    player_args = ','.join(cur.mogrify("(%s,%s,%s,%s)", i).decode('utf-8') for i in player_values)
    cur.execute(f"INSERT INTO player (points, winner, longest_road, largest_army) VALUES {player_args} RETURNING id")
    player_ids = cur.fetchall()

    # insert game_player
    game_player_values = _get_game_player_values(game_id, player_ids)
    game_player_args = ','.join(cur.mogrify("(%s,%s)", i).decode('utf-8') for i in game_player_values)
    cur.execute(f"INSERT INTO game_player VALUES {game_player_args}")

    # insert piece_count
    piece_count_values = _get_piece_count_values(player_ids)
    piece_count_args = ','.join(cur.mogrify("(%s,%s,%s,%s)", i).decode('utf-8') for i in piece_count_values)
    cur.execute(f"INSERT INTO piece_count (player_id, settlement, city, road) VALUES {piece_count_args}")

    # insert hands
    hand_values = _get_hand_values(player_ids)
    hand_args = ','.join(cur.mogrify("(%s,%s,%s,%s,%s,%s)", i).decode('utf-8') for i in hand_values)
    cur.execute(f"INSERT INTO hand (player_id, brick, wood, wheat, ore, sheep) VALUES {hand_args} RETURNING id")


def _get_player_values():
    players = []

    for _ in range(0, 4):
        player = (0, False, 1, 0)
        players.append(player)

    return players


def _get_game_player_values(game_id, player_ids: list):
    game_players = []

    for id in player_ids:
        game_player = (game_id, id)
        game_players.append(game_player)

    return game_players


def _get_piece_count_values(player_ids: list):
    piece_counts = []

    for id in player_ids:
        piece_count = (id, 5, 4, 15)
        piece_counts.append(piece_count)
        
    return piece_counts


def _get_hand_values(player_ids: list):
    hands = []

    for id in player_ids:
        hand = (id, 0, 0, 0, 0, 0)
        hands.append(hand)

    return hands


def _get_dev_card_values(game_id):
    dev_card_types = ['k','k','k','k','k','k','k','k','k','k','k','k','k','k','vp','vp','vp','vp','vp','rb','rb','yp','yp','m','m']
    dev_cards = []

    for card_type in dev_card_types:
        card = (-1, card_type, False, game_id)
        dev_cards.append(card)

    return dev_cards

