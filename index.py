def func(s):
    n = len(s)
    if n == 0:
        return 0

    ans = 1
    length = 1
    for i in range(n-1):
        if s[i] == s[i+1]:
            length += 1
        else:
            ans = max(ans, length)
            length = 1

    ans = max(ans, length)

    ab = {}
    bc = {}
    ca = {}
    abc = {}

    abc[(0, 0)] = -1
    ab[(0, 0)] = -1
    bc[(0, 0)] = -1
    ca[(0, 0)] = -1

    cnt = [0, 0, 0]

    for i, c in enumerate(s):
        cnt[ord(c)-ord('a')] += 1
        a, b, c = cnt

        key = (b-a, c-a)
        if key in abc:
            ans = max(ans, i-abc[key])
        else:
            abc[key] = i

        key = (a-b, c)
        if key in ab:
            ans = max(ans, i-ab[key])
        else:
            ab[key] = i

        key = (b-c, a)
        if key in bc:
            ans = max(ans, i-bc[key])
        else:
            bc[key] = i

        key = (c-a, b)
        if key in ca:
            ans = max(ans, i-ca[key])
        else:
            ca[key] = i

    return ans


print(func('abbac'))
