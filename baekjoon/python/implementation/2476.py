#2476

import sys
input = sys.stdin.readline

N = int(input())
_max = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    dp = [0] * 7
    dp[a] += 1
    dp[b] += 1
    dp[c] += 1
    count_one = 0
    count_two = 0
    count_three = 0
    for i in dp:
        if i == 1:
            count_one += 1
        if i == 2:
            count_two += 1
        if i == 3:
            count_three += 1
    if count_three == 1:
        x = dp.index(3)
        _max = max(_max, 10000 + x * 1000)
    elif count_two == 1:
        x = dp.index(2)
        _max = max(_max, 1000 + x * 100)
    else:
        x = 0
        for j in range(6, -1, -1):
            if dp[j] != 0:
                x = j
        _max = max(_max, x * 100)

print(_max)

