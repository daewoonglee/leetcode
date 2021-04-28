# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insert(self, nums, idx=1):
        if idx > len(nums):
            return None
        elif nums[idx-1] is None:
            return None
        root = TreeNode(nums[idx-1])
        root.left = self.insert(nums, idx*2)
        root.right = self.insert(nums, idx*2+1)
        return root

    def print_node(self, root):
        if root:
            print(root.val)
            self.print_node(root.left)
            self.print_node(root.right)

    def get_height(self, root):
        if root is None:
            return 0
        l = self.get_height(root.left)
        r = self.get_height(root.right)
        h = max(l, r) + 1
        return h-1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        root = self.insert(root)
        self.print_node(root)
        l = self.get_height(root.left)
        r = self.get_height(root.right)
        return True if abs(l-r) <= 1 else False


s = Solution()
# print(s.isBalanced([3, 9, 20, None, None, 15, 7]))
# print(s.isBalanced([1, 2, 2, 3, 3, None, None, 4, 4]))
# print(s.isBalanced([]))
print(s.isBalanced([1, 2, 2, 3, None, None, 3, 4, None, None, 4]))
