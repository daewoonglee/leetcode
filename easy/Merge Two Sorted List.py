"""
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        for i, n in enumerate(l1):
            if i == 0:
                ln1 = ListNode(n)
                head1 = ln1
            else:
                ln1.next = ListNode(n)
                ln1 = ln1.next
        # while 1:
        #     print(ln1_head.val)
        #     if not ln1_head.next:
        #         break
        #     ln1_head = ln1_head.next

        for i, n in enumerate(l2):
            if i == 0:
                ln2 = ListNode(n)
                head2 = ln2
            else:
                ln2.next = ListNode(n)
                ln2 = ln2.next
        # while 1:
        #     print(ln2_head.val)
        #     if not ln2_head.next:
        #         break
        #     ln2_head = ln2_head.next

        head = ListNode(0)
        tail = head
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        tail.next = head1 if head1 else head2

        # head = head.next
        # while 1:
        #     print(f"val: {head.val}")
        #     if not head.next:
        #         break
        #     head = head.next
        return head.next


s = Solution()
print(s.mergeTwoLists([1, 2, 4], [1, 3, 4]))

