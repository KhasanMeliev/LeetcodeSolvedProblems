def func(n, k):
    x = (n+1)//2
    if k <= x:
        return 2*k-1
    else:
        return 2*(k-x)


n, k = map(int, input().split())
print(func(n, k))
