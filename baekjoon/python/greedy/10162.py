#10162

import sys
input = sys.stdin.readline
T = int(input())
A = 5 * 60
B = 1 * 60
C = 10
dp = [0] * 3

if T % C != 0:
    print(-1)
else:
    while T-A >= 0:
        dp[0] += 1
        T -= A
    while T-B >= 0:
        dp[1] += 1
        T -= B
    while T-C >= 0:
        dp[2] += 1
        T -= C
    for i in dp:
        print(i, end = " ")

