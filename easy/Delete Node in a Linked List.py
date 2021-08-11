# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def create_linked_list(self, nums):
        head = ListNode(nums[0])
        temp = head
        for n in nums[1:]:
            temp.next = ListNode(n)
            temp = temp.next
        return head

    def print_linked_list(self, head):
        while head:
            print(f"val: {head.val}")
            head = head.next

    # def deleteNode(self, node):
    def deleteNode(self, node, li):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        head = self.create_linked_list(li)
        # self.print_linked_list(head)

        temp = head
        for _ in range(node-1):
            temp = temp.next
        node = temp

        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
        del next_node

        self.print_linked_list(head)


s = Solution()
print(s.deleteNode(3, [1, 2, 3, 4]))
