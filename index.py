from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def func(root):
    if not root:
        return 
    queue = deque([(root)])
    last = []
    level = 0
    removed = []
    while queue:
        level+=1
        lev = []
        for i in range(len(queue)):
            node = queue.popleft()
            if not node.left and not node.right:
                removed.append(node.val)

            if node.left:
                queue.append(node.left)
                lev.append(node.left.val)
            if node.right:
                queue.append(node.right)
                lev.append(node.right.val)
        last.append([lev, level])
    if len(last)<=2:
        return root.val
    depth = last[-3][0]
    return depth, removed
    for i in depth:
        if i not in removed:
            return i

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
d.right=f


print(func(a))
