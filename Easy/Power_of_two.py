# Problem URL: https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        return n > 0 and not (n & n-1)
        
        # binary = bin(n)[2:]
        # return all([binary[0] == "1"] + ["1" not in binary[1:]])
        
        
        
        
        