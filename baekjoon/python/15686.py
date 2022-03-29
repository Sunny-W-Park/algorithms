#15686

import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

houses = []
chicken = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i+1, j+1))
        if graph[i][j] == 2:
            chicken.append((i+1, j+1))

chicken_distance = []
for i in chicken:
    d = 0
    for j in houses:
         d += (abs(i[0]-j[0]) + abs(i[1]-j[1]))
    chicken_distance.append((d, i[0], i[1]))

combs = list(itertools.combinations(chicken_distance, M))
distances = []
for i in combs:
    result = 0
    for j in houses:
        _min = int(10**9)
        for k in range(M):
            _min = min(_min, abs(j[0]-i[k][1])+abs(j[1]-i[k][2]))
        result += _min
    distances.append(result)

print(min(distances))
