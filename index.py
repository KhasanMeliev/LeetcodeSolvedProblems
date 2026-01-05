def func(arr):
    res = 0
    cnt = 0
    mini = float("infinity")

    for i in arr:
        for j in i:
            res += abs(j)
            mini = min(mini, abs(j))
            if j <= 0:
                cnt += 1

    return res if cnt % 2 == 0 else res - (mini * 2)


print(func([[-1, 0, -1], [-2, 1, 3], [3, 2, 2]]))
print(func([[2, 9, 3], [5, 4, -4], [1, 7, 1]]))
