def func(n):
    f = [0]*(n+1)
    f[0] = 1
    f[1] = 0
    for i in range(2, n+1):
        f[i] = 2*f[i-2]
    return f[n]


n = int(input())
print(func(n))

print(func(4))
