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
    res = 0
    maxi = root.val
    level=1
    while queue:
        curr_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            curr_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if maxi < curr_sum:
            maxi = curr_sum
            res = level

        level += 1

    return res


# a = Node(1)
# a.left = Node(7)
# a.right = Node(0)
# b = a.left
# b.left = Node(7)
# b.right = Node(-8)

a = Node(-100)
a.left = Node(-200)
a.right = Node(-300)
b = a.left
c = a.right
b.left = Node(-20)
b.right = Node(-5)
c.left = Node(-10)

print(func(a))
