# Problem URL: https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        return bin(n).count("1")
    
        # c = 0
        # while n:
        #     n &= n - 1
        #     c += 1
        # return c