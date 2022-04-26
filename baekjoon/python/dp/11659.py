#11659 재풀이

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0]*(N+1)
dp[1] = arr[0]
for i in range(2, N+1):
    dp[i] = dp[i-1] + arr[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])
