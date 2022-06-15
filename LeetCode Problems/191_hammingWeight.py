#!/usr/bin/env python3
import timeit
import sys
import os
import psutil

"""Leetcode Prompt:
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Constraints:

The input must be a binary string of length 32.
 

Follow up: If this function is called many times, how would you optimize it?
"""
#First Solution, diagnostics: ~80% speed.
def hammingWeight1(n: int) -> int:
    return bin(n)[2:].count("1")

#Second solution, diagnostics: 97.53% speed. 
def hammingWeight2(n: int) -> int:
    count = 0
    for i in bin(n)[2:]:
        if i == "1":
            count += 1
    return count


def isWorking():
    result = True
    if hammingWeight2(5) != 2:
        result = False
        print("Battery Testcase: 5 -> " + str(hammingWeight2(5)) + ": Failed, expected 2")
    
    if hammingWeight2(15) != 4:
        result = False
        print("Battery Testcase: 15 -> " + str(hammingWeight2(15)) + ": Failed, expected 4")
    
    if hammingWeight2(321222212) != 13:
        result = False
        print("Battery Testcase: 321222212 -> " + str(hammingWeight2(321222212)) + ": Failed, expected 13")
    
    if result:
        print("All battery tests passed.")
    return result

def endResult():
    for i in sys.argv[1:]:
        print(i + " -> " + str(hammingWeight2(int(i))))

if isWorking():
    endResult()

print(str(round(timeit.timeit(stmt="lambda: endResult()", number=1000000)*1000)) + " Milliseconds after 1,000,000 executions")

process = psutil.Process(os.getpid())
print(str(process.memory_info().rss) + " bytes of memory used")  # in bytes 