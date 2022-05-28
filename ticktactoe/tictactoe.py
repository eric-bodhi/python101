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
    if turn:
        i = input("Player x's turn, where do you pick?:")
        if not i.isnumeric() or int(i) > 9 or int(i) < 1:
            i = input("Try again, invalid input.")
        board[int(i) - 1] = "X"
    if not turn:
        i = input("Player 0's turn, where do you pick?:")
        if not i.isnumeric() or int(i) > 9 or int(i) < 1:
            i = input("Try again, invalid input.")
        board[int(i) - 1] = "0"
    printBoard(board)
    turn = changeTurn(turn)

if isTie():
    print("Tie!")
elif playerWin("X"):
    print("Player X wins!")
elif playerWin("0"):
    print("Player 0 wins!")