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