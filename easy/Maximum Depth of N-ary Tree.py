from collections import deque


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    """
    create_tree 미완, 우선 get_depth에 대한 문제풀이만 진행

    def create_tree(self, r, n, idx):
        if len(r) > idx:
            N = len(n) if isinstance(n, list) else 1
            for i in range(N):
                childrens = []
                for v in r[idx:]:
                    if not v: break
                    childrens.append(Node(v))
                    idx += 1
                if isinstance(n, list):
                    n[i].children = childrens
                else:
                    n.children = childrens

            if isinstance(n, list):
                for i in range(N):
                    self.create_tree(r, n[i].children, idx+1)
            else:
                self.create_tree(r, n.children, idx+1)

    def print_tree(self, node):
        if not node:
            return
        print("==print==")
        if isinstance(node, list):
            for i in range(len(node)):
                print(node[i].val)
        else:
            print(node.val)

        if isinstance(node, list):
            for i in range(len(node)):
                self.print_tree(node[i].children)
        else:
            self.print_tree(node.children)
    """

    def get_depth(self, node):
        if not node:
            return 0

        ans = 0
        q = deque([[node, 1]])
        while q:
            n, d = q.popleft()
            if n:
                ans = max(ans, d)
            if isinstance(n, list):
                for i in range(len(n)):
                    if n[i].children:
                        q.append([n[i].children, d+1])
            else:
                q.append([n.children, d+1])
        return ans

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        head = Node(root[0], [])
        self.create_tree(root, head, 2)
        self.print_tree(head)

        return self.get_depth(head)

s = Solution()
# print(s.maxDepth([1,None,3,2,4,None,5,6])) # 3
print(s.maxDepth([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]))

"""
0 (1) 2 3 4 (5) 6 7 8 9 10 11 (6)
"""
