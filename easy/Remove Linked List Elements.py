# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def add_node(self, val_list):
        head = ptr = None
        for val in val_list:
            node = ListNode(val)
            if ptr is None:
                ptr = node
                head = ptr
            else:
                ptr.next = node
                ptr = ptr.next
        return head

    def print_node(self, head):
        while head:
            print(head.val)
            head = head.next

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        head = self.add_node(head)
        # self.print_node(head)

        pre_ptr = cur_ptr = head
        while cur_ptr:
            if cur_ptr.val == val:
                if pre_ptr == cur_ptr:
                    head = pre_ptr = cur_ptr = cur_ptr.next
                else:
                    temp = cur_ptr.next
                    del cur_ptr
                    pre_ptr.next = cur_ptr = temp
            else:
                pre_ptr = cur_ptr
                cur_ptr = cur_ptr.next

        # self.print_node(head)
        return head


s = Solution()
print(s.removeElements([1, 2, 6, 3, 4, 5, 6], 6))
# print(s.removeElements([7, 7, 7, 7], 7))
