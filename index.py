def func(prices):
    dp = {}

    def dfs(i, buying):
        if i >= len(prices):
            return 0
        x = (i, buying)
        if x in dp:
            return dp[x]

        cooldown = dfs(i+1, buying)
        if buying:
            buy = dfs(i+1, not buying)-prices[i]
            dp[x] = max(buy, cooldown)
        else:
            sell = dfs(i+2, buying)+prices[i]
            dp[x] = max(sell, cooldown)
        return dp[x]
    return dfs(0, True)


print(func([1, 2, 3, 0, 2]))
