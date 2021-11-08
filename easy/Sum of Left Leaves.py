# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_binary_node(self, li, idx, N):
        if idx >= N  or li[idx] is None:
            return None
        node = TreeNode(li[idx])
        node.left = self.create_binary_node(li, idx=(idx*2)+1, N=N)
        node.right = self.create_binary_node(li, idx=(idx*2)+2, N=N)
        return node

    def print_node(self, root):
        if root is not None:
            print(root.val)
            self.print_node(root.left)
            self.print_node(root.right)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 0.12919005937874317
        #def is_leave(r):
        #    return r.left is None and r.right is None

        #def search(r, ans):
        #    if r.left:
        #        if is_leave(r.left):
        #            ans += r.left.val
        #        else:
        #            ans = search(r.left, ans)
        #    if r.right:
        #        ans = search(r.right, ans)
        #    return ans

        #root_pts = self.create_binary_node(root, 0, len(root))
        ## self.print_node(root_pts)
        #return search(root_pts, 0)

        # code refactoring (R) - 0.12677290011197329
        def search(root, is_left):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val if is_left else 0
            return search(root.left, True) + search(root.right, False)
        
        root_pts = self.create_binary_node(root, 0, len(root))
        return search(root_pts, False)


s = Solution()
print(s.sumOfLeftLeaves([3, 9, 20, None, None, 15, 7]))
print(s.sumOfLeftLeaves([3, 9, 20, None, 8, 1, 3, None, None, None, None, 4]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[3, 9, 20, None, None, 15, 7],
             [3, 9, 20, None, 8, 1, 3, None, None, None, None, 4]]
    t = Timer(f"for t in {query}: Solution().sumOfLeftLeaves(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

