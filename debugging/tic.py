#!/usr/bin/python3
def print_board(board):
    """
    Affiche le tableau du jeu de morpion.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Vérifie si un joueur a gagné.

    Paramètres :
    board (list): Le tableau de jeu 3x3.

    Retourne :
    bool: True si un joueur a gagné, sinon False.
    """
    # Vérifier les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifier les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifier les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def get_valid_input(board):
    """
    Demande à l'utilisateur de saisir une ligne et une colonne valides.

    Paramètres :
    board (list): Le tableau du jeu.

    Retourne :
    tuple: Une paire de coordonnées valides (row, col).
    """
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            # Vérifie que les indices sont dans la plage valide
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue

            # Vérifie que la case n'est pas déjà occupée
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            return row, col

        except ValueError:
            print("Invalid input. Please enter numbers only.")

def tic_tac_toe():
    """
    Fonction principale pour jouer au morpion.
    """
    board = [[" "]*3 for _ in range(3)]  # Création du plateau de jeu vide
    player = "X"  # Le joueur X commence

    while not check_winner(board):
        print_board(board)

        # Demande à l'utilisateur de saisir des coordonnées valides
        row, col = get_valid_input(board)

        # Place le symbole du joueur sur le tableau
        board[row][col] = player

        # Change de joueur
        player = "O" if player == "X" else "X"

    print_board(board)
    print(f"Player {player} wins!")

# Démarre le jeu
tic_tac_toe()

"""
Changements apportés :
Fonction get_valid_input(board) : Cette fonction demande à l'utilisateur de saisir une ligne et une colonne. Elle vérifie :

Si les valeurs saisies sont dans la plage correcte (0, 1, ou 2).

Si la case n'est pas déjà occupée.

Si l'utilisateur entre des valeurs valides (en cas de texte ou de caractères non numériques, un message d'erreur est affiché).

Gestion des erreurs :

Si un utilisateur entre une valeur incorrecte (par exemple, une lettre au lieu d'un nombre), le programme demande à nouveau une entrée valide.

Si la case choisie est déjà occupée, l'utilisateur est invité à essayer à nouveau.
"""
