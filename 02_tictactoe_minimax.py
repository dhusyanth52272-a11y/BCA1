# Minimax Algorithm - Tic Tac Toe
import math

board = [' ' for _ in range(9)]

# Print Board
def print_board():
    print("\n")
    for i in range(9):
        print(f"|{board[i]}", end="")
        if (i + 1) % 3 == 0:
            print("|")
            if i < 6:
                print("---------")

# Check Winner
def check_winner(player):
    win_position = [
        [0, 1, 2], [3, 4, 5],
        [6, 7, 8], [0, 3, 6],
        [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for pos in win_position:
        if (board[pos[0]] == player and
                board[pos[1]] == player and
                board[pos[2]] == player):
            return True
    return False

# Minimax
def minimax(is_maximizing):
    if check_winner('X'):
        return 1
    if check_winner('O'):
        return -1
    if ' ' not in board:
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'X'

# Player Move
def player_move():
    while True:
        move = int(input("Enter your position (1-9): "))
        if move < 1 or move > 9:
            print("Invalid position!")
            continue
        move = move - 1
        if board[move] != ' ':
            print("Position already occupied!")
            continue
        board[move] = 'O'
        break

# Main Program
print("TIC TAC TOE")
print("You are O")
print("AI is X")
print("\nPosition:")
print("1 | 2 | 3")
print("---------")
print("4 | 5 | 6")
print("---------")
print("7 | 8 | 9")

while True:
    # Player Move
    player_move()
    print_board()

    # Check Player Winner
    if check_winner('O'):
        print("You win!")
        break

    # Check Draw
    if ' ' not in board:
        print("Draw!")
        break

    # AI Move
    print("AI is thinking...")
    ai_move()
    print_board()

    # Check AI Winner
    if check_winner('X'):
        print("AI wins!")
        break

    # Check Draw
    if ' ' not in board:
        print("Draw!")
        break

# Sample Output:
# Enter your position (1-9): 3
# | | |O|
# ---------
# | | | |
# ---------
# | | | |
# AI is thinking...
# | | |O|
# ---------
# | |X| |
# ---------
# | | | |
# ... (game continues until AI wins)
