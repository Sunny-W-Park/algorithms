#14502

import sys
import copy
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
g = []
v = []

for i in range(N):
    g.append(list(map(int, input().split())))
    for j in range(M):
        if g[i][j] == 2:
            v.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

def bfs():
    global ans
    c = copy.deepcopy(g)
    q = deque(v)

    while q:
        x, y = q.popleft()
        for r in range(4):
            nx = x + dx[r]
            ny = y + dy[r]
            if 0 <= nx < N and 0 <= ny < M:
                if c[nx][ny] == 0:
                    c[nx][ny] = 2
                    q.append([nx, ny])

    count = 0
    for i in c:
        count += i.count(0)
    ans = max(ans, count)

def wall(x):
    if x == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if g[i][j] == 0:
                g[i][j] = 1
                wall(x+1)
                g[i][j] = 0

wall(0)
print(ans)


