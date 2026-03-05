# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_li1, num_li2 = [], []
        while l1 or l2:
            if l1 is not None:
                num_li1.append(l1.val)
                l1 = l1.next
            if l2 is not None:
                num_li2.append(l2.val)
                l2 = l2.next
        num_li1.reverse()
        num_li2.reverse()

        head, cur = None, None
        for n in str(int("".join(map(str, num_li1))) + int("".join(map(str, num_li2))))[::-1]:
            if head is None:
                head = ListNode(int(n))
                cur = head
            else:
                cur.next = ListNode(int(n))
                cur = cur.next
        return head


n1 = ListNode(2)
n1.next = ListNode(4)
n1.next.next = ListNode(3)

n2 = ListNode(5)
n2.next = ListNode(6)
n2.next.next = ListNode(4)

print(Solution().addTwoNumbers(n1, n2))
