def func(grid):
    res = 0
    if len(grid) == 0 or grid[0][0] == 1:
        return 0
    rows = len(grid)
    columns = len(grid[0])

    dp = [0]*columns
    dp[0] = 1

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1:
                dp[c] = 0
            else:
                if c > 0:
                    dp[c] += dp[c-1]

    return dp

    for i in grid:
        print(i)


print(func([[0, 1], [0, 0]]))
