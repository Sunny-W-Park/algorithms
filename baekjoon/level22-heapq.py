#11279

import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    if x > 0:
        arr.append((-1*x, x))
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            y = heapq.heappop(arr)
            print(y[1])

#1927

import heapq

N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            y = heapq.heappop(arr)
            print(y)
    else:
        heapq.heappush(arr, x)

#11286

import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(q, (abs(x), x))
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            y = heapq.heappop(q)
            print(y[1])


