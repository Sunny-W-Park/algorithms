#1789

import sys
input = sys.stdin.readline

S = int(input())
n = 0
_max = 0
while True:
    n += 1
    if (n * (n+1)) // 2 <= S:
        _max = max(_max, n)
    else:
        break

print(_max)

