def func(arr):
    res = set()
    cur = set()
    for num in arr:
        cur = {num | x for x in cur} | {num}
        res |= cur
        print(res, cur, num) 
    return len(res)


print(func([1, 1, 2]))
