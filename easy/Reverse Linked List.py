# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(nums):
    head = ListNode(nums[0])
    pts = head
    for num in nums[1:]:
        node = ListNode(num)
        pts.next = node
        pts = pts.next
    return head


def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head = create_linked_list(head)
        # print_linked_list(head)

        # 0.660604941
        # if not head or not head.next:
        #     return head
        # elif not head.next.next:
        #     temp = head.next
        #     head.next.next = head
        #     head.next = None
        #     head = temp
        #     return head
        # else:
        #     pre_pts = head
        #     head = head.next
        #     next_pts = head.next
        #     idx = 0
        #
        #     while next_pts:
        #         head.next = pre_pts
        #         if not idx:
        #             pre_pts.next = None
        #             idx = 1
        #         pre_pts = head
        #         head = next_pts
        #         next_pts = next_pts.next
        #     head.next = pre_pts
        #     return head

        # code refactoring - 0.557256441
        pre_pts = None
        while head:
            next_pts = head.next
            head.next = pre_pts
            pre_pts = head
            head = next_pts
        return pre_pts


s = Solution()
# print_linked_list(s.reverseList([1, 2, 3]))
# print_linked_list(s.reverseList([1, 2, 3, 4, 5]))
print_linked_list(s.reverseList([1, 2]))
print_linked_list(s.reverseList([1]))
# print_linked_list(s.reverseList([]))

if __name__ == '__main__':
    from timeit import Timer
    query = [[1, 2, 3],
             [1, 2, 3, 4, 5],
             [1, 2],
             [1],
             [i for i in range(100)]]
    t = Timer(f"for t in {query}: Solution().reverseList(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
