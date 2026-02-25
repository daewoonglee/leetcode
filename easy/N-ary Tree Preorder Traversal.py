# Definition for a Node.
class Node:
    def __init__(self, val: int | None = None, children: list['Node'] | None = None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> list[int]:
        return self.dfs(root, [])

    def dfs(self, root_node: Node, ans: list[int]) -> list[int]:
        if root_node:
            ans.append(root_node.val)
            if root_node.children is not None:
                for r in root_node.children:
                    self.dfs(r, ans)
        return ans



root = Node(1)
# root.children = [Node(3), Node(2), Node(4)]
# root.children[0].children = [Node(5), Node(6)]

root.children = [Node(2), Node(3), Node(4), Node(5)]

root.children[1].children = [Node(6), Node(7)]
root.children[2].children = [Node(8)]
root.children[3].children = [Node(9), Node(10)]

root.children[1].children[1].children = [Node(11)]
root.children[2].children[0].children= [Node(12)]
root.children[3].children[0].children = [Node(13)]

root.children[1].children[1].children[0].children = [Node(14)]

s = Solution()
print(s.preorder(root))
