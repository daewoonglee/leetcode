# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_node(self, n, idx=1):
        if idx > len(n) or n[idx-1] is None:
            return None
        r = TreeNode(n[idx-1])
        r.left = self.create_node(n, idx*2)
        r.right = self.create_node(n, idx*2+1)
        return r

    def print_node(self, r):
        if r and r.val is not None:
            print(r.val)
            self.print_node(r.left)
            self.print_node(r.right)

    def is_leaf(self, r):
        return True if not r.left and not r.right else False

    def calc_sum(self, r, total, target):
        if not r:
            return False
        total += r.val
        if self.is_leaf(r):
            return total == target
        return True if self.calc_sum(r.left, total, target) else self.calc_sum(r.right, total, target)

    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        r = self.create_node(root)
        # self.print_node(r)
        return self.calc_sum(r, 0, targetSum)


s = Solution()
# print(s.hasPathSum([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], targetSum=22))
# print(s.hasPathSum([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1], targetSum=22))
# print(s.hasPathSum([1, 2, 3], targetSum=5))
# print(s.hasPathSum([1, 2], targetSum=0))
print(s.hasPathSum([], targetSum=0))
print(s.hasPathSum([0], targetSum=0))
