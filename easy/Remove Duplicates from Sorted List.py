"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.


Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 0.018867328999999995
        if not head:
            return None

        # set ListNode
        node_head = ListNode(head[0])
        cur_head = node_head
        for h in head[1:]:
            node = ListNode(h)
            cur_head.next = node
            cur_head = cur_head.next

        # print ListNode
        # while node_head:
        #     print(node_head.val)
        #     node_head = node_head.next

        # ans_head = ListNode(node_head.val)
        # ans = ans_head
        # while node_head:
        #     # print(f"ans: {ans.val}, node: {node_head.val}")
        #     if ans.val != node_head.val:
        #         ans.next = node_head
        #         ans = ans.next
        #     node_head = node_head.next
        # ans.next = None
        #
        # # print ListNode
        # while ans_head:
        #     # print(f"p: {ans_head.val}")
        #     ans_head = ans_head.next
        # return ans_head

        # code refactoring - 0.017514743
        ans = node_head
        head = ans
        while ans and ans.next:
            if ans.val != ans.next.val:
                ans = ans.next
            else:
                ans.next = ans.next.next

        # print ListNode
        while head:
            # print(f"p: {head.val}")
            head = head.next
        return head


s = Solution()
print(s.deleteDuplicates([1, 1, 2]))
# print(s.deleteDuplicates([1, 1, 2, 3, 3]))
# print(s.deleteDuplicates([1, 1, 2, 3, 3, 4]))
# print(s.deleteDuplicates([]))
# print(s.deleteDuplicates([0, 0, 0]))
# print(s.deleteDuplicates([1, 2, 2, 2]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[1, 1, 2], [1, 1, 2, 3, 3], [1, 1, 2, 3, 3, 4], [], [0, 0, 0], [1, 2, 2, 2]]
    t = Timer(f"for t in {query}: Solution().deleteDuplicates(t)", "from __main__ import Solution")
    print(t.timeit(number=1000))
