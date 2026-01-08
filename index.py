def func(nums1, nums2):
    n,m=len(nums1), len(nums2)
    dp = [[0]*(m) for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            product = nums1[i]*nums2[j]
            dp[i][j]=product

            if i>0 and j>0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+product)
            if i>0:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j>0:
                dp[i][j] = max(dp[i][j], dp[i][j-1])
    
    return dp[i][j]

print(func([2,1,-2,5],[3,0,-6]))