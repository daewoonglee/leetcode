from collections import deque


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def __init__(self):
        self.idx = 2

    def create_tree(self, r, n):
        if len(r) > self.idx:
            N = len(n)
            for i in range(N):
                childrens = []
                for v in r[self.idx:]:
                    self.idx += 1
                    if not v:
                        break
                    childrens.append(Node(v))
                n[i].children = childrens

            for i in range(N):
                if n[i].children:
                    self.create_tree(r, n[i].children)
                else:
                    self.idx += 1

    def print_tree(self, node):
        if not node:
            return
        print("==print==")
        for i in range(len(node)):
            print(node[i].val)

        for i in range(len(node)):
            self.print_tree(node[i].children)

    def clear(self):
        self.idx = 2

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def get_depth(node):
            # 0.30547391399999996
            # ans = 0
            # q = deque([[node, 1]])
            # while q:
            #     n, d = q.popleft()
            #     if n:
            #         ans = max(ans, d)
            #     for i in range(len(n)):
            #         if n[i].children:
            #             q.append([n[i].children, d + 1])
            # return ans

            # code refactoring - 0.28522715099999996
            if not node:
                return 1
            dep = 0
            for i in range(len(node)):
                if node[i].children:
                    dep = max(dep, get_depth(node[i].children)+1)
            return dep

        head = [Node(root[0], [])]
        self.create_tree(root, head)
        # self.print_tree(head)
        if not head:
            return 0
        return get_depth(head)+1


s = Solution()
print(s.maxDepth([1,None,3,2,4,None,5,6])) # 3
s.clear()
print(s.maxDepth([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14])) # 5


if __name__ == '__main__':
    from timeit import Timer
    query = [[1,None,3,2,4,None,5,6],
             [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]]
    t = Timer(f"for t in {query}: Solution().maxDepth(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
