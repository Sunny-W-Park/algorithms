#2163

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
X = int(input())

arr.sort()
s = 0
e = N-1
count = 0

while s < e:
    _sum = arr[s] + arr[e]
    if _sum == X:
        count += 1
        s += 1
        e -= 1
    if _sum < X:
        s += 1
    if _sum > X:
        e -= 1

print(count)

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
