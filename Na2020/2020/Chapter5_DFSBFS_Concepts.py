from collections import deque

### Factorial Implementation

### Iterative

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    print(result)

factorial_iterative(5)

### Recursive

def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n-1)

factorial_recursive(5)

###DFS

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

visited = [False] * 9
graph = [
            [],
            [2, 3, 8],
            [1, 7],
            [1, 4, 5],
            [3, 5],
            [3, 4],
            [7],
            [2, 6, 8],
            [1, 7]
        ]

dfs(graph, 1, visited)

###BFS

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] == True

visited = [False] * 9
graph = [
            [],
            [2, 3, 8],
            [1, 7],
            [1, 4, 5],
            [3, 5],
            [3, 4],
            [7],
            [2, 6, 8],
            [1, 7]
        ]
bfs(graph, 1, visited)

