# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_tree(self, r, h, idx):
        if idx <= len(r)//2:
            h.left = TreeNode(r[idx*2-1])
            h.right = TreeNode(r[idx*2])
            self.create_tree(r, h.left, idx*2)
            self.create_tree(r, h.right, idx*2+1)

    def print_tree(self, stack):
        if not stack[0]:
            return None

        nums = []
        new_stack = []
        while stack:
            node = stack.pop(0)
            new_stack.append(node.left)
            new_stack.append(node.right)
            nums.append(node.val)
        print(nums)
        self.print_tree(new_stack)

    # 0.0340235
    # def get_depth(self, r1, r2, depth):
    #     if r1 is None and r2 is None:
    #         return depth
    #     l1 = self.get_depth(r1.left, r1.right, depth+1)
    #     l2 = self.get_depth(r2.left, r2.right, depth+1)
    #     return l1 if l1 > l2 else l2

    # code refactoring - 0.027760454999999996
    def get_depth(self, r):
        return 0 if r is None else 1 + max(self.get_depth(r.left), self.get_depth(r.right))

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        head = TreeNode(root[0])
        self.create_tree(root, head, 1)
        # self.print_tree([head])

        if not head:
            return 0
        elif not head.left and not head.right:
            return 1
        else:
            # return self.get_depth(head.left, head.right, 1)
            return self.get_depth(head)


s = Solution()
print(s.maxDepth([3, 9, 20, None, None, 15, 7]))
print(s.maxDepth([3, 9, 20, 10, None, 15, 7, None, None, None, None, None, None, None, 9]))
print(s.maxDepth([1, None, 2]))
# print(s.maxDepth([]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[[3, 9, 20, None, None, 15, 7]],
             [[3, 9, 20, 10, None, 15, 7, None, None, None, None, None, None, None, 9]],
             [[1, None, 2]]]
    t = Timer(f"for t in {query}: Solution().maxDepth(t)", "from __main__ import Solution")
    print(t.timeit(number=10000))
