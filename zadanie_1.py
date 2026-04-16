import time

def newton_rec(n, k):
    if k == 0 or k == n:
        return 1
    return newton_rec(n-1, k-1) + newton_rec(n-1, k)


def newton_dp(n, k):
    dp = [[0]*(k+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp[n][k]


def newton_dp_1d(n, k):
    dp = [0]*(k+1)
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(min(i, k), 0, -1):
            dp[j] = dp[j] + dp[j-1]

    return dp[k]

n = 4
k = 2

print("Rekurencyjnie:", newton_rec(n, k))
print("DP 1D:", newton_dp_1d(n, k))
print("DP 2D:", newton_dp(n, k))