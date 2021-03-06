# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # def get_height(self, node, h=0):
    #     if node:
    #         l = self.get_height(node.left)
    #         r = self.get_height(node.right)
    #         h = max(l, r) + 1
    #     return h
    #
    # def get_factor(self, root):
    #     l = self.get_height(root.left)
    #     r = self.get_height(root.right)
    #     return l-r
    #
    # def rotated_rr(self, root):
    #     pnode = root
    #     cnode = root.right
    #     pnode.right = cnode.left
    #     cnode.left = pnode
    #     root = cnode
    #     return root
    #
    # def rotated_ll(self, root):
    #     pnode = root
    #     cnode = root.left
    #     pnode.left = cnode.right
    #     cnode.right = pnode
    #     root = cnode
    #     return root
    #
    # def balance(self, root):
    #     factor = self.get_factor(root)
    #     if factor > 1:
    #         root = self.rotated_ll(root)
    #     elif factor < -1:
    #         root = self.rotated_rr(root)
    #     return root
    #
    # def insert(self, root, node):
    #     if root:
    #         if node.val < root.val:
    #             if root.left is None:
    #                 root.left = node
    #             else:
    #                 root.left = self.insert(root.left, node)
    #         else:
    #             if root.right is None:
    #                 root.right = node
    #             else:
    #                 root.right = self.insert(root.right, node)
    #         root = self.balance(root)
    #     else:
    #         root = node
    #     return root
    #
    # def print_tree(self, root):
    #     if root:
    #         print(root.val)
    #         self.print_tree(root.left)
    #         self.print_tree(root.right)
    #
    # def sortedArrayToBST(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: TreeNode
    #     """
    #     root = None
    #     for i, n in enumerate(nums):
    #         root = self.insert(root, TreeNode(n))
    #     self.print_tree(root)
    #     return root

    def insert(self, nums):
        # 0.11282189000000001
        # if len(nums) == 1:
        #     return TreeNode(nums[0])
        # elif len(nums) == 0:
        #     return None
        # else:
        #     root = TreeNode(nums[len(nums)//2])
        #     root.left = self.insert(nums[:len(nums)//2])
        #     root.right = self.insert(nums[len(nums)//2+1:])
        #     return root

        # code refactoring01 - 0.150501664
        if len(nums) == 0:
            return None
        root = TreeNode(nums[len(nums)//2])
        root.left = self.insert(nums[:len(nums)//2])
        root.right = self.insert(nums[len(nums)//2+1:])
        return root


    def print_tree(self, root):
        if root:
            print(f"val: {root.val}")
            self.print_tree(root.left)
            self.print_tree(root.right)

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # root = TreeNode(nums[len(nums)//2])
        # root.left = self.insert(nums[:len(nums)//2])
        # root.right = self.insert(nums[len(nums)//2+1:])

        # code refactoring 02 - 0.155116043
        root = self.insert(nums)
        # self.print_tree(root)
        return root


s = Solution()
print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))
# print(s.sortedArrayToBST([-10, -3, 0]))
# print(s.sortedArrayToBST([5, 7, 9]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[-10, -3, 0, 5, 9],
             [-10, -3, 0],
             [5, 7, 9]]
    t = Timer(f"for t in {query}: Solution().sortedArrayToBST(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
