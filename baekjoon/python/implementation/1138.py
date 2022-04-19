#1138

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    count = 0
    for j in range(N):
        if count == arr[i]:
            for k in range(j, N):
                if dp[k] == 0:
                    dp[k] = i+1
                    break
            break
        if dp[j] == 0:
            count += 1

for i in range(N):
    print(dp[i], end = ' ')


