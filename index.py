from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def func(root):
    res = []

    def dfs(node,level):
        if not node:
            return 
        if level==len(res):
            res.append([])


a = Node(3)
b = Node(9)
c = Node(20)
d = Node(15)
e = Node(7)

a.left = b
a.right = c
c.left = d
c.right = e

print(func(a))
