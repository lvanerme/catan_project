import random
import psycopg2
from check_resources import check_resources


def buy_dev_card(cur, conn, player_id, game_id) -> bool:

    (hand_id, player_id, brick, wood, wheat, ore, sheep) = check_resources(cur, player_id)

    if wheat < 1 or ore < 1 or sheep < 1:
        return False

    cur.execute(f"SELECT * FROM dev_card WHERE game_id = {game_id} AND hand_id IS NULL")
    dev_cards = list(cur.fetchall())

    if len(dev_cards) < 1:
        return False

    card = random.choice(dev_cards)

    cur.execute(f"UPDATE hand SET wheat = {wheat - 1}, ore = {ore - 1}, sheep = {sheep - 1} WHERE hand.player_id = {player_id}")
    cur.execute(f"UPDATE dev_card SET hand_id = {hand_id} WHERE id = {card[0]}")
    conn.commit()

    return True


connection = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
cursor = connection.cursor()

buy_dev_card(cursor, connection, 1, 44)