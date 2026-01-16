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

#-----------------------------------------------------
# 1339. Maximum Product of Splitted Binary Tree
# from collections import deque


# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# def func(root):
#     tree_sums = []
#     def dfs(node):
#         if not node:
#             return 0
#         l_sum = dfs(node.left)
#         r_sum = dfs(node.right)
        
#         cur_sum = l_sum+r_sum+node.val

#         tree_sums.append(cur_sum)

#         return cur_sum

#     total_sum = dfs(root)
#     max_product = 0
#     for sum_ in tree_sums:
#         max_product = max(max_product, (total_sum-sum_)*sum_)

#     return max_product

        


# a = Node(1)
# a.left = Node(2)
# a.right = Node(3)
# b = a.left
# c = a.right
# b.left = Node(4)
# b.right = Node(5)
# c.left = Node(6)

# print(func(a))

#-----------------------------------------------------------------------
# 1458. Max Dot Product of Two Subsequences
# def func(nums1, nums2):
#     n,m=len(nums1), len(nums2)    
#     dp = [[0]*(m) for _ in range(n)]
    
#     for i in range(n):
#         for j in range(m):
#             product = nums1[i]*nums2[j]
#             dp[i][j]=product

#             if i>0 and j>0:
#                 dp[i][j] = max(dp[i][j], dp[i-1][j-1]+product)
#             if i>0:
#                 dp[i][j] = max(dp[i][j], dp[i-1][j])
#             if j>0:
#                 dp[i][j] = max(dp[i][j], dp[i][j-1])
#     return dp[i][j]

# print(func([2,1,-2,5],[3,0,-6]))

#------------------------------------------------
# 865. Smallest Subtree with all the Deepest Nodes
# from collections import deque

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# def func(root):
#     def dfs(node):
#         if not node:
#             return (0, None)
#         left_depth, left_lca = dfs(node.left)
#         right_depth, right_lca=dfs(node.right)
#         if left_depth>right_depth:
#             return (left_depth+1, left_lca)
#         elif right_depth>left_depth:
#             return (right_depth+1, right_lca)
#         else:
#             return (left_depth+1, node)
        
#     return dfs(root)[1]

# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(6)
# f = Node(5)
# # g = Node(8)
# # h = Node(7)
# # i = Node(4)
# a.left = b
# b.left = c
# b.right = d
# c.right = e


# print(func(a))


# 2943. Maximize Area of Square Hole in Grid
# class Solution:
#     def maximizeSquareHoleArea(
#         self, n: int, m: int, hBars: List[int], vBars: List[int]
#     ) -> int:
#         def maxSpan(bars):
#             bars.sort()
#             res = 1
#             streak = 1
#             for i in range(1, len(bars)):
#                 if bars[i] - bars[i - 1] == 1:
#                     streak += 1
#                 else:
#                     streak = 1
#                 res = max(res, streak)
#             return res + 1

#         return min(maxSpan(hBars), maxSpan(vBars)) ** 2


# 3598. Longest Common Prefix Between Adjacent Strings After Removals
# class Solution:
#     def longestCommonPrefix(self, words: List[str]) -> List[int]:
#         def lcp(a, b):
#             i = 0
#             while i < len(a) and i < len(b) and a[i] == b[i]:
#                 i += 1
#             return i
        
#         n = len(words)
#         if n<=1:
#             return [0]*n
#         lcpArr = []
#         res = [0] * n
#         for i in range(n - 1):
#             lcpArr.append(lcp(words[i], words[i + 1]))
#         pref = [0] * (n - 1)
#         pref[0] = lcpArr[0]
#         for i in range(1, n - 1):
#             pref[i] = max(pref[i - 1], lcpArr[i])
#         suf = [0] * (n - 1)
#         suf[-1] = lcpArr[-1]
#         for i in range(n - 3, -1, -1):
#             suf[i] = max(suf[i + 1], lcpArr[i])

#         for i in range(n):
#             best = 0
#             if i - 2 >= 0:
#                 best = max(best, pref[i - 2])
#             if i + 1 < n - 1:
#                 best = max(best, suf[i + 1])
#             if 0 < i < n - 1:
#                 best = max(best, lcp(words[i - 1], words[i + 1]))

#             res[i] = best

#         return res


# 1208. Get Equal Substrings Within Budget
# class Solution:
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         n = len(s)
#         cost = []
#         for i in range(n):
#             cost.append(abs(ord(s[i]) - ord(t[i])))

#         left = 0
#         curr_cost = 0
#         res = 0
#         for right in range(n):
#             curr_cost += cost[right]
#             while curr_cost > maxCost:
#                 curr_cost -= cost[left]
#                 left += 1

#             res = max(res, right - left + 1)

#         return res
