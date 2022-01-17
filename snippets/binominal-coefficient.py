#Binominal Coefficient (이항 계수)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def binominal_coefficient(N, K):
    return factorial(N) // (factorial(N - K) * factorial(K))

#DP (동적 계획법, 파스칼의 삼각형)

def binominal_coefficient(N, K):
    dp = [[0 for _ in range(K + 1)] for _ in range(N+1)]

    for i in range(N + 1):
        dp[i][0] = 1
    for i in range(K + 1):
        dp[i][i] = 1
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

    return dp[n][k]



