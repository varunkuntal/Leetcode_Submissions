# Problem URL: https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        l = []
        
        while head:
            if head.val or head.val == 0:
                l.append(head.val)
            head = head.next
                        
        n = len(l)
            
        if n == 1:
            return True
        
        for i in range(int(n//2)):
            if l[i] != l[-1-i]:
                return False
            
        return True