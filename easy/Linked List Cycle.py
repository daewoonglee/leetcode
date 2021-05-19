# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def cycle_list_node(self, li, pos):
        root = ListNode(li[0])
        h = root
        h1 = root
        for n in li[1:]:
            root.next = ListNode(n)
            root = root.next

        if pos != -1:
            cnt = 0
            while h1:
                if cnt == pos:
                    root.next = h1
                    break
                h1 = h1.next
                cnt += 1
        return h

    def print_node(self, head):
        while head:
            print(head.val)
            head = head.next

    def hasCycle(self, head, pos):
        """
        :type head: ListNode
        :rtype: bool
        """
        head = self.cycle_list_node(head, pos)
        # self.print_node(head)

        fin = ListNode(-1)
        while head:
            pre = head
            if head.next == fin:
                return True
            head = head.next
            pre.next = fin
        return False




s = Solution()
print(s.hasCycle([3, 2, 0, -4], 1))
print(s.hasCycle([3], -1))
print(s.hasCycle([3], 0))
# print(s.hasCycle([], -1))
