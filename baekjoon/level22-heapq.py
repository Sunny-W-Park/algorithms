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

