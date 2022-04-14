#1806

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = 0
_sum = 0
_min = int(10**9+1)

for s in range(N):
    while e < N and _sum < S:
        _sum += arr[e]
        e += 1
    if _sum >= S:
        _min = min(_min, e-s)
    _sum -= arr[s]

if _min >= int(10**9):
    print(0)
else:
    print(_min)
