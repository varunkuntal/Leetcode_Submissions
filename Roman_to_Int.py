# Problem URL
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        dt = {'I':1,'V':5,'X':10,'L':50  ,'C':100 ,'D':500 ,'M':1000}

        subs = {'XL':40, 'XC':90, 'IX':9, 'IV':4, 'CD':400, 'CM':900}

        number = 0

        d = {x: s.count(x) for x in set(s)}

        dsubs = {y:s.count(y) for y in subs if s.count(y) != 0}

        for i in dsubs:
            ii = list(set(i))
            for j in range(dsubs[i]):
                number += subs[i]
                d[ii[0]] -= 1
                d[ii[1]] -= 1

        for i in d:
            number += d[i] * dt[i]

        return number
                    
                    
                    