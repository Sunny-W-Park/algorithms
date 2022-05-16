#2636

import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))

t = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            t += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[False for _ in range(N)] for _ in range(M)]
    cnt = 0
    q = deque()
    q.append((0, 0))
    while q:
        px, py = q.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx <= M-1 and 0 <= ny <= N-1:
                if graph[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    graph[nx][ny] = 0
                    cnt += 1
    return cnt

time = 0
counts = []
while t != 0:
    time += 1
    count = bfs()
    t -= count
    counts.append(count)

print(time)
print(counts[-1])

