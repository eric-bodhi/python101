#if you or your opponent has two in a row plan on the remaining square
#otherwise if there's a move that creates two lines of two in a row play that
#otherwise if the center square is free play there
#otherwise if your opponent has played in a corner plan in the opposite corner
#otherwise if there's an empty corner play there
#otherwise play any empty square
'''
make everything into a grid of 
    "-" for empty (or 0)
    "x" for not empty (or 1)
find a line of 2

if that line is vertical
    if that line is in the middle
        look to the left to find another "x"
            if that "x" is in the middle cell
                copy the original line of 2 to the left # there is probably a better way to do this
            otherwise
                play the middle cell 
        look to the right to find another "x"
            if that "x" is in the middle cell
                copy the original line of 2 to the right
            otherwise
                play the middle cell 
    otherwise
        look at the middle to find another "x"
            if that "x" is in the middle cell
                copy the original line of 2 to the middle
            otherwise
                play the middle cell
otherwise
    if that line is in the middle
        look up to find another "x"
            if that "x" is in the middle cell
                copy the original line of 2 up
            otherwise
                play the middle cell 
        look down to find another "x"
            if that "x" is in the middle cell
                copy the original line of 2 down
            otherwise
                play the middle cell 
    otherwise
        look at the middle to find another "x"
            if that "x" is in the middle cell
                copy the original line of 2 to the middle
            otherwise
                play the middle cell'''

#print the board function, utilized each time
#get() function, basically returns x,y axis
board = ['-','-','-','-','-','-','-','-','-']

def get(row, col):
    return 3*row+col
def printBoard(board):
    print(f"""
     |     |     
  {board[get(0, 0)]}  |  {board[get(0, 1)]}  |  {board[get(0, 2)]}  
_____|_____|_____
     |     |     
  {board[get(1, 0)]}  |  {board[get(1, 1)]}  |  {board[get(1, 2)]}  
_____|_____|_____
     |     |     
  {board[get(2,0)]}  |  {board[get(2, 1)]}  |  {board[get(2, 2)]}
     |     |  """)

def isWin(p1, p2, p3):
    return p1 == p2 and p2 == p3

def vertical(turn):
    return all([board[get(0, 0)] == turn, board[get(1, 0)] == turn, board[get(2, 0)] == turn]) or all([board[get(0, 1)] == turn, board[get(1, 1)] == turn, board[get(2, 1)] == turn]) or all([board[get(0, 2)] == turn, board[get(1, 2)] == turn, board[get(2, 2)] == turn])

def horizontal(turn):
    return all([board[get(0, 0)] == turn, board[get(0, 1)] == turn, board[get(0, 2)] == turn]) or all([board[get(1, 0)] == turn, board[get(1, 1)] == turn, board[get(1, 2)] == turn]) or all([board[get(2, 0)] == turn, board[get(2, 1)] == turn, board[get(2, 2)] == turn])

def diagonal(turn):
    return all([board[get(0, 0)] == turn, board[get(1, 1)] == turn, board[get(2, 2)] == turn]) or all([board[get(0, 2)] == turn, board[get(1, 1)] == turn, board[get(2, 0)] == turn])

def playerWin(turn):
    return any([vertical(turn), horizontal(turn), diagonal(turn)])

def changeTurn(turn):
    return False if turn else True

def isTie():
    for i in board:
        if i == "-":
            return False
    return True
    
turn = True
printBoard(board)
while not playerWin("X") and not playerWin("0") and not isTie():
    if turn: #player turn
        i = input("Player x's turn, where do you pick?:\n")
        if not i.isnumeric() or int(i) > 9 or int(i) < 1:
            i = input("Try again, invalid input.\n")
        board[int(i) - 1] = "X"
    if not turn: #bot turn
        
        board[int(i) - 1] = "0"
    printBoard(board)
    turn = changeTurn(turn)

if isTie():
    print("Tie!")
elif playerWin("X"):
    print("Player X wins!")
elif playerWin("0"):
    print("Player 0 wins!")