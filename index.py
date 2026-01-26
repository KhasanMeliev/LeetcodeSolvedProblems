def func(s):
    n = len(s)
    obj = {}
    cnt = 0
    for i in range(0, len(s)-1, 2):
        color = s[i]
        pos = s[i+1]
        if pos not in obj:
            obj[pos] = []
        obj[pos].append(color)
    for i in obj.values():
        if 'R' in i and 'G' in i and 'B' in i:
            cnt += 1
    return cnt


print(func('B0B6G0R6R0R6G9'))
