class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left-right) > 1:
            return -1

        return max(left, right)+1
    return dfs(root) != -1


a = Node(3)
b = Node(9)
c = Node(20)
d = Node(15)
e = Node(7)
a.left = b
a.right = c
b.left = d
b.right = e

print(isBalanced(a))
