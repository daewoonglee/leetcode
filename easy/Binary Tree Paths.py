# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_binary_tree(self, nums, idx=1):
        if idx > len(nums) or nums[idx-1] is None:
            return None
        root = TreeNode(nums[idx-1])
        root.left = self.create_binary_tree(nums, idx=idx*2)
        root.right = self.create_binary_tree(nums, idx=idx*2+1)
        return root

    def print_binary_tree(self, root):
        if root:
            print(root.val)
            self.print_binary_tree(root.left)
            self.print_binary_tree(root.right)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def is_leaf(n):
            return n.left is None and n.right is None

        root = self.create_binary_tree(root)
        # self.print_binary_tree(root)

        stack = [[root, []]]
        ans = []
        while stack:
            node, log = stack.pop()
            log.append(str(node.val))
            if is_leaf(node):
                ans.append("->".join(log))
            else:
                if node.left:
                    stack.append([node.left, log[:]])
                if node.right:
                    stack.append([node.right, log[:]])
        return ans


s = Solution()
# print(s.binaryTreePaths([1]))
# print(s.binaryTreePaths([1, 2]))
# print(s.binaryTreePaths([1, 2, 3]))
# print(s.binaryTreePaths([1, 2, 3, 4]))
# print(s.binaryTreePaths([1, 2, 3, None, 5]))
# print(s.binaryTreePaths([1, 2, 3, 4, 5, 6]))
print(s.binaryTreePaths([1, 2, 3, 4, 5, 6, 7]))
