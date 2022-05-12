# Problem URL: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        p = 1
        s = 0
        
        while n != 0:
            r = n % 10
            p = p * r
            s += r
            n = int(n // 10)
        
        return p - s
    
    
#         ll = [i for i in str(n)]
#         s = 0
#         p = 1
        
#         for i in ll:
#             s = s + int(i)
#             p = p * int(i)
            
#         return p - s
        