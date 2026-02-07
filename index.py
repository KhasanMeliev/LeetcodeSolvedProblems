import bisect


def func(arr, n):
    cur = n + 1

    idx = bisect.bisect_left(arr, cur)

    while idx < len(arr) and arr[idx] == cur:
        cur += 1
        idx += 1
    
    return cur


print(func([2, 7, 5, 4, 9, 15], 3))
print(func([2, 7, 5, 9, 15], 9))
