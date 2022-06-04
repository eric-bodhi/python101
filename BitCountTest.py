#!/usr/bin/python3
import sys
from threading import Timer
import timeit
def count1(s):
    return s.count("1")
def countBits(n):
    ret = []
    for i in range(n+1):
        ret.append(count1(bin(i)[2:]))
    return ret
try:
    print("Result of function: " + str(countBits(int(sys.argv[1]))))
    print("Speed of Program after 10000 executions: " + str(timeit.timeit(stmt=lambda: countBits(int(sys.argv[1])), number=10000)))
    print("Test Passed")
except:
    print("Test Failed")
