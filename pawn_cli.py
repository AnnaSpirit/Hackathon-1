# import et connexion à la BD
import os
import sqlite3

# 🇫🇷 Codes ANSI pour colorer ton CLI
class Ansi:
    RESET   = '\033[0m'
    BOLD    = '\033[1m'
    DIM     = '\033[2m'
    WHITE   = '\033[37m'
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'


def init_db(db_name="pawn_to_king.db"):
    # 1. Chemin absolu du script SQL
    base_dir = os.path.dirname(__file__)
    script_path = os.path.join(base_dir, "pawn_to_king.sql")
    
    print(f"🔍 Working dir : {os.getcwd()}") ####
    
    print(f"🔍 SQL script   : {script_path} -> exists? {os.path.exists(script_path)}") ####

    # 2. Connexion SQLite
    conn = sqlite3.connect(os.path.join(base_dir, db_name))
    with open(script_path, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    return conn

def start_new_game(conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO games DEFAULT VALUES")
    game_id = cur.lastrowid

    # 🇫🇷 Position de départ : rangées 1,2 pour white ; 7,8 pour black
    setup = [
        ("rook",1,1),("knight",1,2),("bishop",1,3),("queen",1,4),
        ("king",1,5),("bishop",1,6),("knight",1,7),("rook",1,8),
        *[("pawn",2,c) for c in range(1,9)],
        *[("pawn",7,c) for c in range(1,9)],
        ("rook",8,1),("knight",8,2),("bishop",8,3),("queen",8,4),
        ("king",8,5),("bishop",8,6),("knight",8,7),("rook",8,8),
    ]

    for typ, row, col in setup:
        color = "white" if row <= 2 else "black"
        cur.execute(
            "INSERT INTO pieces(game_id, type, color, row, col) VALUES (?, ?, ?, ?, ?)",
            (game_id, typ, color, row, col)
        )
    conn.commit()
    return game_id


# def init_board():
#     board = [['' for _ in range(8)] for _ in range(8)]
#     board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']  # Black pieces
#     board[1] = ['p'] * 8  # Black pawns
#     board[6] = ['P'] * 8  # White pawns
#     board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']  # White pieces
#     return board

##représentation Python du plateau. Crée une fonction load_board_from_db qui retourne une matrice 8×8 

# def show_board(board):
#     for line in board:
#         print(' '.join(['.' if case == '' else case for case in line]))
#     print()

def load_board_from_db(conn, game_id):
    # 🇫🇷 Initialise un plateau vide
    board = [['' for _ in range(8)] for _ in range(8)]
    cur = conn.cursor()
    # 🇫🇷 Récupère toutes les pièces de la partie
    cur.execute("SELECT type, color, row, col FROM pieces WHERE game_id=?", (game_id,))
    for typ, color, row, col in cur.fetchall():
        symbol = {'king':'K','queen':'Q','rook':'R','bishop':'B','knight':'N','pawn':'P'}[typ]
        # 🇫🇷 majuscule pour white, minuscule pour black
        board[8-row][col-1] = symbol if color=='white' else symbol.lower()
    return board

##Afficher le plateau: On adapte show_board pour qu’elle prenne la matrice renvoyée

def show_board(board, indent=4):
    margin = " " * indent

    # 1) Affiche les entêtes abc… en bleu gras
    header = "".join(f"{Ansi.BOLD}{Ansi.BLUE}{c}{Ansi.RESET} " for c in "abcdefgh")
    print(margin + "  " + header)

    # 2) Parcours chaque rangée
    for i, rank in enumerate(board, start=1):
        row_label = f"{Ansi.BOLD}{Ansi.CYAN}{9-i}{Ansi.RESET}"

        cells = []
        for cell in rank:
            # -- Décide d’abord ce qu’on affiche : pièce ou point
            disp = cell if cell else '.'

            # -- Puis on choisit la couleur :
            if disp == '.':
                # point vide en gris foncé
                colored = f"{Ansi.DIM}.{Ansi.RESET}"
            elif disp.isupper():
                # pièce blanche en jaune
                colored = f"{Ansi.YELLOW}{disp}{Ansi.RESET}"
            else:
                # pièce noire en magenta
                colored = f"{Ansi.MAGENTA}{disp}{Ansi.RESET}"

            # ajoute un espace séparateur
            cells.append(colored + " ")

        # 3) Affiche la ligne complète, avec marge à gauche
        print(margin + row_label + " " + "".join(cells))

    # 4) Ligne vide en bas pour respirer
    print()


def transform_input(moove):
    try:
        depart, arrivee = moove.split()
        if len(depart) != 2 or len(arrivee) != 2:
            raise ValueError
        col_depart = ord(depart[0]) - ord('a')
        row_depart = 8 - int(depart[1])
        col_arrivee = ord(arrivee[0]) - ord('a')
        row_arrivee = 8 - int(arrivee[1])
        return (row_depart, col_depart), (row_arrivee, col_arrivee)
    except Exception:
        raise ValueError("Invalid move format.'")

#Valider un coup en BDD

def valid_moove(board, coords, piece):
    (from_row, from_col), (to_row, to_col) = coords
    direction = -1 if piece.isupper() else 1

    delta_row = to_row - from_row
    delta_col = to_col - from_col

    def is_opponent(target):
        return target != '' and piece.isupper() != target.isupper()

    # Pawn
    if piece.lower() == 'p':
        if delta_col == 0:
            if delta_row == direction and board[to_row][to_col] == '':
                return True
            if delta_row == 2 * direction and from_row in (6, 1) and board[to_row][to_col] == '' and board[from_row + direction][to_col] == '':
                return True
        if abs(delta_col) == 1 and delta_row == direction and is_opponent(board[to_row][to_col]):
            return True

    # Rook
    if piece.lower() == 'r':
        if from_row == to_row or from_col == to_col:
            step_row = (to_row - from_row) // max(1, abs(to_row - from_row)) if from_row != to_row else 0
            step_col = (to_col - from_col) // max(1, abs(to_col - from_col)) if from_col != to_col else 0
            row, col = from_row + step_row, from_col + step_col
            while (row, col) != (to_row, to_col):
                if board[row][col] != '':
                    return False
                row += step_row
                col += step_col
            return board[to_row][to_col] == '' or is_opponent(board[to_row][to_col])

    # Knight
    if piece.lower() == 'n':
        if (abs(delta_row), abs(delta_col)) in [(2, 1), (1, 2)]:
            return board[to_row][to_col] == '' or is_opponent(board[to_row][to_col])

    # Bishop
    if piece.lower() == 'b':
        if abs(delta_row) == abs(delta_col):
            step_row = (to_row - from_row) // abs(delta_row)
            step_col = (to_col - from_col) // abs(delta_col)
            row, col = from_row + step_row, from_col + step_col
            while (row, col) != (to_row, to_col):
                if board[row][col] != '':
                    return False
                row += step_row
                col += step_col
            return board[to_row][to_col] == '' or is_opponent(board[to_row][to_col])

    # Queen
    if piece.lower() == 'q':
        if abs(delta_row) == abs(delta_col) or from_row == to_row or from_col == to_col:
            step_row = (to_row - from_row) // max(1, abs(to_row - from_row)) if delta_row != 0 else 0
            step_col = (to_col - from_col) // max(1, abs(to_col - from_col)) if delta_col != 0 else 0
            row, col = from_row + step_row, from_col + step_col
            while (row, col) != (to_row, to_col):
                if board[row][col] != '':
                    return False
                row += step_row
                col += step_col
            return board[to_row][to_col] == '' or is_opponent(board[to_row][to_col])

    # King
    if piece.lower() == 'k':
        if abs(delta_row) <= 1 and abs(delta_col) <= 1:
            return board[to_row][to_col] == '' or is_opponent(board[to_row][to_col])

    return False

#enregistrer un coup en BDD

def make_move_db(conn, game_id, from_rc, to_rc):
    fr, fc = from_rc
    tr, tc = to_rc
    cur = conn.cursor()
    # 🇫🇷 Trouver la pièce déplacée
    cur.execute(
        "SELECT piece_id FROM pieces WHERE game_id=? AND row=? AND col=?",
        (game_id, 8-fr, fc+1)  # conversion inverse ligne/col
    )
    res = cur.fetchone()
    if not res:
        return False
    pid = res[0]

    # 🇫🇷 Chercher une éventuelle capture
    cur.execute(
        "SELECT piece_id FROM pieces WHERE game_id=? AND row=? AND col=?",
        (game_id, 8-tr, tc+1)
    )
    cap = cur.fetchone()
    cap_id = cap[0] if cap else None

    # 🇫🇷 Insérer dans moves
    cur.execute(
        """INSERT INTO moves(game_id,piece_id,from_row,from_col,to_row,to_col,captured_piece_id)
            VALUES(?,?,?,?,?,?,?)""",
        (game_id, pid, fr, fc, tr, tc, cap_id)
    )
    # 🇫🇷 Mettre à jour la table pieces
    cur.execute(
        "UPDATE pieces SET row=?,col=?,has_moved=1 WHERE piece_id=?",
        (8-tr, tc+1, pid)
    )
    # 🇫🇷 Supprimer la pièce capturée
    if cap_id:
        cur.execute("DELETE FROM pieces WHERE piece_id=?", (cap_id,))
    conn.commit()
    return True


# def play_moove(board, coords):
#     (from_row, from_col), (to_row, to_col) = coords
#     piece = board[from_row][from_col]

#     if piece == '':
#         print("Error: no piece to move here.")
#         return

#     if not valid_moove(board, coords, piece):
#         print("Invalid move for this piece.")
#         return

#     board[to_row][to_col] = piece
#     board[from_row][from_col] = ''


# Boucle principale
def play_game():
    conn = init_db("pawn_to_king.db")
    game_id = start_new_game(conn)

    while True:
        board = load_board_from_db(conn, game_id)
        show_board(board)
        inp = input("Your move (ex : e2 e4) ou 'quit' : ")
        if inp.lower()=="quit":
            print("GG! The next chessboard! 🎉")
            break
        try:
            coords = transform_input(inp)
            fr, fc = coords[0]
            piece = board[fr][fc]
            if not piece:
                print("Empty box! Repeat.")
                continue
            if not valid_moove(board, coords, piece):
                print("Invalid movement for this type.")
                continue
            # 🇫🇷 On enregistre le coup en BDD
            make_move_db(conn, game_id, coords[0], coords[1])
        except ValueError as e:
            print("Invalid format. Tap something like 'e2 e4'.")


##main qui : 1. Ouvre ta base. 2. Lance une nouvelle partie, 3. Charge le plateau depuis la BDD, 4. L’affiche (ou autre contrôle)


if __name__ == "__main__":
    # 0. Supprime l’ancienne .db manuellement si besoin
    conn = init_db("pawn_to_king.db")
    # 1. Connexion et création des tables
    conn = init_db("pawn_to_king.db")
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    ).fetchall()
    print("🕵️‍♂️ SQLite tables:", tables)

    # 2. Démarrer une nouvelle partie et insérer les pièces
    game_id = start_new_game(conn)

    # 3. Charger le plateau actuel depuis la BDD
    board = load_board_from_db(conn, game_id)

    # 4. Afficher ce plateau
    show_board(board)

    print("Number of playing pieces in base: 32 :", conn.execute("SELECT COUNT(*) FROM pieces").fetchone()[0])
    
    play_game()

