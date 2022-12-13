import random


def buy_dev_card(cur, conn, player_id, game_id, hand_id):
    print(hand_id)

    # get hand values
    cur.execute(f"SELECT * FROM hand WHERE player_id = {player_id}")
    (id, player_id, brick, wood, wheat, ore, sheep) = cur.fetchone()

    if wheat < 1 or ore < 1 or sheep < 1:
        return False

    # get dev_cards
    cur.execute(f"SELECT * FROM dev_card WHERE game_id = {game_id} AND hand_id IS null")
    dev_cards = list(cur.fetchall())


    if len(dev_cards) == 0:
        return False

    # update selected card with hand_id
    dev_card = random.choice(dev_cards)
    cur.execute(f"UPDATE dev_card SET hand_id = {hand_id} WHERE id = {dev_card[0]}")
    conn.commit()

    return dev_card

    

