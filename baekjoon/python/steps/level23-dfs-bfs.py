#1260

import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
visited_dfs = [0] * 1001
visited_bfs = [0] * 1001
g = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(N+1):
    g[i].sort()

result_dfs = []
result_bfs = []

def dfs(g, visited_dfs, V):
    visited_dfs[V-1] = 1
    result_dfs.append(V)
    for i in range(len(g[V])):
        if visited_dfs[g[V][i]-1] == 0:
            dfs(g, visited_dfs, g[V][i])

dfs(g, visited_dfs, V)

def bfs(g, visited_bfs, V):
    visited_bfs[V-1] = 1
    q = deque([V])
    while len(q) != 0:
        p = q.popleft()
        result_bfs.append(p)
        for i in range(len(g[p])):
            if visited_bfs[g[p][i]-1] == 0:
                visited_bfs[g[p][i]-1] = 1
                q.append(g[p][i])

bfs(g, visited_bfs, V)

for i in range(len(result_dfs)):
    print(result_dfs[i], end = ' ')
print()
for i in range(len(result_bfs)):
    print(result_bfs[i], end = ' ')

#2606

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
visited = [0] * (N+1)
g = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(g, visited, start):
    visited[start] = 1
    for i in range(len(g[start])):
        if visited[g[start][i]] == 0:
            dfs(g, visited, g[start][i])

dfs(g, visited, 1)

count = 0
for i in range(1, N+1):
    if i != 1 and visited[i] == 1:
        count += 1

print(count)

#2667

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
g = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    l = str(input())
    for j in range(N):
        g[i][j] = int(l[j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
list_town_count = []

for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            g[i][j] = 999
            count += 1
            town_count = 1
            town = deque([i, j])
            while len(town) != 0:
                tx = town.popleft()
                ty = town.popleft()
                for k in range(4):
                    if 0 <= tx + dx[k] <= (N-1) and 0 <= ty + dy[k] <= (N-1):
                        ntx = tx + dx[k]
                        nty = ty + dy[k]
                        if g[ntx][nty] == 1:
                            g[ntx][nty] = 999
                            town.append(ntx)
                            town.append(nty)
                            town_count += 1 
            list_town_count.append(town_count)

print(count)
for i in range(count):
    print(sorted(list_town_count)[i])

#1012

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    M, N, K = map(int, input().split())
    g = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    for _ in range(K):
        x, y = map(int, input().split())
        g[y][x] = 1

    for i in range(N):
        for j in range(M):
            if g[i][j] == 1:
                count += 1
                g[i][j] = 999
                q = deque([i, j])
                while len(q) != 0:
                    pos_x = q.popleft()
                    pos_y = q.popleft()
                    for k in range(4):
                        nx = pos_x + dx[k]
                        ny = pos_y + dy[k]
                        if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                            if g[nx][ny] == 1:
                                g[nx][ny] = 999
                                q.append(nx)
                                q.append(ny)

    print(count)

#2178 BFS로 풀기

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph_line = []
graph = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph_line.append(str(input()))
for i in range(N):
    for j in range(M):
        graph[i][j] = int(graph_line[i][j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start_x, start_y = 0, 0
q = deque([start_x, start_y])

while len(q) != 0:
    pos_x = q.popleft()
    pos_y = q.popleft()
    for i in range(4):
        nx = pos_x + dx[i]
        ny = pos_y + dy[i]
        if 0 <= nx <= N-1 and 0 <= ny <= M-1:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[pos_x][pos_y] + 1
                q.append(nx)
                q.append(ny)

print(graph[N-1][M-1])

#1697 재풀이

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(count[x])
            break

        for j in (x-1, x+1, x*2):
            if 0 <= j <= 100000 and count[j] == 0:
                count[j] = count[x] + 1
                q.append(j)

N, K = map(int, input().split())
count = [0] * 100001
bfs()

#7576

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

count_zero = 0
pos_tomato = []

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            count_zero += 1
        if maps[i][j] == 1:
            pos_tomato.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count_days = 0

if count_zero == 0:
    print(0)

else:
    queue = deque(pos_tomato)
    while len(queue) != 0:
        for k in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                    if maps[nx][ny] == 0:
                        maps[nx][ny] = 1
                        queue.append((nx, ny))
        count_days += 1

    impos = False
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                impos = True

    if impos == True:
        print(-1)
    else:
        print(count_days-1)


#7562

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dx = [-2, -1, -2, -1, 2, 1, 2, 1]
dy = [-1, -2, 1, 2, -1, -2, 1, 2]

for _ in range(T):
    I = int(input())
    x_start, y_start = map(int, input().split())
    x_end, y_end = map(int, input().split())

    maps = [[0 for _ in range(I)] for _ in range(I)]
    maps[x_start][y_start] = 1

    q = deque()
    q.append((x_start, y_start))
    while len(q) != 0:
        x, y = q.popleft()
        if x == x_end and y == y_end:
            print(maps[x][y]-1)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= I-1 and 0 <= ny <= I-1:
                if maps[nx][ny] == 0:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
