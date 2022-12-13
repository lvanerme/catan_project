import random
from check_resources import check_resources


def buy_dev_card(cur, player_id, game_id) -> bool:

    # get hand values
    (id, player_id, brick, wood, wheat, ore, sheep) = check_resources(cur, player_id)

    if wheat < 1 or ore < 1 or sheep < 1:
        return False

    # get dev_cards
    cur.execute(f"SELECT * FROM dev_card WHERE game_id = {game_id} AND hand_id = -1")
    dev_cards = list(cur.fetchall())

    if len(dev_cards) == 0:
        return False

    # update selected card with hand_id
    dev_card = random.choice(dev_cards)
    cur.execute(f"UPDATE dev_card SET hand_id = {dev_card[1]} WHERE id = {dev_card[0]}")

    return True

    

