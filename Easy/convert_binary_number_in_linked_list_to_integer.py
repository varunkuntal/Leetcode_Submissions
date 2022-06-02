# Problem URL: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        number = 0
        while head:
            number = (number << 1) | head.val
            head = head.next
        
        return number
        
        
#                   
#         string = ""
#         number = 0
#         while True:
#             string += str(head.val)
#             head = head.next
#             if head == None:
#                 break
            
#         for i in range(len(string)):
#             number = number + int(string[-i-1]) * (2 ** i)
            
#         return number
            