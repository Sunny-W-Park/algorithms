#1475

import math

N = int(input())
dp = [0 for _ in range(10)]

for i in str(N):
    if int(i) == 6:
        dp[9] += 1
    if int(i) == 9:
        dp[6] += 1
    dp[int(i)] += 1

_max = max(dp)
result = 0
for i in range(0, 10):
    if dp[i] == _max:
        if i == 6 or i == 9:
            if dp[i] % 2 == 0:
                if dp[i]//2 > result:
                    result = dp[i]//2
            else:
                if dp[i]//2 + 1 > result:
                    result = dp[i]//2 + 1
        else:
            if dp[i] > result:
                result = dp[i]
print(result)
