# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, cur = None, None
        q = 0
        while l1 or l2:
            n = q
            if l1 is not None:
                n += l1.val
                l1 = l1.next
            if l2 is not None:
                n += l2.val
                l2 = l2.next

            q, n = divmod(n, 10)
            if head is None:
                head = ListNode(n)
                cur = head
            else:
                cur.next = ListNode(n)
                cur = cur.next
        if q != 0:
            cur.next = ListNode(q)

        return head


n1 = ListNode(2)
n1.next = ListNode(4)
n1.next.next = ListNode(3)

n2 = ListNode(5)
n2.next = ListNode(6)
n2.next.next = ListNode(4)

print(Solution().addTwoNumbers(n1, n2))


n1_head = ListNode(9)
cur1 = n1_head
for i in range(6):
    cur1.next = ListNode(9)
    cur1 = cur1.next

n2_head = ListNode(9)
cur2 = n2_head
for i in range(3):
    cur2.next = ListNode(9)
    cur2 = cur2.next

print(Solution().addTwoNumbers(n1_head, n2_head))
