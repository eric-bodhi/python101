def validUnit(unit):
    unit = [i for i in unit if i != "."]
    return len(set(unit)) == len(unit)
    
def validRows(board):
    for i in board:
        if not validUnit(i):
            return False
    return True
    
def validCols(board):
    for i in zip(*board):
        if not validUnit(i) :
            return False
    return True
    
def validSquares(board):
    for i in range(3, 10, 3):
        for j in range(3, 10, 3):
            square = board[i-3][j-3:j] + board[i-2][j-3:j] + board[i-1][j-3:j]
            if not validUnit(square):
                return False
    return True
    
def isValidSudoku(board):
    return validRows(board) and validCols(board) and validSquares(board)
