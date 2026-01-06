# https://leetcode.com/problems/plus-one/description/
# 66. Plus One

# def func(nums):
#     x = len(nums)-1
#     i = 0
#     while True:
#         if nums[x] < 9:
#             if 0 in nums and len(set(nums)) == 1:
#                 return [nums[x]+1]+[0]*i
#             return nums[:x]+[nums[x]+1]+[0]*i
#         nums[x] = 0
#         x -= 1
#         i += 1


# print(func([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
# print(func([5, 9, 9]))
# print(func([9, 9, 9, 9, 9]))

# ----------------------------------------------------------------
# 961. N-Repeated Element in Size 2N Array
# class Solution:
#     def repeatedNTimes(self, nums: List[int]) -> int:
#         d = {}
#         for i in nums:
#             if i in d:
#                 return i
#             d[i] = 1


#-----------------------------------------------------
# 3794. Reverse String Prefix

# class Solution:
#     def reversePrefix(self, s: str, k: int) -> str:
#         return s[:k][::-1]+s[k:]

#-----------------------------------------------------

# 1390. Four Divisors
# def func(arr):
#     res = 0
#     for i in arr:
#         divisor=0
#         subRes = 0
#         for j in range(2, int(i**0.5)+1):
#             if i%j==0:
#                 if i//j==j:
#                     divisor=10
#                 divisor+=2
#                 subRes=(j+i//j)+1+i
#             if divisor>2:
#                 break
            
#         if divisor==2:
#             res+=subRes
        

#     return res

# print(func([21,4,7,16])) #32

#------------------------------------------------------------------

# 1975. Maximum Matrix Sum
# def func(arr):
#     res = 0
#     cnt = 0
#     mini = float("infinity")

#     for i in arr:
#         for j in i:
#             res += abs(j)
#             mini = min(mini, abs(j))
#             if j <= 0:
#                 cnt += 1

#     return res if cnt % 2 == 0 else res - (mini * 2)


# print(func([[-1, 0, -1], [-2, 1, 3], [3, 2, 2]]))
# print(func([[2, 9, 3], [5, 4, -4], [1, 7, 1]]))


#---------------------------------------------------------------

# 1161. Maximum Level Sum of a Binary Tree
# from collections import deque


# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# def func(root):
#     if not root:
#         return

#     queue = deque([(root)])
#     res = 0
#     maxi = root.val
#     level=1
#     while queue:
#         curr_sum = 0
#         for _ in range(len(queue)):
#             node = queue.popleft()
#             curr_sum += node.val
            
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)

#         if maxi < curr_sum:
#             maxi = curr_sum
#             res = level

#         level += 1

#     return res


# # a = Node(1)
# # a.left = Node(7)
# # a.right = Node(0)
# # b = a.left
# # b.left = Node(7)
# # b.right = Node(-8)

# a = Node(-100)
# a.left = Node(-200)
# a.right = Node(-300)
# b = a.left
# c = a.right
# b.left = Node(-20)
# b.right = Node(-5)
# c.left = Node(-10)

# print(func(a))
