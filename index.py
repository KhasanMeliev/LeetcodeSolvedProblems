from collections import Counter
def func(nums):
    d = Counter(nums)
    n=max(d, key=d.get)
    return n

print(func([1,2,3,3]))