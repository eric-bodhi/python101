#!/usr/bin/env python3
import logging as log
from validSudoku import isValidSudoku
from generator import generate
from random import sample
    #Helper Functions


log.basicConfig(format="%(levelname)s:%(message)s", level=log.DEBUG)
class Sudoku:
    def __init__(self, board):
        self.board = board

    def make_playable(self):
        for i in sample(range(81), 60):
            self.board[i//9][i%9] = 0

    def validMove(self, val, row, col):
        if self.board[row][col] != 0:
            return False

        if val in self.board[row]:
            return False
            
        elif val in [i[col] for i in self.board]:
            return False
            
        for m in range((row//3) * 3, (row//3) * 3 + 3):
            for n in range((col//3) * 3, (col//3)*3 + 3):
                if (row,col) != (m,n) and self.board[m][n] == val:
                    return False
        return True
        
    def findEmptyCell(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    return (i, j)

    def solve(self):
        emptyCell = self.findEmptyCell()

        if not emptyCell:
            return board
        
        row, col = emptyCell
        for num in range(1, 10):
            if self.validMove(num, row, col):
                self.board[row][col] = num
                log.debug((board.board[row][col], (row, col)))
                if self.solve():
                    return True
            self.board[row][col] = 0
        
        return False


board = Sudoku(generate())
board.make_playable()

#log.debug(board.board)

board.solve()
log.debug(board.board)