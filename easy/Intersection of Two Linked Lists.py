# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def create_linked_list(self, head, idx=0, skip=None):
        if idx >= len(head)-1:
            return ListNode(head[idx])
        node = ListNode(head[idx])
        node.next = self.create_linked_list(head, idx+1)
        return node

    def merge_linked_list(self, headA, headB, skipA, skipB):
        head = headB
        for _ in range(skipA):
            headA = headA.next
        for _ in range(skipB-1):
            headB = headB.next
        while headA:
            headB.next = headA
            headB = headA
            headA = headA.next
        return head

    def print_linked_list(self, head):
        while head:
            print(f"val: {head.val}")
            head = head.next

    def get_length(head):
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt

    def move_node(head, N):
        for _ in range(N):
            head = head.next
        return head

    def getIntersectionNode(self, headA, headB, skipA, skipB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        headA = self.create_linked_list(headA)
        # self.print_linked_list(headA)
        headB = self.create_linked_list(headB)
        # self.print_linked_list(headB)
        headB = self.merge_linked_list(headA, headB, skipA, skipB)
        # self.print_linked_list(headB)

        # time limited
        # while headA:
        #     new_headB = headB
        #     while new_headB:
        #         if headA == new_headB:
        #             return new_headB.val
        #         new_headB = new_headB.next
        #     headA = headA.next
        # return None


        AN = self.get_length(headA)
        BN = self.get_length(headB)

        if AN > BN:
            headA = self.move_node(headA, AN-BN)
        else:
            headB = self.move_node(headB, BN-AN)

        while headA:
            if headA == headB:
                return headA.val
            headA = headA.next
            headB = headB.next
        return None


s = Solution()
print(s.getIntersectionNode([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], skipA=2, skipB=3))
print(s.getIntersectionNode([1, 9, 1, 2, 4], [3, 2, 4], skipA=3, skipB=1))
print(s.getIntersectionNode([2, 6, 4], [1, 5], skipA=3, skipB=2))
