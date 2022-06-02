"""Leetcode Prompt:
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""

from math import comb
class Solution:
    #implement nCr for pascal triangle (math.comb)
    def rowData(self, n, r):
        ret = []
        for i in range(n+1):
            r = i
            ret.append(math.comb(n, r))
        return ret
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(numRows):
            ret.append(self.rowData(i, 0))
        return ret