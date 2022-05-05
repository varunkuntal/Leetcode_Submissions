# Problem URL: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = {i:deck.count(i) for i in set(deck)}
        minn = min(d.values())
        for i in range(2, minn+1):
            if all([j%i==0 for j in d.values()]):
                return True
        return False