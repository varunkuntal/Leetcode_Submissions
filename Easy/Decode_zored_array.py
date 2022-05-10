# Problem URL: https://leetcode.com/problems/decode-xored-array

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ll = [first]
        n = len(encoded)
        for i in range(1, n+1):
            ll.append(encoded[i-1] ^ ll[i-1])
        return ll