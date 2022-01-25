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
        # 0.23148754984140396
        if not r and not s:
            return True
        elif r and s and r.val == s.val:
            return self.is_sub(r.left, s.left) and self.is_sub(r.right, s.right)
        return False


    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        root = self.create_binary_tree(root)
        subRoot = self.create_binary_tree(subRoot)
        #q = deque([root])
        #while q:
        #    node = q.popleft()
        #    if node.val == subRoot.val:
        #        if self.is_sub(node, subRoot): return True
        #    if node.left: q.append(node.left)
        #    if node.right: q.append(node.right)
        #return False

        # code refactoring (R) - 0.26330114901065826
        def convert(p):
            return f" {p.val}{convert(p.left)}{convert(p.right)}" if p else " # "
        return convert(subRoot) in convert(root)


s = Solution()
print(s.isSubtree([3,4,5,1,2], [4,1,2]))
print(s.isSubtree([1], [1]))
print(s.isSubtree([1, 1], [1]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[[3,4,5,1,2],[4,1,2]], [[1], [1]], [[1, 1], [1]], [[1,2,3,4,5], [5]]]
    t = Timer(f"for t in {query}: Solution().isSubtree(*t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

