# https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s = 1
        e = n
        
        if n == 1:
            return 1
        
        while s <= e:
            mid = (s + e) // 2
            
            res = isBadVersion(mid)
            
            if res and not isBadVersion(mid-1):
                return mid
            
            elif res:
                e = mid
            
            elif not res:
                s = mid + 1             