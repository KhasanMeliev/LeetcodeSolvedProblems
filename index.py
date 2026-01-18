def func(nums,target):
    nums.sort()
    coverage = 0
    added = 0
    i=0
    while coverage<target:
        if i<len(nums) and nums[i]<=coverage+1:
            coverage+=nums[i]
            print('kichkina', nums[i], coverage)
            i+=1
        else:
            print(coverage,'+ 1 +', coverage, '---', added) 
            coverage+=coverage+1
            added+=1
    

    return added

print(func([1,3],6))
