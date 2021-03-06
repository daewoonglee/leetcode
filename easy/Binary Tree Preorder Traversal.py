# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_tree(self, nums, idx=1):
        if idx > len(nums) or not nums[idx-1]:
            return None
        root = TreeNode(nums[idx-1])
        root.left = self.create_tree(nums, idx*2)
        root.right = self.create_tree(nums, idx*2+1)
        return root

    # 0.13815577499999998
    # def get_pre_order(self, root, ans):
    #     if root:
    #         ans.append(root.val)
    #         self.get_pre_order(root.left, ans)
    #         self.get_pre_order(root.right, ans)
    #     return ans
    #
    # def preorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     head = self.create_tree(root)
    #     ans = self.get_pre_order(head, [])
    #     return ans

    # code refactoring - 0.131090362
    def get_pre_order(self, root, ans):
        if root:
            ans.append(root.val)
            self.get_pre_order(root.left, ans)
            self.get_pre_order(root.right, ans)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        head = self.create_tree(root)
        ans = []
        self.get_pre_order(head, ans)
        return ans


s = Solution()
# print(s.preorderTraversal([1, None, 2, None, None, 3]))
# print(s.preorderTraversal([]))
# print(s.preorderTraversal([1]))
# print(s.preorderTraversal([1, 2]))
print(s.preorderTraversal([1, None, 2]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[1, None, 2, None, None, 3],
             [],
             [1],
             [1, 2],
             [1, None, 2]]
    t = Timer(f"for t in {query}: Solution().preorderTraversal(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
