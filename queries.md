# Queries

## Game Setup
1. `create_game()`
    1. `INSERT game`
    1. `INSERT board`, associate with `game`
    1. `INSERT` 8 `port` entries
    1. `INSERT` 19 `tile` entries, associate with `board`
        1. Randomize `tile.number`
    1. `INSERT INTO tile_port` with correct `port` and `tile` ids
    1. `INSERT` 4 `player` entries
    1. `INSERT INTO game_player` with appropriate `player_id` and `game_id` values
    1. `INSERT` 4 `hand` entries, associate with respective `player`
    1. `INSERT` 4 `piece_count` entries, associate with respective `player`
    1. `INSERT` 25 `dev_card` entries with appropriate types, associated with `game.id`

2. `place_initial_pieces()`
    1. `INSERT turn`, associate with first `player` and `board`
    1. `for i in 8:` (two placing turns for each player)
        1. `INSERT piece` with `type == settlement` and associate with respective `player` and `tile`. Assign location on `tile`
        1. `INSERT piece` with `type == road` and associate with respective `player` and `tile`. Assign location on `tile`
        1. All placements validated with `validate_placement()`

## Typical Game Flow
1. `check_win(game_id)`
1. `INSERT turn` with next `turn.id` and associate with next `player.id` random `roll` value
1. `get_resources()`
1. `while not end_turn():`
    1. perform action

### Actions
- NOTE: All actions should be *TRANSACTIONS*
1. `place_piece(player_id, tile_id, location, type)`
    1. `if validate_placement(tile_id, location, type):`
    1. `INSERT INTO piece(tile_id, location, type) VALUES(tile_id, location, type)`
    1. `UPDATE hand SET <new_card_values> WHERE hand.player_id = player_id`
    1. `UPDATE piece_count SET <type> = <type> - 1 WHERE piece_count.player_id = player_id`

1. `buy_dev_card(player_id)`
    1. `hand = SELECT * FROM hand WHERE hand.player_id = player_id`
    1. `check_resources(hand.id)`
    1. `INSERT INTO dev_card(hand_id, active) VALUES(hand.id, true)`
        - NOTE: `dev_card.type` will have to randomized somehow

1. `play_dev_card(dev_card_id)`
    1. Gross case statement for different types of dev cards...too much work to think about rn

## Helper queries
1. `validate_placement(tile_id, location, type)`
    1. `SELECT row, col as location FROM piece WHERE piece.location in location.adjacent_tiles`
    1. Getting adjacent locations (IMPOSSIBLE):
        1. `pass`

1. `check_resources(hand_id, type)`
    1. `pass`

1. `get_resources(roll, game_id)`
    1. `pass`

1. `check_win(game_id)`
    1. `players = SELECT * FROM game_player INNER JOIN player ON game_player.player_id = player.id WHERE game_player.game_id = game_id`
    1. `for player in players:`
        1. `if player.points >= 10`:
            1. `player.winner = True`
            1. `game.status = False`
            1. `return True`
    1. `return False`
