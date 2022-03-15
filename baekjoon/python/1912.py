#1912

import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
dp = [0] * N
dp[0] = num[0]

for i in range(1, N):
    if dp[i-1] > 0:
        dp[i] = dp[i-1] + num[i]
    else:
        dp[i] = num[i]

print(max(dp))


