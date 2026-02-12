def func(words, groups):
    res = [words[0]]
    curr = [words[0]]
    prev = groups[0]
    for i in range(1, len(groups)):
        if groups[i] != prev:
            curr.append(words[i])
            prev = groups[i]
        else:
            if len(curr) > len(res):
                res = curr

    return res


print(func(["a", "b", "c", 'd'], [1, 0, 0, 1]))
