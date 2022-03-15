#1392

import sys
from collections import deque

input = sys.stdin.readline
N, Q = map(int, input().split())
list_N = deque()
for _ in range(N):
    list_N.append(int(input()))
list_Q = []
for _ in range(Q):
    list_Q.append(int(input()))

list_R = [0 for _ in range(sum(list_N)+1)]
result = 0
page = 0
while len(list_N) != 0:
    k = list_N.popleft()
    result += k
    page += 1
    for i in range(result):
        if list_R[i] == 0 and list_R[i] < result:
            list_R[i] = page

for i in range(Q):
    print(list_R[list_Q[i]])


