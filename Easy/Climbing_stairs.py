# Problem URL: https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        
        n1 = 1
        n2 = 1
        total = 0
        
        if n == 1:
            return 1
        
        for i in range(n-1):
            
            total = n1 + n2
            
            n2 = n1
            
            n1 = total
            
        return total
