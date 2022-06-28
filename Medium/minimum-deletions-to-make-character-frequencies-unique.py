# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

class Solution:
    def minDeletions(self, s: str) -> int:
        d = {}
        result = 0
        visted = []

        for char in s:

            if char not in d:
                d[char] = 1
            else:
                d[char] = d[char] + 1

        d = dict(sorted(d.items(), key = lambda x : x[1]))

        for i in d:

            if d[i] not in visted:
                visted.append(d[i])
            else:
                while d[i] != 0:

                    if d[i] not in visted:
                        visted.append(d[i])
                        break

                    d[i] = d[i] - 1

                    result = result + 1

        return result
        
        
        
        
        
        
#         d = {i:s.count(i) for i in set(s)}
        
#         f = {s.count(i):i for i  in set(s)}
        
#         d = dict(sorted(d.items(), key=lambda items: items[1], reverse=True))
        
#         e = list(d.items())
        
#         changes = 0
        
#         for i in range(1, len(e)):
#             if e[i][1] == e[i-1][1]:
                
            
            
        
        