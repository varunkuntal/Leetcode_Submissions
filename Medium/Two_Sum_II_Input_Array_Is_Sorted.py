# Problem URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        i = 0
        j = n-1
        
        while i < n - 1:
            
            total = numbers[i] + numbers[j]
            
            if total > target:
                j -= 1
                
            elif total < target:
                i += 1
                
            else:
                return [i+1, j+1]
        