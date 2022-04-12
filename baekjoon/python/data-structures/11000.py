#11000

import sys
import heapq
input = sys.stdin.readline
N = int(input())

classes = []
for _ in range(N):
    start, end = map(int, input().split())
    classes.append((start, end))
classes.sort()

room = []
heapq.heappush(room, classes[0][1])

for i in range(1, N):
    if classes[i][0] < room[0]:
        heapq.heappush(room, classes[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, classes[i][1])

print(len(room))

