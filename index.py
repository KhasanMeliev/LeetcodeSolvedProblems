def lcp(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return i


def func(words):
    n = len(words)
    lcpArr = []
    res = [0] * n
    for i in range(n - 1):
        lcpArr.append(lcp(words[i], words[i + 1]))
    pref = [0] * (n - 1)
    pref[0] = lcpArr[0]
    for i in range(1, n - 1):
        pref[i] = max(pref[i - 1], lcpArr[i])
    suf = [0] * (n - 1)
    suf[-1] = lcpArr[-1]
    for i in range(n - 3, -1, -1):
        suf[i] = max(suf[i + 1], lcpArr[i])
    
    return pref, suf

    for i in range(n):
        best = 0
        if i-2 >= 0:
            best = max(best, pref[i-2])
        if i+1 < n-1:
            best = max(best, suf[i+1])
        if 0 < i < n-1:
            best = max(best,  lcp(words[i-1], words[i+1]))

        res[i] = best

    return res


print(func(["jump", "run", "run", "jump", "run"]))
