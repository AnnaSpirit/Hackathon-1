def init_board():
    board = [['' for _ in range(8)] for _ in range(8)]
    board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']       ## pièces noires (r = rook = tour, n = knight = cavalier, etc)
    board[1] = ['p'] * 8                                      ##  pions noirs
    board[6] = ['P'] * 8                                      ##  pions blancs
    board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']       ##  pièces blanches
    return board                   ##pour reutiliser plus facilement le tableau de base quand jen aurais besoin


#rajoute des points au endroits vide pour que ca ressemble plus a un echeqiet et ensuite je l'affiche- ligne 20
def show_board(init_board):
    for line in init_board:
        print(' '.join(['.' if case == '' else case for case in line]))

board = init_board()

show_board(board)


## transforme une saisie d'utilisateur comme "e5 e5" en coordonnees utilisables dans mon board
def tranform_input(moove):
    depart, arivale = moove.split()  
    col_depart = ord(depart[0]) - ord('a')
    row_depart = 8 - int(depart[1])
    col_arivale = ord(arivale[0]) - ord('a')
    row_arivale = 8 - int(arivale[1])
    return (row_depart, col_depart), (row_arivale, col_arivale)


moove = input('Enter a moove : ')
coords = tranform_input(moove)

print("Python coordonates :", coords)



## creation de la fonction qui fera les deplacements

def play_moove(board, coords):
    (from_row, from_col), (to_row, to_col) = coords          #from_row et from_col = ligne et colonne de depart.    #to_row et to_col = ligne et colonne d’arrivee


    piece = board[from_row][from_col]

    if piece == '':
        print("Error : no piece to move here.")
        return

    board[to_row][to_col] = piece
    board[from_row][from_col] = ''

    board[to_row][to_col] = piece
    board[from_row][from_col] = ''


try:
    coords = tranform_input(moove)
    play_moove(board, coords)
    show_board(board)
except ValueError:
    print("Invalid format. Enter a moove like 'e5 e5'.")


while True:
    show_board(board)  # Affiche le plateau à chaque tour
    moove = input("Enter a moove or 'quit' for quit : ")

    if moove.lower() == 'quit':
        print("End of the game. See you soon! ")
        break

    try:
        coords = tranform_input(moove)
        play_moove(board, coords)
    except ValueError:
        print("Invalid format. Enter a moove like 'e5 e5'.")
