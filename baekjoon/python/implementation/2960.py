#2960

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

result = 0
cnt = 0
dp = [0 for _ in range(1001)]

for i in range(2, N+1):
    R = i
    while R <= N:
        if dp[R] == 0:
            dp[R] = 1
            cnt += 1
        if cnt == K:
            result = R
            break
        R = R + i
    if result != 0:
        print(result)
        break
