# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def init_linked_list(self, nums, idx=0):
        if idx >= len(nums):
            return None
        head = ListNode(nums[idx])
        head.next = self.init_linked_list(nums, idx+1)
        return head


    def print_linked_list(self, head):
        while head:
            print(head.val)
            head = head.next


    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        head = self.init_linked_list(head)
        # self.print_linked_list(head)

        arr = list()
        while head:
            arr.append(head.val)
            # if arr:
            #     if arr[-idx] == head.val:
            #         arr.pop()
            #     elif len(arr) >= 2 and arr[-2] == head.val:
            #         arr.pop()
            #         arr.pop()
            #     else:
            #         arr.append(head.val)
            # else:
            #     arr.append(head.val)
            head = head.next
        # return True if len(arr) <= 1 else False
        N = len(arr)
        return arr[:N//2] == arr[N//2:][::-1] if N % 2 == 0 else arr[:N//2] == arr[N//2+1:][::-1]


s = Solution()
print(s.isPalindrome([1, 2, 2, 1]))
print(s.isPalindrome([1, 2, 3, 2, 1]))
print(s.isPalindrome([1, 1, 1, 1, 1]))
print(s.isPalindrome([1, 0, 0]))
