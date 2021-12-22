# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def create_binary_tree(self, r, idx, N):
        if N < idx or not r[idx-1]:
            return None
        node = TreeNode(r[idx-1])
        node.left = self.create_binary_tree(r, idx=idx*2, N=N)
        node.right = self.create_binary_tree(r, idx=idx*2+1, N=N)
        return node

    def print_binary_tree(self, r):
        if r:
            print(r.val)
            self.print_binary_tree(r.left)
            self.print_binary_tree(r.right)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        root = self.create_binary_tree(root, idx=1, N=len(root))
        #self.print_binary_tree(root)
        dfs = [root]
        cnt = {}
        while dfs:
            r = dfs.pop()
            if r.val not in cnt: cnt[r.val] = 0
            cnt[r.val] += 1
            if r.left: dfs.append(r.left)
            if r.right: dfs.append(r.right)
        
        max_n = max(cnt.values())
        ans = [k for k, v in cnt.items() if max_n == v]
        return ans


s = Solution()
print(s.findMode([1, None, 2, None, None, 2]))
print(s.findMode([1, 2, 3, 4, 5, 6]))
print(s.findMode([1, 2, 3, 2, 3]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[1, None, 2, None, None, 2], [1, 2, 3, 4, 5, 6], [1, 2, 3, 2, 3]]
    t = Timer(f"for t in {query}: Solution().findMode(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
 
