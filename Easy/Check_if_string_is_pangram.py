# Problem URL: https://leetcode.com/problems/check-if-the-sentence-is-pangram

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        bitsum = 0
        base = ord('a')
        target = (1 << 26) - 1
        
        for i in sentence:
            c = ord(i) - base
            bitsum = bitsum | 1 << c
            
        return bitsum == target
        
        
        # Pythonic Solution
        # return len(set(sentence)) == 26