class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = {}
        n1 = len(list1)
        n2 = len(list2)
        
        for i in range(n1):
            for j in range(n2):
                if list1[i] == list2[j]:
                    common[list1[i]] = i+j
                    
        minix = min(common.values())
        
        return [i for i, j in common.items() if j == minix]