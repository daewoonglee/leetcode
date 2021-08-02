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
        head = self.create_tree(root)
        ans = []
        self.get_inorder(head, ans)
        return ans


s = Solution()
print(s.inorderTraversal([1, None, 2, None, None, 3]))
