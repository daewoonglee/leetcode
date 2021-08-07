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

    def search_node(self, root, p, q):
        stack = [root]
        search_list = []
        p_idx = q_idx = 0
        while stack and (not p_idx or not q_idx):
            node = stack.pop(0)
            # if node is None:
            #     continue
            search_list.append(node)
            # if p == node:
            if p.val == node.val:
                p_idx = len(search_list)
            # elif q == node:
            elif q.val == node.val:
                q_idx = len(search_list)
            stack.append(node.left)
            stack.append(node.right)
        return search_list, p_idx, q_idx

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        root = self.create_binary_search_tree(root)
        while root:
            if root.val > p and root.val > q:
                root = root.left
            elif root.val < p and root.val < q:
                root = root.right
            else:
                return root.val


s = Solution()
# print(s.lowestCommonAncestor([6, 2, 8, 0, 4, 7, 9], 2, 8))  # 6
# print(s.lowestCommonAncestor([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8))    # 6
# print(s.lowestCommonAncestor([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4))    # 2
# print(s.lowestCommonAncestor([2, 1], 2, 1)) # 2
# print(s.lowestCommonAncestor([6, None, 8, None, None, None, 9, None, None, None, None, None, None, None, 2], 8, 9)) # 8
# print(s.lowestCommonAncestor([6, None, 8, None, None, None, 9, None, None, None, None, None, None, None, 2], 9, 6)) # 6
# print(s.lowestCommonAncestor([5, 3, 6, 2, 4, None, None, 1], 6, 1))
print(s.lowestCommonAncestor([45,30,46,10,36,None,49,8,24,34,42,48,None,4,9,14,25,31,35,41,43,47,None,0,6,None,None,11,
                              20,None,28,None,33,None,None,37,None,None,44,None,None,None,1,5,7,None,12,19,21,26,29,32,
                              None,None,38,None,None,None,3,None,None,None,None,None,13,18,None,None,22,None,27,None,
                              None,None,None,None,39,2,None,None,None,15,None,None,23,None,None,None,40,None,None,None,
                              16,None,None,None,None,None,17], 47, 15))
print(s.lowestCommonAncestor([30, 10, 36, 8, 24, 34, 42, 14, 25, 31, 35, 41, 43, 47, None, None, 33, None, None, 37,
                              None, None, 44, None, None, None, 1, 5, 7, None, 12, None, 13, 18, None, None, 22, None,
                              27, None, None, None, None, None, 39, 2, None, None, None, 15, None, None, 23, None, None,
                              None, 40, None, None], 47, 15))

#                                                                                          45,\
#                                                      30,                                                                        46,\
#                         10,                                                     36,                                   N,                          49,\
#               8,                         24,                        34,                    42,                                             48,               N,
#         4,            9,           14,           25,          31,         35,        41,         43,                                   47,        N,
#     0,     6,      N,     N,     11,   20,     N,   28,     N,    33,   N,    N,   37,   N,    N,   44,                               N, N,
#   N, 1,  5, 7,                  N,12, 19,21,      26, 29,        32, N,           N, 38 ,          N ,N ,
#     N,3,N N NN,                   N1318N N22,    N,27,NN,        NN,                 N,39,
#      2,N,                         N,N15,N, N,23, N,N, N,40, N,N, N,16, N,N, N,N, N,17

