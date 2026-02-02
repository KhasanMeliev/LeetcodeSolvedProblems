def func(nums, k):
    positive = []
    for i in nums:
        if i >= 0:
            positive.append(i)
    k = k % len(positive)
    x = 0
    for i in range(len(nums)):
        if nums[i] >= 0:
            nums[i] = positive[(x+k) % len(positive)]
            x += 1

    return nums


print(func([3, 17, 3], 89646))
# print(func([5, 4, -9, 6], 10))
# print(func([1, -2, 3, -4], 3))
