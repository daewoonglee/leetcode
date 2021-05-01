# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_node(self, nums, idx=1):
        if idx > len(nums) or nums[idx-1] is None:
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
        l = self.get_height(root.left)
        r = self.get_height(root.right)

        # 0.284066799
        # return min(l, r) + 1 if l+r > 2 and l and r else max(l, r) + 1

        # code refactoring 01 - 0.270606075
        return max(l, r) + 1 if not l or not r else min(l, r) + 1

    # code refactoring 02 - 0.250741706
    def get_height_bfs(self, root):
        def is_leef(root):
            return True if root.left is None and root.right is None else False

        if root is None:
            return 0
        search_stack = [root]
        depth = 1
        while 1:
            new_stack = []
            for node in search_stack:
                if is_leef(node):
                    return depth
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            search_stack = new_stack
            depth += 1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root = self.create_node(root)
        # self.print_node(root)

        # return self.get_height(root)
        return self.get_height_bfs(root)


s = Solution()
# print(s.minDepth([3, 9, 20, None, None, 15, 7]))    # 2
# print(s.minDepth([2, None, 3, None, 4, None, 5, None, 6]))  # 3
# print(s.minDepth([1, 2, 2, 3])) # 2
# print(s.minDepth([2, None, 3, None, None, None, 4, None, None, None, None, None, None, None, 5])) # 4
print(s.minDepth([]))   # 0
print(s.minDepth([1]))  # 1


if __name__ == '__main__':
    from timeit import Timer
    query = [[3, 9, 20, None, None, 15, 7],
             [2, None, 3, None, 4, None, 5, None, 6],
             [1, 2, 2, 3],
             [2, None, 3, None, None, None, 4, None, None, None, None, None, None, None, 5],
             [1],
             []]
    t = Timer(f"for t in {query}: Solution().minDepth(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
