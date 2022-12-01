#!/usr/bin/env python3
import logging as log
import copy
from generator import generate
from os import getenv
import random
import validSudoku
log.basicConfig(format='%(asctime)s, %(msecs)03d %(levelname)s %(message)s', datefmt='%H:%M.%S', level=getenv('LOG_LEVEL', 'DEBUG'))

def make_playable(board):
    for i in random.sample(range(81), 45):
        board[i//9][i%9] = 0
    
    return board


class Cell:
    def __init__(self, row, col, val, forward):
        self.row, self.col, self.val, self.forward = row, col, val, forward

    def cords(self):
        return[(self.row)//3, (self.col)//3]

    def possibleRow(self, num):
        r = board[self.row]
        return num not in r

    def possibleCol(self, num):
        line = [board[i][self.col] for i in range(9)]
        print(line)
        return num not in line

    def possibleSquare(self, num):
        r, c = self.cords()[0] * 3, self.cords()[1] * 3
        square = sum([board[r+i][c:c+3] for i in range(3)], [])
        return num not in square

    def checkPossible(self, num):
        return all([self.possibleSquare(num), self.possibleRow(num), self.possibleCol(num)])

    def forwards(self):
        log.debug("going forwards")
        if self.row == 8 and self.col == 8:
            log.debug(((validSudoku.isValidSudoku(board), all([0 not in i for i in board])), board))
            return 
        return Cell(self.row, self.col+1, board[self.row][self.col+1], True).solve() if self.col != 8 else Cell(self.row+1, 0, board[self.row+1][0], True).solve()

    def backward(self):
        log.debug("going backwards")
        return Cell(self.row-1, 8, board[self.row-1][8], False).solve() if self.col == 0 else Cell(self.row, self.col-1, board[self.row][self.col-1], False).solve()

    def wasModified(self):
        return original[self.row][self.col] != board[self.row][self.col]

    def solve(self):
        cords = [self.row, self.col]
        log.debug((cords, self.val, self.forward, self.wasModified(), original==board))
        
        if not self.forward and not self.wasModified():
            return self.backward()

        if (self.val == 0) or (self.val != 0 and self.wasModified()):
            for i in range(self.val+1, 10):
                if self.checkPossible(i):
                    board[self.row][self.col] = i 
                    log.debug(i)
                    return self.forwards()
            log.debug("could not place")
            board[self.row][self.col] = 0
            return self.backward()
        else:
            return self.forwards()
board = make_playable(generate())
original = copy.deepcopy(board)

log.debug(sum([i.count(0) for i in board]))
log.debug(board)
c = Cell(0, 0, board[0][0], True)
c.solve()