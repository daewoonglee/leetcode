# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_tree(self, nums, idx=1):
        if idx > len(nums) or nums[idx-1] is None:
            return None
        root = TreeNode(nums[idx-1])
        root.left = self.create_tree(nums, idx*2)
        root.right = self.create_tree(nums, idx*2+1)
        return root

    def get_inorder(self, head, ans):
        if head.left:
            self.get_inorder(head.left, ans)
        ans.append(head.val)
        if head.right:
            self.get_inorder(head.right, ans)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 0.053219652
        # head = self.create_tree(root)
        # if head is None:
        #     return []
        # ans = []
        # self.get_inorder(head, ans)
        # return ans

        # 0.053970130000000005
        # if root is None:
        #     return []
        # order_traversal = self.inorderTraversal(root.left)
        # order_traversal.append(root.val)
        # order_traversal.extend(self.inorderTraversal(root.right))
        # return order_traversal

        # 0.053800414000000005
        return [] if root is None else self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


s = Solution()
# print(s.inorderTraversal([1, None, 2, None, None, 3]))
print(s.inorderTraversal(s.create_tree([1, None, 2, None, None, 3])))


if __name__ == '__main__':
    from timeit import Timer
    query = [[1, None, 2, None, None, 3]]
    t = Timer(f"for t in {query}: Solution().inorderTraversal(Solution().create_tree(t))", "from __main__ import Solution")
    # t = Timer(f"for t in {query}: Solution().inorderTraversal(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
