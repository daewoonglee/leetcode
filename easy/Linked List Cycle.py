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

        # 0.195928443
        # fin = ListNode(-1)
        # while head:
        #     pre = head
        #     if head.next == fin:
        #         return True
        #     head = head.next
        #     pre.next = fin
        # return False

        # code refactoring 01 - 0.17435736500000001
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


s = Solution()
print(s.hasCycle([3, 2, 0, -4], 1))
print(s.hasCycle([3], -1))
print(s.hasCycle([3], 0))
print(s.hasCycle([1, 1, 1, 1, 1, 1, 1, 1, 1], 0))
# print(s.hasCycle([], -1))


if __name__ == '__main__':
    from timeit import Timer
    query = [[[3, 2, 0, -4], 1],
             [[3], -1],
             [[3], 0],
             [[1, 1, 1, 1, 1, 1, 1, 1, 1], 0],
             [[1, 1, 1, 1, 1, 1, 1, 1, 1], -1]]
    t = Timer(f"for t in {query}: Solution().hasCycle(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
