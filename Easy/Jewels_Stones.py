# Problem URL: https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        d = {x:stones.count(x) for x in set(stones)}
        
        total = 0
        
        for i in jewels:
            if d.get(i):
                total += d[i]
                
        return total
        
        
#         total = 0
#         for i in stones:
#             for j in jewels:
#                 total += 1 if i == j else 0
                
#         return total