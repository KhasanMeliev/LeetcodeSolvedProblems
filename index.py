def func(s, t, maxCost):
    n=len(s)
    cost = []
    for i in range(n):
        cost.append(abs(ord(s[i])-ord(t[i])))

    left= 0
    curr_cost = 0
    res = 0
    for right in range(n):
        curr_cost+=cost[right]
        while curr_cost>maxCost:
            curr_cost-=cost[left]
            left+=1

        res=max(res, right-left+1)

    return res

print(func('abcd', 'bcdf', 3))