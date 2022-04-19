# Problem URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution:
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        d1 = {}
        i = 0
        n = len(s)
        maxlength = 0
        
        while i < n:
            if not d1.get(s[i]):
                d1[s[i]] = i + 1
                
            else:
                d1length = len(d1)
                if d1length > maxlength:
                    maxlength = d1length
                i = d1[s[i]] - 1
                d1 = {}
                
            i += 1

        if len(d1) > maxlength:
            maxlength = len(d1)
            
        return maxlength