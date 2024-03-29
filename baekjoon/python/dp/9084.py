#9084

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M+1)
    dp[0] = 1
    for i in coins:
        for j in range(1, M+1):
            if j - i >= 0:
                dp[j] += dp[j-i]
    print(dp[M])

