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

    def print_post_order(self, root, ans):
        if root:
            self.print_post_order(root.left, ans)
            self.print_post_order(root.right, ans)
            ans.append(root.val)
        return ans

    def print_post_order_r(self, root, ans):
        if root:
            if root.left:
                self.print_post_order(root.left, ans)
            if root.right:
                self.print_post_order(root.right, ans)
            ans.append(root.val)
        return ans

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        head = self.create_tree(root)

        ans = []

        # 0.132638456
        # self.print_post_order(head, ans)

        # code refactoring - 0.128562277
        self.print_post_order_r(head, ans)

        return ans


s = Solution()
# print(s.postorderTraversal([1, None, 2, None, None, 3]))
# print(s.postorderTraversal([]))
# print(s.postorderTraversal([1]))
# print(s.postorderTraversal([1, 2]))
print(s.postorderTraversal([1, None, 2]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[1, None, 2, None, None, 3],
             [],
             [1],
             [1, 2],
             [1, None, 2]]
    t = Timer(f"for t in {query}: Solution().postorderTraversal(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
