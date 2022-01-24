from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_binary_tree(self, root, idx=1):
        if idx > len(root) or not root[idx-1]: return None
        node = TreeNode(root[idx-1])
        node.left = self.create_binary_tree(root, idx=idx*2)
        node.right = self.create_binary_tree(root, idx=idx*2+1)
        return node

    def is_sub(self, r, s):
        if r and not s or not r and s:
            return False
        elif not r and not s:
            return True
        else:
            if r.val == s.val:
                L = self.is_sub(r.left, s.left)
                R = self.is_sub(r.right, s.right)
                return L and R
            return False

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        root = self.create_binary_tree(root)
        subRoot = self.create_binary_tree(subRoot)
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                if self.is_sub(node, subRoot): return True
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return False


s = Solution()
print(s.isSubtree([3,4,5,1,2], [4,1,2]))
print(s.isSubtree([1], [1]))
print(s.isSubtree([1, 1], [1]))

