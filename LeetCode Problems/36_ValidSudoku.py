#!/usr/bin/env python3

from multiprocessing import cpu_count
import sys

class Solution:
    def validUnit(self, unit):
        unit = "".join([i for i in unit if i != "."])
        return len(set(unit)) == len(unit)
    
    def validRows(self, board):
        for i in board:
            if not self.validUnit(i):
                return False
        return True
    
    def validCols(self, board):
        for i in zip(*board):
            if not self.validUnit(i) :
                return False
        return True
    
    def validSquares(self, board):
        for i in range(3, 10, 3):
            for j in range(3, 10, 3):
                square = board[i-3][j-3:j] + board[i-2][j-3:j] + board[i-1][j-3:j]
                if not self.validUnit(square):
                        return False
        return True
    
    def isValidSudoku(self, board):
        return self.validRows(board) and self.validCols(board) and self.validSquares(board)

validSudoku = Solution()
def test():
    count = 2
    if validSudoku.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]) != True:
        print("Test failed, Testcase: [[5,3,.,.,7,.,.,.,.],[6,.,.,1,9,5,.,.,.],[.,9,8,.,.,.,.,6,.],[8,.,.,.,6,.,.,.,3],[4,.,.,8,.,3,.,.,1],[7,.,.,.,2,.,.,.,6],[.,6,.,.,.,.,2,8,.],[.,.,.,4,1,9,.,.,5],[.,.,.,.,8,.,.,7,9]] -> False")
        count -= 1 

    if validSudoku.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]) != False:
        print("Test failed, Testcase: [[8,3,.,.,7,.,.,.,.],[6,.,.,1,9,5,.,.,.],[.,9,8,.,.,.,.,6,.],[8,.,.,.,6,.,.,.,3],[4,.,.,8,.,3,.,.,1],[7,.,.,.,2,.,.,.,6],[.,6,.,.,.,.,2,8,.],[.,.,.,4,1,9,.,.,5],[.,.,.,.,8,.,.,7,9]] -> True")
        count -= 1
    
    if count == 2:
        print("All Testcases passed")
    
if len(sys.argv) < 2:
    test()
else:
    for i in [validSudoku.isValidSudoku(sys.argv[1:])]:
        if not i:
            print("Not a valid sudoku board")
        else:
            print("Valid sudoku board")
    test()
