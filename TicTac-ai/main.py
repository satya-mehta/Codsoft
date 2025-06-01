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