#DFS

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

#BFS

from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] == True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
