from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def func(root):
    tree_sums = []
    def dfs(node):
        if not node:
            return 0
        l_sum = dfs(node.left)
        r_sum = dfs(node.right)
        
        cur_sum = l_sum+r_sum+node.val

        tree_sums.append(cur_sum)

        return cur_sum

    total_sum = dfs(root)
    max_product = 0
    for sum_ in tree_sums:
        max_product = max(max_product, (total_sum-sum_)*sum_)

    return max_product

        


a = Node(1)
a.left = Node(2)
a.right = Node(3)
b = a.left
c = a.right
b.left = Node(4)
b.right = Node(5)
c.left = Node(6)

print(func(a))
