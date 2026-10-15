# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        current = head
        values.reverse()
        for value in values:
            current.val = value
            current = current.next
        return head
            
        