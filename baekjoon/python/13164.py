#13164

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stds = list(map(int, input().split()))
stds.sort()
dp = [0] * (N-1)
for i in range(N-1):
    dp[i] = stds[i+1] - stds[i]

dp.sort()
result = 0
for j in range(len(dp)-(K-1)):
    result += dp[j]
print(result)

