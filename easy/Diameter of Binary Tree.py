# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_binary_tree(self, root, idx=1):
        if idx > len(root) or not root[idx-1]:
            return None

        node = TreeNode(root[idx-1])
        node.left = self.create_binary_tree(root, idx=idx*2)
        node.right = self.create_binary_tree(root, idx=idx*2+1)
        return node

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_edges(pts):
            edges = 0
            stack = [[pts, 1]]
            while stack:
                node, depth = stack.pop()
                if node.left: stack.append([node.left, depth+1])
                if node.right: stack.append([node.right, depth+1])
                if edges < depth: edges = depth
            return edges

        root = self.create_binary_tree(root)
        left_depth = get_edges(root.left) if root.left else 0
        right_depth = get_edges(root.right) if root.right else 0
        return left_depth + right_depth


s = Solution()
print(s.diameterOfBinaryTree([1, 2, 3, 4, 5])) # 3
print(s.diameterOfBinaryTree([1, None, 3, None, None, None, 4, None, None, None, None, None, None, 5, 6])) # 3
print(s.diameterOfBinaryTree([1])) # 0
print(s.diameterOfBinaryTree([1,2])) # 1
i#print(s.diameterOfBinaryTree([4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2])) # expected 8, output 7
 
