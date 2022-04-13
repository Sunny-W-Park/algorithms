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


