def func(matrix):
    m, n = len(matrix), len(matrix[0])
    INF = 10**9
    dp = [[INF]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                dp[i][j] = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1]+1)

    for i in reversed(range(m)):
        for j in reversed(range(n)):
            if matrix[i][j] == 1:
                if i < m-1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j]+1)
                if j < n-1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1]+1)

    return dp


# print(func([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
print(func([[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [
      0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]))

# print(func([[0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [
#       0, 0, 0, 1, 0], [1, 0, 1, 1, 1], [1, 0, 0, 0, 1]]))
