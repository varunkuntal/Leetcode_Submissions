# Problem URL: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if d.get(i):
                return i
            else:
                d[i] = 1