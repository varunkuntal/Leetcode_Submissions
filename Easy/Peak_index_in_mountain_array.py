# Problem URL: https://leetcode.com/problems/peak-index-in-a-mountain-array
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        s = 0
        e = len(arr)-1

        while s <= e:

            mid = (s + e) // 2

            if arr[mid] > arr[mid+1]:
                e = mid -1

            elif arr[mid] < arr[mid+1]:
                s = mid + 1

        if arr[mid] > arr[s]:
            return mid
        return s
        
        
        # # Since array is guaranteed mountain, O(n) solution follows
        # return arr.index(max(arr))