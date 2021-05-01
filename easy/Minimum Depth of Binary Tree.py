# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_node(self, nums, idx=1):
        if idx > len(nums):
            return None
        root = TreeNode(nums[idx-1])
        root.left = self.create_node(nums, idx*2)
        root.right = self.create_node(nums, idx*2+1)
        return root

    def print_node(self, root):
        if root:
            print(root.val)
            self.print_node(root.left)
            self.print_node(root.right)

    def get_height(self, root):
        if root is None:
            return 0
        if root.val is None:
            return 0
        l = self.get_height(root.left)
        r = self.get_height(root.right)
        return min(l, r) + 1 if l+r > 2 and l and r else max(l, r) + 1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root = self.create_node(root)
        # self.print_node(root)
        return self.get_height(root)


s = Solution()
# print(s.minDepth([3, 9, 20, None, None, 15, 7]))
# print(s.minDepth([2, None, 3, None, 4, None, 5, None, 6]))
print(s.minDepth([2, None, 3, None, None, None, 4, None, None, None, None, None, None, None, 5]))