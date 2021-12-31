import queue

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def create_bst(self, nums, idx=1):
        if idx > len(nums) or nums[idx-1] is None: return None
        node = TreeNode(nums[idx-1])
        node.left = self.create_bst(nums, idx=idx*2)
        node.right = self.create_bst(nums, idx=idx*2+1)
        return node

    def helper(self, root,minn,maxx,res):
        if root is None:
            return

        self.helper(root.left,minn,root.val,res)
        self.helper(root.right,root.val,maxx,res)

        res[0] = min(res[0],min(root.val-minn,maxx-root.val))


    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """          
        res = [float('inf')]
        self.helper(root,-1000000,1000000,res)
        return res[0]

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #root_pts = self.create_bst(root)
        #q = queue.Queue()
        #q.put(root_pts)
        #min_ans = N = 10 ** 5

        """
        # 1.402242835611105
        while q.qsize():
            node = q.get()
            #print(f"val: {node.val}")
            if node.left:
                nl1 = node.val - node.left.val
                q.put(node.left)
                if node.left.right:
                    lnode = node.left
                    while lnode.right.right:
                        lnode = lnode.right
                    nr1 = node.val - lnode.right.val
                    nl = nl1 if nl1 < nr1 else nr1
                else:
                    nl = nl1
                #print(f"val: {node.val}, nl: {nl}")

            if node.right:
                nr2 = node.right.val - node.val
                q.put(node.right)
                if node.right.left:
                    rnode = node.right
                    while rnode.left.left:
                        rnode = rnode.left
                    nl2 = rnode.left.val - node.val
                    nr = nl2 if nl2 < nr2 else nr2
                else:
                    nr= nr2
                #print(f"val: {node.val}, nr: {nr}")

            if not node.left and node.right:
                n = nr
            elif node.left and not node.right:
                n = nl
            elif node.left and node.right:
                n = nl if nl < nr else nr
            else:
                continue 
            #print(f"diff: {n}\n")

            if min_ans > n: min_ans = n
        return min_ans
        """

        """
        # code refactoring - 1.3477903213351965
        while q.qsize():
            nl = nr = N
            node = q.get()
            if node.left:
                q.put(node.left)
                if node.left.right:
                    lnode = node.left
                    while lnode.right.right:
                        lnode = lnode.right
                    nl = node.val - lnode.right.val
                else:
                    nl = node.val - node.left.val

            if node.right:
                q.put(node.right)
                if node.right.left:
                    rnode = node.right
                    while rnode.left.left:
                        rnode = rnode.left
                    nr = rnode.left.val - node.val
                else:
                    nr = node.right.val - node.val

            diff = nl if nl < nr else nr
            if min_ans > diff: min_ans = diff
        return min_ans
        """

        # code refactoring (R) - 0.358064747415483
        root_pts = self.create_bst(root)
        res = [float('inf')]
        self.helper(root_pts, -1000000, 1000000,res)
        return res[0]


s = Solution()
#print(s.getMinimumDifference([4, 2, 6, 1, 3, 5]))
#print(s.getMinimumDifference([1, 0, 48, None, None, 12, 49]))
#print(s.getMinimumDifference([1, None, 5, None, None, 3]))
#print(s.getMinimumDifference([1, None, 50, None, None, 10]))
print(s.getMinimumDifference([10, 1, None, None, 5, None, None, None, None, None, 8]))
#print(s.getMinimumDifference([4, 2, 6, 1, 3]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[4, 2, 6, 1, 3, 5], [1, 0, 48, None, None, 12, 49], [1, None, 5, None, None, 3], [1, None, 50, None, None, 10], [10, 1, None, None, 5, None, None, None, None, None, 8]]
    t = Timer(f"for t in {query}: Solution().getMinimumDifference(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))

