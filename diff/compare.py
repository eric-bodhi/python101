#!/usr/bin/env python3
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Incorrect # of inputs")
        exit()

    def checkPath(path: str):
        if os.path.isfile(path):
            return path

        print("Incorrect file (path): " + path)
        exit()

    file1 = checkPath(sys.argv[1])
    file2 = checkPath(sys.argv[2])

    def readFile(file):
        with open(file, 'r') as f:
            lines = f.readlines()

        for i in range(len(lines)):
            if lines[i].endswith("\n"):
                lines[i] = lines[i][:-1]

        return lines

    lines1 = readFile(file1)
    lines2 = readFile(file2)

    red = "\033[31m"    # Darker red color
    green = "\033[32m"  # Darker green color
    white = "\033[97m"  # White color
    reset = "\033[0m"  # Reset color formatting

    red_highlight = "\033[101m"       # Lighter red color
    green_highlight = "\033[102m"     # Lighter green color

    print(white)
    for (l1, l2) in zip(lines1, lines2):
        if l1 != l2:
            print("- " + red + l1 + white)
            print("+ " + green + l2 + white)

        else:
            print("= " + white + l1)

    print(reset)  # Reset back to terminal's color