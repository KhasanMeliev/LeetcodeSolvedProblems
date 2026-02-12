def func(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[1]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1

    for i in dp:
        print(i)

    return dp[-1][-1]


print(func('horse', 'ros'))
