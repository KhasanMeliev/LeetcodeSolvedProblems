from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def func(root):
    def dfs(node):
        if not node:
            return (0, None)
        left_depth, left_lca = dfs(node.left)
        right_depth, right_lca=dfs(node.right)
        if left_depth>right_depth:
            return (left_depth+1, left_lca)
        elif right_depth>left_depth:
            return (right_depth+1, right_lca)
        else:
            return (left_depth+1, node)
        
    return dfs(root)[1]

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(6)
f = Node(5)
# g = Node(8)
# h = Node(7)
# i = Node(4)
a.left = b
b.left = c
b.right = d
c.right = e


print(func(a))
