def func(nums):
    res = 0
    for i in range(len(nums)):
        l,r=i,i+1
        while r<len(nums)-1:
            if nums[r]-nums[l]==1:
                l+=1
                r+=1
                print(l,r,nums[r], nums[l])
                res+=1
            else:
                break
    return res
            


print(func([2, 3, 4, 3, 4]))
