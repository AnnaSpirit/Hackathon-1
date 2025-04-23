-- pawn_to_king.sql (pour SQLite)
CREATE TABLE IF NOT EXISTS games (
  game_id     INTEGER PRIMARY KEY AUTOINCREMENT,
  started_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pieces (
  piece_id    INTEGER PRIMARY KEY AUTOINCREMENT,
  game_id     INTEGER,
  type        TEXT,
  color       TEXT,
  row         INTEGER,
  col         INTEGER,
  has_moved   INTEGER DEFAULT 0,
  FOREIGN KEY(game_id) REFERENCES games(game_id)
);

CREATE TABLE IF NOT EXISTS moves (
  move_id            INTEGER PRIMARY KEY AUTOINCREMENT,
  game_id            INTEGER,
  piece_id           INTEGER,
  from_row           INTEGER,
  from_col           INTEGER,
  to_row             INTEGER,
  to_col             INTEGER,
  captured_piece_id  INTEGER,
  FOREIGN KEY(game_id) REFERENCES games(game_id),
  FOREIGN KEY(piece_id) REFERENCES pieces(piece_id)
);
