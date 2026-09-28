# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        divisor = a
        dividend = b
        rem = divisor % dividend
        while(rem!=0):
            divisor = dividend
            dividend = rem
            rem = divisor % dividend
        return dividend
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duphead= head
        while(duphead.next!=None):
            gcdV = self.gcd(duphead.val, duphead.next.val)
            newNode = ListNode(gcdV, duphead.next)
            duphead.next = newNode
            duphead = newNode.next
        return head



        