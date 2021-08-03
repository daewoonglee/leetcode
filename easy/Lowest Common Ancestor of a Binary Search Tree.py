# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def create_binary_search_tree(self, root, idx=1):
        if root is None or len(root) < idx:
            return None
        node = TreeNode(root[idx-1])
        node.left = self.create_binary_search_tree(root, idx*2)
        node.right = self.create_binary_search_tree(root, idx*2+1)
        return node

    # def search_node(self, root, p, q):
    #     return pass

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        root = self.create_binary_search_tree(root)

        li, p_idx, q_idx = self.search_node(root, p, q)
        p_root_idx = q_root_idx = 0
        while p_root_idx != q_root_idx:
            if p_idx < q_idx:
                q_root_idx = q_root_idx // 2
            else:
                p_root_idx = p_root_idx // 2
        return li[p_root_idx]


s = Solution()
print(s.lowestCommonAncestor([6, 2, 8, 0, 4, 7, 9], 2, 8))
