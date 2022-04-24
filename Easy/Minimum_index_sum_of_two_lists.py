#Problem URL: https://leetcode.com/problems/minimum-index-sum-of-two-lists/submissions/
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1 = {}
        common = {}
        n1 = len(list1)
        n2 = len(list2)
                
        for i in range(n1):
            l1[list1[i]] = i+1
            
        for j in range(n2):
            if l1.get(list2[j]):
                common[list2[j]] = l1[list2[j]] + j

        minix = min(common.values())
        
        return [i for i, j in common.items() if j == minix]