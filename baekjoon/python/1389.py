#1389

import sys
N, M = map(int, input().split())
INF = int(10**6)
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = min(graph[a][b], 1)
    graph[b][a] = min(graph[b][a], 1)

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i!=j and k!=i and k!=j:
                graph[i][j] = min(graph[i][k] + graph[j][k], graph[i][j])

dp = [0 for _ in range(N+1)]
for i in range(1, N+1):
    dp[i] = sum(graph[i][1:])

_min = min(dp[1:])
for i in range(1, N+1):
    if dp[i] == _min:
        print(i)
        break


