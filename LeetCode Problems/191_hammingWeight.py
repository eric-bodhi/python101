#!/usr/bin/env python3
import sys

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
    x = [hammingWeight1(0)==0, hammingWeight1(1)==1, hammingWeight1(2)==1, hammingWeight1(3)==2, hammingWeight1(500)==6]
    y = [hammingWeight2(0)==0, hammingWeight2(1)==1, hammingWeight2(2)==1, hammingWeight2(3)==2, hammingWeight2(500)==6]

    if all(x):
        print("First solution is working, all test cases passed")

    else:
        print("First solution is not working, " + str(x.count(True)) + "/5 Test cases passed.")

    if all(y):
        print("Second solution is working, all test cases passed")

    else:
        print("Second solution is not working, " + str(y.count(True)) + "/5 Test cases passed.")


print(sys.argv)