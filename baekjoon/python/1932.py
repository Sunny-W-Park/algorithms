#1932

import sys

input = sys.stdin.readline
n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(t[i])):
        if j == 0:
            t[i][j] = t[i-1][j] + t[i][j]
        elif j == len(t[i])-1:
            t[i][j] = t[i-1][j-1] + t[i][j]
        else:
            t[i][j] = max(t[i-1][j]+t[i][j], t[i-1][j-1]+t[i][j])

print(max(t[n-1]))

