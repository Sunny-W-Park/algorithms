#18405

import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
g = []
v = []
for i in range(N):
    g.append(list(map(int, input().split())))
    for j in range(N):
        if g[i][j] != 0:
            v.append([g[i][j], i, j])
S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(X, Y, S):
    t = 0
    q = deque(v)

    while q:
        if t == S:
            break
        for _ in range(len(q)):
            virus = q.popleft()
            for k in range(4):
                nx = virus[1] + dx[k]
                ny = virus[2] + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if g[nx][ny] == 0:
                        g[nx][ny] = virus[0]
                        q.append([virus[0], nx, ny])
        t += 1
    return g[X-1][Y-1]

v.sort()
print(bfs(X, Y, S))


