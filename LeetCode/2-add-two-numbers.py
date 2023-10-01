from typing import Optional
from math import floor


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + (str(self.next) if self.next else "")


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result1 = []
        while l1.next:
            result1.append(str(l1.val))
            l1 = l1.next
        result1.append(str(l1.val))
        result2 = []
        while l2.next:
            result2.append(str(l2.val))
            l2 = l2.next
        result2.append(str(l2.val))

        result1.reverse()
        result2.reverse()
        result1 = "".join(result1)
        result2 = "".join(result2)

        digits = str(int(result1) + int(result2))
        result = None
        for i in digits:
            result = ListNode(int(i), result)
        return result


a = Solution()
# assert a.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))) == 807
assert str(a.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))) == "89990001"
assert str(a.addTwoNumbers(ListNode(2, ListNode(4, ListNode(9))), ListNode(5, ListNode(6, ListNode(4, ListNode(9)))))) == "70401"

