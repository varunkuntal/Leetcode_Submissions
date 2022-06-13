# Problem URL: https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        # In place O(n), O(1)
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums