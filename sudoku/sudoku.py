#!/usr/bin/env python3
import random
import generator
import validSudoku
import time

solved_board = generator.generate()

difficulty = input("Choose a difficulty (Easy, Medium, Hard, Impossible \n").lower()
while difficulty != "easy" and difficulty and difficulty != "medium" and difficulty != "hard" and difficulty != "impossible" and len(difficulty) == 0:
    difficulty = input("Error! Choose a difficulty. (Easy, Medium, Hard, Impossible \n").lower()

mistakes_status = input("Do you want mistakes on. Y/N (You can only make 3 mistakes before you lose) \n").lower()
if mistakes_status == "y" or "yes":
    mistakes = 3

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
    print(validSudoku.isValidSudoku(board))
    prev = board[row-1][col-1]
    if prev == 0:
        print("You've successfully added {} at row {}, col {}!").format(num, row, col)
        print("------------------------------------------")
        board[row-1][col-1] = int(num)
    else:
        print("Oops! There's already a number there!")
        print("------------------------------------------")
        return False
    

    if validSudoku.isValidSudoku(board):
        return True
    else:
        mistakes -= 1
        print("The number you added made the sudoku invalid, *reversing what you've done*")
        time.sleep(1)
        print("Done! You only have {} left!".format(mistakes))
        print("------------------------------------------")
        board[row-1][col-1] = prev
        return False

def remove(row, col):
    prev = board[row-1][col-1]
    if solved_board[row-1][col-1] == prev:
        print("Oops! That was the correct placement, dont remove it!")
        time.sleep(1)
        print("You only have {} left!".format(mistakes))
        print("------------------------------------------")

    else:
        board[row-1][col-1] = 0
        print("You've successfully removed {} at row {}, col {}.".format(prev, row, col))
        print("------------------------------------------")
    if validSudoku.isValidSudoku(board):
        return True
    else:
        board[row-1][col-1] = prev
        print("The number you removed made the sudoku invalid, *reversing what you've done*")
        time.sleep(1)
        print("Done!")
        print("You only have {} left!".format(mistakes))
        print("------------------------------------------")
        return False

def isSolved(board):
    for line in board:
        if 0 in line:
            return False
    
    return True and validSudoku.isValidSudoku(board)



def game():
    printBoard(board)
    while not isSolved(board) or (mistakes_status and mistakes == 0):
        if mistakes_status == "y":
            print("You currently have {} mistakes left.".format(mistakes))

        response = input("What would you like to do? add, remove, or quit? Not k-sensitive: \n").lower()
        print("------------------------------------------")
        if response == "quit":
            print("You quit! ")
            return

        while response != "add" and response != "remove" and response != "quit":
            response = input("Invalid input, please make sure you input add, remove or quit, not k-sensitive \n")
            if response == "quit":
                print("You quit what a loser")
                return

        cords = input("Where would you like to {}? (row,col) 1-9, 1-9: \n".format(response))
        while len(cords) != 3 and not cords[0].isnumeric() and not cords[2].isnumeric() and board[cords[0]][cords[2] != 0]:
            cords = input("Error, try again, where would you like to {}? (row,col) 1-9, 1-9: \n".format(response))
            print("-")

        


        if response == "add":
            num = input("What would you like to add? Has to be a number between 1-9 \n")
            while not num.isnumeric() and int(num) and 9 and int(num) < 1:
                num = input("Error! Please provide a valid input. What would you like to {}? Has to be a number between 1-9 \n".format(response))
            if add(int(cords[0]), int(cords[2]), int(num)):
                print("You've successfuly added {} at row {} and col {}.".format(num, cords[0], cords[2]))
                print("------------------------------------------")
            
        if response == "remove":
            if remove(int(cords[0]), int(cords[2])):
                print("You've successfuly removed the number at row {} and col {}.".format(cords[0], cords[2]))
                print("------------------------------------------")

        time.sleep(1)
        printBoard(board)

game()
if isSolved(board):
    print("Congrats! You have solved your sudoku!")
else:
    print("This is the correct solution")
    printBoard(solved_board)
