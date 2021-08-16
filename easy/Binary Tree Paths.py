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

        # 0.623115534
        # stack = [[root, []]]
        # ans = []
        # while stack:
        #     node, log = stack.pop()
        #     log.append(str(node.val))
        #     if is_leaf(node):
        #         ans.append("->".join(log))
        #     else:
        #         if node.left:
        #             stack.append([node.left, log[:]])
        #         if node.right:
        #             stack.append([node.right, log[:]])
        # return ans

        # code refactoring 01 - 0.522292423
        stack = [[root, ""]]
        ans = []
        while stack:
            node, log = stack.pop()
            # code refactoring 01
            # log = log + "->" + str(node.val) if log else str(node.val)

            # code refactoring 02 - 0.513015967
            log = log + "->" + str(node.val)
            if is_leaf(node):
                # code refactoring 01
                # ans.append(log)

                # code refactoring 02 - 0.513015967
                ans.append(log[2:])
            else:
                if node.left:
                    stack.append([node.left, log])
                if node.right:
                    stack.append([node.right, log])
        return ans


s = Solution()
# print(s.binaryTreePaths([1]))
# print(s.binaryTreePaths([1, 2]))
# print(s.binaryTreePaths([1, 2, 3]))
# print(s.binaryTreePaths([1, 2, 3, 4]))
# print(s.binaryTreePaths([1, 2, 3, None, 5]))
print(s.binaryTreePaths([1, 2, 3, None, None, None, 5]))
# print(s.binaryTreePaths([1, 2, 3, 4, 5, 6]))
# print(s.binaryTreePaths([1, 2, 3, 4, 5, 6, 7]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[1],
             [1, 2],
             [1, 2, 3],
             [1, 2, 3, 4],
             [1, 2, 3, None, 5],
             [1, 2, 3, 4, 5, 6],
             [1, 2, 3, 4, 5, 6, 7]]
    t = Timer(f"for t in {query}: Solution().binaryTreePaths(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
