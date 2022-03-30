#14503

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

count = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def turn():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1

while True:
    #print(r, c, d)
    if graph[r][c] == 0:
        graph[r][c] = 2
        count += 1

    #for i in range(N):
    #    for j in range(M):
    #        print(graph[i][j], end = ' ')
    #    print()

    newmove = False
    for i in range(4):
        turn()
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr <= N-1 and 0 <= nc <= M-1:
            if graph[nr][nc] != 1 and graph[nr][nc] != 2:
                r = nr
                c = nc
                newmove = True
                break

    if newmove == False:
        nr = r - dr[d]
        nc = c - dc[d]
        if 0 <= nr <= N-1 and 0 <= nc <= M-1:
            if graph[nr][nc] == 1:
                print(count)
                break
            else:
                r = nr
                c = nc 



