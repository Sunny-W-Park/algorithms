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

