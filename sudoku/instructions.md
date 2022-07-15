# Instructions on how to play Sudoku

## How to start the game
In order to start the puzzle you are to download the file and to execute the file in your terminal/command line with the command ./sudoku.py
This will execute the file starting the game!

The puzzle download download is right here: https://codeload.github.com/Bodhi2011/python101/zip/refs/heads/main
## How to actually play the game
The goal of sudoku is to have all numbers 1-9 in every row, column, and 3x3 square.
The problem of the game is achieving this without have more than one instance of a number in every row, column, and square. 
As in, I could not a have 2 3's in one row. 
An example of a solved sudoku:
https://www.7sudoku.com/images/examples/solved_puzzle.png
The way the puzzle works is (depending on your difficulty) a certain number of squares are taken away. You have to fill those squares accordingly.
If you want to **add** a number to a square the format is "add [number you want to add] at [row, col]".
The **same** format with **remove**
"remove [number you want to remove] at [row,col]"

If you add a number to invalidate the sudoku then it will reverse what you've done.
If you remove a number that was in the correct spot, it will reverse what you've done. 
Please report any bugs to erixefb@gmail.com
