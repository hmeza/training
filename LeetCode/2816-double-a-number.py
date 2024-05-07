"""
Runtime
237 ms
Beats 64.98% of users with Python3
Memory
20.58 MB
Beats 16.88% of users with Python3
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = self.doDouble(head)
        if carry:
            return ListNode(carry, head)
        return head

    def doDouble(self, head):
        if head.next is None:
            carry = 0
        else:    
            carry = self.doDouble(head.next)
        val = head.val * 2
        head.val = val % 10 + carry
        return int(val / 10)         
