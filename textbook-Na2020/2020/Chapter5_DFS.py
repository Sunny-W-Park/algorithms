from collections import deque

#5-3 음료수 얼려먹기

N, M = map(int, input().split())
graph = [[0 for j in range(M)] for i in range(N)]
for i in range(N):
    graph[i] = list(map(int, input()))

def dfs(i, j):
#재귀함수 구현
    if i < 0 or j < 0 or i >= N or j >= M:
        return False
    if graph[i][j] == 1:
        return False

    graph[i][j] = 1
    dfs(i-1, j)
    dfs(i+1, j)
    dfs(i, j-1)
    dfs(i, j+1)

count = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            #조건문
            dfs(i, j)
            #재귀식은 조건이 주어졌을때 작동
            count += 1

print(count)


