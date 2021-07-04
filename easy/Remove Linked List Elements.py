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

        # 0.19631843699999998
        # pre_ptr = cur_ptr = head
        # while cur_ptr:
        #     if cur_ptr.val == val:
        #         if pre_ptr == cur_ptr:
        #             head = pre_ptr = cur_ptr = cur_ptr.next
        #         else:
        #             temp = cur_ptr.next
        #             del cur_ptr
        #             pre_ptr.next = cur_ptr = temp
        #     else:
        #         pre_ptr = cur_ptr
        #         cur_ptr = cur_ptr.next
        #
        # # self.print_node(head)
        # return head

        # code refactoring (R) 01 - 0.222853806
        init = ListNode(-1)
        init.next = head

        pre_ptr, cur_ptr = init, head
        while cur_ptr:
            if cur_ptr.val == val:
                temp = cur_ptr.next
                del cur_ptr
                pre_ptr.next = cur_ptr = temp
            else:
                pre_ptr = cur_ptr
                cur_ptr = cur_ptr.next
        # self.print_node(init.next)
        return init.next


s = Solution()
print(s.removeElements([1, 2, 6, 3, 4, 5, 6], 6))
# print(s.removeElements([7, 7, 7, 7], 7))


if __name__ == '__main__':
    from timeit import Timer
    query = [[[1, 2, 6, 3, 4, 5, 6], 6],
             [[7, 7, 7, 7], 7],
             [[], 3],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10],
             [[1, 1, 1, 1, 1, 1, 1, 1, 1, 10], 1]]
    t = Timer(f"for t in {query}: Solution().removeElements(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
