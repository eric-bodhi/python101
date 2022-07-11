from typing import List
import random

# Declare global 2d array for sudoku board
sudoku_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# Print sudoku board
def print_sudoku(sudoku_board: List[List[int]]) -> None:
    for row in sudoku_board:
	    for col in row:
			print(str(col) + '  ', end='')
		print('')
	print('')


# Check if sudoku board follows rules of sudoku
def check_valid_sudoku(sudoku_board: List[List[int]]) -> bool:
    # Check each row for duplicates
    for row in range(9):
        row_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            if sudoku_board[row][i] == row_values[sudoku_board[row][i]] and sudoku_board[row][i] != 0:
                return False
            else:
                row_values[sudoku_board[row][i]] = sudoku_board[row][i]

    # Check each column for duplicates
    for col in range(9):
        col_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            if sudoku_board[i][col] == col_values[sudoku_board[i][col]] and sudoku_board[i][col] != 0:
                return False
            else:
                col_values[sudoku_board[i][col]] = sudoku_board[i][col]

    # Check each box for duplicates
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            box_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(3):
                for j in range(3):
                    if sudoku_board[row + i][col + j] == box_values[sudoku_board[row + i][col + j]] \
                            and sudoku_board[row + i][col + j] != 0:
                        return False
                    else:
                        box_values[sudoku_board[row + i][col + j]] = sudoku_board[row + i][col + j]

    # Sudoku board is valid
    return True


# Add random box entries
def random_box(sudoku_board: List[List[int]]) -> None:
    used_num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            i = random.randint(0, 2)
            j = random.randint(0, 2)

            while sudoku_board[row + i][col + j] == 0:
                new_value = random.randint(1, 9)
                
		if used_num[new_value] == 0:
                    sudoku_board[row + i][col + j] = new_value
                    used_num[new_value] = 1


def shift_values(sudoku_board: List[List[int]], cord: List[int]) -> bool:
    for i in range(9):
        for j in range(9):
            if sudoku_board[i][j] == 0:
                cord[0] = i
                cord[1] = j

                return True

    return False


def can_it_be_placed(sudoku_board: List[List[int]], row: int, col: int, num: int) -> bool:

    # Check Row
    for i in range(9):
        if sudoku_board[row][i] == num:
            return False

    # Check Column
    for i in range(9):
        if sudoku_board[i][col] == num:
            return False

    # Check Box
    r = row - (row % 3)
    c = col - (col % 3)

    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if sudoku_board[i][j] == num:
                return False

    return True


def sudoku_solution(sudoku_board: List[List[int]]) -> int:

    cord = [0, 0]

    if not shift_values(sudoku_board, cord):
        return 1

    row = cord[0]
    col = cord[1]

    for i in range(1, 10):
        if can_it_be_placed(sudoku_board, row, col, i):

            # Set Value
            sudoku_board[row][col] = i

            # Backtrack
            if sudoku_solution(sudoku_board) == 1:
                return 1

            sudoku_board[row][col] = 0

    return 0


# Clear boxes to allow player to solve
def remove_boxes(sudoku_board: List[List[int]], num: int) -> None:
    for loops in range(num):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        
	while sudoku_board[x][y] == 0:
            x = random.randint(0, 8)
            y = random.randint(0, 8)

        sudoku_board[x][y] = 0


def main():

    random_box(sudoku_grid)

    sudoku_solution(sudoku_grid)

    print("Welcome To Daily Sudoku")
    print()
    print("Difficulties:")
    print("Easy = 1")
    print("Medium = 2")
    print("Hard = 3")
    print("Professional = 4")
    print()

    level = input("Please Enter Your Desired Difficulty: ")

    while(level != 1 and level != 2 and level != 3 and level != 4):
        print("Input Does Not Meet Parameters Specified.")
        level = input("Please Enter Your Desired Difficulty: ")

    if level == 1:
        print("Easy")
        remove_boxes(sudoku_grid, 35)
    elif level == 2:
        print("Medium")
        remove_boxes(sudoku_grid, 45)
    elif level == 3:
        print("Hard")
        remove_boxes(sudoku_grid, 55)
    elif level == 4:
        print("Professional")
        remove_boxes(sudoku_grid, 65)

    print_sudoku(sudoku_grid)

    finished = input("Press Any Key When You are Finished and Ready for Solution.")

    sudoku_solution(sudoku_grid)

    print_sudoku(sudoku_grid)


if __name__ == '__main__':
    main()