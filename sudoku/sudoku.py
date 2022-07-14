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
    if num > 9 or num < 1:
        print("Oops! Number has to be between 1-9")
        return False

    prev = board[row-1][col-1]
    if prev == 0:
        board[row-1][col-1] = int(num)
    else:
        print("Oops! There's already a number there!")
        print("------------------------------------------")
        return False
    

    if validSudoku.isValidSudoku(board):
        return True
    else:
        print("The number you added made the sudoku invalid, *reversing what you've done*")
        time.sleep(1)
        print("Reversed!")
        print("------------------------------------------")
        board[row-1][col-1] = prev
        return False

def remove(row, col):
    prev = board[row-1][col-1]
    if solved_board[row-1][col-1] == prev:
        print("Oops! That was the correct placement, dont remove it!")
        print("------------------------------------------")

    else:
        board[row-1][col-1] = 0

    if validSudoku.isValidSudoku(board):
        return True
    else:
        board[row-1][col-1] = prev
        print("The number you removed made the sudoku invalid, *reversing what you've done*")
        time.sleep(1)
        print("Done!")
        print("You only have {} left!".format())
        print("------------------------------------------")
        return False

def isSolved(board):
    for line in board:
        if 0 in line:
            return False
    
    return True and validSudoku.isValidSudoku(board)



def game():
    printBoard(board)
    while not isSolved(board):
        response = input("What would you like to do? ([add/remove] [number] at [row,col]) **ADD SPACES TO SEPERATE INPUTS** Type quit to quit. \n").lower().split()

        if response != []:
            print(response[0])
            if response[0] == "quit":
                print("You quit!")
                return 

        while response == [] or len(response) != 4 or len(response[3]) != 3:
            response = input("Invalid input. What would you like to do? ([add/remove] [number] at [row,col]) **ADD SPACES TO SEPERATE INPUTS** Type quit to quit \n").lower().split()

        while response[0] != "add" and response[0] != "remove" and not response[1].isnumeric() and int(response[1]) > 0 and int(response[1]) < 10 and int(response[3][0]) > 0 and int(response[3][0]) < 10 and int(response[3][2]) > 0 and int(response[3][2]) < 10 and len(response[1]) != 1 and len(response[3]) != 3:
            response = input("Invalid input. What would you like to do? ([add/remove] [number] at [row,col]) **ADD SPACES TO SEPERATE INPUTS** Type quit to quit \n").lower().split()

        action = response[0]
        num = response[1]
        cords = response[3]

        if action == "add":
            if add(int(cords[0]), int(cords[2]), int(num)):
                print("Added {num} at row {row}, col {col} succesfully!".format(num=num, row=cords[0], col=cords[2]))

        else:
            if remove(int(cords[0]), int(cords[2])):
                print("Removed {num} at row {row}, col {col} succesfully!".format(num=num, row=cords[0], col=cords[2]))


        """
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

        cords = input("Where would you like to {response}? (row,col) 1-9, 1-9: \n".format(response=response))
        x = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        while len(cords) != 3 and cords[0] not in x and cords[2] not in x and board[cords[0]][cords[2] != 0]:
            cords = input("Error, try again, where would you like to {response}? (row,col) 1-9, 1-9: \n".format(response=response))
            print("------------------------------------------")

        


        if response == "add":
            num = input("What would you like to add? Has to be a number between 1-9 \n")
            while not num.isnumeric() and int(num) and 9 and int(num) < 1:
                num = input("Error! Please provide a valid input. What would you like to {}? Has to be a number between 1-9 \n".format(response))
            if add(int(cords[0]), int(cords[2]), int(num)):
                print("You've successfuly added {num} at row {row} and col {col}.".format(num=num, row=cords[0], col=cords[2]))
                print("------------------------------------------")
            
        if response == "remove":
            if remove(int(cords[0]), int(cords[2])):
                print("You've successfuly removed the number at row {row} and col {col}.".format(row=cords[0], col=cords[2]))
                print("------------------------------------------")

        """
        time.sleep(1)
        printBoard(board)

game()
if isSolved(board):
    print("Congrats! You have solved your sudoku!")
else:
    print("This is the correct solution")
    printBoard(solved_board)
