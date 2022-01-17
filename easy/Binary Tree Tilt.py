# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.ans = 0

    def create_binary_tree(self, nums, idx=1):
        if idx > len(nums) or nums[idx-1] is None: return None
        node = TreeNode(nums[idx-1])
        node.left = self.create_binary_tree(nums, idx=idx*2)
        node.right = self.create_binary_tree(nums, idx=idx*2+1)
        return node

    def search_node(self, root):
        if not root: return 0
        L = self.search_node(root.left)
        R = self.search_node(root.right)
        self.ans += abs(L-R)
        return root.val + L + R

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root = self.create_binary_tree(root)
        self.search_node(root)
        return self.ans
       

s = Solution()
#print(s.findTilt([1,2,3]))
print(s.findTilt([4,2,9,3,5,None,7]))
 
