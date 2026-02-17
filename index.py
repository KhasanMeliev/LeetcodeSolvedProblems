from collections import Counter


def func(words1, words2):
    maxFreq = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}
    for i in words2:
        for j in i:
            x = i.count(j)
            if maxFreq[j] < x:
                maxFreq[j] = x
    res = []
    for i in words1:
        x = Counter(i)
        if all(x[j] >= maxFreq[j] for j in maxFreq if maxFreq[j] > 0):
            res.append(i)
    return res


print(func(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]))
