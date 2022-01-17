from collections import deque

#5-4 미로 탈출

N, M = map(int, input().split())
graph = [[0 for i in range(M)] for j in range(N)]
for i in range(N):
    graph[i] = list(map(int, input()))

dx = [-1, 1, 0, 0] #up, down
dy = [0, 0, -1, 1] #left, right

def isValidPos(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        return True

def bfs(x, y):
    queue = deque()
    queue.append( (x, y) )
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            #4회 반복
            nx = x + dx[i]
            ny = y + dy[i]
            if isValidPos(nx, ny) == True:
                graph[nx][ny] = graph[x][y] + 1
                queue.append( (nx, ny) )

    return graph[N-1][M-1]

print(graph)
print(bfs(0, 0))

