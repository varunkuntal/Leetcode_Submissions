# Problem URL: https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        head2 = head
        while head:
            head = head.next
            length += 1
            
        length //= 2
        
        while length:
            head2 = head2.next
            length -= 1
            
        return head2
        