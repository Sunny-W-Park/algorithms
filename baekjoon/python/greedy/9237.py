#9237

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
_max = 0

arr.sort(reverse = True)
for i in range(N):
    _max = max(_max, i+arr[i]+2)

print(_max)
