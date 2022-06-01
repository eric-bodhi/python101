class Solution:
    def isGood(self, s):
        if len(s) >= 3:
            return len(set(s)) == len(s)
        return False
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if self.isGood(s[i:i+3]):
                count += 1
        return count