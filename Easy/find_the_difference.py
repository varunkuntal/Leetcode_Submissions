class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
		# Bitwise Ops TC: O(n), SC: O(1)
        k = 0
        for i in s:
            k ^= ord(i)
            
        for i in t:
            k ^= ord(i)
            
        return chr(k)
        
        # One Liner TC: O(n), SC(n)
        #return chr(abs(sum([ord(i) for i in s]) - sum([ord(i) for i in t])))