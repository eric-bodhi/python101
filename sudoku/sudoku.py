import random
import generator
import validSudoku

solved_board = generator.generate()

difficulty = input("Choose a difficulty 1-4 (Easy, Medium, Hard, Impossible \n")
while not difficulty.isnumeric() or int(difficulty) < 1 or int(difficulty) > 4:
    difficulty = input("Error, please choose a number Choose a difficulty 1-4 (Easy, Medium, Hard, Impossible \n")

def make_playable(board):
    for i in range(9):
        for j in range(9):
            if difficulty == "1":
                if random.randint(1, 5) == 2:
                    board[i][j] = "."
            elif difficulty == "2":
                if random.randint(1, 3) == 2:
                    board[i][j] = "."
            elif difficulty == "3":
                if random.randint(1, 2) == 2:
                    board[i][j] = "."
            else:
                board = generator.degenerate(board)
                board[5][4] = random.randint(1, 9)
                return board
    return board

board = make_playable(solved_board)

def printBoard(board):
    print(" ----|----|----|----|----|----|----|----|---")
    for i in range(9):
        print(board[i])
        print(" ----|----|----|----|----|----|----|----|---")

solved = False

def add(row, col, num):
    prev = board[row-1][col-1]
    board[row-1][col-1] = num
    if validSudoku.isValidSudoku(board):
        return True
    else:
        board[row-1][col-1] = prev
        return False

