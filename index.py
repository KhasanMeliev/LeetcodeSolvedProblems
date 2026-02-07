def func(s):
    n = len(s)
    pref = [0]*n
    suff = [0]*n
    if s[0] == 'b':
        pref[0] = 1
    if s[-1] == 'a':
        suff[-1] = 1

    for i in range(1, len(s)):
        pref[i] = pref[i-1]
        if s[i] == 'b':
            pref[i] += 1
    for i in range(len(s)-2, -1, -1):
        suff[i] = suff[i+1]
        if s[i] == 'a':
            suff[i] += 1
    # return suff
    res = float('inf')
    for i in range(len(s)):
        left = pref[i-1] if i > 0 else 0
        res = min(res, (left+suff[i]))

    res = min(res, pref[n-1])

    return res


print(func('aabbbbaabababbbbaaaaaabbababaaabaabaabbbabbbbabbabbababaabaababbbbaaaaabbabbabaaaabbbabaaaabbaaabbbaabbaaaaabaa'))


# def func(s):
#     res = count = 0

#     for i in s:
#         if i == 'b':
#             count += 1
#         elif count:
#             res += 1
#             count -= 1

#     return res


# print(func('aabbbbaabababbbbaaaaaabbababaaabaabaabbbabbbbabbabbababaabaababbbbaaaaabbabbabaaaabbbabaaaabbaaabbbaabbaaaaabaa'))
