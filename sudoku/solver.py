#!/usr/bin/env python3
import logging as log
from validSudoku import isValidSudoku
from generator import generate
from random import sample

log.basicConfig(format="%(levelname)s:%(message)s", level=log.DEBUG)

#Helper Functions
def make_playable(board):
    for i in sample(range(81), 5):
        board[i//9][i%9] = 0
    
    return board

def cords(row, col):
    return [(row-1)//3, (col-1)//3]

def possibleRow(row, col, num, board):
    row = board[row]
    return num not in row and row[col] == 0

def possibleCol(row, col, num, board):
    line = [board[i][col] for i in range(9)]
    print(line)
    return num not in line and line[row] == 0

def possibleSquare(row, col, num, board):
    r, c = cords(row+1, col+1)[0] * 3, cords(row+1, col+1)[1] * 3
    square = sum([board[r+i][c:c+3] for i in range(3)], [])
    log.debug()
    return num not in square and board[row][col] == 0


solved_board = generate()
board = make_playable(solved_board)
prev_board = board[:]
print("hi")
