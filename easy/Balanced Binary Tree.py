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
        if l == -1:
            return -1
        r = self.get_height(root.right)
        if r == -1:
            return -1
        return -1 if abs(l-r) > 1 else max(l, r) + 1

    def height(self, root, left=0, right=0):
        if root:
            if root.left:
                left = self.height(root.left)
            if left == -1:
                return -1
            if root.right:
                right = self.height(root.right)
            if right == -1:
                return -1
            if abs(left - right) <= 1:
                return max(left, right) + 1
            return -1
        return 0

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # if not root:
        #     return True
        root = self.insert(root)
        # self.print_node(root)

        # 0.39347390399962023
        # return self.get_height(root) != -1

        # code refactoring - 0.32359435299986217
        return self.height(root) != -1


s = Solution()
print(s.isBalanced([3, 9, 20, None, None, 15, 7]))
print(s.isBalanced([1, 2, 2, 3, 3, None, None, 4, 4]))
print(s.isBalanced([]))
print(s.isBalanced([1]))
print(s.isBalanced([1, 2, 2, 3, None, None, 3, 4, None, None, 4]))
print(s.isBalanced([1, 2, 2, 3, None, None, None, 4, None, None, 4]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[3, 9, 20, None, None, 15, 7],
             [1, 2, 2, 3, 3, None, None, 4, 4],
             [],
             [1],
             [1, 2, 2, 3, None, None, 3, 4, None, None, 4],
             [1, 2, 2, 3, None, None, None, 4, None, None, 4]]
    t = Timer(f"for t in {query}: Solution().isBalanced(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
