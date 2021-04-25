# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_tree(self, r, node, idx):
        if idx <= len(r)//2:
            node.left = TreeNode(r[idx*2-1])
            node.right = TreeNode(r[idx*2])
            self.create_tree(r, node.left, idx*2)
            self.create_tree(r, node.right, idx*2+1)

    def print_node(self, stack):
        if not stack[0]:
            return None
        vals = []
        new_stack = []
        while stack:
            node = stack.pop(0)
            new_stack.append(node.left)
            new_stack.append(node.right)
            vals.append(node.val)
        print(vals)
        self.print_node(new_stack)

    def get_bool(self, stack):
        # if not stack[0]:
        if all([1 if s is None else 0 for s in stack]):
            return True

        nums = []
        new_stack = []
        while stack:
            node = stack.pop()
            new_stack.append(node.left if node.left else None)
            new_stack.append(node.right if node.right else None)
            nums.append(node.val)
        N = len(nums)//2
        left = nums[:N]
        right = nums[N:]
        print(f"nums: {nums}, left: {left}, right: {right}")
        for i in range(N):
            if left[N-i-1] != right[i]:
                return False
        return self.get_bool(new_stack)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # if not root.left and not root.right:
        #     return True
        # elif not root.left or not root.right:
        #     return False
        # else:
        #     return self.get_bool([root.left, root.right])
        head = TreeNode(root[0])
        self.create_tree(root, head, idx=1)
        # self.print_node([head])
        return self.get_bool([head.left, head.right])


s = Solution()
# print(s.isSymmetric([1, 2, 2, 3, 4, 4, 3])) # T
# print(s.isSymmetric([1, 2, 2, 3, 4, 3, 3])) # F
# print(s.isSymmetric([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5])) # T
# print(s.isSymmetric([1, 2, 2, None, 3, None, 3]))   # F
# print(s.isSymmetric([1, 2, 2, 3, None, 3, None]))   # F
print(s.isSymmetric([1, 0]))
print(s.isSymmetric([1]))
