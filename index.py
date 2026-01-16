def func(n,board):
    dp = [-1] * (1 << n)
    dp[0] = 0 

    for i in range(1 << n):
        if dp[i] == -1:
            continue

        x = bin(i).count('1')

        for y in range(n):
            if i & (1 << y):
                continue  
            update = i | (1 << y)
            dp[update] = max(dp[update], dp[i] + board[x][y])

    return dp[(1 << n) - 1]  

board = []
n=int(input())
for _ in range(n):
    x=[int(x) for x in input().split()]
    board.append(x)
print(func(n, board))