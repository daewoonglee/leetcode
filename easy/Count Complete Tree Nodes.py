# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0

        n = 0
        if root.left:
            n += self.countNodes(root.left)
        if root.right:
            n += self.countNodes(root.right)
        return n + 1


r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.left.right = TreeNode(5)
r.right.left = TreeNode(6)

s = Solution()
print(s.countNodes(r))