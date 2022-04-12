#11724

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, visited):
    global connected
    visited[start-1] = 1
    for i in graph[start]:
        if visited[i-1] == 0:
            dfs(i, visited)
            connected = True

count = 0
for i in range(1, N+1):
    connected = False
    if visited[i-1] == 0:
        dfs(i, visited)
        if connected == True:
            count += 1
        else:
            count += 1

print(count)
    
