# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_binary_tree(self, nums, idx):
        if idx >= len(nums):
            return None
        root = TreeNode(nums[idx])
        root.left = self.create_binary_tree(nums, idx*2+1)
        root.right = self.create_binary_tree(nums, idx*2+2)
        return root

    def print_node(self, root):
        if root:
            print(f"val: {root.val}")
            self.print_node(root.left)
            self.print_node(root.right)

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        # 0.370668258
        # temp = root.left
        # root.left = root.right
        # root.right = temp
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        # code refactoring 01 - 0.347262953
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        # code refactoring 02 - 0.335051392
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def test(self, nums):
        root = self.create_binary_tree(nums, 0)
        # self.print_node(root)
        inv_root = self.invertTree(root)
        # self.print_node(inv_root)


s = Solution()
# s.test([4, 2, 7, 1, 3, 6, 9])
# s.test([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# s.test([])
# s.test([1])
s.test([1, 2, 3])


if __name__ == '__main__':
    from timeit import Timer
    query = [[4, 2, 7, 1, 3, 6, 9],
             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
             [],
             [1],
             [1, 2, 3]]
    t = Timer(f"for t in {query}: Solution().test(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
