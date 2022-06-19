# Problem URL: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/submissions/

class Solution:
    def minimumSum(self, num: int) -> int:
        
        x = ""
        
        for i in str(num):
            x = x + (i if i != "0" else "")
        
        x = sorted(x)
        
        n = len(x)
        
        if n == 0:
            return 0
        
        if n == 1:
            return x[0]
        
        if n == 2:
            return int(x[0]) + int(x[1])
        
        if n == 3:
            return int(x[0]+x[1]) + int(x[-1])
        
        if n == 4:
            return int(x[0]+x[2]) + int(x[1]+x[3])
        
        
        