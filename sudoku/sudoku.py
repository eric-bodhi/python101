#!/usr/bin/env python3
import random
import generator
import validSudoku
import time

solved_board = generator.generate()

difficulty = input("Choose a difficulty (Easy, Medium, Hard, Impossible \n").lower()
while difficulty != "easy" and difficulty != "medium" and difficulty != "hard" and difficulty != "impossible":
    difficulty = input("Error! Choose a difficulty. (Easy, Medium, Hard, Impossible \n").lower()

input("Ok are you ready to start? Make sure to read the readme instructions on github! Press any key to begin \n")
if difficulty == "easy":
    difficulty = 30

elif difficulty == "medium":
    difficulty = 50

elif difficulty == "hard":
    difficulty = 60

else:
    difficulty = 80

def make_playable(board):
    for i in random.sample(range(81), difficulty):
        board[i//9][i%9] = 0
    
    return board

board =  list(map(list, solved_board))

def make_playable(board):
    for i in random.sample(range(81), difficulty):
        board[i//9][i%9] = 0
    
    return board

board = make_playable(board)

def printBoard(board):
    base  = 3
    side  = base*base   
    def expandLine(line):
        return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]
    line0  = expandLine("╔═══╤═══╦═══╗")
    line1  = expandLine("║ . │ . ║ . ║")
    line2  = expandLine("╟───┼───╫───╢")
    line3  = expandLine("╠═══╪═══╬═══╣")
    line4  = expandLine("╚═══╧═══╩═══╝")

    symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums   = [ [""]+[symbol[n] for n in row] for row in board ]
    print(line0)
    for r in range(1,side+1):
        print("".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
        print([line2,line3,line4][(r%side==0)+(r%base==0)])

def add(row, col, num):
    prev = board[row-1][col-1]
    if prev != 0 and solved_board[row-1][col-1] != num:
        print("Don't change it! It was the correct number already!")
        return False

    board[row-1][col-1] = num
    if validSudoku.isValidSudoku(board):
        print("Successfully changed " + str(prev) + " to " + str(num) + "!")
        return True

    else:
        print("The number you changed has made the sudoku invalid!")
        time.sleep(1)
        board[row-1][col-1] = prev
        print("Reversed!")
        return False

        e
def remove(row, col):
    prev = board[row-1][col-1]
    if prev == 0:
        print("No number there why are you removing it!")
        return False
    if solved_board[row-1][col-1] == prev:
        print("Oops! That was the correct placement, dont remove it!")
        print("------------------------------------------")
        return False

    else:
        board[row-1][col-1] = 0


    if validSudoku.isValidSudoku(board):
        print("Successfully removed!")
        return True
    else:
        board[row-1][col-1] = prev
        print("The number you removed made the sudoku invalid, *reversing what you've done*")
        time.sleep(1)
        print("Done!")
        print("------------------------------------------")
        return False

def isSolved(board):
    for line in board:
        if 0 in line:
            return False
    
    return True and validSudoku.isValidSudoku(board)

def validResponse(response):
    def validNum(num):
        return int(num) > 0 and int(num) < 10
    
    if response.lower() == "q":
        return True

    if len(response) != 3 or not all([response[i].isnumeric() for i in range(3)]):
        return False

    return all([validNum(response[i]) for i in range(2)]) and int(response[2]) > -1 and int(response[2]) < 10

def game():
    printBoard(board)
    while not isSolved(board):
        response = input(" ...What would you like to do? R/C/N. Input row, column, number. E.g. 223. Add 2 at row 3 and column 2. If there is already a number at your coordinates then it will overide that number placing your input there instead.. Last number should be 0 if you would like to remove, q is to quit... \n")
        while not validResponse(response):
            response = input("Error! What would you like to do? R/C/N. Input row, column, number. Last number should be 0 if you would like to remove. \n")

        if response.lower() == "q":
            print("You quit!")
            return

        row = int(response[0])
        col = int(response[1])
        num = int(response[2])

        if num == 0:
            remove(row, col)

        else:
            add(row, col, num)
        
        printBoard(board)

game()
if isSolved(board):
    print("Congrats! You have solved your sudoku!")
else:
    print("This is the correct solution")
    printBoard(solved_board)