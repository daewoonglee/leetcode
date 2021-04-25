# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_tree(self, p):
        if not p:
            return None

        pt = TreeNode(p[0])
        pt_head = pt
        for i, n in enumerate(p[1:]):
            node = TreeNode(n)
            if i % 2 == 0:
                pt.left = node
            else:
                pt.right = node
        return pt_head

    def print_tree(self, pt):
        if pt:
            print(pt.val)
            self.print_tree(pt.left)
            self.print_tree(pt.right)

    def get_bool(self, p, q):
        # 0.30504002399999997
        # if p and q and p.val == q.val:
        #     if self.get_bool(p.left, q.left):
        #         return self.get_bool(p.right, q.right)
        #     else:
        #         return False
        # return True if not p and not q else False

        # code refactoring - 0.290420576
        if p and q and p.val == q.val:
            return self.get_bool(p.left, q.left) and self.get_bool(p.right, q.right)
        return True if not p and not q else False

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pt = self.create_tree(p)
        # self.print_tree(pt)
        qt = self.create_tree(q)
        # self.print_tree(qt)

        return self.get_bool(pt, qt)


s = Solution()
print(s.isSameTree([1, 2, 3], [1, 2, 3]))
print(s.isSameTree([1, 2], [1, None, 2]))
print(s.isSameTree([1, 2, 1], [1, 1, 2]))
print(s.isSameTree([1, None, 2], [1, 1, 2]))
print(s.isSameTree([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
print(s.isSameTree([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[[1, 2, 3], [1, 2, 3]],
             [[1, 2], [1, None, 2]],
             [[1, 2, 1], [1, 1, 2]],
             [[1, None, 2], [1, 1, 2]],
             [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
             [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]]
    t = Timer(f"for t in {query}: Solution().isSameTree(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
