#2455

import sys
input = sys.stdin.readline

dp = 0
now = 0
for i in range(4):
    o, e = map(int, input().split())
    if i == 0:
        dp = e - o
        now = e - o
    if i > 0:
        dp = max(dp, now - o + e)
        now = now - o + e

print(dp)


