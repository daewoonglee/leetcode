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

        if not head or not head.next:
            return head
        elif not head.next.next:
            temp = head.next
            head.next.next = head
            head.next = None
            head = temp
            return head
        else:
            pre_pts = head
            head = head.next
            next_pts = head.next
            idx = 0

            while next_pts:
                head.next = pre_pts
                if not idx:
                    pre_pts.next = None
                    idx = 1
                pre_pts = head
                head = next_pts
                next_pts = next_pts.next
            head.next = pre_pts
            return head


s = Solution()
# print_linked_list(s.reverseList([1, 2, 3]))
# print_linked_list(s.reverseList([1, 2, 3, 4, 5]))
# print_linked_list(s.reverseList([1, 2]))
print_linked_list(s.reverseList([1]))
# print_linked_list(s.reverseList([]))
