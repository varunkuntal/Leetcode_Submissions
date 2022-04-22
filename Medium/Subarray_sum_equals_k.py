class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

# More optimized approach O(n^2), Time out after 86 / 90 test cases
        n = len(nums)

        count = 0
        cumulative = [nums[0]]
        
        for i in range(1, n):
            cumulative.append(cumulative[i-1] + nums[i])  

        for i in range(n):
            count += cumulative[i+1:].count(k+cumulative[i])
            count += 1 if cumulative[i] == k else 0
        return count
            

            
# Slightly optimized approach O(n^2), Time Out after 61 / 90 test cases
#         n = len(nums)
#         count = 0

#         total_sum = sum(nums)

#         fixed = total_sum

#         for i in range(n):

#             j = n

#             while j != i:

#                 if total_sum == k:
#                     count += 1

#                 j -= 1
#                 total_sum -= nums[j]

#             fixed -= nums[i]
#             total_sum = fixed

#         return count
            
            
        
## Brute Force O(n^3) - Time Out after 31 / 90 test cases
#         count = 0
#         for i in range(n):
#             for j in range(i+1, n+1):
#                 if sum(nums[i:j]) == k:
#                     count += 1
                    
#         return count