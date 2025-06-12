import math

HUMAN = 'X'
AI = 'O'
EMPTY = ' '

#Initializing board
board = [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board():
    print("\n")
    for row in board:
        print("| " + " | ".join(row) + "|")
    print("\n")

def is_move_left(b):
    return any(EMPTY in row for row in b)

def evaluate(b):
    for row in b:
        if row[0] == row[1] == row[2] != EMPTY:
            return 10 if row[0] == AI else -10
    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col] != EMPTY:
            return 10 if b[0][col] == AI else -10
    
    if b[0][0] == b[1][1] == b[2][2] != EMPTY:
        return 10 if b[0][0] == AI else -10
    
    if b[0][2] == b[1][1] == b[2][0] != EMPTY:
        return 10 if b[0][2] == AI else -10
    
    return 0

def minimax(b, depth, is_max, alpha, beta):
    score = evaluate(b)

    if score == 10 or score == -10:
        return score - depth if score > 0 else score + depth
    
    if not is_move_left(b):
        return 0
    
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = AI
                    best = max(best, minimax(b, depth + 1, False, alpha, beta))
                    b[i][j] = EMPTY
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        return best
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = HUMAN
                    best = min(best, minimax(b, depth + 1, True, alpha, beta))
                    b[i][j] = EMPTY
                    beta = min(beta, best)
                    if beta <= alpha:
                        return best
        return best

def find_best_move(b):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if b[i][j] == EMPTY:
                b[i][j] = AI
                move_val = minimax(b, 0, False, -math.inf, math.inf)
                b[i][j] = EMPTY
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def check_winner():
    score = evaluate(board)
    if score == 10:
        return AI
    elif score == -10:
        return HUMAN
    elif not is_move_left(board):
        return 'Draw'
    return None

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    first = input("Do you want to go first? (y/n): ").lower() == 'y'
    print_board()

    while True:
        if first:
            move = input("Enter your move (row col): ").split()
            if len(move) != 2 or not all(i.isdigit() for i in move):
                print("Invalid input. Try again. Ex: 0 1")
                continue

            x, y = map(int, move)
            if x not in range(3) or y not in range(3) or board[x][y] != EMPTY:
                print("Invalid move. Try again.")
                continue
            board[x][y] = HUMAN
        else:
            print("AI's Turn:")
            x, y = find_best_move(board)
            board[x][y] = AI

        print_board()
        winner = check_winner()
        if winner:
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

        first = not first

#begin
play_game()