def func(s):
    def helper(s, left, right):
        while left>=0 and right<len(s)-1 and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1
    start = 0
    end = 0
    for i in range(len(s)):
        odd = helper(s,i,i)
        even = helper(s,i,i+1)
        max_length = max(even, odd)
        print(max_length)
        if max_length>end-start:
            start=i-(max_length-1)//2
            end=i+max_length//2
    return s[start:end+1]

print(func('babad'))