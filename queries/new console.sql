SELECT tile.number, tile.type, piece.type, piece.player_id
FROM tile INNER JOIN tile_pieces ON tile.id = tile_pieces.tile_id
INNER JOIN piece ON piece.id = tile_pieces.piece_id
WHERE tile.number = 9
AS sub;

DO $$
DECLARE
rows RECORD;
BEGIN
FOR rows IN SELECT tile.number, tile.type, piece.type, piece.player_id FROM tile INNER JOIN tile_pieces ON tile.id = tile_pieces.tile_id INNER JOIN piece ON piece.id = tile_pieces.piece_id WHERE tile.number = 9
    LOOP
    UPDATE hand SET rows.type = rows.type + 1 WHERE hand.player_id = rows.player_id;
    end loop;
END$$;