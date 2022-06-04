#!/usr/bin/python3
#Imports
import sys
from threading import Timer
import timeit

#Helper Function, returns number of 1's in s.
def count1(s):
    return s.count("1")

#Main function, counts bits in range of n+1 returning an array of those counts.
def countBits(n):
    ret = []
    for i in range(n+1):
        ret.append(count1(bin(i)[2:]))
    return ret

#Edge cases, if no parameters passed, etc. Includes speed as well!
try:
    print("Result of function: " + str(countBits(int(sys.argv[1]))))
    print("Speed of Program after 10000 executions: " + str(timeit.timeit(stmt=lambda: countBits(int(sys.argv[1])), number=10000)))
    print("Test Passed")
    
except:
    print("Test Failed")
