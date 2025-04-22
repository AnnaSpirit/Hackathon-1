-- Database: pawn_to_king

-- DROP DATABASE IF EXISTS pawn_to_king;

-- CREATE DATABASE pawn_to_king
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'French_France.1252'
--     LC_CTYPE = 'French_France.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

--création de la base et des tables
-- CREATE TABLE games (
--     game_id   INTEGER PRIMARY KEY,
--     created_at TEXT DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE pieces (
--     piece_id  INTEGER PRIMARY KEY,
--     game_id   INTEGER NOT NULL,
--     type      TEXT    NOT NULL,     -- 'king','queen','rook','bishop','knight','pawn'
--     color     TEXT    NOT NULL,     -- 'white' ou 'black'
--     row       INTEGER NOT NULL,     -- 1 à 8
--     col       INTEGER NOT NULL,     -- 1 à 8
--     has_moved BOOLEAN DEFAULT TRUE,      -- pour le roque ou la prise en passant
--     FOREIGN KEY(game_id) REFERENCES games(game_id)
-- );

-- CREATE TABLE moves (
--     move_id    INTEGER PRIMARY KEY,
--     game_id    INTEGER NOT NULL,
--     piece_id   INTEGER NOT NULL,
--     from_row   INTEGER NOT NULL,
--     from_col   INTEGER NOT NULL,
--     to_row     INTEGER NOT NULL,
--     to_col     INTEGER NOT NULL,
--     captured_piece_id INTEGER,      -- NULL si pas de capture
--     moved_at   TEXT DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY(game_id) REFERENCES games(game_id),
--     FOREIGN KEY(piece_id) REFERENCES pieces(piece_id),
--     FOREIGN KEY(captured_piece_id) REFERENCES pieces(piece_id)
-- );
